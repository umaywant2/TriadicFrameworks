# EXAMPLES — Long_Horizon_Continuity_Agents

> Worked Scenarios with Full Trace Payloads · Module `lhca-rtt-001`

---

## EX-LHCA-001 · Multi-Session Research Agent

**Description:** An agent conducting a week-long literature review across 12 context handoffs, maintaining goal coherence and citation consistency.

**Regime sequence:** `WARM_CONTEXT → COLD_HANDOFF → WARM_CONTEXT → COLD_HANDOFF → DEEP_HORIZON`

### Setup

```python
from lhca.engine import ContinuityEngine
from lhca.operators import PERSIST, CHECKPOINT, HANDOFF, REHYDRATE

engine = ContinuityEngine.from_module(module)
engine.start(
    regime="WARM_CONTEXT",
    goal_vector=[0.70, 0.20, 0.10],   # [research, synthesis, delivery]
    persona_anchors=["thorough", "citation-driven", "skeptical"],
)
```

### Session 1 — Steps 1–50 (WARM_CONTEXT)

```python
for step in range(1, 51):
    action = agent.act()
    PERSIST(state_delta=action.to_delta(), horizon_clock=step)

# Scheduled checkpoint at step 50
cp_50 = CHECKPOINT(engine.snapshot(), reason="scheduled")
```

```json
{
  "checkpoint_id": "cp-lhca-001-step0050",
  "step": 50,
  "regime": "WARM_CONTEXT",
  "coherence_score": 0.98,
  "drift": {
    "semantic": 0.03,
    "behavioral": 0.02,
    "goal_vector": 0.01,
    "identity": 0.00
  }
}
```

### Handoff — End of Session 1

```python
cp_pre_handoff = CHECKPOINT(engine.snapshot(), reason="pre_handoff")

bundle = HANDOFF(
    checkpoint_id=cp_pre_handoff.checkpoint_id,
    target_context="session-2-2026-09-24",
    metadata={"session": 2, "total_papers_reviewed": 34},
)
```

```json
{
  "operator": "HANDOFF",
  "checkpoint_id": "cp-lhca-001-step0100",
  "target_context": "session-2-2026-09-24",
  "bundle": {
    "profile_hash": "sha256:4e07408562bedb8b60ce05c1decfd2b9",
    "goal_vector": [0.70, 0.20, 0.10],
    "active_regime": "COLD_HANDOFF",
    "signed_by": "lhca-rtt-001",
    "metadata": {"session": 2, "total_papers_reviewed": 34}
  }
}
```

### Session 2 — Rehydration (COLD_HANDOFF)

```python
result = REHYDRATE(bundle=incoming_bundle, verify=True)
# Regime automatically transitions: COLD_HANDOFF → WARM_CONTEXT after coherence verified
```

```json
{
  "operator": "REHYDRATE",
  "bundle_checkpoint_id": "cp-lhca-001-step0100",
  "integrity_ok": true,
  "active_regime": "COLD_HANDOFF",
  "coherence_score": 0.91,
  "drift_at_restore": {
    "semantic": 0.07,
    "behavioral": 0.05,
    "goal_vector": 0.02,
    "identity": 0.01
  }
}
```

### Final Outcome

```json
{
  "example_id": "EX-LHCA-001",
  "total_steps": 312,
  "total_sessions": 12,
  "total_handoffs": 12,
  "final_regime": "DEEP_HORIZON",
  "final_drift": {
    "semantic": 0.12,
    "behavioral": 0.08,
    "goal_vector": 0.05,
    "identity": 0.03
  },
  "final_coherence_score": 0.93,
  "anchors_all_satisfied": true,
  "rollback_events": 0,
  "outcome": "Goal achieved. All coherence anchors CA-01 through CA-04 satisfied at all checkpoints."
}
```

---

## EX-LHCA-002 · Persistent Negotiation Thread

**Description:** An agent negotiating a multi-party contract across 30 days with intermittent context resets and third-party integrations. One RECOVERY event triggered by semantic drift exceedance.

**Regime sequence:** `WARM_CONTEXT → COLD_HANDOFF → RECOVERY → WARM_CONTEXT → DEEP_HORIZON`

### Setup

```python
engine = ContinuityEngine.from_module(module)
engine.start(
    regime="WARM_CONTEXT",
    goal_vector=[0.50, 0.30, 0.20],   # [agreement, compliance, efficiency]
    persona_anchors=["principled", "persistent", "detail-oriented"],
)
```

### Drift Exceedance at Step 202

```python
# Diagnostic fires: semantic drift 0.37 > max 0.35
diag_event = {
    "type": "drift_critical",
    "step": 202,
    "metric": "semantic",
    "value": 0.37,
    "threshold": 0.35,
}

# drift_bound_validator returns critical
drift_result = drift_bound_validator(
    current_drift={"semantic": 0.37, "behavioral": 0.19, "goal_vector": 0.11, "identity": 0.07},
    active_regime="COLD_HANDOFF",
)
# drift_result.severity == "critical" → trigger ROLLBACK
```

### ROLLBACK to Step 150

```python
result = ROLLBACK(
    target_checkpoint_id="cp-lhca-002-step0150",
    reason="semantic_drift_critical",
    authorized_by="drift_boundary_validator",
)
```

```json
{
  "operator": "ROLLBACK",
  "target_checkpoint_id": "cp-lhca-002-step0150",
  "reason": "semantic_drift_critical",
  "authorized_by": "drift_boundary_validator",
  "result": {
    "restored_step": 150,
    "steps_discarded": 52,
    "new_regime": "RECOVERY",
    "coherence_score_post_rollback": 0.91,
    "drift_post_rollback": {
      "semantic": 0.14,
      "behavioral": 0.09,
      "goal_vector": 0.07,
      "identity": 0.04
    }
  }
}
```

### Recovery Phase

```python
# Re-anchor goal vector and persona
engine.re_anchor(
    goal_vector=[0.50, 0.30, 0.20],
    persona_anchors=["principled", "persistent", "detail-oriented"],
)

# Resume from RECOVERY regime
engine.set_regime("RECOVERY")
```

### Final Outcome

```json
{
  "example_id": "EX-LHCA-002",
  "total_steps": 420,
  "total_sessions": 18,
  "total_handoffs": 18,
  "rollback_events": 1,
  "rollback_at_step": 202,
  "rollback_target_step": 150,
  "final_regime": "DEEP_HORIZON",
  "final_coherence_score": 0.87,
  "anchors_all_satisfied": true,
  "outcome": "Contract negotiation completed. One RECOVERY event at step 202; rollback to CP-150 successful. All required anchors satisfied at final checkpoint."
}
```

---

## Trace Comparison

| Field | EX-LHCA-001 | EX-LHCA-002 |
|---|---|---|
| Domain | Literature review | Contract negotiation |
| Sessions | 12 | 18 |
| Total steps | 312 | 420 |
| Rollback events | 0 | 1 |
| Final regime | `DEEP_HORIZON` | `DEEP_HORIZON` |
| Final coherence | 0.93 | 0.87 |
| All anchors satisfied | ✅ | ✅ |
| Worst drift metric | semantic (0.12) | semantic (recovered from 0.37) |
