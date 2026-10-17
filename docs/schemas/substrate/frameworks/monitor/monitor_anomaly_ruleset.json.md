This file defines:

- telemetry anomaly rules  
- drift / coherence / stability / resonance / ignition anomaly conditions  
- cycle‑report anomaly triggers  
- monitor‑level severity classification  
- anomaly actions and constraints  

Below is the **ready‑to‑paste canonical artifact**, fully aligned with your monitor grammar and the triadic execution engine.

---

# **monitor_anomaly_ruleset.json**  
### *Canonical anomaly‑detection ruleset for the Triadic Runtime Monitor*

```json
{
  "ruleset": "triadic-monitor-anomalies",
  "version": "1.0",
  "generated": "YYYY-MM-DD",

  "imports": {
    "triadic_execution_state": "../execution/triadic-execution-state.json",
    "monitor_telemetry": "./monitor_telemetry_packets.json",
    "monitor_cycle_reports": "./monitor_cycle_reports.json",
    "coherence_map": "../coherence/global-coherence-map.json",
    "drift_map": "../drift/global-drift-boundary-map.json",
    "stability_envelope": "../stability/planetary-stability-envelope.json",
    "resonance_map": "../resonance/global-resonance-map.json",
    "ignition_ledger": "../ignition/global-ignition-ledger.json",
    "epochal_timeline": "../epoch/timeline.json"
  },

  "monitor_anomaly_rules": [
    {
      "rule": "coherence-break",
      "description": "Coherence envelope falls below minimum threshold.",
      "conditions": [
        "coherence_envelope < coherence_min",
        "coherence_phase misaligned"
      ],
      "signals": [
        "coherence_drop",
        "coherence_phase_break"
      ],
      "severity": "medium | high | critical",
      "actions": [
        "apply_coherence_stabilizer",
        "realign_coherence_phase"
      ],
      "constraints": [
        "prevent_coherence_collapse"
      ]
    },
    {
      "rule": "drift-spike",
      "description": "Drift magnitude or velocity exceeds safe boundary.",
      "conditions": [
        "drift_magnitude > drift_boundary",
        "drift_velocity > velocity_limit"
      ],
      "signals": [
        "drift_spike",
        "drift_boundary_break"
      ],
      "severity": "high | critical",
      "actions": [
        "apply_drift_dampening",
        "realign_drift_phase"
      ],
      "constraints": [
        "prevent_drift_overrun"
      ]
    },
    {
      "rule": "stability-collapse",
      "description": "Stability index drops below minimum envelope.",
      "conditions": [
        "stability_index < stability_min",
        "stability_phase misaligned"
      ],
      "signals": [
        "stability_instability",
        "stability_collapse"
      ],
      "severity": "critical",
      "actions": [
        "apply_stability_rebuild",
        "realign_stability_phase"
      ],
      "constraints": [
        "prevent_stability_failure"
      ]
    },
    {
      "rule": "resonance-surge",
      "description": "Resonance magnitude exceeds harmonic threshold.",
      "conditions": [
        "resonance_magnitude > harmonic_threshold",
        "resonance_phase outside allowed_window"
      ],
      "signals": [
        "resonance_surge",
        "phase_inversion"
      ],
      "severity": "high | critical",
      "actions": [
        "apply_harmonic_dampening",
        "correct_resonance_phase"
      ],
      "constraints": [
        "prevent_resonance_cascade"
      ]
    },
    {
      "rule": "ignition-overrun",
      "description": "Ignition magnitude or phase exceeds safe ignition envelope.",
      "conditions": [
        "ignition_magnitude > ignition_threshold",
        "ignition_phase misaligned"
      ],
      "signals": [
        "ignition_overrun",
        "ignition_phase_break"
      ],
      "severity": "critical",
      "actions": [
        "apply_ignition_dampening",
        "realign_ignition_phase"
      ],
      "constraints": [
        "prevent_ignition_failure"
      ]
    },
    {
      "rule": "epoch-transition-anomaly",
      "description": "Epoch transition occurs under invalid propagation or misaligned phase.",
      "conditions": [
        "epoch_transition_invalid",
        "propagation_phase misaligned"
      ],
      "signals": [
        "epoch_transition_break",
        "epoch_phase_mismatch"
      ],
      "severity": "medium | high",
      "actions": [
        "apply_epochal_stabilizer",
        "correct_epoch_phase"
      ],
      "constraints": [
        "prevent_epoch_misalignment"
      ]
    }
  ],

  "output": {
    "monitor_anomaly_ruleset": "./monitor_anomaly_ruleset.json"
  },

  "meta": {
    "notes": "Canonical anomaly-detection ruleset for the Triadic Runtime Monitor."
  }
}
```
