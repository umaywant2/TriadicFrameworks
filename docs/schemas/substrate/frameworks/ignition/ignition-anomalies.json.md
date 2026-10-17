# 🔥 **ignition-anomalies.json**  
### *Canonical anomaly registry for planetary ignition events*

```json
{
  "anomalies": "ignition",
  "version": "1.0",
  "generated": "YYYY-MM-DD",

  "imports": {
    "ignition_ledger": "./global-ignition-ledger.json",
    "ignition_cascade": "./ignition-cascade.json",
    "ignition_harmonics": "./ignition-harmonics.json",
    "epochal_anomalies": "../epoch/epochal-anomalies.json",
    "resonance_map": "../resonance/global-resonance-map.json",
    "drift_map": "../drift/global-drift-boundary-map.json",
    "stability_envelope": "../stability/planetary-stability-envelope.json",
    "coherence_map": "../coherence/global-coherence-map.json"
  },

  "ignition_anomalies": {
    "sequence_anomalies": {
      "description": "Anomalies in the ignition sequence (adapter → sync → merge → fuse → ignite → validate → stabilize).",
      "signals": [
        "sequence_break",
        "sequence_loop",
        "sequence_overrun",
        "sequence_misalignment"
      ],
      "conditions": [
        "step_missing",
        "step_out_of_order",
        "invalid_transition",
        "sequence_time > sequence_limit"
      ]
    },

    "harmonic_anomalies": {
      "description": "Anomalies in ignition harmonic alignment.",
      "signals": [
        "harmonic_misalignment",
        "harmonic_collapse",
        "harmonic_inversion"
      ],
      "conditions": [
        "harmonic_profile_invalid",
        "phase_shift > allowed_window",
        "harmonic_strength > harmonic_threshold"
      ]
    },

    "resonance_anomalies": {
      "description": "Anomalies in resonance magnitude or phase during ignition.",
      "signals": [
        "resonance_surge",
        "resonance_collapse",
        "phase_inversion"
      ],
      "conditions": [
        "resonance_magnitude > ignition_resonance_limit",
        "phase outside ignition_phase_window"
      ]
    },

    "drift_anomalies": {
      "description": "Anomalies in drift magnitude or velocity during ignition.",
      "signals": [
        "drift_spike",
        "drift_boundary_break",
        "drift_velocity_overrun"
      ],
      "conditions": [
        "drift_magnitude > drift_boundary",
        "drift_velocity > velocity_limit"
      ]
    },

    "stability_anomalies": {
      "description": "Anomalies in stability envelope during ignition.",
      "signals": [
        "stability_instability",
        "stability_collapse",
        "stability_phase_break"
      ],
      "conditions": [
        "stability_index < stability_min",
        "stability_envelope breach"
      ]
    },

    "epochal_interference": {
      "description": "Anomalies where ignition interferes with epoch transitions.",
      "signals": [
        "ignition_epoch_conflict",
        "ignition_overrun",
        "ignition_phase_mismatch"
      ],
      "conditions": [
        "ignition_event during forbidden_epoch",
        "ignition_phase misaligned with epoch_phase",
        "ignition_magnitude > epoch_threshold"
      ]
    }
  },

  "output": {
    "ignition_anomalies": "./ignition-anomalies.json"
  },

  "meta": {
    "notes": "Canonical anomaly registry for planetary ignition events, covering sequence, harmonics, resonance, drift, stability, and epochal interference."
  }
}
```

---

### Source reference  
This regeneration is grounded in the content retrieved from your active tab.   [github.com](https://github.com/umaywant2/TriadicFrameworks/edit/main/docs/schemas/substrate/frameworks/ignition/ignition-anomalies.json)
