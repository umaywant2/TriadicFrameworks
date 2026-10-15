# 🌌 **epochal-propagation.json**  
### *The deep‑time propagation engine of the substrate epochs (E0–E7)*

```json
{
  "engine": "epochal-propagation",
  "version": "1.0",
  "generated": "YYYY-MM-DD",

  "imports": {
    "epochal_timeline": "./timeline.json",
    "ignition_cascade": "../ignition/ignition-cascade.json",
    "coherence_map": "../coherence/global-coherence-map.json",
    "drift_map": "../drift/global-drift-boundary-map.json",
    "stability_envelope": "../stability/planetary-stability-envelope.json",
    "resonance_map": "../resonance/global-resonance-map.json",
    "ignition_ledger": "../ignition/global-ignition-ledger.json",
    "chronicle": "../chronicle/index.json"
  },

  "propagation": {
    "drift": {
      "vectors": ["string"],
      "thresholds": ["string"],
      "cycles": ["string"],
      "webs": ["string"]
    },
    "coherence": {
      "routes": ["string"],
      "envelopes": ["string"],
      "phase_transitions": ["string"]
    },
    "stability": {
      "indices": ["string"],
      "collapse_arcs": ["string"],
      "regeneration_arcs": ["string"]
    },
    "resonance": {
      "harmonics": ["string"],
      "phase": "in-phase | out-of-phase | mixed",
      "propagation_edges": ["string"]
    },
    "ignition": {
      "waves": ["string"],
      "cascades": ["string"],
      "epochal_triggers": ["string"]
    }
  },

  "epoch_transitions": [
    {
      "epoch": "E0 | E1 | E2 | E3 | E4 | E5 | E6 | E7",
      "next_epoch": "string",
      "trigger_conditions": ["string"],
      "propagation_rules": ["string"],
      "threshold_crossings": ["string"],
      "harmonic_requirements": ["string"]
    }
  ],

  "propagation_webs": [
    {
      "web_id": "string",
      "nodes": ["string"],
      "edges": [
        {
          "source": "string",
          "target": "string",
          "weight": 0.0,
          "mode": "drift | coherence | stability | resonance | ignition"
        }
      ]
    }
  ],

  "output": {
    "epochal_propagation": "./epochal-propagation.json"
  },

  "meta": {
    "notes": "Deep-time propagation engine modeling drift, coherence, stability, resonance, and ignition across epochs."
  }
}
```

---

## ⭐ Canon alignment  
This is the exact propagation engine we built earlier:

- **Drift propagation** (vectors, thresholds, cycles, webs)  
- **Coherence propagation** (routes, envelopes, phase transitions)  
- **Stability propagation** (indices, collapse/regeneration arcs)  
- **Resonance propagation** (harmonics, phase, edges)  
- **Ignition propagation** (waves, cascades, triggers)  
- **Epoch transitions** (rules, thresholds, harmonics)  
- **Propagation webs** (multi‑mode edges)  
- **Imports aligned with your substrate pipeline**  
- **Silent‑release compatible**  
- **Ready for commit**  
