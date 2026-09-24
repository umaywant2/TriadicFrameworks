# EXAMPLES — High_Stakes_Operational_Corridors

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
