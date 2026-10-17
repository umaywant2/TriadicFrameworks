# **triadic-execution-engine.schema.json**  
### *Canonical JSON Schema for the Triadic Execution Engine*  
  [github.com](https://github.com/umaywant2/TriadicFrameworks/edit/main/docs/schemas/substrate/frameworks/execution/triadic-execution-engine.schema.json)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Triadic Execution Engine Schema",
  "type": "object",

  "properties": {
    "engine": {
      "type": "string",
      "const": "triadic-execution"
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

    "runtime": {
      "type": "object",
      "properties": {
        "state": {
          "type": "object",
          "properties": {
            "coherence": { "type": "number" },
            "drift": { "type": "number" },
            "stability": { "type": "string" },
            "resonance": { "type": "number" },
            "epoch": { "type": "string" },
            "ignition": { "type": "string" }
          }
        },

        "evaluation": {
          "type": "object",
          "properties": {
            "operators": { "type": "array", "items": { "type": "string" } },
            "dimensions": { "type": "array", "items": { "type": "string" } },
            "regimes": { "type": "array", "items": { "type": "string" } },
            "layers": { "type": "array", "items": { "type": "string" } }
          }
        },

        "update_cycles": {
          "type": "object",
          "properties": {
            "drift": { "type": "array", "items": { "type": "string" } },
            "coherence": { "type": "array", "items": { "type": "string" } },
            "stability": { "type": "array", "items": { "type": "string" } },
            "resonance": { "type": "array", "items": { "type": "string" } },
            "epoch": { "type": "array", "items": { "type": "string" } },
            "ignition": { "type": "array", "items": { "type": "string" } }
          }
        },

        "execution_rules": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "rule": { "type": "string" },
              "conditions": { "type": "array", "items": { "type": "string" } },
              "actions": { "type": "array", "items": { "type": "string" } },
              "constraints": { "type": "array", "items": { "type": "string" } }
            },
            "required": ["rule"]
          }
        },

        "synchronization": {
          "type": "object",
          "properties": {
            "atlas": { "type": "array", "items": { "type": "string" } },
            "continuity": { "type": "array", "items": { "type": "string" } },
            "propagation": { "type": "array", "items": { "type": "string" } },
            "resonance": { "type": "array", "items": { "type": "string" } }
          }
        }
      }
    },

    "output": {
      "type": "object",
      "properties": {
        "execution_state": { "type": "string" }
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
    "runtime"
  ]
}
```
