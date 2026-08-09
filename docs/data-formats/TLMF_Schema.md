# Temporal Layer Markup Format Schema

**Status:** STUB
**Priority:** P2
**Document ID:** data-formats-002
**Canonical Path:** `docs/data-formats/TLMF_Schema.md`
**Related Module:** `docs/post-ASML_era/module.json`

---

## About This Document

This document is a **planned stub**. It has been registered in the TriadicFrameworks documentation graph and is referenced by two canonical post-ASML era documents. It is a **P2 priority** deliverable, required for PDK generation toolchains and model validation workflows.

---

## Purpose

The Temporal Layer Markup Format (TLMF) Schema defines the file format used to encode SC Class Layer Maps (SCLM) within a TRS-Aware PDK deliverable. TLMF files carry spatially resolved SC class annotations, regime boundary positions, RWDL contours, and SC_eff scalar fields across the substrate plane. They are the primary data interchange format between fab metrology outputs (SC_eff maps from TGI Metrology) and EDA layer assignment toolchains.

---

## Citing Documents

| Document | Context of Citation |
|---|---|
| `docs/post-ASML_era/The_TRS-Aware_PDK_Specification.md` | TLMF is the normative file format for the SCLM (SC Class Layer Map) PDK component; PDK deliverable directory must include one TLMF file per SC zone configuration; TLMF format version is part of the PDK version string |
| `docs/post-ASML_era/The_Multi-Regime_Semiconductor_Model.md` | TLMF is referenced as the export format for spatially resolved ψ(r,t) regime maps and CLG fields produced by model validation runs |

---

## Expected Content

When authored, this document is expected to cover:

1. **Format Overview** — TLMF design goals; relationship to GDS/OASIS layer systems; TLMF as an overlay format annotating spatial coordinates with temporal properties.
2. **File Structure**
   - `tlmf_header` — Format version, process node, fab ID, SCR zone config ID, generation timestamp, originating tool
   - `tlmf_substrate` — Substrate geometry (die extent, coordinate origin, units)
   - `tlmf_layers` — Array of named temporal layers, each containing:
     - `layer_id` — Unique layer identifier within the PDK
     - `sc_class_map` — Rasterized or polygon-decomposed SC class assignment (SC-I / SC-II / SC-III) per region
     - `sc_eff_field` — Optional continuous SC_eff scalar field (floating point grid or contour list)
     - `rwdl_contours` — RWDL boundary polylines in substrate coordinates
     - `clg_field` — Optional Coherence Length Gradient field
     - `regime_boundaries` — CCR/CPR/TR regime boundary polygons (from MRSM validation data, where available)
   - `tlmf_metadata` — Measurement provenance (TCT-DEF session IDs, TGI Metrology run IDs, MRSM model version)
3. **Coordinate System** — Origin convention; units (nm or μm); handedness; relationship to die corner marking.
4. **SC Class Encoding** — Integer codes for SC class values in raster maps; polygon winding rules for vector encoding.
5. **Scalar Field Encoding** — Grid resolution requirements; interpolation method specification; NaN handling for out-of-bounds regions.
6. **TLMF Schema** — Formal schema definition (JSON Schema or XML Schema); standalone schema file location in `docs/data-formats/schemas/`.
7. **TLMF Version Field** — Format version field; version lock to PDK version; backward compatibility policy.
8. **Conformance** — Minimum required layers for a conforming TLMF file; optional extended layers; producer/consumer conformance separately stated.
9. **Toolchain Integration** — How EDA tools load TLMF for layer assignment; how PDK generation scripts produce TLMF from metrology inputs; reference toolchain scripts.
10. **Example File** — Annotated example TLMF for a two-zone substrate with SC-I core and SC-II periphery.

---

## Dependencies

When authored, this document is expected to reference:

- `docs/post-ASML_era/The_TRS-Aware_PDK_Specification.md` — Primary consumer; SCLM component definition
- `docs/post-ASML_era/The_TGI_Metrology_Standard.md` — Source of SC_eff and RWDL maps that populate TLMF fields
- `docs/data-formats/TCT_DEF_Schema.md` — TCT-DEF SC rating data used in TLMF SC class map generation
- `docs/materials/SC_Classification.md` — SC class boundary definitions encoded in TLMF layer values
- `docs/fab/SCR_Zone_Config.md` — Zone topology that defines TLMF zone partitioning

---

## Authoring Notes

- Field names in TLMF layer records MUST be consistent with field names in the PDK SCLM deliverable as defined in `The_TRS-Aware_PDK_Specification.md`.
- The SC_eff scalar field resolution MUST be specified as a function of the minimum design rule pitch for the target SC class.
- Raster and vector encoding paths MUST both be defined; tools may support either or both.
- TLMF version number MUST be embedded in the PDK version string per the `{process_node}_{fab_id}_{scr_zone_config}_{major}.{minor}.{patch}[P]` format.

---

## Related Documents

| Document | Relationship |
|---|---|
| `docs/post-ASML_era/The_TRS-Aware_PDK_Specification.md` | Primary consumer — SCLM is a TLMF-encoded PDK component |
| `docs/post-ASML_era/The_Multi-Regime_Semiconductor_Model.md` | Secondary consumer — regime maps exported in TLMF format |
| `docs/data-formats/TCT_DEF_Schema.md` | Upstream data source — TCT-DEF SC ratings populate TLMF maps |
| `docs/data-formats/TDRC_Violation_Log_Schema.md` | Sibling schema — TDRC violations are spatially mapped against TLMF zone boundaries |
| `docs/materials/SC_Classification.md` | SC class authority for TLMF layer encoding |
| `docs/post-ASML_era/README.md` | Module index |

---

*This stub was scaffolded from the TriadicFrameworks post-ASML era documentation suite. See `docs/post-ASML_era/README.md` for the full document graph.*
