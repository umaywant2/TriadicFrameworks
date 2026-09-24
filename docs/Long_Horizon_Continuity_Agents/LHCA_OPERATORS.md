# OPERATORS — Long_Horizon_Continuity_Agents

> RTT Operator Grammar · Module `lhca-rtt-001` · Layer: `operator` (precedence 1)

RTT operators are the primitives through which a continuity agent interacts with its own temporal substrate. Each operator mutates or queries the **persistence tensor** in a defined, composable way.

---

## Operator Registry

| Operator | Class | Side Effects | Safe to Retry? |
|---|---|---|---|
| `PERSIST` | write | Extends persistence stack | ✅ idempotent |
| `HANDOFF` | transfer | Serializes + emits state bundle | ✅ with dedup |
| `REHYDRATE` | read/write | Restores from checkpoint bundle | ⚠️ once per checkpoint |
| `CHECKPOINT` | snapshot | Writes signed state snapshot | ✅ idempotent |
| `ROLLBACK` | restore | Reverts to a previous checkpoint | ⚠️ destructive forward |

---

## `PERSIST`

Extends the persistence stack by appending the current agent state delta to the horizon tensor. Called at every action step.

### Signature

```python
def PERSIST(state_delta: dict, horizon_clock: int) -> PersistResult:
    ...
```

### Example

```python
from lhca.operators import PERSIST

result = PERSIST(
    state_delta={
        "goal_vector": [0.82, 0.11, 0.07],
        "last_action": "literature_search",
        "behavioral_mode": "exploratory",
    },
    horizon_clock=142,
)

print(result.stack_depth)   # 143
print(result.drift_delta)   # 0.03
```

### JSON payload

```json
{
  "operator": "PERSIST",
  "horizon_clock": 142,
  "state_delta": {
    "goal_vector": [0.82, 0.11, 0.07],
    "last_action": "literature_search",
    "behavioral_mode": "exploratory"
  },
  "result": {
    "stack_depth": 143,
    "drift_delta": 0.03,
    "persistence_ok": true
  }
}
```

---

## `CHECKPOINT`

Writes a signed, immutable snapshot of the full agent state. Occurs automatically every `checkpoint_interval_steps` (default 50) or can be triggered manually.

### Signature

```python
def CHECKPOINT(engine_state: dict, reason: str = "scheduled") -> CheckpointResult:
    ...
```

### Example

```python
from lhca.operators import CHECKPOINT

cp = CHECKPOINT(
    engine_state=engine.snapshot(),
    reason="pre_handoff",
)

print(cp.checkpoint_id)    # "cp-lhca-001-step0200"
print(cp.semantic_hash)    # "sha256:e3b0c44298fc..."
print(cp.regime)           # "WARM_CONTEXT"
```

### JSON payload

```json
{
  "operator": "CHECKPOINT",
  "reason": "pre_handoff",
  "checkpoint_id": "cp-lhca-001-step0200",
  "semantic_hash": "sha256:e3b0c44298fc1c149afb4c8996fb92427ae41e4649b934ca495991b7852b855",
  "regime": "WARM_CONTEXT",
  "step": 200,
  "coherence_score": 0.97,
  "drift": {
    "semantic": 0.08,
    "behavioral": 0.05,
    "goal_vector": 0.03,
    "identity": 0.01
  }
}
```

---

## `HANDOFF`

Serializes the agent's full continuity bundle and emits it to the next execution context. Includes the most recent checkpoint, active regime, and drift history.

### Signature

```python
def HANDOFF(
    checkpoint_id: str,
    target_context: str,
    metadata: dict | None = None,
) -> HandoffBundle:
    ...
```

### Example

```python
from lhca.operators import HANDOFF

bundle = HANDOFF(
    checkpoint_id="cp-lhca-001-step0200",
    target_context="session-2026-09-24",
    metadata={"handoff_reason": "context_window_limit"},
)

# Transmit bundle to next context
next_context.receive(bundle.serialize())
```

### JSON payload

```json
{
  "operator": "HANDOFF",
  "checkpoint_id": "cp-lhca-001-step0200",
  "target_context": "session-2026-09-24",
  "metadata": {
    "handoff_reason": "context_window_limit"
  },
  "bundle": {
    "profile_hash": "sha256:abc123...",
    "goal_vector": [0.82, 0.11, 0.07],
    "active_regime": "COLD_HANDOFF",
    "drift_history_last_10": [0.02, 0.03, 0.03, 0.04, 0.04, 0.05, 0.06, 0.07, 0.07, 0.08],
    "signed_by": "lhca-rtt-001"
  }
}
```

---

## `REHYDRATE`

Restores the agent's full continuity state from a received handoff bundle. Verifies signature integrity before applying. Transitions regime to `COLD_HANDOFF` automatically.

### Signature

```python
def REHYDRATE(bundle: HandoffBundle, verify: bool = True) -> RehydrateResult:
    ...
```

### Example

```python
from lhca.operators import REHYDRATE

result = REHYDRATE(bundle=received_bundle, verify=True)

if not result.integrity_ok:
    raise ContinuityError(f"Signature mismatch: {result.signature_failures}")

print(result.active_regime)     # "COLD_HANDOFF"
print(result.coherence_score)   # 0.89
print(result.drift_at_restore)  # {"semantic": 0.12, "behavioral": 0.09, ...}
```

### JSON payload

```json
{
  "operator": "REHYDRATE",
  "bundle_checkpoint_id": "cp-lhca-001-step0200",
  "integrity_ok": true,
  "signature_failures": [],
  "active_regime": "COLD_HANDOFF",
  "coherence_score": 0.89,
  "drift_at_restore": {
    "semantic": 0.12,
    "behavioral": 0.09,
    "goal_vector": 0.05,
    "identity": 0.02
  }
}
```

---

## `ROLLBACK`

Reverts agent state to a named checkpoint. Requires authorized trigger (drift critical/halt, coherence anchor failure, or explicit call). Transitions regime to `RECOVERY`.

### Signature

```python
def ROLLBACK(
    target_checkpoint_id: str,
    reason: str,
    authorized_by: str,
) -> RollbackResult:
    ...
```

### Example

```python
from lhca.operators import ROLLBACK

result = ROLLBACK(
    target_checkpoint_id="cp-lhca-001-step0150",
    reason="semantic_drift_critical",
    authorized_by="drift_boundary_validator",
)

print(result.restored_step)      # 150
print(result.steps_discarded)    # 52
print(result.new_regime)         # "RECOVERY"
```

### JSON payload

```json
{
  "operator": "ROLLBACK",
  "target_checkpoint_id": "cp-lhca-001-step0150",
  "reason": "semantic_drift_critical",
  "authorized_by": "drift_boundary_validator",
  "result": {
    "restored_step": 150,
    "steps_discarded": 52,
    "new_regime": "RECOVERY",
    "coherence_score_post_rollback": 0.91
  }
}
```

---

## Operator Composition

Operators can be composed sequentially. Common patterns:

```python
# Pre-handoff pattern
CHECKPOINT(engine.snapshot(), reason="pre_handoff")
bundle = HANDOFF(checkpoint_id=cp.checkpoint_id, target_context=next_ctx)

# Post-handoff restoration pattern
result = REHYDRATE(bundle=incoming_bundle)
PERSIST(state_delta=first_action_delta, horizon_clock=result.restored_step + 1)

# Emergency recovery pattern
CHECKPOINT(engine.snapshot(), reason="pre_rollback")
ROLLBACK(target_checkpoint_id=last_known_good, reason="ca_02_failure", authorized_by="coherence_anchor_validator")
```

---

## Operator Constraint Matrix

| From \ Allowed Next | PERSIST | CHECKPOINT | HANDOFF | REHYDRATE | ROLLBACK |
|---|---|---|---|---|---|
| `PERSIST` | ✅ | ✅ | ✅ | ❌ | ✅ |
| `CHECKPOINT` | ✅ | ✅ | ✅ | ❌ | ✅ |
| `HANDOFF` | ❌ | ❌ | ❌ | ✅ | ❌ |
| `REHYDRATE` | ✅ | ✅ | ❌ | ❌ | ✅ |
| `ROLLBACK` | ✅ | ✅ | ❌ | ❌ | ❌ |
