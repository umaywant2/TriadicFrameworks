# ROLES — Long_Horizon_Continuity_Agents

> Role Enum Definitions · Module `lhca-rtt-001`

Each role maps to a distinct substrate responsibility in the continuity pipeline. Roles marked `required: true` must be bound before the engine can start.

---

## Role Enum

```python
from enum import Enum

class LHCARole(str, Enum):
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

**Required** · Bindings: `horizon_clock`, `persistence_stack`, `rehydration_protocol`

Core execution substrate. Propagates continuity tensors across time steps, manages state serialization, and orchestrates operator dispatch.

```python
from lhca.roles import EngineRole

engine_role = EngineRole(
    horizon_clock=HorizonClock(start_step=0, max_depth=500),
    persistence_stack=PersistenceStack(format="safetensors"),
    rehydration_protocol=RehydrationProtocol.FULL_STATE_RESTORE,
)
```

```json
{
  "role": "engine",
  "bindings": {
    "horizon_clock": {"start_step": 0, "max_depth": 500},
    "persistence_stack": {"format": "safetensors", "checkpoint_interval_steps": 50},
    "rehydration_protocol": "full_state_restore"
  }
}
```

---

## `profile`

**Required** · Bindings: `identity_hash`, `goal_vector`, `persona_anchor_set`

Agent identity profile tensor. Encodes the behavioral fingerprint, goal hierarchy, and persona anchors that define *who* this agent is across all horizon steps. The identity hash is re-verified at every `REHYDRATE`.

```python
from lhca.roles import ProfileRole

profile = ProfileRole(
    identity_hash="sha256:4e07408562bedb8b60ce05c1decfd2b9...",
    goal_vector=[0.82, 0.11, 0.07],          # sums to 1.0
    persona_anchor_set=["analytical", "concise", "citation-driven"],
)
```

```json
{
  "role": "profile",
  "bindings": {
    "identity_hash": "sha256:4e07408562bedb8b60ce05c1decfd2b9",
    "goal_vector": [0.82, 0.11, 0.07],
    "persona_anchor_set": ["analytical", "concise", "citation-driven"]
  }
}
```

---

## `signature`

**Required** · Bindings: `state_checksum`, `semantic_hash`, `temporal_stamp`

Cryptographic and semantic signature of the agent's operational state at each checkpoint. Powers drift detection (by diffing successive semantic hashes) and rollback authorization (by verifying the checksum chain).

```python
from lhca.roles import SignatureRole

sig = SignatureRole.sign(
    state_bundle=engine.snapshot(),
    step=200,
)

print(sig.state_checksum)   # "sha256:e3b0c44298fc..."
print(sig.semantic_hash)    # "vec:cosine:0.98"
print(sig.temporal_stamp)   # "2026-09-23T20:45:00-04:00"
```

```json
{
  "role": "signature",
  "step": 200,
  "bindings": {
    "state_checksum": "sha256:e3b0c44298fc1c149afb4c8996fb924",
    "semantic_hash": "vec:cosine:0.98",
    "temporal_stamp": "2026-09-23T20:45:00-04:00"
  }
}
```

---

## `diagnostic`

**Required** · Bindings: `drift_monitor`, `coherence_probe`, `anomaly_emitter`

Runtime health monitor. Continuously samples the persistence tensor and emits structured events when drift metrics approach bounds or coherence anchors decay.

```python
from lhca.roles import DiagnosticRole

diag = DiagnosticRole(
    drift_monitor=DriftMonitor(sample_every_n_steps=5),
    coherence_probe=CoherenceProbe(anchors=module["analyzer_layers"]["coherence"]["coherence_anchors"]),
    anomaly_emitter=AnomalyEmitter(channel="rtt/events/continuity-v1"),
)

# Attach to engine
engine.attach_diagnostic(diag)
```

```json
{
  "role": "diagnostic",
  "bindings": {
    "drift_monitor": {"sample_every_n_steps": 5},
    "coherence_probe": {"anchor_ids": ["CA-01", "CA-02", "CA-03", "CA-04", "CA-05"]},
    "anomaly_emitter": {"channel": "rtt/events/continuity-v1"}
  },
  "last_sample": {
    "step": 200,
    "drift_status": "ok",
    "coherence_score": 0.97,
    "anomalies": []
  }
}
```

---

## `map`

**Required** · Bindings: `task_graph`, `regime_transition_table`, `horizon_depth_index`

Topological map of the long-horizon task graph. Nodes represent regime checkpoints; edges encode transition probabilities and drift vectors. The engine consults the map before every `HANDOFF` or `ROLLBACK` to determine valid successor states.

```python
from lhca.roles import MapRole

task_map = MapRole(
    task_graph=TaskGraph.from_adjacency({
        "start":        ["research_phase"],
        "research_phase": ["synthesis_phase", "COLD_HANDOFF"],
        "synthesis_phase": ["delivery", "COLD_HANDOFF"],
        "COLD_HANDOFF": ["research_phase", "synthesis_phase"],
        "delivery":     [],
    }),
    regime_transition_table=REGIME_TRANSITIONS,
    horizon_depth_index=HorizonDepthIndex(max_depth=500),
)
```

```json
{
  "role": "map",
  "bindings": {
    "task_graph": {
      "nodes": ["start", "research_phase", "synthesis_phase", "delivery"],
      "edges": [
        {"from": "start", "to": "research_phase", "weight": 1.0},
        {"from": "research_phase", "to": "synthesis_phase", "weight": 0.7},
        {"from": "research_phase", "to": "COLD_HANDOFF", "weight": 0.3}
      ]
    },
    "regime_transition_table": "see ANALYZER_LAYERS.md",
    "horizon_depth_index": {"max_depth": 500, "current_depth": 200}
  }
}
```

---

## `example`

**Optional** · Bindings: `scenario_library`, `trace_archive`, `outcome_registry`

Canonical worked examples. See [`EXAMPLES.md`](./EXAMPLES.md) for full trace payloads.

```json
{
  "role": "example",
  "bindings": {
    "scenario_library": ["EX-LHCA-001", "EX-LHCA-002"],
    "trace_archive": "./examples/traces/",
    "outcome_registry": "./examples/outcomes.json"
  }
}
```

---

## `extension`

**Optional** · Bindings: `adapter_registry`, `plugin_manifest`, `capability_flags`

Plug-in surface for domain-specific continuity strategies.

```python
from lhca.roles import ExtensionRole
from lhca.extensions import RedisCheckpointStore, PGVectorDriftMetricProvider

ext = ExtensionRole()
ext.register("ICheckpointStore", RedisCheckpointStore(url="redis://localhost:6379"))
ext.register("IDriftMetricProvider", PGVectorDriftMetricProvider(conn=pg_conn))
```

```json
{
  "role": "extension",
  "bindings": {
    "adapter_registry": {
      "ICheckpointStore": "RedisCheckpointStore",
      "IDriftMetricProvider": "PGVectorDriftMetricProvider",
      "IMemoryConsolidationAdapter": null
    },
    "capability_flags": {
      "external_checkpoint_store": true,
      "custom_drift_metrics": true,
      "memory_consolidation": false
    }
  }
}
```

---

## `index`

**Required** · Bindings: `artifact_index`, `checkpoint_log`, `drift_ledger`

Searchable index over all continuity artifacts. Supports range queries by step, checkpoint ID, or drift severity.

```json
{
  "role": "index",
  "bindings": {
    "artifact_index": {"total_artifacts": 42, "last_indexed_step": 200},
    "checkpoint_log": [
      {"id": "cp-lhca-001-step0050", "step": 50, "regime": "WARM_CONTEXT", "coherence": 0.98},
      {"id": "cp-lhca-001-step0100", "step": 100, "regime": "WARM_CONTEXT", "coherence": 0.96},
      {"id": "cp-lhca-001-step0150", "step": 150, "regime": "COLD_HANDOFF", "coherence": 0.84},
      {"id": "cp-lhca-001-step0200", "step": 200, "regime": "WARM_CONTEXT", "coherence": 0.97}
    ],
    "drift_ledger": {"warning_events": 1, "critical_events": 0, "halt_events": 0}
  }
}
```

---

## `reference`

**Optional** · Bindings: `rtt_spec_link`, `continuity_algebra_doc`, `axiom_registry`

Normative reference material pointers. Not loaded at runtime — used by tooling and documentation generators.

```json
{
  "role": "reference",
  "bindings": {
    "rtt_spec_link": "REF-RTT-SPEC",
    "continuity_algebra_doc": "REF-CONTINUITY-ALGEBRA",
    "axiom_registry": "REF-TEMPORAL-PERSISTENCE"
  }
}
```

---

## `template`

**Optional** · Bindings: `checkpoint_template`, `horizon_profile_template`, `drift_bound_template`

Scaffold templates for new continuity configurations.

```json
{
  "role": "template",
  "bindings": {
    "checkpoint_template": {
      "checkpoint_id": "cp-{module_id}-step{step:04d}",
      "regime": null,
      "semantic_hash": null,
      "state_checksum": null,
      "coherence_score": null,
      "drift": {
        "semantic": null,
        "behavioral": null,
        "goal_vector": null,
        "identity": null
      }
    },
    "horizon_profile_template": {
      "max_horizon_depth": 500,
      "checkpoint_interval_steps": 50,
      "drift_bounds": "see ANALYZER_LAYERS.md"
    },
    "drift_bound_template": {
      "semantic_drift_max": 0.35,
      "behavioral_drift_max": 0.25,
      "goal_vector_drift_max": 0.15,
      "identity_drift_max": 0.10
    }
  }
}
```
