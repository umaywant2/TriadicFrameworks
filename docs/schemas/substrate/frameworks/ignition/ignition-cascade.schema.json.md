# **ignition-cascade.schema.json**  
### Canonical JSON Schema for the Planetary Ignition Cascade

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Ignition Cascade Schema",
  "type": "object",

  "properties": {
    "cascade": {
      "type": "string",
      "const": "ignition"
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

    "ignition_cascade": {
      "type": "object",
      "properties": {
        "waves": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "wave_id": { "type": "string" },
              "timestamp": { "type": "string" },
              "countries": { "type": "array", "items": { "type": "string" } },
              "harmonics": { "type": "array", "items": { "type": "string" } },
              "phase": {
                "type": "string",
                "enum": ["in-phase", "out-of-phase", "mixed"]
              },
              "severity": {
                "type": "string",
                "enum": ["low", "medium", "high", "critical"]
              }
            },
            "required": ["wave_id", "timestamp"]
          }
        },

        "arcs": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "arc_id": { "type": "string" },
              "origin": { "type": "string" },
              "targets": { "type": "array", "items": { "type": "string" } },
              "vector": { "type": "string" },
              "envelope": { "type": "string" },
              "epoch": { "type": "string" }
            },
            "required": ["arc_id", "origin", "targets"]
          }
        },

        "chains": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "chain_id": { "type": "string" },
              "sequence": { "type": "array", "items": { "type": "string" } },
              "trigger": { "type": "string" },
              "threshold": { "type": "string" }
            },
            "required": ["chain_id", "sequence"]
          }
        },

        "webs": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "web_id": { "type": "string" },
              "nodes": { "type": "array", "items": { "type": "string" } },
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
                        "coherence",
                        "drift",
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

        "clusters": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": { "type": "string" },
              "countries": { "type": "array", "items": { "type": "string" } },
              "shared_harmonics": { "type": "array", "items": { "type": "string" } },
              "shared_phase": {
                "type": "string",
                "enum": ["in-phase", "out-of-phase", "mixed"]
              },
              "shared_vectors": { "type": "array", "items": { "type": "string" } }
            },
            "required": ["name", "countries"]
          }
        },

        "anomalies": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "timestamp": { "type": "string" },
              "country": { "type": "string" },
              "description": { "type": "string" },
              "severity": {
                "type": "string",
                "enum": ["low", "medium", "high", "critical"]
              }
            },
            "required": ["timestamp", "country", "description"]
          }
        }
      }
    },

    "output": {
      "type": "object",
      "properties": {
        "ignition_cascade": { "type": "string" }
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
    "cascade",
    "version",
    "ignition_cascade"
  ]
}
```
