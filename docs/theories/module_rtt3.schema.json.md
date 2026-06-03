```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "RTT/3 Substrate Integration Schema",
  "description": "Schema for RTT/3 substrate-integration files across all TriadicFrameworks modules.",
  "type": "object",

  "properties": {
    "ai.module": {
      "type": "string",
      "description": "Module identifier (e.g., standard_model.rtt3)."
    },

    "ai.version": {
      "type": "string",
      "description": "Version of the RTT/3 substrate integration."
    },

    "substrate_integration": {
      "type": "array",
      "description": "List of substrate-level integration structures.",
      "items": {
        "type": "object",
        "properties": {
          "integration_name": {
            "type": "string",
            "description": "Name of the integration structure (e.g., substrate_resonance_map)."
          },
          "description": {
            "type": "string",
            "description": "Explanation of how this structure integrates the module with substrate-level behavior."
          },
          "imports": {
            "type": "array",
            "description": "List of substrate-level invariants or structures imported from deeper layers.",
            "items": { "type": "string" }
          },
          "exports": {
            "type": "array",
            "description": "List of structures this module provides to higher layers.",
            "items": { "type": "string" }
          },
          "regime_behavior": {
            "type": "object",
            "description": "Behavior of the integration structure across regimes R1–R4.",
            "properties": {
              "R1": { "type": "string" },
              "R2": { "type": "string" },
              "R3": { "type": "string" },
              "R4": { "type": "string" }
            },
            "required": ["R1", "R2", "R3", "R4"]
          },
          "coherence_constraints": {
            "type": "array",
            "description": "List of constraints required to maintain coherence.",
            "items": { "type": "string" }
          },
          "drift_boundary": {
            "type": "string",
            "description": "Description of conceptual drift to avoid."
          }
        },
        "required": [
          "integration_name",
          "description",
          "imports",
          "exports",
          "regime_behavior",
          "coherence_constraints",
          "drift_boundary"
        ]
      }
    },

    "notes": {
      "type": "string",
      "description": "Additional notes for RTT/3 reasoning."
    }
  },

  "required": ["ai.module", "ai.version", "substrate_integration"]
}
```
