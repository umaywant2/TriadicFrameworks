# OPERATORS — High_Stakes_Operational_Corridors

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
