# 🜂 **module.regimes.json**  
### *Canonical module‑regimes template — structural regime grammar*

```json
{
  "$schema": "../../module.schema.json",
  "module": "my-regimes-module",
  "identity": "student.my-regimes-module",
  "purpose": "Defines structural regimes for module architecture, including drift, coherence, stability, resonance, epoch, and ignition regimes.",

  "files": [
    {
      "name": "README.md",
      "role": "profile"
    },
    {
      "name": "drift-regime.md",
      "role": "map"
    },
    {
      "name": "coherence-regime.md",
      "role": "map"
    },
    {
      "name": "stability-regime.md",
      "role": "map"
    },
    {
      "name": "resonance-regime.md",
      "role": "map"
    },
    {
      "name": "epoch-regime.md",
      "role": "map"
    },
    {
      "name": "ignition-regime.md",
      "role": "map"
    }
  ],

  "regimes": {
    "drift": {
      "fields": ["string"],
      "rules": ["string"]
    },
    "coherence": {
      "fields": ["string"],
      "rules": ["string"]
    },
    "stability": {
      "fields": ["string"],
      "rules": ["string"]
    },
    "resonance": {
      "fields": ["string"],
      "rules": ["string"]
    },
    "epoch": {
      "fields": ["string"],
      "rules": ["string"]
    },
    "ignition": {
      "fields": ["string"],
      "rules": ["string"]
    }
  },

  "operators": [
    {
      "name": "regime-define",
      "description": "Define a new structural regime for the module.",
      "example": "Define drift regime → drift-regime.md"
    },
    {
      "name": "regime-extend",
      "description": "Extend an existing regime with module-specific fields.",
      "example": "Extend coherence regime → coherence-regime.md"
    },
    {
      "name": "regime-bind",
      "description": "Bind module regimes to substrate structural engines.",
      "example": "Bind stability regime → stability-regime.md"
    }
  ],

  "output": {
    "regimes_template": "./module.regimes.json"
  },

  "meta": {
    "notes": "Structural regime grammar for module-level regime declarations."
  }
}
```

---

## Why this is the correct regimes template  
- Mirrors your **TriadicFrameworks structural grammar** exactly.  
- Includes all six canonical regime types: drift, coherence, stability, resonance, epoch, ignition.  
- Uses **map‑role files** for each regime.  
- Includes **operators** for define / extend / bind.  
- Fully **schema‑aligned**, silent‑release compatible, and ready for commit.  
