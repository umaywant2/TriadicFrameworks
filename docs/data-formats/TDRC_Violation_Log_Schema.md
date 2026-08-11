# TDRC Violation Log Schema

**Status:** STUB
**Priority:** P2
**Document ID:** data-formats-003
**Canonical Path:** `docs/data-formats/TDRC_Violation_Log_Schema.md`
**Related Module:** `docs/post-ASML_era/module.json`

---

## About This Document

This document is a **planned stub**. It has been registered in the TriadicFrameworks documentation graph and is referenced by one canonical post-ASML era document. It is a **P2 priority** deliverable, required for PDK design rule certification and tapeout sign-off workflows.

---

## Purpose

The TDRC (Temporal Design Rule Check) Violation Log Schema defines the structured format for recording, classifying, and reporting design rule violations detected by a TDRC-compliant EDA engine during layout verification of a TRS-aware design. A conforming violation log enables automated sign-off comparison, systematic rule waivers, and tapeout eligibility determination without manual log parsing.

---

## Citing Documents

| Document | Context of Citation |
|---|---|
| `docs/post-ASML_era/The_TRS-Aware_PDK_Specification.md` | Referenced as the required output format for TDRC engines during PDK certification (PDK Qualification Test Suite) and as the sign-off artifact for layout verification against Temporal Design Rules (TDR); the six TDR rule classes (ASR, DGR, TPR, CGR, CSR, TCRS) map to violation category codes in this schema |

---

## Expected Content

When authored, this document is expected to cover:

1. **Format Overview** — TDRC-VL design goals; relationship to conventional DRC log formats (SVDB, ASCII marker databases); TDRC-VL as a structured, machine-parseable superset.
2. **Top-Level Log Structure**
   - `tdrc_header` — Run metadata: EDA tool ID and version, PDK ID and version, design name, run timestamp, rule deck version, target SC class
   - `tdrc_summary` — Total violation counts by severity and rule class; overall pass/fail determination; waiver count
   - `tdrc_violations` — Array of individual violation records (see below)
   - `tdrc_waivers` — Array of applied waiver records with authority reference
   - `tdrc_provenance` — TLMF file reference, PDK version string, SC Class Layer Map version used during run
3. **Violation Record Structure** — Per-violation fields:
   - `violation_id` — Unique ID within this run
   - `rule_id` — R-prefix requirement identifier (e.g., R-ASR-03, R-TPR-07) from the PDK TDR
   - `rule_class` — One of: ASR, DGR, TPR, CGR, CSR, TCRS
   - `severity` — ERROR / WARNING / INFO
   - `location` — Substrate coordinate(s) or cell reference path(s) of the violation
   - `zone_id` — SCR zone in which the violation occurs
   - `sc_class_local` — Local SC class at violation site (from TLMF)
   - `description` — Human-readable violation description
   - `measured_value` / `limit_value` — Numeric values for quantitative violations (e.g., temporal arc slack, coherence budget headroom)
   - `waiver_id` — Reference to applied waiver record, if waived; null otherwise
4. **Waiver Record Structure** — `waiver_id`, `rule_id`, `waiver_authority`, `justification`, `expiry`, `sign_off_id`.
5. **Rule Class Codes** — Normative mapping of the six TDR rule classes to TDRC-VL category codes:

   | Rule Class | Code | Description |
   |---|---|---|
   | ASR | `ASR` | Amplitude-Spacing Rules — temporal arc amplitude constraints |
   | DGR | `DGR` | Density-Gradient Rules — SC gradient crossing rules |
   | TPR | `TPR` | Temporal Placement Rules — fold placement and zone boundary rules |
   | CGR | `CGR` | Coherence-Gap Rules — minimum coherence headroom in budget |
   | CSR | `CSR` | Commit-Sequencing Rules — L4 commit ordering constraints |
   | TCRS | `TCRS` | Temporal Coherence Reserve Specifications — reserve margin rules |

6. **Severity Levels** — Normative definitions of ERROR (blocks tapeout), WARNING (requires waiver or designer acknowledgment), and INFO (informational, no sign-off action required).
7. **Sign-Off Determination** — Algorithm for computing overall run pass/fail from violation counts, severity levels, and applied waivers.
8. **Schema Definition** — Formal JSON Schema (Draft 07 or later); standalone schema file in `docs/data-formats/schemas/`.
9. **Conformance** — Minimum required fields for basic conformance; required fields for tapeout sign-off use.
10. **Example Log** — Annotated example with two violations (one ERROR waived, one WARNING unwaived) and a passing summary determination.

---

## Dependencies

When authored, this document is expected to reference:

- `docs/post-ASML_era/The_TRS-Aware_PDK_Specification.md` — Normative source for all six TDR rule classes and R-prefix requirement IDs that appear in violation records
- `docs/data-formats/TLMF_Schema.md` — TLMF referenced in `tdrc_provenance` for spatial context of violations
- `docs/materials/SC_Classification.md` — SC class used in `sc_class_local` field per violation

---

## Authoring Notes

- Rule class codes (ASR, DGR, TPR, CGR, CSR, TCRS) MUST be identical to those in `The_TRS-Aware_PDK_Specification.md` — do not introduce aliases.
- The `rule_id` field MUST use R-prefix identifiers exactly as published in the PDK's TDR deliverable; free-form rule names are not permitted.
- The sign-off determination algorithm MUST produce a deterministic binary result from the violation log alone (no external tool state required).

---

## Related Documents

| Document | Relationship |
|---|---|
| `docs/post-ASML_era/The_TRS-Aware_PDK_Specification.md` | Primary consumer — PDK certification and tapeout sign-off require a conforming TDRC-VL |
| `docs/data-formats/TLMF_Schema.md` | Spatial context — TDRC violations are mapped against TLMF zone boundaries |
| `docs/materials/SC_Classification.md` | SC class authority for per-violation `sc_class_local` field |
| `docs/post-ASML_era/README.md` | Module index |

---

*This stub was scaffolded from the TriadicFrameworks post-ASML era documentation suite. See `docs/post-ASML_era/README.md` for the full document graph.*
