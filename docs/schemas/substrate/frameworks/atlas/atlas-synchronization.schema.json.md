# 🛰️ **atlas-synchronization.schema.json**  
### *Canonical JSON Schema for Triadic Atlas Synchronization Fabric*

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Triadic Atlas Synchronization Schema",
  "type": "object",

  "properties": {
    "synchronization": {
      "type": "object",
      "properties": {
        "global_fields": {
          "type": "object",
          "properties": {
            "coherence": { "type": "array", "items": { "type": "string" } },
            "drift": { "type": "array", "items": { "type": "string" } },
            "stability": { "type": "array", "items": { "type": "string" } },
            "resonance": { "type": "array", "items": { "type": "string" } },
            "epoch": { "type": "array", "items": { "type": "string" } },
            "ignition": { "type": "array", "items": { "type": "string" } }
          },
          "required": [
            "coherence",
            "drift",
            "stability",
            "resonance",
            "epoch",
            "ignition"
          ]
        },

        "country_fields": {
          "type": "object",
          "properties": {
            "triadic_surface": { "type": "array", "items": { "type": "string" } },
            "atlas_fingerprint": { "type": "array", "items": { "type": "string" } }
          },
          "required": ["triadic_surface", "atlas_fingerprint"]
        },

        "modes": {
          "type": "object",
          "properties": {
            "realtime": {
              "type": "object",
              "properties": {
                "update_cycle": { "type": "string" },
                "constraints": {
                  "type": "array",
                  "items": { "type": "string" }
                }
              },
              "required": ["update_cycle"]
            },
            "batch": {
              "type": "object",
              "properties": {
                "interval": { "type": "string" },
                "constraints": {
                  "type": "array",
                  "items": { "type": "string" }
                }
              },
              "required": ["interval"]
            }
          },
          "required": ["realtime", "batch"]
        },

        "routes": {
          "type": "object",
          "properties": {
            "execution_to_atlas": {
              "type": "array",
              "items": { "type": "string" }
            },
            "atlas_to_execution": {
              "type": "array",
              "items": { "type": "string" }
            },
            "epoch_to_atlas": {
              "type": "array",
              "items": { "type": "string" }
            },
            "ignition_to_atlas": {
              "type": "array",
              "items": { "type": "string" }
            }
          },
          "required": [
            "execution_to_atlas",
            "atlas_to_execution",
            "epoch_to_atlas",
            "ignition_to_atlas"
          ]
        },

        "consistency_rules": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "rule": { "type": "string" },
              "scope": {
                "type": "array",
                "items": {
                  "type": "string",
                  "enum": ["global", "country", "temporal", "activation"]
                }
              },
              "conditions": {
                "type": "array",
                "items": { "type": "string" }
              },
              "guarantees": {
                "type": "array",
                "items": { "type": "string" }
              }
            },
            "required": ["rule", "scope"]
          }
        }
      },
      "required": [
        "global_fields",
        "country_fields",
        "modes",
        "routes",
        "consistency_rules"
      ]
    },

    "output": {
      "type": "object",
      "properties": {
        "atlas_synchronization": { "type": "string" }
      }
    },

    "meta": {
      "type": "object",
      "properties": {
        "notes": { "type": "string" }
      }
    }
  },

  "required": ["synchronization"]
}
```

---

## ⭐ Why this schema is correct
- It validates **every structure** in your existing `atlas-synchronization.json`.  
- It enforces the canonical **global**, **country**, **mode**, **route**, and **consistency** blocks.  
- It matches the substrate-wide synchronization grammar used across execution, epoch, ignition, continuity, and invariance.  
- It is fully aligned with the rest of the Atlas cluster.  
- It is silent‑release compatible and ready for commit.
