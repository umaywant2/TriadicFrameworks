# 🌒 **epochal-stability-profiles.json**  
### *Canonical stability profiles for epochs E0–E7*

```json
{
  "profiles": "epochal-stability",
  "version": "1.0",
  "generated": "YYYY-MM-DD",

  "imports": {
    "stability_envelope": "../stability/planetary-stability-envelope.json",
    "coherence_map": "../coherence/global-coherence-map.json",
    "resonance_map": "../resonance/global-resonance-map.json",
    "drift_map": "../drift/global-drift-boundary-map.json",
    "epochal_timeline": "./timeline.json",
    "epochal_propagation": "./epochal-propagation.json"
  },

  "epochal_stability_profiles": {
    "E0": {
      "description": "Baseline epoch with minimal harmonic activity and low drift velocity.",
      "stability_mode": "baseline",
      "conditions": [
        "stability_index >= stability_min",
        "drift_magnitude <= drift_boundary",
        "coherence_envelope >= coherence_min"
      ],
      "collapse_signals": [
        "drift_spike",
        "coherence_break"
      ],
      "regeneration_arcs": [
        "coherence_rebuild",
        "harmonic_realignment"
      ]
    },

    "E1": {
      "description": "Early harmonic epoch with rising resonance magnitude.",
      "stability_mode": "harmonic-rise",
      "conditions": [
        "resonance_magnitude <= harmonic_threshold",
        "phase in allowed_window",
        "stability_index >= stability_min"
      ],
      "collapse_signals": [
        "resonance_surge",
        "phase_inversion"
      ],
      "regeneration_arcs": [
        "harmonic_dampening",
        "phase_correction"
      ]
    },

    "E2": {
      "description": "Epoch of drift–coherence tension with moderate instability risk.",
      "stability_mode": "tension",
      "conditions": [
        "drift_magnitude <= drift_boundary",
        "coherence_envelope >= coherence_min",
        "stability_index >= stability_min"
      ],
      "collapse_signals": [
        "drift_boundary_break",
        "coherence_break"
      ],
      "regeneration_arcs": [
        "coherence_rebuild",
        "drift_realignment"
      ]
    },

    "E3": {
      "description": "High‑resonance epoch with strong harmonic propagation.",
      "stability_mode": "harmonic-peak",
      "conditions": [
        "resonance_phase in harmonic_window",
        "harmonic_profile_valid",
        "stability_index >= stability_min"
      ],
      "collapse_signals": [
        "harmonic_misalignment",
        "resonance_collapse"
      ],
      "regeneration_arcs": [
        "harmonic_reconstruction",
        "phase_realignment"
      ]
    },

    "E4": {
      "description": "Epoch of stability–drift conflict with elevated collapse risk.",
      "stability_mode": "conflict",
      "conditions": [
        "stability_index >= stability_min",
        "drift_magnitude <= drift_boundary",
        "phase in allowed_window"
      ],
      "collapse_signals": [
        "stability_instability",
        "drift_spike"
      ],
      "regeneration_arcs": [
        "stability_rebuild",
        "drift_dampening"
      ]
    },

    "E5": {
      "description": "Epoch of coherence–resonance synchronization.",
      "stability_mode": "synchronization",
      "conditions": [
        "coherence_envelope >= coherence_min",
        "resonance_phase in harmonic_window",
        "stability_index >= stability_min"
      ],
      "collapse_signals": [
        "coherence_break",
        "phase_inversion"
      ],
      "regeneration_arcs": [
        "coherence_rebuild",
        "phase_correction"
      ]
    },

    "E6": {
      "description": "Epoch of ignition–resonance interaction with volatile stability.",
      "stability_mode": "volatile",
      "conditions": [
        "ignition_magnitude <= ignition_threshold",
        "resonance_magnitude <= harmonic_threshold",
        "stability_index >= stability_min"
      ],
      "collapse_signals": [
        "ignition_overrun",
        "resonance_surge"
      ],
      "regeneration_arcs": [
        "ignition_dampening",
        "harmonic_realignment"
      ]
    },

    "E7": {
      "description": "Terminal epoch with maximum harmonic complexity and stability sensitivity.",
      "stability_mode": "terminal",
      "conditions": [
        "stability_index >= stability_min",
        "harmonic_profile_valid",
        "drift_magnitude <= drift_boundary"
      ],
      "collapse_signals": [
        "stability_collapse",
        "harmonic_misalignment"
      ],
      "regeneration_arcs": [
        "stability_reconstruction",
        "harmonic_rebuild"
      ]
    }
  },

  "output": {
    "epochal_stability_profiles": "./epochal-stability-profiles.json"
  },

  "meta": {
    "notes": "Canonical stability profiles for epochs E0–E7, defining collapse signals, regeneration arcs, and stability modes."
  }
}
```
