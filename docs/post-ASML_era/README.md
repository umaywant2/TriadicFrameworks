# post-ASML_era

- [`module.json`](https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/refs/heads/main/docs/post-ASML_era/module.json) — Agentic module schema role assignments

**Module:** `docs/post-ASML_era`
**Status:** Active · Revision 1.0.0
**Updated:** 2026-08-08
**Series:** TriadicFrameworks Canonical Reference

This directory contains the foundational reference series for temporal manufacturing
in the post-ASML era. The series defines — from physical theory through manufacturing
infrastructure, metrology, design rules, and architectural methodology — the complete
knowledge base for Substrate Clarity–based computing.

---

## Document Catalog

| # | Filename | Title | Type | Status | Revision |
|---|----------|-------|------|--------|----------|
| 1 | `The_Temporal_Manufacturing_Primer.md` | The Temporal Manufacturing Primer | Reference | Canonical | 1.0.0 |
| 2 | `The_SCR_Specification.md` | The SCR Specification | Specification | Canonical | 1.0.0 |
| 3 | `The_TGI_Metrology_Standard.md` | The TGI Metrology Standard | Standard | Canonical | 1.0.0 |
| 4 | `TCT_Protocol.md` | TCT Protocol | Protocol | Canonical | 1.0.0 |
| 5 | `The_TRS-Aware_PDK_Specification.md` | The TRS-Aware PDK Specification | Specification | Canonical | 1.0.0 |
| 6 | `The_Logic_Folding_Architecture_Guide.md` | The Logic Folding Architecture Guide | Guide | Canonical | 1.0.0 |
| 7 | `The_Multi-Regime_Semiconductor_Model.md` | The Multi-Regime Semiconductor Model | Model | Informative | 0.9.0 draft |
| — | `pae_Capture.md` | Module Capture Index | Internal | Active | — |
| — | `module.json` | Module Descriptor | Machine-readable | Active | 1.0.0 |

> **Note on `TCT_Protocol.md` path.** Prior documents in this series reference the TCT
> Protocol at `docs/metrology/TCT_Protocol.md`. That path is maintained as a redirect
> stub resolving here. The canonical location is `docs/post-ASML_era/TCT_Protocol.md`.
>
> **Note on `The_TRS-Aware_PDK_Specification.md`.** Referenced elsewhere as
> `docs/eda/PostASML_PDK_Integration.md`. That path resolves here via redirect stub.

---

## Dependency Graph

Documents must be read — and authored revisions must be evaluated — in dependency
order. An arrow (→) indicates "depends on" or "assumes familiarity with."

```
The_Multi-Regime_Semiconductor_Model.md   [Physical foundation — INFORMATIVE]
        │
        ▼
TCT_Protocol.md ──────────────────────────────────────┐
        │                                              │
        ▼                                              │
The_TGI_Metrology_Standard.md                         │
        │                                              │
        ▼                                              │
The_Temporal_Manufacturing_Primer.md  ◄───────────────┘
        │
        ├──────────────────────┐
        ▼                      ▼
The_SCR_Specification.md   The_TRS-Aware_PDK_Specification.md
        │                          │
        └──────────┬───────────────┘
                   ▼
        The_Logic_Folding_Architecture_Guide.md
```

For normative rule resolution, the dependency graph also determines precedence:
a downstream document's normative requirements take precedence over any
conflicting guidance in an upstream document.

---

## Reading Paths by Audience

### Fab Architect / Equipment Vendor
1. The_Temporal_Manufacturing_Primer.md
2. The_SCR_Specification.md ← primary reference
3. The_TGI_Metrology_Standard.md (§4–§6)
4. The_TRS-Aware_PDK_Specification.md (§6 Coherence Budget Tables)

### Process Engineer / Metrology
1. The_Multi-Regime_Semiconductor_Model.md ← start here for physical grounding
2. TCT_Protocol.md ← primary reference
3. The_TGI_Metrology_Standard.md ← primary reference
4. The_Temporal_Manufacturing_Primer.md (§3 Substrate Clarity)

### EDA Tool Developer / PDK Integrator
1. The_Temporal_Manufacturing_Primer.md
2. The_TRS-Aware_PDK_Specification.md ← primary reference
3. The_SCR_Specification.md (§11 SCR Interface Contracts)
4. The_TGI_Metrology_Standard.md (§9 RWDL and SC_eff)

### Logic Architect / RTL Designer
1. The_Temporal_Manufacturing_Primer.md
2. The_Logic_Folding_Architecture_Guide.md ← primary reference
3. The_TRS-Aware_PDK_Specification.md (§5 Temporal Design Rules, §7 TTF Arc Library)

### Materials Engineer / Process Developer
1. The_Multi-Regime_Semiconductor_Model.md ← primary reference
2. TCT_Protocol.md
3. The_TGI_Metrology_Standard.md (§6 Interface Continuity, §9 CLG)

### Timing Engineer
1. The_TRS-Aware_PDK_Specification.md (§7 TTF Arc Library)
2. The_Logic_Folding_Architecture_Guide.md (§10 Timing Closure)
3. The_SCR_Specification.md (§6 SLF, §7 Inter-Zone Handoff)

---

## Outbound Stub Registry

The following files are referenced by documents in this module but have not yet
been authored. They are scaffolded at the listed paths. Priority tiers:

- **P1** — Referenced by ≥ 4 documents in this series; blocks process qualification
- **P2** — Referenced by 2–3 documents; blocks EDA or design workflows
- **P3** — Referenced by 1 document; extends the framework

| Priority | Path | Description | Cited By |
|----------|------|-------------|----------|
| P1 | `docs/fab/TRS_Qualification.md` | TRS Stack Qualification Procedure | All 7 docs |
| P1 | `docs/materials/SC_Classification.md` | Substrate Clarity Classification Standard | All 7 docs |
| P1 | `docs/eda/TTF_Reference.md` | Temporal Timing Format Reference | Primer, TGI Metro, PDK, Logic Folding, MRSM |
| P1 | `docs/fab/SCR_Zone_Config.md` | SCR Zone Configuration Guide | SCR Spec, TGI Metro, PDK, Logic Folding, MRSM |
| P2 | `docs/foundations/Triadic_Operator_Primer.md` | Triadic Operator Primer | Primer, MRSM |
| P2 | `docs/data-formats/TCT_DEF_Schema.md` | TCT Data Exchange Format Schema | TCT Protocol, PDK Spec, MRSM |
| P2 | `docs/data-formats/TLMF_Schema.md` | Temporal Layer Markup Format Schema | PDK Spec, MRSM |
| P2 | `docs/data-formats/TDRC_Violation_Log_Schema.md` | TDRC Violation Log Schema | PDK Spec |
| P3 | `docs/design/Temporal_Address_Mapping_Spec.md` | Temporal Address Mapping Specification | MRSM |
| — | `docs/metrology/TCT_Protocol.md` | **Redirect stub** → `docs/post-ASML_era/TCT_Protocol.md` | Primer, TGI Metro |
| — | `docs/eda/PostASML_PDK_Integration.md` | **Redirect stub** → `docs/post-ASML_era/The_TRS-Aware_PDK_Specification.md` | TGI Metro, TCT Protocol |

---

## Naming Conventions

| Convention | Rule |
|------------|------|
| Guide documents | `The_{Subject}_Guide.md` |
| Specification documents | `The_{Subject}_Specification.md` |
| Standard documents | `The_{Subject}_Standard.md` |
| Protocol documents | `{Subject}_Protocol.md` |
| Model documents | `The_{Subject}_Model.md` |
| Schema documents | `{Format}_Schema.md` (in `docs/data-formats/`) |
| Stub documents | Same name as target; carries `status: STUB` frontmatter |
| Redirect stubs | Same name as alias path; carries `redirect_to:` frontmatter |

---

## Authoring Notes

- All documents in this series use `MUST / MUST NOT / SHOULD / SHOULD NOT / MAY`
  normative language as defined in each document's §1 Normative Language table.
- The MRSM (`The_Multi-Regime_Semiconductor_Model.md`) is INFORMATIVE. It does not
  impose normative requirements. Revisions that change model formula results by more
  than 5% at an SC class boundary require a cross-impact analysis across all
  dependent normative documents before merge.
- Revisions to SC class threshold values (0.92 and 0.75) require simultaneous updates
  to: TCT_Protocol.md §10, SC_Classification.md, The_TRS-Aware_PDK_Specification.md
  §13.2, and The_Multi-Regime_Semiconductor_Model.md §8.2.
- `pae_Capture.md` is the internal module capture index. It is maintained separately
  and does not follow the standard document template.
