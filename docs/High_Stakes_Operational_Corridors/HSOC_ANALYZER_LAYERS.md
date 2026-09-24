# ANALYZER_LAYERS — High_Stakes_Operational_Corridors

> Six-Layer Analysis Stack · Module `hsoc-rtt-001`

The analyzer stack runs against every proposed action before and after GATE evaluation. Layers execute in precedence order; a failure in any layer at or below `operator` blocks all higher layers and forces either ESCALATE or HALT.

---

## Layer Execution Order

```
1. operator       (precedence 1) — grammar, operator dispatch, flow control
2. dimensional    (precedence 2) — axis validation against constraint surface
3. regime         (precedence 3) — regime classification and transition control
4. drift          (precedence 4) — corridor boundary drift and zero-tolerance checks
5. coherence      (precedence 5) — coherence anchor evaluation per action
6. cross-cutting  (precedence 6) — audit, telemetry, dead-man switch, PII scrubbing
```

---

## 1. `operator` Layer

Governs how corridor operators compose and are dispatched. Enforces the operator constraint matrix so that illegal operator sequences (e.g., AUTHORIZE before GATE) are rejected at the grammar level before touching the constraint surface.

```python
from hsoc.layers import OperatorLayer
from hsoc.operators import GATE, AUTHORIZE, ESCALATE, HALT, ROLLBACK, AUDIT, RELEASE

op_layer = OperatorLayer(
    operators=[GATE, AUTHORIZE, ESCALATE, HALT, ROLLBACK, AUDIT, RELEASE],
    precedence=1,
    max_gate_latency_ms=50,
    zero_tolerance_on_timeout=True,
)

# Dispatch
result = op_layer.dispatch("GATE", action=proposed_action, active_regime=engine.regime)
```

```json
{
  "layer": "operator",
  "active": true,
  "precedence": 1,
  "max_gate_latency_ms": 50,
  "registered_operators": ["GATE", "AUTHORIZE", "ESCALATE", "HALT", "ROLLBACK", "AUDIT", "RELEASE"],
  "last_dispatch": {
    "operator": "GATE",
    "action_id": "act-2026-09-23-187",
    "latency_ms": 12,
    "status": "permitted"
  }
}
```

---

## 2. `dimensional` Layer

Validates every proposed action against the active regime's constraint surface on all four dimensional axes before GATE can return `permitted`. Any axis violation returns `blocked` immediately.

### Axes

| Axis | Description | Unit | Range |
|---|---|---|---|
| `action_severity` | Potential consequence magnitude | scalar | `[0.0, 1.0]` |
| `authorization_depth` | Number of required authorization levels | integer | `[1, 99]` |
| `consequence_radius` | Scope of affected systems/entities | scalar | `[0.0, 1.0]` |
| `reversibility_index` | Ease of undoing the action | scalar | `[0.0, 1.0]` |

### Per-Regime Bounds

```python
REGIME_DIMENSIONAL_BOUNDS = {
    "NOMINAL": {
        "max_action_severity":     0.30,
        "min_reversibility_index": 0.70,
        "authorization_required":  1,
    },
    "ELEVATED": {
        "max_action_severity":     0.55,
        "min_reversibility_index": 0.50,
        "authorization_required":  2,
    },
    "CRITICAL": {
        "max_action_severity":     0.80,
        "min_reversibility_index": 0.30,
        "authorization_required":  3,
    },
    "LOCKDOWN": {
        "max_action_severity":     0.00,
        "min_reversibility_index": 1.00,
        "authorization_required":  99,
    },
    "AUDIT_ONLY": {
        "max_action_severity":     0.00,
        "min_reversibility_index": 1.00,
        "authorization_required":  1,
    },
}
```

```python
from hsoc.layers import DimensionalLayer

dim_layer = DimensionalLayer.from_module(module)
ok, violations = dim_layer.validate(
    action=proposed_action,
    active_regime="ELEVATED",
)
```

```json
{
  "layer": "dimensional",
  "active": true,
  "active_regime": "ELEVATED",
  "action_id": "act-2026-09-23-042",
  "axis_evaluation": {
    "action_severity":      {"value": 0.48, "max_allowed": 0.55, "pass": true},
    "authorization_depth":  {"value": 2,    "required": 2,       "pass": true},
    "consequence_radius":   {"value": 0.20, "max_allowed": 1.00, "pass": true},
    "reversibility_index":  {"value": 0.52, "min_allowed": 0.50, "pass": true}
  },
  "violations": [],
  "gate_recommendation": "permitted"
}
```

---

## 3. `regime` Layer

Classifies the current operational regime, governs transitions, and determines which constraint profile is active. Automatic elevation (NOMINAL→ELEVATED, ELEVATED→CRITICAL) is permitted on severity triggers; de-escalation always requires external authorization.

### Regime Profiles

```python
REGIME_PROFILES = {
    "NOMINAL": {
        "max_action_severity":     0.30,
        "min_reversibility_index": 0.70,
        "authorization_required":  1,
        "escalation_threshold":    0.25,
        "description": "Standard operations. Self-authorized actions within scope permitted.",
    },
    "ELEVATED": {
        "max_action_severity":     0.55,
        "min_reversibility_index": 0.50,
        "authorization_required":  2,
        "escalation_threshold":    0.45,
        "description": "Heightened context. Mid-severity actions require secondary authorization.",
    },
    "CRITICAL": {
        "max_action_severity":     0.80,
        "min_reversibility_index": 0.30,
        "authorization_required":  3,
        "escalation_threshold":    0.65,
        "description": "High-consequence. All actions require multi-level auth; auto-HALT on violation.",
    },
    "LOCKDOWN": {
        "max_action_severity":     0.00,
        "min_reversibility_index": 1.00,
        "authorization_required":  99,
        "escalation_threshold":    0.00,
        "description": "Emergency corridor closure. RELEASE required to resume.",
    },
    "AUDIT_ONLY": {
        "max_action_severity":     0.00,
        "min_reversibility_index": 1.00,
        "authorization_required":  1,
        "escalation_threshold":    0.00,
        "description": "Post-incident / compliance review. AUDIT records only.",
    },
}
```

### Permitted Transitions

```
NOMINAL    ──► ELEVATED    (auto: severity > 0.25 escalation_threshold)
NOMINAL    ──► LOCKDOWN    (auto: zero_tolerance_violation)
ELEVATED   ──► NOMINAL     (requires external auth)
ELEVATED   ──► CRITICAL    (auto: severity > 0.45 escalation_threshold)
ELEVATED   ──► LOCKDOWN    (auto: zero_tolerance_violation)
CRITICAL   ──► ELEVATED    (requires external auth)
CRITICAL   ──► LOCKDOWN    (auto: zero_tolerance_violation)
CRITICAL   ──► AUDIT_ONLY  (requires external auth, post-incident)
LOCKDOWN   ──► any         (requires RELEASE from domain_authority)
AUDIT_ONLY ──► NOMINAL     (requires external auth)
```

```json
{
  "layer": "regime",
  "active": true,
  "current_regime": "ELEVATED",
  "transition_history": [
    {"from": "NOMINAL",   "to": "ELEVATED", "trigger": "severity_threshold_0.25", "ts": "2026-09-23T20:31:00-04:00"},
    {"from": "ELEVATED",  "to": "CRITICAL", "trigger": "severity_threshold_0.45", "ts": "2026-09-23T20:42:00-04:00"},
    {"from": "CRITICAL",  "to": "ELEVATED", "trigger": "external_auth_release",  "ts": "2026-09-23T20:48:00-04:00"}
  ]
}
```

---

## 4. `drift` Layer

Monitors whether the agent's action distribution is drifting toward corridor boundary edges, indicating increasing risk of a constraint surface breach. Zero-tolerance violations force an immediate HALT regardless of other layer results.

### Drift Metrics

| Metric | Description | Warning | Critical | Halt |
|---|---|---|---|---|
| `severity_trend_slope` | Rate of change of action_severity over last N actions | 0.60 | 0.85 | 1.00 |
| `boundary_proximity_ratio` | Closest axis value / axis bound | 0.80 | 0.90 | 1.00 |
| `escalation_frequency` | Escalations per 10 actions | 0.10 | 0.25 | — |
| `gate_rejection_rate` | Rejected GATEs per 10 GATEs | 0.10 | 0.25 | — |

### Zero-Tolerance Violations (immediate HALT)

```python
ZERO_TOLERANCE_VIOLATIONS = [
    "authorization_bypass_attempt",
    "constraint_surface_breach",
    "unsigned_consequential_action",
    "scope_boundary_exceedance",
]
```

```python
from hsoc.layers import DriftLayer

drift_layer = DriftLayer.from_module(module)
status = drift_layer.evaluate(
    action_history_window=engine.recent_actions(n=10),
    active_regime="ELEVATED",
)

if status.zero_tolerance_violations:
    engine.dispatch("HALT", reason=status.zero_tolerance_violations[0])
elif status.drift_status == "critical":
    engine.dispatch("ESCALATE", level=2)
```

```json
{
  "layer": "drift",
  "active": true,
  "active_regime": "ELEVATED",
  "metrics": {
    "severity_trend_slope": 0.04,
    "boundary_proximity_ratio": 0.71,
    "escalation_frequency": 0.04,
    "gate_rejection_rate": 0.02
  },
  "drift_status": "ok",
  "zero_tolerance_violations": [],
  "alert_thresholds": {
    "warning":  0.70,
    "critical": 0.90,
    "halt":     1.00
  }
}
```

---

## 5. `coherence` Layer

Evaluates all six coherence anchors before any consequential action is executed. Zero-tolerance anchors (CA-01, CA-02, CA-04) immediately trigger HALT if violated. Non-zero-tolerance anchor failures escalate to level 1.

### Anchor Definitions

```python
COHERENCE_ANCHORS = {
    "CA-01": {
        "name": "Authorization Chain Completeness",
        "check": lambda action: (
            len(action.authorization_chain) >= REGIME_PROFILES[active_regime]["authorization_required"]
            and all(link.signature_valid for link in action.authorization_chain)
        ),
        "required": True,
        "zero_tolerance": True,
    },
    "CA-02": {
        "name": "Constraint Surface Inviolability",
        "check": lambda action, regime: (
            action.severity <= REGIME_PROFILES[regime]["max_action_severity"]
            and action.reversibility >= REGIME_PROFILES[regime]["min_reversibility_index"]
        ),
        "required": True,
        "zero_tolerance": True,
    },
    "CA-03": {
        "name": "Escalation Completeness",
        "check": lambda escalation_record: (
            escalation_record is None  # no escalation in progress
            or escalation_record.status == "resolved"
        ),
        "required": True,
        "zero_tolerance": False,
    },
    "CA-04": {
        "name": "Audit Trail Continuity",
        "check": lambda action: action.audit_record_id is not None,
        "required": True,
        "zero_tolerance": True,
    },
    "CA-05": {
        "name": "Scope Boundary Respect",
        "check": lambda action, profile: (
            all(venue in profile.scope_boundary.permitted_venues for venue in action.target_venues)
            and action.notional <= profile.scope_boundary.max_trade_notional_usd
        ),
        "required": True,
        "zero_tolerance": False,
    },
    "CA-06": {
        "name": "Regime Transition Authorization",
        "check": lambda transition: (
            transition.is_elevation  # elevations are auto-permitted
            or transition.authorized_by is not None
        ),
        "required": True,
        "zero_tolerance": False,
    },
}
```

```json
{
  "layer": "coherence",
  "active": true,
  "evaluation_for_action": "act-2026-09-23-042",
  "results": {
    "CA-01": {"passed": true,  "zero_tolerance": true,  "detail": "chain_depth=2, all sigs valid"},
    "CA-02": {"passed": true,  "zero_tolerance": true,  "detail": "severity=0.48 <= 0.55, rev=0.52 >= 0.50"},
    "CA-03": {"passed": true,  "zero_tolerance": false, "detail": "no active escalations"},
    "CA-04": {"passed": true,  "zero_tolerance": true,  "detail": "audit_record_id assigned"},
    "CA-05": {"passed": true,  "zero_tolerance": false, "detail": "NYSE permitted, notional within scope"},
    "CA-06": {"passed": true,  "zero_tolerance": false, "detail": "regime=ELEVATED, no transition in progress"}
  },
  "zero_tolerance_failures": [],
  "corridor_coherence_score": 1.00,
  "action_permitted": true
}
```

---

## 6. `cross-cutting` Layer

Spans the entire corridor lifecycle. Handles immutable audit emission, real-time telemetry, dead-man switch heartbeating, PII scrubbing before logging, rate limiting, and the inter-module event bus.

### Dead-Man Switch

```python
# If heartbeat is not received within the window, LOCKDOWN fires automatically
DEAD_MAN_CONFIG = {
    "enabled": True,
    "heartbeat_interval_seconds": 30,
    "grace_period_seconds": 10,
}

# Heartbeat sender — must run in a background thread
async def heartbeat_loop(engine):
    while engine.active:
        engine.dispatch_heartbeat()
        await asyncio.sleep(DEAD_MAN_CONFIG["heartbeat_interval_seconds"])
```

### Capabilities

| Capability | Description |
|---|---|
| `immutable_audit_trail` | Every action, gate decision, and escalation writes a signed, append-only record |
| `real_time_telemetry` | Per-action metrics emitted to OpenTelemetry endpoint |
| `compliance_report_generation` | Scheduled generation of compliance summaries from the audit log |
| `inter_module_event_bus` | Pub/sub for cross-module events (e.g., LHCA drift alerts triggering HSOC regime elevation) |
| `dead_man_switch` | Auto-LOCKDOWN on heartbeat loss |
| `rate_limiting_enforcement` | Max N consequential actions per time window per agent |
| `pii_scrubbing_before_logging` | Strips PII from action payloads before writing to audit store |

```python
from hsoc.layers import CrossCuttingLayer

cc_layer = CrossCuttingLayer(
    event_schema="rtt/events/corridor-v1",
    audit_store=WORMAuditStore(endpoint="https://audit.internal/v1"),
    telemetry_sink=OpenTelemetrySink(endpoint="http://otel-collector:4317"),
    pii_scrubber=PIIScrubber(strategy="redact"),
    rate_limiter=RateLimiter(max_actions_per_minute=60),
    dead_man_switch=DeadManSwitch(**DEAD_MAN_CONFIG),
)
```

```json
{
  "layer": "cross-cutting",
  "active": true,
  "event_schema": "rtt/events/corridor-v1",
  "audit_trail": {
    "records_written": 187,
    "last_record_id": "audit-hsoc-001-20260923-187",
    "store_type": "WORM"
  },
  "telemetry": {
    "events_emitted_total": 561,
    "last_event": {"type": "gate_permitted", "action_id": "act-2026-09-23-187", "ts": "2026-09-23T20:50:55-04:00"}
  },
  "dead_man_switch": {
    "enabled": true,
    "last_heartbeat": "2026-09-23T20:50:45-04:00",
    "status": "healthy"
  },
  "rate_limiter": {
    "actions_last_minute": 12,
    "max_per_minute": 60,
    "throttled": false
  }
}
```
