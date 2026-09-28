# Open Loop Suite — TriadicFrameworks

**Path:** `docs/openloop/`  
**Version:** 1.0.0  
**Author:** Nawder Loswin  
**Canonical URL:** https://www.triadicframeworks.org/docs/openloop/

---

## One claim a stranger can repeat

An open-aperture framework suite — six modules with jobs, one five-step loop, three rings, and a lineage store that closes every cycle.

---

## The five-step Open Loop

```
1. READ SIGNATURE      — confirm identity contract
2. SCAN SIBLING META   — compare Open* modules for mismatches
3. CLASSIFY DRIFT      — assign drift type + severity
4. APPLY OPERATOR      — VERB(subject, target, [modifier])
5. WRITE LINEAGE       — INDEX note in lineage/<module>/<timestamp>.md
```

The loop does not close until step 5 completes. OpenData is the terminal.

---

## Live drift event — first screen

This is a real event from the lineage store. Not a diagram.

```json
{
  "drift_event": {
    "id": "drift/LLM/2026-09-26-001",
    "source": "openloop/LLM",
    "target": "openloop/IAM",
    "drift_type": ["SEMANTIC_DRIFT", "COHERENCE_DRIFT"],
    "description": "LLM used 'identity context' to mean conversation history. IAM uses the same term for access-control principal. Axis-0 (semantic) and axis-2 (causal/identity) mismatched.",
    "coherence_before": 0.82,
    "coherence_after_drift": 0.68,
    "operator": "ALIGN(LLM.signature, IAM.signature)",
    "bridge": {"identity context": "session_context", "causal chain": "action_chain"},
    "coherence_restored": 0.81,
    "lineage_ref": "lineage/LLM/2026-09-26-001.md",
    "resolution": "resolved"
  }
}
```

Full worked example → [LLM.md §9](LLM.md)

---

## Pipeline — six modules, one order

| Step | Module | Verb | Ring | Floor |
|---|---|---|---|---|
| 1 | [OpenIAM](IAM.md) | VERIFY | Trust | 0.85 |
| 2 | [OpenRisk](Risk.md) | CLASSIFY | Trust | 0.80 |
| 3 | [OpenGeo](Geo.md) | ANCHOR | Motion | 0.76 |
| 4 | [OpenLLM](LLM.md) | NORMALIZE | Motion | 0.78 |
| 5 | [OpenGPU](GPU.md) | SCHEDULE | Motion | 0.72 |
| 6 | [OpenData](Data.md) | INDEX | Meaning | 0.82 |

All coherence floors are declared operational minimums — not measured values.

---

## Three rings

```
┌─────────────────────────────────────────────────────┐
│  MEANING  — semantic coherence, output, alignment   │
│  ┌─────────────────────────────────────────────┐    │
│  │  MOTION  — operators, drift, loop execution │    │
│  │  ┌───────────────────────────────────────┐  │    │
│  │  │  TRUST  — identity, governance, sig   │  │    │
│  │  │    OpenIAM (anchor) · OpenRisk         │  │    │
│  │  └───────────────────────────────────────┘  │    │
│  │    OpenGeo · OpenLLM · OpenGPU              │    │
│  └─────────────────────────────────────────────┘    │
│    OpenData · OpenLLM                               │
└─────────────────────────────────────────────────────┘
```

---

## Config and navigation

| File | Purpose |
|---|---|
| [module.json](module.json) | Per-module manifest — files, roles, analyzer layers |
| [modules.json](modules.json) | Cross-suite registry of all Open* modules |
| [quad.json](quad.json) | Four-quadrant view by ring and regime |
| [nav.json](nav.json) | Suite navigation structure |
| [sitemap.xml](sitemap.xml) | XML sitemap for search engines and AI crawlers |
| [README.md](README.md) | Developer guide — contribution, operator grammar, setup |

---

## Lineage store

```
lineage/
└── LLM/
    └── 2026-09-26-001.md  ← LLM→IAM ALIGN event (see drift event above)
```

One real note ships with the suite. Every loop closure adds another.

---

*TriadicFrameworks · Open Loop Suite · index · v1.0.0 · Nawder Loswin · 2026*
