# Changelog — `/docs/rtt/`

> RTT-Tech Root — the Resonance-Time Technology root module. Core substrates, engines, diagrams, examples, maps, and navigation surface for the full RTT module tree.

All notable changes to files in `/docs/rtt/` (root level, excluding child module subdirectories) are documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [1.1] — 2026-05-06

### Context

Metadata and session context refresh for the RTT root module infrastructure. Full 53-entry audit (trimmed — child modules audited separately). Manifest expanded from 2 to 49 file entries.

### Changed — `rtt-root_module.json` (Module Manifest)

- **`_meta`** — Added full module registry block (module, canonical_id, module_type, role, version, status, author, license, canonical_path, module_home, module_url, repository, last_updated).
- **`_session_context`** — Replaced old non-standard `session_context` with standardized `_session_context` block.
- **`_version_history`** — Added array with v1.0 and v1.1 entries.
- **`submodules`** — Populated from empty array to 5 entries:
  - `core/` (10 files — substrates and engines)
  - `diagrams/` (16 files — 8 paired .md + .svg)
  - `examples/` (9 files — domain applications)
  - `maps/` (8 files — cross-scale navigation)
  - `sort/` (9 files — sorting and index views, noted as trimmed from audit)
- **`files`** — Expanded from 2 to 49 entries. Added `purpose`, `role`, and `analyzer_layer` to all entries.
- **`cross_module_propagation.exports`** — Added core substrates list.
- **`module.purpose`** — Expanded to include file counts and child module listing.
- **Version** — Bumped from 1.0 → 1.1.

### Changed — `index.html` (Module Front Door)

- **Module identity block** — Added 13 meta tags previously missing (module, canonical-id, module-type, version, status, parent, siblings, canonical-path, last-updated, license, ai-ready, ai-module-id, ai-operators).
- **`last-modified`** — Updated from 2026-05-05 → 2026-05-06.
- **`ai.version`** — Updated from 1.0 → 1.1.
- **`citation_publication_date`** — Updated from `2025` → `2026-05-06` (renamed to `citation_date`).
- **`ai.module.summary`** — Updated with full file counts and child module listing.
- **`description`** — Expanded to include file counts and child module listing.
- **Session context** — `Modules` field updated from linear chain → `core (10) → diagrams (8 paired) → examples (9 domains) → maps (8 cross‑scale) → sort indexes`. Version updated to 1.1.
- **Badge div** — Updated to `📘 Resonance‑Time Technology Root · v1.1`.
- **All existing tags** — Preserved; reorganized with section comments.

### Not Changed — Content Files (43 files)

All content files pass clean — no metadata changes required:

| Section | Files | Roles | Status |
|---------|------:|-------|--------|
| `core/` | 10 | engine | ✅ all pass |
| `diagrams/*.md` | 8 | map | ✅ all pass |
| `diagrams/*.svg` | 8 | map | ✅ all pass |
| `examples/` | 9 | reference | ✅ all pass |
| `maps/` | 8 | map | ✅ all pass |

### Not Changed — Root Files

| File | Role | Status |
|------|------|--------|
| `README.md` | index | ✅ pass |
| `README_Doc_Index.md` | index | ✅ pass |
| `files.md` | reference | ✅ pass |
| `include.js` | engine | ✅ pass |

### Not Changed — DOC_MAP & Navigation

DOC_MAP has 54 entries (45 from this audit + 9 from `sort/`). No duplicate keys, no broken references, no missing entries. All hash links match DOC_MAP keys.

### Noted — Trimmed Submodules

The following child module directories are under `/docs/rtt/` but audited separately:

- `1/` — RTT/1
- `app/` — RTT-App
- `c64host/` — c64host
- `codes/` — RTT/codes ✅ (audited this session)
- `codex/` — RTT Codex
- `D369_Chip_Spec/` — D369 ✅ (audited this session)
- `Echo_Classifier/` — Echo Classifier
- `extension/` — Browser Extension
- `Harmonic_Stability_Profile/` — HSP
- `Inside/` — RTT/Inside
- `micro_core/` — Micro-Core
- `RTT_12/` — RTT-12
- `sdk/` — RTT-SDK
- `sort/` — Sorting & Indexes
- `store/` — RTT-Store
- `Substrate_Flow/` — Substrate Flow
- `The_Inverted_Star/` — The Inverted Star
- `Triadic_Echo_Lattice/` — Triadic Echo Lattice

---

## [1.0] — 2026-05-05

### Added

- `rtt-root_module.json` — Module manifest (2 file entries).
- `index.html` — Interactive reader with DOC_MAP (54 entries), full nav sidebar, MathJax support.
- `README.md` — Module front door.
- `README_Doc_Index.md` — Document index.
- `files.md` — File listing reference.
- `include.js` — Shared JavaScript utilities.
- `core/` — 10 core substrate and engine specifications.
- `diagrams/` — 8 paired diagram sets (.md + .svg).
- `examples/` — 9 domain-specific application examples.
- `maps/` — 8 cross-scale navigation maps.

---

## File Inventory

| Section | Files | Version | Role | Status |
|---------|------:|---------|------|--------|
| Root infrastructure | 6 | 1.1 | index/engine/reference | 2 refreshed, 4 pass |
| `core/` | 10 | 1.0 | engine | all pass |
| `diagrams/` | 16 | 1.0 | map | all pass |
| `examples/` | 9 | 1.0 | reference | all pass |
| `maps/` | 8 | 1.0 | map | all pass |
| `CHANGELOG.md` | — | — | — | this file |
| **Total** | **49 + 1** | | | |

---

*Maintained by: Nawder Loswin · TriadicFrameworks · MIT*

