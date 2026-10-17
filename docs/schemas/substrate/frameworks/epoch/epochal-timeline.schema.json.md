# **epochal-timeline.schema.json**  
### *Canonical JSON Schema for the Epochal Timeline (E0–E7)*

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Epochal Timeline Schema",
  "type": "object",

  "properties": {
    "timeline": {
      "type": "string",
      "const": "epochal"
    },

    "version": {
      "type": "string"
    },

    "generated": {
      "type": "string",
      "description": "ISO date of generation"
    },

    "epochs": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "epoch": {
            "type": "string",
            "enum": ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7"]
          },
          "description": { "type": "string" },
          "phase": { "type": "string" },
          "conditions": {
            "type": "array",
            "items": { "type": "string" }
          },
          "transitions_to": {
            "type": "array",
            "items": { "type": "string" }
          }
        },
        "required": ["epoch", "phase", "conditions", "transitions_to"]
      }
    },

    "sequence": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7"]
      }
    },

    "output": {
      "type": "object",
      "properties": {
        "epochal_timeline": { "type": "string" }
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
    "timeline",
    "version",
    "epochs",
    "sequence"
  ]
}
```
