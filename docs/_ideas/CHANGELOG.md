# Changelog — `/docs/_ideas/`

> Ideas Sandbox — non-canonical cooker for prototypes, sketches, drafts, and early-stage concepts.

All notable changes to infrastructure files in `/docs/_ideas/` are documented in this file.
Individual idea files are not tracked here — the sandbox is a living workspace.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [1.1] — 2026-05-06

### Context

Metadata and session context refresh for the sandbox infrastructure. Census taken of all 288 entries. Promotion history documented for recently graduated articles.

### Census

| Type | Count |
|------|------:|
| Markdown (.md) | 219 |
| HTML (.html) | 39 |
| JSON (.json) | 10 |
| Python (.py) | 3 |
| PDF (.pdf) | 2 |
| ZIP (.zip) | 2 |
| SVG (.svg) | 4 |
| Other | 3 |
| Directories | 6 |
| **Total** | **288** |

### Changed — `_ideas_module.json` (Module Manifest)

- **`_meta`** — Added full module registry block with census_note documenting 288-entry inventory.
- **`_session_context`** — Replaced old `session_context` with standardized `_session_context` block.
- **`_version_history`** — Added array with v1.0 and v1.1 entries.
- **`cross_module_propagation.recent_promotions`** — Added 10-entry promotion history tracking articles graduated from cooker to `/docs/Research/`.
- **`submodules`** — Added 3 submodule groups:
  - `How_RTT_Helps_Planes_Not_Go_Boom/` (7 chapters, 3 asset dirs)
  - `art/` (4 SVGs)
  - 9 game/mythic JSON manifests
- **`files`** — Expanded from 1 to 4 infrastructure entries (README.md, index.html, _ideas_module.json, LINEAGE.md).
- **Version** — Bumped from 1.0 → 1.1.

### Changed — `index.html` (Module Front Door)

- **Module identity block** — Added 13 meta tags previously missing (module, canonical-id, module-type, version, status, parent, siblings, canonical-path, last-updated, license, ai-ready, ai-module-id, ai-operators).
- **`last-updated`** — Updated from 2026-05-01 → 2026-05-06.
- **`ai.version`** — Updated from 1.0 → 1.1.
- **`ai.module.summary`** — Updated with 288-entry census breakdown.
- **`description`** — Expanded to include census count and domain coverage.
- **`citation_date`** — Updated from 2026-05-01 → 2026-05-06.
- **Session context** — `Modules` field updated to include `→ promoted articles`. Version updated to 1.1. Format field expanded to include all file types.
- **Badge div** — Updated to `📘 Non‑Canonical Cooker · 288 entries · v1.1`.
- **All existing tags** — Preserved.

### Not Changed

- All 219 idea markdown files — sandbox content, not tracked in changelog.
- All 39 HTML renderers — sandbox content.
- All 9 game/mythic JSON manifests — sandbox content.
- DOC_MAP (30 entries) — unchanged; remains the living navigation layer.
- CSS, SVG glyph, script block — unchanged.

### Noted — Recent Promotions to `/docs/Research/`

10 articles recently graduated from cooker to canonical Research module:

1. `Advance_DPU_VCG_NIMMS_Architecture.md`
2. `Aging_Substrate_Analysis.md`
3. `AI_Web_Agentic_Grammar_Options.md`
4. `Domain_Forking_and_New_Governance_Through_Grammar_Not_Policy.md`
5. `European_Spallation_Source_needs_TriadicFrameworksTech.md`
6. `JWST-RTT_Triadic_Core_Primitive_as_a_QA_Layer.md`
7. `Substrate_Communications.md`
8. `Supercomputers_Are_Already_Triadic_They_Just_Dont_Know_It.md`
9. `Warp_Drive_Architecture_Plan_Scaffolded_with_RTT-Inside.md`
10. `ZipNN_Triadic_Patterns_and_the_Hidden_Two_Thirds.md`

HTML renderers for these articles remain in the sandbox as frozen references.

### Noted — DOC_MAP Coverage

The DOC_MAP in `index.html` covers 30 of 219 markdown files (13%). This is **by design** — the sandbox is a low-friction workspace. Not every idea needs to be navigable from the sidebar. Ideas are promoted to the DOC_MAP as they mature, then graduated to canonical modules when ready.

---

## [1.0] — 2026-05-01

### Added

- `_ideas_module.json` — Module manifest (1 file entry).
- `index.html` — Interactive reader with DOC_MAP (30 entries).
- `README.md` — Sandbox front door.

---

## Infrastructure Inventory

| File | Version | Role | Status |
|------|---------|------|--------|
| `_ideas_module.json` | 1.1 | index | refreshed |
| `index.html` | 1.1 | index | refreshed |
| `README.md` | 1.0 | index | pass |
| `LINEAGE.md` | 1.0 | reference | pass |
| `CHANGELOG.md` | — | — | this file |

---

*Maintained by: Nawder Loswin · TriadicFrameworks · MIT*

