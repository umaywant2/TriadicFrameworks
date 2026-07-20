# Changelog — `/docs/Research/`

> Research module — original RTT research articles, SEO interpreter tools, and dimensional analysis methods.

All notable changes to files in `/docs/Research/` are documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [1.1] — 2026-05-06

### Context

Full 33-entry module audit and metadata refresh. Multiple research articles recently migrated from the cooker (`_ideas/`) into the Research module. Infrastructure files updated to reflect the expanded collection.

### Changed — `research_module.json` (Module Manifest)

- **`_meta`** — Added full module registry block.
- **`_session_context`** — Replaced old non-standard `session_context` with standardized `_session_context` block.
- **`_version_history`** — Added array with v1.0 and v1.1 entries.
- **`structural_grammar`** — Added D0–D9, R0–R3, C0–C3 envelopes.
- **`cross_module_propagation`** — Added imports and exports.
- **`files`** — Expanded from 8 to 33 entries. Added `purpose` and `role` fields to all entries.
- **Version** — Bumped from 1.0 → 1.1.

### Changed — `index.html` (Module Front Door)

- **Module identity block** — Added 13 meta tags previously missing (module, canonical-id, module-type, version, status, parent, siblings, canonical-path, last-updated, license, ai-ready, ai-module-id, ai-operators).
- **`last-modified`** — Fixed typo from `2026-05-5` → `2026-05-06`.
- **`ai.version`** — Updated from 1.0 → 1.1.
- **`citation_date`** — Updated from `2025` → `2026-05-06`.
- **`ai.module.summary`** — Updated to reflect 22 articles and expanded domain coverage.
- **Session context** — `Modules` field updated from 4 articles → `22 research articles → 3 SEO interpreters → 4‑mode dimensional search`. Version updated to 1.1.
- **DOC_MAP** — Fixed duplicate `DOMAIN_FORKING` key (JS overwrite bug). Added 3 missing entries: `SUBSTRATE_COMMS`, `DRAFT_WIKIPEDIA`, `MODULE_WORK`.
- **Nav sidebar** — Added 3 matching nav links for newly mapped files.
- **Badge div** — Updated to `📘 22 Original RTT Articles · v1.1`.

### Bug Fixes

- **`DOMAIN_FORKING` duplicate key** — The DOC_MAP contained `DOMAIN_FORKING` twice, causing the second entry to silently overwrite the first. Both pointed to the same file, so no data was lost — but the duplicate has been removed.
- **`last-modified` typo** — `2026-05-5` corrected to `2026-05-06`.

### Not Changed — Research Articles (22 files)

All 22 research article markdown files pass clean — no metadata changes required:

| File | Role | Status |
|------|------|--------|
| `Advance_DPU_VCG_NIMMS_Architecture.md` | engine | ✅ pass |
| `Aging_Substrate_Analysis.md` | engine | ✅ pass |
| `AI_Web_Agentic_Grammar_Options.md` | engine | ✅ pass |
| `A_Resonant_Review_of_The_Universe_in_a_Nutshell.md` | reference | ✅ pass |
| `Beyond_Structure_The_Equations_for_Clarity.md` | engine | ✅ pass |
| `Domain_Forking_and_New_Governance_Through_Grammar_Not_Policy.md` | engine | ✅ pass |
| `Draft_TriadicFrameworks_Wikipedia_Info.md` | reference | ✅ pass |
| `European_Spallation_Source_needs_TriadicFrameworksTech.md` | engine | ✅ pass |
| `How_RTT_Applies_to_a_Standard_Power_Transformer.md` | engine | ✅ pass |
| `JWST-RTT_Triadic_Core_Primitive_as_a_QA_Layer.md` | engine | ✅ pass |
| `Power_Supplies_Mobile_Sensors_and_Enhanced_BMS_using_RTT-Inside.md` | engine | ✅ pass |
| `qCompute_with_RTT-Inside_Preview.md` | engine | ✅ pass |
| `Quantum_Energy_Banks_and_Corridor‑Based_Energy_System_Analysis.md` | engine | ✅ pass |
| `Quantum_Lens_Layer_Triadic_Protocols_for_Resonance_Scanning.md` | engine | ✅ pass |
| `Resonance_Triadic_Aligned_Overview.md` | reference | ✅ pass |
| `RTT_Above‑Ground_Electrical_Re-design_Initiative.md` | engine | ✅ pass |
| `RTT_Facilities_Playbook.md` | engine | ✅ pass |
| `Substrate_Communications.md` | engine | ✅ pass |
| `Supercomputers_Are_Already_Triadic_They_Just_Dont_Know_It.md` | engine | ✅ pass |
| `The_Choices_We_Made_and_Why.md` | reference | ✅ pass |
| `Warp_Drive_Architecture_Plan_Scaffolded_with_RTT-Inside.md` | engine | ✅ pass |
| `ZipNN_Triadic_Patterns_and_the_Hidden_Two_Thirds.md` | engine | ✅ pass |

### Not Changed — Research Tools (3 tools + 3 manifests)

| File | Role | Status |
|------|------|--------|
| `Google.md` | engine | ✅ pass |
| `Google_module.json` | index | ✅ pass |
| `Bing.md` | engine | ✅ pass |
| `Bing_module.json` | index | ✅ pass |
| `DuckDuckGo.md` | engine | ✅ pass |
| `DuckDuckGo_module.json` | index | ✅ pass |

### Not Changed — Other Files

| File | Role | Status |
|------|------|--------|
| `README.md` | index | ✅ pass |
| `module_work.md` | reference | ✅ pass (added to manifest) |
| `The_Choices_We_Made_and_Why.pdf` | reference | ✅ pass (added to manifest) |

---

## [1.0] — 2025-01-01

### Added

- `README.md` — Module front door.
- `index.html` — Interactive reader with DOC_MAP.
- `research_module.json` — Module manifest (8 entries).
- `Google.md`, `Bing.md`, `DuckDuckGo.md` — SEO interpreter tools.
- `Google_module.json`, `Bing_module.json`, `DuckDuckGo_module.json` — Tool manifests.
- 5 initial research articles.

---

## File Inventory

| File | Version | Role | Status |
|------|---------|------|--------|
| `research_module.json` | 1.1 | index | refreshed |
| `index.html` | 1.1 | index | refreshed |
| `README.md` | 1.0 | index | pass |
| `module_work.md` | 1.0 | reference | pass |
| 22 research articles | 1.0 | engine/reference | pass |
| 3 SEO tools (.md) | 1.0 | engine | pass |
| 3 tool manifests (.json) | 1.0 | index | pass |
| 1 PDF asset | 1.0 | reference | pass |
| `CHANGELOG.md` | — | — | this file |
| **Total** | | | **33 entries** |

---

*Maintained by: Nawder Loswin · TriadicFrameworks · MIT*

