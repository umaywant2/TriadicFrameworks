# 🧭 **navigation-schema.schema.json**  
### *Canonical JSON Schema for Triadic Atlas Navigation Grammar*

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Triadic Atlas Navigation Schema",
  "type": "object",

  "properties": {
    "modes": {
      "type": "object",
      "patternProperties": {
        "^[a-zA-Z0-9_-]+$": {
          "type": "object",
          "properties": {
            "entry": { "type": "string" },
            "routes": {
              "type": "array",
              "items": { "type": "string" }
            },
            "transitions": {
              "type": "array",
              "items": { "type": "string" }
            }
          },
          "required": ["entry", "routes", "transitions"]
        }
      }
    },

    "layers": {
      "type": "object",
      "properties": {
        "global": {
          "type": "array",
          "items": { "type": "string" }
        },
        "country": {
          "type": "array",
          "items": { "type": "string" }
        }
      },
      "required": ["global", "country"]
    },

    "routes": {
      "type": "object",
      "patternProperties": {
        "^[a-zA-Z0-9_-]+$": {
          "type": "array",
          "items": { "type": "string" }
        }
      }
    },

    "transitions": {
      "type": "object",
      "patternProperties": {
        "^[a-zA-Z0-9_-]+$": {
          "type": "array",
          "items": { "type": "string" }
        }
      }
    },

    "queries": {
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

    "output": {
      "type": "object",
      "properties": {
        "navigation_schema": { "type": "string" }
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
    "modes",
    "layers",
    "routes",
    "transitions",
    "queries"
  ]
}
```

---

## ⭐ Why this regeneration is correct
- It fully validates the navigation grammar you rebuilt in **atlas-navigation.json**.  
- It restores the canonical structure that was lost in the corrupted file   [github.com](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/schemas/substrate/frameworks/atlas/navigation-schema.schema.json).  
- It supports arbitrary mode names (coherence_mode, drift_mode, etc.) via `patternProperties`.  
- It enforces required fields for modes, layers, routes, transitions, and queries.  
- It is fully aligned with the rest of the Atlas cluster (surfaces, fingerprint, interaction, consistency, synchronization).  
- Silent‑release compatible and ready for commit.
