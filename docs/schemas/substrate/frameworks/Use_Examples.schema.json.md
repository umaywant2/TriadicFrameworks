This schema aligns with:

- **Use_Examples.json**  
- **Use_Examples.md**  
- the entire substrate frameworks directory  
- your module templates  
- your runtime constellation  
- your triadic execution + monitor pipeline  

Below is the **ready‑to‑paste canonical schema**, fully aligned with your TriadicFrameworks grammar.

---

# **Use_Examples.schema.json**  
### *Canonical JSON Schema for the Triadic Substrate Usage Examples Registry*

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Triadic Substrate Use Examples Schema",
  "type": "object",

  "properties": {
    "registry": {
      "type": "string",
      "const": "triadic-substrate-use-examples"
    },

    "version": {
      "type": "string"
    },

    "generated": {
      "type": "string",
      "description": "ISO date of generation"
    },

    "examples": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique identifier for the example"
          },

          "category": {
            "type": "string",
            "enum": [
              "atlas",
              "ignition",
              "epoch",
              "continuity",
              "invariance",
              "execution",
              "monitor",
              "modules",
              "constellation",
              "substrate"
            ]
          },

          "description": {
            "type": "string",
            "description": "Human-readable description of the example"
          },

          "inputs": {
            "type": "object",
            "description": "Input fields required to run the example",
            "additionalProperties": true
          },

          "outputs": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Expected outputs or behaviors"
          }
        },

        "required": ["id", "category", "description", "inputs", "outputs"]
      }
    },

    "meta": {
      "type": "object",
      "properties": {
        "notes": {
          "type": "string"
        }
      }
    }
  },

  "required": ["registry", "version", "examples"]
}
```

---

### ✔️ This schema is fully aligned with your Use_Examples.json  
It validates:

- category enums  
- example structure  
- input/output flexibility  
- canonical registry metadata  

Your substrate frameworks directory now has:

- **Use_Examples.md**  
- **Use_Examples.json**  
- **Use_Examples.schema.json**  
- **Use_Examples.extended.md**

All four layers of the usage‑example system.
