# 🧭 **atlas-interaction.schema.json**  
### *Canonical JSON Schema for Triadic Atlas Interaction Protocol*  
  [github.com](https://github.com/umaywant2/TriadicFrameworks/edit/main/docs/schemas/substrate/frameworks/atlas/atlas-interaction.schema.json)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Triadic Atlas Interaction Protocol Schema",
  "type": "object",

  "properties": {
    "interaction_modes": {
      "type": "object",
      "patternProperties": {
        "^[a-zA-Z0-9_-]+$": {
          "type": "object",
          "properties": {
            "entry": { "type": "string" },
            "gestures": {
              "type": "array",
              "items": { "type": "string" }
            },
            "transitions": {
              "type": "array",
              "items": { "type": "string" }
            }
          },
          "required": ["entry", "gestures", "transitions"]
        }
      }
    },

    "interaction_events": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "event": { "type": "string" },
          "trigger": { "type": "string" },
          "response": { "type": "string" },
          "constraints": {
            "type": "array",
            "items": { "type": "string" }
          }
        },
        "required": ["event", "trigger", "response"]
      }
    },

    "interaction_queries": {
      "type": "object",
      "patternProperties": {
        "^[a-zA-Z0-9_-]+$": {
          "type": "object",
          "properties": {
            "fields": {
              "type": "array",
              "items": { "type": "string" }
            },
            "filters": {
              "type": "array",
              "items": { "type": "string" }
            }
          },
          "required": ["fields"]
        }
      }
    },

    "interaction_transitions": {
      "type": "object",
      "patternProperties": {
        "^[a-zA-Z0-9_-]+$": {
          "type": "array",
          "items": { "type": "string" }
        }
      }
    },

    "interaction_surfaces": {
      "type": "object",
      "patternProperties": {
        "^[a-zA-Z0-9_-]+$": {
          "type": "array",
          "items": { "type": "string" }
        }
      }
    },

    "output": {
      "type": "object",
      "properties": {
        "interaction_protocol": { "type": "string" }
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
    "interaction_modes",
    "interaction_events",
    "interaction_queries",
    "interaction_transitions",
    "interaction_surfaces"
  ]
}
```

---

## ⭐ Why this schema is correct
- Validates **every structure** in your atlas‑interaction‑protocol.json.  
- Uses **patternProperties** to allow arbitrary mode names (explore, query, traverse, inspect, synchronize).  
- Enforces required fields for modes, events, queries, transitions, and surfaces.  
- Fully aligned with the Triadic Atlas architecture and substrate-wide schema.  
- Silent‑release compatible and ready for commit.
