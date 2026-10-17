# **invariance-evaluator.json**  
### *Canonical evaluator for structural, behavioral, temporal, atlas, and activation invariance*

```json
{
  "evaluator": "substrate-invariance",
  "version": "1.0",
  "generated": "YYYY-MM-DD",

  "imports": {
    "substrate_invariance": "./substrate-invariance.json",
    "execution_state": "../execution/triadic-execution-state.json",
    "continuity_field": "../continuity/substrate-continuity.json",
    "atlas": "../atlas/triadic-atlas.json",
    "epochal_timeline": "../epoch/timeline.json",
    "resonance_map": "../resonance/global-resonance-map.json",
    "coherence_map": "../coherence/global-coherence-map.json",
    "drift_map": "../drift/global-drift-boundary-map.json",
    "stability_envelope": "../stability/planetary-stability-envelope.json"
  },

  "invariance_evaluation": {
    "structural": {
      "operators": ["string"],
      "dimensions": ["string"],
      "regimes": ["string"],
      "layers": ["string"],
      "rules": ["string"],
      "status": "string",
      "breaks": ["string"],
      "restorations": ["string"]
    },

    "behavioral": {
      "drift": ["string"],
      "coherence": ["string"],
      "stability": ["string"],
      "resonance": ["string"],
      "ignition": ["string"],
      "rules": ["string"],
      "status": "string",
      "breaks": ["string"],
      "restorations": ["string"]
    },

    "temporal": {
      "epochs": ["string"],
      "transitions": ["string"],
      "propagation": ["string"],
      "rules": ["string"],
      "status": "string",
      "breaks": ["string"],
      "restorations": ["string"]
    },

    "atlas": {
      "routes": ["string"],
      "modes": ["string"],
      "transitions": ["string"],
      "rules": ["string"],
      "status": "string",
      "breaks": ["string"],
      "restorations": ["string"]
    },

    "activation": {
      "waves": ["string"],
      "cascades": ["string"],
      "harmonics": ["string"],
      "rules": ["string"],
      "status": "string",
      "breaks": ["string"],
      "restorations": ["string"]
    }
  },

  "invariance_web_evaluation": [
    {
      "web_id": "string",
      "nodes": ["string"],
      "edges": [
        {
          "source": "string",
          "target": "string",
          "weight": 0.0,
          "mode": "structural | behavioral | temporal | atlas | activation"
        }
      ],
      "status": "string",
      "breaks": ["string"],
      "restorations": ["string"]
    }
  ],

  "output": {
    "invariance_evaluation": "./invariance-evaluator.json"
  },

  "meta": {
    "notes": "Evaluator for structural, behavioral, temporal, atlas, and activation invariance across the planetary substrate."
  }
}
```
