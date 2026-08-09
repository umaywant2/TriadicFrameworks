# Substrate Clarity Classification Standard

**Status:** STUB
**Priority:** P1
**Document ID:** materials-001
**Canonical Path:** `docs/materials/SC_Classification.md`
**Related Module:** `docs/post-ASML_era/module.json`

---

## About This Document

This document is a **planned stub**. It has been registered in the TriadicFrameworks documentation graph and is referenced by **all seven** canonical post-ASML era documents, making it the highest-priority outstanding materials deliverable and one of only two P1 stubs cited by every canonical document (alongside `docs/fab/TRS_Qualification.md`).

---

## Purpose

The Substrate Clarity Classification Standard is the normative authority for SC class assignment. It defines the boundaries, measurement traceability chain, class assignment authority, labeling conventions, and re-classification procedures for all substrates processed under the post-ASML era canon. The SC class of a substrate governs which process flows, equipment tiers, and design rules apply at every stage of manufacturing and design.

---

## Citing Documents

| Document | Context of Citation |
|---|---|
| `docs/post-ASML_era/The_Temporal_Manufacturing_Primer.md` | Defines SC conceptually; references this standard for normative class thresholds and assignment authority |
| `docs/post-ASML_era/The_SCR_Specification.md` | SC class governs SCR zone eligibility, CMA alert thresholds, and inter-zone handoff qualification |
| `docs/post-ASML_era/The_TGI_Metrology_Standard.md` | SC class drives acceptance criteria tables (Table 4); SC_eff is the primary measured quantity mapped to class |
| `docs/post-ASML_era/TCT_Protocol.md` | TCT SC Rating derivation (Section 7.3) produces the SC value that is classified by this standard; AER at Δτ_ref=1/256 is the classification input |
| `docs/post-ASML_era/The_TRS-Aware_PDK_Specification.md` | SC Class Layer Maps (SCLM) in the PDK are keyed to SC classes defined here; design rule stringency is class-dependent |
| `docs/post-ASML_era/The_Logic_Folding_Architecture_Guide.md` | Fold architecture type selection and Temporal Register refresh rate are SC class–dependent |
| `docs/post-ASML_era/The_Multi-Regime_Semiconductor_Model.md` | SC class is described as the observable indicator of regime membership; class boundaries correspond to regime transition thresholds |

---

## Current Canonical SC Class Thresholds

The following thresholds are currently established across the post-ASML era series and MUST be reproduced verbatim in this document:

| SC Class | SC Value Range | Regime Association | Notes |
|---|---|---|---|
| SC-I | SC > 0.92 | Coherent Crystalline Regime (CCR) | Highest coherence; supports all fold architecture types |
| SC-II | 0.75 ≤ SC ≤ 0.92 | Transitional Regime (TR) | Moderate coherence; single-cycle and multi-cycle folds; PDK design rules more conservative |
| SC-III | SC < 0.75 | Classical Patterning Regime (CPR) | Low coherence; temporal logic unreliable; process re-evaluation required |

> **Note to authors:** These thresholds are currently embedded inline across seven documents. Any revision to these values in this standard MUST trigger a synchronized update to all seven canonical documents. See `docs/post-ASML_era/README.md` — Authoring Notes for the update procedure.

---

## Expected Content

When authored, this document is expected to cover:

1. **Classification Authority** — Which entity (fab metrology authority, process qualification body) has authority to issue SC class assignments; chain of custody requirements.
2. **Measurement Traceability** — Required measurement chain from raw AER/SC values through TCT Protocol to final class assignment; instrument class minimums; calibration requirements.
3. **Class Boundary Definitions** — Normative values (see table above); derivation basis; rationale for threshold positions relative to regime physics.
4. **Class Assignment Procedure** — Step-by-step classification workflow; required number of measurement sites; spatial uniformity requirements for class assignment (uniform vs. graded class substrate handling).
5. **Substrate Labeling** — Required labeling format for classified substrates; class identifier encoding in substrate tracking systems.
6. **Borderline Cases** — Protocol for substrates measuring within ±0.02 of a class boundary; retest requirements; escalation path.
7. **Re-Classification** — Conditions permitting substrate re-classification (e.g., after annealing or process recovery); required re-measurement scope.
8. **Cross-Document Consistency** — List of all documents that embed SC class thresholds with version-lock table; procedure for coordinated threshold revision.
9. **Historical Class Map** — Relationship of SC classes to legacy geometric process node tiers for migration planning.

---

## Dependencies

When authored, this document is expected to reference:

- `docs/post-ASML_era/TCT_Protocol.md` — The normative measurement protocol that produces SC values for classification
- `docs/post-ASML_era/The_TGI_Metrology_Standard.md` — The broader metrology framework within which SC classification sits
- `docs/post-ASML_era/The_Multi-Regime_Semiconductor_Model.md` — Physical basis for class boundary positions

---

## Authoring Notes

- This document MUST use normative language with R-prefix identifiers (R-SCC-NN format recommended).
- The three SC class thresholds (SC-I: >0.92, SC-II: 0.75–0.92, SC-III: <0.75) are currently the canonical values and may not be changed without a coordinated cross-document update.
- A **version-lock table** listing every document that embeds these thresholds is strongly recommended in an appendix.
- This is a **P1 priority** document — all seven canonical documents gate on its existence.

---

## Related Documents

| Document | Relationship |
|---|---|
| `docs/post-ASML_era/TCT_Protocol.md` | Normative measurement source for SC classification input |
| `docs/post-ASML_era/The_TGI_Metrology_Standard.md` | Broader metrology context; SC_eff maps feed class assignment |
| `docs/post-ASML_era/The_Multi-Regime_Semiconductor_Model.md` | Physical regime theory underlying class boundary positions |
| `docs/post-ASML_era/The_TRS-Aware_PDK_Specification.md` | PDK consumer of class definitions |
| `docs/post-ASML_era/README.md` | Module index |

---

*This stub was scaffolded from the TriadicFrameworks post-ASML era documentation suite. See `docs/post-ASML_era/README.md` for the full document graph.*
