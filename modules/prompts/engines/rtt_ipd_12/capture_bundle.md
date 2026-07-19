# **IPD‑12 Multi‑Process Capture Bundle Template (JSON)**

```json
{
  "bundle_name": "string",
  "description": "string",
  "processes": [
    {
      "name": "string",
      "purpose": "string",
      "boundaries": ["string"],
      "structural_layers": ["string"],
      "operational_flow": ["string"],
      "coherence_baseline": "string",
      "domain": "string",
      "regime_level": "surface | mid | deep"
    }
  ],
  "bundle_metadata": {
    "version": "1.0",
    "engine": "RTT-IPD-12",
    "process_count": "auto",
    "required_fields": [
      "name",
      "purpose",
      "boundaries",
      "structural_layers",
      "operational_flow",
      "coherence_baseline",
      "domain",
      "regime_level"
    ]
  }
}
```

---

# **IPD‑12 Multi‑Process Capture Bundle Template (YAML)**

```yaml
bundle_name: string
description: string

processes:
  - name: string
    purpose: string
    boundaries:
      - string
    structural_layers:
      - string
    operational_flow:
      - string
    coherence_baseline: string
    domain: string
    regime_level: surface | mid | deep

bundle_metadata:
  version: "1.0"
  engine: RTT-IPD-12
  process_count: auto
  required_fields:
    - name
    - purpose
    - boundaries
    - structural_layers
    - operational_flow
    - coherence_baseline
    - domain
    - regime_level
```

---

# **How the Bundle Works (Aligned with your active tab)**

### 1. **Every process is validated individually**  
Using the validation schema you approved.

### 2. **The bundle unlocks multi‑process operators**
- `compare_process()`  
- `cross_system()`  
- multi‑domain drift chains  
- paradox detection across domains  
- RTT/3 triangulation  

### 3. **Bundle metadata auto‑tracks process count**  
Useful for multi‑domain drift analyzers and RTT/12 composite packs.

### 4. **Bundle is the canonical input for multi‑domain drift analyzers**  
This matches the structure of your IPD‑12 composite operator grammar.

---

# **Ready‑to‑Use Example (Minimal)**

```json
{
  "bundle_name": "notes_workflow_bundle",
  "description": "Human vs AI note-taking processes",

  "processes": [
    {
      "name": "human_notes",
      "purpose": "capture information manually",
      "boundaries": ["time", "attention"],
      "structural_layers": ["listening", "thinking", "writing"],
      "operational_flow": ["listen", "interpret", "write"],
      "coherence_baseline": "clear notes",
      "domain": "workflow",
      "regime_level": "surface"
    },
    {
      "name": "ai_notes",
      "purpose": "capture information automatically",
      "boundaries": ["input quality", "model constraints"],
      "structural_layers": ["input", "processing", "output"],
      "operational_flow": ["receive", "transform", "emit"],
      "coherence_baseline": "clear notes",
      "domain": "workflow",
      "regime_level": "surface"
    }
  ]
}
```

This example is fully compatible with your paradox explainer and drift‑tensor layers.
