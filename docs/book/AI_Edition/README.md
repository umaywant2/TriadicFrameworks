# TriadicFrameworks — AI Edition (Books 1–9)

This directory contains the **AI Edition** of the TriadicFrameworks canon — a nine‑book teaching arc designed for AI systems and advanced readers.  
Each book has its own folder and front‑door, with HTML metadata for AI parsing and a minimal README for human navigation.

## Books

### **Book 1 — Framework Field Theory (FFT)**
`/docs/book/AI_Edition/Book1_Framework_Field_Theory/`
- Live site: https://www.triadicframeworks.org/Framework_Field_Theory/AI_Edition/

### **Book 2 — The Inverted Star**
`/docs/book/AI_Edition/Book2_The_Inverted_Star/`
- Live site: https://www.triadicframeworks.org/rtt/The_Inverted_Star/AI_Edition/

### **Book 3 — Structural Detection**
`/docs/book/AI_Edition/Book3_Structural_Detection/`
- Live site: https://www.triadicframeworks.org/Structural_Detection/AI_Edition/

### **Book 4 — Opacity & Revelation**
`/docs/book/AI_Edition/Book4_Opacity_and_Revelation/`

### **Book 5 — TEL: Expression & Representation**
`/docs/book/AI_Edition/Book5_TEL_Expression_and_Representation/`

### **Book 6 — Governance & Regime Logic**
`/docs/book/AI_Edition/Book6_Governance_and_Regime_Logic/`

### **Book 7 — SARG: Structural Argumentation**
`/docs/book/AI_Edition/Book7_SARG_Structural_Argumentation/`

### **Book 8 — NoS: Nature of Structure**
`/docs/book/AI_Edition/Book8_NoS_Nature_of_Structure/`

### **Book 9 — Pattern Dynamics**
`/docs/book/AI_Edition/Book9_Pattern_Dynamics/`

Each book is designed to stand alone, with its own front‑door metadata, module.json manifest, and AI‑Edition structure.

---

## ✅ AI Edition — Books 1–9 File Generation Complete

### Files Generated Per Book

| Book | Folder | module.json | README.md |
|---|---|---|---|
| 1 — FFT | `Book1_FFT/` | ✅ | ✅ |
| 2 — Inverted Star | `Book2_Inverted_Star/` | ✅ | ✅ |
| 3 — Structural Detection | `Book3_Structural_Detection/` | ✅ | ✅ |
| 4 — Opacity & Revelation | `Book4_Opacity_Revelation/` | ✅ | ✅ |
| 5 — TEL | `Book5_TEL/` | ✅ | ✅ |
| 6 — Governance & Regime Logic | `Book6_Governance/` | ✅ | ✅ |
| 7 — SARG | `Book7_SARG/` | ✅ | ✅ |
| 8 — Nature of Structure | `Book8_NoS/` | ✅ | ✅ |
| 9 — Pattern Dynamics | `Book9_Pattern_Dynamics/` | ✅ | ✅ |

---

### What's in Each File

**`module.json`** — Full AI Edition manifest including:
- `book` block: id, number, title, abbreviation, edition, version, status
- `ai` block: module ID, version, purpose, keywords (10 per book), audience (5 types), full summary, dependency graph (`dependencies` + `unlocks`)
- `invariants` block: 4 named invariants per book with `INV-[CODE]-00N` identifiers + reference to invariants file
- `canonical_metadata`: domain, tier, reading order, prerequisite list, live site URL, last updated

**`README.md`** — Human-readable navigation including:
- Book purpose in plain language
- Chapter coverage table
- All 4 core invariants listed
- ASCII reading-order dependency tree (showing prerequisites → current book → what it unlocks)
- AI module metadata summary table
- Live site link

---

### Dependency Graph Summary

```
Book 1 (FFT) ──────────────────────────────────────────── Foundation
  ├── Book 2 (Inverted Star) ─────────────────────────── Topology
  ├── Book 3 (Structural Detection) ──────────────────── Methodology
  │     └── Book 4 (Opacity & Revelation) ─────────────── Epistemology
  │           └── Book 5 (TEL) ────────────────────────── Core Language
  │                 ├── Book 6 (Governance) ─────────────── Applied
  │                 │     └── Book 7 (SARG) ──────────────── Applied
  │                 │           └── Book 8 (NoS) ────────── Capstone
  │                 │                 └── Book 9 (PD) ───── Synthesis
```

