# 🌑 **module.blank.json**  
### *Zero‑assumption, schema‑aligned starter template*

```json
{
  "$schema": "../../module.schema.json",
  "module": "my-module",
  "identity": "student.my-module",
  "purpose": "Blank starter module template with no assumptions.",

  "files": [],

  "operators": [],
  "dimensions": [],
  "regimes": [],
  "layers": [],

  "maps": [],
  "signatures": [],
  "diagnostics": [],
  "extensions": [],
  "examples": [],
  "references": [],
  "templates": [],

  "meta": {
    "notes": "This is the minimal blank module.json template."
  }
}
```

---

## Why this is the correct blank template  
- **No roles pre‑declared** — avoids accidental semantic commitments.  
- **All structural arrays empty** — operators, dimensions, regimes, layers.  
- **All file‑role arrays empty** — maps, signatures, diagnostics, etc.  
- **Schema‑aligned** — `$schema` points to your substrate module schema.  
- **Student‑safe** — no substrate‑level fields that imply behavior.  
- **Silent‑release compatible** — nothing that triggers runtime hooks.  
