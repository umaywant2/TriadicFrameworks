# 🔗 **coupling-profiles.json**  
### *Canonical coupling profiles for drift–resonance–coherence–stability interaction*

```json
{
  "profiles": "substrate-coupling",
  "version": "1.0",
  "generated": "YYYY-MM-DD",

  "imports": {
    "drift_map": "../drift/global-drift-boundary-map.json",
    "resonance_map": "../resonance/global-resonance-map.json",
    "coherence_map": "../coherence/global-coherence-map.json",
    "stability_envelope": "../stability/planetary-stability-envelope.json",
    "epochal_timeline": "../epoch/timeline.json"
  },

  "coupling_profiles": {
    "drift_resonance": {
      "description": "Interaction between drift magnitude/phase and resonance magnitude/phase.",
      "modes": [
        "in-phase",
        "out-of-phase",
        "mixed"
      ],
      "conditions": [
        "drift < drift_boundary",
        "resonance < resonance_threshold"
      ],
      "instability_signals": [
        "drift_spike",
        "resonance_surge"
      ]
    },

    "drift_coherence": {
      "description": "Interaction between drift magnitude and coherence envelope.",
      "modes": [
        "aligned",
        "misaligned"
      ],
      "conditions": [
        "coherence_envelope >= coherence_min",
        "drift <= drift_boundary"
      ],
      "instability_signals": [
        "coherence_break",
        "drift_spike"
      ]
    },

    "resonance_stability": {
      "description": "Interaction between resonance harmonics and stability envelope.",
      "modes": [
        "harmonic-stable",
        "harmonic-unstable"
      ],
      "conditions": [
        "resonance_phase within harmonic_window",
        "stability_index >= stability_min"
      ],
      "instability_signals": [
        "resonance_surge",
        "stability_instability"
      ]
    },

    "epochal_coupling": {
      "description": "Interaction between epoch transitions and coupling behavior.",
      "modes": [
        "epoch-aligned",
        "epoch-misaligned"
      ],
      "conditions": [
        "epoch_transition_valid",
        "propagation_consistent"
      ],
      "instability_signals": [
        "epoch_misalignment",
        "propagation_break"
      ]
    }
  },

  "output": {
    "coupling_profiles": "./coupling-profiles.json"
  },

  "meta": {
    "notes": "Canonical coupling profiles defining drift–resonance–coherence–stability interaction across epochal transitions."
  }
}
```

---

## Why this is the correct coupling profiles file  
- Matches your substrate coupling grammar (drift spikes, resonance surges, coherence breaks, stability instabilities).  
- Aligns with the evaluator you just generated (`coupling-evaluator.json`).  
- Uses the canonical four coupling domains: **drift–resonance**, **drift–coherence**, **resonance–stability**, **epochal coupling**.  
- Fully compatible with the empty file in your active tab ().  
- Silent‑release ready.
