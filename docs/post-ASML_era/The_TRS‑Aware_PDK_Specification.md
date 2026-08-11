# The TRS-Aware PDK Specification

**Repository:** TriadicFrameworks
**Path:** `docs/post-ASML_era/The_TRS-Aware_PDK_Specification.md`
**Canonical alias:** `docs/eda/PostASML_PDK_Integration.md` → resolves here
**Status:** Canonical Reference
**Revision:** 1.0.0

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [PDK Architecture Overview](#2-pdk-architecture-overview)
3. [SC Class Layer Maps](#3-sc-class-layer-maps)
4. [TRS Stack Parameter Sets](#4-trs-stack-parameter-sets)
5. [Temporal Design Rules](#5-temporal-design-rules)
6. [Coherence Budget Tables](#6-coherence-budget-tables)
7. [TTF Arc Library](#7-ttf-arc-library)
8. [Temporal Crosstalk Rules](#8-temporal-crosstalk-rules)
9. [RWDL and SC_eff Map Integration](#9-rwdl-and-sc_eff-map-integration)
10. [PDK Deliverable Structure](#10-pdk-deliverable-structure)
11. [PDK Generation Workflow](#11-pdk-generation-workflow)
12. [EDA Tool Integration Requirements](#12-eda-tool-integration-requirements)
13. [PDK Qualification and Sign-off](#13-pdk-qualification-and-sign-off)
14. [PDK Versioning and Change Control](#14-pdk-versioning-and-change-control)
15. [Glossary](#15-glossary)
16. [Related Documents](#16-related-documents)

---

## 1. Purpose and Scope

### 1.1 Purpose

This document is the normative specification for the **TRS-Aware Process Design Kit (PDK)** — the structured data package that translates the fab's temporal manufacturing characterization into rule sets, parameter tables, timing arcs, and spatial maps consumable by EDA tools. The TRS-Aware PDK is the interface between the physical world of substrate properties, SCR zone configuration, and TRS stack behavior and the design world of floorplanning, timing closure, verification, and tape-out signoff.

Without a conformant TRS-Aware PDK, no EDA tool has the information required to correctly constrain or verify a design intended for temporal manufacturing. A design signed off against a PDK that is missing, incomplete, or incorrectly derived from upstream measurements will exhibit systematic yield loss in the temporal layers, timing failures at SCR zone boundaries, and coherence budget violations that are not detectable until wafer-level testing.

This specification defines:

- What a TRS-Aware PDK must contain
- How each PDK component is derived from upstream measurement data
- How EDA tools must consume each component
- How a PDK release is generated, validated, and released
- How changes to upstream measurements trigger PDK updates

### 1.2 Canonical Path Note

Prior documents in the post-ASML era series reference this specification at `docs/eda/PostASML_PDK_Integration.md`. The canonical location for this revision is `docs/post-ASML_era/The_TRS-Aware_PDK_Specification.md`. The path `docs/eda/PostASML_PDK_Integration.md` is maintained as a redirect alias. Both paths resolve to this document.

### 1.3 Scope

This specification covers:

- The two-domain PDK architecture and the five TRS-aware PDK component categories
- SC class layer maps: derivation from TCT and TGI data, encoding format, and usage
- TRS stack parameter sets: apodization profiles, address spacing minima, commit sequencing overhead
- Temporal design rules for TDRC: address spacing, density gradient, TGI proximity, and causal graph rules
- Coherence budget tables encoding SCR zone parameters for CBA consumption
- The TTF arc library: arc type definitions, derivation sources, and STA tool consumption requirements
- Temporal crosstalk rules: physical model, rule table structure, per SC class and density tier
- RWDL and SC_eff spatial map integration and their role in position-dependent design rules
- The complete PDK deliverable directory and file structure
- The PDK generation pipeline from upstream measurement data to release package
- EDA tool certification requirements for TDRC, CGV, CBA, and TTF-aware STA
- PDK qualification test suite and sign-off authority chain
- PDK versioning semantics and change control rules

This specification does not cover:

- The classical (non-temporal) PDK components — DRC rules for Tier 1 spatial layers, SPICE device models, parasitic extraction decks for non-temporal layers — except where those components interact with TRS-aware extensions
- The internal operation of EDA tools; this specification defines what tools must accept and produce, not how they implement it
- Substrate material design for target SC classes, which is governed by the Substrate Clarity Classification Standard

### 1.4 Normative Language

| Term | Meaning |
|---|---|
| **MUST** | Required. Non-conformant if omitted or violated. |
| **MUST NOT** | Prohibited. Non-conformant if present. |
| **SHOULD** | Strongly recommended. Deviation requires documented justification. |
| **SHOULD NOT** | Strongly discouraged. Deviation requires documented justification. |
| **MAY** | Permitted but not required. |

---

## 2. PDK Architecture Overview

### 2.1 The Two-Domain PDK

A TRS-Aware PDK operates across two domains that classical PDKs addressed only one of:

**The spatial domain** encompasses the physical layout of the die — layer stack definitions, geometric design rules, parasitic models, and device models. Classical PDKs were exclusively spatial-domain artifacts. TRS-aware PDKs retain the spatial domain but extend it: some spatial-domain components must be modified to account for their interaction with temporal manufacturing steps.

**The temporal domain** encompasses the address-space structure of TRS commit operations — address spacing rules, coherence slot assignments, timing arcs through the SCR, and density constraints derived from substrate SC class. The temporal domain has no classical analog; it is entirely new with temporal manufacturing.

The two domains are not independent. The TGI — the Temporal-Geometric Interface — is the coupling zone between them. TRS-aware PDK components that characterize the TGI (SC_eff maps, RWDL maps, TGI proximity rules) span both domains and belong to neither exclusively.

### 2.2 PDK Component Categories

A conformant TRS-Aware PDK contains five component categories. All five MUST be present for the PDK to be considered complete. A PDK missing any category is incomplete and MUST NOT be used for tape-out signoff.

| Category | Abbreviation | Primary Consumer | Derives From |
|---|---|---|---|
| SC Class Layer Maps | SCLM | TDRC tool, CBA tool, floorplanning | TCT Protocol, TGI Metrology Standard |
| TRS Stack Parameter Sets | TSPS | TDRC tool, TRS intent map generator | TRS Qualification Procedure |
| Temporal Design Rules | TDR | TDRC tool, CGV tool | SCLM, TSPS, TGI Metrology Standard |
| Coherence Budget Tables | CBT | CBA tool, fab scheduler | SCR Specification, SCR qualification record |
| TTF Arc Library | TTFAL | TTF-aware STA tool | SCR Specification, TGI Metrology Standard |

A sixth component, the **Temporal Crosstalk Rule Set (TCRS)**, is considered a sub-component of the TDR category but is specified separately in §8 due to its distinct physical basis and rule format.

### 2.3 Spatial Domain Extensions

The following classical PDK components require modification or augmentation in a TRS-aware PDK:

**Layer stack definition:** The layer stack must include the TGI zone — the transition region between Tier 1 structural layers and Tier 2 temporal layers — with its z_f and z_c boundaries, qualified SC class per layer, and interface quality parameters. Layer definitions without TGI zone specification cannot support TGI-aware extraction or TDRC.

**Power delivery network rules:** As noted in The Temporal Manufacturing Primer, TCUs draw burst current synchronized to the coherence clock. Classical average-current power delivery network rules are insufficient; rules must be augmented with burst-current specifications derived from the SCR coherence cycle period and the per-slot TCU activation count in the coherence budget tables.

**Signal integrity decks:** Classical signal integrity analysis must be extended with temporal crosstalk rules (§8) to capture the phenomenon of high-density commit operations at one temporal address inducing perturbation at adjacent addresses in spatially proximate substrate regions. This is distinct from classical electromagnetic crosstalk and requires dedicated extraction and analysis flows.

### 2.4 Versioning and Compatibility

Every TRS-Aware PDK release carries a version identifier with the format:

```
{process_node}_{fab_id}_{scr_zone_config}_{pdk_major}.{pdk_minor}.{pdk_patch}

Example: TF-N3T_FAB01_ZC-A_2.1.0
```

The fields are defined in §14. EDA tools MUST record the full PDK version identifier in all signoff reports. Signoff reports without a PDK version identifier are non-conformant.

---

## 3. SC Class Layer Maps

### 3.1 Purpose

SC Class Layer Maps encode the substrate clarity class and spatial SC variation for every layer in the process stack that carries temporal address encoding. They are the foundational input to the TDRC tool and the CBA tool: both tools must know the SC class of each layer at each die location before they can apply correct rule thresholds or budget allocations.

### 3.2 Layer-Level SC Class Assignment

Each layer in the process stack is assigned one of four SC designations:

| Designation | Definition | Source |
|---|---|---|
| `SC-I` | Layer qualified for high-density temporal addressing; SC > 0.92 | TCT lot-level SC rating |
| `SC-II` | Layer qualified for restricted temporal addressing; 0.75 ≤ SC ≤ 0.92 | TCT lot-level SC rating |
| `SC-III` | Layer not qualified for temporal addressing; SC < 0.75 | TCT lot-level SC rating |
| `SPATIAL` | Layer not processed by TRS; spatial-only Tier 1 layer | Layer stack definition; no TCT required |

**R-SCLM-01:** Every layer in the process stack MUST have an explicit SC designation in the PDK layer stack definition. Layers without a designation are treated as `SPATIAL` by default, but this default MUST be explicitly confirmed in the PDK generation record; silent defaulting is non-conformant.

**R-SCLM-02:** The SC designation for temporally addressed layers MUST be derived from the TCT SC rating for the substrate lot qualified for that process node, as documented in the TCT Report referenced in the TRS Qualification Record. SC designations derived from supplier specifications or materials-modeled estimates, without TCT measurement evidence, are non-conformant.

### 3.3 Spatial SC Variation Maps

The lot-level SC class assignment establishes the tier for the full die. The spatial SC variation map — derived from the TCT 5×5 subregion SC grid and the TGI metrology SC_eff map — provides finer-grained SC information that drives position-dependent rule variations within the die.

The spatial SC variation map in the PDK is a 2D grid defined in die coordinates with the following properties:

**Resolution:** The map grid resolution is determined by the coarser of the TCT subregion grid (nominally 4.2 mm × 4.2 mm cells) and the TGI metrology SC_eff measurement site spacing. The finer grid is downsampled to the coarser resolution for the merged PDK map.

**Values:** Each grid cell contains:
- `SC_bulk`: the TCT-derived SC rating for that subregion
- `SC_eff`: the TGI-derived effective SC at the TGI boundary for that die region
- `SC_design`: the operative SC value used for rule derivation; defined as `min(SC_bulk, SC_eff)`
- `SC_class_local`: the SC class assignment derived from `SC_design` at that grid cell

**R-SCLM-03:** `SC_design` MUST use `min(SC_bulk, SC_eff)` — the more conservative of the two. Using `SC_bulk` alone in regions where `SC_eff < SC_bulk` would overstate the effective temporal addressing capability at the TGI boundary, producing rules that are too permissive.

**R-SCLM-04:** When `SC_class_local` differs from the lot-level SC class assignment for more than 10% of grid cells in any die quadrant, the PDK MUST implement position-dependent rule zones (§5.6) rather than a uniform lot-level rule set for the affected quadrant.

### 3.4 SC Class Map Format

SC Class Layer Maps are encoded in the **Temporal Layer Markup Format (TLMF)**, a structured text format defined in [`docs/data-formats/TLMF_Schema.md`](../data-formats/TLMF_Schema.md). Each TLMF record specifies:

```
LAYER  {layer_name}  {z_bottom_nm}  {z_top_nm}  {SC_designation}
  SUBREGION  {x_min_um}  {y_min_um}  {x_max_um}  {y_max_um}
    SC_BULK   {value}
    SC_EFF    {value}
    SC_DESIGN {value}
    SC_CLASS  {SC-I | SC-II | SC-III | SPATIAL}
  END_SUBREGION
  ...
END_LAYER
```

**R-SCLM-05:** TLMF files MUST be schema-validated against the current TLMF schema version before PDK packaging. TLMF files that fail schema validation MUST NOT be included in a PDK release.

---

## 4. TRS Stack Parameter Sets

### 4.1 Purpose

TRS Stack Parameter Sets encode the operational parameters of the Temporal Resolution Stack as configured and qualified for the target process node. These parameters govern how the TDRC tool evaluates address spacing feasibility, how the TRS intent map generator computes apodization envelopes, and how the timing model accounts for L3 resolution overhead.

### 4.2 Parameter Set Structure

A TRS Stack Parameter Set is defined per SC class. Processes that use multiple SC classes in their layer stack — SC-I layers for high-density temporal logic and SC-II layers for mixed layers — require a separate parameter set for each SC class in use.

Each parameter set contains the following fields:

**Address spacing parameters:**

| Parameter | Symbol | Unit | Definition |
|---|---|---|---|
| Minimum qualified address spacing | Δτ_min | normalized addr. units | The minimum address spacing at which the TRS, operating on the qualified substrate, achieves the process MQD without exceeding the AER acceptance threshold |
| Address spacing design margin | Δτ_margin | normalized addr. units | Required margin above Δτ_min that designs must maintain; provides headroom for TAOE and manufacturing variation |
| Effective minimum spacing | Δτ_eff | normalized addr. units | Δτ_min + Δτ_margin; the value actually enforced by TDRC |

**Apodization parameters:**

| Parameter | Symbol | Unit | Definition |
|---|---|---|---|
| Apodization window width | W_apod | normalized addr. units | The half-width of the L3 apodization envelope applied to each commit operation |
| Apodization roll-off exponent | n_apod | dimensionless | Controls the steepness of the apodization envelope edges; higher n = sharper rolloff |
| Maximum side-lobe level | SLL_max | dB | The maximum permitted side-lobe amplitude of the apodized operation, normalized to the main lobe |

**Commit sequencing overhead:**

| Parameter | Symbol | Unit | Definition |
|---|---|---|---|
| L2 sequencing latency per operation | T_seq | coherence cycles | The scheduling overhead added by the L2 Sequencing Layer per operation; used as a timing arc in the TTF arc library |
| Maximum operations per coherence slot | N_slot_max | operations | The maximum number of operations the TRS can sequence into a single coherence slot without exceeding sequencing bandwidth |

**R-TSPS-01:** All parameter set values MUST be derived from TRS qualification measurements on the qualified substrate lot, as documented in the TRS Qualification Record. Parameter values taken from simulation, prior-node extrapolation, or supplier data sheets without qualification measurement evidence are non-conformant.

**R-TSPS-02:** Δτ_margin MUST be ≥ 15% of Δτ_min for SC-I processes and ≥ 20% of Δτ_min for SC-II processes. These minimum margins account for TAOE_rnd and spatial SC variation at the die level.

**R-TSPS-03:** A separate TSPS MUST be provided for each SC class present in the process layer stack. TDRC tools that receive a process stack containing SC-I and SC-II layers MUST apply the SC-I TSPS to SC-I layers and the SC-II TSPS to SC-II layers; applying a single TSPS to all temporal layers is non-conformant.

### 4.3 TSPS File Format

TRS Stack Parameter Sets are encoded in the **Temporal Parameter Set Format (TPSF)**, a structured key-value format:

```
TSPS_BEGIN
  PROCESS_NODE    {node_identifier}
  SC_CLASS        {SC-I | SC-II}
  SOURCE_TRS_QUAL {TRS_qualification_record_ID}

  ADDR_SPACING
    DELTA_TAU_MIN     {value}
    DELTA_TAU_MARGIN  {value}
    DELTA_TAU_EFF     {value}   # = MIN + MARGIN; must equal sum
  END_ADDR_SPACING

  APODIZATION
    W_APOD     {value}
    N_APOD     {value}
    SLL_MAX_DB {value}
  END_APODIZATION

  COMMIT_SEQUENCING
    T_SEQ_CYCLES   {value}
    N_SLOT_MAX_OPS {value}
  END_COMMIT_SEQUENCING
TSPS_END
```

**R-TSPS-04:** The TSPS file MUST include the `SOURCE_TRS_QUAL` field referencing the TRS Qualification Record ID from which the parameters were derived. PDK files without traceability to the qualification record are non-conformant.

---

## 5. Temporal Design Rules

### 5.1 Purpose and Rule Categories

Temporal Design Rules (TDR) are the rule set enforced by the TDRC tool during design verification. They are the temporal analog of classical geometric DRC rules: just as DRC rules prevent spatial features from violating fab patterning limits, TDR rules prevent temporal address assignments from violating the substrate's resolution limits, the TRS stack's sequencing capacity, or the SCR's coherence budget.

TDR rules are organized into five categories:

| Category | Code Prefix | Governs |
|---|---|---|
| Address Spacing Rules | ASR | Minimum separation between temporal addresses within and across layers |
| Density Gradient Rules | DGR | Maximum rate of change of temporal density across die regions |
| TGI Proximity Rules | TPR | Constraints on temporal operations sited near TGI-zone boundaries |
| Causal Graph Rules | CGR | Validity constraints on the operation dependency graph |
| Coherence Slot Rules | CSR | Constraints on operation-to-slot assignments relative to the coherence budget |

### 5.2 Address Spacing Rules (ASR)

Address spacing rules enforce the minimum address separation between any two commit operations that share spatial proximity on the substrate. Two operations are considered spatially proximate if their spatial distance is less than the **interaction radius** r_int, derived from the substrate's coherence length L_c:

```
r_int = α × L_c

Where:
  L_c  = material coherence length from the TSPS material record (μm)
  α    = interaction radius multiplier; fixed at 3.0 for this revision
  r_int = the spatial radius within which address spacing rules apply (μm)
```

**ASR-001 — Intra-layer minimum spacing:** Two operations committed in the same layer, whose spatial positions are within r_int of each other, MUST have temporal address separation ≥ Δτ_eff for the layer's SC class.

**ASR-002 — Inter-layer minimum spacing:** Two operations committed in different temporal layers, whose spatial positions project within r_int of each other in the die plane, MUST have temporal address separation ≥ Δτ_eff_inter, where:

```
Δτ_eff_inter = max( Δτ_eff(layer_A), Δτ_eff(layer_B) ) × f_inter

Where:
  f_inter = inter-layer coupling factor from the TSPS material record (≥ 0.5, ≤ 1.0)
```

The inter-layer coupling factor f_inter reflects that coupling between layers is weaker than intra-layer coupling; it relaxes the inter-layer spacing requirement proportionally.

**ASR-003 — Address boundary clearance:** No operation MUST be assigned an address within Δτ_eff/2 of the address space boundary (τ = 0 or τ approaching 1). Operations near the boundary have only one valid neighbor direction and cannot satisfy symmetric spacing to both sides.

**ASR-004 — SC-class mismatch penalty:** When a temporal operation in an SC-I layer is spatially proximate to an operation in an SC-II layer within the same die, the spacing between them MUST satisfy the SC-II Δτ_eff (the more conservative requirement). The lower SC class governs cross-class proximate pairs.

**R-TDR-01:** TDRC tools MUST evaluate address spacing rules using the spatial SC variation map (§3.3) at each operation's die location, not the lot-level SC class alone. A tool that applies uniform lot-level spacing rules without consulting the spatial SC map is non-conformant.

### 5.3 Density Gradient Rules (DGR)

Density gradient rules constrain the rate at which temporal density changes across the die. Abrupt density transitions — a high-density cluster immediately adjacent to a low-density region — produce stress and field gradients within the substrate that elevate TAOE in the transition region, even if the absolute density in each region is within its RWDL.

**DGR-001 — Maximum density gradient:** The temporal density, averaged over any 500 μm × 500 μm die region, MUST NOT change by more than ΔTD_max between adjacent 500 μm × 500 μm regions:

```
ΔTD_max = TD_limit × g_max

Where:
  TD_limit = the RWDL for the lower-density region (operations/cycle/mm²)
  g_max    = maximum density gradient fraction; SC-class-specific:
             SC-I:  g_max = 0.35
             SC-II: g_max = 0.25
```

**DGR-002 — Transition zone buffering:** When the design contains a density step that exceeds ΔTD_max, a transition zone of width w_trans MUST be inserted between the high-density and low-density regions, in which density changes monotonically:

```
w_trans = (ΔTD_actual / ΔTD_max − 1) × 500 μm  (minimum)
```

The transition zone is a design constraint on floorplanning; it is not a physical structure. The designer must ensure that no operations are assigned to the transition zone at densities inconsistent with the monotonic gradient requirement.

**DGR-003 — SCR zone boundary gradient:** The density transition across an SCR zone boundary MUST NOT exceed ΔTD_max as defined for the lower SC class on either side of the boundary. Zone boundaries are already subject to L_handoff latency; density gradients at zone boundaries compound timing risk and are doubly constrained.

### 5.4 TGI Proximity Rules (TPR)

TGI proximity rules constrain temporal operations that are sited in layers close to the TGI ceiling (z_c) — the boundary between the TGI zone and the fully qualified temporal layer above it. Operations near z_c may be affected by the residual interface effects captured in the SC_eff map, even if the layer they occupy is nominally SC-I.

**TPR-001 — TGI ceiling clearance:** Operations committed in layers within 5 nm above z_c MUST satisfy the SC_eff-derived Δτ_eff for their die location rather than the SC_bulk-derived Δτ_eff. If SC_eff < SC_bulk at that location, this rule is more restrictive.

**TPR-002 — Non-monotonic CLG exclusion zone:** In die regions where the TGI metrology spatial map records a CLG non-monotonicity finding (as defined in §9.3 of The TGI Metrology Standard), no temporal operations MUST be assigned to layers within 10 nm above z_c. This exclusion zone applies regardless of SC_eff in that region; a non-monotonic CLG indicates a buried low-coherence layer whose effect on operations immediately above it is not fully captured by the SC_eff computation.

**TPR-003 — TGI floor keep-out:** No temporal operations MUST be assigned to layers within the TGI zone itself — between z_f and z_c inclusive. The TGI zone is a transition region, not a qualified temporal layer.

**R-TDR-02:** TPR rules MUST be evaluated using the layer z-coordinate of each operation's assigned layer, referenced to the process stack definition in the PDK. Operations without a defined z-coordinate assignment in the intent map cannot be evaluated for TPR compliance and MUST be flagged as a CGR violation (§5.5).

### 5.5 Causal Graph Rules (CGR)

Causal graph rules constrain the structure of the operation dependency graph that the TRS L2 Sequencing Layer receives as input. A dependency graph that violates these rules cannot be sequenced by L2 and will generate arbitration failures at the Commit Arbiter.

**CGR-001 — Acyclicity:** The operation dependency graph MUST be a directed acyclic graph (DAG). Any cycle — a sequence of dependencies that returns to its origin — is a sequencing deadlock. CGR-001 is a hard rule: no waivers are permitted.

**CGR-002 — Bounded fan-in:** No single operation MUST have more than F_in_max predecessor dependencies, where F_in_max is taken from the coherence budget tables (§6) for the target SCR zone. An operation with excessive fan-in creates a sequencing bottleneck: the CA cannot authorize it until all predecessors are acknowledged, and if those predecessors span multiple zones, the L_handoff latency stack can exceed the available coherence budget.

**CGR-003 — Bounded fan-out:** No single operation MUST have more than F_out_max successor dependencies. Excessive fan-out concentrates the causal ordering load on one operation's acknowledgment signal; if that operation is deferred (per the CA deferred-slot procedure), all successors are simultaneously deferred, potentially starving multiple coherence slots.

**CGR-004 — Cross-zone dependency depth:** A chain of dependencies that crosses k zone boundaries incurs a minimum latency of k × L_handoff coherence cycles. The total cross-zone latency of any dependency chain MUST NOT exceed the CBA coherence budget allocation for inter-zone operations. Chains that exceed this allocation cannot be scheduled within the coherence cycle budget.

**CGR-005 — Unresolved operation identifiers:** Every predecessor operation identifier referenced in the dependency graph MUST correspond to an operation present in the same design's intent map. References to undefined operation identifiers are non-conformant; they represent dependencies that L1 cannot resolve before passing to L2.

**R-TDR-03:** CGR-001 (acyclicity) MUST be checked before any other CGR rule. A cyclic graph produces undefined behavior in subsequent rule checks and MUST be reported as a blocking error requiring design correction before TDRC can continue.

### 5.6 Coherence Slot Rules (CSR)

Coherence slot rules constrain the assignment of operations to coherence slots, ensuring that no slot is oversubscribed and that the slot assignments are consistent with the SCR zone configuration.

**CSR-001 — Slot capacity:** The number of operations assigned to any single coherence slot MUST NOT exceed N_slot_max from the TSPS for the layer's SC class.

**CSR-002 — Zone slot index validity:** Coherence slot assignments MUST use slot indices in the range [0, N_slots − 1], where N_slots is the zone's qualified slot count from the coherence budget tables. Slot indices outside this range are non-conformant.

**CSR-003 — Slot-address consistency:** An operation assigned to coherence slot s MUST have a temporal address τ that falls within the address subrange associated with slot s in the coherence budget tables. Slot s is associated with address subrange [s/N_slots, (s+1)/N_slots). Operations whose address and slot assignment are inconsistent will be rejected by the L1 Intent Layer.

**CSR-004 — Reserved slot margins:** The first and last coherence slot of each cycle (slot 0 and slot N_slots − 1) are reserved for SCR synchronization traffic. Design operations MUST NOT be assigned to slots 0 or N_slots − 1.

---

## 6. Coherence Budget Tables

### 6.1 Purpose

Coherence Budget Tables encode the temporal resource constraints imposed by the SCR zone configuration. They are the primary input to the CBA (Coherence Budget Analysis) tool, which verifies that the design's total operation count, distributed across SCR zones, fits within the coherence cycle budget at the target temporal density.

### 6.2 Budget Table Structure

A separate Coherence Budget Table (CBT) is provided for each SCR zone configuration present in the target fab. A fab with a single zone has one CBT; a multi-zone fab has one CBT per zone plus a cross-zone budget section.

Each CBT record contains:

**Zone identification:**

| Field | Definition |
|---|---|
| `zone_id` | Zone identifier matching the SCR qualification record |
| `scr_config_id` | SCR zone configuration record ID |
| `fab_id` | Facility identifier |

**Timing parameters (from SCR qualification record):**

| Field | Symbol | Unit | Source |
|---|---|---|---|
| `coherence_cycle_period` | T_c | ns | SCR qualification |
| `synchronization_latency_floor` | SLF | ns | SCR qualification |
| `slot_count` | N_slots | integer | SCR qualification |
| `slot_period` | T_slot = T_c / N_slots | ns | Derived |
| `arbiter_processing_latency` | T_arb | ns | SCR qualification |
| `max_deferral_count` | D_max | integer | SCR qualification |

**Capacity parameters:**

| Field | Symbol | Unit | Definition |
|---|---|---|---|
| `operations_per_slot_max` | N_slot_max | ops | From TSPS for the zone's qualified SC class |
| `operations_per_cycle_max` | N_cycle_max = N_slot_max × (N_slots − 2) | ops | Derived; excludes reserved slots 0 and N_slots−1 |
| `temporal_density_limit` | TD_limit | ops/cycle/mm² | MQD for the zone's SC class |
| `zone_active_area` | A_zone | mm² | Physical area of the zone covered by TCUs |
| `total_cycle_budget` | B_cycle = TD_limit × A_zone | ops/cycle | Derived; the hard ceiling for CBA |

**Fan-in/fan-out limits:**

| Field | Symbol | Unit | Source |
|---|---|---|---|
| `max_fan_in` | F_in_max | predecessors | Derived from T_arb and T_slot; F_in_max = floor(T_slot / T_arb) |
| `max_fan_out` | F_out_max | successors | Fixed at 32 for this revision; process-specific values MAY override |

**R-CBT-01:** The CBT MUST be regenerated whenever any of the following SCR parameters change: T_c, N_slots, SLF, T_arb, D_max, zone physical extent. A PDK with a CBT derived from stale SCR parameters is non-conformant for production use.

**R-CBT-02:** The CBT `total_cycle_budget` value MUST be confirmed against the actual CMA-monitored coherence utilization data from at least one production lot before the PDK is released for volume production. Simulation-derived budget values that have not been validated against production data are provisional; PDKs containing provisional CBTs MUST carry a `PROVISIONAL` flag in the PDK version record.

### 6.3 Cross-Zone Budget Section

For multi-zone fabs, the CBT package includes a cross-zone budget section that encodes the inter-zone handoff latency contracts from the SCR Specification:

| Field | Definition |
|---|---|
| `zone_pair` | Ordered pair (zone_A_id, zone_B_id) representing a directional inter-zone link |
| `L_handoff` | Handoff latency in Zone B coherence cycles; from the SCR qualification record |
| `zbi_message_latency` | T_ZBI in ns; from ZBI commissioning measurement |
| `cross_zone_budget_fraction` | Maximum fraction of B_cycle that may be consumed by cross-zone dependent operations; default 0.20 |

The `cross_zone_budget_fraction` reflects that cross-zone operations are latency-penalized relative to intra-zone operations. Dedicating more than 20% of the coherence budget to cross-zone traffic creates scheduling pressure that elevates deferral rates toward D_max.

**R-CBT-03:** CBA tools MUST enforce the `cross_zone_budget_fraction` limit separately from the total `B_cycle` limit. A design may pass total budget analysis while failing the cross-zone fraction limit if its dependency graph is heavily biased toward zone-crossing paths.

---

## 7. TTF Arc Library

### 7.1 The Temporal Timing Format

The **Temporal Timing Format (TTF)** is the standardized format for expressing temporal manufacturing timing constraints as arcs in a timing model consumable by STA tools. TTF extends classical static timing analysis — which reasons about spatial propagation delays through logic gates and interconnect — with arc types that model delays and constraints arising from TRS commit sequencing, SCR coherence slot assignments, and inter-zone handoff latency.

The TTF arc library delivered in the PDK is the complete set of TTF arcs characterizing the target process node and SCR zone configuration. It is the primary input to any TTF-aware STA tool performing temporal timing closure.

The full TTF syntax and arc type definitions are specified in the TTF Reference ([`docs/eda/TTF_Reference.md`](../eda/TTF_Reference.md)). This section specifies which arc types MUST be present in the PDK TTF arc library and how their values are derived from upstream measurements.

### 7.2 Required Arc Types

#### 7.2.1 Commit Sequencing Arc (CSA)

The commit sequencing arc models the latency introduced by the TRS L2 Sequencing Layer for a single operation, from intent-layer delivery to commit-layer authorization.

```
TTF_ARC  COMMIT_SEQUENCING
  TYPE          CSA
  SC_CLASS      {SC-I | SC-II}
  MIN_DELAY     T_seq_min  (coherence cycles)
  MAX_DELAY     T_seq_max  (coherence cycles)
  SOURCE        TSPS
  TSPS_REF      {TSPS_record_ID}
END_ARC
```

T_seq_min and T_seq_max represent the best-case and worst-case sequencing latency. T_seq_min applies when the operation has no predecessor conflicts and is assigned to its nominal slot. T_seq_max = T_seq_min + D_max applies when the operation is deferred the maximum permitted number of times.

**R-TTFAL-01:** Both T_seq_min and T_seq_max MUST be present in the CSA arc. STA tools that model only best-case or worst-case sequencing will respectively miss timing violations and generate false negatives.

#### 7.2.2 Zone Boundary Arc (ZBA)

The zone boundary arc models the latency incurred when a dependency crosses a zone boundary via the ZBI inter-zone handoff protocol.

```
TTF_ARC  ZONE_BOUNDARY
  TYPE          ZBA
  ZONE_PAIR     {zone_A_id}  {zone_B_id}
  L_HANDOFF     {value}      (Zone B coherence cycles)
  T_ZBI_NS      {value}      (nanoseconds; from ZBI commissioning)
  SOURCE        SCR_QUALIFICATION
  SCR_ZONE_CFG  {scr_zone_config_id}
END_ARC
```

A ZBA is directional: the arc from Zone A to Zone B reflects L_handoff measured in Zone B cycles. If Zone A and Zone B have different coherence cycle periods, the STA tool MUST use Zone B's T_c for arc delay computation when the dependency crosses from A to B, and Zone A's T_c when it crosses from B to A.

**R-TTFAL-02:** A ZBA MUST be provided for every ordered zone pair (A→B) and its reverse (B→A) in the fab configuration. Directed arcs for both directions are required because L_handoff is asymmetric when zone cycle periods differ.

#### 7.2.3 Arbiter Processing Arc (APA)

The arbiter processing arc models the CA processing latency T_arb — the delay from the SCR slot boundary to the TAIS authorization signal assertion.

```
TTF_ARC  ARBITER_PROCESSING
  TYPE          APA
  ZONE_ID       {zone_id}
  T_ARB_NS      {value}      (nanoseconds; from SCR qualification)
  T_AUTH_NS     {value}      (setup window; from SCR qualification)
  SOURCE        SCR_QUALIFICATION
  SCR_ZONE_CFG  {scr_zone_config_id}
END_ARC
```

The APA is used by STA tools to model the window between the coherence slot boundary and the earliest moment at which a TCU can begin its commit operation. T_AUTH_NS is the setup margin (the T_auth window from the SCR Specification) within which the CA must assert authorization before the slot boundary.

#### 7.2.4 TAOE Correction Arc (TCA)

The TAOE correction arc encodes the systematic component of temporal address overlay error (TAOE_sys) as a position-dependent timing offset. This arc type is unique to TRS-aware STA: it represents the spatial pattern of address registration offset measured by TGI metrology, expressed as a timing perturbation to operations in die regions where the STR systematic gradient is non-zero.

```
TTF_ARC  TAOE_CORRECTION
  TYPE          TCA
  LAYER         {layer_name}
  DIE_REGION    {x_min_um}  {y_min_um}  {x_max_um}  {y_max_um}
  TAU_OFFSET    {value}     (normalized address units; signed)
  ADDR_GRADIENT {value}     (addr. units/mm; in-plane systematic gradient)
  SOURCE        TGI_METROLOGY
  TGI_REPORT_ID {report_id}
END_ARC
```

When PIMC (Predictive Intent Map Correction) is applied to the design, the TCA offsets are pre-compensated in the TRS intent map and SHOULD be set to zero in the PDK TTF arc library for that lot. When PIMC is not applied, the TCA arcs represent uncorrected systematic address offsets that the STA tool must treat as timing perturbations.

**R-TTFAL-03:** TCA arcs MUST be derived from the TGI metrology TAOE_sys spatial map for the qualified substrate lot. TCA arcs derived from modeled or extrapolated TAOE values are non-conformant.

**R-TTFAL-04:** A TCA arc MUST be provided for every die region in the spatial SC variation map (§3.3) where |TAOE_sys| > 0.001 normalized address units. Regions with |TAOE_sys| ≤ 0.001 MAY be assigned zero-valued TCA arcs or omitted, as they are within the instrument noise floor.

#### 7.2.5 Density-Dependent Derating Arc (DDA)

The density-dependent derating arc encodes the reduction in effective timing margin that occurs when a die region operates near its RWDL. As temporal density approaches the RWDL, TAOE_rnd increases and commit fidelity degrades — a phenomenon that manifests in the timing model as a reduction in the available margin for operations in high-density regions.

```
TTF_ARC  DENSITY_DERATING
  TYPE           DDA
  LAYER          {layer_name}
  DIE_REGION     {x_min_um}  {y_min_um}  {x_max_um}  {y_max_um}
  TD_DESIGN      {value}     (ops/cycle/mm²; design's intended density in this region)
  RWDL           {value}     (ops/cycle/mm²; from TGI metrology)
  DERATING_SLOPE {value}     (addr. units per unit density fraction; from TSPS)
  SOURCE         TGI_METROLOGY + TSPS
END_ARC
```

The derating slope converts the fractional proximity to RWDL (TD_design / RWDL) into a timing margin reduction in address units. The slope is derived from the TSPS material record and reflects the empirically characterized relationship between density loading and TAOE_rnd for the qualified substrate class.

**R-TTFAL-05:** DDA arcs MUST be evaluated at final routed density, not at pre-route estimated density. PDK releases used for pre-route timing analysis MUST include a disclaimer that DDA derating is estimated and MUST be rechecked at final route.

### 7.3 TTF Arc Library File Format

TTF arcs are encoded in the Temporal Timing Format as specified in [`docs/eda/TTF_Reference.md`](../eda/TTF_Reference.md). Each arc type is stored in a separate file within the `ttf/` subdirectory of the PDK package (§10). The master TTF library manifest (`ttf/MANIFEST.ttf`) lists all arc files, their types, and their source traceability references.

**R-TTFAL-06:** The TTF library manifest MUST be present and MUST enumerate every arc file in the `ttf/` directory. STA tools that load the PDK MUST validate the manifest against the directory contents before accepting the arc library as complete.

---

## 8. Temporal Crosstalk Rules

### 8.1 Physical Mechanism

Temporal crosstalk is the perturbation induced at one temporal address by a high-density cluster of commit operations at an adjacent address in a spatially proximate substrate region. It is distinct from classical electromagnetic crosstalk in two respects:

1. **Direction:** Classical crosstalk propagates spatially (from aggressor net to victim net). Temporal crosstalk propagates in the address domain (from aggressor address cluster to victim address), at a fixed spatial location or within a spatial radius determined by the coherence length.

2. **Mechanism:** Classical crosstalk arises from capacitive or inductive coupling between conductors. Temporal crosstalk arises from the inter-site interaction mechanism in the substrate — the same mechanism quantified in the TCT address pattern design as the basis for d_pair — when a high density of operations at one address collectively perturbs the phase state of the substrate at a neighboring address.

Temporal crosstalk is directional in the density sense: a low-density address adjacent to a high-density address receives more perturbation than a high-density address adjacent to a low-density address, because the high-density cluster generates a larger aggregate field in the substrate phase state.

### 8.2 Crosstalk Interaction Model

The temporal crosstalk-induced address shift Δτ_xtalk at a victim address τ_v caused by an aggressor cluster at address τ_a is modeled as:

```
Δτ_xtalk = K_xtalk × TD_aggressor × G(|τ_v − τ_a|) × H(d_spatial)

Where:
  K_xtalk        = crosstalk coupling constant (material-class-specific; from TSPS)
  TD_aggressor   = temporal density of the aggressor cluster (ops/cycle/mm²)
  G(Δτ)          = address-domain coupling function; G(Δτ) = exp(−Δτ / Δτ_decay)
  Δτ_decay       = address-domain coupling decay length (addr. units; from TSPS)
  H(d_spatial)   = spatial coupling function; H(d) = exp(−d / L_c) for d ≤ r_int, 0 otherwise
  d_spatial      = spatial distance between aggressor and victim commit sites (μm)
```

The coupling functions G and H capture the two-dimensional nature of temporal crosstalk: coupling decays both with address separation (G) and with physical distance (H), becoming negligible beyond the interaction radius r_int.

### 8.3 Crosstalk Rule Format

Temporal crosstalk rules are expressed as maximum permitted aggressor density limits as a function of address separation and spatial distance from the victim:

**TCRS-001 — Absolute aggressor density limit:** For any victim address τ_v, the aggregate temporal density of all aggressors within the interaction radius r_int and within address separation Δτ_eff of τ_v MUST NOT cause Δτ_xtalk to exceed 10% of Δτ_eff for the victim address's SC class.

**TCRS-002 — Aggressor cluster rule:** A cluster of operations sharing the same temporal address and occupying a continuous spatial region exceeding 100 μm × 100 μm MUST be checked for temporal crosstalk impact on all addresses within Δτ_eff in all adjacent die regions within r_int. This rule targets the highest-risk configuration — a large, spatially coherent, high-density cluster — that produces the largest Δτ_xtalk.

**TCRS-003 — Density tier stratification:** The crosstalk coupling constant K_xtalk takes different values at different density tiers relative to RWDL:

| Density Tier | Condition | K_xtalk Multiplier |
|---|---|---|
| Low | TD ≤ 0.50 × RWDL | 1.0 (base value from TSPS) |
| Medium | 0.50 < TD ≤ 0.75 × RWDL | 1.4 |
| High | 0.75 < TD ≤ 0.90 × RWDL | 2.1 |
| Near-limit | TD > 0.90 × RWDL | 3.0 |

The multipliers reflect non-linear growth in inter-site interaction strength as density approaches the substrate clarity limit. Near-limit density produces disproportionately large crosstalk because operations are committed at spacings approaching the minimum resolvable Δτ, where phase state overlap is significant.

**R-TCRS-01:** TDRC tools MUST evaluate TCRS rules after ASR rules, using the ASR-confirmed address assignments as the basis for aggressor density computation. Evaluating TCRS before ASR produces incorrect aggressor density estimates because addresses may shift during ASR correction.

**R-TCRS-02:** The K_xtalk base value and Δτ_decay MUST be taken from the TSPS for the victim address's SC class, not the aggressor's. The victim's substrate environment governs susceptibility; the aggressor's density governs exposure.

---

## 9. RWDL and SC_eff Map Integration

### 9.1 Purpose

The Registration-Weighted Density Limit (RWDL) and SC_eff maps from TGI metrology are spatial maps of the maximum safe temporal density and effective substrate clarity at each die location. They are the outputs of the TGI Metrology Standard's data analysis workflow and the most directly design-relevant products of the metrology program.

In the PDK, these maps serve two distinct roles:

1. **Rule parameterization:** RWDL values feed directly into DGR-001 (density gradient rules) and the DDA arc computation. SC_eff values feed into TPR-001 (TGI ceiling clearance) and the SCLM SC_design field.
2. **Floorplanning guidance:** RWDL and SC_eff maps, presented as heat maps in the PDK documentation, allow designers to make informed floorplanning decisions about where to place high-density temporal blocks.

### 9.2 Map Ingestion and Format

RWDL and SC_eff maps are ingested from TGI Metrology Reports and encoded in TLMF format (§3.4) as additional subregion fields within each `LAYER` record:

```
LAYER  {layer_name}  {z_bottom_nm}  {z_top_nm}  {SC_designation}
  SUBREGION  {x_min_um}  {y_min_um}  {x_max_um}  {y_max_um}
    SC_BULK     {value}
    SC_EFF      {value}
    SC_DESIGN   {value}
    SC_CLASS    {SC-I | SC-II | SC-III | SPATIAL}
    RWDL        {value}   # ops/cycle/mm²
    RWDL_SOURCE {TGI_report_ID}
  END_SUBREGION
END_LAYER
```

**R-RWDL-01:** RWDL values MUST be present for every subregion in every temporal layer's TLMF record. A subregion without an RWDL value is treated as RWDL = 0 by compliant TDRC tools — effectively prohibiting all temporal operations in that subregion. This conservative default ensures that missing data does not silently permit over-density.

**R-RWDL-02:** RWDL values MUST be derived from the TGI Metrology Report for the specific substrate lot being qualified. RWDL values estimated from prior lots or from material models without measurement evidence are non-conformant for production PDKs and are permissible only in provisional PDKs (§13.4).

### 9.3 RWDL Margin Policy

The RWDL value delivered in the PDK is the raw TGI-metrology-derived RWDL, without additional margin applied at the PDK level. Margin is applied at the design level: designers are responsible for leaving a design margin between their intended temporal density and the RWDL.

The recommended design margin is:
- **SC-I layers:** 15% below RWDL (TD_design ≤ 0.85 × RWDL)
- **SC-II layers:** 20% below RWDL (TD_design ≤ 0.80 × RWDL)

These are recommendations, not enforced PDK rules. Designs that operate closer to RWDL are not blocked by TDRC but will experience higher DDA derating (§7.2.5) and elevated TCRS multipliers (§8.3).

### 9.4 SC_eff Consistency Check

When the PDK is generated, a consistency check MUST be performed between the SC_eff values in the TLMF records and the SC_bulk values from the TCT spatial SC map:

**R-RWDL-03:** For any subregion where SC_eff > SC_bulk, the TLMF record MUST flag the inconsistency and use SC_bulk as SC_design. SC_eff cannot exceed SC_bulk — the TGI boundary can only reduce or maintain the bulk SC, never increase it. An SC_eff > SC_bulk result indicates a measurement error in either the TCT or TGI metrology and MUST be escalated to the metrology team before the PDK is released.

---

## 10. PDK Deliverable Structure

### 10.1 Directory Layout

A conformant TRS-Aware PDK release is a versioned directory package with the following structure:

```
{pdk_version}/
├── MANIFEST.pdk          # Master manifest: lists all files, checksums, and version metadata
├── RELEASE_NOTES.md      # Human-readable description of changes from prior version
├── SIGN_OFF.pdk          # Sign-off record with authority chain signatures
│
├── layer_stack/
│   ├── layer_stack.tlmf  # Full process stack definition in TLMF format
│   ├── layer_stack.pdf   # Human-readable layer stack diagram
│   └── tgi_zone.tlmf     # TGI zone-specific TLMF sub-record
│
├── tsps/
│   ├── tsps_SC-I.tpsf    # TRS Stack Parameter Set for SC-I layers
│   ├── tsps_SC-II.tpsf   # TRS Stack Parameter Set for SC-II layers
│   └── TSPS_MANIFEST.md  # Lists all TSPS files and their source TRS Qualification Records
│
├── tdr/
│   ├── asr.tdr           # Address Spacing Rules
│   ├── dgr.tdr           # Density Gradient Rules
│   ├── tpr.tdr           # TGI Proximity Rules
│   ├── cgr.tdr           # Causal Graph Rules
│   ├── csr.tdr           # Coherence Slot Rules
│   ├── tcrs.tdr          # Temporal Crosstalk Rule Set
│   └── TDR_MANIFEST.md   # Lists all TDR files, rule counts, and source traceability
│
├── cbt/
│   ├── cbt_{zone_id}.cbt # Coherence Budget Table per zone
│   ├── cbt_cross_zone.cbt # Cross-zone budget section (multi-zone fabs only)
│   └── CBT_MANIFEST.md   # Lists all CBT files and their source SCR configuration records
│
├── ttf/
│   ├── csa_{SC_class}.ttf   # Commit Sequencing Arcs per SC class
│   ├── zba_{zone_pair}.ttf  # Zone Boundary Arcs per zone pair
│   ├── apa_{zone_id}.ttf    # Arbiter Processing Arcs per zone
│   ├── tca_{layer}.ttf      # TAOE Correction Arcs per temporal layer
│   ├── dda_{layer}.ttf      # Density-Dependent Derating Arcs per temporal layer
│   └── MANIFEST.ttf         # TTF library manifest per R-TTFAL-06
│
├── sc_maps/
│   ├── sc_map_{layer}.tlmf  # Per-layer SC variation maps with RWDL and SC_eff
│   ├── sc_map_summary.pdf   # Human-readable heat maps for all temporal layers
│   └── SC_MAP_MANIFEST.md   # Source TCT and TGI report IDs per layer
│
├── crosstalk/
│   ├── xtalk_model.tpsf     # Crosstalk coupling constants and decay parameters
│   └── xtalk_lookup.csv     # Pre-computed Δτ_xtalk lookup table by density tier and spacing
│
├── docs/
│   ├── pdk_user_guide.md    # EDA tool integration instructions
│   ├── pdk_changelog.md     # Full change history across all versions
│   └── traceability.md      # Cross-reference of all PDK data to source measurement records
│
└── qualification/
    ├── tdrc_testcase_results.log   # TDRC qualification test suite results (§13)
    ├── cba_testcase_results.log    # CBA qualification test suite results (§13)
    ├── ttf_testcase_results.log    # TTF STA qualification test suite results (§13)
    └── pdk_qual_summary.md         # Qualification summary with pass/fail status per test
```

**R-STRUCT-01:** Every file listed in `MANIFEST.pdk` MUST be present with a matching SHA-256 checksum. PDK packages with missing files or checksum mismatches MUST be rejected by EDA tool loaders before any rule or arc data is consumed.

**R-STRUCT-02:** The `SIGN_OFF.pdk` file MUST be present and MUST contain the signatures of all required sign-off authorities (§13.3) before the PDK is distributed. An unsigned PDK MUST NOT be used for tape-out signoff.

---

## 11. PDK Generation Workflow

### 11.1 Workflow Overview

The PDK generation workflow is the pipeline that assembles upstream measurement data into a conformant PDK package. It is executed whenever a new PDK version is required (§14.2). The workflow has six phases executed in sequence:

```
Phase 1: Data Ingestion
        ↓
Phase 2: Consistency Validation
        ↓
Phase 3: Rule and Parameter Derivation
        ↓
Phase 4: File Generation and Formatting
        ↓
Phase 5: Qualification Test Suite Execution
        ↓
Phase 6: Sign-off and Release Packaging
```

No phase may proceed until the preceding phase has completed without errors. A generation run that halts in any phase before sign-off does not produce a valid PDK release.

### 11.2 Phase 1 — Data Ingestion

The following upstream data sources are ingested at the start of every PDK generation run. All sources must be present; a generation run with missing sources MUST abort.

| Data Source | Required Fields | Providing Protocol |
|---|---|---|
| TCT Report(s) | SC rating, SC class, spatial SC map, lot ID | TCT Protocol |
| TGI Metrology Report(s) | SC_eff map, RWDL map, TAOE_sys map, CLG non-monotonicity flags | TGI Metrology Standard |
| TRS Qualification Record | TSPS parameter values, qualified MQD, lot ID | TRS Qualification Procedure |
| SCR Zone Qualification Record(s) | T_c, N_slots, SLF, T_arb, D_max, L_handoff per zone pair | SCR Specification |
| Process Stack Definition | Layer names, z coordinates, SC designations, TGI zone boundaries | Process engineering record |

**R-GEN-01:** All ingested data sources MUST be for the same substrate lot or, for SCR records, for the specific zone configuration in which the substrate lot will be processed. Cross-lot or cross-zone mixing of data sources is non-conformant unless all lots carry the same SC class assignment and the PDK generation record documents the mixing with justification.

### 11.3 Phase 2 — Consistency Validation

Before any rule derivation, the ingested data is validated for internal consistency:

- TCT SC_bulk and TGI SC_eff are compared per subregion; any SC_eff > SC_bulk is flagged per R-RWDL-03
- TRS Qualification Record substrate lot ID is confirmed to match the TCT Report lot ID
- SCR T_c is confirmed to satisfy T_c > SLF × 1.05 per R-SLF-01
- CLG non-monotonicity flags from TGI metrology are checked; affected die regions are automatically assigned TPR-002 exclusion zones
- TSPS Δτ_eff is confirmed to be ≥ 1.15 × Δτ_min for SC-I and ≥ 1.20 × Δτ_min for SC-II per R-TSPS-02

Any consistency failure halts the generation run. The failure is logged with the specific inconsistency and the affected source records.

### 11.4 Phase 3 — Rule and Parameter Derivation

Rules and parameters are derived from the validated input data in the following order:

1. SC Class Layer Maps (TLMF records per layer) — from TCT spatial SC map + TGI SC_eff map
2. TRS Stack Parameter Sets — directly from TRS Qualification Record
3. Temporal Design Rules — derived in order: ASR → DGR → TPR → CGR → CSR → TCRS
   - ASR thresholds computed from Δτ_eff per SC class and the interaction radius r_int
     derived from L_c in the TSPS material record
   - DGR ΔTD_max values computed from RWDL per die subregion
   - TPR exclusion zones applied automatically at any subregion flagged for CLG
     non-monotonicity in the TGI metrology data
   - CGR limits F_in_max and F_out_max populated from CBT-derived slot timing
   - CSR reserved-slot indices assigned from N_slots in the CBT
   - TCRS coupling constants K_xtalk and Δτ_decay populated from TSPS material record;
     density tier multiplier table is fixed by this specification and not re-derived

4. Coherence Budget Tables — assembled per zone from the SCR zone qualification records;
   cross-zone section assembled from all measured ZBI L_handoff values

5. TTF Arc Library — arcs derived in the following order, each depending on the prior:
   - APA arcs: directly from T_arb and T_auth in SCR qualification record
   - CSA arcs: from T_seq in TSPS; T_seq_max = T_seq_min + D_max
   - ZBA arcs: from L_handoff and T_ZBI per zone pair in SCR record
   - TCA arcs: from TAOE_sys spatial map in TGI metrology report; zero-valued arcs
     written for regions where |TAOE_sys| ≤ 0.001
   - DDA arcs: from RWDL spatial map and TSPS derating slope; populated with
     TD_design field left as a placeholder at generation time — STA tools fill this
     field at analysis time from the design's actual routed density

6. Spatial SC and RWDL maps — TLMF subregion records merged from TCT spatial SC map
   and TGI metrology RWDL and SC_eff maps; SC_design set to min(SC_bulk, SC_eff) per
   subregion; SC_class_local assigned from SC_design

7. Temporal Crosstalk rule set — K_xtalk lookup table populated; pre-computed
   Δτ_xtalk lookup table generated by evaluating the crosstalk interaction model
   across all combinations of density tier, Δτ spacing, and spatial distance up to
   r_int, and written to `crosstalk/xtalk_lookup.csv`

8. Traceability index — a cross-reference table mapping every PDK data field to its
   source measurement record (TCT Report ID, TGI Report ID, TRS Qual Record ID, SCR
   Zone Config ID). This index is written to `docs/traceability.md` and is a required
   deliverable of Phase 3

**R-GEN-02:** Steps 3 through 8 MUST be executed by an automated generation script,
not by manual data entry. Manual PDK data entry is non-conformant regardless of the
review process applied afterward. Automation is required because the volume and
interdependency of derived values makes manual entry error rates unacceptably high.

**R-GEN-03:** The generation script MUST emit a machine-readable generation log that
records, for every output field: the input values used, the formula or rule applied,
and the computed output. The generation log is a primary audit artifact and MUST be
retained with the PDK release package for the life of the PDK version.

### 11.5 Phase 4 — File Generation and Formatting

Phase 4 converts the derived rule and parameter data into the file formats specified
for each PDK component category and assembles the directory structure of §10.1.

**Schema validation:** Each generated file MUST be validated against its format schema
before being accepted into the package:

| File type | Schema | Validation tool |
|---|---|---|
| `.tlmf` | TLMF schema | `tlmf-validate` per TLMF_Schema.md |
| `.tpsf` | TPSF key-value schema | `tpsf-validate` |
| `.tdr` | TDR rule schema | `tdr-validate` |
| `.cbt` | CBT schema | `cbt-validate` |
| `.ttf` | TTF arc schema per arc type | `ttf-validate` per TTF_Reference.md |

**R-GEN-04:** Any file that fails schema validation MUST be treated as a Phase 4
failure. The generation run halts; Phase 5 MUST NOT begin until the validation failure
is corrected and the affected files are regenerated and re-validated.

**Checksum generation:** After all files pass schema validation, SHA-256 checksums are
computed for every file in the package and written into `MANIFEST.pdk`. The manifest
itself is checksummed last, and its checksum is recorded in `SIGN_OFF.pdk`.

**R-GEN-05:** The `MANIFEST.pdk` checksum MUST be recomputed from scratch at the
start of Phase 6. If any file has been modified between Phase 4 and Phase 6, the
checksum mismatch will be detected. Post-Phase-4 file modifications that are not
accompanied by a full Phase 5 re-execution are non-conformant.

### 11.6 Phase 5 — Qualification Test Suite Execution

Phase 5 executes the PDK qualification test suite (§13.2) against the assembled
package. The test suite verifies that the generated PDK produces correct results when
consumed by qualified EDA tools on defined test designs.

Phase 5 is fully automated. Its execution is recorded in the three test result logs
placed in the `qualification/` directory. A Phase 5 run that produces any FAIL result
in any test case halts the generation; Phase 6 MUST NOT begin until all test cases
pass.

The qualification test suite is described in full in §13. Phase 5 is its automated
execution step within the generation workflow.

### 11.7 Phase 6 — Sign-off and Release Packaging

Phase 6 is the final human-in-the-loop step of the generation workflow. It consists of:

1. **Engineering review:** A process engineer reviews the `pdk_qual_summary.md` from
   Phase 5, the `docs/traceability.md` from Phase 3, and the `RELEASE_NOTES.md`. The
   engineer confirms that all test cases passed, that all upstream source records are
   current, and that the release notes accurately describe all changes from the prior
   PDK version.

2. **Authority sign-off:** The sign-off authorities defined in §13.3 review and sign
   the `SIGN_OFF.pdk` record. All required signatures MUST be present before packaging.

3. **Release packaging:** The fully signed package is compressed, its outer archive is
   checksummed, and the release is published to the fab's PDK distribution system with
   the version identifier (§14.1) as the release tag.

4. **Downstream notification:** The yield management system, EDA tool administrators,
   and design teams are notified of the new PDK release. The notification includes the
   version identifier, a summary of changes from the prior version, and the list of
   upstream source records that changed since the last release.

**R-GEN-06:** The compressed release archive MUST be immutable after publication.
Post-publication corrections require a new PDK version with an incremented version
number per §14. Patch-in-place modifications to a published PDK are non-conformant.

---

## 12. EDA Tool Integration Requirements

### 12.1 Tool Certification Requirement

A TRS-Aware PDK is only useful if the EDA tools consuming it correctly implement its
temporal domain components. Tools that silently ignore TTF arcs, apply spatial DRC
rules only, or treat the temporal address map as unconstrained will produce designs
that pass tool verification but fail in the fab.

To address this, the TriadicFrameworks system defines a **Tool Certification** process.
EDA tools used for signoff-level analysis against a TRS-Aware PDK MUST be certified
for each tool function they perform. Certification is performed by running the tool
against the PDK qualification test suite (§13.2) in tool-evaluation mode and verifying
that results match the reference outputs.

**R-TOOL-01:** The PDK release package MUST NOT be used for tape-out signoff with any
EDA tool that is not certified for the tool functions exercised in that signoff. A
design signed off using a non-certified tool is non-conformant regardless of whether
the tool-reported results are correct.

**R-TOOL-02:** Tool certifications are PDK-version-specific. A tool certified against
PDK version X is not automatically certified against PDK version X+1. Re-certification
is required for each new PDK major or minor version (§14.1). Patch versions that do
not alter rule thresholds or arc values do not require re-certification.

### 12.2 TDRC Tool Requirements

A TDRC tool consuming this PDK MUST implement the following behaviors:

**Loading:**

- MUST ingest all `.tdr` files enumerated in `TDR_MANIFEST.md`
- MUST validate TLMF layer stack records against the process stack definition before
  commencing rule checks
- MUST load the spatial SC variation map and apply subregion-level SC_class_local to
  all rule threshold lookups, not lot-level SC class

**Rule evaluation order:**

TDRC tools MUST evaluate rule categories in the following sequence. Out-of-order
evaluation produces incorrect results because later categories depend on the outputs
of earlier ones:

```
1. CGR-001 (acyclicity check) — blocking; halt on failure
2. ASR rules — address spacing
3. TPR rules — TGI proximity (requires z-coordinate from layer stack)
4. DGR rules — density gradient (requires ASR-confirmed address assignments)
5. TCRS rules — temporal crosstalk (requires DGR-confirmed density map)
6. CSR rules — coherence slot validity
7. CGR-002 through CGR-005 — remaining causal graph rules
```

**R-TOOL-03:** TDRC tools MUST report violations with sufficient context for the
designer to resolve them: the specific rule violated, the violating operation
identifier(s), the spatial coordinates, the temporal addresses involved, and the
measured vs. required value. A violation report that identifies only the rule number
without operation context is non-conformant tool output.

**R-TOOL-04:** TDRC tools MUST produce a machine-readable violation log in addition
to any human-readable report. The violation log format is specified in
[`docs/data-formats/TDRC_Violation_Log_Schema.md`](../data-formats/TDRC_Violation_Log_Schema.md).
The violation log is consumed by the CGV tool for causal graph re-evaluation after
TDRC correction.

### 12.3 CBA Tool Requirements

A CBA tool consuming this PDK MUST implement the following behaviors:

**Loading:**

- MUST ingest the CBT for every SCR zone relevant to the design's die assignment
- MUST ingest the cross-zone budget section if the design's dependency graph contains
  any cross-zone arcs
- MUST accept the design's routed temporal density map as input, not the pre-route
  estimated map

**Budget evaluation:**

- MUST evaluate total B_cycle utilization per zone separately from cross-zone fraction
  utilization. Both limits apply independently; a design that passes total budget but
  exceeds cross-zone fraction fails CBA
- MUST flag any coherence slot that is assigned more than N_slot_max operations as a
  slot oversubscription violation, even if total B_cycle is not exceeded

**R-TOOL-05:** CBA tools MUST report the coherence budget utilization as a fraction of
B_cycle per zone in the signoff report, not only a pass/fail result. The fraction is
required for design margin tracking across PDK versions.

**R-TOOL-06:** CBA tools MUST accept the PROVISIONAL flag in CBT records and, when
present, elevate all budget utilization warnings by one severity level. A utilization
that would be an advisory on a validated CBT becomes a warning on a provisional CBT;
a warning becomes a blocking failure.

### 12.4 TTF-Aware STA Tool Requirements

A TTF-aware STA tool consuming this PDK MUST implement the following behaviors:

**Arc loading:**

- MUST ingest the full TTF arc library manifest and all enumerated arc files
- MUST validate the manifest checksum per R-TTFAL-06 before accepting any arc data
- MUST apply APA, CSA, and ZBA arcs to all temporal paths in the timing graph. These
  three arc types are unconditional; they apply to every temporal operation regardless
  of its die location
- MUST apply TCA arcs to operations in the die regions specified by each arc's
  `DIE_REGION` field. TCA arcs are spatially scoped and MUST NOT be applied to
  operations outside their specified region
- MUST apply DDA arcs using the design's actual routed density at each die region as
  the `TD_DESIGN` field. DDA arcs with unresolved `TD_DESIGN` placeholders MUST NOT
  be used for signoff

**Timing graph construction:**

- Zone boundary crossings in the dependency graph MUST be modeled as ZBA arcs, not as
  zero-delay edges. The ZBA arc latency is expressed in Zone B coherence cycles and
  MUST be converted to absolute time using Zone B's T_c before being added to the
  timing path
- The L_handoff latency is a minimum latency, not a maximum. STA tools MUST model ZBA
  arcs as minimum-delay constraints on the dependent operation's slot assignment; the
  dependent operation cannot be placed in a slot earlier than L_handoff cycles after
  the dependency's slot, but it may be placed later

**R-TOOL-07:** TTF-aware STA tools MUST distinguish temporal timing paths (those
containing at least one TTF arc) from classical spatial timing paths (those containing
only classical STA arcs) in their reporting. Mixed paths — those containing both TTF
and classical arcs — MUST be reported as temporal paths. The distinction is required
for sign-off review; temporal and spatial path timing budgets are managed separately.

**R-TOOL-08:** TTF-aware STA tools MUST report the breakdown of path delay by arc
type (APA, CSA, ZBA, TCA, DDA, classical) for every reported timing path. Aggregate
path delay without arc-type breakdown is insufficient for temporal timing closure.

### 12.5 CGV Tool Requirements

The Causal Graph Verification tool checks the design's operation dependency graph
against the CGR rules. It consumes:

- The design's intent map (operation graph with all dependency declarations)
- The CGR rule file from the PDK (`tdr/cgr.tdr`)
- The CBT for the target SCR zones (for F_in_max, F_out_max, and cross-zone depth
  limits)
- The TDRC violation log from the preceding TDRC run (to exclude operations that are
  pending address correction from the graph analysis)

**R-TOOL-09:** CGV tools MUST execute CGR-001 (acyclicity) as a standalone first
pass before loading CBT-derived limits. If the graph is cyclic, limits on fan-in,
fan-out, and cross-zone depth cannot be meaningfully evaluated because the cyclic
subgraph has unbounded path length.

**R-TOOL-10:** CGV tools MUST report every dependency chain that approaches or
exceeds the cross-zone latency budget as a warning, even if it does not strictly
violate CGR-004. Chains within 10% of the budget limit are candidates for
architectural refactoring and MUST be surfaced to the designer during the sign-off
review phase.

### 12.6 Signoff Flow Integration

The canonical signoff flow for a design targeting this PDK is:

```
Step 1  CGV — acyclicity check (CGR-001 only; fast, blocking if cyclic)
Step 2  TDRC — full rule evaluation (ASR → TPR → DGR → TCRS → CSR)
Step 3  CGV — full rule evaluation (CGR-002 through CGR-005; uses TDRC violation log)
Step 4  CBA — coherence budget analysis (requires TDRC-clean intent map)
Step 5  TTF STA — temporal timing analysis (requires CBA-confirmed slot assignments
        and DDA arcs populated with final routed density)
Step 6  Classical DRC/LVS — spatial verification (parallel to Steps 1–5 but must
        complete before tape-out)
Step 7  Signoff review — engineer reviews all tool reports; all checks must be clean
        or waivered per §13.4
```

**R-TOOL-11:** Steps 1 through 5 MUST be completed in the order listed. Running CBA
before TDRC produces an incorrect budget analysis because TDRC may change address
assignments, which changes density distribution. Running TTF STA before CBA produces
incorrect derating because DDA arc TD_design values depend on CBA-confirmed slot
assignments affecting the coherence-cycle-averaged density.

---

## 13. PDK Qualification and Sign-off

### 13.1 Qualification Purpose

PDK qualification verifies that the generated PDK produces correct, reproducible
results when consumed by certified EDA tools on a defined set of test designs. It is
the executable evidence that the PDK is internally consistent, correctly derived from
upstream measurements, and correctly consumed by the tools that will use it for
production design sign-off.

Qualification is required for every PDK major and minor version. Patch versions
require only a targeted re-qualification of the components that changed.

### 13.2 Qualification Test Suite

The test suite comprises three sections, each targeting a different PDK component
category.

#### 13.2.1 TDRC Test Cases

The TDRC test suite consists of a library of synthetic intent maps with known
violations and known-clean configurations. Each test case specifies:

- The test intent map (a minimal set of temporal operations with defined addresses,
  spatial coordinates, and dependencies)
- The expected TDRC outcome (clean, or a specific set of violations with their rule
  identifiers, operation identifiers, and measured vs. required values)

| Test Case | Targets | Expected Result |
|---|---|---|
| TDRC-TC-01 | ASR-001: two operations within r_int at Δτ < Δτ_eff | One ASR-001 violation |
| TDRC-TC-02 | ASR-001: same operations at Δτ = Δτ_eff + 0.001 | Clean |
| TDRC-TC-03 | ASR-004: SC-I and SC-II proximate pair at SC-I Δτ_eff | One ASR-004 violation |
| TDRC-TC-04 | ASR-004: same pair at SC-II Δτ_eff | Clean |
| TDRC-TC-05 | DGR-001: density step exceeding ΔTD_max between adjacent regions | One DGR-001 violation |
| TDRC-TC-06 | DGR-002: same step with compliant transition zone inserted | Clean |
| TDRC-TC-07 | TPR-001: operation within 5 nm of z_c in SC_eff-degraded subregion | One TPR-001 violation |
| TDRC-TC-08 | TPR-002: operation within 10 nm of z_c in CLG non-monotonicity subregion | One TPR-002 violation |
| TDRC-TC-09 | CSR-001: slot with N_slot_max + 1 operations | One CSR-001 violation |
| TDRC-TC-10 | CSR-004: operation assigned to slot 0 | One CSR-004 violation |
| TDRC-TC-11 | TCRS-001: aggressor density causing Δτ_xtalk > 10% of Δτ_eff | One TCRS-001 violation |
| TDRC-TC-12 | Fully compliant design spanning SC-I and SC-II regions | Clean across all rules |

**R-QUAL-01:** All 12 TDRC test cases MUST pass. A PDK release in which any test case
produces an unexpected result — either a missed violation or a false violation — is
non-conformant and MUST NOT be released until the discrepancy is resolved.

#### 13.2.2 CBA Test Cases

| Test Case | Targets | Expected Result |
|---|---|---|
| CBA-TC-01 | Single zone; total utilization at 95% of B_cycle | Clean; 95% utilization reported |
| CBA-TC-02 | Single zone; total utilization at 101% of B_cycle | B_cycle exceeded violation |
| CBA-TC-03 | Multi-zone; cross-zone fraction at 18% | Clean; fraction reported |
| CBA-TC-04 | Multi-zone; cross-zone fraction at 22% | Cross-zone fraction violation |
| CBA-TC-05 | Single slot oversubscribed; total B_cycle within budget | Slot oversubscription violation |
| CBA-TC-06 | Provisional CBT flag present; utilization at 82% | Warning elevated to blocking |

**R-QUAL-02:** All 6 CBA test cases MUST pass.

#### 13.2.3 TTF STA Test Cases

| Test Case | Targets | Expected Result |
|---|---|---|
| TTF-TC-01 | Single operation; APA + CSA arcs only | Path delay = T_arb + T_seq_min; no violations |
| TTF-TC-02 | Same operation at T_seq_max | Path delay = T_arb + T_seq_max; reported as maximum |
| TTF-TC-03 | Cross-zone dependency; ZBA arc applied | Path delay includes L_handoff × T_c(zone_B) |
| TTF-TC-04 | ZBA applied in wrong direction (B→A arc for A→B dependency) | Tool must reject; arc direction mismatch |
| TTF-TC-05 | TCA arc in affected die region; non-zero TAU_OFFSET | Offset applied to affected operations; clean outside region |
| TTF-TC-06 | DDA arc; TD_design at 92% RWDL (Near-limit tier) | Derating applied with multiplier 3.0; timing margin reduced |
| TTF-TC-07 | DDA arc; TD_design placeholder not resolved | Tool must report unresolved DDA arc; block signoff |
| TTF-TC-08 | Mixed temporal and spatial path; both arc types present | Path reported as temporal; breakdown by arc type present |

**R-QUAL-03:** All 8 TTF STA test cases MUST pass.

### 13.3 Sign-off Authority Chain

A PDK release requires signatures from the following authorities, applied in order.
No authority may sign before all preceding signatures are present.

| Authority | Role | Criteria for Signature |
|---|---|---|
| PDK Generation Engineer | Confirms generation log is complete and no Phase 1–4 errors occurred | Generation log reviewed; all schema validations passed |
| Metrology Lead | Confirms all upstream source records are current and within re-qualification intervals | TCT, TGI, TRS, SCR record dates reviewed against requalification schedules |
| Process Engineering Lead | Confirms TSPS parameter values are consistent with current process performance; reviews DGR and TPR rules for process risk | Parameter comparison to prior PDK version; process change log reviewed |
| EDA Tool Administrator | Confirms all signoff-flow tools are certified against this PDK version per R-TOOL-01 | Tool certification records reviewed |
| PDK Release Authority | Final approval; confirms all preceding signatures are present and qualification test suite is fully passing | `pdk_qual_summary.md` reviewed; SIGN_OFF.pdk countersigned |

**R-QUAL-04:** The PDK Release Authority MUST be a different individual from the PDK
Generation Engineer. Self-signed releases are non-conformant.

**R-QUAL-05:** All signatures in `SIGN_OFF.pdk` MUST be cryptographic signatures
(GPG or equivalent) tied to the signer's authenticated identity in the fab's PKI
system. Plaintext name fields without cryptographic binding are non-conformant for
production PDK releases. Provisional PDKs (§13.4) MAY use plaintext signatures.

### 13.4 Provisional PDKs

A provisional PDK is a PDK release intended for early design exploration before all
upstream measurement data is available. Provisional PDKs are valid for:

- Pre-layout floorplanning and density estimation
- Preliminary TDRC checks using estimated SC class and RWDL
- Architecture-level CBA with estimated coherence budget fractions

Provisional PDKs MUST NOT be used for:

- Tape-out sign-off
- TRS intent map generation for production lots
- Any signoff check that requires RWDL-derived or SC_eff-derived rule thresholds

**R-QUAL-06:** Provisional PDKs MUST carry a `PROVISIONAL` flag in the version
identifier (§14.1 format suffix `P`) and in the `MANIFEST.pdk` header. Certified EDA
tools MUST detect the `PROVISIONAL` flag and block sign-off operations when a
provisional PDK is loaded. A tool that permits tape-out sign-off against a provisional
PDK is non-conformant.

**R-QUAL-07:** A provisional PDK MUST be superseded by a full production PDK before
any design built with it reaches tape-out. The superseding production PDK MUST be
used for all final sign-off checks, even if the design was developed entirely against
the provisional PDK.

---

## 14. PDK Versioning and Change Control

### 14.1 Version Identifier Format

Every TRS-Aware PDK release carries a version identifier with the format:

```
{process_node}_{fab_id}_{scr_zone_config}_{major}.{minor}.{patch}[P]

Where:
  process_node    = process node identifier (e.g., TF-N3T)
  fab_id          = facility identifier (e.g., FAB01)
  scr_zone_config = SCR zone configuration identifier (e.g., ZC-A)
  major           = incremented for changes that alter tape-out sign-off requirements
  minor           = incremented for changes to rule thresholds or arc values that do
                    not alter sign-off requirements
  patch           = incremented for corrections, documentation updates, and file
                    format fixes that do not change any rule or arc value
  [P]             = optional suffix indicating a provisional PDK

Example: TF-N3T_FAB01_ZC-A_2.1.0
```

### 14.2 Version Increment Triggers

| Change Type | Version Component Incremented | Re-qualification Required |
|---|---|---|
| New upstream measurement data (new TCT, TGI, TRS, or SCR lot) | Minor | Full qualification suite |
| Change to SCR zone configuration (new T_c, N_slots, zone extent) | Major | Full qualification suite; tool re-certification |
| Addition of a new TDR rule category | Major | Full qualification suite; tool re-certification |
| Threshold or arc value change within an existing rule | Minor | Targeted re-qualification of affected test cases |
| Bug fix in generation script with no rule value change | Patch | Targeted re-qualification of affected test cases |
| Documentation correction with no data change | Patch | None |
| Format schema update (TLMF, TPSF, TTF) | Major if breaking, Minor if additive | Full if major, targeted if minor |
| New optional field in TLMF or TPSF (backward compatible) | Patch | None |

**R-VER-01:** Major version increments REQUIRE all designs currently in development
against the prior major version to be re-checked against the new major version before
tape-out. A design signed off against major version N is not valid for tape-out under
major version N+1.

**R-VER-02:** Minor version increments SHOULD prompt re-check of any design where
the changed threshold or arc value is within 20% of the design's measured slack. The
re-check is recommended, not mandatory, for minor versions.

**R-VER-03:** Patch version increments do not require re-check unless the patch
corrects a rule value that was previously incorrect. When a patch corrects a
previously incorrect rule value, the corrected value is treated as a minor version
change with respect to re-check requirements, even though the version component
incremented is patch.

### 14.3 Deprecation Policy

A PDK version is deprecated when a newer version of the same major release has been
available for 90 days. Deprecated versions:

- MUST NOT be used for new tape-out sign-off
- MAY continue to be used for in-progress designs that were signed off before
  deprecation, provided they do not require re-sign-off due to design changes
- MUST be clearly marked as deprecated in the PDK distribution system

A PDK version is retired when it has been deprecated for 180 days. Retired versions
are removed from active distribution. Access to retired PDK packages for archival
review requires a formal request to the PDK Release Authority.

### 14.4 Change Request Process

A change request (CR) is required for any planned modification to a released PDK.
CRs are also filed retrospectively when a defect in a released PDK is identified.

Each CR MUST contain:

- CR identifier (unique, sequential within the process node)
- Description of the proposed or discovered change
- Affected PDK components and version identifier
- Classification of the change (see §14.2 for version increment type)
- Impact assessment on designs currently signed off against the affected version
- Proposed corrective action
- Reference to upstream measurement records that motivate the change (if applicable)

CRs are reviewed by the same authority chain as PDK releases (§13.3). Approved CRs
result in a new PDK version. Rejected CRs are archived with the rejection rationale.

**R-VER-04:** When a CR identifies a defect that would have caused a design to pass
sign-off incorrectly under the defective PDK, the CR MUST be escalated to the PDK
Release Authority and Process Engineering Lead within 24 hours of identification. All
designs signed off against the defective PDK version MUST be reviewed for impact
before their wafers proceed to Tier 2 commit operations.

---

## 15. Glossary

| Term | Definition |
|---|---|
| **APA** | Arbiter Processing Arc — TTF arc encoding CA processing latency T_arb; applied to all temporal operations |
| **AER** | Address Error Rate — the fraction of committed address pairs that cannot be correctly recovered; defined in the TCT Protocol |
| **ASR** | Address Spacing Rules — TDR category enforcing minimum Δτ between spatially proximate temporal operations |
| **B_cycle** | Total coherence cycle budget; TD_limit × A_zone; the hard ceiling enforced by CBA |
| **CBA** | Coherence Budget Analysis — design verification check confirming total operation count fits within the SCR coherence cycle budget |
| **CBT** | Coherence Budget Table — PDK component encoding SCR zone timing parameters and capacity limits for CBA consumption |
| **CGR** | Causal Graph Rules — TDR category constraining the structure of the operation dependency graph |
| **CGV** | Causal Graph Verification — the EDA tool that checks CGR rules against the design's dependency graph |
| **CLG** | Coherence Layer Gradient — rate of change of normalized coherence capacity with depth through the TGI zone; defined in The TGI Metrology Standard |
| **CR** | Change Request — a formal record of a proposed or retrospective change to a released PDK |
| **CSA** | Commit Sequencing Arc — TTF arc encoding TRS L2 sequencing latency T_seq; applied to all temporal operations |
| **CSR** | Coherence Slot Rules — TDR category constraining operation-to-slot assignments relative to the SCR coherence budget |
| **DDA** | Density-Dependent Derating Arc — TTF arc encoding timing margin reduction as design temporal density approaches RWDL |
| **DGR** | Density Gradient Rules — TDR category constraining the spatial rate of change of temporal density |
| **Δτ_eff** | Effective minimum address spacing enforced by TDRC; equals Δτ_min + Δτ_margin |
| **Δτ_margin** | Required margin above Δτ_min; absorbs TAOE_rnd and spatial SC variation |
| **Δτ_min** | Minimum qualified address spacing at which the process achieves MQD without exceeding AER threshold |
| **Δτ_xtalk** | Temporal crosstalk-induced address shift at a victim address caused by an aggressor cluster |
| **F_in_max** | Maximum permitted fan-in (predecessor count) for a single operation in the dependency graph |
| **F_out_max** | Maximum permitted fan-out (successor count) for a single operation in the dependency graph |
| **FSCP** | Full-Spectrum Contrast Pattern — the standard TCT address injection pattern; defined in the TCT Protocol |
| **IC** | Interface Continuity — composite TGI boundary quality parameter; defined in The TGI Metrology Standard |
| **K_xtalk** | Temporal crosstalk coupling constant; material-class-specific; density-tier-dependent multiplier applied per §8.3 |
| **L_c** | Coherence length — the distance over which the substrate's phase-encoding state remains stable |
| **L_handoff** | Inter-zone handoff latency in Zone B coherence cycles; from SCR qualification |
| **MQD** | Maximum Qualified Density — process-specific maximum temporal density at which yield meets the process target floor |
| **N_slot_max** | Maximum operations assignable to a single coherence slot without exceeding TRS sequencing bandwidth |
| **N_slots** | Number of coherence slots per coherence cycle; fixed at SCR qualification |
| **PDK** | Process Design Kit — the structured data package translating fab characterization into EDA-consumable rule sets and parameters |
| **PIMC** | Predictive Intent Map Correction — pre-warping of the TRS intent map using TGI GDA data; defined in The TGI Metrology Standard |
| **Provisional PDK** | A PDK release intended for early design exploration; not valid for tape-out sign-off; carries `P` version suffix |
| **r_int** | Interaction radius — the spatial distance within which address spacing rules apply; derived from L_c |
| **RWDL** | Registration-Weighted Density Limit — the maximum temporal density safely supportable at a given die location given measured TGI quality |
| **SC** | Substrate Clarity — bulk measure of a substrate's capacity to sustain distinct temporal addresses; measured by TCT |
| **SC_bulk** | TCT-measured SC rating for a substrate lot; the lot-level bulk SC value |
| **SC_design** | The operative SC value for rule derivation at a given die subregion; min(SC_bulk, SC_eff) |
| **SC_eff** | Effective interface SC at the TGI boundary; defined in The TGI Metrology Standard |
| **SC_class_local** | The SC class assignment derived from SC_design at a specific die subregion; may differ from lot-level SC class |
| **SCR** | Substrate Coherence Regime — the synchronization architecture for temporal manufacturing; defined in The SCR Specification |
| **SLF** | Synchronization Latency Floor — minimum conformant coherence cycle duration; defined in The SCR Specification |
| **SLL_max** | Maximum permitted side-lobe level of an apodized commit operation |
| **STA** | Static Timing Analysis — the EDA analysis that verifies timing closure; extended with TTF arcs for temporal paths |
| **T_arb** | Commit Arbiter processing latency; component of SLF and APA arc |
| **T_auth** | Setup window before coherence slot boundary within which the CA must assert authorization |
| **T_c** | Coherence cycle period; from SCR qualification |
| **T_seq** | TRS L2 sequencing latency per operation; used in CSA arc |
| **T_slot** | Duration of one coherence slot; T_c / N_slots |
| **T_ZBI** | ZBI message transmission latency; component of ZBA arc |
| **TAOE** | Temporal Address Overlay Error — difference between intended and committed temporal address; defined in The TGI Metrology Standard |
| **TAOE_sys** | Systematic component of TAOE; source of TCA arc values |
| **TCA** | TAOE Correction Arc — TTF arc encoding the spatially patterned systematic address offset from TGI metrology |
| **TCT** | Temporal Contrast Test — the protocol for measuring SC; defined in TCT Protocol |
| **TDR** | Temporal Design Rules — the complete rule set enforced by TDRC; comprises ASR, DGR, TPR, CGR, CSR, and TCRS |
| **TDRC** | Temporal Design Rule Check — the EDA verification tool that checks TDR rules against the design's temporal address map |
| **TGI** | Temporal-Geometric Interface — the boundary domain between Tier 1 spatial and Tier 2 temporal layers |
| **TLMF** | Temporal Layer Markup Format — the file format for SC Class Layer Maps |
| **Tool Certification** | The process by which an EDA tool is verified to correctly consume a specific PDK version |
| **TPSF** | Temporal Parameter Set Format — the file format for TRS Stack Parameter Sets |
| **TPR** | TGI Proximity Rules — TDR category constraining temporal operations near the TGI boundary |
| **TRS** | Temporal Resolution Stack — the four-layer operator system governing temporal manufacturing; defined in The Temporal Manufacturing Primer |
| **TSPS** | TRS Stack Parameter Set — PDK component encoding TRS operational parameters per SC class |
| **TTF** | Temporal Timing Format — the standardized format for temporal timing constraints as EDA timing arcs |
| **TTFAL** | TTF Arc Library — the complete set of TTF arcs for a process node and SCR zone configuration |
| **W_apod** | Apodization window width — the half-width of the L3 resolution layer apodization envelope |
| **ZBA** | Zone Boundary Arc — TTF arc encoding ZBI inter-zone handoff latency L_handoff |
| **ZBI** | Zone Boundary Interface — SCR component managing inter-zone handoff; defined in The SCR Specification |

---

## 16. Related Documents

| Document | Path | Relationship |
|---|---|---|
| The Temporal Manufacturing Primer | `docs/post-ASML_era/The_Temporal_Manufacturing_Primer.md` | Foundational concepts: SC classes, TRS stack, temporal density, MQD, TCU; defines the system this PDK serves |
| The SCR Specification | `docs/post-ASML_era/The_SCR_Specification.md` | Source of CBT timing parameters: T_c, N_slots, SLF, T_arb, D_max, L_handoff; governs ZBA and APA arc values |
| The TGI Metrology Standard | `docs/post-ASML_era/The_TGI_Metrology_Standard.md` | Source of RWDL maps, SC_eff maps, TAOE_sys maps, CLG non-monotonicity flags; drives TCA and DDA arcs and TPR rules |
| TCT Protocol | `docs/post-ASML_era/TCT_Protocol.md` | Source of SC class assignment and spatial SC map; root of the SC measurement chain that feeds SCLM |
| TRS Stack Qualification Procedure | `docs/fab/TRS_Qualification.md` | Source of TSPS parameter values: Δτ_min, W_apod, N_apod, SLL_max, T_seq, N_slot_max |
| SCR Zone Configuration Guide | `docs/fab/SCR_Zone_Config.md` | Zone sizing and layout decisions that determine the zone topology encoded in the CBT |
| Substrate Clarity Classification Standard | `docs/materials/SC_Classification.md` | Defines SC class threshold values used in SCLM and TDR threshold derivation |
| TTF Reference | `docs/eda/TTF_Reference.md` | Normative specification of the Temporal Timing Format syntax and arc type semantics consumed by §7 |
| TLMF Schema | `docs/data-formats/TLMF_Schema.md` | Schema for SC Class Layer Map files |
| TCT Data Exchange Format Schema | `docs/data-formats/TCT_DEF_Schema.md` | Machine-parseable TCT Report format; Phase 1 data ingestion source |
| TDRC Violation Log Schema | `docs/data-formats/TDRC_Violation_Log_Schema.md` | Required machine-readable output format for TDRC tools per R-TOOL-04 |

---

*This document is part of the TriadicFrameworks canonical reference set. Proposed
revisions should be submitted via pull request to the `docs/post-ASML_era/` directory
with a linked issue describing the change rationale. Revisions to §13.2 (qualification
test cases), §13.3 (sign-off authority chain), or §14.2 (version increment triggers)
require review by at least three maintainers. Revisions to EDA tool certification
requirements in §12 additionally require a tool vendor impact assessment.*
