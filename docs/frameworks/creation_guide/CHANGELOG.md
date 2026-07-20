# Changelog — `/docs/frameworks/creation_guide/`

> Framework Creation Guide (FCG) — structural grammar for designing coherent, minimal, regime‑aware frameworks.

All notable changes to files in `/docs/frameworks/creation_guide/` are documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [1.1] — 2026-05-06

### Context

Metadata and session context refresh across the FCG module infrastructure files, aligning with the standardized TriadicFrameworks module template (D369 convention).

### Changed — `FCG_module.json` (Module Manifest)

- **`_meta`** — Added full module registry block (module, canonical_id, module_type, role, version, status, author, license, canonical_path, module_home, module_url, repository, last_updated).
- **`_session_context`** — Added standardized 9-field session context block.
- **`_version_history`** — Added array with v1.0 and v1.1 entries.
- **`structural_grammar`** — Added dimensional (D0–D5), regime (R0–R3), coherence (C0–C3), drift, and regime sensitivity envelopes.
- **`cross_module_propagation`** — Added imports (RTT/1 operators, SARG structural grammar, FFT field theory) and exports (6 FCG operators, framework structural grammar, RF-Builder submodule, regime design patterns).
- **`submodules`** — Added RF-Builder declaration with path and purpose.
- **`module.siblings`** — Added explicit array: FFT, SARG, Mode.
- **`files`** — Expanded from 12 to 22 entries:
  - Added 7 paired HTML renderers (history, principles, models, structure, operators, regimes, generator).
  - Added `fft.html` (FFT integration page).
  - Added `guide.html` (consolidated guide view).
  - Added `RF-Builder/RF-Builder.html` (interactive builder tool).
  - Added `FCG_module.json` (self-reference).
  - Added `purpose` field to all 22 file entries.
  - Added `analyzer_layer` to all new entries.
- **Version** — Bumped from 1.0 → 1.1.

### Changed — `index.html` (Module Front Door)

- **Module identity block** — Added 13 meta tags previously missing:
  - `module`, `canonical-id`, `module-type`, `version`, `status`, `parent`, `siblings`, `canonical-path`, `last-updated`, `license`, `ai-ready`, `ai-module-id`, `ai-operators`.
- **`last-modified`** — Updated from 2026-05-02 → 2026-05-06.
- **`ai.version`** — Updated from 1.0 → 1.1.
- **`citation_date`** — Updated from 2026 → 2026-05-06.
- **Session context block** — Version updated from 1.0 (fcg‑stable) → 1.1 (fcg‑refreshed).
- **Badge div** — Updated to `📐 Structural Grammar · v1.1`.
- **All existing tags** — Preserved; reorganized with section comments for readability.

### Not Changed

- All 7 markdown content files (history, principles, models, structure, operators, regimes, generator) — pass clean.
- `capture.md` — pass clean.
- `README.md` — pass clean.
- All 7 paired HTML renderers — content unchanged (manifest inclusion only).
- `fft.html`, `guide.html` — content unchanged (manifest inclusion only).
- `RF-Builder/RF-Builder.html` — content unchanged (manifest inclusion only).
- `RF-Builder/RF-Builder_capture.md` — pass clean.
- `RF-Builder/diagrams/rf-builder-mermaid.md` — pass clean.
- DOC_MAP, nav sidebar, CSS, script block — all unchanged.

---

## [1.0] — 2026-05-02

### Added

- `README.md` — Module front door with purpose, module map, triadic structural overview.
- `index.html` — Interactive reader with sidebar nav, markdown rendering, DOC_MAP.
- `capture.md` — Capture document and lineage root.
- `history.md` — FCG Core Layer 1: evolution of frameworks.
- `principles.md` — FCG Core Layer 2: universal design principles.
- `models.md` — FCG Core Layer 3: internal structure and identity.
- `structure.md` — FCG Core Layer 4: framework backbone and components.
- `operators.md` — FCG Core Layer 5: actions and transformations.
- `regimes.md` — FCG Core Layer 6: coherent modes of operation.
- `generator.md` — FCG Core Layer 7: procedural framework engine.
- `fft.html` — Framework Field Theory integration page.
- `guide.html` — Consolidated single-page guide view.
- `FCG_module.json` — Module manifest (12 file entries).
- `RF-Builder/RF-Builder.html` — Resonance Framework Builder tool.
- `RF-Builder/RF-Builder_capture.md` — RF-Builder capture document.
- `RF-Builder/diagrams/rf-builder-mermaid.md` — RF-Builder Mermaid diagrams.
- 7 paired HTML renderers (history, principles, models, structure, operators, regimes, generator).

---

## File Inventory

| File | Version | Role | Status |
|------|---------|------|--------|
| `README.md` | 1.0 | index | pass |
| `index.html` | 1.1 | index | refreshed |
| `capture.md` | 1.0 | reference | pass |
| `history.md` | 1.0 | reference | pass |
| `history.html` | 1.0 | index | pass (added to manifest) |
| `principles.md` | 1.0 | engine | pass |
| `principles.html` | 1.0 | index | pass (added to manifest) |
| `models.md` | 1.0 | engine | pass |
| `models.html` | 1.0 | index | pass (added to manifest) |
| `structure.md` | 1.0 | engine | pass |
| `structure.html` | 1.0 | index | pass (added to manifest) |
| `operators.md` | 1.0 | engine | pass |
| `operators.html` | 1.0 | index | pass (added to manifest) |
| `regimes.md` | 1.0 | engine | pass |
| `regimes.html` | 1.0 | index | pass (added to manifest) |
| `generator.md` | 1.0 | engine | pass |
| `generator.html` | 1.0 | index | pass (added to manifest) |
| `fft.html` | 1.0 | reference | pass (added to manifest) |
| `guide.html` | 1.0 | reference | pass (added to manifest) |
| `RF-Builder/RF-Builder.html` | 1.0 | engine | pass (added to manifest) |
| `RF-Builder/RF-Builder_capture.md` | 1.0 | reference | pass |
| `RF-Builder/diagrams/rf-builder-mermaid.md` | 1.0 | map | pass |
| `FCG_module.json` | 1.1 | index | refreshed |
| `CHANGELOG.md` | — | — | this file |

---

*Maintained by: Nawder Loswin · TriadicFrameworks · MIT*

