# ✅ **`sarg.schema.json` (commit‑ready)**

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "SARG Object",
  "description": "Substrate-Agnostic Resonance Grammar (SARG) minimal data model.",
  "type": "object",

  "properties": {
    "substrate": {
      "type": "object",
      "description": "The domain carrying structure.",
      "properties": {
        "type": { "type": "string" },
        "description": { "type": "string" },
        "domain": { "type": "string" },
        "notes": { "type": "string" }
      },
      "required": ["type", "description", "domain"]
    },

    "lens": {
      "type": "object",
      "description": "The operator used to read or transform the substrate.",
      "properties": {
        "type": { "type": "string" },
        "variant": { "type": "string" },
        "notes": { "type": "string" }
      },
      "required": ["type"]
    },

    "invariants": {
      "type": "object",
      "description": "Stable features that persist across transformations.",
      "properties": {
        "vertical": {
          "type": "array",
          "items": { "type": "string" }
        },
        "horizontal": {
          "type": "array",
          "items": { "type": "string" }
        },
        "dual": {
          "type": "array",
          "items": { "type": "string" }
        }
      }
    },

    "resonance": {
      "type": "object",
      "description": "Mapping to universal anchors (● ○ × |) or resonance families.",
      "properties": {
        "anchors": {
          "type": "array",
          "items": { "type": "string" }
        },
        "family": { "type": "string" },
        "notes": { "type": "string" }
      }
    }
  },

  "required": ["substrate", "lens", "invariants", "resonance"]
}
```

---

# 🧩 Why this schema is correct for SARG

It matches the **exact four‑layer structure** defined in your Capture.md:

1. **Substrate**  
2. **Lens**  
3. **Invariants**  
4. **Resonance Mapping**

It also aligns with:

- the Latin alphabet example  
- the lostational supsphere atom example  
- the substrate files you just created  
- the README you committed  
- the overall grammar you’re building  

This schema is intentionally **minimal** so the grammar stays lightweight and extensible.
