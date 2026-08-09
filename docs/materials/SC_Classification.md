# Substrate Clarity Classification Standard

**Document ID:** materials-001
**Canonical Path:** `docs/materials/SC_Classification.md`
**Revision:** 1.0.0
**Status:** CANONICAL
**Type:** Standard
**Normative:** Yes
**Updated:** 2026-08-08
**Maintainer:** TriadicFrameworks

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Normative Language](#2-normative-language)
3. [SC Metric Definition and Traceability Chain](#3-sc-metric-definition-and-traceability-chain)
4. [SC Class Boundaries](#4-sc-class-boundaries)
5. [Primary Classification Procedure](#5-primary-classification-procedure)
6. [Borderline Case Handling](#6-borderline-case-handling)
7. [Spatial Classification and Within-Substrate Variation](#7-spatial-classification-and-within-substrate-variation)
8. [Substrate Labeling Conventions](#8-substrate-labeling-conventions)
9. [Class Assignment Authority and Records](#9-class-assignment-authority-and-records)
10. [Re-Classification Conditions and Procedure](#10-re-classification-conditions-and-procedure)
11. [Downgrade and Rejection Disposition](#11-downgrade-and-rejection-disposition)
12. [Cross-Document SC Class Version Lock](#12-cross-document-sc-class-version-lock)
13. [Conformance Requirements](#13-conformance-requirements)
14. [Glossary](#14-glossary)
15. [Related Documents](#15-related-documents)

---

## 1. Purpose and Scope

### 1.1 Purpose

This standard is the normative authority for Substrate Clarity (SC) class assignment in the TriadicFrameworks post-ASML era manufacturing canon. It establishes the classification boundaries, measurement traceability chain, assignment procedure, labeling conventions, spatial qualification rules, and re-classification conditions governing all substrates processed under the post-ASML era process canon.

The SC class assigned under this standard propagates to every downstream manufacturing and design decision: which SCR zone topology the substrate is eligible for, which TRS Stack qualification tier applies, which PDK design rule set governs logic implementation, and which fold architecture types are permitted. No substrate may enter production processing without a valid SC class assignment issued under this standard.

### 1.2 Scope

This standard applies to:

- All substrates presented for classification under the TriadicFrameworks post-ASML era canon, regardless of material system, process node, or originating fab.
- All entities with authority to assign, audit, or challenge SC class designations.
- All toolchains, data systems, and EDA environments that consume SC class designations as input.

This standard does **not** define the physical measurement protocols that generate the SC value presented for classification. Those protocols are normatively defined in:

- `docs/post-ASML_era/TCT_Protocol.md` — primary SC value source
- `docs/post-ASML_era/The_TGI_Metrology_Standard.md` — SC_eff derivation from TGI parameters

This standard governs the classification decision made from a validly produced SC value; it does not re-specify measurement procedure.

### 1.3 Relationship to Upstream and Downstream Standards

```
TCT_Protocol.md          The_TGI_Metrology_Standard.md
       │                            │
       │ SC Rating (AER-based)      │ SC_eff (derived from STR, IC, TAOE)
       └──────────────┬─────────────┘
                      │
                      ▼
          ┌─────────────────────────┐
          │  SC_Classification.md   │  ← THIS DOCUMENT
          │  (normative authority)  │
          └─────────────────────────┘
                      │
           SC Class (SC-I / SC-II / SC-III)
                      │
          ┌───────────┼──────────────────┐
          ▼           ▼                  ▼
  SCR zone       PDK design        Fold architecture
  eligibility    rule tier         type selection
  (pae-002)      (pae-005)         (pae-006)
```

The SC value entering this standard MUST have been produced by a conformant measurement session under `docs/post-ASML_era/TCT_Protocol.md` or `docs/post-ASML_era/The_TGI_Metrology_Standard.md`. Classification from informal, uncalibrated, or non-conformant measurements is prohibited.

---

## 2. Normative Language

### 2.1 Keyword Definitions

The following keywords carry normative weight in this document. They are used in accordance with the convention established across the post-ASML era documentation series.

| Keyword | Meaning |
|---|---|
| **MUST** | Absolute requirement. Non-compliance constitutes a conformance failure. |
| **MUST NOT** | Absolute prohibition. Violation constitutes a conformance failure. |
| **SHOULD** | Recommended practice. Deviation requires documented justification. |
| **SHOULD NOT** | Discouraged practice. Adoption requires documented justification. |
| **MAY** | Permitted but not required. No justification needed if omitted. |

Requirement identifiers use the format **R-SCC-NN**, where `SCC` denotes the Substrate Clarity Classification standard and `NN` is a two-digit sequential number. Requirements are normative obligations on any entity claiming conformance to this standard.

---

## 3. SC Metric Definition and Traceability Chain

### 3.1 The SC Scalar

Substrate Clarity (SC) is a dimensionless scalar in the range [0, 1] quantifying the temporal coherence fidelity of a substrate's phase-state ensemble. An SC value of 1.0 denotes a theoretically perfect phase-coherent substrate; a value of 0.0 denotes a fully incoherent substrate in which no temporal address commitment is reproducible.

The SC scalar is derived from the error function of the normalized phase deviation across the substrate address space:

```
SC = erf( π / (256 · σ_phase · √2) )
```

Where:

- `σ_phase` — Standard deviation of committed temporal address phase across the FSCP address set (rad)
- `erf(·)` — Gauss error function
- The factor `π/256` normalizes to the reference interval Δτ_ref = 1/256, which defines the canonical SC rating point in the TCT Protocol

This formula is the canonical SC derivation as established in `docs/post-ASML_era/The_Multi-Regime_Semiconductor_Model.md`. Classifiers operating on SC values from alternative derivations MUST document the derivation basis and its equivalence to this canonical form.

### 3.2 SC Value Sources

Two primary SC value sources are recognized under this standard:

**R-SCC-01** SC values presented for class assignment MUST originate from one of the following two conformant measurement pathways:

| Source | Parameter | Reference |
|---|---|---|
| TCT Protocol | SC Rating at Δτ_ref = 1/256 | `docs/post-ASML_era/TCT_Protocol.md`, §7.3 |
| TGI Metrology Standard | SC_eff (derived from STR, IC, TAOE) | `docs/post-ASML_era/The_TGI_Metrology_Standard.md`, §6.1 |

Both pathways produce a value on the [0, 1] scale compatible with the thresholds defined in §4. When both measurements are available for the same substrate, the TCT-derived SC Rating is treated as primary for class assignment; SC_eff is used as a secondary confirmation unless §6.2 (borderline conflict resolution) applies.

**R-SCC-02** The measurement session that produced the SC value MUST have been conducted under calibration traceable to the Reference Lock Standard Set (RLSS) as defined in `docs/post-ASML_era/TCT_Protocol.md`, §11.1, or the equivalent Spatial Reference Array (SRA) calibration defined in `docs/post-ASML_era/The_TGI_Metrology_Standard.md`, §9.1. SC values lacking documented calibration provenance MUST NOT be used for class assignment.

### 3.3 Measurement Uncertainty and Classification

**R-SCC-03** The combined expanded measurement uncertainty U(SC) at coverage factor k = 2 (approximately 95% confidence) MUST be reported alongside every SC value presented for classification. U(SC) is computed according to the GUM uncertainty framework as specified in `docs/post-ASML_era/The_TGI_Metrology_Standard.md`, §8, and `docs/post-ASML_era/TCT_Protocol.md`, §12.

**R-SCC-04** When applying measurement uncertainty to the classification decision, the classifier MUST treat the SC value as an interval [SC − U(SC), SC + U(SC)] for the purposes of boundary proximity detection as defined in §6. The point value SC is used for the class assignment itself; the interval determines whether borderline handling applies.

Typical U(SC) values by instrument class and process condition:

| Instrument Class | Typical U(SC) at k=2 | Notes |
|---|---|---|
| TRM-1 (Temporal Resolution Module, entry) | ±0.025 | Acceptable only for SC-III screening; not for SC-I/II boundary determination |
| TRM-2 (standard production) | ±0.012 | Sufficient for SC-II/SC-III boundary; marginal for SC-I boundary |
| ISP-1 (Interference Scanning Probe, standard) | ±0.008 | Recommended minimum for SC-I boundary determination |
| ISP-2 (high-resolution) | ±0.004 | Required for borderline cases within ±0.02 of any boundary |

---

## 4. SC Class Boundaries

### 4.1 Canonical Threshold Table

The following SC class thresholds are canonical and normative across the entire TriadicFrameworks post-ASML era documentation series. These values MUST NOT be modified in any document within the series without a synchronized revision to all seven canonical post-ASML era documents and this standard (see §12).

| SC Class | SC Value Range | Regime Association | Manufacturing Status |
|---|---|---|---|
| **SC-I** | SC > 0.92 | Coherent Phase Regime (CPR) | Full temporal manufacturing eligible |
| **SC-II** | 0.75 ≤ SC ≤ 0.92 | Transitional Regime (TR) | Temporal manufacturing with constraints |
| **SC-III** | SC < 0.75 | Classical Carrier Regime (CCR) | Temporal logic unreliable; process re-evaluation required |

**R-SCC-05** The SC class thresholds specified in this section MUST be applied exactly as stated. No rounding, interpolation, or site-specific modification of class boundaries is permitted without a formal revision to this standard and all cross-referenced canonical documents listed in §12.

**R-SCC-06** The boundary at SC = 0.92 is exclusive of SC-II and inclusive of SC-I (i.e., SC > 0.92 → SC-I; SC = 0.92 → SC-II). The boundary at SC = 0.75 is inclusive of SC-II and exclusive of SC-III (i.e., SC = 0.75 → SC-II; SC < 0.75 → SC-III).

### 4.2 Regime Physics Basis

The SC class thresholds are grounded in the physical regime model defined in `docs/post-ASML_era/The_Multi-Regime_Semiconductor_Model.md`. Class boundaries correspond to regime transition thresholds in the order parameter ψ(r,t):

- **SC > 0.92:** Substrate operates predominantly in the Coherent Phase Regime (CPR). Phase stiffness ρ_s is high; coherence length L_c significantly exceeds zone dimensions. All four TRS operator layers (L1–L4) function with high fidelity. Temporal address commitment is reproducible across the substrate's operational lifetime.

- **0.75 ≤ SC ≤ 0.92:** Substrate operates in the Transitional Regime (TR). Phase stiffness is moderate; L_c is of order zone dimensions or smaller. L3 Resolution and L4 Commit operators exhibit degraded but recoverable fidelity. Temporal density must be derated per §4.3.

- **SC < 0.75:** Substrate operates predominantly in the Classical Carrier Regime (CCR). Coherent phase stiffness is insufficient to sustain temporal address commitment. Anomalous Event Rate (AER) exceeds the threshold at which error correction can maintain logical integrity. Temporal logic is unreliable.

### 4.3 Capability Implications by Class

The following capability table summarizes the manufacturing and design constraints imposed by each SC class. Normative requirements for each domain are specified in the referenced documents; this table is informative.

| Capability | SC-I | SC-II | SC-III |
|---|---|---|---|
| TRS operator layers active | L1, L2, L3, L4 | L1, L2, L3, L4 (derated) | L1 only (no commit) |
| SCR zone eligibility | All zone topologies | Linear strip and grid; no hierarchical | Not eligible for SCR commissioning |
| Coherence Clock Generator (CCG) lock | Unconditional | Conditional on SLF stability check | Not achievable |
| PDK design rule tier | Standard (full) | Conservative (+15–30% margins) | Not eligible for TRS-aware PDK flow |
| Fold architecture types permitted | All four types | Single-cycle and multi-cycle only | None |
| Temporal Register (TR) refresh rate | Standard per TSH formula | Increased by ×1.5–×2.5 | Not applicable |
| Inter-zone handoff (ZBI) | Permitted | Permitted with derated L_handoff | Prohibited |
| Logic folding tapeout eligibility | Eligible | Eligible with constraints | Not eligible |

---

## 5. Primary Classification Procedure

### 5.1 Procedure Overview

Classification is a five-step procedure executed by a qualified SC Class Assignment Authority (SCAA) following completion of a conformant measurement session.

```
Step 1: Receive and validate measurement record
        │
        ▼
Step 2: Check calibration provenance
        │
        ▼
Step 3: Extract SC value and U(SC)
        │
        ▼
Step 4: Determine boundary proximity (see §6 if within ±0.02)
        │
        ▼
Step 5: Assign SC class and issue Classification Record
```

### 5.2 Step 1 — Measurement Record Receipt and Validation

**R-SCC-07** Before proceeding with classification, the SCAA MUST validate that the received measurement record:

- Is formatted in conformance with `docs/data-formats/TCT_DEF_Schema.md` (for TCT-sourced records) or an equivalent structured format for TGI-sourced records.
- Contains a complete calibration provenance block (RLSS ID, FTRC ID, session calibration timestamp).
- Reports a lot ID, wafer ID, and session timestamp that can be cross-referenced against the fab's measurement scheduling records.
- Contains a reported U(SC) value at k = 2.

**R-SCC-08** Any measurement record missing one or more required provenance fields MUST be returned to the originating measurement team for correction before classification proceeds. The SCAA MUST NOT assign a class from an incomplete record.

### 5.3 Step 2 — Calibration Provenance Check

**R-SCC-09** The SCAA MUST verify that the RLSS and FTRC IDs reported in the measurement record are registered in the fab's calibration management system and that the calibration expiry date for the referenced standards has not elapsed at the time of the measurement session.

**R-SCC-10** If calibration has lapsed, the measurement MUST be voided. The SCAA MUST flag the lot for re-measurement under a current calibration session. Expired calibration cannot be retroactively extended.

### 5.4 Step 3 — SC Value and Uncertainty Extraction

**R-SCC-11** For TCT-sourced records, the classification SC value is the `tcr_sc_rating.sc_value` field at Δτ_ref = 1/256, as computed per `docs/post-ASML_era/TCT_Protocol.md`, §7.

**R-SCC-12** For TGI-sourced records used as primary (in the absence of a TCT record), the classification SC value is `SC_eff` as derived from the TGI parameter set per `docs/post-ASML_era/The_TGI_Metrology_Standard.md`, §6.1.

**R-SCC-13** When both a TCT record and a TGI record exist for the same substrate and session, the TCT-derived SC value is primary. The TGI-derived SC_eff MUST be retained as a secondary confirmation and recorded in the Classification Record.

### 5.5 Step 4 — Boundary Proximity Determination

**R-SCC-14** Before applying the threshold table in §4.1, the SCAA MUST compute the distance from the SC value to each class boundary:

```
d_upper = |SC − 0.92|    (distance to SC-I/SC-II boundary)
d_lower = |SC − 0.75|    (distance to SC-II/SC-III boundary)
```

If either d_upper ≤ 0.02 or d_lower ≤ 0.02, the measurement is in the borderline zone and MUST be processed under §6 before a class is assigned.

### 5.6 Step 5 — Class Assignment and Classification Record Issuance

**R-SCC-15** If the SC value is not in the borderline zone, the SCAA assigns the SC class directly from the threshold table in §4.1 and issues a Classification Record containing at minimum:

| Field | Content |
|---|---|
| `lot_id` | Fab lot identifier |
| `wafer_id` | Wafer identifier within lot |
| `sc_value` | Numeric SC value used for classification |
| `u_sc` | Expanded uncertainty U(SC) at k=2 |
| `sc_class` | Assigned class: SC-I, SC-II, or SC-III |
| `measurement_source` | TCT \| TGI \| TCT+TGI |
| `session_id` | Measurement session identifier |
| `rlss_id` | RLSS calibration standard ID |
| `assignment_authority_id` | SCAA identifier |
| `assignment_timestamp` | ISO 8601 timestamp of assignment |
| `borderline_flag` | Boolean; true if §6 procedure was invoked |
| `secondary_sc_eff` | TGI-derived SC_eff, if available |
| `notes` | Free text; required when borderline_flag is true |

**R-SCC-16** The Classification Record MUST be signed by the SCAA and archived in the fab's quality management system with a minimum retention period of five (5) years or the lifetime of the process node, whichever is longer.

---

## 6. Borderline Case Handling

### 6.1 Definition of Borderline Zone

A measurement is in the **borderline zone** if the SC point value falls within ±0.02 of either canonical class boundary:

| Boundary | Borderline Zone Range | Boundary Value |
|---|---|---|
| SC-I / SC-II | 0.90 ≤ SC ≤ 0.94 | 0.92 |
| SC-II / SC-III | 0.73 ≤ SC ≤ 0.77 | 0.75 |

The ±0.02 window is sized to encompass the typical expanded uncertainty range of ISP-1 class instruments (U(SC) ≈ ±0.008 at k=2) with a safety factor of approximately 2.5×, ensuring that no measurement whose true value could plausibly be on the opposite side of a boundary is classified without additional scrutiny.

### 6.2 Borderline Procedure — Confirmation Measurement

**R-SCC-17** When a measurement falls in the borderline zone, the SCAA MUST NOT assign a class solely from the original measurement. A confirmation measurement MUST be performed under the following conditions:

- Instrument class: ISP-2 or equivalent (U(SC) ≤ ±0.005 at k=2)
- Independent calibration session: MUST NOT re-use the same FTRC session as the original measurement
- Same physical substrate: the same wafer and test coupon site MUST be used for the confirmation
- Minimum inter-measurement interval: 4 hours (to allow thermal stabilization)

**R-SCC-18** The SCAA MUST average the original SC value and the confirmation SC value, weighted by their respective inverse squared uncertainties:

```
SC_combined = (SC_orig / U_orig² + SC_conf / U_conf²) / (1/U_orig² + 1/U_conf²)

U_combined  = 1 / sqrt(1/U_orig² + 1/U_conf²)
```

The combined SC_combined and U_combined are used for the final class assignment under §4.1.

**R-SCC-19** If SC_combined ± U_combined still straddles a class boundary (i.e., the uncertainty interval contains the boundary value), the SCAA MUST assign the **lower** class (the class with the lesser capability tier) and record a conservative classification note in the Classification Record.

This conservative assignment principle ensures that substrates whose true SC value is ambiguous relative to a boundary do not enter a process flow for which they may be insufficient.

### 6.3 Borderline Zone — Dual-Source Conflict Resolution

When a TCT-derived SC value and a TGI-derived SC_eff are both available and disagree across a class boundary:

**R-SCC-20** If the TCT value and TGI SC_eff differ by more than U_combined (combined uncertainty of both measurements), the SCAA MUST:

1. Initiate a dual-source discrepancy review.
2. Examine the calibration provenance of both measurements independently.
3. Perform a re-measurement with ISP-2 class instruments before assigning a class.
4. Document the discrepancy, its investigation, and its resolution in the Classification Record.

**R-SCC-21** In the absence of discrepancy resolution data, the TCT-derived value is primary and MUST be used for the interim class assignment, marked as provisional (see §9.3).

### 6.4 Fast-Track Borderline Exception

**R-SCC-22** In production environments where lot cycle time constraints make a 4-hour inter-measurement interval impractical, the fab MAY invoke a Fast-Track Borderline Exception (FTBE) under the following conditions:

- The original measurement falls in the borderline zone but the SC point value is more than 1.5 × U(SC) from the boundary (i.e., the boundary is outside the one-sigma uncertainty interval).
- The SCAA documents the FTBE invocation and its basis in the Classification Record.
- The lot is flagged for confirmation measurement at the next available ISP-2 session, within 48 hours of the FTBE assignment.

If the subsequent confirmation measurement produces a class different from the FTBE assignment, the lot MUST be recalled for re-evaluation of any process steps completed under the erroneous class.

---

## 7. Spatial Classification and Within-Substrate Variation

### 7.1 Wafer-Level vs. Die-Level Classification

SC class assignment under this standard applies at two spatial granularities:

- **Lot-level classification:** A single SC class assigned to the entire lot, based on the median SC value across all measured wafers. Used for routing decisions at the lot level (zone assignment, process flow selection).
- **Die-level classification:** Per-die SC class annotation embedded in the TLMF (Temporal Layer Markup Format) SC Class Layer Map. Used by EDA tools during layout verification and PDK rule set selection.

**R-SCC-23** Lot-level classification MUST be completed before any wafer in the lot enters SCR zone commissioning or TRS Stack Qualification. Die-level classification MUST be completed before the corresponding SCLM (SC Class Layer Map) is generated for the lot's PDK build.

### 7.2 Spatial Uniformity Requirements

**R-SCC-24** A substrate with a lot-level classification of SC-I or SC-II MUST also satisfy the following spatial uniformity criteria, as measured by the 5×5 subregion spatial uniformity analysis defined in `docs/post-ASML_era/TCT_Protocol.md`, §8:

| SC Class | Maximum subregion SC deviation from lot median | Maximum fraction of subregions below class lower boundary |
|---|---|---|
| SC-I | ±0.04 | 0 of 25 (no subregion may fall below SC = 0.92) |
| SC-II | ±0.06 | ≤ 4 of 25 (up to 16% of area may fall into SC-III) |
| SC-III | Not specified (uniformity not required for re-evaluation) | — |

**R-SCC-25** If a substrate's lot-level SC value qualifies for SC-I but more than 0 subregions fall below SC = 0.92, the lot-level class MUST be downgraded to SC-II. The affected subregion boundaries MUST be recorded in the TLMF SC_eff field for die-level design rule enforcement.

**R-SCC-26** If a substrate's lot-level SC value qualifies for SC-II but more than 4 subregions fall below SC = 0.75, the lot-level class MUST be downgraded to SC-III. Downgrade is immediate and non-negotiable; FTBE does not apply to spatial downgrade decisions.

### 7.3 RWDL-Based Spatial Boundary Marking

**R-SCC-27** For any substrate with a lot-level classification of SC-I or SC-II, the Regime Width Distribution Locus (RWDL) spatial boundary MUST be computed from the TGI Metrology data per `docs/post-ASML_era/The_TGI_Metrology_Standard.md`, §6.2, and embedded in the substrate's TLMF file as `rwdl_contours` layer data.

RWDL contours identify the physical substrate positions at which the regime transitions between CCR and TR or TR and CPR. These contours govern die-placement exclusion zones in SC-II substrates and constrain ZBA (Zone Boundary Arc) routing paths in PDK design rule enforcement.

---

## 8. Substrate Labeling Conventions

### 8.1 Physical Label Requirements

**R-SCC-28** Every substrate that has received a valid SC class assignment MUST be physically labeled before it leaves the metrology station. Physical labels are the primary mechanism for preventing mis-routing of substrates in the fab environment.

**R-SCC-29** The physical label MUST include, in human-readable and machine-readable (2D barcode) form:

| Label Field | Format | Example |
|---|---|---|
| SC class | `SC-I` / `SC-II` / `SC-III` | `SC-II` |
| SC numeric value | Four decimal places | `0.8741` |
| U(SC) | Four decimal places, preceded by `±` | `±0.0082` |
| Classification date | ISO 8601 date | `2026-08-08` |
| Assignment authority ID | Alphanumeric SCAA code | `SCAA-FAB3-007` |
| Lot ID | Fab-standard lot format | `LOT-2026-08-441` |
| Borderline flag | `BL` suffix if borderline procedure invoked | `SC-II-BL` |
| Provisional flag | `PROV` suffix if classification is provisional | `SC-II-PROV` |

**R-SCC-30** The 2D barcode on the physical label MUST encode the full Classification Record session ID, enabling direct lookup of the complete classification provenance from the fab's quality management system.

### 8.2 Digital Metadata Labeling

**R-SCC-31** In addition to physical labeling, the SC class MUST be recorded in all of the following digital systems before the substrate proceeds to the next process step:

- The fab lot tracking system (lot-level entry)
- The TLMF file for the substrate (die-level SC class layer)
- The TCT-DEF record (in the `tcr_sc_rating.sc_class` field, if TCT measurement was the source)
- The PDK build manifest for the corresponding process run

**R-SCC-32** If any of these digital systems cannot be updated (e.g., due to system unavailability), the substrate MUST be placed on hold until the update is completed. Processing under an incompletely recorded SC class is prohibited.

### 8.3 Lot-Level vs. Wafer-Level Labeling

**R-SCC-33** When an entire lot receives the same SC class, a single lot-level label MUST be applied to the lot carrier. Individual wafer labels MUST additionally be applied to each wafer cassette within the lot, repeating all fields from §8.1.

**R-SCC-34** If individual wafers within a lot receive different SC classes (see §7.2 downgrade conditions), each wafer MUST be individually labeled with its own SC class. The lot carrier label MUST reflect the lowest (most conservative) class present among the lot's wafers.

---

## 9. Class Assignment Authority and Records

### 9.1 Qualified SC Class Assignment Authority

**R-SCC-35** SC class assignments MUST be performed by a designated SC Class Assignment Authority (SCAA). An SCAA is a qualified individual or automated system that has demonstrated competency in:

- Executing the classification procedure of §5.
- Applying borderline handling per §6.
- Interpreting spatial uniformity data per §7.
- Operating under the calibration traceability requirements of §3.2.

**R-SCC-36** Individual SCAAs MUST be qualified by demonstrated performance on a minimum of 50 classification decisions reviewed by a senior authority, with a discrepancy rate below 2% against reference classifications. Automated SCAA systems MUST pass a certification suite of no fewer than 200 reference cases with a discrepancy rate below 0.5%.

**R-SCC-37** Qualification records for SCAAs MUST be maintained in the fab's personnel or system qualification registry and reviewed annually. Lapsed qualification disqualifies the individual or system from performing classifications until re-qualification is complete.

### 9.2 Classification Record Requirements

All requirements for Classification Record content are specified in §5.6 (Table: Classification Record Fields). Additional requirements:

**R-SCC-38** Classification Records MUST be immutable once issued. Corrections to an issued Classification Record MUST be made by issuing a superseding Classification Record, which references the original by session ID and states the correction and its basis. The original record is archived, not deleted.

**R-SCC-39** Classification Records MUST be accessible to downstream process steps (SCR zone commissioning, TRS Stack Qualification, PDK generation) within four (4) hours of issuance.

### 9.3 Provisional Classification

A classification is designated **provisional** when:

- It is the result of an FTBE assignment per §6.4 pending confirmation measurement.
- It is the result of a dual-source conflict assignment per §6.3 pending discrepancy resolution.
- It is issued under emergency conditions (e.g., measurement system degradation) with documented justification.

**R-SCC-40** Provisional classifications MUST be marked with the `PROV` flag on all physical and digital labels per §8.1 and §8.2. Process steps MAY proceed under a provisional classification subject to fab risk acceptance procedures, but tapeout sign-off MUST NOT proceed until the provisional flag is resolved.

**R-SCC-41** A provisional classification MUST be resolved within 72 hours of issuance. If not resolved within 72 hours, the substrate MUST be placed on hold.

---

## 10. Re-Classification Conditions and Procedure

### 10.1 Conditions Requiring Re-Classification

**R-SCC-42** A substrate MUST undergo re-classification if any of the following conditions are met:

| Condition | Trigger | Action Required |
|---|---|---|
| Time elapsed | More than 90 days since last classification | Re-measure and re-classify before entering any new process step |
| Thermal excursion | Substrate exposed to temperatures > 450 °C for > 10 minutes | Re-classify within 24 hours of excursion |
| Mechanical stress event | Substrate subjected to unplanned mechanical stress (drop, impact, excessive clamping force) | Re-classify before proceeding |
| Process-induced SC degradation | Process step known to affect SC (e.g., aggressive etch, high-dose implant) | Re-classify after the process step |
| Class challenge | SCAA challenge issued by downstream process owner | Re-classify within 48 hours |
| Spatial downgrade trigger | In-process monitoring detects spatial non-uniformity exceeding §7.2 limits | Re-classify immediately; hold processing |
| CMA alert | Coherence Monitor Array reports SC degradation below class lower boundary during SCR operation | Suspend SCR operation; re-classify before resuming |

**R-SCC-43** Re-classification follows the full procedure of §5. It is not abbreviated even when re-classification is triggered by a routine time expiry.

### 10.2 Re-Classification Authority

**R-SCC-44** Re-classification MUST be performed by an SCAA qualified under §9.1. The re-classifying SCAA MUST NOT be the same individual who issued the original classification for the same substrate (to prevent confirmation bias), unless no other qualified SCAA is available. If the same SCAA must perform re-classification, the fact MUST be noted in the Classification Record.

### 10.3 Impact of Re-Classification on In-Process Substrates

**R-SCC-45** If re-classification results in a lower SC class than the current assignment, all process steps completed under the previous class MUST be reviewed for compliance with the new class's requirements. The process owner MUST determine whether any completed steps are invalidated and what corrective action is required.

**R-SCC-46** If re-classification results in a higher SC class than the current assignment (upgrade), the upgrade is valid and the substrate may proceed under the higher class. Upgrades do not require retroactive review of completed process steps.

---

## 11. Downgrade and Rejection Disposition

### 11.1 SC-II to SC-III Downgrade Disposition

When a substrate is downgraded to SC-III, either by initial classification or re-classification:

**R-SCC-47** The substrate MUST be immediately withdrawn from any active SCR zone processing. Any silicon produced from an SC-III substrate under SC-II process conditions MUST be rejected and cannot be used for any temporal logic application.

**R-SCC-48** SC-III substrates MAY be redirected to legacy (non-temporal) process flows if such flows exist in the fab and the substrate's material properties are otherwise acceptable. The SC class label MUST remain on the substrate and MUST be recorded in any non-temporal lot tracking records.

### 11.2 Rejection — Below Minimum Threshold

**R-SCC-49** There is no minimum SC threshold below which a substrate is automatically rejected for all purposes. Rejection for temporal manufacturing purposes occurs at the SC-III boundary (SC < 0.75). However, substrate rejection for material quality reasons (e.g., catastrophic crystallographic defects, contamination) is governed by material inspection standards outside the scope of this document.

### 11.3 Escalation Path

**R-SCC-50** If an SCAA determines that a substrate's SC measurement history is inconsistent (e.g., oscillating between SC-I and SC-II across multiple re-classifications without process events to explain the variation), the SCAA MUST escalate to the fab's metrology engineering team. The substrate MUST be held until the source of variation is identified and documented.

---

## 12. Cross-Document SC Class Version Lock

### 12.1 Purpose of Version Lock

The SC class thresholds defined in §4.1 (SC-I > 0.92, SC-II 0.75–0.92, SC-III < 0.75) are embedded by reference in all seven canonical post-ASML era documents. Any modification to these thresholds requires a synchronized update across the entire documentation set. This section records the current version lock state and mandates the change control procedure.

### 12.2 Current Version Lock Table

The following table records all canonical documents that embed the SC class thresholds. All entries are locked at the versions shown. A change to SC class thresholds requires simultaneous revision of all documents in this table.

| Document | Document ID | Revision | SC Threshold Embedding Location |
|---|---|---|---|
| `docs/materials/SC_Classification.md` (this document) | materials-001 | 1.0.0 | §4.1 — Canonical Threshold Table |
| `docs/post-ASML_era/The_Temporal_Manufacturing_Primer.md` | pae-001 | 1.0.0 | §3: SC class definitions; §6: equipment tier eligibility table |
| `docs/post-ASML_era/The_SCR_Specification.md` | pae-002 | 1.0.0 | §4: Zone eligibility; §8: CMA alert thresholds; §9: Commissioning criteria |
| `docs/post-ASML_era/The_TGI_Metrology_Standard.md` | pae-003 | 1.0.0 | Table 4: Acceptance criteria by SC class; §6.1: SC_eff class mapping |
| `docs/post-ASML_era/TCT_Protocol.md` | pae-004 | 1.0.0 | §7.3: SC Rating class assignment; §8: Spatial uniformity by SC class |
| `docs/post-ASML_era/The_TRS-Aware_PDK_Specification.md` | pae-005 | 1.0.0 | §3: SCLM class keys; §5: Design rule stringency by class; §8: Qualification criteria |
| `docs/post-ASML_era/The_Logic_Folding_Architecture_Guide.md` | pae-006 | 1.0.0 | §4: Fold type eligibility by SC class; §7: Temporal Register refresh rate by class |
| `docs/post-ASML_era/The_Multi-Regime_Semiconductor_Model.md` | pae-007 | 0.9.0 draft | §3: SC class as regime indicator; §5: Observable parameter thresholds |

**R-SCC-51** Any revision to SC class thresholds MUST be accompanied by simultaneous revision of all eight documents listed in this table. A revision to SC thresholds in one document that is not reflected in all others within the same release constitutes a canon conflict and renders the conflicting documents non-conformant until reconciled.

**R-SCC-52** The revision history section of each updated document MUST explicitly note the SC threshold change, the prior value, the new value, and the release identifier under which the synchronized update was made.

### 12.3 Threshold Change Control Process

Proposals to modify SC class thresholds MUST follow the change control process defined below:

1. **Technical justification:** The proposal MUST include a quantitative basis for the new thresholds, derived from updated physical modeling or metrology evidence that the current boundaries misclassify a statistically significant fraction of substrates.
2. **Impact assessment:** All eight documents in the version lock table MUST be assessed for the impact of the proposed change.
3. **Review authority:** The proposal MUST be reviewed and approved by the TriadicFrameworks documentation maintainer and at minimum two independent domain reviewers (one from metrology, one from design).
4. **Simultaneous publication:** All revised documents MUST be published in the same release. Staggered publication of threshold changes is prohibited.
5. **Transition period:** A transition period MUST be specified during which both old and new thresholds are valid, to allow in-flight substrates to be re-classified under the new standard.

---

## 13. Conformance Requirements

### 13.1 Conformance Claims

An entity (fab, metrology service, EDA tool, automated classification system) claims conformance to this standard if it asserts compliance with all MUST and MUST NOT requirements in this document.

**R-SCC-53** Conformance claims MUST be documented in writing and MUST specify the entity's scope of conformance (e.g., "classification procedure only" vs. "full standard including re-classification and labeling").

**R-SCC-54** Partial conformance is permitted and MUST be explicitly scoped. An entity claiming partial conformance MUST identify the sections not covered and the alternative procedures applied.

### 13.2 Minimum Conformance Requirements

For a fab to claim full conformance to this standard:

| Requirement Area | MUST Satisfy |
|---|---|
| SC value sourcing | R-SCC-01 through R-SCC-04 |
| Class boundaries | R-SCC-05, R-SCC-06 |
| Primary classification procedure | R-SCC-07 through R-SCC-16 |
| Borderline handling | R-SCC-17 through R-SCC-22 |
| Spatial classification | R-SCC-23 through R-SCC-27 |
| Labeling | R-SCC-28 through R-SCC-34 |
| Assignment authority | R-SCC-35 through R-SCC-41 |
| Re-classification | R-SCC-42 through R-SCC-46 |
| Disposition | R-SCC-47 through R-SCC-50 |
| Version lock | R-SCC-51, R-SCC-52 |
| Conformance claims | R-SCC-53, R-SCC-54 |

### 13.3 Non-Conformance and Dispute Resolution

Disputes regarding SC class assignments that cannot be resolved between the originating SCAA and the challenging party MUST be escalated to the TriadicFrameworks documentation maintainer for arbitration. Arbitration decisions are binding and constitute an amendment to the applicable Classification Record.

---

## 14. Glossary

| Term | Definition |
|---|---|
| **AER (Anomalous Event Rate)** | The rate of temporal address commitment failures per unit time, normalized to the FSCP address set. The primary observable used to derive SC Rating in TCT Protocol. |
| **Assignment Authority ID** | A unique identifier for the qualified individual or automated system that issued a Classification Record. |
| **Borderline Zone** | The SC value range within ±0.02 of either class boundary (0.92 or 0.75) in which confirmation measurement is required before class assignment. |
| **CCG (Coherence Clock Generator)** | The master timing source for the Substrate Coherence Regime; provides phase-locked coherence clock signals distributed via the CDN. |
| **CCR (Classical Carrier Regime)** | The physical phase regime in which substrate behavior is dominated by classical carrier transport rather than coherent phase dynamics. Associated with SC < 0.75. |
| **CDN (Coherence Distribution Network)** | The physical clock distribution network that carries CCG signals to all SCR zones. |
| **CMA (Coherence Monitor Array)** | An array of in-situ sensors that monitors SC-related parameters during SCR operation, providing real-time early warning of coherence degradation. |
| **Conservative Classification** | The assignment of the lower SC class when measurement uncertainty straddles a class boundary, per R-SCC-19. |
| **CPR (Coherent Phase Regime)** | The physical phase regime in which coherent phase dynamics dominate substrate behavior. Associated with SC > 0.92. |
| **FTBE (Fast-Track Borderline Exception)** | A conditional procedure allowing class assignment in the borderline zone without the full 4-hour inter-measurement interval, subject to follow-up confirmation. |
| **FTRC (Frequency and Temporal Reference Cell)** | A secondary calibration standard used for session-level instrument verification, traceable to the RLSS. |
| **GUM (Guide to the Expression of Uncertainty in Measurement)** | The international standard framework for expressing and combining measurement uncertainties. |
| **ISP (Interference Scanning Probe)** | High-resolution TGI metrology instrument class. ISP-2 is required for borderline case confirmation measurement. |
| **L1 Intent** | The first layer of the TRS operator stack; responsible for temporal intent injection. |
| **L2 Sequencing** | The second TRS layer; governs temporal ordering and sequencing integrity. |
| **L3 Resolution** | The third TRS layer; governs resolution of temporal addresses to physical commit positions. |
| **L4 Commit** | The fourth TRS layer; governs final commit arbitration and SLF synchronization. |
| **Lot-Level Classification** | An SC class assigned to an entire lot, based on the statistical summary (typically median) of individual wafer SC values. |
| **PROV (Provisional Flag)** | A label and digital metadata flag indicating that a classification is provisional and subject to resolution within 72 hours. |
| **RLSS (Reference Lock Standard Set)** | The primary calibration standard for TRS metrology instruments; the root of the calibration traceability chain. |
| **RWDL (Regime Width Distribution Locus)** | A spatial boundary map identifying the physical positions of regime transitions across the substrate, derived from TGI metrology data. |
| **SC (Substrate Clarity)** | Dimensionless scalar [0, 1] quantifying the temporal phase coherence fidelity of a substrate. The primary classification input. |
| **SC Class** | A categorical designation (SC-I, SC-II, or SC-III) assigned to a substrate based on its SC scalar value relative to the canonical thresholds. |
| **SC_eff (Effective Substrate Clarity)** | A derived TGI Metrology parameter that aggregates STR, IC, and TAOE into a single SC-equivalent scalar; used as secondary classification input. |
| **SCAA (SC Class Assignment Authority)** | A qualified individual or certified automated system with authority to assign SC classes, issue Classification Records, and perform re-classifications. |
| **SCLM (SC Class Layer Map)** | A PDK component that encodes spatially resolved SC class designations for use by EDA design rule engines. |
| **SCR (Substrate Coherence Regime)** | The ensemble of hardware (CCG, CDN, Commit Arbiter, CMA, ZBI) that maintains phase coherence across a substrate during temporal manufacturing operations. |
| **SLF (Synchronization Lock Frame)** | The timing reference frame within which commit arbitration operates, derived from CCG phase and CDN propagation timing. |
| **STR (Spatial Temporal Resolution)** | TGI primary parameter measuring the finest resolvable temporal address spacing on the substrate surface. |
| **TAOE (Temporal Address Occupation Efficiency)** | TGI primary parameter measuring the fraction of temporal address space usably committed per unit substrate area. |
| **TCT (Temporal Contrast Test)** | The normative measurement protocol for deriving SC Rating from AER measurements, defined in `docs/post-ASML_era/TCT_Protocol.md`. |
| **TCT-DEF (TCT Data Exchange Format)** | The machine-readable schema for TCT Report data, defined in `docs/data-formats/TCT_DEF_Schema.md`. |
| **TGI (Temporal-Geometric Interface)** | The physical boundary region at which the substrate transitions between classical and temporal behavior; the primary site of TRS metrology. |
| **TLMF (Temporal Layer Markup Format)** | The file format encoding spatially resolved SC class annotations, regime boundaries, RWDL contours, and SC_eff fields for a substrate. |
| **TR (Transitional Regime)** | The physical phase regime intermediate between CCR and CPR, characterized by moderate phase stiffness. Associated with SC values in [0.75, 0.92]. |
| **TRM (Temporal Resolution Module)** | Entry-level TGI metrology instrument class. TRM-2 is the minimum for production SC_eff measurements. |
| **TRS (Temporal Resolution Stack)** | The four-layer operator stack (L1–L4) that converts temporal intent into committed substrate address states. |
| **U(SC) (Expanded Uncertainty of SC)** | The combined expanded measurement uncertainty of an SC value at coverage factor k=2, representing approximately a 95% confidence interval. |
| **ZBA (Zone Boundary Arc)** | A TTF arc type encoding timing for signals that cross an SCR zone boundary; its routing is constrained by RWDL contours. |
| **ZBI (Zone Boundary Interface)** | The hardware and protocol layer managing inter-zone handoff timing and phase alignment at SCR zone boundaries. |

---

## 15. Related Documents

| Document | Relative Path | Relationship |
|---|---|---|
| TCT Protocol | `docs/post-ASML_era/TCT_Protocol.md` | Primary upstream: produces SC Rating (classification input via §3.2) |
| The TGI Metrology Standard | `docs/post-ASML_era/The_TGI_Metrology_Standard.md` | Secondary upstream: produces SC_eff (alternative classification input) |
| The Multi-Regime Semiconductor Model | `docs/post-ASML_era/The_Multi-Regime_Semiconductor_Model.md` | Physical basis: SC class boundaries correspond to regime transition thresholds |
| The Temporal Manufacturing Primer | `docs/post-ASML_era/The_Temporal_Manufacturing_Primer.md` | Introductory context: defines SC conceptually; references this standard for normative thresholds |
| The SCR Specification | `docs/post-ASML_era/The_SCR_Specification.md` | Downstream consumer: SC class governs SCR zone eligibility and CMA thresholds |
| The TRS-Aware PDK Specification | `docs/post-ASML_era/The_TRS-Aware_PDK_Specification.md` | Downstream consumer: SCLM keys and design rule tier selection driven by SC class |
| The Logic Folding Architecture Guide | `docs/post-ASML_era/The_Logic_Folding_Architecture_Guide.md` | Downstream consumer: fold type eligibility and TR refresh rate are SC class–dependent |
| TRS Stack Qualification Procedure | `docs/fab/TRS_Qualification.md` | Peer normative: qualification gate that consumes SC class assignment |
| SCR Zone Configuration Guide | `docs/fab/SCR_Zone_Config.md` | Downstream configuration: zone topology selection is constrained by SC class |
| TCT Data Exchange Format Schema | `docs/data-formats/TCT_DEF_Schema.md` | Data format: `tcr_sc_rating.sc_class` field carries the classification output |
| Temporal Layer Markup Format Schema | `docs/data-formats/TLMF_Schema.md` | Data format: `sc_class_map` layer encodes classification output for EDA |
| post-ASML_era Module Index | `docs/post-ASML_era/README.md` | Navigation: module-level reading guide and dependency graph |

---

*This document is part of the TriadicFrameworks canonical reference series. Proposed revisions must be submitted as pull requests against the `docs/` tree. All normative changes require review by the TriadicFrameworks documentation maintainer. Changes to §4.1 (SC class thresholds) require simultaneous revision of all documents listed in §12.2.*

*Document ID: materials-001 · Revision 1.0.0 · 2026-08-08*
