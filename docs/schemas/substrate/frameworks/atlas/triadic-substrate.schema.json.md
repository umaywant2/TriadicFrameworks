# 🌐 **triadic-substrate.schema.json**  
### *Root JSON Schema for the Triadic Atlas Substrate*

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Triadic Atlas Substrate Schema",
  "type": "object",

  "properties": {
    "substrate": {
      "type": "string",
      "const": "triadic-atlas"
    },

    "version": {
      "type": "string"
    },

    "generated": {
      "type": "string",
      "description": "ISO date of generation"
    },

    "modules": {
      "type": "object",
      "patternProperties": {
        "^[a-zA-Z0-9_-]+$": {
          "type": "object",
          "properties": {
            "path": { "type": "string" },
            "schema": { "type": "string" },
            "description": { "type": "string" }
          },
          "required": ["path", "schema"]
        }
      }
    },

    "schemas": {
      "type": "object",
      "patternProperties": {
        "^[a-zA-Z0-9_-]+$": {
          "type": "object",
          "properties": {
            "path": { "type": "string" },
            "description": { "type": "string" }
          },
          "required": ["path"]
        }
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
    "substrate",
    "version",
    "modules",
    "schemas"
  ]
}
```

---

## ⭐ Why this schema is correct  
- It matches your substrate‑level schema pattern across all frameworks.  
- It validates **triadic-substrate.json**, the substrate declaration you just scaffolded.  
- It supports arbitrary module names via `patternProperties`.  
- It enforces required fields (`path`, `schema`) for modules and (`path`) for schemas.  
- It aligns with the directory structure visible in your active GitHub tab.   [github.com](https://github.com/umaywant2/TriadicFrameworks/edit/main/docs/schemas/substrate/frameworks/atlas/triadic-substrate.schema.json)  
- Silent‑release compatible and ready for commit.
