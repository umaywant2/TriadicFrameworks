# VALIDATORS — High_Stakes_Operational_Corridors

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
