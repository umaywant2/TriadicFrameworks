# **resonance-drift-coupling.schema.json**  
### *Root JSON Schema for the Resonance–Drift Coupling Regulator*

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Resonance–Drift Coupling Schema",
  "type": "object",

  "properties": {
    "regulator": {
      "type": "string",
      "const": "resonance-drift-coupling"
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

    "coupling": {
      "type": "object",
      "properties": {
        "strength": {
          "type": "object",
          "properties": {
            "min": { "type": "number" },
            "max": { "type": "number" },
            "default": { "type": "number" },
            "rules": {
              "type": "array",
              "items": { "type": "string" }
            }
          },
          "required": ["min", "max", "default"]
        },

        "phase_relation": {
          "type": "object",
          "properties": {
            "modes": {
              "type": "array",
              "items": {
                "type": "string",
                "enum": ["in-phase", "out-of-phase", "mixed"]
              }
            },
            "allowed_transitions": {
              "type": "array",
              "items": { "type": "string" }
            },
            "correction_rules": {
              "type": "array",
              "items": { "type": "string" }
            }
          },
          "required": ["modes"]
        },

        "magnitude_relation": {
          "type": "object",
          "properties": {
            "drift_limits": {
              "type": "array",
              "items": { "type": "string" }
            },
            "resonance_limits": {
              "type": "array",
              "items": { "type": "string" }
            },
            "surge_prevention": {
              "type": "array",
              "items": { "type": "string" }
            }
          }
        },

        "epochal_profiles": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "epoch": {
                "type": "string",
                "enum": ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7"]
              },
              "coupling_mode": { "type": "string" },
              "conditions": {
                "type": "array",
                "items": { "type": "string" }
              },
              "actions": {
                "type": "array",
                "items": { "type": "string" }
              }
            },
            "required": ["epoch", "coupling_mode"]
          }
        }
      },
      "required": ["strength", "phase_relation"]
    },

    "regulation_rules": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "rule": { "type": "string" },
          "conditions": {
            "type": "array",
            "items": { "type": "string" }
          },
          "effects": {
            "type": "array",
            "items": { "type": "string" }
          },
          "constraints": {
            "type": "array",
            "items": { "type": "string" }
          }
        },
        "required": ["rule"]
      }
    },

    "output": {
      "type": "object",
      "properties": {
        "resonance_drift_coupling": { "type": "string" }
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
    "regulator",
    "version",
    "coupling",
    "regulation_rules"
  ]
}
```

---

## Why this schema is correct  
- Matches the structure of your existing **resonance-drift-coupling.json** instance.  
- Aligns with your **coupling-profiles.json** and **coupling-evaluator.json**.  
- Uses canonical substrate grammar: strength, phase, magnitude, epochal profiles, regulation rules.  
- Fully compatible with the empty file in your active tab.  
- Silent‑release ready.
