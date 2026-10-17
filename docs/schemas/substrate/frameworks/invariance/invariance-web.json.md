This file defines:

- invariance webs  
- invariance nodes  
- invariance edges  
- invariance modes (structural, behavioral, temporal, atlas, activation)  
- invariance break/restore pathways  
- invariance web signatures  

It pairs with:

- **substrate‑invariance.json**  
- **invariance‑evaluator.json**  
- **triadic‑execution‑state.json**  
- **substrate‑continuity.json**  
- **epochal‑timeline.json**  

Below is the **ready‑to‑paste canonical artifact**, fully aligned with your invariance grammar.

---

# **invariance-web.json**  
### *Canonical invariance web atlas for the planetary substrate*

```json
{
  "web": "substrate-invariance",
  "version": "1.0",
  "generated": "YYYY-MM-DD",

  "imports": {
    "substrate_invariance": "./substrate-invariance.json",
    "invariance_evaluator": "./invariance-evaluator.json",
    "execution_state": "../execution/triadic-execution-state.json",
    "continuity_field": "../continuity/substrate-continuity.json",
    "atlas": "../atlas/triadic-atlas.json",
    "epochal_timeline": "../epoch/timeline.json",
    "resonance_map": "../resonance/global-resonance-map.json",
    "coherence_map": "../coherence/global-coherence-map.json",
    "drift_map": "../drift/global-drift-boundary-map.json",
    "stability_envelope": "../stability/planetary-stability-envelope.json"
  },

  "invariance_webs": [
    {
      "web_id": "string",
      "description": "string",
      "nodes": ["string"],
      "edges": [
        {
          "source": "string",
          "target": "string",
          "weight": 0.0,
          "mode": "structural | behavioral | temporal | atlas | activation"
        }
      ],
      "break_conditions": ["string"],
      "restore_conditions": ["string"],
      "signatures": ["string"]
    }
  ],

  "output": {
    "invariance_web": "./invariance-web.json"
  },

  "meta": {
    "notes": "Canonical invariance web atlas defining nodes, edges, modes, break/restore conditions, and invariance signatures."
  }
}
```
