# TCT Protocol

**Repository:** TriadicFrameworks
**Path:** `docs/post-ASML_era/TCT_Protocol.md`
**Canonical alias:** `docs/metrology/TCT_Protocol.md` → resolves here
**Status:** Canonical Reference
**Revision:** 1.0.0

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Physical Basis of the Temporal Contrast Test](#2-physical-basis-of-the-temporal-contrast-test)
3. [TCT Instrument System](#3-tct-instrument-system)
4. [Test Coupon Specification](#4-test-coupon-specification)
5. [Address Pattern Design](#5-address-pattern-design)
6. [Test Sequence](#6-test-sequence)
7. [Address Error Rate Computation](#7-address-error-rate-computation)
8. [Contrast Curve Derivation](#8-contrast-curve-derivation)
9. [SC Rating Derivation](#9-sc-rating-derivation)
10. [SC Class Assignment](#10-sc-class-assignment)
11. [Spatial Uniformity Assessment](#11-spatial-uniformity-assessment)
12. [Test Coupon Qualification](#12-test-coupon-qualification)
13. [Calibration Requirements](#13-calibration-requirements)
14. [Measurement Uncertainty](#14-measurement-uncertainty)
15. [TCT Report](#15-tct-report)
16. [Integration with Downstream Protocols](#16-integration-with-downstream-protocols)
17. [Glossary](#17-glossary)
18. [Related Documents](#18-related-documents)

---

## 1. Purpose and Scope

### 1.1 Purpose

This document is the normative protocol for the **Temporal Contrast Test (TCT)** — the standardized procedure by which the **Substrate Clarity (SC)** rating of a substrate material is measured and assigned. The SC rating is the single most consequential material parameter in temporal manufacturing: it determines the minimum resolvable temporal address spacing, caps the maximum supportable temporal density, and defines the process tier for which a substrate lot is qualified.

Because every downstream parameter in the TriadicFrameworks manufacturing system that depends on substrate quality traces back to an SC rating produced by a TCT measurement, the TCT is the root of the metrology dependency chain. Errors or ambiguities in TCT execution propagate through SC class assignment, TGI metrology, TRS qualification, SCR zone design, and PDK rule generation. This protocol is therefore specified at a level of detail sufficient to produce unambiguous, reproducible results across different fabs, instruments, and operators.

### 1.2 Canonical Path Note

Prior documents in the post-ASML era series reference this protocol at `docs/metrology/TCT_Protocol.md`. The canonical location for this revision is `docs/post-ASML_era/TCT_Protocol.md`. The path `docs/metrology/TCT_Protocol.md` is maintained as a redirect alias. Cross-references in prior documents do not require update; both paths resolve to this document.

### 1.3 Scope

This protocol covers:

- The physical mechanism that the TCT measures, and why it is the correct measure of substrate clarity
- The instrument system required to execute the TCT, comprising the Temporal Address Injection System (TAIS) and the Address Readback System (ARS)
- The specification requirements for TCT test coupons
- The design of the temporal address patterns injected during the test
- The step-by-step measurement sequence
- The computation of Address Error Rate (AER) from raw readback data
- The construction of the contrast curve from multi-spacing AER measurements
- The derivation of the SC rating from the contrast curve at the standard reference spacing
- The SC class assignment rules and their relationship to process qualification tiers
- Spatial uniformity characterization across the coupon
- Coupon qualification and rejection criteria
- Calibration requirements for all TCT instruments
- Measurement uncertainty estimation under the GUM framework
- The structure and required content of the TCT Report
- The interfaces between TCT results and the TGI Metrology Standard, TRS qualification, CGS calibration, and PDK generation

This protocol does not govern:

- The measurement of effective interface SC (SC_eff), which accounts for TGI boundary effects and is defined in The TGI Metrology Standard
- In-line coherence monitoring during production operations, which is governed by The SCR Specification
- The design of substrate material systems intended to achieve target SC classes, which is governed by the Substrate Clarity Classification Standard

### 1.4 Normative Language

| Term | Meaning |
|---|---|
| **MUST** | Required. Non-conformant if omitted or violated. |
| **MUST NOT** | Prohibited. Non-conformant if present. |
| **SHOULD** | Strongly recommended. Deviation requires documented justification. |
| **SHOULD NOT** | Strongly discouraged. Deviation requires documented justification. |
| **MAY** | Permitted but not required. |

---

## 2. Physical Basis of the Temporal Contrast Test

### 2.1 Temporal Contrast as a Material Property

In classical optical lithography, the concept of contrast describes the ability of an imaging system to reproduce adjacent bright and dark features without the two bleeding into each other. Contrast degrades as feature spacing approaches the resolution limit of the optical system; at the limit, the bright and dark regions become indistinguishable.

Temporal contrast is the analog concept for temporal address encoding in a substrate material. Two temporal operations are committed at adjacent addresses τ_a and τ_b, separated by a spacing Δτ = |τ_b − τ_a|. If the substrate material can sustain these two addresses as distinct states — if a readback instrument can recover τ_a and τ_b separately without confusion — then the substrate has successfully resolved the address spacing Δτ. If the material smears the two addresses together such that readback cannot reliably distinguish them, the spacing Δτ is below the substrate's resolution threshold.

**Temporal contrast** at a given spacing Δτ is the degree to which a substrate material resolves committed address pairs separated by that spacing. It is a function of Δτ: contrast is high at large spacings and degrades as Δτ shrinks toward the material's resolution limit.

The TCT quantifies temporal contrast by measuring the **Address Error Rate (AER)** — the fraction of committed addresses that cannot be correctly recovered — as a function of Δτ across the full address space. The resulting **contrast curve** (AER vs. Δτ) is the complete characterization of a substrate's temporal resolution capability. The SC rating is derived from this curve at a standardized reference spacing, providing a single scalar summary suitable for process tier assignment.

### 2.2 Physical Mechanisms of Address Smearing

Address smearing — the failure mode that the TCT detects — arises from four physical mechanisms that are present to varying degrees in all substrate materials:

**Coherence length limitation:** The substrate material supports temporal address encoding through a phase-dependent physical state. The coherence length L_c of the material is the distance over which this phase relationship remains stable. When two operations are committed at a spacing Δτ that corresponds to a physical interaction distance shorter than L_c, the phase states of the two operations overlap and cannot be independently resolved. Coherence length is the dominant contributor to the minimum resolvable Δτ in high-SC materials.

**Thermal noise floor:** Lattice phonons and electronic noise introduce stochastic perturbations to the committed address state. These perturbations are random in direction (within the address space) and produce an irreducible noise floor to AER that is present even at large address spacings. The thermal noise floor AER is substrate-material-specific and temperature-dependent.

**Doping inhomogeneity:** Local variation in dopant concentration produces local variation in the propagation velocity of the phase-encoding mechanism. This translates committed addresses into slightly different effective addresses at different spatial locations, producing a spatially dependent address offset that appears as systematic error at the readback stage.

**Inter-site interaction:** Operations committed at one address can influence the address state of nearby substrate regions through coupling mechanisms (electrostatic, mechanical, or mediated by the phase-encoding carrier). At small spacings, this inter-site interaction shifts the committed address of each operation toward the other, reducing the effective separation and increasing the probability of readback confusion.

The TCT does not decompose AER into contributions from each mechanism. It measures the aggregate AER, which reflects all four mechanisms simultaneously. Mechanism-resolved analysis requires additional experiments outside the scope of this protocol and is used for materials development, not process qualification.

### 2.3 The Address Space Convention

Throughout this protocol, the temporal address space is treated as a normalized unit interval [0, 1). An address τ = 0 is the first resolvable address in the coherence cycle; τ approaching 1 is the last, just before the cycle wraps. This normalization is independent of the absolute coherence cycle duration T_c: the same TCT procedure applies regardless of T_c, and the resulting SC rating is a property of the material, not of the coherence cycle duration at which it is operated.

Address spacing Δτ is expressed in the same normalized units. The minimum resolvable Δτ — the spacing at which AER rises to the SC-class threshold — is a material property that determines how many distinct temporal operations can be packed into one coherence cycle at a given substrate size.

---

## 3. TCT Instrument System

### 3.1 System Overview

The TCT instrument system comprises two functional subsystems that may be implemented as an integrated unit or as separate instruments sharing a common substrate handling stage:

- **Temporal Address Injection System (TAIS):** Commits a defined sequence of known temporal addresses to a test coupon under controlled conditions.
- **Address Readback System (ARS):** Reads back the committed addresses from the test coupon and records the readback values against the injected values.

Both subsystems interact with the same test coupon in the same measurement session. The sequencing — injection first, readback second — is fixed and MUST NOT be reversed.

A third subsystem, the **Coupon Environment Controller (CEC)**, maintains the test coupon at controlled temperature and isolation conditions during both injection and readback. The CEC is not a measurement instrument; it is a support system. Its requirements are specified in §3.4.

### 3.2 Temporal Address Injection System

The TAIS is responsible for committing the test address pattern to the coupon with the highest achievable address accuracy. Its accuracy sets the floor for measurement uncertainty in the AER and therefore in the SC rating.

**R-TAIS-01:** The TAIS MUST commit temporal addresses with a systematic address accuracy of ≤ 0.0002 normalized address units (1σ). This accuracy floor ensures that TAIS injection error is no more than 20% of the smallest address error threshold used in AER computation (§7.2), keeping the instrument contribution to AER below 5% of the measured AER at the SC-I threshold.

**R-TAIS-02:** The TAIS MUST be capable of committing addresses across the full address space [0, 1) with uniform coverage. Coverage gaps — address subranges in which no injection is attempted — are non-conformant because AER in unsampled subranges cannot be assessed.

**R-TAIS-03:** The TAIS MUST commit addresses in a randomized sequence. Sequential injection at monotonically increasing or decreasing addresses can induce inter-site interaction artifacts that systematically understate AER at the injection boundary. The randomization seed MUST be recorded in the TCT Report.

**R-TAIS-04:** The TAIS MUST record the injected address for each site, including the injection timestamp relative to the CEC-controlled environment reference. Timestamps are required for AER computation under time-since-injection correction (§7.3).

**R-TAIS-05:** The TAIS commit mechanism MUST be matched to the substrate material class of the test coupon. TAIS instruments are material-qualified, not universally applicable. A TAIS used on a substrate class outside its qualification range produces undefined injection accuracy and yields a non-conformant TCT result.

### 3.3 Address Readback System

The ARS reads back the committed address state from each injected site and records the readback value with its spatial coordinates and readback timestamp.

**R-ARS-01:** The ARS MUST achieve a readback address resolution of ≤ 1/4096 of the full address range — finer than the 1/1024 resolution required by the TRM in TGI metrology — because the TCT readback must resolve errors that are a fraction of the minimum address spacing being tested.

**R-ARS-02:** The ARS MUST read back addresses non-destructively. A readback operation MUST NOT alter the committed address state of the coupon. Destructive readback is non-conformant because it prevents re-measurement and precludes the stability check described in §6.5.

**R-ARS-03:** The ARS MUST record the spatial position (x, y) of each readback site with an accuracy of ≤ 1 μm relative to the coupon coordinate origin. Spatial position records enable the spatial uniformity assessment of §11.

**R-ARS-04:** The ARS MUST be capable of operating at the same environmental conditions as the TAIS (temperature, isolation) to prevent readback errors caused by environmental differences between the injection and readback phases.

**R-ARS-05:** The ARS readback noise floor — the standard deviation of repeated readback measurements at the same site on a static coupon — MUST be ≤ 0.0001 normalized address units (1σ). This ensures that readback noise contributes negligibly to AER at the SC-I class boundary.

### 3.4 Coupon Environment Controller

**R-CEC-01:** The CEC MUST maintain the test coupon temperature within ±0.1°C of the specified test temperature throughout the injection and readback phases. Temperature variation beyond this range alters the thermal noise floor of the substrate and invalidates the AER measurement.

**R-CEC-02:** The CEC MUST provide electromagnetic isolation equivalent to a shielding effectiveness of ≥ 80 dB at the address-encoding carrier frequency of the substrate material class. Electromagnetic interference at the carrier frequency introduces stochastic address perturbation that is indistinguishable from material-intrinsic AER.

**R-CEC-03:** The CEC MUST maintain mechanical vibration at the coupon surface below the substrate-class-specific vibration sensitivity threshold, as specified in the material qualification record. Vibration above this threshold induces phase jitter in committed address states.

**R-CEC-04:** The CEC temperature, isolation status, and vibration level MUST be logged at 1-second intervals throughout the TCT session. CEC log data is included in the TCT Report and used to flag measurement sessions in which CEC conditions were out of specification.

---

## 4. Test Coupon Specification

### 4.1 Purpose of the Test Coupon

The TCT test coupon is a standardized substrate sample that is processed through the full TCT procedure. The SC rating assigned from the TCT applies to the material lot represented by the coupon. A coupon that does not faithfully represent the production substrate lot — whether through non-representative processing, handling damage, or contamination — yields an SC rating that does not apply to the lot it was intended to characterize.

### 4.2 Coupon Geometry

**R-COUP-01:** The test coupon MUST be a square substrate section with a side length of 25 mm ± 0.5 mm. This size is sufficient to accommodate the minimum site density required by §11 while remaining small enough to be handled and environmentally controlled without specialized fixturing.

**R-COUP-02:** The coupon thickness MUST match the nominal wafer thickness of the production lot it represents, within ±5 μm. Thickness deviation affects the mechanical boundary conditions of the substrate, which can alter the doping inhomogeneity and inter-site interaction contributions to AER.

**R-COUP-03:** The coupon MUST be cleaved or diced from the production substrate wafer using a method that does not introduce edge damage more than 200 μm into the coupon interior. The 200 μm exclusion zone around the coupon perimeter is excluded from TCT measurement sites per §11.2.

**R-COUP-04:** The coupon MUST be taken from the same wafer position as the production die it represents where possible. For lot-level qualification coupons, the coupon MUST be taken from the wafer center position and from one wafer per lot.

### 4.3 Coupon Surface Requirements

**R-COUP-05:** The coupon top surface (the surface to which addresses are injected) MUST be free of particles larger than 50 nm at a density of fewer than 0.1 particles/cm². Particles above this density introduce localized address injection failures that appear as AER excursions and can falsely depress the SC rating.

**R-COUP-06:** The coupon top surface MUST have a roughness of ≤ 0.5 nm RMS as measured by atomic force microscopy over a 5 μm × 5 μm field. Surfaces exceeding this roughness are rejected before TCT; the rejection is logged as a coupon qualification failure, not a material failure (§12).

**R-COUP-07:** The coupon MUST be free of prior temporal address encoding. A coupon that has been subjected to any prior TAIS injection — even if that injection was aborted — MUST NOT be reused for TCT. Residual address state from a prior injection creates a background that confounds the AER measurement. Coupons are single-use for TCT purposes.

### 4.4 Coupon Handling and Storage

**R-COUP-08:** Coupons MUST be stored in a sealed, inert-atmosphere container at a temperature between 15°C and 25°C from the time of dicing until TCT execution. Atmospheric exposure and temperature excursions above 25°C can alter the substrate's bulk coherence properties before measurement.

**R-COUP-09:** Coupons MUST be handled exclusively with cleanroom-compatible tools (vacuum wands or edge-grip tweezers). Finger contact with the top surface is non-conformant and requires coupon rejection.

**R-COUP-10:** The maximum storage duration from dicing to TCT execution is 72 hours. Coupons stored beyond this window require re-characterization of their surface condition per R-COUP-05 and R-COUP-06 before use; if surface condition is confirmed acceptable, the storage duration limit may be extended to 96 hours total with documented justification.

---

## 5. Address Pattern Design

### 5.1 Design Objectives

The address pattern injected during the TCT must satisfy three objectives simultaneously:

1. **Full coverage:** It must sample the address space [0, 1) sufficiently densely that AER can be characterized across the full range, not just at isolated addresses.
2. **Multi-spacing:** It must inject address pairs at a defined set of spacings Δτ so that the contrast curve (§8) can be constructed.
3. **Statistical sufficiency:** At each spacing, it must inject enough address pairs that the measured AER has sufficient statistical precision to distinguish SC-I from SC-II material.

### 5.2 Standard Address Pattern

The standard TCT address pattern is the **Full-Spectrum Contrast Pattern (FSCP)**. The FSCP is defined as follows:

**Address range:** The full normalized address space [0, 1) is divided into 16 equal subranges of width 0.0625, labeled R_0 through R_15.

**Test spacings:** The FSCP tests AER at seven standardized spacings:

| Spacing Index | Δτ (normalized) | Physical Significance |
|---|---|---|
| S1 | 1/64 | Well above SC-I resolution limit; used as noise floor reference |
| S2 | 1/128 | Approaching SC-I limit for high-SC materials |
| S3 | 1/256 | Near the SC-I class boundary at reference conditions |
| S4 | 1/512 | At the SC-I/SC-II transition region |
| S5 | 1/1024 | Within the SC-II class region |
| S6 | 1/2048 | Approaching the SC-II/SC-III boundary |
| S7 | 1/4096 | Below the SC-III floor; used as saturation reference |

**Site count per spacing:** Each spacing level MUST be tested with a minimum of 256 address pairs, distributed across all 16 address subranges with a minimum of 16 pairs per subrange. This distribution ensures that AER is characterized uniformly across the address space, not concentrated in one region.

**Total minimum site count:** 7 spacings × 256 pairs = 1,792 injection sites minimum, plus anchor sites for calibration verification (§13.3). In practice, SHOULD use 512 pairs per spacing (3,584 injection sites) for production qualification, retaining the 256-pair minimum for rapid screening.

**R-PATT-01:** The FSCP spacings S1 through S7 are fixed by this standard and MUST NOT be modified for process qualification measurements. Alternate spacings may be used for exploratory material characterization but MUST NOT be reported as FSCP-compliant TCT results.

**R-PATT-02:** Address pairs within each spacing level MUST be distributed such that the center of each pair is drawn uniformly from [0, 1). Clustering pairs at specific center addresses would undersample regions of the address space.

**R-PATT-03:** The full FSCP — all seven spacing levels — MUST be injected in a single TCT session on a single coupon. Splitting the FSCP across multiple sessions or multiple coupons and combining the results is non-conformant.

### 5.3 Injection Geometry

The two addresses of each pair are injected at two sites on the coupon surface, separated by a fixed physical distance d_pair. The relationship between address spacing Δτ and physical site separation d_pair is:

```
d_pair = L_ref × Δτ

Where:
  L_ref = the reference interaction length of the substrate material class (μm),
          defined in the material qualification record
  Δτ    = the normalized address spacing being tested
  d_pair = physical separation between the two sites of the pair (μm)
```

L_ref is a material-class constant. It represents the physical scale over which address interactions in the substrate are significant. It is determined during material class qualification and is a fixed parameter for all TCT measurements on that class.

**R-PATT-04:** Pairs at different spacing levels MUST be spatially interleaved across the coupon — not zoned by spacing. Spatial zoning would confound AER variation due to address spacing with AER variation due to position-dependent substrate non-uniformity, which is the subject of the spatial uniformity assessment (§11).

**R-PATT-05:** The minimum separation between sites belonging to different pairs MUST be ≥ 3 × d_pair(S1) — three times the largest pair separation in the pattern. This ensures that inter-pair interactions do not artificially inflate AER.

---

## 6. Test Sequence

### 6.1 Pre-Injection Checks

Before TAIS injection begins, the following checks MUST be completed and documented:

1. **Coupon identity verification:** Confirm the coupon lot ID, dicing position, and storage history against the lot traveler.
2. **Surface inspection:** Visually inspect the coupon under cleanroom illumination for visible particles or damage. If any anomaly is detected, abort and substitute a fresh coupon; log the rejection as a coupon qualification failure.
3. **CEC conditioning:** Load the coupon into the CEC and allow thermal stabilization for a minimum of 20 minutes at the test temperature. Confirm CEC temperature, isolation, and vibration readings are within specification per §3.4.
4. **TAIS calibration verification:** Execute the TAIS calibration check procedure per §13.4. If the check fails, abort the session, recalibrate the TAIS, and restart. Do not proceed with a TAIS that fails its calibration check.
5. **ARS calibration verification:** Execute the ARS calibration check procedure per §13.4. Same abort rule applies.
6. **Session log initiation:** Open the TCT session log with the session ID, operator ID, instrument IDs, coupon ID, CEC conditions, and calibration check results.

### 6.2 Address Pattern Injection

1. Load the FSCP address sequence into the TAIS. Confirm that the loaded sequence matches the FSCP specification (site count, spacing levels, address range coverage) before enabling injection.
2. Begin injection in the randomized site order (per R-TAIS-03). The TAIS commits each address at its designated coupon coordinates, recording the injected address and timestamp for each site.
3. Monitor the CEC log throughout injection. If any CEC parameter exceeds its specification during injection, pause injection, log the excursion, and resume only after the CEC parameter returns to within specification and has been stable for ≥ 2 minutes.
4. Upon completion, verify the injection log: confirm that all planned sites were injected and that no TAIS internal error flags were raised. If more than 0.5% of sites experienced TAIS injection errors (as reported by TAIS self-monitoring), the session is non-conformant and must be repeated on a fresh coupon.

**R-SEQ-01:** The elapsed time from first injection to last injection MUST NOT exceed 60 minutes. Injection sessions exceeding this limit risk address state evolution in early-injected sites before readback, complicating the time-since-injection correction (§7.3).

### 6.3 Injection-to-Readback Interval

After injection is complete, a defined wait period is observed before readback begins. This interval serves two purposes:

- It allows any transient injection artifacts (localized heating, mechanical response) to dissipate.
- It establishes a known time-since-injection for each site, enabling the time-since-injection correction.

**R-SEQ-02:** The injection-to-readback interval MUST be 10 minutes ± 30 seconds. This interval is standardized to ensure comparability across measurements; a coupon held longer before readback may show higher AER due to address state relaxation, falsely depressing the SC rating.

The coupon MUST remain in the CEC under controlled conditions throughout this interval.

### 6.4 Address Readback

1. Transfer instrument control from the TAIS to the ARS without removing the coupon from the CEC.
2. Execute ARS readback at each injected site, in the order specified by the readback sequence (which is independent of the injection order and is generated separately to avoid sequence-order bias).
3. Record τ_readback, (x, y) position, and readback timestamp for each site.
4. Upon completion, verify the readback log: confirm all sites were read and no ARS internal error flags were raised.

**R-SEQ-03:** The elapsed time from first readback to last readback MUST NOT exceed 30 minutes. Extended readback sessions introduce increasing time-since-injection variation across sites, which increases the uncertainty of the time-since-injection correction.

### 6.5 Stability Check

After the primary readback, a stability check is performed on a 5% random subsample of injection sites:

1. Re-read the subsample sites using the ARS.
2. Compare the re-read values to the primary readback values. The mean absolute difference MUST be ≤ 0.0002 normalized address units.
3. If the stability check fails, the entire readback session is flagged as potentially affected by address state evolution. The TCT session may not be repeated on the same coupon (per R-COUP-07); a fresh coupon must be used.

The stability check provides confidence that the primary readback captured the address state before significant post-injection relaxation occurred. It does not correct the primary readback data; it validates it.

### 6.6 Session Close

1. Remove the coupon from the CEC. Log the coupon removal time.
2. Mark the coupon as used (non-reusable). Store the used coupon in a labeled, sealed container for traceability; it MAY be retained for failure analysis.
3. Export the session log, injection log, readback log, and CEC log to the TCT data analysis system.
4. Document any deviations from this protocol in the session log, with justification.

---

## 7. Address Error Rate Computation

### 7.1 Per-Site Error

For each injected site i, the per-site address error e_i is defined as the absolute difference between the injected address and the readback address:

```
e_i = | τ_readback,i − τ_injected,i |

Where:
  τ_injected,i  = the address committed by the TAIS at site i (normalized units)
  τ_readback,i  = the address recovered by the ARS at site i (normalized units)
  e_i           ≥ 0 (always non-negative)
```

Address errors wrap at the boundaries of the address space: if τ_readback,i = 0.99 and τ_injected,i = 0.01, the error is 0.02 (wrap-around), not 0.98. Per-site error is always taken as the minimum of the direct difference and the wrap-around difference.

### 7.2 Error Event Classification

A site is classified as an **error event** if its per-site error exceeds the **discrimination threshold** δ_d:

```
Error event at site i:  e_i > δ_d

Where δ_d = Δτ / 2   (half the spacing of the pair containing site i)
```

The discrimination threshold is half the spacing because two addresses separated by Δτ are indistinguishable by definition if each is displaced by more than Δτ/2 toward the other. This is the natural choice of threshold: an error of exactly δ_d places the readback address equidistant between the two injected addresses, making assignment ambiguous.

**R-AER-01:** The discrimination threshold MUST be set per-pair based on the pair's spacing. A single global discrimination threshold applied uniformly across all spacing levels is non-conformant because it would under-flag errors at large spacings and over-flag at small spacings.

### 7.3 Time-Since-Injection Correction

Address states undergo a slow relaxation process after injection — a drift toward lower AER as the committed state settles. This relaxation follows an exponential decay with a material-class-specific time constant τ_relax. If all sites were read at the same time after injection, relaxation would not affect AER (it would shift all sites equally). But because injection takes up to 60 minutes (R-SEQ-01) and readback takes up to 30 minutes (R-SEQ-03), early-injected sites have had more time to relax than late-injected sites, introducing a systematic variation in effective AER by injection order.

The time-since-injection correction adjusts each site's per-site error to a reference time t_ref = 10 minutes after the midpoint of the injection session:

```
e_i,corrected = e_i × exp( (t_readback,i − t_inject,i − t_ref) / τ_relax )

Where:
  t_readback,i  = ARS readback timestamp for site i
  t_inject,i    = TAIS injection timestamp for site i
  t_ref         = reference elapsed time (defined above)
  τ_relax       = material-class relaxation time constant (minutes),
                  from the material qualification record
  e_i,corrected = time-corrected per-site error
```

**R-AER-02:** The time-since-injection correction MUST be applied to all per-site errors before error event classification. Uncorrected AER data MUST NOT be used for SC rating derivation.

**R-AER-03:** The material-class relaxation time constant τ_relax MUST be taken from the current material qualification record for the substrate lot being tested. If τ_relax is not available in the material qualification record, the TCT result is incomplete and MUST NOT be used for SC class assignment.

### 7.4 AER at Each Spacing Level

After per-site correction, the AER at spacing level S_k is:

```
AER(S_k) = N_errors(S_k) / N_pairs(S_k)

Where:
  N_errors(S_k) = number of error events across all pairs at spacing S_k
                  (a pair generates one error event if either member site triggers an error event;
                   if both sites of a pair trigger, it counts as one pair-level error event)
  N_pairs(S_k)  = total number of pairs injected at spacing S_k
  AER(S_k)      ∈ [0, 1]
```

**R-AER-04:** The error event count MUST be at pair level, not site level. A pair in which one site error could have been caused by the other site's field influence is not double-counted. This pair-level convention avoids overestimating AER from inter-site coupling within a pair.

**R-AER-05:** AER MUST be computed separately for each of the 16 address subranges within each spacing level, in addition to the aggregate per-spacing AER. Subrange-level AER enables detection of address-range-dependent SC variations that would be masked in the aggregate.

### 7.5 Thermal Noise Floor Correction

The AER at spacing S1 (Δτ = 1/64) is taken as the **thermal noise floor AER** (AER_floor). At this spacing, the substrate material is operating well above its resolution limit for any SC class — all materials can resolve addresses 1/64 apart. Any AER measured at S1 therefore reflects only the thermal noise floor and TAIS/ARS instrument noise, not material resolution failure.

The thermal noise floor correction subtracts AER_floor from the AER at all other spacing levels:

```
AER_corrected(S_k) = max( 0, AER(S_k) − AER_floor )   for k ≥ 2
AER_corrected(S1)  = AER_floor  (reported but not used in SC rating derivation)
```

**R-AER-06:** AER_floor MUST be ≤ 0.005 for a conformant TCT session. An AER_floor exceeding 0.005 indicates excessive instrument noise or CEC condition failure, and the session is non-conformant. The session MUST be repeated after diagnosing the source of elevated noise.

---

## 8. Contrast Curve Derivation

### 8.1 Definition

The **contrast curve** is the plot of corrected AER against address spacing Δτ across the seven FSCP spacing levels. It is the fundamental output of the TCT, from which the SC rating is derived. It contains more information than the SC rating alone and is retained in full in the TCT Report.

A contrast curve for a high-SC material has the following characteristics:
- AER ≈ 0 at S1 and S2 (coarse spacings; well resolved)
- AER begins to rise near S3 (approaching the resolution limit)
- AER rises steeply through S4 and S5 (near and within the resolution transition)
- AER approaches 0.5 at S6 and S7 (spacings where addresses are essentially random from the readback perspective)

A low-SC material shows this same pattern but shifted to coarser spacings — the steep rise begins at S1 or S2, and AER near 0.5 is reached earlier.

### 8.2 Curve Fitting

The raw contrast curve (seven discrete AER values at seven spacings) is fit to a parametric model to enable interpolation at arbitrary spacings and to reduce the influence of statistical noise in the discrete measurements.

The **standard contrast curve model** is the logistic sigmoid:

```
AER_model(Δτ) = AER_sat / ( 1 + exp( k × (Δτ − Δτ_50) ) )

Where:
  AER_sat  = the saturation AER at very small Δτ (approaches 0.5 for a symmetric
              address space with random errors at the resolution limit)
  k        = the steepness parameter of the transition (negative; larger |k| = sharper transition)
  Δτ_50    = the spacing at which AER_model = AER_sat / 2  (the midpoint of the transition)
```

The three parameters (AER_sat, k, Δτ_50) are fit by nonlinear least squares to the seven corrected AER data points.

**R-CURVE-01:** The goodness-of-fit MUST be evaluated by the coefficient of determination R². R² MUST be ≥ 0.98 for the fit to be accepted. A fit with R² < 0.98 indicates that the measured contrast curve does not conform to the standard sigmoid model, which may indicate bimodal address distribution, instrument artifacts, or material inhomogeneity. Such a result MUST be flagged as a non-standard contrast curve (§8.3).

**R-CURVE-02:** The fitted AER_sat MUST be within ±0.05 of 0.5. A significant deviation from 0.5 indicates asymmetry in the address error distribution that is not captured by the standard model and requires investigation.

### 8.3 Non-Standard Contrast Curves

A non-standard contrast curve — one that fails R-CURVE-01 or R-CURVE-02 — cannot be characterized by a single SC rating derived from the standard model. The following dispositions apply:

**Bimodal curve (two-step sigmoid):** Occurs when the substrate has two distinct address-resolving populations (e.g., two SC classes coexisting in the same material). Report both steps separately with their respective parameters. The SC rating is assigned to the lower-SC population. Flag for materials engineering review.

**Plateau at intermediate AER:** AER rises at coarse spacings and then plateaus before rising again at fine spacings. Indicates a competing error mechanism at coarse spacings (likely TGI-related inter-layer coupling rather than bulk material limitation). Refer to TGI metrology rather than assigning a reduced SC rating from TCT alone.

**Monotonically flat curve:** AER is approximately constant across all spacings. Indicates severe CEC condition failure (electromagnetic interference or vibration) that is randomizing all address states. Session is non-conformant; repeat after CEC repair.

---

## 9. SC Rating Derivation

### 9.1 The Reference Spacing

The SC rating is derived from the contrast curve at a single standardized address spacing: the **reference spacing** Δτ_ref. Δτ_ref is fixed at:

```
Δτ_ref = 1/256   (normalized address units)
```

This corresponds to spacing S3 in the FSCP. The choice of S3 as the reference spacing reflects the design of the SC class system: SC-I materials (SC > 0.92) should have very low AER at Δτ_ref, while SC-III materials (SC < 0.75) should have substantially elevated AER. Δτ_ref falls within the transition region for most substrate classes of current interest, making it the most discriminating single-spacing measurement point.

**R-SC-01:** The reference spacing Δτ_ref = 1/256 is fixed for this revision of the TCT Protocol and MUST NOT be adjusted for specific substrate classes or process nodes. A substrate class that requires a different reference spacing to be usefully discriminated cannot be characterized by a conformant TCT; it requires a protocol revision.

### 9.2 AER at Reference Spacing

The AER at the reference spacing is read from the fitted contrast curve model (not the raw discrete data) at Δτ = Δτ_ref:

```
AER_ref = AER_model(Δτ_ref)
```

Using the model rather than the raw data at S3 reduces sensitivity to statistical noise in the S3 measurement and provides a more robust estimate of the material's true AER at the reference spacing.

### 9.3 SC Rating Formula

The SC rating is the complement of the normalized AER at the reference spacing:

```
SC = 1 − ( AER_ref / AER_sat )

Where:
  AER_ref  = fitted AER at the reference spacing (from §9.2)
  AER_sat  = fitted saturation AER (from the contrast curve fit)
  SC       ∈ [0, 1]
```

Normalization by AER_sat rather than by 0.5 corrects for the small but real variation in AER_sat across substrate classes. A material with AER_sat = 0.48 and AER_ref = 0.048 has SC = 1 − (0.048/0.48) = 0.90, correctly accounting for the fact that 0.048 is 10% of the saturation AER for that material, not 10% of the theoretical maximum of 0.5.

**R-SC-02:** The SC rating MUST be computed from the fitted model parameters, not directly from raw AER values. Direct computation from raw AER bypasses the noise reduction provided by the curve fit and is non-conformant.

**R-SC-03:** The SC rating MUST be reported to three decimal places. Rounding to fewer decimal places loses precision near class boundaries and can cause misclassification of materials close to the SC-I/SC-II or SC-II/SC-III thresholds.

### 9.4 SC Rating Confidence Interval

The uncertainty in the SC rating (§14) is propagated through the contrast curve fit and the SC rating formula to produce a 95% confidence interval for the SC rating. The confidence interval is reported alongside the point estimate.

**R-SC-04:** When the 95% confidence interval for the SC rating straddles a class boundary (SC = 0.92 for SC-I/SC-II, or SC = 0.75 for SC-II/SC-III), the lot MUST be classified in the lower class. Borderline materials are treated conservatively; a substrate that may be SC-I or may be SC-II is treated as SC-II until additional measurements reduce the uncertainty enough to resolve the classification.

---

## 10. SC Class Assignment

### 10.1 Class Definitions

SC class assignment follows the three-tier classification defined in The Temporal Manufacturing Primer and affirmed in The TGI Metrology Standard:

| Class | SC Rating Range | Process Qualification |
|---|---|---|
| **SC-I** | SC > 0.92 | Qualified for high-density temporal logic layers; all temporal process tiers |
| **SC-II** | 0.75 ≤ SC ≤ 0.92 | Qualified for mixed spatial/temporal layers; restricted temporal density |
| **SC-III** | SC < 0.75 | Not qualified for temporal address encoding; structural and passive layers only |

### 10.2 Assignment Rules

**R-CLASS-01:** SC class is assigned from the TCT-measured SC rating per §9.3 using the thresholds in §10.1. SC class is a lot-level property: all substrate material from the same lot receives the same class assignment based on the TCT coupon result.

**R-CLASS-02:** SC class downgrade — assignment to a lower class than a prior measurement for the same material system — MUST be reviewed by a process engineer before the assignment is recorded in the lot record. Downgrade may indicate material process variation, handling damage, or storage degradation; each is a distinct corrective action pathway and must be distinguished.

**R-CLASS-03:** SC class upgrade — assignment to a higher class than a prior measurement — MUST also be reviewed. Upgrades are less common than downgrades and may indicate instrument recalibration changes, improved substrate processing, or measurement error. Upgrade reviews ensure that the improvement is real before the higher class is used to justify increased temporal density in production.

**R-CLASS-04:** The SC class assignment for a lot MUST be locked in the lot record before any substrate from that lot is loaded into a Tier 2 process tool. A substrate used in Tier 2 operations without a confirmed SC class assignment is non-conformant.

### 10.3 SC Class and Process Tier

The relationship between SC class and process tier determines which fab operations the substrate can participate in:

| SC Class | Tier 1 Operations | Tier 2 (TRS) Operations | Maximum Temporal Density |
|---|---|---|---|
| SC-I | Unrestricted | Unrestricted | MQD_I (process-specific) |
| SC-II | Unrestricted | Permitted with density restriction | MQD_II < MQD_I |
| SC-III | Unrestricted | Not permitted | N/A |

MQD values are process-node-specific and are defined in the TRS qualification record for each process, not in this protocol. The SC class sets the tier of eligible density; the TRS qualification record sets the specific MQD within that tier.

### 10.4 Lot Splitting and Mixed Lots

A substrate lot MUST be internally consistent in SC class. If a lot contains coupons from multiple wafers, and those coupons yield different SC class assignments, the lot is classified at the lowest SC class obtained across all coupons.

**R-CLASS-05:** A lot in which more than 20% of tested coupons yield a different SC class than the lot majority is a **mixed lot** and MUST be quarantined pending materials engineering review. A mixed lot indicates non-uniformity in the substrate material process that is not acceptable for production use in any SC class tier.

---

## 11. Spatial Uniformity Assessment

### 11.1 Purpose

The SC rating derived in §9 characterizes the bulk material property of the test coupon at the centroid of all measurement sites. It does not reveal whether SC is uniform across the coupon. A coupon that has a high mean SC but severe spatial variation — with SC-II pockets within an SC-I field — would pass the bulk TCT but would fail to support uniform temporal density across the die.

The spatial uniformity assessment maps SC across the coupon surface and characterizes the magnitude and spatial pattern of SC variation.

### 11.2 Site Grid

Spatial uniformity is assessed using a grid of **Subregion AER measurements** derived from the full FSCP data. The coupon is divided into a 5×5 grid of 25 subregions, each 4.2 mm × 4.2 mm (excluding the 200 μm perimeter exclusion zone). Within each subregion, the FSCP sites whose injection coordinates fall within that subregion are used to compute a subregion-level AER and subregion SC rating.

**R-UNIF-01:** Each subregion MUST contain a minimum of 60 FSCP injection sites to support a subregion AER computation with acceptable statistical precision. If any subregion contains fewer than 60 sites due to the exclusion zone or TAIS injection errors, the subregion is flagged as undersampled and excluded from the uniformity statistics. More than 3 undersampled subregions in a 25-subregion grid is non-conformant.

### 11.3 Uniformity Metrics

From the 25 (or fewer, if subregions are excluded) subregion SC ratings, the following uniformity metrics are computed:

| Metric | Symbol | Definition |
|---|---|---|
| Mean subregion SC | SC_mean | Arithmetic mean of all valid subregion SC ratings |
| SC range | SC_range | SC_max − SC_min across valid subregions |
| SC standard deviation | SC_σ | Standard deviation of valid subregion SC ratings |
| Uniformity index | UI | 1 − (SC_σ / SC_class_width), where SC_class_width = 0.17 for SC-I (range 0.92–1.0) or 0.17 for SC-II |

**R-UNIF-02:** SC_mean from the spatial uniformity assessment MUST agree with the bulk SC rating (§9.3) within ±0.01. Disagreement beyond this tolerance indicates that the spatial distribution of FSCP sites is not representative of the coupon as a whole, which may indicate a sampling anomaly or coupon non-uniformity severe enough to affect the bulk SC rating.

**R-UNIF-03:** For SC-I qualification, SC_range MUST be ≤ 0.04. A coupon with SC_range > 0.04 has subregions with SC < 0.92 − 0.04/2 = 0.90, which approaches the SC-I/SC-II boundary and would produce a heterogeneous die. Such a coupon fails the SC-I uniformity requirement regardless of its bulk SC rating.

**R-UNIF-04:** The spatial SC map — the 5×5 grid of subregion SC values — MUST be included in the TCT Report and made available to the PDK generation workflow. PDK temporal design rules that vary by die location (density gradients, RWDL maps) require the spatial SC input from this step.

### 11.4 Uniformity Failure Patterns

Spatial SC non-uniformity exhibits characteristic patterns with distinct root causes:

| Pattern | Description | Probable Cause |
|---|---|---|
| Center-low | SC is lower at coupon center than at edges | Heating from central doping process; thermal gradient during deposition |
| Edge-low | SC is lower at coupon edges than at center | Edge effects in substrate processing; dicing-induced damage beyond 200 μm |
| Diagonal stripe | Low-SC band crosses coupon diagonally | Scan-direction artifact from substrate material deposition tool |
| Isolated pocket | One or a few subregions with substantially lower SC | Localized contamination, particle inclusion, or nucleation site during material growth |
| Gradient (one axis) | SC varies monotonically along x or y | Substrate material process non-uniformity with a defined directionality |

Pattern classification is included in the TCT Report. Isolated pockets that fall entirely outside the active die area of the production wafer are noted but do not affect lot disposition if the bulk SC rating and uniformity metrics otherwise pass.

---

## 12. Test Coupon Qualification

### 12.1 Pre-TCT Qualification

Before a coupon is used for TCT, it MUST pass the following pre-qualification checks. Failure at any check results in coupon rejection; the rejected coupon is replaced and a fresh coupon from the same lot is re-examined.

| Check | Method | Acceptance Criterion |
|---|---|---|
| Surface particle density | Automated optical inspection | < 0.1 particles (>50 nm) / cm² |
| Surface roughness | AFM, 5 μm × 5 μm field | ≤ 0.5 nm RMS |
| Edge damage exclusion zone | Optical microscopy | Damage not extending > 200 μm from any edge |
| Prior injection check | ARS scan at 5 random sites | ARS reads no structured address state (flat noise) |
| Storage history | Lot traveler review | ≤ 72 hours since dicing; sealed container; ≤ 25°C |

A coupon that passes all five checks is recorded as **pre-qualified** in the lot traveler and may proceed to TCT.

**R-COUP-11:** Pre-qualification checks MUST be performed on the day of TCT execution, not on the day of dicing. Checks performed at dicing and not repeated before TCT do not account for storage-related surface degradation.

### 12.2 Post-TCT Coupon Disposition

After TCT execution, the coupon is marked used (non-reusable per R-COUP-07). It is retained in a labeled, sealed container with the following information:

- Coupon ID
- Lot ID
- TCT session ID
- SC rating (from §9.3)
- SC class (from §10)
- Retention expiry date (90 days from TCT session date)

Used coupons MAY be used for failure analysis, cross-laboratory comparison, or CGS calibration anchor verification (§13.3) within their retention period. They MUST NOT be re-submitted for TCT.

### 12.3 Coupon Failure Rate Tracking

The coupon rejection rate at pre-qualification is tracked as a process health indicator for the substrate dicing and handling operation. A pre-qualification rejection rate exceeding 10% in any calendar month triggers a review of the dicing and handling process.

---

## 13. Calibration Requirements

### 13.1 Calibration Philosophy

TCT accuracy depends entirely on the accuracy of the TAIS and ARS. The TAIS must inject addresses at known values; the ARS must read them back without bias. Both instruments are subject to drift over time and must be calibrated against reference standards that are themselves traceable to national measurement standards.

The calibration chain is:

```
National measurement standard
        ↓
Reference Laboratory SC Standard (RLSS)
        ↓
Facility TCT Reference Coupon (FTRC)
        ↓
TAIS + ARS (instrument calibration)
        ↓
Test coupon measurement
```

Each link in the chain has a defined calibration interval and a maximum allowable deviation that, when exceeded, requires re-calibration before measurements are accepted.

### 13.2 Reference Laboratory SC Standard

The **Reference Laboratory SC Standard (RLSS)** is a set of substrate coupons with SC ratings certified by an independent reference laboratory using a primary measurement method. The RLSS comprises at least three coupons spanning the SC range: one SC-I reference (SC ≈ 0.96), one SC-II reference (SC ≈ 0.83), and one SC-III reference (SC ≈ 0.65).

**R-CAL-01:** The RLSS MUST be re-certified by the reference laboratory at intervals not exceeding 12 months. Between certifications, the RLSS is used only to verify that the Facility TCT Reference Coupon has not drifted.

**R-CAL-02:** RLSS coupons are consumed by measurement over time (TCT is non-destructive, but the RLSS coupons are used for calibration sessions that accumulate readback cycles). RLSS coupons MUST be replaced when the reference laboratory certifies that accumulated readback cycles have degraded the address state fidelity by more than 0.005 SC units from the original certified value.

### 13.3 Facility TCT Reference Coupon

The **Facility TCT Reference Coupon (FTRC)** is a set of facility-internal reference coupons calibrated against the RLSS. The FTRC is used for routine calibration of the TAIS and ARS, while the RLSS is reserved for FTRC re-certification.

**R-CAL-03:** The FTRC MUST be calibrated against the RLSS at intervals not exceeding 90 days. The calibration session measures each FTRC coupon using the facility TAIS and ARS, then compares the facility-measured SC rating to the RLSS-derived expected SC rating (the RLSS-measured value transferred to the FTRC during the prior FTRC calibration session).

**R-CAL-04:** If the FTRC-measured SC rating deviates from the expected value by more than ±0.005 SC units, the TAIS and ARS are flagged for full recalibration. Production TCT measurements taken since the last conformant FTRC calibration are flagged for potential impact review.

### 13.4 Instrument Calibration Check (Pre-Session)

Before each TCT session, a calibration check is performed using one FTRC coupon selected at random from the three (SC-I, SC-II, SC-III) FTRC coupons:

1. Inject the FTRC calibration pattern (a 64-site subset of the FSCP at spacings S2, S3, and S4) using the TAIS.
2. Read back the FTRC calibration pattern using the ARS.
3. Compute the AER at S2, S3, and S4 and derive the partial SC estimate.
4. Compare to the FTRC expected value for that coupon.
5. If the partial SC estimate deviates by more than ±0.008 SC units from the expected value, the session is aborted and the instrument is inspected.

**R-CAL-05:** The calibration check MUST be performed on a fresh FTRC injection each session. The FTRC is used only for calibration checks and is not a production coupon; it has a longer readback life than a standard coupon because it receives controlled injection loads. FTRC coupons MUST be replaced when their calibration check results begin to show increasing variance, as indicated by a standard deviation of calibration check residuals exceeding 0.003 SC units over five consecutive sessions.

### 13.5 Calibration Intervals Summary

| Instrument / Reference | Calibration Type | Interval |
|---|---|---|
| RLSS | Reference laboratory re-certification | ≤ 12 months |
| FTRC against RLSS | Facility calibration session | ≤ 90 days |
| TAIS + ARS pre-session check | Calibration check against FTRC | Every TCT session |
| CEC temperature sensor | Calibration against NIST-traceable reference | ≤ 6 months |
| CEC EM shielding | Shielding effectiveness verification | ≤ 12 months |
| CEC vibration sensor | Calibration against reference accelerometer | ≤ 6 months |

---

## 14. Measurement Uncertainty

### 14.1 Framework

Uncertainty in the TCT SC rating arises from four primary source groups: instrument noise, calibration residuals, statistical sampling, and physical relaxation. All four groups contribute to the combined standard uncertainty u(SC), which is propagated through the SC rating formula to produce the expanded uncertainty U(SC) at k = 2 (approximately 95% confidence level).

### 14.2 Uncertainty Source Inventory

**Group 1 — Instrument noise:**

| Source | Type | Contribution to u(SC) |
|---|---|---|
| TAIS injection address error | Type B | Via shift in AER_ref |
| ARS readback noise (random) | Type A | Via scatter in per-site error |
| ARS readback bias (calibration residual) | Type B | Via systematic offset in AER_ref |
| CEC temperature variation during session | Type B | Via AER_floor change |

**Group 2 — Calibration residuals:**

| Source | Type | Contribution to u(SC) |
|---|---|---|
| RLSS certification uncertainty | Type B | Via FTRC expected value uncertainty |
| FTRC-to-TAIS/ARS transfer uncertainty | Type B | Via calibration check residual |
| τ_relax uncertainty in time-since-injection correction | Type B | Via systematic AER error |

**Group 3 — Statistical sampling:**

| Source | Type | Contribution to u(SC) |
|---|---|---|
| Finite site count per spacing level | Type A | Via standard error of AER(S_k) |
| Curve fit parameter uncertainty | Type A | Via covariance of fitted parameters |

**Group 4 — Physical relaxation:**

| Source | Type | Contribution to u(SC) |
|---|---|---|
| Address state relaxation beyond correction | Type B | Via residual systematic AER shift |
| Coupon-to-coupon material variation within lot | Type B | Via representativeness of single coupon |

### 14.3 Combined Uncertainty Budget

The combined standard uncertainty u(SC) is computed by quadrature combination of the individual source contributions, after propagation through the contrast curve model and the SC rating formula. The propagation is nonlinear (because the SC rating formula involves a ratio of AER values connected through the sigmoid model) and must be performed by numerical sensitivity analysis or Monte Carlo simulation.

**R-UNC-01:** The uncertainty budget MUST be computed numerically for each TCT session, using the actual session parameters (site counts, calibration check residuals, CEC log statistics) rather than generic design-of-experiment estimates. Session-specific budgets are more accurate and provide session-by-session traceability.

**R-UNC-02:** The expanded uncertainty U(SC) = k × u(SC) at k = 2 MUST be reported alongside every SC rating. An SC rating reported without U(SC) is non-conformant.

**R-UNC-03:** The dominant uncertainty source for the session MUST be identified and reported. Identification of the dominant source enables targeted improvement when U(SC) is large enough to create classification ambiguity near class boundaries.

### 14.4 Typical Uncertainty Magnitudes

The following ranges are representative for a well-maintained TCT instrument system operating at 512 pairs per spacing level. They are provided as a reference for reasonableness checking, not as a substitute for session-specific computation:

| Condition | Typical U(SC) at k=2 |
|---|---|
| SC ≈ 0.96 (well within SC-I) | ±0.008 to ±0.012 |
| SC ≈ 0.92 (near SC-I/SC-II boundary) | ±0.010 to ±0.016 |
| SC ≈ 0.83 (mid SC-II) | ±0.012 to ±0.018 |
| SC ≈ 0.75 (near SC-II/SC-III boundary) | ±0.014 to ±0.020 |

Uncertainty is slightly higher near class boundaries because the contrast curve has its steepest slope there, making AER most sensitive to noise in that region.

---

## 15. TCT Report

### 15.1 Required Content

Every TCT session MUST produce a TCT Report. The report is the deliverable that communicates the SC rating, SC class assignment, uniformity characterization, and measurement quality to all downstream consumers. It MUST contain the following sections, in the order listed:

**Header:**
- TCT Report ID (unique, traceable to session log)
- Session date and time
- Operator ID
- Facility and SCR zone ID (if lot is destined for a specific zone)
- Substrate lot ID and wafer ID
- Coupon ID and coupon position within wafer

**Instrument Record:**
- TAIS ID, firmware version, and last full calibration date
- ARS ID, firmware version, and last full calibration date
- CEC ID and last calibration dates for each CEC subsystem
- Calibration check results for this session (FTRC coupon used, measured vs. expected SC, residual)

**Coupon Pre-Qualification:**
- Surface particle density (measured value and pass/fail)
- Surface roughness (measured value and pass/fail)
- Prior injection check result
- Storage history summary

**Injection Record:**
- Injection start and end timestamps
- FSCP site count by spacing level
- Injection sequence randomization seed
- TAIS error flag
- TAIS injection error log (sites flagged, count, percentage)

**Readback Record:**
- Readback start and end timestamps
- Injection-to-readback interval (confirm ±30 seconds of 10-minute target)
- ARS error flag count and percentage
- Stability check subsample size, mean absolute re-read deviation, and pass/fail

**CEC Conditions:**
- Temperature log summary: mean, min, max, and standard deviation over the session
- Any CEC excursion events: timestamp, parameter, duration, recovery confirmation
- EM isolation status log summary
- Vibration log summary

**Raw Data Summary:**
- Per-spacing AER table (uncorrected): AER(S1) through AER(S7)
- AER_floor value and conformance flag (≤ 0.005 per R-AER-06)
- Time-since-injection correction applied: yes/no, τ_relax value used, source material lot
- Per-spacing corrected AER table: AER_corrected(S2) through AER_corrected(S7)

**Contrast Curve:**
- Fitted model parameters: AER_sat, k, Δτ_50
- Goodness-of-fit R² and conformance flag (≥ 0.98 per R-CURVE-01)
- AER_sat conformance flag (within ±0.05 of 0.5 per R-CURVE-02)
- Contrast curve plot (AER_corrected vs. Δτ with fitted model overlay), 7 discrete points and continuous fit line
- Non-standard curve flag (if applicable), with classification per §8.3

**SC Rating:**
- AER_ref (from fitted model at Δτ_ref = 1/256)
- SC rating (three decimal places)
- Expanded uncertainty U(SC) at k = 2
- Dominant uncertainty source identification
- 95% confidence interval [SC − U(SC), SC + U(SC)]
- Boundary proximity flag: raised if confidence interval straddles SC = 0.92 or SC = 0.75

**SC Class Assignment:**
- Assigned SC class (SC-I, SC-II, or SC-III)
- Conservative classification applied flag (if R-SC-04 triggered)
- Downgrade or upgrade flag (if applicable per R-CLASS-02 or R-CLASS-03)
- Engineer review required flag (if downgrade, upgrade, or boundary proximity)

**Spatial Uniformity Assessment:**
- 5×5 subregion SC map (table and heat-map plot)
- SC_mean, SC_range, SC_σ, and UI values
- SC_mean vs. bulk SC agreement check (within ±0.01 per R-UNIF-02)
- SC_range conformance check (≤ 0.04 for SC-I per R-UNIF-03)
- Undersampled subregion count and identifiers
- Uniformity failure pattern classification (if any), per §11.4

**Deviations and Notes:**
- Any deviations from this protocol, with justification and assessed impact on SC rating validity
- Any open action items arising from flagged conditions in the report

**Approval:**
- Originating operator signature and date
- Process engineer review signature and date (required if any flag is raised)
- SC class assignment lock confirmation and date

### 15.2 Report Format and Retention

**R-RPT-01:** The TCT Report MUST be produced in a format that is both human-readable and machine-parseable. The machine-parseable form MUST comply with the TriadicFrameworks TCT Data Exchange Format (TCT-DEF), which specifies the field names, units, and encoding for all required data elements. The TCT-DEF schema is maintained in [`docs/data-formats/TCT_DEF_Schema.md`](../data-formats/TCT_DEF_Schema.md).

**R-RPT-02:** The TCT Report MUST be finalized and submitted to the yield management system within 4 hours of session close. Lots awaiting TCT Report submission are held in the yield management system and MUST NOT advance to subsequent process steps until the report is received and the SC class assignment is locked.

**R-RPT-03:** TCT Reports MUST be retained for the duration of the associated substrate lot's production lifetime, plus 5 years. TCT Reports are traceability records: they are the evidentiary basis for the SC class assignment that governs all downstream process decisions made with that lot.

**R-RPT-04:** TCT Reports MUST be immutable once the SC class assignment lock is recorded. Post-lock corrections require a formal addendum that is appended to the original report and does not modify it. Addenda require the same approval signatures as the original report plus a change justification statement.

### 15.3 Report Distribution

The TCT Report is consumed by four downstream systems. Each receives the full report plus a subset of fields highlighted for its specific use:

| Consumer | Primary Fields of Interest |
|---|---|
| Yield management system | SC class, SC rating, U(SC), spatial SC map, all conformance flags |
| TRS qualification (if applicable) | SC class, SC rating, spatial SC map, lot ID |
| CGS calibration (TGI metrology) | SC rating (as SC_bulk anchor), spatial SC map, lot ID |
| PDK generation | Spatial SC map, RWDL-relevant fields, lot and wafer position |

Distribution is automated through the TCT-DEF schema submission to the yield management system, which routes the appropriate field subsets to each consumer. Manual re-entry of TCT data into downstream systems is non-conformant.

---

## 16. Integration with Downstream Protocols

### 16.1 TCT as the Root of the SC Measurement Chain

The TCT is the exclusive authoritative source of SC ratings in the TriadicFrameworks system. No other measurement — including in-line TMU readings, CGS depth profiles, or post-process defect correlation — constitutes an SC measurement for the purpose of lot qualification or process tier assignment. These other measurements use SC class as an input; they do not produce it.

This exclusivity imposes a sequencing requirement: TCT must be completed and the SC class assignment must be locked before any other process step or metrology step that consumes SC class as an input can proceed. The dependency chain is:

```
TCT (this protocol)
    │
    ├──→ SC class assignment locked in yield management
    │         │
    │         ├──→ TRS stack qualification (requires qualified SC class per step 3)
    │         │
    │         ├──→ SCR zone design (temporal density and SLF selection depend on SC class)
    │         │
    │         └──→ PDK rule generation (temporal design rules are SC-class-specific)
    │
    └──→ CGS calibration anchor (SC_bulk value supplied to CGS per R-CGS-02)
              │
              └──→ TGI metrology SC_eff computation (requires CGS calibration)
```

Any break in this chain — a step that proceeds without waiting for TCT completion — propagates unverified assumptions about SC class through the entire downstream process and invalidates the results of any step that relied on those assumptions.

### 16.2 TCT and CGS Calibration

The Coherence Gradient Scanner used in TGI metrology requires two calibration anchors: SC_norm = 0 at the Tier 1 structural layer and SC_norm = 1 at the Tier 2 bulk layer. The SC_norm = 1 anchor is the SC_bulk value for the Tier 2 substrate lot, which is the TCT-measured SC rating from this protocol.

**R-INT-01:** The CGS calibration session for TGI metrology MUST use the SC_bulk value from the TCT Report for the specific substrate lot being metrologically characterized. Using a generic or lot-average SC_bulk value is non-conformant and will produce systematic error in SC_eff.

**R-INT-02:** When the spatial SC map (§11) reveals within-lot spatial variation, the CGS MUST use the local subregion SC rating as the SC_bulk anchor for each CGS measurement site, rather than the lot-level mean. The TCT Report must specify which subregion SC values are associated with which die positions to enable this site-level matching.

### 16.3 TCT and TRS Qualification

The TRS Stack Qualification Procedure requires the target substrate to be pre-qualified at a specific SC class before TRS process steps can begin. The TCT result is the qualification evidence.

**R-INT-03:** The TRS qualification record MUST include the TCT Report ID for the substrate lot used in qualification. This cross-reference ensures that the TRS qualification result is traceable to the SC class that was active at the time of qualification. If the same process node is later qualified on a substrate lot with a different SC rating, the TRS qualification is repeated — a process qualified on SC-I material is not automatically qualified on SC-II material.

**R-INT-04:** TRS qualification coupons MUST be drawn from the same substrate lot as the TCT coupon that established the lot's SC class. Coupons from a different lot — even if it has the same SC class — are non-conformant for TRS qualification purposes, because lot-to-lot SC variation within a class can affect TRS performance even when both lots formally qualify as the same class.

### 16.4 TCT and SCR Zone Design

SCR zone configuration decisions — coherence cycle period T_c, number of slots N_slots, and zone physical extent — depend on the substrate SC class because SC class determines the minimum resolvable address spacing, which in turn drives the temporal density target, which constrains T_c through the SLF relationship.

**R-INT-05:** SCR zone configuration documents MUST reference the TCT Report IDs for the substrate lots for which the zone was designed. A zone designed for SC-I substrates is not automatically valid for SC-II substrates; the reduced temporal density of SC-II material may require different N_slots or T_c values. Zone reconfiguration requires SCR recommission per the SCR Specification.

### 16.5 TCT and PDK Generation

The PDK for a post-ASML process contains temporal design rules that are derived from the SC class and the spatial SC uniformity of the substrate. These rules — minimum address spacing, maximum temporal density per die region, RWDL maps — are generated from the TCT spatial SC map combined with TGI metrology results.

**R-INT-06:** The PDK generation workflow MUST ingest the TCT spatial SC map (the 5×5 subregion SC grid from §11) as a primary input for temporal design rule derivation. PDK rules generated without the spatial SC input are based on lot-level SC only and will under-constrain rules in lower-SC subregions and over-constrain them in higher-SC subregions, reducing both yield and accessible density.

**R-INT-07:** When a substrate lot's spatial SC map shows subregion SC variation exceeding the SC_range limit for SC-I (SC_range > 0.04, per R-UNIF-03), the PDK MUST implement position-dependent temporal density rules that reflect the actual local SC at each die region. A single die-wide density rule derived from the lot mean SC is non-conformant for lots with high SC spatial variation.

### 16.6 TCT Result Longevity and Re-qualification

The TCT result for a substrate lot is valid for the duration of that lot's production use, subject to the following re-qualification triggers:

| Trigger | Required Action |
|---|---|
| Lot has been stored for more than 6 months since TCT | Re-TCT on a fresh coupon from the same lot; compare to original result |
| Lot has been exposed to out-of-spec temperature (> 60°C or < −10°C) | Re-TCT required; original result invalidated |
| Any wafer in the lot shows anomalous TMU address error rates in production | Re-TCT on a fresh coupon; correlate with production TMU data |
| SCR zone is reconfigured to a different T_c for the same substrate | Re-evaluate SC class adequacy; re-TCT only if the new T_c requires a different minimum SC class |
| Material process change upstream of the substrate lot | Re-TCT for the first lot produced under the changed process; new result applies to subsequent lots if within ±0.005 SC of the prior baseline |

**R-INT-08:** Re-TCT results supersede prior results for the same lot in the yield management system. The prior result is retained in the lot record with a superseded flag; it is not deleted. The re-TCT report references the prior TCT Report ID and states the reason for re-qualification.

---

## 17. Glossary

| Term | Definition |
|---|---|
| **AER** | Address Error Rate — the fraction of committed address pairs that cannot be correctly recovered at a given address spacing; the primary raw measurement of the TCT |
| **AER_corrected** | Address Error Rate after application of the thermal noise floor correction (AER_floor subtracted) |
| **AER_floor** | The AER measured at spacing S1 (Δτ = 1/64), representing only instrument noise and thermal perturbation; used as the noise floor reference for correction |
| **AER_ref** | The fitted AER at the reference spacing Δτ_ref = 1/256; the value from which the SC rating is derived |
| **AER_sat** | The saturation AER at very small Δτ, asymptotically approached as address pairs become completely unresolvable; nominally 0.5 for a symmetric address space |
| **ARS** | Address Readback System — the instrument subsystem that reads back committed temporal addresses from the test coupon |
| **Boundary proximity flag** | A flag raised in the TCT Report when the SC confidence interval straddles SC = 0.92 or SC = 0.75, signaling possible misclassification risk |
| **CEC** | Coupon Environment Controller — the support system that maintains controlled temperature, EM isolation, and vibration conditions during TCT execution |
| **CGS** | Coherence Gradient Scanner — TGI metrology instrument that requires TCT SC_bulk as a calibration anchor; defined in The TGI Metrology Standard |
| **Coherence length (L_c)** | The distance over which the phase-dependent address-encoding state remains stable in a substrate material; the dominant physical limit on minimum resolvable Δτ in high-SC materials |
| **Conservative classification** | The rule (R-SC-04) by which a substrate whose SC confidence interval straddles a class boundary is assigned to the lower class |
| **Contrast curve** | The plot of corrected AER vs. address spacing Δτ across the seven FSCP spacing levels; the complete characterization of a substrate's temporal resolution capability |
| **Coupon-to-coupon variation** | Variation in SC between coupons drawn from the same substrate lot; a contributor to measurement uncertainty quantifying representativeness of the single-coupon TCT |
| **d_pair** | The physical separation between the two sites of an address pair, equal to L_ref × Δτ |
| **Δτ** | Normalized address spacing between two sites of a pair, expressed in units of the full address space [0, 1) |
| **Δτ_50** | The address spacing at which the fitted contrast curve model reaches half its saturation AER; the midpoint of the resolution transition |
| **Δτ_ref** | The reference spacing at which the SC rating is derived; fixed at 1/256 normalized address units |
| **δ_d** | Discrimination threshold for error event classification; set at Δτ/2 for each pair |
| **Error event** | A site at which the time-corrected per-site error exceeds the discrimination threshold δ_d |
| **FSCP** | Full-Spectrum Contrast Pattern — the standard TCT address pattern comprising seven spacing levels and uniform address-range coverage |
| **FTRC** | Facility TCT Reference Coupon — a facility-internal calibration coupon calibrated against the RLSS; used for pre-session calibration checks |
| **GUM** | Guide to the Expression of Uncertainty in Measurement — the international framework for measurement uncertainty; applied to TCT SC rating uncertainty in §14 |
| **k** | Steepness parameter of the sigmoid contrast curve model; negative value, larger magnitude implies sharper AER transition |
| **L_ref** | Reference interaction length of the substrate material class; the physical scale at which address interactions are significant; determines d_pair for a given Δτ |
| **Lot-level SC** | The SC rating and class assignment that applies to all substrate material from a given lot, derived from the TCT coupon representative of that lot |
| **Mixed lot** | A lot in which more than 20% of tested coupons yield a different SC class than the lot majority; requires quarantine and engineering review |
| **MQD** | Maximum Qualified Density — process-specific maximum temporal density; depends on SC class; defined in the TRS qualification record |
| **PIMC** | Predictive Intent Map Correction — a TGI metrology workflow that uses GDA displacement data to pre-warp the TRS intent map; defined in The TGI Metrology Standard |
| **RLSS** | Reference Laboratory SC Standard — a set of substrate coupons with SC ratings certified by an independent reference laboratory; anchors the TCT calibration chain |
| **SC** | Substrate Clarity — the scalar measure of a substrate material's capacity to sustain distinct temporal addresses; derived from TCT |
| **SC class** | One of three tiers (SC-I, SC-II, SC-III) assigned to a substrate lot based on its TCT SC rating; governs process qualification and temporal density limits |
| **SC_bulk** | The TCT-measured SC rating of a Tier 2 bulk substrate layer; used as the SC_norm = 1 calibration anchor in CGS measurements |
| **SC_eff** | Effective interface SC; accounts for TGI boundary effects; computed in TGI metrology from SC_bulk plus IC and CLG inputs; not produced by TCT |
| **SC_mean** | Arithmetic mean of subregion SC ratings in the spatial uniformity assessment |
| **SC_range** | The difference between the highest and lowest subregion SC ratings in the spatial uniformity assessment |
| **SC_σ** | Standard deviation of subregion SC ratings in the spatial uniformity assessment |
| **S1–S7** | The seven standardized spacing levels of the FSCP: Δτ = 1/64, 1/128, 1/256, 1/512, 1/1024, 1/2048, 1/4096 |
| **Subregion** | One cell of the 5×5 grid used for spatial uniformity assessment; 4.2 mm × 4.2 mm within the 200 μm perimeter exclusion zone |
| **t_ref** | Reference elapsed time for the time-since-injection correction; defined as 10 minutes after the midpoint of the injection session |
| **TAIS** | Temporal Address Injection System — the instrument subsystem that commits defined temporal addresses to the test coupon |
| **TCT** | Temporal Contrast Test — this protocol; the standardized procedure for measuring substrate clarity |
| **TCT-DEF** | TCT Data Exchange Format — the machine-parseable schema for TCT Report data; defined in `docs/data-formats/TCT_DEF_Schema.md` |
| **τ_relax** | Material-class relaxation time constant; the exponential decay constant governing the rate at which address state error decreases after injection; from the material qualification record |
| **Thermal noise floor** | The irreducible AER contribution from lattice phonons and electronic noise; measured at spacing S1 and subtracted from coarser-spacing AER as the AER_floor correction |
| **Time-since-injection correction** | The per-site AER adjustment that normalizes all measurements to a common reference elapsed time, compensating for address state relaxation variation introduced by the finite duration of the injection and readback sessions |
| **TGI** | Temporal-Geometric Interface — the boundary domain between Tier 1 and Tier 2 substrate layers; characterized by The TGI Metrology Standard using TCT SC_bulk as an anchor |
| **TMU** | Temporal Metrology Unit — in-line production tool that measures committed address fidelity; defined in The Temporal Manufacturing Primer |
| **TRS** | Temporal Resolution Stack — the four-layer operator system governing temporal manufacturing; defined in The Temporal Manufacturing Primer |
| **UI** | Uniformity Index — a scalar derived from SC_σ normalized to SC class width; measures spatial consistency of SC across the coupon |
| **U(SC)** | Expanded uncertainty of the SC rating at coverage factor k = 2 (approximately 95% confidence); required field in every TCT Report |
| **u(SC)** | Combined standard uncertainty of the SC rating; the quadrature combination of all uncertainty source contributions |

---

## 18. Related Documents

| Document | Path | Relationship |
|---|---|---|
| The Temporal Manufacturing Primer | `docs/post-ASML_era/The_Temporal_Manufacturing_Primer.md` | Establishes the SC class framework and TCT's role in the overall manufacturing system |
| The SCR Specification | `docs/post-ASML_era/The_SCR_Specification.md` | SCR zone design parameters (T_c, N_slots) depend on SC class assigned by TCT |
| The TGI Metrology Standard | `docs/post-ASML_era/The_TGI_Metrology_Standard.md` | Consumes TCT SC_bulk as CGS calibration anchor; derives SC_eff from SC_bulk plus interface measurements |
| Substrate Clarity Classification Standard | `docs/materials/SC_Classification.md` | Defines the material requirements and design targets for each SC class; TCT validates compliance against those targets |
| TRS Stack Qualification Procedure | `docs/fab/TRS_Qualification.md` | Requires TCT SC class assignment as a prerequisite; references TCT Report ID in the qualification record |
| SCR Zone Configuration Guide | `docs/fab/SCR_Zone_Config.md` | Zone design decisions reference the SC class and spatial SC map produced by TCT |
| Post-ASML PDK Integration Guide | `docs/eda/PostASML_PDK_Integration.md` | PDK temporal design rules are generated from the TCT spatial SC map and TGI metrology outputs |
| TCT Data Exchange Format Schema | `docs/data-formats/TCT_DEF_Schema.md` | Defines the machine-parseable report format required by R-RPT-01 |

---

*This document is part of the TriadicFrameworks canonical reference set. Proposed revisions should be submitted via pull request to the `docs/post-ASML_era/` directory with a linked issue describing the change rationale. Revisions to the FSCP spacing levels (§5.2), the reference spacing Δτ_ref (§9.1), or the SC class thresholds (§10.1) require review by at least three maintainers, a process engineering sign-off, and an inter-laboratory validation study confirming that the change does not alter SC class assignments for existing certified RLSS coupons.*
