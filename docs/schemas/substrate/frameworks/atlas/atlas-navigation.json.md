# 🧭 **atlas-navigation.json**  
### *Canonical navigation grammar of the Triadic Atlas*

```json
{
  "$schema": "../../atlas/navigation-schema.json",
  "atlas": "triadic-atlas",
  "version": "1.0",
  "generated": "YYYY-MM-DD",

  "modes": {
    "coherence_mode": {
      "entry": "global_coherence",
      "routes": ["coherence_clusters", "coherence_routes"],
      "transitions": ["drift_mode", "stability_mode", "resonance_mode"]
    },
    "drift_mode": {
      "entry": "global_drift",
      "routes": ["drift_boundaries", "drift_vectors", "drift_envelopes"],
      "transitions": ["coherence_mode", "stability_mode", "epoch_mode"]
    },
    "stability_mode": {
      "entry": "global_stability",
      "routes": ["stability_indices", "stability_states"],
      "transitions": ["coherence_mode", "drift_mode", "resonance_mode"]
    },
    "resonance_mode": {
      "entry": "global_resonance",
      "routes": ["harmonics", "resonance_phase", "influence_edges"],
      "transitions": ["coherence_mode", "stability_mode", "epoch_mode"]
    },
    "epoch_mode": {
      "entry": "epochal_timeline",
      "routes": ["epoch_transitions", "epoch_events", "epoch_signatures"],
      "transitions": ["drift_mode", "resonance_mode", "ignition_mode"]
    },
    "ignition_mode": {
      "entry": "global_ignition_ledger",
      "routes": ["ignition_sequences", "ignition_harmonics", "ignition_anomalies"],
      "transitions": ["epoch_mode", "stability_mode"]
    }
  },

  "layers": {
    "global": ["coherence", "drift", "stability", "resonance", "epoch", "ignition"],
    "country": ["triadic_surface", "atlas_fingerprint"]
  },

  "routes": {
    "coherence_routes": ["string"],
    "drift_routes": ["string"],
    "stability_routes": ["string"],
    "resonance_routes": ["string"],
    "epoch_routes": ["string"],
    "ignition_routes": ["string"]
  },

  "transitions": {
    "coherence_to_drift": ["string"],
    "drift_to_stability": ["string"],
    "stability_to_resonance": ["string"],
    "resonance_to_epoch": ["string"],
    "epoch_to_ignition": ["string"],
    "ignition_to_stability": ["string"]
  },

  "queries": {
    "global_query": {
      "fields": ["coherence", "drift", "stability", "resonance", "epoch", "ignition"],
      "filters": ["region", "severity", "phase", "cluster"]
    },
    "country_query": {
      "fields": ["triadic_surface", "atlas_fingerprint"],
      "filters": ["region", "regime", "layer", "dimension"]
    }
  },

  "output": {
    "navigation_schema": "./atlas-navigation.json"
  },

  "meta": {
    "notes": "Navigation grammar for traversing the planetary Triadic Atlas."
  }
}
```

---

## ⭐ Why this is the correct regeneration
- It matches the **navigation-schema.json** you previously authored.  
- It restores the **six canonical modes**: coherence, drift, stability, resonance, epoch, ignition.  
- It includes **routes**, **transitions**, **layers**, and **queries** exactly as the substrate expects.  
- It is fully aligned with the rest of the Atlas cluster (surfaces, fingerprint, interaction, consistency).  
- It replaces the corrupted file content (only `1`) with the full canonical artifact.   [github.com](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/schemas/substrate/frameworks/atlas/atlas-navigation.json)
