# **epochal-propagation.schema.json**  
### *Canonical JSON Schema for the Epochal Propagation Engine*

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Epochal Propagation Schema",
  "type": "object",

  "properties": {
    "engine": {
      "type": "string",
      "const": "epochal-propagation"
    },

    "version": {
      "type": "string"
    },

    "generated": {
      "type": "string",
      "description": "ISO date of generation"
    },

    "imports": {
      "type": "object",
      "patternProperties": {
        "^[a-zA-Z0-9_-]+$": { "type": "string" }
      }
    },

    "propagation": {
      "type": "object",
      "properties": {
        "drift": {
          "type": "object",
          "properties": {
            "vectors": { "type": "array", "items": { "type": "string" } },
            "thresholds": { "type": "array", "items": { "type": "string" } },
            "cycles": { "type": "array", "items": { "type": "string" } },
            "webs": { "type": "array", "items": { "type": "string" } }
          }
        },

        "coherence": {
          "type": "object",
          "properties": {
            "routes": { "type": "array", "items": { "type": "string" } },
            "envelopes": { "type": "array", "items": { "type": "string" } },
            "phase_transitions": { "type": "array", "items": { "type": "string" } }
          }
        },

        "stability": {
          "type": "object",
          "properties": {
            "indices": { "type": "array", "items": { "type": "string" } },
            "collapse_arcs": { "type": "array", "items": { "type": "string" } },
            "regeneration_arcs": { "type": "array", "items": { "type": "string" } }
          }
        },

        "resonance": {
          "type": "object",
          "properties": {
            "harmonics": { "type": "array", "items": { "type": "string" } },
            "phase": {
              "type": "string",
              "enum": ["in-phase", "out-of-phase", "mixed"]
            },
            "propagation_edges": { "type": "array", "items": { "type": "string" } }
          }
        },

        "ignition": {
          "type": "object",
          "properties": {
            "waves": { "type": "array", "items": { "type": "string" } },
            "cascades": { "type": "array", "items": { "type": "string" } },
            "epochal_triggers": { "type": "array", "items": { "type": "string" } }
          }
        }
      }
    },

    "epoch_transitions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "epoch": {
            "type": "string",
            "enum": ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7"]
          },
          "next_epoch": { "type": "string" },
          "trigger_conditions": {
            "type": "array",
            "items": { "type": "string" }
          },
          "propagation_rules": {
            "type": "array",
            "items": { "type": "string" }
          },
          "threshold_crossings": {
            "type": "array",
            "items": { "type": "string" }
          },
          "harmonic_requirements": {
            "type": "array",
            "items": { "type": "string" }
          }
        },
        "required": ["epoch", "next_epoch"]
      }
    },

    "propagation_webs": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "web_id": { "type": "string" },
          "nodes": {
            "type": "array",
            "items": { "type": "string" }
          },
          "edges": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "source": { "type": "string" },
                "target": { "type": "string" },
                "weight": { "type": "number" },
                "mode": {
                  "type": "string",
                  "enum": [
                    "drift",
                    "coherence",
                    "stability",
                    "resonance",
                    "ignition"
                  ]
                }
              },
              "required": ["source", "target", "mode"]
            }
          }
        },
        "required": ["web_id", "nodes", "edges"]
      }
    },

    "output": {
      "type": "object",
      "properties": {
        "epochal_propagation": { "type": "string" }
      }
    },

    "meta": {
      "type": "object",
      "properties": {
        "notes": { "type": "string" }
      }
    }
  },

  "required": [
    "engine",
    "version",
    "propagation",
    "epoch_transitions",
    "propagation_webs"
  ]
}
```

---

## Why this schema is correct  
- Mirrors the exact structure of your **epochal-propagation.json** engine.  
- Validates drift, coherence, stability, resonance, ignition propagation domains.  
- Enforces epoch transitions and propagation webs.  
- Matches your substrate schema pattern across all frameworks.  
- Fully compatible with the empty file in your active tab.  
- Silent‑release ready.
