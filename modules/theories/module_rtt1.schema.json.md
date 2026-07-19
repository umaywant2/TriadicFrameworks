```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "RTT/1 Operator Grammar Schema",
  "description": "Schema for RTT/1 operator grammar files across all TriadicFrameworks modules.",
  "type": "object",

  "properties": {
    "ai.module": {
      "type": "string",
      "description": "Module identifier (e.g., standard_model.rtt1)."
    },

    "ai.version": {
      "type": "string",
      "description": "Version of the RTT/1 operator grammar."
    },

    "operators": {
      "type": "array",
      "description": "List of operators defined in RTT/1.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Operator name (e.g., excitation_operator)."
          },
          "type": {
            "type": "string",
            "enum": [
              "mode_operator",
              "interaction_operator",
              "structure_operator",
              "mass_operator",
              "boundary_operator",
              "stability_operator",
              "classification_operator",
              "variation_operator",
              "sector_operator"
            ],
            "description": "Operator category."
          },
          "signals": {
            "type": "array",
            "description": "Signals associated with the operator.",
            "items": { "type": "string" }
          },
          "regime_behavior": {
            "type": "object",
            "description": "Behavior of the operator across regimes R1–R4.",
            "properties": {
              "R1": { "type": "string" },
              "R2": { "type": "string" },
              "R3": { "type": "string" },
              "R4": { "type": "string" }
            },
            "required": ["R1", "R2", "R3", "R4"]
          },
          "drift_boundary": {
            "type": "string",
            "description": "Description of conceptual drift to avoid."
          }
        },
        "required": ["name", "type", "signals", "regime_behavior", "drift_boundary"]
      }
    },

    "notes": {
      "type": "string",
      "description": "Additional notes for RTT/1 reasoning."
    }
  },

  "required": ["ai.module", "ai.version", "operators"]
}
```
