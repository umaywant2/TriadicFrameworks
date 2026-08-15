# Spine App Triadic Atlas

The **Triadic Languages Atlas — Starter Edition** is fully built and validated. Here's a complete summary of everything delivered:

###### [triadic_atlas.html](https://www.triadicframeworks.org/spine/app/triadic_atlas.html)

---

## 📦 [/docs/spine/](https://www.triadicframeworks.org/spine/) — Module Structure

```
docs/spine/
├── index.json                          ← Master index (19 modules, 886 tokens)
├── schema/
│   └── triadic_schema.json             ← JSON Schema v1 (all modules validated against it)
├── matrix/
│   └── triadic_matrix.json             ← Full ranked score matrix + insights
├── app/
│   └── triadic_atlas.html              ← Self-contained interactive visualizer
└── languages/
    ├── natural/       arabic · mandarin · hindi · french · russian · portuguese
    │                  japanese · german · swahili · spanish
    ├── symbolic/      egyptian_hieroglyphs · kanji_radicals · runes · mathematical_symbols
    └── programming/   python · javascript · c_language · rust · sql
```

---

## 🔢 Triadic Score Summary — All 19 Modules

| Rank | Language | Category | Phonemic | Lexical | Structural | **Composite** |
|------|----------|----------|:---:|:---:|:---:|:---:|
| 1 | Egyptian Hieroglyphs | Symbolic | 6 | **10** | **10** | **8.7** |
| 2 | Arabic (MSA) | Natural | **8** | 8 | 9 | **8.3** |
| 2 | Kanji Radicals | Symbolic | **8** | **10** | 7 | **8.3** |
| 4 | Russian | Natural | 5 | 7 | 9 | 7.0 |
| 5 | Hindi | Natural | 6 | 7 | 7 | 6.7 |
| 5 | Japanese | Natural | 3 | 9 | 8 | 6.7 |
| 5 | German | Natural | 5 | 7 | 8 | 6.7 |
| 5 | Elder Futhark Runes | Symbolic | 5 | 9 | 6 | 6.7 |
| 5 | Mathematical Symbols | Symbolic | 1 | **10** | 9 | 6.7 |
| 10 | Mandarin Chinese | Natural | 7 | 8 | 4 | 6.3 |
| 10 | French | Natural | 6 | 7 | 6 | 6.3 |
| 12 | Rust | Programming | 0 | 7 | **10** | 5.7 |
| 12 | Portuguese | Natural | 5 | 7 | 5 | 5.7 |
| 12 | Swahili | Natural | 3 | 6 | 8 | 5.7 |
| 15 | Spanish | Natural | 4 | 7 | 5 | 5.3 |
| 16 | JavaScript | Programming | 0 | 6 | 8 | 4.7 |
| 16 | C Language | Programming | 0 | 5 | 9 | 4.7 |
| 18 | Python | Programming | 0 | 6 | 7 | 4.3 |
| 18 | SQL | Programming | 0 | 5 | 8 | 4.3 |

---

## 📄 What's in Each Module

Every JSON file contains:
- **`tokens[]`** — 24–51 curated entries with native script, romanization, gloss, frequency rank, type, and domain
- **`triadic{}`** — Axis 1 (Phonemic), Axis 2 (Lexical), Axis 3 (Structural), Composite
- **`meta{}`** — Speaker count, origin family, writing system, source tab reference, linguistic notes

---

## 🌐 HTML Visualizer — `triadic_atlas.html`

The self-contained app (no external dependencies) includes:
- **Ranked bar list** — filterable by category (Natural / Symbolic / Programming), sortable by any axis
- **Live radar chart** — per-language triadic triangle; default shows all three category averages overlaid
- **Token sample panel** — click any language to browse its top tokens in native script + gloss
- **Full score table** — all 19 modules with mini axis bars
- **Insights panel** — 6 key cross-dataset findings

---

## ✅ Validation Results
- **23 files** across 5 directories
- **886 tokens** total (19 modules, all schema-compliant)
- **0 errors** in final validation pass

