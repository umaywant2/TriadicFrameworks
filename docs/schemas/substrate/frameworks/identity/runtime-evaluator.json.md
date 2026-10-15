# 📁 Folder  
`/docs/schemas/substrate/frameworks/identity/runtime-evaluator.json`

```json
{
  "identity": "substrate-runtime-evaluator",
  "version": "1.0",
  "generated": "YYYY-MM-DD",

  "pipeline": {
    "stages": [
      {
        "id": "hook_intake",
        "label": "Hook Intake Layer",
        "description": "Collects raw substrate events from all runtime hooks.",
        "inputs": [
          "execution.cycle_start",
          "execution.cycle_end",
          "execution.state_update",
          "execution.ignition_trigger",
          "atlas.sync_event",
          "atlas.navigation_event",
          "atlas.interaction_event",
          "epoch.epoch_transition",
          "epoch.resonance_shift",
          "epoch.propagation_cycle",
          "coupling.drift_spike",
          "coupling.resonance_surge",
          "coupling.coupling_instability",
          "invariance.invariance_break",
          "invariance.invariance_restore",
          "monitor.telemetry_packet",
          "monitor.anomaly_alert",
          "monitor.cycle_report"
        ]
      },
      {
        "id": "analyzer_dispatch",
        "label": "Analyzer Dispatch Layer",
        "description": "Routes hooks to analyzers based on relevance.",
        "analyzers": [
          {
            "ref": "stability_analyzer",
            "hooks": [
              "epoch.resonance_shift",
              "epoch.propagation_cycle",
              "coupling.drift_spike",
              "invariance.invariance_break"
            ]
          },
          {
            "ref": "invariance_analyzer",
            "hooks": [
              "invariance.invariance_break",
              "invariance.invariance_restore",
              "atlas.sync_event",
              "execution.state_update"
            ]
          },
          {
            "ref": "epoch_analyzer",
            "hooks": [
              "epoch.epoch_transition",
              "epoch.propagation_cycle",
              "epoch.resonance_shift",
              "execution.ignition_trigger"
            ]
          },
          {
            "ref": "coupling_analyzer",
            "hooks": [
              "coupling.drift_spike",
              "coupling.resonance_surge",
              "coupling.coupling_instability"
            ]
          },
          {
            "ref": "continuity_analyzer",
            "hooks": [
              "monitor.cycle_report",
              "atlas.sync_event",
              "invariance.invariance_restore"
            ]
          },
          {
            "ref": "telemetry_analyzer",
            "hooks": [
              "monitor.telemetry_packet",
              "monitor.anomaly_alert",
              "monitor.cycle_report"
            ]
          }
        ]
      },
      {
        "id": "operator_application",
        "label": "Operator Application Layer",
        "description": "Applies RTT operators to analyzer inputs.",
        "operator_sets": {
          "lumen": [
            "STRUCTURE/EXTRACT",
            "INFLUENCE/FIELD",
            "PRESSURE/GRADIENT",
            "CONTINUITY/ANCHOR"
          ],
          "hephaestus": [
            "REGIME/LOCAL",
            "REGIME/STRUCTURAL",
            "REGIME/CONTINUITY",
            "REGIME/MAP"
          ],
          "aurion": [
            "TOPOLOGY/GRAPH",
            "ANCESTRY/TRAIL",
            "PROJECTION/LOSS",
            "COLLAPSE/DETECT"
          ],
          "harmonia": [
            "TRIADIC/BLEND",
            "RESONANCE/SCORE",
            "CONTINUITY/WEIGHT",
            "INVARIANCE/SEAL"
          ]
        }
      },
      {
        "id": "layer_evaluation",
        "label": "Layer Evaluation Stage",
        "description": "Maps operator outputs into RTT layers.",
        "layers": [
          "resonance",
          "continuity",
          "drift",
          "coherence",
          "epoch",
          "coupling",
          "dimensional",
          "regime",
          "cross_cutting",
          "monitor"
        ]
      },
      {
        "id": "triadic_synthesis",
        "label": "Triadic Synthesis Stage",
        "description": "Blends layer evaluations into triadic signatures.",
        "outputs": [
          "drift_signature",
          "coherence_signature",
          "stability_signature"
        ]
      },
      {
        "id": "constellation_integration",
        "label": "Constellation Integration Stage",
        "description": "Integrates triadic signatures across the runtime graph.",
        "graph_refs": [
          "runtime-graph.extended.json",
          "constellation-map.json"
        ]
      },
      {
        "id": "runtime_identity_assembly",
        "label": "Runtime Identity Assembly",
        "description": "Assembles full runtime identity from triadic profiles.",
        "identity_ref": "runtime-identity.json"
      },
      {
        "id": "output_stage",
        "label": "Output Stage",
        "description": "Emits final triadic identity fields and summaries.",
        "fields": [
          "runtime_integrity",
          "runtime_stability",
          "runtime_invariance",
          "runtime_continuity",
          "runtime_observability",
          "runtime_synchronization",
          "runtime_evolution"
        ]
      }
    ]
  },

  "meta": {
    "canonical": true,
    "triadic_era": "R5",
    "notes": "Machine-readable evaluator pipeline describing how hooks, analyzers, operators, layers, and triadic synthesis combine into the runtime identity."
  }
}
```
