# 🔧 Tightened RTTcode Schema (experiment IDs, seeds, lineage)
Below is a drop‑in upgrade to the RTTcode v1.0 schema.

It adds:
- experiment_id — globally unique experiment lineage
- seed — deterministic RNG seed for reproducibility
- trial — optional sub‑run index
- tags — arbitrary labels for grouping
- provenance — where this packet came from (engine, version, user, etc.)

All additions are optional but strongly recommended for research, debugging, and reviewer reproducibility.

## How it fits into the full schema
You simply add "experiment" to the top‑level properties and optionally to required if you want strict reproducibility.

```json
"properties": {
  "rtt_version": {...},
  "tick": {...},
  "entities": {...},
  "environment": {...},
  "intent": {...},
  "experiment": { "$ref": "#/$defs/experiment" }
}
```

This keeps RTTcode clean, extensible, and reviewer‑friendly.
