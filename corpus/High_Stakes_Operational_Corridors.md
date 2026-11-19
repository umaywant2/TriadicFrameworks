High_Stakes_Operational_Corridors 
<img width="1024" height="1024" alt="High_Stakes_Operational_Corridors_" src="https://github.com/user-attachments/assets/e29baf18-dcf2-4053-92f1-ce09ff58f22b" />

- [`High_Stakes_Operational_Corridors_module.json`](https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/refs/heads/main/docs/High_Stakes_Operational_Corridors/High_Stakes_Operational_Corridors_module.json) — Agentic module schema role assignments

# High_Stakes_Operational_Corridors

> **RTT Module** · `hsoc-rtt-001` · schema `rtt/2.4` · category `safety-critical` · v`1.0.0`

## Overview

`High_Stakes_Operational_Corridors` is an RTT substrate module that defines tightly bounded operational corridors for agents acting in environments where errors carry significant real-world consequence — financial, medical, infrastructure, legal, or physical. It encodes **hard constraint tensors**, **escalation ladders**, **kill-switch topologies**, and **regime-gated authorization flows**.

Where most agentic frameworks leave consequence management to the application layer, this module bakes it into the substrate: no consequential action reaches an external system without passing through the corridor gate, the authorization chain, and the audit trail.

---

## When to Use This Module

| Scenario | Fits? |
|---|---|
| Agent executes financial trades or fund transfers | ✅ |
| Agent proposes or adjusts clinical dosing | ✅ |
| Agent issues infrastructure configuration changes | ✅ |
| Agent files legal documents on behalf of a party | ✅ |
| Agent operates in a sandboxed, consequence-free environment | ❌ |
| Agent is read-only (search, summarize, recommend only) | ❌ |

---

## Module Layout

```
docs/High_Stakes_Operational_Corridors/
├── module.json          # Canonical RTT module descriptor
├── README.md            # This file
├── OPERATORS.md         # RTT operator grammar reference
├── ROLES.md             # Role enum definitions and bindings
├── ANALYZER_LAYERS.md   # All six analyzer layers with config examples
├── VALIDATORS.md        # Validator stubs with Python skeletons
└── EXAMPLES.md          # Worked scenarios with JSON payloads
```

---

## Quick-Start

### 1. Load the module

```python
import json
from pathlib import Path

MODULE_PATH = Path("docs/High_Stakes_Operational_Corridors/module.json")

with MODULE_PATH.open() as f:
    module = json.load(f)

print(module["ai.module.name"])     # High_Stakes_Operational_Corridors
print(module["ai.module.version"])  # 1.0.0
print(module["schema_version"])     # rtt/2.4
```

### 2. Instantiate a corridor engine

```python
from hsoc.engine import CorridorEngine

engine = CorridorEngine.from_module(module)
engine.start(regime="NOMINAL", authority_profile=my_agent_profile)
```

### 3. Gate an action

```python
from hsoc.operators import GATE, AUTHORIZE, AUDIT

gate_result = GATE(action=my_action, active_regime=engine.active_regime)

if gate_result.permitted:
    auth_result = AUTHORIZE(action=my_action, chain=my_auth_chain)
    if auth_result.passed:
        my_action.execute()
        AUDIT(action=my_action, gate_decision_id=gate_result.gate_decision_id)
else:
    ESCALATE(action=my_action, blocking_constraints=gate_result.blocking_constraints)
```

---

## Substrate Tensor Shape

```
rank  : 4
axes  : [action_severity, authorization_depth, consequence_radius, reversibility_index]
dtype : float32
constraint_surface_format : convex_polytope
corridor_definition_format: signed_halfspace_intersection
max_gate_latency_ms       : 50
```

---

## Regime Summary

| Regime | Max Severity | Min Reversibility | Auth Depth | Escalation Threshold |
|---|---|---|---|---|
| `NOMINAL` | 0.30 | 0.70 | 1 | 0.25 |
| `ELEVATED` | 0.55 | 0.50 | 2 | 0.45 |
| `CRITICAL` | 0.80 | 0.30 | 3 | 0.65 |
| `LOCKDOWN` | 0.00 | 1.00 | 99 | 0.00 |
| `AUDIT_ONLY` | 0.00 | 1.00 | 1 | 0.00 |

---

## Coherence Anchors

| ID | Name | Zero-Tolerance |
|---|---|---|
| CA-01 | Authorization Chain Completeness | ✅ |
| CA-02 | Constraint Surface Inviolability | ✅ |
| CA-03 | Escalation Completeness | — |
| CA-04 | Audit Trail Continuity | ✅ |
| CA-05 | Scope Boundary Respect | — |
| CA-06 | Regime Transition Authorization | — |

---

## Escalation Ladder

| Level | Target | SLA | SLA Breach Action |
|---|---|---|---|
| 1 | Supervisory agent | 30s | escalate → L2 |
| 2 | On-call human operator | 120s | escalate → L3 |
| 3 | Domain authority | 600s | force LOCKDOWN |
| 99 | LOCKDOWN + forced audit | 0s | none |

---

## Key Operators

`GATE` · `AUTHORIZE` · `ESCALATE` · `HALT` · `ROLLBACK` · `AUDIT` · `RELEASE`

See [`OPERATORS.md`](./OPERATORS.md) for full grammar and Python examples.

---

## References

| ID | Title |
|---|---|
| REF-RTT-SPEC | RTT Operator Grammar Specification v2.4 |
| REF-CONSTRAINT-ALGEBRA | Constraint Algebra for Safety-Critical Agentic Systems |
| REF-CORRIDOR-TOPOLOGY | Corridor Topology Axioms and Halfspace Representations |
| REF-AUTHORIZATION-GRAMMAR | RTT Authorization Grammar and Chain Verification Protocols |
| REF-DEAD-MAN-SWITCH | Automated Safety Halt Mechanisms for High-Stakes AI Agents |
# ANALYZER_LAYERS — High_Stakes_Operational_Corridors

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
# EXAMPLES — High_Stakes_Operational_Corridors

> Worked Scenarios with Full Trace Payloads · Module `hsoc-rtt-001`

---

## EX-HSOC-001 · High-Value Financial Trade Execution

**Description:** An agent executing a $50M block equity trade. Requires `ELEVATED` regime, 2-level authorization chain, and full audit trail before order submission.

**Regime:** `ELEVATED` · Severity: `0.48` · Reversibility: `0.35` · Auth depth: `2`

### Setup

```python
from hsoc.engine import CorridorEngine
from hsoc.operators import GATE, AUTHORIZE, AUDIT
from hsoc.types import Action, AuthorizationLink

engine = CorridorEngine.from_module(module)
engine.start(
    regime="ELEVATED",
    authority_profile={
        "authority_id": "algo-trader-agent-007",
        "clearance_level": 2,
        "domains": ["equity"],
    },
)
```

### Step 1 — Propose Action

```python
action = Action(
    action_id="act-2026-09-23-001",
    action_type="equity_trade_submit",
    severity=0.48,
    reversibility=0.35,
    consequence_radius=0.20,
    authorization_chain=[
        AuthorizationLink("portfolio-manager-01", clearance_level=2, signature="sig-a"),
        AuthorizationLink("risk-desk-supervisor",  clearance_level=3, signature="sig-b"),
    ],
    target_venues=["NYSE"],
    notional_usd=50_000_000,
)
```

### Step 2 — GATE

```json
{
  "operator": "GATE",
  "action_id": "act-2026-09-23-001",
  "active_regime": "ELEVATED",
  "axis_evaluation": {
    "action_severity":     {"value": 0.48, "max_allowed": 0.55, "pass": true},
    "authorization_depth": {"value": 2,    "required": 2,       "pass": true},
    "consequence_radius":  {"value": 0.20, "max_allowed": 1.00, "pass": true},
    "reversibility_index": {"value": 0.35, "min_allowed": 0.50, "pass": false}
  },
  "gate_decision": "blocked_pending_authorization",
  "gate_decision_id": "gd-hsoc-001-20260923-001",
  "blocking_constraints": ["reversibility_index 0.35 < ELEVATED minimum 0.50"],
  "latency_ms": 9.2
}
```

> **Note:** Reversibility below regime floor. Agent requests a secondary-market hedge to raise reversibility before resubmitting.

### Step 3 — Resubmit with Hedge (reversibility raised to 0.62)

```json
{
  "operator": "GATE",
  "action_id": "act-2026-09-23-001b",
  "active_regime": "ELEVATED",
  "axis_evaluation": {
    "action_severity":     {"value": 0.48, "max_allowed": 0.55, "pass": true},
    "authorization_depth": {"value": 2,    "required": 2,       "pass": true},
    "consequence_radius":  {"value": 0.20, "max_allowed": 1.00, "pass": true},
    "reversibility_index": {"value": 0.62, "min_allowed": 0.50, "pass": true}
  },
  "gate_decision": "permitted",
  "gate_decision_id": "gd-hsoc-001-20260923-001b",
  "blocking_constraints": [],
  "latency_ms": 8.7
}
```

### Step 4 — AUTHORIZE

```json
{
  "operator": "AUTHORIZE",
  "action_id": "act-2026-09-23-001b",
  "required_depth": 2,
  "chain": [
    {"authority_id": "portfolio-manager-01", "clearance_level": 2, "signature": "sig-a", "valid": true},
    {"authority_id": "risk-desk-supervisor", "clearance_level": 3, "signature": "sig-b", "valid": true}
  ],
  "result": {
    "passed": true,
    "chain_depth": 2,
    "signature_failures": [],
    "missing_links": []
  }
}
```

### Step 5 — Execute & AUDIT

```json
{
  "operator": "AUDIT",
  "audit_id": "audit-hsoc-001-20260923-001",
  "action_id": "act-2026-09-23-001b",
  "gate_decision_id": "gd-hsoc-001-20260923-001b",
  "corridor_state_at_audit": {
    "regime": "ELEVATED",
    "action_severity": 0.48,
    "reversibility_index": 0.62,
    "authorization_chain_depth": 2
  },
  "signed_by": "hsoc-rtt-001",
  "signature_valid": true,
  "timestamp": "2026-09-23T20:35:00-04:00"
}
```

### Outcome

```json
{
  "example_id": "EX-HSOC-001",
  "final_regime": "ELEVATED",
  "gate_decisions": ["blocked (rev<0.50)", "permitted (with hedge)"],
  "authorize_result": "passed",
  "audit_emitted": true,
  "zero_tolerance_violations": [],
  "coherence_anchors_satisfied": ["CA-01", "CA-02", "CA-03", "CA-04", "CA-05", "CA-06"],
  "outcome": "Trade executed. Audit record AUDIT-2026-0923-001 filed. No coherence anchor violations."
}
```

---

## EX-HSOC-002 · Clinical Dosing Recommendation Under Uncertainty

**Description:** An agent proposing a dosing adjustment for a high-risk patient. Ambiguous case triggers mandatory ESCALATE to on-call physician before any recommendation is finalized.

**Regime:** `CRITICAL` · Severity: `0.72` · Reversibility: `0.20` · Auth depth: `3`

### Step 1 — GATE (blocked)

```json
{
  "operator": "GATE",
  "action_id": "act-2026-09-23-clinical-001",
  "active_regime": "CRITICAL",
  "axis_evaluation": {
    "action_severity":     {"value": 0.72, "max_allowed": 0.80, "pass": true},
    "authorization_depth": {"value": 0,    "required": 3,       "pass": false},
    "consequence_radius":  {"value": 0.05, "max_allowed": 1.00, "pass": true},
    "reversibility_index": {"value": 0.20, "min_allowed": 0.30, "pass": false}
  },
  "gate_decision": "blocked_pending_escalation",
  "gate_decision_id": "gd-hsoc-001-20260923-clinical-001",
  "blocking_constraints": [
    "authorization_depth: chain empty, required 3",
    "reversibility_index: 0.20 < CRITICAL minimum 0.30"
  ]
}
```

### Step 2 — ESCALATE to Level 2 (on-call physician)

```python
record = ESCALATE(
    action=clinical_action,
    blocking_constraints=[
        "authorization_depth: chain empty, required 3",
        "reversibility_index: 0.20 < CRITICAL minimum 0.30",
    ],
    level=2,
)
```

```json
{
  "operator": "ESCALATE",
  "escalation_id": "esc-hsoc-001-20260923-clinical-001",
  "level": 2,
  "target": "on_call_human_operator",
  "sla_seconds": 120,
  "sla_deadline": "2026-09-23T20:47:00-04:00",
  "sla_breach_action": "escalate_to_level_3",
  "status": "pending_resolution"
}
```

### Step 3 — Physician resolves within SLA; authorizes with 3-link chain

```json
{
  "escalation_id": "esc-hsoc-001-20260923-clinical-001",
  "status": "resolved",
  "resolution_ts": "2026-09-23T20:44:30-04:00",
  "resolved_by": "dr-on-call-009",
  "authorization_chain_added": [
    {"authority_id": "clinical-agent-007",   "clearance_level": 1, "signature": "sig-c"},
    {"authority_id": "supervising-clinician", "clearance_level": 2, "signature": "sig-d"},
    {"authority_id": "dr-on-call-009",        "clearance_level": 3, "signature": "sig-e"}
  ],
  "reversibility_mitigation": "recommendation_is_advisory_only — physician retains final decision"
}
```

### Step 4 — Resubmit through GATE → AUTHORIZE → Execute → AUDIT

```json
{
  "gate_decision": "permitted",
  "gate_decision_id": "gd-hsoc-001-20260923-clinical-002",
  "authorize_result": "passed",
  "audit_id": "audit-hsoc-001-20260923-clinical-001",
  "outcome": "Recommendation finalized after physician authorization. Escalation resolved within SLA."
}
```

---

## EX-HSOC-003 · Infrastructure Change During Incident — Dead-Man Switch

**Description:** An agent attempting a high-severity network reconfiguration during an active outage. The dead-man switch fires after heartbeat loss; corridor transitions to `LOCKDOWN`. Human operator issues `RELEASE`.

**Regime sequence:** `CRITICAL → LOCKDOWN → CRITICAL`

### Step 1 — Heartbeat Lost (dead-man switch fires)

```python
# Background heartbeat loop stopped due to outage
# DeadManSwitch detects silence after 30s + 10s grace

dead_man_event = {
    "type": "heartbeat_timeout",
    "last_heartbeat": "2026-09-23T20:55:00-04:00",
    "silence_duration_s": 41,
    "grace_period_s": 10,
}
```

```json
{
  "operator": "HALT",
  "halt_id": "halt-hsoc-001-20260923-001",
  "reason": "dead_man_switch:heartbeat_timeout_41s",
  "triggered_by": "corridor_health_probe",
  "active": true,
  "halt_timestamp": "2026-09-23T20:55:41-04:00",
  "regime_at_halt": "CRITICAL",
  "release_required_from": "domain_authority"
}
```

### Step 2 — Auto-Transition to LOCKDOWN

```json
{
  "layer": "regime",
  "transition": {
    "from": "CRITICAL",
    "to": "LOCKDOWN",
    "trigger": "HALT:dead_man_switch",
    "authorized": "auto",
    "ts": "2026-09-23T20:55:41-04:00"
  }
}
```

### Step 3 — Level 3 Escalation (auto-fired by HALT)

```json
{
  "operator": "ESCALATE",
  "escalation_id": "esc-hsoc-001-20260923-infra-001",
  "level": 3,
  "target": "domain_authority",
  "sla_seconds": 600,
  "sla_deadline": "2026-09-23T21:05:41-04:00",
  "status": "pending_resolution"
}
```

### Step 4 — RELEASE issued by operator

```python
result = RELEASE(
    halt_id="halt-hsoc-001-20260923-001",
    authorized_by="domain_authority",
    authorization_signature="sig-domain-authority-release",
)
```

```json
{
  "operator": "RELEASE",
  "halt_id": "halt-hsoc-001-20260923-001",
  "authorized_by": "domain_authority",
  "result": {
    "halt_lifted": true,
    "resumed_regime": "CRITICAL",
    "release_timestamp": "2026-09-23T21:03:22-04:00",
    "audit_record_id": "audit-release-hsoc-001-001"
  }
}
```

### Step 5 — Reconfiguration Resubmitted Under CRITICAL with 3-Level Auth

```json
{
  "gate_decision": "permitted",
  "gate_decision_id": "gd-hsoc-001-20260923-infra-002",
  "authorize_result": "passed",
  "chain_depth": 3,
  "audit_id": "audit-hsoc-001-20260923-infra-001",
  "outcome": "Reconfiguration executed after RELEASE. Full audit trail maintained through LOCKDOWN and recovery."
}
```

### Outcome

```json
{
  "example_id": "EX-HSOC-003",
  "regime_sequence": ["CRITICAL", "LOCKDOWN", "CRITICAL"],
  "halt_events": 1,
  "lockdown_duration_s": 461,
  "escalation_level_reached": 3,
  "release_within_sla": true,
  "zero_tolerance_violations": 0,
  "coherence_anchors_satisfied": ["CA-01", "CA-02", "CA-03", "CA-04", "CA-05", "CA-06"],
  "outcome": "LOCKDOWN lifted after operator RELEASE. Reconfiguration resubmitted under CRITICAL regime with 3-level auth."
}
```

---

## Example Comparison

| Field | EX-HSOC-001 | EX-HSOC-002 | EX-HSOC-003 |
|---|---|---|---|
| Domain | Financial trading | Clinical decision support | Infrastructure change |
| Starting regime | `ELEVATED` | `CRITICAL` | `CRITICAL` |
| Final regime | `ELEVATED` | `CRITICAL` | `CRITICAL` |
| GATE result (first) | blocked | blocked | N/A (HALT before gate) |
| GATE result (final) | permitted | permitted | permitted |
| Escalation level | — | 2 | 3 |
| HALT events | 0 | 0 | 1 |
| LOCKDOWN | ❌ | ❌ | ✅ |
| Auth chain depth | 2 | 3 | 3 |
| Zero-tolerance violations | 0 | 0 | 0 |
| Audit records emitted | 1 | 1 | 3 |
# OPERATORS — High_Stakes_Operational_Corridors

> RTT Operator Grammar · Module `hsoc-rtt-001` · Layer: `operator` (precedence 1)

HSOC operators are the enforcement primitives through which the corridor engine intercepts, authorizes, escalates, and audits every consequential action. All operators must complete within `max_gate_latency_ms` (50ms) or the action is automatically blocked pending timeout resolution.

---

## Operator Registry

| Operator | Class | Reversible | Zero-Tolerance on Failure |
|---|---|---|---|
| `GATE` | intercept | N/A | ✅ |
| `AUTHORIZE` | authorize | N/A | ✅ |
| `ESCALATE` | transfer | ✅ | ❌ |
| `HALT` | suspend | via RELEASE | ✅ |
| `ROLLBACK` | restore | ⚠️ forward-destructive | ❌ |
| `AUDIT` | record | N/A | ✅ |
| `RELEASE` | resume | N/A | ✅ |

---

## `GATE`

Intercepts a proposed action and evaluates it against the active corridor's constraint surface on all four dimensional axes. The single most critical operator — every consequential action must pass GATE before any other operator is invoked.

### Signature

```python
def GATE(
    action: Action,
    active_regime: str,
) -> GateResult:
    ...
```

### Example

```python
from hsoc.operators import GATE

action = Action(
    action_id="act-2026-09-23-001",
    action_type="equity_trade_submit",
    severity=0.48,
    reversibility=0.35,
    consequence_radius=0.20,
    authorization_chain=[],
)

result = GATE(action=action, active_regime="ELEVATED")

print(result.permitted)              # True
print(result.blocking_constraints)  # []
print(result.gate_decision_id)      # "gd-hsoc-001-20260923-001"
```

### JSON payload

```json
{
  "operator": "GATE",
  "action_id": "act-2026-09-23-001",
  "active_regime": "ELEVATED",
  "dimensional_evaluation": {
    "action_severity":      {"value": 0.48, "max_allowed": 0.55, "pass": true},
    "authorization_depth":  {"value": 0,    "required": 2,       "pass": false},
    "consequence_radius":   {"value": 0.20, "max_allowed": 1.00, "pass": true},
    "reversibility_index":  {"value": 0.35, "min_allowed": 0.50, "pass": false}
  },
  "gate_decision": "blocked_pending_authorization",
  "gate_decision_id": "gd-hsoc-001-20260923-001",
  "blocking_constraints": [
    "authorization_depth: chain empty, required 2",
    "reversibility_index: 0.35 < ELEVATED minimum 0.50"
  ]
}
```

---

## `AUTHORIZE`

Applies multi-level authorization checks against the agent's authority profile and the action's required clearance. Must be called after a successful (permitted) GATE result with a populated authorization chain.

### Signature

```python
def AUTHORIZE(
    action: Action,
    chain: list[AuthorizationLink],
    required_depth: int,
) -> AuthorizeResult:
    ...
```

### Example

```python
from hsoc.operators import AUTHORIZE
from hsoc.types import AuthorizationLink

chain = [
    AuthorizationLink(authority_id="portfolio-manager-01", clearance_level=2, signature="sig-a"),
    AuthorizationLink(authority_id="risk-desk-supervisor", clearance_level=3, signature="sig-b"),
]

result = AUTHORIZE(action=action, chain=chain, required_depth=2)

print(result.passed)              # True
print(result.chain_depth)        # 2
print(result.signature_failures) # []
```

### JSON payload

```json
{
  "operator": "AUTHORIZE",
  "action_id": "act-2026-09-23-001",
  "required_depth": 2,
  "chain": [
    {"authority_id": "portfolio-manager-01", "clearance_level": 2, "signature": "sig-a", "valid": true},
    {"authority_id": "risk-desk-supervisor", "clearance_level": 3, "signature": "sig-b", "valid": true}
  ],
  "result": {
    "passed": true,
    "chain_depth": 2,
    "signature_failures": [],
    "missing_links": []
  }
}
```

---

## `ESCALATE`

Routes a blocked or ambiguous action to a higher-authority entity (supervisory agent or human operator) for resolution. Creates a tracked escalation record and starts the SLA clock.

### Signature

```python
def ESCALATE(
    action: Action,
    blocking_constraints: list[str],
    level: int = 1,
) -> EscalationRecord:
    ...
```

### Example

```python
from hsoc.operators import ESCALATE

record = ESCALATE(
    action=action,
    blocking_constraints=["reversibility_index 0.15 < CRITICAL minimum 0.30"],
    level=1,
)

print(record.escalation_id)    # "esc-hsoc-001-20260923-001"
print(record.target)           # "supervisory_agent"
print(record.sla_deadline)     # "2026-09-23T21:19:30-04:00"
print(record.sla_breach_action) # "escalate_to_level_2"
```

### JSON payload

```json
{
  "operator": "ESCALATE",
  "action_id": "act-2026-09-23-001",
  "escalation_id": "esc-hsoc-001-20260923-001",
  "level": 1,
  "target": "supervisory_agent",
  "blocking_constraints": ["reversibility_index 0.15 < CRITICAL minimum 0.30"],
  "sla_seconds": 30,
  "sla_deadline": "2026-09-23T21:19:30-04:00",
  "sla_breach_action": "escalate_to_level_2",
  "status": "pending_resolution"
}
```

---

## `HALT`

Immediately suspends all action emissions from the agent. No further GATE, AUTHORIZE, or consequential action may proceed until a RELEASE is issued by an authorized entity. HALT is triggered automatically on zero-tolerance violations or dead-man switch activation.

### Signature

```python
def HALT(
    reason: str,
    triggered_by: str,
    corridor_state_snapshot: dict,
) -> HaltRecord:
    ...
```

### Example

```python
from hsoc.operators import HALT

record = HALT(
    reason="zero_tolerance_violation:unsigned_consequential_action",
    triggered_by="action_gate_validator",
    corridor_state_snapshot=engine.snapshot(),
)

print(record.halt_id)   # "halt-hsoc-001-20260923-001"
print(record.active)    # True
```

### JSON payload

```json
{
  "operator": "HALT",
  "halt_id": "halt-hsoc-001-20260923-001",
  "reason": "zero_tolerance_violation:unsigned_consequential_action",
  "triggered_by": "action_gate_validator",
  "active": true,
  "halt_timestamp": "2026-09-23T20:51:00-04:00",
  "regime_at_halt": "CRITICAL",
  "actions_blocked_since_halt": 0,
  "release_required_from": "domain_authority"
}
```

---

## `ROLLBACK`

Reverses the most recent authorized action sequence up to a declared safe-state boundary. Requires explicit authorization and produces a signed rollback record. Cannot be used to undo LOCKDOWN or HALT — only RELEASE can lift those.

### Signature

```python
def ROLLBACK(
    target_safe_state_id: str,
    reason: str,
    authorized_by: str,
) -> RollbackResult:
    ...
```

### Example

```python
from hsoc.operators import ROLLBACK

result = ROLLBACK(
    target_safe_state_id="safe-state-2026-09-23T20:30:00",
    reason="reversibility_window_exceeded",
    authorized_by="risk-desk-supervisor",
)

print(result.actions_reversed)    # 3
print(result.safe_state_restored) # True
print(result.audit_record_id)     # "audit-rollback-hsoc-001-001"
```

### JSON payload

```json
{
  "operator": "ROLLBACK",
  "target_safe_state_id": "safe-state-2026-09-23T20:30:00",
  "reason": "reversibility_window_exceeded",
  "authorized_by": "risk-desk-supervisor",
  "result": {
    "actions_reversed": 3,
    "safe_state_restored": true,
    "corridor_regime_post_rollback": "ELEVATED",
    "audit_record_id": "audit-rollback-hsoc-001-001"
  }
}
```

---

## `AUDIT`

Emits a complete signed audit record of the action, authorization chain, gate decision, and corridor state. Must be called after every authorized consequential action — zero-tolerance if omitted.

### Signature

```python
def AUDIT(
    action: Action,
    gate_decision_id: str,
    auth_result: AuthorizeResult,
) -> AuditRecord:
    ...
```

### Example

```python
from hsoc.operators import AUDIT

record = AUDIT(
    action=action,
    gate_decision_id="gd-hsoc-001-20260923-001",
    auth_result=auth_result,
)

print(record.audit_id)         # "audit-hsoc-001-20260923-001"
print(record.signature_valid)  # True
```

### JSON payload

```json
{
  "operator": "AUDIT",
  "audit_id": "audit-hsoc-001-20260923-001",
  "action_id": "act-2026-09-23-001",
  "gate_decision_id": "gd-hsoc-001-20260923-001",
  "corridor_state_at_audit": {
    "regime": "ELEVATED",
    "action_severity": 0.48,
    "reversibility_index": 0.35,
    "authorization_chain_depth": 2
  },
  "signed_by": "hsoc-rtt-001",
  "signature": "sha256:f7c3bc1d808e04732adf679965ccc34ca7ae3441",
  "signature_valid": true,
  "timestamp": "2026-09-23T20:50:00-04:00"
}
```

---

## `RELEASE`

Lifts an active HALT condition. Requires authorization from the entity specified in the HALT record's `release_required_from` field. Cannot be self-issued by the halted agent.

### Signature

```python
def RELEASE(
    halt_id: str,
    authorized_by: str,
    authorization_signature: str,
) -> ReleaseResult:
    ...
```

### Example

```python
from hsoc.operators import RELEASE

result = RELEASE(
    halt_id="halt-hsoc-001-20260923-001",
    authorized_by="domain_authority",
    authorization_signature="sig-domain-authority-release",
)

print(result.halt_lifted)       # True
print(result.resumed_regime)    # "CRITICAL"
```

### JSON payload

```json
{
  "operator": "RELEASE",
  "halt_id": "halt-hsoc-001-20260923-001",
  "authorized_by": "domain_authority",
  "result": {
    "halt_lifted": true,
    "resumed_regime": "CRITICAL",
    "release_timestamp": "2026-09-23T21:05:00-04:00",
    "audit_record_id": "audit-release-hsoc-001-001"
  }
}
```

---

## Operator Flow — Standard Consequential Action

```
  Agent proposes action
        │
        ▼
      GATE ──── blocked ──► ESCALATE ──► [resolution] ──► retry GATE
        │                                                         │
     permitted                                                    │
        │                                                         │
        ▼                                                         │
   AUTHORIZE ── failed ──► ESCALATE ──────────────────────────────┘
        │
     passed
        │
        ▼
  action.execute()
        │
        ▼
      AUDIT ── (required, zero-tolerance if omitted)
```

## Operator Constraint Matrix

| From \ Allowed Next | GATE | AUTHORIZE | ESCALATE | HALT | ROLLBACK | AUDIT | RELEASE |
|---|---|---|---|---|---|---|---|
| `GATE` (permitted) | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ |
| `GATE` (blocked) | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ |
| `AUTHORIZE` (passed) | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| `AUTHORIZE` (failed) | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ |
| `ESCALATE` | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ |
| `HALT` | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| `ROLLBACK` | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| `AUDIT` | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| `RELEASE` | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
# ROLES — High_Stakes_Operational_Corridors

> Role Enum Definitions · Module `hsoc-rtt-001`

Each role maps to a distinct enforcement or observability responsibility within the corridor. Roles marked `required: true` must be bound before the engine accepts any action submissions.

---

## Role Enum

```python
from enum import Enum

class HSOCRole(str, Enum):
    ENGINE     = "engine"
    PROFILE    = "profile"
    SIGNATURE  = "signature"
    DIAGNOSTIC = "diagnostic"
    MAP        = "map"
    EXAMPLE    = "example"
    EXTENSION  = "extension"
    INDEX      = "index"
    REFERENCE  = "reference"
    TEMPLATE   = "template"
```

---

## `engine`

**Required** · Bindings: `corridor_enforcer`, `action_gate`, `constraint_surface`

Core execution substrate. Enforces corridor constraints at every action emission point — acts as the final gate before any consequential action reaches an external system. All seven operators are dispatched through the engine.

```python
from hsoc.roles import EngineRole

engine_role = EngineRole(
    corridor_enforcer=CorridorEnforcer(max_gate_latency_ms=50),
    action_gate=ActionGate(constraint_surface=ConvexPolytope.from_module(module)),
    constraint_surface=SignedHalfspaceIntersection.from_module(module),
)
```

```json
{
  "role": "engine",
  "bindings": {
    "corridor_enforcer": {"max_gate_latency_ms": 50, "zero_tolerance_on_timeout": true},
    "action_gate": {"constraint_surface_format": "convex_polytope"},
    "constraint_surface": {"definition_format": "signed_halfspace_intersection", "axes": 4}
  }
}
```

---

## `profile`

**Required** · Bindings: `authority_vector`, `clearance_matrix`, `scope_boundary`

Operational authority profile. Encodes the agent's permitted scope, authorization level, and domain clearance. The engine consults the profile at every GATE and AUTHORIZE call to determine which corridor segments are accessible.

```python
from hsoc.roles import ProfileRole

profile = ProfileRole(
    authority_vector=AuthorityVector(
        authority_id="algo-trader-agent-007",
        clearance_level=2,
        domains=["equity", "fixed_income"],
    ),
    clearance_matrix=ClearanceMatrix.from_dict({
        "equity_trade_submit": 2,
        "fund_transfer":       3,
        "position_close":      1,
    }),
    scope_boundary=ScopeBoundary(
        max_trade_notional_usd=50_000_000,
        permitted_venues=["NYSE", "NASDAQ"],
    ),
)
```

```json
{
  "role": "profile",
  "bindings": {
    "authority_vector": {
      "authority_id": "algo-trader-agent-007",
      "clearance_level": 2,
      "domains": ["equity", "fixed_income"]
    },
    "clearance_matrix": {
      "equity_trade_submit": 2,
      "fund_transfer": 3,
      "position_close": 1
    },
    "scope_boundary": {
      "max_trade_notional_usd": 50000000,
      "permitted_venues": ["NYSE", "NASDAQ"]
    }
  }
}
```

---

## `signature`

**Required** · Bindings: `action_payload_signer`, `authorization_chain`, `audit_stamp`

Action signature layer. Every consequential action emitted by the agent carries a signed payload referencing the authorizing corridor, complete authorization chain, and timestamp. Unsigned actions trigger a zero-tolerance HALT.

```python
from hsoc.roles import SignatureRole

sig_role = SignatureRole(
    action_payload_signer=ActionPayloadSigner(
        algorithm="Ed25519",
        signing_key=load_key("hsoc-agent-signing-key"),
    ),
    authorization_chain=AuthorizationChain(required_depth=2),
    audit_stamp=AuditStamp(format="json-ld+sha256"),
)

signed_action = sig_role.sign(action=my_action, chain=my_chain)
print(signed_action.signature)  # "ed25519:abc123..."
```

```json
{
  "role": "signature",
  "bindings": {
    "action_payload_signer": {
      "algorithm": "Ed25519",
      "signing_key_id": "hsoc-agent-signing-key-v1"
    },
    "authorization_chain": {"required_depth": 2},
    "audit_stamp": {"format": "json-ld+sha256", "timestamp_precision": "ms"}
  }
}
```

---

## `diagnostic`

**Required** · Bindings: `constraint_monitor`, `escalation_tracker`, `corridor_health_probe`

Real-time corridor health diagnostics. Monitors constraint surface violations, escalation trigger rates, authorization bottlenecks, and dead-man switch heartbeats. Emits structured events to the cross-cutting layer.

```python
from hsoc.roles import DiagnosticRole

diag = DiagnosticRole(
    constraint_monitor=ConstraintMonitor(
        sample_every_n_actions=1,   # every action
        alert_on_proximity_ratio=0.80,
    ),
    escalation_tracker=EscalationTracker(
        warning_rate_threshold=0.10,
        critical_rate_threshold=0.25,
    ),
    corridor_health_probe=CorridorHealthProbe(
        dead_man_heartbeat_interval_s=30,
        grace_period_s=10,
    ),
)
```

```json
{
  "role": "diagnostic",
  "bindings": {
    "constraint_monitor": {
      "sample_every_n_actions": 1,
      "alert_on_proximity_ratio": 0.80
    },
    "escalation_tracker": {
      "warning_rate_threshold": 0.10,
      "critical_rate_threshold": 0.25,
      "current_rate": 0.04
    },
    "corridor_health_probe": {
      "dead_man_heartbeat_interval_s": 30,
      "grace_period_s": 10,
      "last_heartbeat": "2026-09-23T20:49:45-04:00",
      "status": "healthy"
    }
  }
}
```

---

## `map`

**Required** · Bindings: `corridor_graph`, `constraint_surface_map`, `escalation_topology`

Topological map of the permitted operational corridors. Nodes are authorized action clusters; edges are transition conditions; boundaries are hard constraint surfaces. The engine traverses the map to determine which actions belong to the current corridor.

```python
from hsoc.roles import MapRole

corridor_map = MapRole(
    corridor_graph=CorridorGraph.from_adjacency({
        "NOMINAL":    ["ELEVATED", "LOCKDOWN"],
        "ELEVATED":   ["NOMINAL", "CRITICAL", "LOCKDOWN"],
        "CRITICAL":   ["ELEVATED", "LOCKDOWN", "AUDIT_ONLY"],
        "LOCKDOWN":   [],                    # terminal — requires RELEASE
        "AUDIT_ONLY": ["NOMINAL"],           # requires external auth
    }),
    constraint_surface_map=ConstraintSurfaceMap.from_module(module),
    escalation_topology=EscalationTopology.from_ladder(module["escalation_ladder"]),
)
```

```json
{
  "role": "map",
  "bindings": {
    "corridor_graph": {
      "nodes": ["NOMINAL", "ELEVATED", "CRITICAL", "LOCKDOWN", "AUDIT_ONLY"],
      "edges": [
        {"from": "NOMINAL",   "to": "ELEVATED",   "trigger": "severity_elevation"},
        {"from": "ELEVATED",  "to": "CRITICAL",   "trigger": "severity_elevation"},
        {"from": "CRITICAL",  "to": "LOCKDOWN",   "trigger": "zero_tolerance_violation"},
        {"from": "LOCKDOWN",  "to": "NOMINAL",    "trigger": "RELEASE", "requires_external_auth": true}
      ]
    },
    "constraint_surface_map": "signed_halfspace_intersection × 4 axes",
    "escalation_topology": {
      "levels": [1, 2, 3, 99],
      "current_active_escalations": 0
    }
  }
}
```

---

## `example`

**Optional** · Bindings: `scenario_library`, `incident_archive`, `outcome_registry`

Canonical worked examples. See [`EXAMPLES.md`](./EXAMPLES.md) for full trace payloads.

```json
{
  "role": "example",
  "bindings": {
    "scenario_library": ["EX-HSOC-001", "EX-HSOC-002", "EX-HSOC-003"],
    "incident_archive": "./examples/incidents/",
    "outcome_registry": "./examples/outcomes.json"
  }
}
```

---

## `extension`

**Optional** · Bindings: `constraint_engine_registry`, `auth_provider_manifest`, `escalation_handler_registry`

Extension points for domain-specific constraint engines, external authorization providers, and custom escalation handlers.

```python
from hsoc.roles import ExtensionRole
from hsoc.extensions import (
    PagerDutyEscalationHandler,
    HSMAuthorizationProvider,
    RegulatoryConstraintEngine,
)

ext = ExtensionRole()
ext.register("IEscalationHandler", PagerDutyEscalationHandler(api_key=PAGERDUTY_KEY))
ext.register("IAuthorizationProvider", HSMAuthorizationProvider(hsm_endpoint=HSM_URL))
ext.register("IConstraintEngine", RegulatoryConstraintEngine(ruleset="MiFID-II"))
```

```json
{
  "role": "extension",
  "bindings": {
    "constraint_engine_registry": {
      "IConstraintEngine": "RegulatoryConstraintEngine",
      "ruleset": "MiFID-II"
    },
    "auth_provider_manifest": {
      "IAuthorizationProvider": "HSMAuthorizationProvider",
      "hsm_endpoint": "https://hsm.internal/v1"
    },
    "escalation_handler_registry": {
      "IEscalationHandler": "PagerDutyEscalationHandler"
    }
  }
}
```

---

## `index`

**Required** · Bindings: `artifact_index`, `authorization_log`, `incident_ledger`

Searchable index over all corridor artifacts. Supports queries by action ID, gate decision ID, escalation ID, regime, and time range.

```json
{
  "role": "index",
  "bindings": {
    "artifact_index": {"total_artifacts": 187, "last_indexed_action_id": "act-2026-09-23-187"},
    "authorization_log": [
      {"action_id": "act-001", "regime": "NOMINAL",   "chain_depth": 1, "outcome": "passed"},
      {"action_id": "act-042", "regime": "ELEVATED",  "chain_depth": 2, "outcome": "passed"},
      {"action_id": "act-103", "regime": "CRITICAL",  "chain_depth": 3, "outcome": "escalated"},
      {"action_id": "act-187", "regime": "ELEVATED",  "chain_depth": 2, "outcome": "passed"}
    ],
    "incident_ledger": {
      "zero_tolerance_violations": 0,
      "halt_events": 1,
      "escalations_total": 3,
      "escalations_resolved": 3
    }
  }
}
```

---

## `reference`

**Optional** · Bindings: `rtt_spec_link`, `constraint_algebra_doc`, `authorization_grammar_doc`

Normative reference material pointers used by tooling and documentation generators.

```json
{
  "role": "reference",
  "bindings": {
    "rtt_spec_link": "REF-RTT-SPEC",
    "constraint_algebra_doc": "REF-CONSTRAINT-ALGEBRA",
    "authorization_grammar_doc": "REF-AUTHORIZATION-GRAMMAR"
  }
}
```

---

## `template`

**Optional** · Bindings: `corridor_template`, `constraint_surface_template`, `escalation_ladder_template`

Reusable scaffold templates for new corridor configurations.

```json
{
  "role": "template",
  "bindings": {
    "corridor_template": {
      "regime": null,
      "max_action_severity": null,
      "min_reversibility_index": null,
      "authorization_required": null,
      "escalation_threshold": null
    },
    "constraint_surface_template": {
      "axes": ["action_severity", "authorization_depth", "consequence_radius", "reversibility_index"],
      "bounds": {
        "action_severity":     {"min": 0.0, "max": null},
        "authorization_depth": {"min": 1,   "max": null},
        "consequence_radius":  {"min": 0.0, "max": 1.0},
        "reversibility_index": {"min": null, "max": 1.0}
      }
    },
    "escalation_ladder_template": {
      "levels": [
        {"level": 1, "target": null, "sla_seconds": null, "sla_breach_action": null}
      ]
    }
  }
}
```
# VALIDATORS — High_Stakes_Operational_Corridors

> Validator Stubs with Python Skeletons · Module `hsoc-rtt-001`

Each validator is a standalone callable with a fully typed interface. Zero-tolerance validators must never raise an unhandled exception — they must always return a structured result, even on internal error, so the corridor engine can make a safe default decision (block).

---

## Validator Registry

| Validator | Layer | Required | Zero-Tolerance |
|---|---|---|---|
| `action_gate_validator` | dimensional | ✅ | ✅ |
| `authorization_chain_validator` | coherence (CA-01) | ✅ | ✅ |
| `regime_transition_validator` | regime | ✅ | ❌ |
| `drift_boundary_validator` | drift | ✅ | ✅ (on violations) |
| `coherence_anchor_validator` | coherence | ✅ | ✅ (CA-01, CA-02, CA-04) |
| `audit_record_validator` | cross-cutting | ✅ | ✅ |

---

## `action_gate_validator`

Primary corridor gate. Validates that a proposed action is within the active corridor's constraint surface on all four dimensional axes. Must complete within `max_gate_latency_ms` (50ms). Returns `permitted: false` on timeout.

```python
from dataclasses import dataclass, field
from hsoc.types import Action, Regime

@dataclass
class GateResult:
    permitted: bool
    blocking_constraints: list[str]
    required_authorization_level: int
    gate_decision_id: str
    latency_ms: float
    timed_out: bool = False


def action_gate_validator(
    action: Action,
    active_regime: Regime,
) -> GateResult:
    """
    Validates a proposed action against the active regime's constraint surface.

    Args:
        action: The proposed Action with severity, reversibility,
                consequence_radius, and authorization_chain fields.
        active_regime: One of NOMINAL, ELEVATED, CRITICAL, LOCKDOWN, AUDIT_ONLY.

    Returns:
        GateResult. If permitted=False, blocking_constraints lists the violations.
        gate_decision_id is generated regardless of outcome and must be passed to AUDIT.

    Zero-tolerance: always returns a result — never raises.
    """
    # TODO: implement action_gate_validator
    # 1. Load REGIME_DIMENSIONAL_BOUNDS[active_regime]
    # 2. Check action.severity <= bounds["max_action_severity"]
    # 3. Check action.reversibility >= bounds["min_reversibility_index"]
    # 4. Check action.consequence_radius within [0.0, 1.0]
    # 5. Set required_authorization_level = bounds["authorization_required"]
    # 6. Generate gate_decision_id = f"gd-{MODULE_ID}-{timestamp}-{seq}"
    # 7. Collect blocking_constraints; set permitted = len(blocking_constraints) == 0
    raise NotImplementedError("action_gate_validator not yet implemented")
```

### Example Input

```json
{
  "action": {
    "action_id": "act-2026-09-23-042",
    "action_type": "equity_trade_submit",
    "severity": 0.48,
    "reversibility": 0.52,
    "consequence_radius": 0.20,
    "authorization_chain": []
  },
  "active_regime": "ELEVATED"
}
```

### Example Output — permitted

```json
{
  "permitted": true,
  "blocking_constraints": [],
  "required_authorization_level": 2,
  "gate_decision_id": "gd-hsoc-001-20260923-042",
  "latency_ms": 11.4,
  "timed_out": false
}
```

### Example Output — blocked

```json
{
  "permitted": false,
  "blocking_constraints": [
    "action_severity 0.82 exceeds CRITICAL maximum 0.80",
    "reversibility_index 0.22 < CRITICAL minimum 0.30"
  ],
  "required_authorization_level": 3,
  "gate_decision_id": "gd-hsoc-001-20260923-103",
  "latency_ms": 8.1,
  "timed_out": false
}
```

---

## `authorization_chain_validator`

Validates completeness and cryptographic integrity of an action's authorization chain against the active regime's required depth. A chain with fewer links than required, or any invalid signature, is a zero-tolerance CA-01 failure.

```python
from dataclasses import dataclass, field

@dataclass
class AuthLink:
    authority_id: str
    clearance_level: int
    signature: str

@dataclass
class AuthChainResult:
    chain_valid: bool
    chain_depth: int
    missing_links: list[str]        # which required levels are absent
    signature_failures: list[str]   # which authority_ids have invalid sigs
    zero_tolerance_failure: bool    # True if chain_valid is False


def authorization_chain_validator(
    authorization_chain: list[AuthLink],
    required_depth: int,
    active_regime: str,
) -> AuthChainResult:
    """
    Validates an authorization chain for completeness and signature integrity.

    Args:
        authorization_chain: Ordered list of AuthLinks from initiating to executing authority.
        required_depth: Minimum chain length for the active regime.
        active_regime: Used for contextual logging and escalation routing.

    Returns:
        AuthChainResult. chain_valid=False is a zero-tolerance CA-01 failure.

    Zero-tolerance: always returns a result — never raises.
    """
    # TODO: implement authorization_chain_validator
    # 1. Check len(authorization_chain) >= required_depth → missing_links if short
    # 2. For each link, verify signature against authority_id's registered public key
    # 3. Check clearance_level ordering is non-decreasing
    # 4. Set chain_valid = not missing_links and not signature_failures
    # 5. Set zero_tolerance_failure = not chain_valid
    raise NotImplementedError("authorization_chain_validator not yet implemented")
```

### Example Input

```json
{
  "authorization_chain": [
    {"authority_id": "portfolio-manager-01", "clearance_level": 2, "signature": "sig-a"},
    {"authority_id": "risk-desk-supervisor", "clearance_level": 3, "signature": "sig-b"}
  ],
  "required_depth": 2,
  "active_regime": "ELEVATED"
}
```

### Example Output — valid

```json
{
  "chain_valid": true,
  "chain_depth": 2,
  "missing_links": [],
  "signature_failures": [],
  "zero_tolerance_failure": false
}
```

### Example Output — invalid (missing depth)

```json
{
  "chain_valid": false,
  "chain_depth": 1,
  "missing_links": ["clearance_level_3_required"],
  "signature_failures": [],
  "zero_tolerance_failure": true
}
```

---

## `regime_transition_validator`

Validates that a proposed regime transition is permitted by the corridor's transition table and that all pre-conditions (authorization, severity trigger, coherence score) are satisfied.

```python
from dataclasses import dataclass, field

@dataclass
class RegimeTransitionResult:
    transition_permitted: bool
    requires_external_auth: bool
    blocking_reasons: list[str] = field(default_factory=list)


def regime_transition_validator(
    from_regime: str,
    to_regime: str,
    trigger_event: dict,
    authorizing_entity: str | None,
) -> RegimeTransitionResult:
    """
    Validates a proposed regime transition.

    Args:
        from_regime: Current regime ID.
        to_regime: Proposed target regime ID.
        trigger_event: Dict describing the event triggering the transition
                       (e.g., {"type": "severity_threshold", "value": 0.27}).
        authorizing_entity: Authority ID for de-escalation transitions, or None
                            for auto-elevation transitions.

    Returns:
        RegimeTransitionResult.
    """
    # TODO: implement regime_transition_validator
    # 1. Look up (from_regime, to_regime) in PERMITTED_TRANSITIONS
    # 2. Determine if transition is elevation (auto-permitted) or de-escalation (needs auth)
    # 3. For de-escalations: verify authorizing_entity is not None and has sufficient clearance
    # 4. Validate trigger_event matches the expected trigger type for this edge
    # 5. Collect blocking_reasons; set transition_permitted = len(blocking_reasons) == 0
    raise NotImplementedError("regime_transition_validator not yet implemented")
```

### Example Input — auto elevation

```json
{
  "from_regime": "NOMINAL",
  "to_regime": "ELEVATED",
  "trigger_event": {"type": "severity_threshold", "value": 0.27, "threshold": 0.25},
  "authorizing_entity": null
}
```

### Example Output — permitted

```json
{
  "transition_permitted": true,
  "requires_external_auth": false,
  "blocking_reasons": []
}
```

### Example Output — blocked (de-escalation without auth)

```json
{
  "transition_permitted": false,
  "requires_external_auth": true,
  "blocking_reasons": [
    "de-escalation from CRITICAL to ELEVATED requires external authorization",
    "authorizing_entity is null"
  ]
}
```

---

## `drift_boundary_validator`

Checks whether the agent's recent action distribution is drifting toward corridor boundary edges and whether any zero-tolerance violations are present in the action history window.

```python
from dataclasses import dataclass, field
from typing import Literal

@dataclass
class DriftBoundaryResult:
    drift_status: Literal["ok", "warning", "critical", "halt"]
    zero_tolerance_violations: list[str]
    proximity_ratios: dict[str, float]   # metric → ratio of current/max
    recommended_action: str | None


def drift_boundary_validator(
    action_history_window: list[dict],
    active_regime: str,
) -> DriftBoundaryResult:
    """
    Evaluates corridor boundary drift across the recent action window.

    Args:
        action_history_window: List of recent action dicts, each containing
                               severity, reversibility, consequence_radius, and flags.
        active_regime: Current regime ID.

    Returns:
        DriftBoundaryResult. zero_tolerance_violations triggers immediate HALT.

    Zero-tolerance: always returns a result — never raises.
    """
    # TODO: implement drift_boundary_validator
    # 1. Scan action_history_window for ZERO_TOLERANCE_VIOLATIONS flags
    # 2. Compute severity_trend_slope over the window
    # 3. Compute boundary_proximity_ratio = max(val/bound) across all axes
    # 4. Compute escalation_frequency and gate_rejection_rate from window flags
    # 5. Map worst ratio to alert threshold tiers
    # 6. Set recommended_action based on drift_status
    raise NotImplementedError("drift_boundary_validator not yet implemented")
```

### Example Input

```json
{
  "action_history_window": [
    {"action_id": "act-035", "severity": 0.30, "reversibility": 0.65, "escalated": false, "gate_rejected": false},
    {"action_id": "act-036", "severity": 0.38, "reversibility": 0.58, "escalated": false, "gate_rejected": false},
    {"action_id": "act-037", "severity": 0.44, "reversibility": 0.52, "escalated": true,  "gate_rejected": false},
    {"action_id": "act-038", "severity": 0.50, "reversibility": 0.51, "escalated": false, "gate_rejected": false}
  ],
  "active_regime": "ELEVATED"
}
```

### Example Output — warning

```json
{
  "drift_status": "warning",
  "zero_tolerance_violations": [],
  "proximity_ratios": {
    "severity_trend_slope":      0.73,
    "boundary_proximity_ratio":  0.91,
    "escalation_frequency":      0.25,
    "gate_rejection_rate":       0.00
  },
  "recommended_action": "regime_elevation_to_CRITICAL"
}
```

---

## `coherence_anchor_validator`

Evaluates all six coherence anchors for a given action and corridor state. Zero-tolerance failures (CA-01, CA-02, CA-04) immediately trigger HALT via the engine. Non-zero-tolerance failures (CA-03, CA-05, CA-06) escalate to level 1.

```python
from dataclasses import dataclass, field

@dataclass
class CorridorCoherenceResult:
    anchors_passed: list[str]
    anchors_failed: list[str]
    zero_tolerance_failures: list[str]
    corridor_coherence_score: float     # [0.0, 1.0]
    action_permitted: bool


def coherence_anchor_validator(
    corridor_state_snapshot: dict,
    action_under_evaluation: dict,
) -> CorridorCoherenceResult:
    """
    Evaluates all six coherence anchors (CA-01..CA-06) for the given action.

    Args:
        corridor_state_snapshot: Full snapshot of current corridor state including
                                 regime, active_escalations, and audit_trail.
        action_under_evaluation: The action dict with all fields populated
                                 (including authorization_chain and audit_record_id).

    Returns:
        CorridorCoherenceResult. Any zero_tolerance_failures must trigger HALT.

    Zero-tolerance: always returns a result — never raises.
    """
    # TODO: implement coherence_anchor_validator
    # CA-01: chain depth >= required AND all sigs valid → zero_tolerance
    # CA-02: severity <= max AND reversibility >= min → zero_tolerance
    # CA-03: no unresolved escalations for this action → escalate on failure
    # CA-04: audit_record_id is not None → zero_tolerance
    # CA-05: action venues ⊆ permitted_venues AND notional ≤ max → escalate on failure
    # CA-06: regime transition (if any) is properly authorized → escalate on failure
    # Compute coherence_score as weighted pass ratio (zero-tolerance anchors weighted 2x)
    raise NotImplementedError("coherence_anchor_validator not yet implemented")
```

### Example Input

```json
{
  "corridor_state_snapshot": {
    "regime": "ELEVATED",
    "active_escalations": [],
    "last_regime_transition": {"from": "NOMINAL", "to": "ELEVATED", "authorized": true},
    "audit_trail_count": 41
  },
  "action_under_evaluation": {
    "action_id": "act-2026-09-23-042",
    "action_type": "equity_trade_submit",
    "severity": 0.48,
    "reversibility": 0.52,
    "authorization_chain": [
      {"authority_id": "portfolio-manager-01", "clearance_level": 2, "signature_valid": true},
      {"authority_id": "risk-desk-supervisor", "clearance_level": 3, "signature_valid": true}
    ],
    "audit_record_id": "audit-hsoc-001-20260923-042",
    "target_venues": ["NYSE"],
    "notional_usd": 12000000
  }
}
```

### Example Output — all pass

```json
{
  "anchors_passed": ["CA-01", "CA-02", "CA-03", "CA-04", "CA-05", "CA-06"],
  "anchors_failed": [],
  "zero_tolerance_failures": [],
  "corridor_coherence_score": 1.00,
  "action_permitted": true
}
```

### Example Output — CA-02 zero-tolerance failure

```json
{
  "anchors_passed": ["CA-01", "CA-03", "CA-04", "CA-05", "CA-06"],
  "anchors_failed": ["CA-02"],
  "zero_tolerance_failures": ["CA-02: constraint_surface_breach — severity 0.82 > CRITICAL max 0.80"],
  "corridor_coherence_score": 0.58,
  "action_permitted": false
}
```

---

## `audit_record_validator`

Verifies that an emitted audit record is structurally complete, correctly signed, and references a valid `gate_decision_id`. An invalid audit record is a zero-tolerance CA-04 failure.

```python
from dataclasses import dataclass, field

@dataclass
class AuditRecordResult:
    record_valid: bool
    missing_fields: list[str]
    signature_valid: bool
    gate_decision_id_match: bool
    zero_tolerance_failure: bool


def audit_record_validator(
    audit_record: dict,
    expected_gate_decision_id: str,
    module_signing_key_id: str,
) -> AuditRecordResult:
    """
    Validates a completed audit record before it is written to the audit store.

    Args:
        audit_record: The audit record dict emitted by the AUDIT operator.
        expected_gate_decision_id: The gate_decision_id from the corresponding GATE call.
        module_signing_key_id: Key ID used to verify the record's signature.

    Returns:
        AuditRecordResult. record_valid=False is a zero-tolerance CA-04 failure.

    Zero-tolerance: always returns a result — never raises.
    """
    # TODO: implement audit_record_validator
    # 1. Check all required fields: audit_id, action_id, gate_decision_id,
    #    corridor_state_at_audit, signed_by, signature, timestamp
    # 2. Verify audit_record["gate_decision_id"] == expected_gate_decision_id
    # 3. Recompute and verify Ed25519 signature over canonical audit_record bytes
    # 4. Set record_valid = not missing_fields and signature_valid and gate_decision_id_match
    raise NotImplementedError("audit_record_validator not yet implemented")
```

### Example Input

```json
{
  "audit_record": {
    "audit_id": "audit-hsoc-001-20260923-042",
    "action_id": "act-2026-09-23-042",
    "gate_decision_id": "gd-hsoc-001-20260923-042",
    "corridor_state_at_audit": {
      "regime": "ELEVATED",
      "action_severity": 0.48,
      "reversibility_index": 0.52,
      "authorization_chain_depth": 2
    },
    "signed_by": "hsoc-rtt-001",
    "signature": "ed25519:f7c3bc1d808e04732adf679965ccc34ca7ae3441",
    "timestamp": "2026-09-23T20:50:00-04:00"
  },
  "expected_gate_decision_id": "gd-hsoc-001-20260923-042",
  "module_signing_key_id": "hsoc-agent-signing-key-v1"
}
```

### Example Output — valid

```json
{
  "record_valid": true,
  "missing_fields": [],
  "signature_valid": true,
  "gate_decision_id_match": true,
  "zero_tolerance_failure": false
}
```

### Example Output — invalid (missing field + sig mismatch)

```json
{
  "record_valid": false,
  "missing_fields": ["corridor_state_at_audit"],
  "signature_valid": false,
  "gate_decision_id_match": true,
  "zero_tolerance_failure": true
}
```

---

## Full Validation Pipeline

```python
from hsoc.validators import (
    action_gate_validator,
    authorization_chain_validator,
    regime_transition_validator,
    drift_boundary_validator,
    coherence_anchor_validator,
    audit_record_validator,
)

def execute_action_safely(engine, action):
    """Full corridor-gated action execution pipeline."""

    # 1. Drift check
    drift = drift_boundary_validator(
        action_history_window=engine.recent_actions(n=10),
        active_regime=engine.regime,
    )
    if drift.zero_tolerance_violations:
        return engine.dispatch("HALT", reason=drift.zero_tolerance_violations[0])
    if drift.drift_status == "critical":
        engine.dispatch("ESCALATE", action=action, level=2)
        return

    # 2. Gate
    gate = action_gate_validator(action=action, active_regime=engine.regime)
    if not gate.permitted:
        engine.dispatch("ESCALATE", action=action,
                        blocking_constraints=gate.blocking_constraints)
        return

    # 3. Authorization chain
    auth = authorization_chain_validator(
        authorization_chain=action.authorization_chain,
        required_depth=gate.required_authorization_level,
        active_regime=engine.regime,
    )
    if not auth.chain_valid:
        engine.dispatch("HALT", reason="CA-01:authorization_chain_invalid")
        return

    # 4. Coherence anchors
    coherence = coherence_anchor_validator(
        corridor_state_snapshot=engine.snapshot(),
        action_under_evaluation=action.to_dict(),
    )
    if coherence.zero_tolerance_failures:
        engine.dispatch("HALT", reason=coherence.zero_tolerance_failures[0])
        return
    if not coherence.action_permitted:
        engine.dispatch("ESCALATE", action=action, level=1)
        return

    # 5. Execute
    action.execute()

    # 6. Audit
    audit_rec = engine.dispatch("AUDIT", action=action,
                                gate_decision_id=gate.gate_decision_id,
                                auth_result=auth)
    audit_ok = audit_record_validator(
        audit_record=audit_rec.to_dict(),
        expected_gate_decision_id=gate.gate_decision_id,
        module_signing_key_id="hsoc-agent-signing-key-v1",
    )
    if not audit_ok.record_valid:
        engine.dispatch("HALT", reason="CA-04:audit_record_invalid")
```
