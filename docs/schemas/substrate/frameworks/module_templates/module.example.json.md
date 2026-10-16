# 🌟 **module.example.json**  
### *Minimal working example module.json (canon‑aligned)*

```json
{
  "$schema": "../../module.schema.json",
  "module": "example-module",
  "identity": "student.example-module",
  "purpose": "A minimal working example showing the canonical module.json pattern.",

  "files": [
    {
      "name": "README.md",
      "role": "profile"
    },
    {
      "name": "example-map.md",
      "role": "map"
    },
    {
      "name": "example-signature.md",
      "role": "signature"
    },
    {
      "name": "example-diagnostic.md",
      "role": "diagnostic"
    },
    {
      "name": "example-extension.md",
      "role": "extension"
    }
  ],

  "operators": [
    {
      "name": "example-operator",
      "description": "A simple operator demonstrating the operator grammar.",
      "example": "Apply example-operator → example-map.md"
    }
  ],

  "dimensions": [
    "example-dimension"
  ],

  "regimes": [
    "example-regime"
  ],

  "layers": [
    "example-layer"
  ],

  "maps": [
    "example-map.md"
  ],

  "signatures": [
    "example-signature.md"
  ],

  "diagnostics": [
    "example-diagnostic.md"
  ],

  "extensions": [
    "example-extension.md"
  ],

  "examples": [
    "example-usage.md"
  ],

  "references": [
    "example-reference.md"
  ],

  "templates": [
    "example-template.md"
  ],

  "meta": {
    "notes": "Minimal example module.json demonstrating canonical structure."
  }
}
```

---

## Why this is the correct example template  
- Shows **every major role** (profile, map, signature, diagnostic, extension).  
- Includes **one of each structural field** (operator, dimension, regime, layer).  
- Demonstrates **canonical file naming** and **role assignment**.  
- Fully **schema‑aligned** with your substrate module schema.  
- Clean, minimal, and **student‑safe**.  
- Perfect as a teaching or reference module.
