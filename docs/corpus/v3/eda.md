eda 
# Post-ASML PDK Integration

**Status:** REDIRECT STUB
**Document ID:** eda-redirect-001
**Canonical Path:** `docs/eda/PostASML_PDK_Integration.md`
**Resolves To:** `docs/post-ASML_era/The_TRS-Aware_PDK_Specification.md`

---

## Redirect Notice

> **This path is a registered alias.** The content you are looking for has been published at its canonical location:
>
> **`docs/post-ASML_era/The_TRS-Aware_PDK_Specification.md`**

This file exists to preserve inbound links from tools, scripts, and documentation that reference the EDA-scoped path `docs/eda/PostASML_PDK_Integration.md`. No content is maintained here.

---

## Why This Alias Exists

During the initial documentation architecture, PDK integration content was anticipated to reside under `docs/eda/`. The full specification was subsequently placed in `docs/post-ASML_era/` with the rest of the core post-ASML era canon, as it encompasses fab-side, materials, and metrology concerns beyond EDA scope alone.

The alias `docs/eda/PostASML_PDK_Integration.md` is retained as a stable redirect for tools and external references that predate the canonical path assignment.

---

## Canonical Document Summary

The **TRS-Aware PDK Specification** (`docs/post-ASML_era/The_TRS-Aware_PDK_Specification.md`) is the normative specification for process design kits in TRS-aware fabs. It defines:

- Five PDK component categories: SCLM, TSPS, TDR, CBT, TTFAL
- SC Class Layer Maps in TLMF format
- TRS Stack Parameter Sets
- Temporal Design Rules (six rule classes: ASR, DGR, TPR, CGR, CSR, TCRS)
- Coherence Budget Tables
- TTF Arc Library (five arc types: CSA, ZBA, APA, TCA, DDA)
- RWDL/SC_eff map integration
- Deliverable directory structure and generation workflow
- EDA tool integration requirements and certification
- PDK qualification test suite
- Versioning and change control (format: `{process_node}_{fab_id}_{scr_zone_config}_{major}.{minor}.{patch}[P]`)

---

## Navigation

| | |
|---|---|
| **Canonical document** | `docs/post-ASML_era/The_TRS-Aware_PDK_Specification.md` |
| **EDA companion reference** | `docs/eda/TTF_Reference.md` |
| **Module index** | `docs/post-ASML_era/README.md` |
| **Module metadata** | `docs/post-ASML_era/module.json` |

---

*This redirect stub is maintained by the TriadicFrameworks documentation graph. Do not add content to this file — update the canonical document instead.*
# Temporal Timing Format Reference

**Status:** STUB
**Priority:** P1
**Document ID:** eda-001
**Canonical Path:** `docs/eda/TTF_Reference.md`
**Related Module:** `docs/post-ASML_era/module.json`

---

## About This Document

This document is a **planned stub**. It has been registered in the TriadicFrameworks documentation graph and is referenced by five canonical post-ASML era documents. It is a **P1 priority** deliverable required by EDA tool integration workflows and PDK delivery.

---

## Purpose

The Temporal Timing Format (TTF) Reference provides the complete specification for the TTF arc encoding system used throughout the TRS-aware EDA toolchain. TTF arcs represent temporal causality paths in the logic graph, replacing or augmenting traditional static timing arcs with zone-relative temporal transition descriptors. This reference is the normative authority for arc type definitions, encoding syntax, EDA integration interfaces, and timing engine consumption rules.

---

## Citing Documents

| Document | Context of Citation |
|---|---|
| `docs/post-ASML_era/The_Temporal_Manufacturing_Primer.md` | Referenced as the format authority for temporal timing annotations on logic cells and interconnect; TTF arcs are introduced as the output representation of L3 Resolution |
| `docs/post-ASML_era/The_TGI_Metrology_Standard.md` | Referenced as the output format for CLG (Coherence Length Gradient) and RWDL (Regime Width Distribution Locus) spatial maps when exported for EDA consumption |
| `docs/post-ASML_era/The_TRS-Aware_PDK_Specification.md` | Referenced as the normative arc format for the TTF Arc Library (TTFAL) component; five PDK arc types (CSA, ZBA, APA, TCA, DDA) are defined as TTF arc instances |
| `docs/post-ASML_era/The_Logic_Folding_Architecture_Guide.md` | Referenced throughout for fold boundary arc encoding, Temporal Register timing arcs, and inter-fold ZBA arc definitions |
| `docs/post-ASML_era/The_Multi-Regime_Semiconductor_Model.md` | Referenced as the format for regime-annotated timing arcs used in model validation outputs |

---

## Expected Content

When authored, this document is expected to cover:

1. **TTF Overview** — Design goals; relationship to Liberty (.lib) and Verilog timing models; TTF as a superset or companion format.
2. **Arc Type Definitions**
   - **CSA (Coherence-Sensitive Arc)** — Arcs whose delay is a function of local SC_eff; encoding of SC class dependency.
   - **ZBA (Zone Boundary Arc)** — Arcs that cross SCR zone boundaries; inter-zone handoff latency encoding; ZBI parameter embedding.
   - **APA (Adaptive Phase Arc)** — Arcs whose phase can shift under dynamic coherence conditions; phase adaptation range encoding.
   - **TCA (Temporal Commit Arc)** — Arcs terminating at a Temporal Register commit point; L4 Commit coupling; SLF reference encoding.
   - **DDA (Deferred Delivery Arc)** — Arcs with intentional temporal delay for pipeline fold stages; fold depth parameter encoding.
3. **Encoding Syntax** — File format (text-based, line-oriented); arc record structure; field types and units; example arc records for each type.
4. **Arc Composition Rules** — How multiple TTF arcs combine at a cell output; precedence rules; degenerate arc handling.
5. **SC Class Annotation** — Embedding SC class constraints in arc records; runtime SC class checking by timing engine.
6. **EDA Tool Integration**
   - Timing engine ingestion API; arc discovery and loading sequence.
   - Static timing analysis (STA) extensions for TTF; slack computation with temporal arcs.
   - Required tool certification for TTF consumption (cross-reference to PDK Specification Section 8).
7. **Mapping from Metrology Data** — How RWDL and CLG maps from TGI Metrology are converted to TTF SC class annotations; toolchain scripts and format conversion.
8. **Versioning** — TTF format version field; backward compatibility rules; deprecation policy for arc types.
9. **Quick Reference** — Table of all arc types, required fields, optional fields, and units.

---

## Dependencies

When authored, this document is expected to reference:

- `docs/post-ASML_era/The_TRS-Aware_PDK_Specification.md` — PDK arc library definitions that instantiate TTF arc types
- `docs/post-ASML_era/The_Logic_Folding_Architecture_Guide.md` — Logic fold context for ZBA and DDA arc usage
- `docs/post-ASML_era/The_TGI_Metrology_Standard.md` — Metrology data that feeds into TTF arc SC annotations
- `docs/fab/SCR_Zone_Config.md` — Zone topology parameters embedded in ZBA arc records

---

## Authoring Notes

- This document MUST use normative language with R-prefix identifiers (R-TTF-NN format recommended).
- Arc encoding syntax MUST be specified with sufficient precision that a conforming parser can be implemented from this document alone (no ambiguous fields).
- All five arc types defined in `The_TRS-Aware_PDK_Specification.md` (CSA, ZBA, APA, TCA, DDA) must be explicitly covered and cross-referenced.
- Format version numbering must be defined before first public release.

---

## Related Documents

| Document | Relationship |
|---|---|
| `docs/post-ASML_era/The_TRS-Aware_PDK_Specification.md` | Primary consumer — TTFAL component is a TTF arc library |
| `docs/post-ASML_era/The_Logic_Folding_Architecture_Guide.md` | Major consumer — fold boundary and TR arcs use TTF encoding |
| `docs/eda/PostASML_PDK_Integration.md` | Sibling EDA document — redirect stub to PDK Specification |
| `docs/post-ASML_era/README.md` | Module index |

---

*This stub was scaffolded from the TriadicFrameworks post-ASML era documentation suite. See `docs/post-ASML_era/README.md` for the full document graph.*
