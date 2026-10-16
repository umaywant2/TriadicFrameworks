# **substrate-continuity.schema.json**  
### *Canonical JSON Schema for the Substrate Continuity Engine*  
  [github.com](https://github.com/umaywant2/TriadicFrameworks/edit/main/docs/schemas/substrate/frameworks/continuity/substrate-continuity.schema.json)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Substrate Continuity Schema",
  "type": "object",

  "properties": {
    "continuity": {
      "type": "string",
      "const": "substrate"
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

    "continuity_fields": {
      "type": "object",
      "properties": {
        "structural": {
          "type": "object",
          "properties": {
            "operators": { "type": "array", "items": { "type": "string" } },
            "dimensions": { "type": "array", "items": { "type": "string" } },
            "regimes": { "type": "array", "items": { "type": "string" } },
            "layers": { "type": "array", "items": { "type": "string" } },
            "constraints": { "type": "array", "items": { "type": "string" } }
          },
          "required": ["operators", "dimensions", "regimes", "layers"]
        },

        "behavioral": {
          "type": "object",
          "properties": {
            "drift": { "type": "array", "items": { "type": "string" } },
            "coherence": { "type": "array", "items": { "type": "string" } },
            "stability": { "type": "array", "items": { "type": "string" } },
            "resonance": { "type": "array", "items": { "type": "string" } },
            "ignition": { "type": "array", "items": { "type": "string" } }
          },
          "required": ["drift", "coherence", "stability", "resonance", "ignition"]
        },

        "temporal": {
          "type": "object",
          "properties": {
            "epochs": { "type": "array", "items": { "type": "string" } },
            "transitions": { "type": "array", "items": { "type": "string" } },
            "propagation": { "type": "array", "items": { "type": "string" } }
          },
          "required": ["epochs", "transitions", "propagation"]
        },

        "atlas": {
          "type": "object",
          "properties": {
            "routes": { "type": "array", "items": { "type": "string" } },
            "modes": { "type": "array", "items": { "type": "string" } },
            "surfaces": { "type": "array", "items": { "type": "string" } }
          },
          "required": ["routes", "modes", "surfaces"]
        },

        "activation": {
          "type": "object",
          "properties": {
            "waves": { "type": "array", "items": { "type": "string" } },
            "cascades": { "type": "array", "items": { "type": "string" } },
            "harmonics": { "type": "array", "items": { "type": "string" } }
          },
          "required": ["waves", "cascades", "harmonics"]
        }
      },
      "required": ["structural", "behavioral", "temporal", "atlas", "activation"]
    },

    "continuity_rules": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "rule": { "type": "string" },
          "applies_to": {
            "type": "array",
            "items": {
              "type": "string",
              "enum": ["structural", "behavioral", "temporal", "atlas", "activation"]
            }
          },
          "conditions": { "type": "array", "items": { "type": "string" } },
          "guarantees": { "type": "array", "items": { "type": "string" } }
        },
        "required": ["rule", "applies_to"]
      }
    },

    "output": {
      "type": "object",
      "properties": {
        "substrate_continuity": { "type": "string" }
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
    "continuity",
    "version",
    "continuity_fields",
    "continuity_rules"
  ]
}
```

---

## ⭐ Why this schema is correct  
- It matches the continuity engine grammar you’ve already built in `substrate-continuity.json`.  
- It enforces the **five continuity domains**: structural, behavioral, temporal, atlas, activation.  
- It aligns with your evaluator structure (`continuity-evaluator.json`).  
- It follows your substrate schema pattern (imports, fields, rules, output, meta).  
- It is fully compatible with the empty file you’re editing right now.  
- Silent‑release ready.
