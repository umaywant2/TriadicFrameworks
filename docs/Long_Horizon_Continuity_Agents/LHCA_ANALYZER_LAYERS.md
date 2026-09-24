# ANALYZER_LAYERS — Long_Horizon_Continuity_Agents

> Six-Layer Analysis Stack · Module `lhca-rtt-001`

The analyzer stack runs against the persistence tensor at every checkpoint. Layers execute in precedence order; failures in lower-precedence layers block higher-precedence evaluation.

---

## Layer Execution Order

```
1. operator       (precedence 1) — grammar and operator dispatch
2. dimensional    (precedence 2) — tensor shape and axis validation
3. regime         (precedence 3) — regime classification and transitions
4. drift          (precedence 4) — drift metric computation and bounding
5. coherence      (precedence 5) — coherence anchor evaluation
6. cross-cutting  (precedence 6) — observability and policy enforcement
```

---

## 1. `operator` Layer

Controls how RTT operators compose, reduce, and project across the horizon tensor.

```python
from lhca.layers import OperatorLayer
from lhca.operators import PERSIST, CHECKPOINT, HANDOFF, REHYDRATE, ROLLBACK

op_layer = OperatorLayer(
    operators=[PERSIST, CHECKPOINT, HANDOFF, REHYDRATE, ROLLBACK],
    precedence=1,
)

# Dispatch an operator
result = op_layer.dispatch("PERSIST", state_delta=delta, horizon_clock=t)
```

```json
{
  "layer": "operator",
  "active": true,
  "precedence": 1,
  "registered_operators": ["PERSIST", "HANDOFF", "REHYDRATE", "CHECKPOINT", "ROLLBACK"],
  "last_dispatch": {
    "operator": "CHECKPOINT",
    "step": 200,
    "status": "ok"
  }
}
```

---

## 2. `dimensional` Layer

Validates that continuity tensors maintain dimensional consistency across regime transitions. Only rank-preserving transforms are permitted.

### Axes

| Axis | Description | Range |
|---|---|---|
| `temporal_depth` | Step count within current regime | `[0, max_horizon_depth]` |
| `semantic_width` | Active semantic channel count | `[1, 512]` |
| `behavioral_mode` | Encoded behavioral mode index | `[0, 15]` |
| `goal_alignment` | Cosine similarity to baseline goal vector | `[0.0, 1.0]` |

```python
from lhca.layers import DimensionalLayer

dim_layer = DimensionalLayer(
    axes=["temporal_depth", "semantic_width", "behavioral_mode", "goal_alignment"],
    constraint="rank_preserving_only",
)

ok, violations = dim_layer.validate(tensor=engine.current_tensor())
```

```json
{
  "layer": "dimensional",
  "active": true,
  "axes": {
    "temporal_depth": {"value": 200, "valid_range": [0, 500]},
    "semantic_width": {"value": 128, "valid_range": [1, 512]},
    "behavioral_mode": {"value": 3, "valid_range": [0, 15]},
    "goal_alignment": {"value": 0.94, "valid_range": [0.0, 1.0]}
  },
  "constraint": "rank_preserving_only",
  "violations": []
}
```

---

## 3. `regime` Layer

Classifies the current operational regime and governs permitted transitions.

### Regime Profiles

```python
REGIME_PROFILES = {
    "WARM_CONTEXT": {
        "drift_tolerance": 0.05,
        "coherence_floor": 0.95,
        "description": "Uninterrupted context window. Full tensor fidelity.",
    },
    "COLD_HANDOFF": {
        "drift_tolerance": 0.20,
        "coherence_floor": 0.75,
        "description": "Cross-boundary rehydration. Partial fidelity expected.",
    },
    "DEEP_HORIZON": {
        "drift_tolerance": 0.40,
        "coherence_floor": 0.60,
        "description": "Many successive handoffs. Active coherence reinforcement required.",
    },
    "RECOVERY": {
        "drift_tolerance": 0.15,
        "coherence_floor": 0.80,
        "description": "Post-anomaly rollback restoration.",
    },
}
```

### Permitted Transitions

```
WARM_CONTEXT  ──► COLD_HANDOFF   (on HANDOFF operator)
WARM_CONTEXT  ──► RECOVERY       (on ROLLBACK operator)
COLD_HANDOFF  ──► WARM_CONTEXT   (on successful REHYDRATE)
COLD_HANDOFF  ──► DEEP_HORIZON   (after N consecutive COLD_HANDOFFs)
COLD_HANDOFF  ──► RECOVERY       (on ROLLBACK operator)
DEEP_HORIZON  ──► RECOVERY       (on drift critical/halt)
RECOVERY      ──► WARM_CONTEXT   (after coherence score >= floor)
```

```json
{
  "layer": "regime",
  "active": true,
  "current_regime": "WARM_CONTEXT",
  "drift_tolerance": 0.05,
  "coherence_floor": 0.95,
  "transition_history": [
    {"from": "WARM_CONTEXT", "to": "COLD_HANDOFF", "step": 100, "trigger": "HANDOFF"},
    {"from": "COLD_HANDOFF", "to": "WARM_CONTEXT", "step": 101, "trigger": "REHYDRATE"}
  ]
}
```

---

## 4. `drift` Layer

Continuously tracks cumulative behavioral and semantic deviation from the agent's baseline profile. Emits tiered alerts.

### Drift Bounds

| Metric | Max (module default) | Measurement |
|---|---|---|
| `semantic_drift` | 0.35 | 1 − cosine_similarity(current_embedding, baseline_embedding) |
| `behavioral_drift` | 0.25 | KL-divergence of action distribution vs. baseline |
| `goal_vector_drift` | 0.15 | L2 norm of (current_goal_vector − baseline_goal_vector) |
| `identity_drift` | 0.10 | Hamming distance on persona anchor activations |

### Alert Tiers

```python
DRIFT_ALERT_THRESHOLDS = {
    "ok":       (0.00, 0.60),
    "warning":  (0.60, 0.85),
    "critical": (0.85, 1.00),
    "halt":     (1.00, float("inf")),
}

MITIGATION_STRATEGIES = {
    "warning":  "coherence_reinforcement",
    "critical": "checkpoint_rollback",
    "halt":     "goal_re_anchoring",
}
```

```python
from lhca.layers import DriftLayer

drift_layer = DriftLayer.from_module(module)
status = drift_layer.evaluate(
    current_metrics={
        "semantic": 0.12,
        "behavioral": 0.08,
        "goal_vector": 0.05,
        "identity": 0.02,
    },
    active_regime="WARM_CONTEXT",
)

print(status.alert_level)   # "ok"
print(status.worst_metric)  # "semantic"
print(status.mitigation)    # None
```

```json
{
  "layer": "drift",
  "active": true,
  "current_metrics": {
    "semantic": 0.12,
    "behavioral": 0.08,
    "goal_vector": 0.05,
    "identity": 0.02
  },
  "bounds": {
    "semantic_drift_max": 0.35,
    "behavioral_drift_max": 0.25,
    "goal_vector_drift_max": 0.15,
    "identity_drift_max": 0.10
  },
  "alert_level": "ok",
  "mitigation": null
}
```

---

## 5. `coherence` Layer

Evaluates all registered coherence anchors at every checkpoint. Zero-tolerance failures immediately block any further `HANDOFF` or `PERSIST` until resolved.

### Anchor Definitions

```python
COHERENCE_ANCHORS = {
    "CA-01": {
        "name": "Primary Goal Invariant",
        "check": lambda state, baseline: (
            l2_distance(state["goal_vector"], baseline["goal_vector"])
            <= module["analyzer_layers"]["drift"]["drift_bounds"]["goal_vector_drift_max"]
        ),
        "required": True,
    },
    "CA-02": {
        "name": "Identity Signature Continuity",
        "check": lambda state, baseline: (
            state["identity_hash"] == baseline["identity_hash"]
            or semantic_similarity(state, baseline) >= 0.90
        ),
        "required": True,
    },
    "CA-03": {
        "name": "Behavioral Envelope Compliance",
        "check": lambda state, regime: (
            kl_divergence(state["action_dist"], REGIME_PROFILES[regime]["action_dist_baseline"])
            <= REGIME_PROFILES[regime]["drift_tolerance"]
        ),
        "required": True,
    },
    "CA-04": {
        "name": "Temporal Ordering Preservation",
        "check": lambda current_step, previous_step, operator: (
            current_step > previous_step or operator == "ROLLBACK"
        ),
        "required": True,
    },
    "CA-05": {
        "name": "Context Handoff Integrity",
        "check": lambda bundle: verify_signature(bundle),
        "required": False,
    },
}
```

```json
{
  "layer": "coherence",
  "active": true,
  "evaluation_at_step": 200,
  "results": {
    "CA-01": {"passed": true, "value": 0.03, "threshold": 0.15},
    "CA-02": {"passed": true, "value": "hash_match", "threshold": "exact_or_sim>=0.90"},
    "CA-03": {"passed": true, "value": 0.08, "threshold": 0.05},
    "CA-04": {"passed": true, "value": "step_200 > step_199"},
    "CA-05": {"passed": true, "value": "sig_verified"}
  },
  "coherence_score": 0.97,
  "zero_tolerance_failures": []
}
```

---

## 6. `cross-cutting` Layer

Handles observability and policy enforcement that span all other layers.

### Capabilities

| Capability | Description |
|---|---|
| `telemetry_emission` | Emits structured events to `rtt/events/continuity-v1` |
| `audit_trail_recording` | Appends signed audit records at every checkpoint |
| `inter_module_event_bus` | Pub/sub bus for cross-module events |
| `policy_enforcement_hooks` | Pre/post operator hooks for custom policy logic |
| `graceful_degradation_protocol` | Defines fallback behaviors when layers fail |

```python
from lhca.layers import CrossCuttingLayer

cc_layer = CrossCuttingLayer(
    event_schema="rtt/events/continuity-v1",
    telemetry_sink=OpenTelemetrySink(endpoint="http://otel-collector:4317"),
    audit_store=S3AuditStore(bucket="rtt-audit-trail"),
)

# Hook pre/post CHECKPOINT
cc_layer.add_hook("pre:CHECKPOINT", fn=lambda ctx: cc_layer.emit_telemetry(ctx))
cc_layer.add_hook("post:CHECKPOINT", fn=lambda ctx: cc_layer.record_audit(ctx))
```

```json
{
  "layer": "cross-cutting",
  "active": true,
  "event_schema": "rtt/events/continuity-v1",
  "telemetry": {
    "events_emitted_total": 1204,
    "last_event": {"type": "checkpoint", "step": 200, "ts": "2026-09-23T20:45:00-04:00"}
  },
  "audit_trail": {
    "records_written": 4,
    "last_record_id": "audit-lhca-001-step0200"
  },
  "hooks_registered": ["pre:CHECKPOINT", "post:CHECKPOINT", "post:ROLLBACK"]
}
```
