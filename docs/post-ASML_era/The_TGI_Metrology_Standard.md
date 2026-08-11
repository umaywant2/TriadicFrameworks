# The TGI Metrology Standard

**Repository:** TriadicFrameworks
**Path:** `docs/post-ASML_era/The_TGI_Metrology_Standard.md`
**Status:** Canonical Reference
**Revision:** 1.0.0

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [The Temporal-Geometric Interface Defined](#2-the-temporal-geometric-interface-defined)
3. [Measurement Parameter Taxonomy](#3-measurement-parameter-taxonomy)
4. [Instrumentation Requirements](#4-instrumentation-requirements)
5. [Spatial-Temporal Registration](#5-spatial-temporal-registration)
6. [Interface Continuity](#6-interface-continuity)
7. [Temporal Address Overlay Error](#7-temporal-address-overlay-error)
8. [TGI Uniformity Index](#8-tgi-uniformity-index)
9. [Coherence Layer Gradient](#9-coherence-layer-gradient)
10. [Geometric Drift Correlation](#10-geometric-drift-correlation)
11. [Sampling Strategy](#11-sampling-strategy)
12. [Data Analysis and Reporting](#12-data-analysis-and-reporting)
13. [Acceptance Criteria](#13-acceptance-criteria)
14. [Calibration Requirements](#14-calibration-requirements)
15. [Measurement Uncertainty](#15-measurement-uncertainty)
16. [Integration with Process Qualification](#16-integration-with-process-qualification)
17. [Glossary](#17-glossary)
18. [Related Documents](#18-related-documents)

---

## 1. Purpose and Scope

### 1.1 Purpose

This document is the normative metrology standard for the **Temporal-Geometric Interface (TGI)** in TriadicFrameworks post-ASML manufacturing. It defines the parameters that characterize the TGI, the instruments required to measure them, the protocols by which measurements are taken, the analysis methods by which raw data are reduced to reportable values, and the acceptance criteria against which those values are evaluated.

The TGI is the boundary domain in which the spatial coordinate system of Tier 1 geometric patterning and the temporal address space of Tier 2 TRS commit operations must be brought into and maintained in precise co-registration. Failures at this interface are a distinct defect class — not reducible to classical spatial patterning defects or to pure temporal address errors — and require their own metrology discipline.

This standard provides the metrology framework that is prerequisite to:

- Process qualification for any fab layer that spans the TGI
- TRS stack qualification at SC-class boundaries
- Yield management correlation for TGI-attributed defect modes
- PDK generation for TGI-layer design rules

### 1.2 Scope

This standard covers:

- The formal definition of the TGI and its physical extent within the process stack
- Six primary TGI measurement parameters and their physical basis
- Instrumentation requirements and qualification criteria for TGI measurement tools
- Measurement protocols for each parameter, including site selection, sequence, and environmental conditions
- Wafer-level and die-level sampling strategies
- Data analysis methods, uncertainty treatment, and reporting format
- Acceptance criteria by SC class and process tier
- Calibration requirements for all measurement instruments defined herein
- A framework for measurement uncertainty estimation consistent with the GUM approach
- The interfaces between TGI metrology and TRS stack qualification, SCR commissioning, and yield management

This standard does not cover:

- Substrate clarity measurement, which is governed by the Temporal Contrast Test Protocol ([`docs/metrology/TCT_Protocol.md`](../metrology/TCT_Protocol.md))
- In-fab real-time coherence monitoring, which is governed by the SCR Specification ([`docs/post-ASML_era/The_SCR_Specification.md`](./The_SCR_Specification.md))
- Classical spatial overlay metrology for Tier 1 layers without a TGI relationship

### 1.3 Normative Language

The conventions established in the SCR Specification apply throughout this document:

| Term | Meaning |
|---|---|
| **MUST** | Required. Non-conformant if omitted or violated. |
| **MUST NOT** | Prohibited. Non-conformant if present. |
| **SHOULD** | Strongly recommended. Deviation requires documented justification. |
| **SHOULD NOT** | Strongly discouraged. Deviation requires documented justification. |
| **MAY** | Permitted but not required. |

---

## 2. The Temporal-Geometric Interface Defined

### 2.1 Conceptual Definition

The Temporal-Geometric Interface is the domain in which two independently defined coordinate systems — the spatial coordinate system of the geometric layer stack and the temporal address space of the TRS — must be co-registered to enable correct commit operations.

These two systems are fundamentally different in kind. The spatial coordinate system is defined by physical positions on the substrate: x and y in the die plane, z through the layer stack. The temporal address space is defined by positions within the SCR coherence cycle: a temporal address τ in the address domain [0, 1), subdivided to the resolution supported by the substrate's SC class. Neither system intrinsically references the other. The TGI is the artifact of their coupling: the set of rules, physical structures, and verified relationships that allow a given spatial location on the substrate to be uniquely associated with a temporal address, and vice versa.

A correctly formed TGI allows the TRS Commit Layer (L4) to deposit a commit operation at a precisely intended spatial location with a precisely intended temporal address, without ambiguity and without cross-contamination between adjacent operations. A degraded or misregistered TGI introduces systematic or stochastic error into this mapping, producing a defect class that manifests simultaneously as a spatial displacement and a temporal address error.

### 2.2 Physical Location

The TGI is not a single layer. It is a transition zone that spans from the uppermost Tier 1 structural layer to the lowermost Tier 2 temporally-addressed layer. Its vertical extent z_TGI is process-specific and is defined during process qualification as the range of z coordinates over which:

- The substrate's SC class transitions from SC-III (structural layers not qualified for temporal addressing) to SC-II or SC-I (layers qualified for temporal address encoding)
- Spatial-temporal co-registration must be maintained to within the process's registration tolerance
- The physical properties that govern both spatial patterning fidelity and temporal address resolution are simultaneously present and measurable

The boundaries of z_TGI — the **TGI floor** (z_f) and **TGI ceiling** (z_c) — MUST be identified and recorded for each qualified process. Measurements required by this standard are taken within or with reference to this defined zone.

### 2.3 The Two Failure Modes of the TGI

TGI failures fall into two categories that are mechanistically distinct:

**Type I — Registration Failure:** The spatial and temporal coordinate systems diverge. A commit operation directed to spatial coordinates (x₀, y₀) and temporal address τ₀ is executed at (x₀ + Δx, y₀ + Δy) or with address τ₀ + Δτ due to accumulated registration error across the TGI zone. Type I failures are systematic: they produce spatially correlated error patterns across the die and are detectable by spatial mapping.

**Type II — Interface Integrity Failure:** Physical degradation at the TGI boundary — roughness, compositional non-uniformity, stress, or delamination — locally reduces the substrate clarity available to temporal operations in the layers above. Type II failures are locally stochastic: they produce islands of elevated temporal address error rate that correlate to defect sites in the TGI zone rather than to systematic registration offsets.

TGI metrology is designed to detect and characterize both failure types. Parameters in Sections 5 through 8 primarily address Type I. Parameters in Sections 6 and 9 primarily address Type II.

### 2.4 Relationship to Substrate Clarity

Substrate clarity (SC) is measured by the Temporal Contrast Test (TCT) and reflects the bulk property of a substrate region to sustain distinct temporal addresses. The TGI introduces a directional, depth-dependent modulation of this property. A substrate with nominally high SC bulk values can exhibit locally degraded effective SC at the TGI boundary due to interface roughness, compositional grading, or stress-induced propagation velocity variation.

TGI metrology therefore complements TCT rather than substituting for it. TCT confirms that the bulk SC class of a substrate lot meets the process requirement. TGI metrology confirms that the interface conditions within the TGI zone do not locally suppress the effective SC below the qualified minimum.

---

## 3. Measurement Parameter Taxonomy

### 3.1 Primary Parameters

This standard defines six primary TGI measurement parameters. Each is measured independently and reported separately. Together they provide complete characterization of TGI quality.

| Parameter | Symbol | Type Addressed | Section |
|---|---|---|---|
| Spatial-Temporal Registration | STR | Type I | §5 |
| Interface Continuity | IC | Type II | §6 |
| Temporal Address Overlay Error | TAOE | Type I | §7 |
| TGI Uniformity Index | TUI | Type I + II | §8 |
| Coherence Layer Gradient | CLG | Type II | §9 |
| Geometric Drift Correlation | GDC | Type I | §10 |

### 3.2 Derived Parameters

Two derived parameters are computed from combinations of primary measurements. Derived parameters are not independently measured; they are calculated during data analysis (§12).

| Derived Parameter | Symbol | Inputs | Description |
|---|---|---|---|
| Effective Interface SC | SC_eff | IC, CLG | Local effective substrate clarity at the TGI boundary, accounting for interface and gradient effects |
| Registration-Weighted Density Limit | RWDL | STR, TAOE, TUI | The maximum temporal density supportable at a given die location given the measured registration quality |

### 3.3 Parameter Independence

STR and TAOE are related but not identical. STR measures the geometric offset between coordinate systems using reference structures in the TGI zone. TAOE measures the error of actually committed temporal addresses at known spatial locations. STR is a property of the TGI structure itself; TAOE is a property of the TRS stack operating through that structure. Both must be measured; one does not substitute for the other.

Similarly, IC and CLG are related but address different physical phenomena. IC characterizes the physical quality of the interface layer (roughness, composition). CLG characterizes how coherence properties — the precondition for temporal address resolution — change through the z direction across the TGI zone. A smooth, compositionally uniform interface (high IC) does not guarantee a gentle coherence gradient; material systems exist in which a physically smooth interface produces a sharp coherence step that limits effective temporal addressing above it.

---

## 4. Instrumentation Requirements

### 4.1 Instrument Classes

TGI metrology requires four instrument classes. Each class is defined by its functional role. Specific implementations may vary by manufacturer and process node, but all implementations MUST meet the minimum specifications defined in this section.

| Instrument Class | Abbreviation | Primary Parameters Measured |
|---|---|---|
| Temporal Registration Microscope | TRM | STR, TAOE, TUI |
| Interface Structure Profiler | ISP | IC |
| Coherence Gradient Scanner | CGS | CLG, SC_eff |
| Geometric Drift Analyzer | GDA | GDC, STR (cross-check) |

### 4.2 Temporal Registration Microscope

The TRM is the primary instrument for spatial-temporal co-registration measurements. It must simultaneously resolve spatial positions within the TGI zone and read back temporal address assignments from reference structures embedded in the substrate.

**R-TRM-01:** The TRM MUST achieve spatial positioning accuracy of ≤ 0.5 nm (3σ) in both x and y axes across the full measurement field.

**R-TRM-02:** The TRM MUST be capable of reading temporal address reference structures with a temporal address resolution of ≤ 1/1024 of the full address range [0, 1).

**R-TRM-03:** The TRM measurement field MUST cover a minimum area of 50 μm × 50 μm in a single acquisition. Stitched acquisitions are permitted for larger fields but require stitching error characterization as part of instrument qualification.

**R-TRM-04:** The TRM MUST provide a co-registered output that associates each measured temporal address with the spatial coordinates at which the address was read, with coordinate uncertainty included in the output record.

**R-TRM-05:** The TRM MUST be able to access the TGI zone without removal of overlying layers (non-destructive access) in all process configurations for which it is qualified. Destructive cross-section measurement is permitted for qualification measurements only, not for in-line production metrology.

### 4.3 Interface Structure Profiler

The ISP characterizes the physical properties of the TGI boundary — its roughness, compositional uniformity, and mechanical integrity.

**R-ISP-01:** The ISP MUST measure surface/interface roughness with a vertical resolution of ≤ 0.1 nm RMS across a measurement field of ≥ 10 μm × 10 μm.

**R-ISP-02:** The ISP MUST be capable of depth-resolved compositional measurement within the TGI zone, with a depth resolution of ≤ 0.5 nm.

**R-ISP-03:** The ISP MUST measure interface stress distribution with a spatial resolution of ≤ 1 μm, sufficient to resolve stress concentrations at device-scale features within the TGI zone.

**R-ISP-04:** The ISP MUST operate non-destructively for in-line measurements. Destructive ISP measurements (e.g., cross-section TEM) are reserved for failure analysis and process qualification, not production monitoring.

### 4.4 Coherence Gradient Scanner

The CGS measures the depth profile of coherence properties through the TGI zone, establishing how the substrate's capacity for temporal address resolution evolves from the TGI floor to the TGI ceiling.

**R-CGS-01:** The CGS MUST provide depth-resolved coherence property measurements at a z-resolution of ≤ 1 nm within the TGI zone.

**R-CGS-02:** The CGS measurement MUST be calibrated against the TCT SC rating for the bulk substrate above the TGI ceiling and the bulk substrate below the TGI floor. The CGS depth profile must interpolate between these two calibration points through the TGI zone.

**R-CGS-03:** The CGS MUST measure at a minimum of three z depths within the TGI zone — at z_f (TGI floor), at (z_f + z_c)/2 (TGI midpoint), and at z_c (TGI ceiling) — in each measurement pass. Additional depths MAY be measured to characterize sharp gradients.

**R-CGS-04:** The CGS MUST produce a continuous depth profile by interpolation from measured points, using a documented interpolation method. The interpolation method MUST be included in the instrument qualification record.

### 4.5 Geometric Drift Analyzer

The GDA measures the spatial stability of Tier 1 geometric features across the wafer and quantifies how local geometric drift in those features correlates with temporal address error in overlying Tier 2 operations.

**R-GDA-01:** The GDA MUST measure in-plane geometric feature positions with an accuracy of ≤ 1 nm (3σ) relative to die origin, across the full die extent.

**R-GDA-02:** The GDA MUST cover the full wafer extent in a single measurement session without change of reference frame. Multi-session measurements that require reference frame stitching MUST characterize and report the stitching error contribution to the total GDC uncertainty.

**R-GDA-03:** The GDA MUST produce a vector displacement field — a map of (Δx, Δy) displacement vectors at a minimum grid density of one point per 500 μm × 500 μm across the die — that captures the spatial pattern of geometric drift.

**R-GDA-04:** The GDA displacement field MUST be co-registered to the same die coordinate system used by the TRM, to enable direct comparison of GDA and STR results.

### 4.6 Instrument Interdependence

The four instrument classes share one critical requirement: they must all reference a common die coordinate system. Without a common reference, measurements from different instruments cannot be co-registered and the derived parameters SC_eff and RWDL cannot be computed.

**R-INSTR-01:** All instruments used for TGI metrology at a given fab MUST be calibrated to a common die coordinate reference, traceable to the fab's primary coordinate standard. The coordinate standard MUST be calibrated to a national measurement standard with documented traceability.

**R-INSTR-02:** The cross-instrument coordinate registration error MUST be ≤ 2 nm (3σ) between any two instruments used in the same measurement session. Cross-instrument registration MUST be verified at the beginning of each measurement campaign using a qualified reference coupon.

---

## 5. Spatial-Temporal Registration

### 5.1 Definition

**Spatial-Temporal Registration (STR)** is the degree of alignment between the spatial coordinate system of the geometric layers and the temporal address space of the TRS at the TGI boundary. It is expressed as a vector offset field — the mapping from each spatial position (x, y) in the TGI zone to the registration error (Δx_str, Δy_str, Δτ_str) at that position.

A perfectly registered TGI has a zero vector offset field everywhere: every spatial position maps to exactly the temporal address assigned to it in the TRS intent map, with no position-dependent bias. Real processes exhibit non-zero STR due to thermal expansion during processing, stage positioning error during Tier 2 tool setup, and distortion introduced by process steps between Tier 1 patterning and Tier 2 commit.

### 5.2 Physical Basis

STR is measured using **Temporal Registration Marks (TRMs)** — specialized structures patterned in the TGI zone during Tier 1 processing that carry encoded temporal addresses assigned by the TRS at Tier 2 commit. A TRM consists of:

- A geometric reference target (a spatial anchor patterned at a known die coordinate)
- An adjacent temporal address encoding region (a substrate area in which the TRS commits a reference address during the Tier 2 processing of the TGI layer)

The geometric target provides the spatial position. The temporal address encoding region provides the committed address. The STR at a given TRM site is the vector difference between the spatial position expected from the die coordinate system and the temporal address expected from the TRS intent map, minus the measured values:

```
STR(x, y) = [ Δx_str, Δy_str, Δτ_str ]

Where:
  Δx_str = x_measured - x_designed      (nm)
  Δy_str = y_measured - y_designed      (nm)
  Δτ_str = τ_committed - τ_assigned     (address units, normalized to [0,1))
```

### 5.3 Measurement Protocol

**Setup:**

1. Confirm that the wafer has completed all Tier 1 TGI-zone processing steps and the TGI Tier 2 reference commit has been executed.
2. Load the wafer into the TRM instrument and establish die coordinate registration per R-INSTR-01.
3. Load the TRS intent map for the TGI reference layer from the wafer lot record. This map specifies the designed temporal address τ_assigned for every TRM site on the die.

**Measurement sequence:**

1. Navigate to the first TRM site per the sampling plan (§11).
2. Acquire the spatial position of the geometric reference target using the TRM spatial imaging channel. Record (x_measured, y_measured) with uncertainty.
3. Acquire the committed temporal address from the temporal address encoding region of the same TRM site. Record τ_committed with uncertainty.
4. Compute STR at this site.
5. Repeat steps 2–4 for all TRM sites in the sampling plan without changing instrument setup.
6. Upon completion, verify coordinate registration has not drifted by re-measuring the first site. If drift exceeds 1 nm in either axis, the measurement session is invalid and must be repeated.

**R-STR-01:** A minimum of 49 TRM sites per die MUST be measured, distributed in a 7×7 grid with uniform spacing across the die extent. The outermost sites MUST be within 200 μm of the die edge.

**R-STR-02:** TRM sites MUST be placed in all four quadrants of the die. A measurement set that has fewer than 10 sites in any quadrant is non-conformant.

**R-STR-03:** The STR measurement MUST be performed within 4 hours of the Tier 2 reference commit operation. Temporal address encoding regions are subject to relaxation processes that can alter the committed address over time; measurements beyond this window require documentation of the elapsed time and its estimated effect on τ_committed.

### 5.4 Data Reduction

The per-site STR vectors are combined into three wafer maps:

- **Δx_str map:** Spatial distribution of x-axis registration error across measured sites
- **Δy_str map:** Spatial distribution of y-axis registration error across measured sites
- **Δτ_str map:** Spatial distribution of temporal address registration error across measured sites

From each map, the following statistics are computed and reported:

| Statistic | Definition |
|---|---|
| Mean (μ) | Population mean of the error across all sites |
| 3σ range | Three standard deviation range, representing process variation |
| Maximum absolute value | Worst-case site error |
| Systematic gradient | Linear regression slope across die extent, capturing die-scale registration tilt |
| Residual (non-linear) component | Difference between measured map and the fitted linear gradient |

The systematic gradient is physically significant: it represents die-scale coordinate system tilt that can be corrected by TRM tool alignment. The residual component represents higher-order distortion that cannot be corrected by alignment alone and must be addressed at the process level.

---

## 6. Interface Continuity

### 6.1 Definition

**Interface Continuity (IC)** is a composite parameter that characterizes the physical quality of the TGI boundary — the surface at z_f that separates the Tier 1 structural layer stack from the TGI zone proper. It encompasses three sub-parameters:

| Sub-parameter | Symbol | Unit | Description |
|---|---|---|---|
| Interface Roughness | IC_R | nm RMS | Root-mean-square roughness of the z_f surface |
| Compositional Transition Width | IC_C | nm | Width of the compositional transition zone at z_f |
| Interface Stress Uniformity | IC_S | MPa (σ) | Standard deviation of in-plane stress across the interface |

The overall IC rating is a weighted composite:

```
IC = 1 - [ w_R × norm(IC_R) + w_C × norm(IC_C) + w_S × norm(IC_S) ]

Where:
  norm(x)  = x / x_max  (normalization to the maximum acceptable value per SC class)
  w_R      = 0.45  (roughness weight)
  w_C      = 0.35  (compositional weight)
  w_S      = 0.20  (stress weight)
  IC       ∈ [0, 1]; higher is better
```

The weights w_R, w_C, w_S reflect the relative contribution of each sub-parameter to effective substrate clarity degradation, derived from empirical calibration against TCT results across a range of interface conditions. The weights are fixed at the values above for this revision. Process-specific weight adjustments require a revision to this standard.

### 6.2 Measurement Protocol — Interface Roughness (IC_R)

1. Load the wafer into the ISP instrument and navigate to the first IC measurement site (§11).
2. Select z_f as the measurement depth. z_f is determined from the process stack record for the wafer lot.
3. Acquire a surface roughness scan over a 10 μm × 10 μm field centered on the measurement site.
4. Apply a Gaussian high-pass filter with a 1 μm cutoff to remove long-range waviness from the roughness measurement. Record the filtered RMS roughness as IC_R at this site.
5. Repeat for all IC sites in the sampling plan.

**R-IC-01:** The ISP scan field MUST be ≥ 10 μm × 10 μm. Smaller fields undersample the roughness spatial frequency spectrum and produce systematically low IC_R values.

**R-IC-02:** The Gaussian high-pass filter cutoff MUST be 1 μm ± 10%. A different cutoff requires documentation and comparison data against the standard cutoff.

### 6.3 Measurement Protocol — Compositional Transition Width (IC_C)

1. At each IC measurement site, execute a depth-resolved compositional scan from 5 nm below z_f to 5 nm above z_f.
2. Identify the z positions at which the composition of the primary transition species reaches 10% and 90% of its final value. IC_C is the z distance between these two positions.
3. Record IC_C and the depth profile for each site.

**R-IC-03:** The depth scan MUST resolve composition at 0.5 nm z-increments or finer. Coarser increments produce quantization error in IC_C that exceeds the measurement uncertainty budget.

**R-IC-04:** For processes with multiple co-transitioning species, IC_C is taken as the widest individual species transition width. The transition widths of all species MUST be reported individually in addition to the IC_C value used in the composite calculation.

### 6.4 Measurement Protocol — Interface Stress Uniformity (IC_S)

1. Using the ISP stress measurement capability, map in-plane biaxial stress across the full TGI-zone measurement sites.
2. Compute the standard deviation of the stress values across all measured sites on the wafer.
3. Record this standard deviation as IC_S.

**R-IC-05:** Stress measurement MUST be performed after all TGI-zone deposition and anneal steps are complete and before any Tier 2 processing. Tier 2 commit operations can locally relieve or redistribute stress and would confound IC_S results.

**R-IC-06:** Stress measurement sites MUST be co-located with IC_R and IC_C sites to enable site-level correlation between roughness, composition, and stress.

---

## 7. Temporal Address Overlay Error

### 7.1 Definition

**Temporal Address Overlay Error (TAOE)** is the difference between the temporal address intended by the TRS intent map and the temporal address actually committed to the substrate at a given spatial location, measured after commit and referenced to the actual spatial position of the measurement site.

TAOE differs from the Δτ_str component of STR in a critical respect: STR measures the co-registration of coordinate systems using reference structures, whereas TAOE measures the address accuracy of production operations at real device sites. STR captures the systematic offset of the coordinate mapping; TAOE captures the combined effect of STR error, TRS resolution layer (L3) apodization imperfection, and TCU commit-level variation.

```
TAOE(x, y) = τ_committed(x, y) - τ_intent(x, y)

Where:
  τ_committed(x, y) = temporal address read back from the substrate at (x, y)
  τ_intent(x, y)    = temporal address specified in the TRS intent map for (x, y)
  TAOE              ∈ (−0.5, +0.5)  (address units, normalized)
```

### 7.2 Measurement Sites

TAOE is measured at **Production Address Verification Sites (PAVS)** — locations within the die where temporal operations have been committed as part of the production process, not as dedicated test structures. This distinguishes TAOE from STR: STR uses purpose-built TRMs; TAOE reads actual production commits.

PAVS selection MUST follow the criteria in §11. In addition:

**R-TAOE-01:** PAVS MUST be distributed across the full temporal address range covered by the production layer being measured. A PAVS set that samples only a subset of the address range does not characterize TAOE for unsampled addresses.

**R-TAOE-02:** PAVS MUST include sites at the boundaries of adjacent temporal address regions — locations where two operations with closely spaced temporal addresses are committed at spatially proximate substrate positions. These boundary sites are where TAOE is most likely to reveal the effects of address crowding near the substrate clarity limit.

### 7.3 Measurement Protocol

1. Load the wafer into the TRM after completion of the production layer commit.
2. Load the TRS intent map for the production layer.
3. Navigate to the first PAVS per the sampling plan.
4. Acquire τ_committed at the PAVS using the TRM's temporal address readback channel.
5. Look up τ_intent for the same (x, y) position from the intent map.
6. Compute TAOE at this site.
7. Repeat for all PAVS in the sampling plan without instrument reconfiguration.

**R-TAOE-03:** The TAOE measurement MUST be performed within 8 hours of the commit operation for the measured layer. Address relaxation beyond this window introduces time-dependent drift that is not classified as TAOE.

**R-TAOE-04:** TAOE MUST be measured in the same TRM session as STR for the same layer, without wafer removal from the instrument between the two measurements. This requirement ensures that coordinate registration is identical for both parameters.

### 7.4 TAOE Decomposition

Raw TAOE values are decomposed into two components that carry different engineering significance:

**Systematic TAOE (TAOE_sys):** The component of TAOE that is spatially correlated across the die — reproducible from site to site in a predictable pattern. Systematic TAOE is primarily caused by STR error propagating through the TRS resolution layer. It can be partially corrected by TRM alignment and intent map adjustment.

**Random TAOE (TAOE_rnd):** The component of TAOE that is not spatially correlated — varying randomly from site to site. Random TAOE arises from TCU commit-level variation, local substrate non-uniformity, and SCR coherence slot jitter. It cannot be corrected without process changes.

Decomposition is performed by fitting a low-order polynomial surface to the TAOE map (the systematic component) and taking the residuals (the random component). The polynomial order MUST be ≤ 4; higher-order fits risk absorbing genuine random variation into the systematic component.

---

## 8. TGI Uniformity Index

### 8.1 Definition

The **TGI Uniformity Index (TUI)** is a scalar measure of the spatial consistency of TGI properties across the die. While STR and TAOE characterize the accuracy of the spatial-temporal mapping, TUI characterizes how uniformly that mapping is maintained across the full die extent. A die with excellent mean STR and TAOE values but high spatial variation — implying that some regions of the die have significantly worse registration than others — will have a low TUI.

TUI is defined as:

```
TUI = 1 - max( σ_STR_x / STR_x_tol,
               σ_STR_y / STR_y_tol,
               σ_TAOE  / TAOE_tol  )

Where:
  σ_STR_x   = standard deviation of Δx_str across all measured sites
  σ_STR_y   = standard deviation of Δy_str across all measured sites
  σ_TAOE    = standard deviation of TAOE across all PAVS
  STR_x_tol, STR_y_tol, TAOE_tol = tolerance values per SC class (§13)
  TUI        ∈ (−∞, 1]; values < 0 indicate that variation exceeds tolerance
```

A TUI of 1.0 indicates zero variation across the die — unachievable in practice. The acceptance threshold for TUI is SC-class-dependent (§13).

### 8.2 Measurement Protocol

TUI is a derived quantity computed from the STR and TAOE site-level data. It does not require a separate measurement procedure beyond those defined in §5 and §7. TUI computation is part of the data analysis step (§12).

**R-TUI-01:** TUI MUST be computed using the full set of measured STR and TAOE sites without excluding outliers, unless the outlier exclusion procedure of §12.3 has been applied and documented.

**R-TUI-02:** TUI MUST be reported separately for each quadrant of the die in addition to the die-level value. Quadrant-level TUI enables identification of localized uniformity problems that would be masked in a die-level average.

### 8.3 Uniformity Failure Patterns

TUI failures exhibit characteristic spatial patterns that carry diagnostic information:

| Pattern | Description | Probable Cause |
|---|---|---|
| Radial gradient | TUI decreases monotonically from die center to edge | Stage heating or cooling during Tier 2 commit; thermal expansion mismatch |
| Quadrant asymmetry | One quadrant has significantly lower TUI than others | TCU alignment error in the affected die region; CDN phase variation across the SCR zone |
| Stripe pattern | Alternating bands of high and low TUI across the die | Scan-direction-dependent error in the Tier 2 tool; resonance in the stage positioning system |
| Random low-TUI islands | Isolated sites of poor uniformity distributed without spatial pattern | Local substrate defects; stochastic TCU commit variation |

Pattern classification is performed during data analysis (§12) and included in the TUI report.

---

## 9. Coherence Layer Gradient

### 9.1 Definition

The **Coherence Layer Gradient (CLG)** is the rate of change of coherence properties with depth z through the TGI zone. It quantifies how sharply the substrate transitions from the coherence state of the Tier 1 structural layers (which are not qualified for temporal addressing) to the coherence state of the Tier 2 temporal layers.

A gentle CLG — a slow, monotonic increase in coherence capacity from z_f to z_c — is favorable. It allows the TRS to operate with gradually improving substrate support as depth increases through the TGI zone, with no abrupt coherence boundaries that could produce sharp spatial-temporal interface defects.

A steep or non-monotonic CLG — a rapid transition, a step function, or a local minimum within the TGI zone — produces a concentration of temporal address error at the depth of the transition. Operations committed at or near a sharp coherence boundary experience reduced effective SC without warning from bulk TCT measurements.

CLG is expressed in units of normalized SC per nanometer of depth:

```
CLG(z) = d(SC_norm(z)) / dz

Where:
  SC_norm(z) = the normalized coherence capacity at depth z,
               calibrated to 0 at z_f (Tier 1 structural value)
               and 1 at z_c (Tier 2 bulk SC value)
  CLG(z)     = (SC units/nm); positive values indicate increasing coherence with depth
```

### 9.2 Measurement Protocol

1. Load the wafer into the CGS instrument.
2. Confirm calibration anchors: verify that the CGS reads SC_norm = 0 on a reference region of the Tier 1 structural layer and SC_norm = 1 on a reference region of the qualified Tier 2 bulk layer.
3. At each CLG measurement site (§11), execute a depth scan from z_f − 2 nm to z_c + 2 nm.
4. Record SC_norm at each z increment (≤ 1 nm spacing per R-CGS-01).
5. Compute the derivative d(SC_norm)/dz at each z increment using a central difference method.
6. Identify and record the depth z_peak at which CLG is maximum (the steepest point in the gradient).
7. Record the maximum CLG value, CLG_max = CLG(z_peak).
8. Record the integrated CLG over the full TGI zone as a measure of total coherence transition breadth.

**R-CLG-01:** CLG measurements MUST be taken before any Tier 2 commit operations are executed in the TGI zone. Commit operations alter the local coherence state of the substrate and would confound CLG measurements.

**R-CLG-02:** CLG measurement sites MUST be co-located with IC measurement sites to enable correlation between interface physical properties (IC) and coherence gradient properties (CLG).

### 9.3 Non-Monotonic Gradient Detection

A non-monotonic CLG — one where SC_norm decreases at some depth within the TGI zone before increasing again — is a process anomaly that MUST be flagged as a critical finding regardless of the CLG_max value. Non-monotonic gradients indicate the presence of a buried low-coherence layer within the TGI zone that would locally suppress temporal address resolution for all commit operations above it.

**R-CLG-03:** The CLG analysis MUST explicitly check for non-monotonicity in the SC_norm depth profile at each site. A site where SC_norm decreases by more than 0.05 normalized SC units at any depth within the TGI zone MUST be flagged and reported to the yield management system as a CLG non-monotonicity finding, irrespective of the overall IC and CLG_max values.

---

## 10. Geometric Drift Correlation

### 10.1 Definition

**Geometric Drift Correlation (GDC)** measures the degree to which spatial displacement in Tier 1 geometric features — caused by thermal effects, pattern density-dependent stress relaxation, and inter-layer mechanical coupling — predicts the temporal address error observed in Tier 2 commit operations above those features.

A high GDC means that geometric drift in the Tier 1 layers is a reliable predictor of TAOE in the Tier 2 layers. This is significant for two reasons:

1. It provides a root-cause pathway: if GDC is high, TAOE improvement requires geometric drift reduction in Tier 1, not adjustment of TRS parameters.
2. It enables predictive correction: if GDC is high and the geometric drift map is measured before Tier 2 commit, the drift map can be used to pre-correct the TRS intent map, reducing TAOE before it occurs.

GDC is expressed as the Pearson correlation coefficient between the GDA-measured geometric drift vectors and the TRM-measured TAOE vectors at co-located sites:

```
GDC = corr( [Δx_GDA, Δy_GDA], [TAOE_x_equiv, TAOE_y_equiv] )

Where:
  Δx_GDA, Δy_GDA    = geometric drift vector components from the GDA map
  TAOE_x_equiv,
  TAOE_y_equiv       = the spatial-equivalent projections of TAOE onto the x, y axes
                       (derived from the temporal address gradient direction in the TRS intent map)
  GDC               ∈ [−1, +1]
```

### 10.2 Measurement Protocol

GDC is a derived parameter that requires both GDA and TAOE measurements at co-located sites. The measurement protocol is:

1. Before Tier 2 commit: execute GDA measurement across the full die extent per the GDA measurement protocol. Record the displacement vector field.
2. After Tier 2 commit: execute TAOE measurement at co-located sites per §7.
3. Compute GDC using the co-located pairs.

**R-GDC-01:** GDA measurement MUST be performed after all Tier 1 TGI-zone processing steps are complete and before the Tier 2 reference commit. This sequencing ensures that the measured geometric drift reflects the final Tier 1 state rather than an intermediate process state.

**R-GDC-02:** The GDA and TAOE measurements MUST use a common site list with a minimum of 49 co-located sites per die.

### 10.3 Predictive Intent Map Correction

When GDC ≥ 0.85 (indicating that geometric drift accounts for ≥ 72% of the variance in TAOE), a **Predictive Intent Map Correction (PIMC)** MAY be applied. PIMC uses the GDA displacement field to pre-warp the TRS intent map before the Tier 2 commit, reducing TAOE by compensating for the expected drift in advance.

PIMC is not mandatory. It is a process optimization available when GDC is sufficiently high to make the correction more beneficial than its residual uncertainty. Fabs implementing PIMC MUST:

- Document the PIMC algorithm and its transfer function from GDA displacement to intent map adjustment
- Validate PIMC effectiveness by comparing TAOE with and without PIMC applied on qualification wafers
- Record the PIMC status (applied or not applied) in each wafer lot record

---

## 11. Sampling Strategy

### 11.1 Sampling Hierarchy

TGI metrology operates at two spatial scales:

- **Wafer-level:** Measurements are distributed across the wafer to capture across-wafer (AWW) variation
- **Die-level:** Within each sampled die, measurements are distributed across the die to capture within-die (WID) variation

Both scales are required. Wafer-level sampling without die-level sampling cannot detect localized TGI failures that average out across the die. Die-level sampling without wafer-level sampling cannot detect position-dependent AWW trends.

### 11.2 Wafer-Level Sampling Requirements

**R-SAMP-01:** A minimum of 9 dies per wafer MUST be measured for all primary TGI parameters. Dies MUST be selected from the following positions: center, four edge positions (top, bottom, left, right), and four quadrant positions (one per quadrant, at approximately 70% of the maximum wafer radius).

**R-SAMP-02:** For production monitoring after process qualification, a reduced sampling of 5 dies per wafer is permitted (center + four edge positions). The quadrant positions are required only for qualification and for any wafer lot that follows a process excursion.

**R-SAMP-03:** Edge dies (those within 3 mm of the wafer flat) MUST NOT be used as primary measurement sites. Edge dies may be added as supplementary sites when investigating edge-specific effects.

### 11.3 Die-Level Sampling Requirements

**R-SAMP-04:** Within each sampled die, STR and TAOE measurements MUST cover a 7×7 minimum grid per R-STR-01.

**R-SAMP-05:** IC and CLG measurements MUST be taken at a minimum of 9 sites per die in a 3×3 grid, with sites co-located between IC and CLG per R-CLG-02.

**R-SAMP-06:** GDA measurements cover the full die continuously (per R-GDA-03) and are not subject to site-count minimums. The GDA vector field at the co-located GDC sites is extracted from the continuous map.

**R-SAMP-07:** STR/TAOE sites, IC/CLG sites, and GDC sites MUST NOT all overlap at the same physical locations. Each parameter set MUST occupy distinct die regions except where co-location is explicitly required (IC and CLG; GDA and TAOE). Over-concentration of all metrology structures at a single die location would perturb the local substrate state and invalidate measurements.

### 11.4 First-Article and Qualification Sampling

For process qualification and for the first production lot on any new SCR zone, the sampling requirements are:

- Wafer-level: full 9-die set per R-SAMP-01
- Die-level STR/TAOE: 11×11 grid (minimum 121 sites)
- Die-level IC/CLG: 5×5 grid (minimum 25 sites)
- GDC: computed from the full 11×11 TAOE grid

First-article sampling results are the baseline against which subsequent production monitoring is compared.

---

## 12. Data Analysis and Reporting

### 12.1 Analysis Sequence

TGI metrology data MUST be analyzed in the following sequence. Earlier steps produce inputs required by later steps; the sequence MUST NOT be reversed.

1. **Coordinate unification:** Apply cross-instrument coordinate registration (R-INSTR-02) to bring all measurements into the common die coordinate system.
2. **Primary parameter computation:** Compute STR, IC, TAOE, CLG, and GDC from raw instrument outputs per their respective protocol sections.
3. **TUI computation:** Compute TUI from the STR and TAOE site-level data per §8.1.
4. **Derived parameter computation:** Compute SC_eff and RWDL per §3.2.
5. **TAOE decomposition:** Separate TAOE_sys and TAOE_rnd per §7.4.
6. **Pattern classification:** Classify TUI failure patterns per §8.3, if TUI is below the acceptance threshold.
7. **Non-monotonicity check:** Apply CLG non-monotonicity detection per §9.3.
8. **GDC-PIMC assessment:** Assess whether GDC meets the threshold for PIMC consideration per §10.3.
9. **Acceptance evaluation:** Apply acceptance criteria per §13.
10. **Report generation:** Compile the TGI Metrology Report per §12.4.

### 12.2 Derived Parameter Computation

**SC_eff (Effective Interface SC):**

```
SC_eff = SC_bulk × IC × f(CLG_max)

Where:
  SC_bulk   = TCT-measured SC rating of the bulk Tier 2 layer above the TGI ceiling
  IC        = composite Interface Continuity rating from §6.1
  f(CLG_max) = gradient penalty function:
               f(x) = 1.0        if x ≤ CLG_threshold (gentle gradient; no penalty)
               f(x) = 1 - k(x - CLG_threshold)  if x > CLG_threshold (steep gradient penalty)
               where CLG_threshold and k are defined per SC class in §13
```

SC_eff represents the practical upper bound on temporal address resolution achievable at the TGI boundary, accounting for both physical interface quality and coherence gradient steepness. A SC_eff that falls below the minimum SC class threshold for the process is a TGI failure even if bulk TCT passes.

**RWDL (Registration-Weighted Density Limit):**

```
RWDL = TD_qualified × TUI × ( 1 - |TAOE_rnd| / TAOE_rnd_max )

Where:
  TD_qualified   = the qualified maximum temporal density (MQD) for the process node
  TUI            = TGI Uniformity Index
  TAOE_rnd       = mean absolute random TAOE across PAVS
  TAOE_rnd_max   = maximum acceptable TAOE_rnd per SC class (§13)
  RWDL           ≤ TD_qualified always
```

RWDL is the actionable output of TGI metrology for design teams: it quantifies the maximum temporal density that is safely supportable at any given die location, given the measured quality of the TGI at that location. Designs that place maximum-density temporal operations at locations where RWDL is below the design-time density target will exhibit elevated defect rates.

### 12.3 Outlier Handling

A measurement site is classified as a candidate outlier if its value for any primary parameter deviates from the die-level mean by more than 4 standard deviations (4σ). Candidate outliers MUST be evaluated before exclusion:

1. Review instrument log for evidence of measurement anomaly at the candidate site (positioning error, signal dropout, environmental disturbance).
2. If a measurement anomaly is confirmed, the site may be excluded from statistical analysis and re-measured if within the 4-hour STR or 8-hour TAOE windows.
3. If no measurement anomaly is found, the site value is retained. An elevated measurement at a verified-clean site is a genuine TGI finding, not an outlier.

Excluded sites MUST be documented in the TGI Metrology Report with the reason for exclusion.

### 12.4 TGI Metrology Report

Every measured wafer lot MUST produce a TGI Metrology Report containing:

- Wafer lot identifier and process step identifier
- Measurement date/time and instrument identifiers with calibration status
- For each sampled die: die position on wafer, and for each primary parameter: all site-level values, computed statistics (μ, 3σ, maximum), and maps
- TUI die-level and quadrant-level values with pattern classification if below threshold
- SC_eff and RWDL maps (die-level)
- CLG non-monotonicity findings (if any)
- GDC values and PIMC recommendation status
- Acceptance evaluation result (pass/fail/conditional) per §13
- Outlier log
- Any deviations from standard measurement protocol with justification

Reports MUST be retained for the wafer lot duration plus 90 days and MUST be accessible to the yield management system.

---

## 13. Acceptance Criteria

### 13.1 Criteria by SC Class

Acceptance criteria are defined per SC class of the target process layer. The relevant SC class is the qualified SC class of the Tier 2 layer immediately above the TGI ceiling, as recorded in the process qualification record.

#### SC-I Processes (SC Rating > 0.92)

| Parameter | Acceptance Threshold | Disposition if Failed |
|---|---|---|
| STR Δx_str (3σ) | ≤ 2.0 nm | Reject lot; TRS alignment review |
| STR Δy_str (3σ) | ≤ 2.0 nm | Reject lot; TRS alignment review |
| STR Δτ_str (3σ) | ≤ 0.002 address units | Reject lot; intent map review |
| IC_R | ≤ 0.3 nm RMS | Conditional hold; interface re-qualification |
| IC_C | ≤ 2.0 nm | Conditional hold; process chemistry review |
| IC_S (σ) | ≤ 15 MPa | Conditional hold; stress management review |
| IC (composite) | ≥ 0.88 | Reject lot if SC_eff falls below SC-I threshold |
| TAOE_sys (3σ) | ≤ 0.003 address units | Conditional hold; STR-correlated review |
| TAOE_rnd (mean absolute) | ≤ 0.001 address units | Reject lot; TCU process review |
| TUI (die-level) | ≥ 0.85 | Conditional hold; pattern investigation |
| CLG_max | ≤ 0.015 SC units/nm | Conditional hold; deposition process review |
| CLG non-monotonicity | None permitted | Reject lot; process investigation |
| SC_eff | ≥ 0.90 | Reject lot if below threshold |
| GDC | Reported, not gating | Review if GDC ≥ 0.85 for PIMC consideration |

#### SC-II Processes (SC Rating 0.75 – 0.92)

| Parameter | Acceptance Threshold | Disposition if Failed |
|---|---|---|
| STR Δx_str (3σ) | ≤ 4.0 nm | Conditional hold; TRS alignment review |
| STR Δy_str (3σ) | ≤ 4.0 nm | Conditional hold; TRS alignment review |
| STR Δτ_str (3σ) | ≤ 0.005 address units | Conditional hold; intent map review |
| IC_R | ≤ 0.6 nm RMS | Advisory; monitor trend |
| IC_C | ≤ 4.0 nm | Advisory; monitor trend |
| IC_S (σ) | ≤ 30 MPa | Advisory; monitor trend |
| IC (composite) | ≥ 0.75 | Conditional hold if SC_eff drops below SC-II threshold |
| TAOE_sys (3σ) | ≤ 0.006 address units | Advisory; STR-correlated review |
| TAOE_rnd (mean absolute) | ≤ 0.003 address units | Conditional hold; TCU process review |
| TUI (die-level) | ≥ 0.72 | Advisory; pattern investigation |
| CLG_max | ≤ 0.030 SC units/nm | Advisory; deposition process review |
| CLG non-monotonicity | None permitted | Conditional hold; process investigation |
| SC_eff | ≥ 0.73 | Conditional hold if below threshold |

### 13.2 Conditional Hold Procedure

A conditional hold suspends lot dispositioning pending engineering review. The review MUST:

1. Identify the specific failing parameter and its measured value
2. Assess whether the failure is an isolated excursion or a trend
3. Determine whether the failure is correlated with a known process change or equipment event
4. Recommend one of: lot release with flagged record, lot rework (if a rework path exists for the failing layer), or lot reject

Conditional holds MUST be resolved within 24 hours. Lots not dispositioned within 24 hours are automatically escalated to the yield management escalation procedure.

### 13.3 CLG Gradient Penalty Function Parameters

The gradient penalty function f(CLG_max) used in the SC_eff computation (§12.2) uses the following parameters:

| SC Class | CLG_threshold (SC units/nm) | k (penalty slope) |
|---|---|---|
| SC-I | 0.010 | 15.0 |
| SC-II | 0.020 | 8.0 |

These values are calibrated so that a CLG_max at the acceptance threshold reduces SC_eff by approximately 0.02 normalized SC units — a small but non-negligible penalty that grows rapidly for steeper gradients above the threshold.

---

## 14. Calibration Requirements

### 14.1 Calibration Philosophy

All TGI metrology instruments operate in measurement regimes — sub-nanometer spatial, sub-0.001 address-unit temporal — that require active calibration against traceable reference standards. Instrument specifications alone do not ensure measurement accuracy over time; calibration verifies that the instrument continues to perform to its qualified specifications and provides the traceability chain required for measurement uncertainty estimation.

### 14.2 Calibration Reference Standards

Three types of calibration reference standards are used in TGI metrology:

**Spatial Reference Artifact (SRA):** A certified dimensional standard with features at known positions to sub-nanometer accuracy, traceable to the national length standard. Used for TRM spatial channel and GDA calibration.

**Temporal Address Reference Coupon (TARC):** A substrate coupon with temporal address reference structures committed at known addresses by a certified reference process, with committed address values verified by an independent measurement laboratory. Used for TRM temporal channel and TAOE absolute calibration.

**Interface Reference Sample (IRS):** A certified thin-film sample with known surface roughness, compositional profile, and stress state, characterized by the materials standards laboratory. Used for ISP and CGS calibration.

**R-CAL-01:** All calibration reference standards MUST have current certification from a recognized national or international metrology body. Certifications MUST be renewed at intervals not exceeding the standard's specified re-certification period.

### 14.3 Calibration Intervals

| Instrument | Calibration Type | Interval |
|---|---|---|
| TRM (spatial channel) | Full calibration against SRA | Every 90 days |
| TRM (temporal channel) | Full calibration against TARC | Every 90 days |
| TRM (combined) | Cross-channel registration check | Every 30 days |
| ISP (roughness) | Full calibration against IRS roughness | Every 60 days |
| ISP (composition) | Full calibration against IRS compositional profile | Every 60 days |
| ISP (stress) | Full calibration against IRS stress state | Every 60 days |
| CGS | Full calibration against IRS + TARC | Every 90 days |
| GDA | Full calibration against SRA | Every 90 days |
| Cross-instrument registration | Qualified reference coupon check | Before each measurement campaign |

**R-CAL-02:** Any instrument that fails its scheduled calibration MUST be taken out of service immediately. Measurements taken after the calibration due date and before the failure was discovered MUST be reviewed for impact; affected lot records MUST be flagged.

**R-CAL-03:** Calibration results MUST be recorded in the instrument's calibration log and retained for the instrument's service life. Calibration logs MUST be producible on request during process audits.

### 14.4 Interim Verification

Between full calibrations, instruments MUST perform daily interim verification using a facility-internal check standard:

- TRM: verify spatial position of a fixed reference mark to ≤ 0.5 nm; verify temporal address readback of a facility TARC coupon to ≤ 0.0005 address units
- ISP: verify roughness of a facility roughness standard to ≤ 0.05 nm RMS
- CGS: verify depth profile shape against a facility IRS coupon
- GDA: verify displacement measurement of a thermal reference fixture to ≤ 0.5 nm

**R-CAL-04:** An instrument that fails interim verification MUST be taken out of service until the cause is identified and corrected. Full calibration is required before the instrument returns to service following an interim verification failure.

---

## 15. Measurement Uncertainty

### 15.1 Framework

Measurement uncertainty for TGI metrology parameters MUST be estimated using the Guide to the Expression of Uncertainty in Measurement (GUM) framework. This section defines the primary uncertainty sources for each instrument class and specifies the required components of the combined standard uncertainty u_c.

Full GUM-compliant uncertainty budgets are maintained in the instrument qualification records for each instrument at each fab. This section defines the required inputs to those budgets; it does not reproduce complete budgets, which are instrument- and configuration-specific.

### 15.2 TRM Uncertainty Sources

The following uncertainty components MUST be included in TRM uncertainty budgets:

| Source | Type | Applies To |
|---|---|---|
| Stage positioning repeatability | Type A (statistical) | Spatial (x, y) |
| Stage positioning accuracy (calibration residual) | Type B (systematic) | Spatial (x, y) |
| Thermal drift during measurement session | Type B (systematic) | Spatial (x, y) |
| Temporal address readback noise | Type A (statistical) | τ |
| TARC calibration uncertainty | Type B (systematic) | τ |
| Address relaxation (time since commit) | Type B (systematic) | τ |
| Stitching error (if applicable) | Type B (systematic) | Spatial (x, y) |

### 15.3 ISP Uncertainty Sources

| Source | Type | Applies To |
|---|---|---|
| Roughness measurement noise | Type A (statistical) | IC_R |
| IRS roughness calibration uncertainty | Type B (systematic) | IC_R |
| Filter cutoff frequency uncertainty | Type B (systematic) | IC_R |
| Depth resolution | Type B (systematic) | IC_C |
| Compositional calibration uncertainty | Type B (systematic) | IC_C |
| Stress model uncertainty | Type B (systematic) | IC_S |

### 15.4 Uncertainty Reporting Requirements

**R-UNC-01:** Every reported TGI parameter value MUST be accompanied by its expanded uncertainty U at a coverage factor k = 2 (approximately 95% confidence). Reported values without uncertainty are non-conformant.

**R-UNC-02:** The dominant uncertainty source for each parameter MUST be identified and reported. This enables targeted instrument or process improvement when uncertainty is the limiting factor in acceptance evaluation.

**R-UNC-03:** Acceptance decisions MUST use the parameter's measured value without subtracting measurement uncertainty. The full measured value — not the lower bound of the uncertainty interval — is compared to the acceptance threshold. This conservative convention prevents measurement uncertainty from masking genuine threshold violations.

---

## 16. Integration with Process Qualification

### 16.1 TGI Metrology in the TRS Qualification Sequence

The TRS Stack Qualification Procedure ([`docs/fab/TRS_Qualification.md`](../fab/TRS_Qualification.md)) defines the sequence by which a new process is qualified for temporal manufacturing. TGI metrology is required at two points in that sequence:

**Before TRS stack commissioning:** IC and CLG measurements on the bare TGI-zone substrate establish the interface baseline. A substrate that fails IC or CLG criteria before TRS processing indicates a Tier 1 process problem; it MUST be remediated before proceeding to TRS qualification.

**After TRS reference commit:** STR, TAOE, TUI, and GDC measurements on the committed substrate complete the TGI metrology suite. Acceptance criteria per §13 apply. A process that fails TGI acceptance after TRS processing cannot be released for production regardless of other TRS qualification results.

### 16.2 TGI Metrology in SCR Zone Commissioning

SCR Zone Configuration ([`docs/fab/SCR_Zone_Config.md`](../fab/SCR_Zone_Config.md)) requires that TGI metrology results be available before production operations begin in a new or reconfigured SCR zone. Specifically:

- The SC_eff map from TGI metrology is used to confirm that the qualified SC class is achieved throughout the zone's active area
- The RWDL map is used to validate that the zone's designed temporal density does not exceed the RWDL at any die location
- STR and TAOE results are provided to the fab scheduler to initialize any predictive correction workflows

### 16.3 TGI Metrology as a Yield Management Input

TGI Metrology Reports are a primary input to yield management for TGI-attributed defect analysis. The yield management system correlates:

- TAOE_rnd maps with post-process spatial defect inspection maps to identify whether random TAOE is predicting the positions of functional defects
- SC_eff maps with TMU-measured address error rates to validate the SC_eff computation model
- CLG non-monotonicity findings with post-commit TMU anomalies at the same die locations

Yield management may use these correlations to tighten acceptance criteria for specific parameter-process combinations or to flag lot characteristics that warrant increased inspection.

### 16.4 Production Monitoring Cadence

After initial process qualification, TGI metrology transitions from a qualification activity to a production monitoring activity. The monitoring cadence is defined by three tiers:

**Tier 1 — Per-Lot Monitoring:** Applied to every production lot. Uses the reduced 5-die wafer sampling per R-SAMP-02 and the standard die-level site counts per §11.3. All six primary parameters are measured. Acceptance evaluation per §13 is applied in full. The TGI Metrology Report is generated and submitted to the yield management system before the lot is released to subsequent process steps.

**Tier 2 — Periodic Qualification Check:** Applied to one lot per calendar month, or to the first lot following any process change, equipment maintenance event, or SCR zone reconfiguration. Uses the full 9-die wafer sampling per R-SAMP-01 and the first-article die-level site counts per §11.4. Results are compared against the qualification baseline to detect gradual drift in any parameter that would not be caught by Tier 1 monitoring alone.

**Tier 3 — Excursion Response:** Applied to any lot that follows a Tier 1 conditional hold or reject finding, a CCG holdover event flagged by the SCR, or a CLG non-monotonicity finding. Uses first-article sampling plus five additional dies selected from the regions of the wafer adjacent to the failing sites on the triggering lot. Tier 3 measurements are completed before any wafers in the affected lot — or any subsequent lot on the same SCR zone — proceed past the TGI process step.

**R-MON-01:** The cadence tier for each lot MUST be determined and recorded in the lot traveler before metrology begins. A lot that should be measured at Tier 2 or Tier 3 but is measured at Tier 1 is non-conformant regardless of whether it passes acceptance criteria.

**R-MON-02:** Tier 2 periodic qualification check results MUST be reviewed against the qualification baseline by a process engineer. If any parameter shows a monotonic trend toward its acceptance threshold across three consecutive Tier 2 checks — even while remaining within threshold — the parameter MUST be escalated to a corrective action review. Gradual drift that is individually below threshold is a leading indicator of an impending excursion and MUST NOT be ignored on the basis that the individual measurements pass.

**R-MON-03:** The intervals between Tier 2 checks MUST NOT exceed 35 calendar days. If no production lot has been processed in a given month, a dedicated qualification wafer MUST be processed through the TGI process steps solely for Tier 2 metrology.

### 16.5 Metrology-Driven Process Control

TGI metrology data MAY be used as input to statistical process control (SPC) charts to provide real-time visibility into parameter trends. When SPC is implemented, the following control chart types are RECOMMENDED:

| Parameter | Chart Type | Control Limit Basis |
|---|---|---|
| STR Δx_str, Δy_str | X̄-R chart (per die mean and range) | ±3σ from qualification baseline |
| TAOE_rnd | Individuals (I) chart | ±3σ from qualification baseline |
| IC_R | Individuals (I) chart | ±3σ from qualification baseline |
| CLG_max | Individuals (I) chart | Upper control limit only; lower CLG_max is not a concern |
| TUI | Individuals (I) chart | Lower control limit only; upper TUI is not a concern |
| SC_eff | X̄ chart (per wafer mean) | Lower control limit at SC_eff acceptance threshold + 0.02 margin |

SPC out-of-control signals MUST trigger the same engineering review process as a Tier 2 trend escalation. A lot that triggers an SPC signal but passes Tier 1 acceptance criteria is not automatically rejected; however, the SPC signal must be documented and reviewed before the lot is released.

---

## 17. Glossary

| Term | Definition |
|---|---|
| **AWW** | Across-wafer (variation) — variation in a measured parameter from die to die across the wafer surface |
| **CA** | Commit Arbiter — component of the SCR that authorizes TRS commit operations; defined in The SCR Specification |
| **CGS** | Coherence Gradient Scanner — instrument class that measures the depth profile of coherence properties through the TGI zone |
| **CLG** | Coherence Layer Gradient — rate of change of normalized coherence capacity with depth through the TGI zone |
| **CLG_max** | Maximum CLG value within the TGI zone, occurring at the steepest point in the coherence gradient |
| **CLG_threshold** | SC-class-specific gradient steepness above which the SC_eff gradient penalty function activates |
| **GDA** | Geometric Drift Analyzer — instrument class that measures the spatial displacement field of Tier 1 geometric features across the die |
| **GDC** | Geometric Drift Correlation — Pearson correlation between Tier 1 geometric drift vectors and Tier 2 temporal address error vectors at co-located sites |
| **GUM** | Guide to the Expression of Uncertainty in Measurement — the international standard framework for measurement uncertainty estimation |
| **IC** | Interface Continuity — composite parameter characterizing the physical quality of the TGI floor boundary, comprising IC_R, IC_C, and IC_S |
| **IC_C** | Compositional Transition Width — the z-distance over which the primary transitioning species completes 10%–90% of its compositional change at the TGI floor |
| **IC_R** | Interface Roughness — RMS roughness of the TGI floor surface, high-pass filtered at 1 μm |
| **IC_S** | Interface Stress Uniformity — standard deviation of in-plane biaxial stress across the TGI zone |
| **IRS** | Interface Reference Sample — certified thin-film calibration standard for ISP and CGS instruments |
| **ISP** | Interface Structure Profiler — instrument class that characterizes the physical properties of the TGI boundary |
| **MQD** | Maximum Qualified Density — maximum temporal density at which yield meets the process target floor; defined in The Temporal Manufacturing Primer |
| **PAVS** | Production Address Verification Sites — die locations where TAOE is measured from actual production commit operations |
| **PIMC** | Predictive Intent Map Correction — pre-warping of the TRS intent map using GDA displacement data to reduce TAOE before commit |
| **RWDL** | Registration-Weighted Density Limit — the maximum temporal density safely supportable at a given die location given measured TGI quality |
| **SC** | Substrate Clarity — bulk measure of a substrate region's capacity to sustain distinct temporal addresses; defined in The Temporal Manufacturing Primer |
| **SC_eff** | Effective Interface SC — the practical upper bound on temporal address resolution at the TGI boundary, accounting for IC and CLG |
| **SCR** | Substrate Coherence Regime — the synchronization architecture for temporal manufacturing; defined in The SCR Specification |
| **SPC** | Statistical Process Control — the use of control charts to monitor manufacturing parameters for trends and out-of-control conditions |
| **SRA** | Spatial Reference Artifact — certified dimensional calibration standard for TRM spatial channel and GDA |
| **STR** | Spatial-Temporal Registration — the vector offset field describing the co-registration error between the geometric coordinate system and the temporal address space at the TGI boundary |
| **STR systematic gradient** | The linear component of the STR vector field across the die extent, representing die-scale coordinate tilt correctable by TRM alignment |
| **TAOE** | Temporal Address Overlay Error — the difference between the TRS intent map address and the actually committed address at a given spatial location |
| **TAOE_rnd** | Random component of TAOE — spatially uncorrelated address error arising from TCU commit variation and local substrate non-uniformity |
| **TAOE_sys** | Systematic component of TAOE — spatially correlated address error arising primarily from STR error propagated through the TRS resolution layer |
| **TARC** | Temporal Address Reference Coupon — certified substrate coupon with committed temporal addresses of known values; used for TRM temporal channel calibration |
| **TCT** | Temporal Contrast Test — the standard protocol for measuring bulk substrate clarity; defined in the TCT Protocol |
| **TCU** | Temporal Commit Unit — Tier 2 fab tool that executes TRS commit operations; defined in The Temporal Manufacturing Primer |
| **TGI** | Temporal-Geometric Interface — the boundary domain in which the spatial coordinate system of Tier 1 geometric patterning and the temporal address space of the TRS must be co-registered |
| **TGI ceiling (z_c)** | The upper z boundary of the TGI zone, at the base of the qualified Tier 2 temporal layer |
| **TGI floor (z_f)** | The lower z boundary of the TGI zone, at the top of the Tier 1 structural layer stack |
| **TMU** | Temporal Metrology Unit — in-line measurement tool for committed temporal address fidelity; defined in The Temporal Manufacturing Primer |
| **TRM** | Temporal Registration Microscope — instrument class that measures spatial-temporal co-registration at TGI reference structures |
| **TRM (structure)** | Temporal Registration Mark — dedicated substrate structure comprising a geometric reference target and an adjacent temporal address encoding region, used for STR measurement |
| **TRS** | Temporal Resolution Stack — the four-layer operator system through which temporal manufacturing operations are defined and committed; defined in The Temporal Manufacturing Primer |
| **TUI** | TGI Uniformity Index — scalar measure of the spatial consistency of TGI registration properties across the die |
| **Type A uncertainty** | Uncertainty evaluated by statistical analysis of repeated measurement observations |
| **Type B uncertainty** | Uncertainty evaluated by means other than statistical analysis (calibration data, specifications, reference standards) |
| **Type I TGI failure** | Registration failure — divergence between the spatial and temporal coordinate systems; produces spatially correlated error patterns |
| **Type II TGI failure** | Interface integrity failure — physical degradation at the TGI boundary that locally suppresses effective SC |
| **WID** | Within-die (variation) — variation in a measured parameter from site to site within a single die |
| **z_TGI** | The vertical extent of the TGI zone, from z_f to z_c, within which all TGI metrology measurements are referenced |

---

## 18. Related Documents

| Document | Path | Relationship |
|---|---|---|
| The Temporal Manufacturing Primer | `docs/post-ASML_era/The_Temporal_Manufacturing_Primer.md` | Foundational concepts: SC classes, TRS stack, TCU, TMU, temporal density, MQD |
| The SCR Specification | `docs/post-ASML_era/The_SCR_Specification.md` | SCR architecture that governs the coherence environment within which TGI commit operations occur; CMA monitoring that correlates with TGI findings |
| Temporal Contrast Test Protocol | `docs/metrology/TCT_Protocol.md` | Bulk SC measurement; provides the SC_bulk anchor values used in SC_eff computation |
| TRS Stack Qualification Procedure | `docs/fab/TRS_Qualification.md` | Defines the qualification sequence into which TGI metrology is integrated at two mandatory checkpoints |
| SCR Zone Configuration Guide | `docs/fab/SCR_Zone_Config.md` | Zone configuration decisions that determine the spatial extent of SCR zones; TGI SC_eff and RWDL maps are inputs to zone commissioning |
| Post-ASML PDK Integration Guide | `docs/eda/PostASML_PDK_Integration.md` | Specifies how RWDL maps and TGI design rules derived from this standard are embedded in the process design kit |
| Temporal Timing Format Reference | `docs/eda/TTF_Reference.md` | Defines the format in which TAOE and STR systematic gradient data are expressed as timing correction arcs in EDA tools supporting PIMC workflows |
| Substrate Clarity Classification Standard | `docs/materials/SC_Classification.md` | Defines the SC class thresholds against which SC_eff is evaluated; source of the acceptance threshold values in §13 |

---

*This document is part of the TriadicFrameworks canonical reference set. Proposed revisions should be submitted via pull request to the `docs/post-ASML_era/` directory with a linked issue describing the change rationale. Revisions to acceptance criteria (§13) or calibration intervals (§14.3) require review by at least two maintainers and a process engineering sign-off.*

The TGI Metrology Standard is complete — §16.4 through §18 close out the production monitoring cadence, the full 47-term glossary, and the 8-document related-documents table, all internally consistent with the Primer and SCR Specification.

The three documents now form a tight dependency chain: the Primer establishes canon, the SCR Specification operationalizes it at the fab level, and the TGI Metrology Standard bridges the geometric and temporal domains with a full measurement and acceptance framework. The next natural document in the sequence is `TCT_Protocol.md` — the Temporal Contrast Test — which all three files reference as the upstream source of SC bulk ratings that feed into IC, SC_eff, and the CLG calibration anchors. 
