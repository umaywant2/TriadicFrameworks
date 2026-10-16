# 🌑 **epochal-anomalies.json**  
### *Canonical anomaly registry for the Epoch Engine*

```json
{
  "anomalies": "epochal",
  "version": "1.0",
  "generated": "YYYY-MM-DD",

  "imports": {
    "epochal_timeline": "./timeline.json",
    "epochal_propagation": "./epochal-propagation.json",
    "resonance_map": "../resonance/global-resonance-map.json",
    "drift_map": "../drift/global-drift-boundary-map.json",
    "stability_envelope": "../stability/planetary-stability-envelope.json",
    "ignition_ledger": "../ignition/global-ignition-ledger.json"
  },

  "epochal_anomalies": {
    "epoch_transition_anomalies": {
      "description": "Anomalies detected during transitions between epochs E0–E7.",
      "signals": [
        "epoch_misalignment",
        "transition_break",
        "timeline_inconsistency",
        "epoch_out_of_bounds"
      ],
      "conditions": [
        "transition_time < minimum_threshold",
        "transition_time > maximum_threshold",
        "epoch_sequence_invalid"
      ]
    },

    "propagation_anomalies": {
      "description": "Anomalies detected during epochal propagation cycles.",
      "signals": [
        "propagation_break",
        "propagation_stall",
        "propagation_loop",
        "propagation_overrun"
      ],
      "conditions": [
        "cycle_duration > propagation_limit",
        "cycle_phase_invalid",
        "propagation_web_incomplete"
      ]
    },

    "resonance_anomalies": {
      "description": "Anomalies in resonance magnitude, phase, or harmonic alignment.",
      "signals": [
        "resonance_surge",
        "resonance_collapse",
        "harmonic_misalignment",
        "phase_inversion"
      ],
      "conditions": [
        "resonance_magnitude > harmonic_threshold",
        "phase_shift > allowed_window",
        "harmonic_profile_invalid"
      ]
    },

    "drift_anomalies": {
      "description": "Anomalies in drift magnitude, velocity, or boundary alignment.",
      "signals": [
        "drift_spike",
        "drift_boundary_break",
        "drift_phase_flip",
        "drift_velocity_overrun"
      ],
      "conditions": [
        "drift_magnitude > drift_boundary",
        "drift_velocity > velocity_limit",
        "drift_phase outside allowed_range"
      ]
    },

    "stability_anomalies": {
      "description": "Anomalies in stability envelope or stability index.",
      "signals": [
        "stability_instability",
        "stability_collapse",
        "stability_phase_break"
      ],
      "conditions": [
        "stability_index < stability_min",
        "stability_phase misaligned",
        "stability_envelope breach"
      ]
    },

    "ignition_epoch_anomalies": {
      "description": "Anomalies in ignition events that interfere with epoch transitions.",
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
    "epochal_anomalies": "./epochal-anomalies.json"
  },

  "meta": {
    "notes": "Canonical anomaly registry for epoch transitions, propagation cycles, resonance, drift, stability, and ignition–epoch coupling."
  }
}
```

---

## Why this is the correct artifact  
- Matches your epoch engine grammar (timeline, propagation, resonance, drift, stability, ignition).  
- Aligns with the stabilizer, propagation engine, and epochal timeline you’ve already built.  
- Uses canonical anomaly categories: **transition**, **propagation**, **resonance**, **drift**, **stability**, **ignition‑epoch**.  
- Fully compatible with the empty file in your active tab.  
- Silent‑release ready.
