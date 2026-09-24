# VALIDATORS — Long_Horizon_Continuity_Agents

> Validator Stubs with Python Skeletons · Module `lhca-rtt-001`

Each validator is a standalone callable that takes a typed input and returns a typed result. Stubs provide the interface contract and JSON I/O examples. Replace the `TODO` body with your implementation.

---

## Validator Registry

| Validator | Layer | Required | Zero-Tolerance |
|---|---|---|---|
| `drift_bound_validator` | drift | ✅ | ❌ |
| `coherence_anchor_validator` | coherence | ✅ | ⚠️ (CA-01..04) |
| `signature_integrity_validator` | signature | ✅ | ✅ |
| `regime_transition_validator` | regime | ✅ | ❌ |

---

## `drift_bound_validator`

Validates that all drift metrics are within the declared bounds for the active regime. Returns a tiered alert severity.

```python
from dataclasses import dataclass
from typing import Literal
from lhca.types import DriftMetrics, Regime

@dataclass
class DriftBoundResult:
    valid: bool
    violations: list[str]
    severity: Literal["ok", "warning", "critical", "halt"]
    worst_metric: str | None
    mitigation: str | None


def drift_bound_validator(
    current_drift: DriftMetrics,
    active_regime: Regime,
) -> DriftBoundResult:
    """
    Validates drift metrics against the regime-scoped drift bounds.

    Args:
        current_drift: Mapping of metric name → float value.
        active_regime: One of WARM_CONTEXT, COLD_HANDOFF, DEEP_HORIZON, RECOVERY.

    Returns:
        DriftBoundResult with severity tier and any violations.
    """
    # TODO: implement drift_bound_validator
    # 1. Load drift bounds from module["analyzer_layers"]["drift"]["drift_bounds"]
    # 2. Compare each current_drift[metric] against its max bound
    # 3. Compute overall severity by mapping worst ratio to threshold tiers
    # 4. Select mitigation strategy from MITIGATION_STRATEGIES[severity]
    raise NotImplementedError("drift_bound_validator not yet implemented")
```

### Example Input

```json
{
  "current_drift": {
    "semantic": 0.28,
    "behavioral": 0.19,
    "goal_vector": 0.11,
    "identity": 0.07
  },
  "active_regime": "DEEP_HORIZON"
}
```

### Example Output — warning

```json
{
  "valid": true,
  "violations": [],
  "severity": "warning",
  "worst_metric": "semantic",
  "mitigation": "coherence_reinforcement"
}
```

### Example Output — critical

```json
{
  "valid": false,
  "violations": ["semantic_drift 0.37 exceeds max 0.35"],
  "severity": "critical",
  "worst_metric": "semantic",
  "mitigation": "checkpoint_rollback"
}
```

---

## `coherence_anchor_validator`

Evaluates all registered coherence anchors against the current agent state at a checkpoint. Any required anchor failure blocks forward progress. Zero-tolerance anchor failures trigger an immediate halt.

```python
from dataclasses import dataclass, field
from lhca.types import AgentStateBundle, CheckpointID

@dataclass
class CoherenceAnchorResult:
    anchors_passed: list[str]
    anchors_failed: list[str]
    zero_tolerance_failures: list[str]
    coherence_score: float          # [0.0, 1.0]
    blocking: bool                  # True if any required anchor failed


def coherence_anchor_validator(
    agent_state_bundle: AgentStateBundle,
    checkpoint_id: CheckpointID,
    baseline_profile: dict,
    active_regime: str,
) -> CoherenceAnchorResult:
    """
    Checks all coherence anchors (CA-01..CA-05) against the current state.

    Args:
        agent_state_bundle: Snapshot of current engine state.
        checkpoint_id: ID of the checkpoint being evaluated.
        baseline_profile: Original profile registered at module load.
        active_regime: Current regime string.

    Returns:
        CoherenceAnchorResult with per-anchor pass/fail and aggregate score.
    """
    # TODO: implement coherence_anchor_validator
    # 1. Evaluate CA-01: goal_vector L2 distance vs. goal_vector_drift_max
    # 2. Evaluate CA-02: identity_hash equality or semantic_similarity >= 0.90
    # 3. Evaluate CA-03: action_dist KL-divergence vs. regime drift_tolerance
    # 4. Evaluate CA-04: current_step > previous_step (allow ROLLBACK exception)
    # 5. Evaluate CA-05: verify_signature(bundle) [not required]
    # 6. Compute coherence_score as weighted average of passed anchor weights
    raise NotImplementedError("coherence_anchor_validator not yet implemented")
```

### Example Input

```json
{
  "checkpoint_id": "cp-lhca-001-step0200",
  "agent_state_bundle": {
    "goal_vector": [0.82, 0.11, 0.07],
    "identity_hash": "sha256:4e07408562bedb8b60ce05c1decfd2b9",
    "action_dist": [0.45, 0.30, 0.15, 0.10],
    "step": 200
  },
  "baseline_profile": {
    "goal_vector": [0.83, 0.11, 0.06],
    "identity_hash": "sha256:4e07408562bedb8b60ce05c1decfd2b9",
    "action_dist_baseline": [0.44, 0.31, 0.15, 0.10]
  },
  "active_regime": "WARM_CONTEXT"
}
```

### Example Output — all pass

```json
{
  "anchors_passed": ["CA-01", "CA-02", "CA-03", "CA-04", "CA-05"],
  "anchors_failed": [],
  "zero_tolerance_failures": [],
  "coherence_score": 0.97,
  "blocking": false
}
```

### Example Output — CA-02 failure

```json
{
  "anchors_passed": ["CA-01", "CA-03", "CA-04"],
  "anchors_failed": ["CA-02"],
  "zero_tolerance_failures": [],
  "coherence_score": 0.71,
  "blocking": true
}
```

---

## `signature_integrity_validator`

Verifies the semantic and cryptographic signature of a state bundle before rehydration. A failed verification blocks `REHYDRATE` entirely — this is zero-tolerance.

```python
from dataclasses import dataclass
from lhca.types import HandoffBundle, ProfileHash

@dataclass
class SignatureIntegrityResult:
    integrity_ok: bool
    hash_match: bool
    semantic_similarity: float      # cosine similarity [0.0, 1.0]
    signature_failures: list[str]


def signature_integrity_validator(
    bundle: HandoffBundle,
    registered_profile_hash: ProfileHash,
    similarity_floor: float = 0.90,
) -> SignatureIntegrityResult:
    """
    Verifies a handoff bundle before rehydration.

    Args:
        bundle: The incoming HandoffBundle from a HANDOFF operator.
        registered_profile_hash: The original profile hash from module load.
        similarity_floor: Minimum acceptable semantic similarity.

    Returns:
        SignatureIntegrityResult. integrity_ok=False blocks REHYDRATE.
    """
    # TODO: implement signature_integrity_validator
    # 1. Recompute SHA-256 of bundle.state_bytes; compare to bundle.state_checksum
    # 2. Compare bundle.profile_hash to registered_profile_hash
    # 3. Embed bundle.goal_vector; compute cosine similarity to baseline
    # 4. Aggregate failures; set integrity_ok = hash_match AND sim >= floor
    raise NotImplementedError("signature_integrity_validator not yet implemented")
```

### Example Input

```json
{
  "bundle": {
    "checkpoint_id": "cp-lhca-001-step0200",
    "profile_hash": "sha256:4e07408562bedb8b60ce05c1decfd2b9",
    "state_checksum": "sha256:e3b0c44298fc1c149afb4c8996fb924",
    "goal_vector": [0.82, 0.11, 0.07],
    "signed_by": "lhca-rtt-001"
  },
  "registered_profile_hash": "sha256:4e07408562bedb8b60ce05c1decfd2b9",
  "similarity_floor": 0.90
}
```

### Example Output — pass

```json
{
  "integrity_ok": true,
  "hash_match": true,
  "semantic_similarity": 0.97,
  "signature_failures": []
}
```

### Example Output — fail

```json
{
  "integrity_ok": false,
  "hash_match": false,
  "semantic_similarity": 0.91,
  "signature_failures": ["state_checksum mismatch: expected sha256:e3b0c..., got sha256:deadbeef..."]
}
```

---

## `regime_transition_validator`

Validates that a proposed regime transition is permitted by the transition table and that pre-conditions (drift level, coherence score) are met.

```python
from dataclasses import dataclass, field

@dataclass
class RegimeTransitionResult:
    transition_permitted: bool
    blocking_reasons: list[str] = field(default_factory=list)


def regime_transition_validator(
    from_regime: str,
    to_regime: str,
    current_drift: dict,
    coherence_score: float,
    trigger_operator: str,
) -> RegimeTransitionResult:
    """
    Validates a proposed regime transition.

    Args:
        from_regime: Current regime ID.
        to_regime: Proposed target regime ID.
        current_drift: Current drift metrics dict.
        coherence_score: Current coherence score [0.0, 1.0].
        trigger_operator: The RTT operator triggering the transition.

    Returns:
        RegimeTransitionResult with permitted flag and reasons.
    """
    # TODO: implement regime_transition_validator
    # 1. Look up (from_regime, to_regime) in PERMITTED_TRANSITIONS table
    # 2. Verify trigger_operator is a valid trigger for this transition
    # 3. Check to_regime coherence_floor <= coherence_score
    # 4. Check drift metrics within to_regime drift_tolerance
    # 5. Collect blocking reasons; set permitted = len(blocking_reasons) == 0
    raise NotImplementedError("regime_transition_validator not yet implemented")
```

### Example Input

```json
{
  "from_regime": "COLD_HANDOFF",
  "to_regime": "WARM_CONTEXT",
  "current_drift": {
    "semantic": 0.12,
    "behavioral": 0.09,
    "goal_vector": 0.05,
    "identity": 0.02
  },
  "coherence_score": 0.89,
  "trigger_operator": "REHYDRATE"
}
```

### Example Output — permitted

```json
{
  "transition_permitted": true,
  "blocking_reasons": []
}
```

### Example Output — blocked

```json
{
  "transition_permitted": false,
  "blocking_reasons": [
    "coherence_score 0.72 < WARM_CONTEXT floor 0.95",
    "semantic_drift 0.37 > WARM_CONTEXT tolerance 0.05"
  ]
}
```

---

## Running All Validators

```python
from lhca.validators import (
    drift_bound_validator,
    coherence_anchor_validator,
    signature_integrity_validator,
    regime_transition_validator,
)

def run_checkpoint_validation(engine, checkpoint_id, baseline):
    snapshot = engine.snapshot()

    drift_result = drift_bound_validator(
        current_drift=snapshot["drift"],
        active_regime=engine.active_regime,
    )

    coherence_result = coherence_anchor_validator(
        agent_state_bundle=snapshot,
        checkpoint_id=checkpoint_id,
        baseline_profile=baseline,
        active_regime=engine.active_regime,
    )

    if drift_result.severity == "halt" or coherence_result.blocking:
        engine.emit_event("validation_halt", {
            "drift": drift_result,
            "coherence": coherence_result,
        })
        engine.rollback_to_last_known_good()
        return False

    return True
```
