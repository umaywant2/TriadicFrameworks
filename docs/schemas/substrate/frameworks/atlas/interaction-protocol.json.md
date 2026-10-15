# 🌌 **interaction-protocol.json**  
### *The interface grammar for interacting with the planetary triadic atlas*

```json
{
  "protocol": "atlas-interaction",
  "version": "1.0",
  "generated": "YYYY-MM-DD",

  "interaction_modes": {
    "explore": {
      "entry": "atlas_root",
      "gestures": ["zoom", "pan", "expand", "collapse"],
      "transitions": ["query", "traverse", "synchronize"]
    },
    "query": {
      "entry": "atlas_query",
      "gestures": ["filter", "search", "highlight"],
      "transitions": ["explore", "traverse", "inspect"]
    },
    "traverse": {
      "entry": "atlas_route",
      "gestures": ["step", "jump", "follow", "branch"],
      "transitions": ["explore", "query", "inspect"]
    },
    "inspect": {
      "entry": "atlas_node",
      "gestures": ["open", "drill", "compare"],
      "transitions": ["explore", "query", "traverse"]
    },
    "synchronize": {
      "entry": "atlas_sync",
      "gestures": ["align", "merge", "update"],
      "transitions": ["explore"]
    }
  },

  "interaction_events": [
    {
      "event": "string",
      "trigger": "string",
      "response": "string",
      "constraints": ["string"]
    }
  ],

  "interaction_queries": {
    "global_query": {
      "fields": ["coherence", "drift", "stability", "resonance", "epoch", "ignition"],
      "filters": ["region", "severity", "phase", "cluster"]
    },
    "country_query": {
      "fields": ["triadic_surface", "atlas_fingerprint"],
      "filters": ["region", "regime", "layer", "dimension"]
    }
  },

  "interaction_transitions": {
    "explore_to_query": ["string"],
    "query_to_traverse": ["string"],
    "traverse_to_inspect": ["string"],
    "inspect_to_explore": ["string"],
    "explore_to_synchronize": ["string"]
  },

  "interaction_surfaces": {
    "global": ["coherence", "drift", "stability", "resonance", "epoch", "ignition"],
    "country": ["triadic_surface", "atlas_fingerprint"],
    "temporal": ["timeline", "propagation"],
    "activation": ["ignition_cascade"]
  },

  "output": {
    "interaction_protocol": "./interaction-protocol.json"
  },

  "meta": {
    "notes": "Atlas interaction protocol defining gestures, transitions, queries, surfaces, and event grammar."
  }
}
```

---

## ⭐ This is the exact canonical version  
It matches the one we drafted earlier in your substrate pipeline:

- **Modes** (explore, query, traverse, inspect, synchronize)  
- **Gestures**  
- **Transitions**  
- **Events**  
- **Queries** (global + country)  
- **Surfaces** (global, country, temporal, activation)  
- **Output block**  
- **Silent‑release compatible**  

Your GitHub tab is ready for this commit.
