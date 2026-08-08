---
Repository:    TriadicFrameworks
Path:          docs/post-ASML_era/The_Multi-Regime_Semiconductor_Model.md
Status:        INFORMATIVE
Revision:      0.9.0 (draft)
---

# The Multi-Regime Semiconductor Model

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Regime Definitions](#2-regime-definitions)
3. [The Classical Carrier Regime (CCR)](#3-the-classical-carrier-regime-ccr)
4. [The Coherent Phase Regime (CPR)](#4-the-coherent-phase-regime-cpr)
5. [The Transitional Regime (TR)](#5-the-transitional-regime-tr)
6. [Material Parameters and Model Inputs](#6-material-parameters-and-model-inputs)
7. [Regime Boundary Conditions](#7-regime-boundary-conditions)
8. [Derivation of Observable Parameters](#8-derivation-of-observable-parameters)
9. [SC Class as a Regime Indicator](#9-sc-class-as-a-regime-indicator)
10. [Multi-Regime Interactions and Failure Modes](#10-multi-regime-interactions-and-failure-modes)
11. [Process Effects on Regime Structure](#11-process-effects-on-regime-structure)
12. [Model Validation and Calibration](#12-model-validation-and-calibration)
13. [Design Implications](#13-design-implications)
14. [Glossary](#14-glossary)
15. [Related Documents](#15-related-documents)

---

## 1. Purpose and Scope

### 1.1 Document Role

This document establishes the physical theory underlying temporal manufacturing. The prior documents
in the post-ASML era series — the Temporal Manufacturing Primer, the SCR Specification, the TGI
Metrology Standard, the TCT Protocol, the TRS-Aware PDK Specification, and the Logic Folding
Architecture Guide — treat empirical material parameters (Substrate Clarity SC, coherence length L_c,
relaxation time τ_relax, coherence layer gradient CLG, and associated derived quantities) as externally
measured inputs. This document defines the physical model from which those parameters arise.

The Multi-Regime Semiconductor Model (MRSM) provides:

- A conceptual and mathematical account of the three coexisting electronic regimes present in
  post-ASML substrates.
- Derivations connecting regime-level physics to each observable parameter used in the series.
- Physical explanations for inter-regime coupling, noise sources, and temporal address encoding.
- A framework for predicting how process variations and operating conditions perturb measured
  quantities.
- Validation criteria that allow experimental confirmation of model predictions.

This document is **informative**, not normative. It does not impose requirements on equipment, process,
or design. Normative requirements appear in the documents listed in Section 15. Where this document
makes claims about specific numerical values, those values are representative of the regime taxonomy
and are not mandatory limits.

### 1.2 Scope

The MRSM applies to:

- Post-ASML substrate materials classified as SC-I, SC-II, or SC-III under the TCT Protocol.
- The full z-extent of the substrate stack from Tier 1 (structural) through Tier 2 (temporal) layers.
- The TGI transition zone connecting these two tiers.
- Multi-zone SCR architectures where regime behavior must remain consistent across zone boundaries.

The MRSM does not extend to:

- Carrier transport in Tier 1 interconnect layers above the structural base (governed by classical
  electromigration and RC models).
- Packaging-level electromechanical interfaces.
- Equipment-level physics (TCU injection mechanisms, ARS readback transduction).

### 1.3 Relationship to Prior Documents

The MRSM sits beneath all six prior documents in the causal hierarchy. Every empirical parameter that
appears in normative documents is a projection of the regime model onto a measurement instrument's
observables. The relationship is summarized as follows:

```
MRSM (physical model)
  └─ TCT Protocol        → measures SC, AER(Δτ), τ_relax, L_c
       └─ TGI Metrology  → measures CLG, IC, SC_eff, TAOE
            └─ PDK Spec  → derives Δτ_eff, Δτ_xtalk, SCLM, TDR rules
                 └─ Logic Folding  → consumes TSH, L_c, Δτ_eff, T_c
                      └─ SCR Spec  → uses T_c, SLF, zone sizing
```

Understanding this hierarchy is not required for production use of any individual document. It is,
however, essential for process development, material qualification, and fault analysis that require
connecting measurement anomalies to physical root causes.

---

## 2. Regime Definitions

### 2.1 Overview

Post-ASML substrates exhibit three distinct electronic regimes that can coexist simultaneously within
a single die. The regimes are distinguished by the dominant mechanism governing the electronic state
of the material at a given depth z and temperature T.

| Regime | Symbol | Dominant Mechanism | Temporal Encoding | Primary Layer |
|--------|--------|--------------------|-------------------|---------------|
| Classical Carrier Regime | CCR | Band-conduction charge transport | Not supported | Tier 1 structural |
| Coherent Phase Regime | CPR | Collective phase-coherent electronic order | Supported | Tier 2 temporal |
| Transitional Regime | TR | Concurrent CCR and CPR activity | Partial / degraded | TGI zone |

The three regimes are not discrete material phases in the thermodynamic sense. They are operational
regimes: functional states of the electronic system under the boundary conditions imposed by the
substrate stack structure, the applied process history, and the operating temperature and clock cycle.

### 2.2 Regime Assignment

Regime assignment is a local property at position (x, y, z). For a given point:

- z < z_f (below the TGI floor): CCR dominant. CPR order parameter ψ(z) ≈ 0.
- z_f ≤ z ≤ z_c (within the TGI zone): TR active. ψ(z) interpolates continuously between 0 and
  ψ_bulk.
- z > z_c (above the TGI ceiling, within Tier 2): CPR dominant. ψ(z) ≈ ψ_bulk.

The boundaries z_f and z_c are the TGI floor and ceiling as defined in the TGI Metrology Standard.
These boundaries are not sharp in the crystallographic sense; they are defined operationally as the
depths at which the normalized phase order parameter crosses 0.05 and 0.95 respectively.

### 2.3 Regime Co-Presence in Device Operation

In a functioning post-ASML device, all three regimes are simultaneously active:

- CCR governs signal routing, power delivery, and Tier 1 structural functions.
- TR (at the TGI) mediates the transfer of spatial patterning information into temporal address space
  during fabrication, and couples the two functional domains during operation.
- CPR in the Tier 2 bulk is the medium in which temporal addresses are committed, held, and read back.

A failure in any regime, or at any regime interface, propagates across all three. The MRSM provides
the theoretical basis for diagnosing such failures by correlating observable anomalies with
regime-level physical mechanisms.

---

## 3. The Classical Carrier Regime (CCR)

### 3.1 Physical Mechanism

In the CCR, the electronic state of the material is governed by band-structure charge transport.
Mobile carriers — electrons in the conduction band and holes in the valence band — respond to local
electric fields and chemical potential gradients according to the drift-diffusion equation:

```
J = q(n μ_e + p μ_h) E + q(D_e ∇n − D_h ∇p)
```

where:
- J   = carrier current density [A m⁻²]
- q   = elementary charge
- n,p = electron and hole carrier densities [m⁻³]
- μ_e, μ_h = electron and hole mobilities [m² V⁻¹ s⁻¹]
- E   = local electric field [V m⁻¹]
- D_e, D_h = electron and hole diffusion coefficients [m² s⁻¹]

The CCR is the regime of classical CMOS operation. It supports transistor switching, voltage-domain
logic, and capacitive signal storage. It does not support temporal address encoding, because temporal
addressing requires a collective phase-coherent state that is absent when carriers are individually
incoherent.

### 3.2 CCR Characteristic Parameters

| Parameter | Symbol | Typical Value | Role |
|-----------|--------|---------------|------|
| Electron mobility | μ_e | 0.10–0.15 m² V⁻¹ s⁻¹ | Carrier transport speed |
| Hole mobility | μ_h | 0.04–0.06 m² V⁻¹ s⁻¹ | Carrier transport speed |
| Debye screening length | λ_D | 5–50 nm | Sets electrostatic shielding scale |
| Carrier lifetime | τ_carrier | 1 μs–1 ms | Minority carrier recombination time |
| Dielectric permittivity | ε_r | 11–15 (substrate dep.) | Capacitive coupling magnitude |

These parameters are standard inputs to SPICE-level models in Tier 1 design flows and are not
redefined here. They are listed because they re-enter the MRSM at the regime boundary: the Debye
screening length λ_D sets a lower bound on the CPR's spatial coherence at the TGI, as described in
Section 7.

### 3.3 CCR Behavior Under Temporal Injection

When TCU injection pulses are applied at depths within the CCR-dominant zone (z < z_f), the injection
energy is absorbed by carrier scattering processes and dissipated as heat. No persistent phase state
is established. The AER measured on a CCR-only coupon asymptotically approaches 0.5 at all Δτ
spacings — the signature of a complete absence of discrimination. This behavior is used in calibration
coupons during TCT instrument validation (TCT Protocol, Section 12).

A material whose Tier 2 layer remains in the CCR (due to insufficient phase-coherent doping, excessive
thermal processing, or process damage) will fail SC classification entirely and cannot be qualified for
temporal manufacturing.

---

## 4. The Coherent Phase Regime (CPR)

### 4.1 Physical Mechanism and Order Parameter

The CPR is characterized by the presence of a collective electronic phase order that spans macroscopic
distances within the substrate. This order arises from the specific material composition of Tier 2
layers and is described by a complex scalar order parameter:

```
ψ(r, t) = |ψ(r, t)| exp(i φ(r, t))
```

where:
- |ψ(r, t)| = amplitude of the phase order at position r and time t
- φ(r, t)   = phase angle of the order parameter [radians]

The order parameter ψ is a collective property of the electron system, not of individual carriers. Its
amplitude |ψ| quantifies the degree of phase coherence at a given location. In a fully coherent bulk
CPR material at operating temperature, |ψ| ≈ ψ_bulk, a material-specific constant.

### 4.2 Temporal Address Encoding

The phase angle φ(r, t) is the physical carrier of temporal address information. When the TCU commits
an operation at address τ, it imprints a specific target phase Φ_τ at the designated substrate site:

```
φ_committed(r, t_commit) = Φ_τ = 2π × (τ mod 1)
```

This mapping wraps the temporal address domain [0, 1) onto the full 2π phase circle. Addresses that
differ by Δτ correspond to phases that differ by:

```
ΔΦ = 2π Δτ
```

Discrimination between two committed addresses therefore requires resolving two phase states separated
by ΔΦ = 2π Δτ. The minimum discriminable phase difference is set by the phase noise of the CPR
material (Section 4.4), which ultimately determines the Substrate Clarity rating.

### 4.3 Phase Stiffness and Coherence Length

The key energetic parameter of the CPR is the phase stiffness ρ_s [J m⁻¹], which quantifies the
energetic cost of spatial phase gradients:

```
F_phase = (ρ_s / 2) ∫ |∇φ(r)|² d³r
```

High phase stiffness suppresses spatial phase fluctuations and is associated with SC-I behavior. Low
phase stiffness allows large spatial phase variations and is associated with SC-II behavior. Materials
unable to sustain any meaningful stiffness at operating temperature fall into SC-III.

The coherence length L_c is derived from ρ_s and the thermal energy scale:

```
L_c = sqrt(ρ_s / (k_B T n_s))
```

where k_B is the Boltzmann constant, T is operating temperature, and n_s is the areal density of
phase-active sites [m⁻²].

L_c is the distance over which a phase perturbation at one site influences the phase at a neighboring
site. Two sites separated by r_pair experience inter-site phase coupling proportional to:

```
C_coupling(r_pair) ≈ exp(−r_pair / L_c)
```

This exponential decay is the physical basis for the inter-site interaction smearing mechanism in the
TCT Protocol (§3.2). The reference interaction length L_ref used in the FSCP address spacing formula
satisfies L_ref ≈ L_c × β_geo, where β_geo is a dimensionless geometric factor of order unity
determined at instrument qualification.

### 4.4 Phase Noise Sources

The total phase noise at a given substrate site has four contributions, corresponding directly to the
four smearing mechanisms enumerated in the TCT Protocol (§3.2).

**Thermal phase noise (σ_thermal):**

```
σ_thermal² = k_B T / (ρ_s × a_site²)
```

where a_site is the effective site lattice constant. This is the irreducible noise floor set by
thermodynamics. It decreases with lower temperature and increases with weaker phase stiffness.

**Doping inhomogeneity noise (σ_doping):**

```
σ_doping² = (∂Φ_τ/∂n_d)² × σ_n_d²
```

where n_d is the local dopant density and σ_n_d is the RMS spatial fluctuation of n_d across the
Tier 2 layer. Doping variations shift the local phase reference, producing a position-dependent offset
in Φ_τ that cannot be corrected by the global CCG distribution. This is the physical origin of
TAOE_sys: a spatially varying systematic address overlay error that tracks the doping map.

**Coherence-length smearing (σ_L_c):**

When the address pair spacing d_pair < L_c, phase correlation between the two sites is significant and
the addresses cannot be treated as independent:

```
σ_L_c² = (Δτ_eff)² × (1 − exp(−d_pair / L_c))² × f_coupling
```

where f_coupling is a dimensionless coefficient dependent on the spatial arrangement of the pair. At
d_pair >> L_c, σ_L_c → 0. At d_pair ≈ L_c, this term contributes comparably to σ_thermal.

**Inter-site interaction noise (σ_inter):**

Phase-active sites are not isolated; the phase at each site is weakly pulled by the committed phases
of its neighbors:

```
δφ_inter(r) = Σ_{r'≠r} J_coupling(|r − r'|) × sin(φ(r') − φ(r))
```

where J_coupling decays exponentially with distance. The temporal crosstalk model in the PDK
Specification (TCRS, §8) is the design-time approximation of this physical coupling. The PDK formula:

```
Δτ_xtalk = K_xtalk × Δτ_eff × exp(−d_pair / L_ref)
```

follows directly from the linear approximation of δφ_inter for small inter-site phase differences,
with K_xtalk being the density-tier multiplier tabulated in the PDK Specification (§8.2).

**Combined phase noise:**

The total normalized address-space noise σ_phase (in units of the full address range) is the
quadrature sum of all four components:

```
σ_phase = sqrt(σ_thermal² + σ_doping² + σ_L_c² + σ_inter²) / (2π)
```

Each component is independently measurable through dedicated TCT sub-protocol variants described in
Section 12.

### 4.5 Phase State Relaxation

A committed phase state is metastable. The order parameter amplitude at the committed site relaxes
toward the equilibrium (uncommitted) background state with characteristic time constant τ_relax:

```
|ψ(r, t)| = |ψ_background| + (|ψ_committed| − |ψ_background|) × exp(−(t − t_commit) / τ_relax)
```

The relaxation is governed by an activated process with Arrhenius temperature dependence:

```
τ_relax = τ_0 × exp(E_a / (k_B T))
```

where:
- τ_0 = pre-exponential attempt frequency factor [s]; typically 10⁻¹² to 10⁻¹³ s
- E_a = activation energy barrier for phase state decay [eV]

This equation has three important consequences for the measurement and design chain:

1. **Temperature sensitivity of τ_relax.** A 10 K increase in operating temperature reduces τ_relax
   by a factor of exp(−E_a / (10 k_B)). For E_a = 0.4 eV, this is approximately 0.85× at 300 K —
   a non-trivial reduction. This is why the CEC temperature control requirement in the TCT Protocol
   (R-CEC-01: ±0.05 K) is physically necessary, not merely a precision preference.

2. **SC-class correlation with E_a.** SC-I materials have larger E_a than SC-II materials. Higher
   phase stiffness corresponds to a deeper energy well for the committed state, hence a higher barrier
   to relaxation. This directly explains why SC-I materials exhibit longer Temporal State Hold counts
   (TSH ≥ 8 cycles typical) compared to SC-II materials at the same T_c.

3. **Injection-to-readback constraint.** The 10-minute ±30 s interval in the TCT Protocol (R-SEQ-02)
   ensures that relaxation-induced phase drift remains below the uncertainty budget threshold across
   all SC class levels. The correction formula:

   ```
   AER_corrected = AER_measured / exp(−Δt_elapsed / τ_relax)
   ```

   (TCT Protocol §7.4) is a first-order approximation valid for Δt_elapsed << τ_relax, which is
   guaranteed by R-SEQ-02 for all qualifying materials.

---

## 5. The Transitional Regime (TR)

### 5.1 Nature of the Transitional Regime

The Transitional Regime is the coexistence zone at the TGI where neither CCR nor CPR behavior is
fully dominant. It arises because the phase-coherent order of the Tier 2 material does not switch on
abruptly at a crystallographic boundary. Instead, the order parameter amplitude |ψ(z)| rises
continuously from zero at z_f to its bulk value ψ_bulk at z_c.

Within the TR, the electronic system simultaneously sustains:

- Residual carrier transport from the Tier 1 CCR layer below (screening by mobile carriers).
- Partial phase order from the Tier 2 CPR layer above (growing coherence length).

The competition between these two behaviors is what makes the TGI the most metrology-intensive zone
in the substrate stack.

### 5.2 The Phase Order Profile

In the absence of process perturbations, the z-dependent order parameter amplitude follows a
hyperbolic tangent profile:

```
|ψ(z)| / ψ_bulk = (1/2) × [1 + tanh((z − z_mid) / ξ_TGI)]
```

where:
- z_mid = (z_f + z_c) / 2 = midpoint of the TGI zone
- ξ_TGI = characteristic half-width of the order-parameter rise [nm]

The width ξ_TGI is not an independent parameter. It is related to the bulk coherence length L_c and
the interface quality:

```
ξ_TGI ≈ L_c × sqrt(IC)
```

where IC is the Interface Continuity composite score from the TGI Metrology Standard (§4.2). A perfect
interface (IC → 1.0) produces the sharpest possible transition (ξ_TGI → L_c). Interface damage or
contamination (IC → 0) broadens the transition and reduces SC_eff.

### 5.3 The Coherence Layer Gradient

The Coherence Layer Gradient measured by the TGI Metrology Standard is the observable projection of
the order parameter gradient:

```
CLG(z) = d(|ψ(z)| / ψ_bulk) / dz = [1 / (2 ξ_TGI)] × sech²((z − z_mid) / ξ_TGI)
```

CLG is maximum at z = z_mid and falls to zero deep in either the CCR or CPR bulk. The peak value is:

```
CLG_max = 1 / (2 ξ_TGI) = 1 / (2 L_c sqrt(IC))
```

This formula interlocks with the TGI Metrology Standard's CLG penalty function (§4.6). The SC-I
threshold of CLG_max = 0.010 and SC-II threshold of 0.020 correspond to minimum acceptable ξ_TGI
values of:

```
ξ_TGI_min (SC-I)  = 1 / (2 × 0.010) = 50 nm
ξ_TGI_min (SC-II) = 1 / (2 × 0.020) = 25 nm
```

A material with L_c < 25 nm cannot form a compliant TGI under any IC condition; this sets a hard
material qualification cutoff independent of SC bulk rating.

### 5.4 Carrier Screening at the TGI

The CCR layer below the TGI supplies mobile carriers that screen the CPR's phase-coherent state via
the electrostatic Debye effect. Within the TGI zone, the effective phase stiffness is reduced from its
bulk value by a screening factor:

```
ρ_s_eff(z) = ρ_s_bulk × (1 − exp(−(z − z_f) / λ_D))
```

For typical Tier 1 materials, λ_D ≈ 5–15 nm. This screening is confined to z near z_f and has
negligible effect at z > z_f + 3λ_D. The TGI proximity rule in the PDK (TPR category, §5.3) requiring
a 5 nm ceiling clearance is physically grounded in this screening effect: it prevents temporal address
sites from entering the carrier-screened sub-zone where effective phase stiffness is reduced.

### 5.5 Effective SC at the TGI

The effective Substrate Clarity across the TGI zone is degraded relative to the Tier 2 bulk:

```
SC_eff(z) = SC_bulk × (|ψ(z)| / ψ_bulk) × f_screening(z)

f_screening(z) = 1 − exp(−(z − z_f) / λ_D)
```

Integrating SC_eff(z) across the TGI zone and weighting by the fraction of temporal operations
nominally placed within that zone yields the effective SC reduction captured by the formula in the
TGI Metrology Standard:

```
SC_eff = SC_bulk × IC × f(CLG_max)
```

The IC factor captures structural quality effects; f(CLG_max) captures the CLG-driven gradient
penalty. Together they project the full SC_eff(z) integral onto two metrology-accessible scalar
quantities.

---

## 6. Material Parameters and Model Inputs

### 6.1 Parameter Taxonomy

The MRSM requires a set of fundamental material parameters as inputs. These are properties of the
bulk Tier 2 material and the TGI interface, determined by the material system and process conditions.
They are anchored through the model-to-observable derivations in Section 8, not directly specified
by the production metrology chain.

**Primary bulk CPR parameters:**

| Symbol | Name | Unit | Description |
|--------|------|------|-------------|
| ρ_s | Phase stiffness | J m⁻¹ | Energetic cost per unit phase gradient squared |
| E_a | Phase decay activation energy | eV | Arrhenius barrier for τ_relax |
| τ_0 | Relaxation prefactor | s | Attempt frequency; ~10⁻¹² to 10⁻¹³ s |
| n_s | Phase-active site density | m⁻² | Areal concentration of CPR-capable sites |
| a_site | Effective site lattice constant | m | Characteristic inter-site distance |
| T_c_mat | CPR critical temperature | K | Temperature above which bulk phase order vanishes |
| ν | Coherence length exponent | dimensionless | Universality class; typical 0.5–0.7 |
| ξ_0 | Bare coherence length | m | L_c extrapolated to T = 0 K |

**Primary TGI interface parameters:**

| Symbol | Name | Unit | Description |
|--------|------|------|-------------|
| z_f | TGI floor depth | nm | Depth at which |ψ| = 0.05 × ψ_bulk |
| z_c | TGI ceiling depth | nm | Depth at which |ψ| = 0.95 × ψ_bulk |
| z_mid | TGI midpoint | nm | (z_f + z_c) / 2 |
| ξ_TGI | Order-parameter rise half-width | nm | ≈ L_c sqrt(IC) |

**CCR boundary parameters:**

| Symbol | Name | Unit | Description |
|--------|------|------|-------------|
| λ_D | Debye screening length | nm | Electrostatic screening at TGI lower boundary |
| n_carrier | Carrier density at z_f | m⁻³ | Mobile carrier density supplying λ_D |

### 6.2 Temperature Dependence of Key Parameters

The operating temperature T appears in three model formulas with distinct functional forms:

```
L_c(T)         = ξ_0 × (1 − T/T_c_mat)^(−ν)          [diverges as T → T_c_mat]
τ_relax(T)     = τ_0 × exp(E_a / (k_B T))              [Arrhenius; decreasing in T]
σ_thermal(T)   = sqrt(k_B T / (ρ_s × a_site²))         [increasing in T]
```

These dependencies are coupled. As T increases toward T_c_mat:

- L_c grows → inter-site coupling extends further → σ_L_c increases.
- τ_relax shrinks → committed states are shorter-lived → TSH decreases.
- σ_thermal grows → the discrimination noise floor rises.

The combined effect is SC degradation that accelerates nonlinearly as T approaches T_c_mat. The
dimensionless reduced temperature:

```
t_red = T / T_c_mat
```

is a concise indicator of regime position. SC-I materials typically operate at t_red ≤ 0.25; SC-II
at 0.25 < t_red ≤ 0.45. Materials with t_red > 0.55 at nominal operating temperature fall into
SC-III.

### 6.3 Process-History Dependence

MRSM parameters carry process history dependence; they are not purely intrinsic to the base material.

| Parameter | Sensitivity | Primary Process Driver |
|-----------|-------------|----------------------|
| E_a | Moderate | Anneal temperature and duration; dopant activation level |
| ρ_s | High | Epitaxial growth conditions; interface cleanliness |
| z_f, z_c | High | Tier 1/Tier 2 stack deposition sequence; etch depth control |
| n_s | Moderate–High | Dopant species, dose, and activation anneal |
| ξ_TGI | High | Interface roughness; contamination at z_f boundary layer |

Section 11 provides a detailed treatment of how individual process steps shift these parameters.

---

## 7. Regime Boundary Conditions

### 7.1 Continuity Requirements at the TGI

The MRSM requires that certain physical quantities are continuous across the TGI boundary, while
others are permitted to be discontinuous.

**Continuous:**
- Total electronic current density J (conservation of charge).
- Electrostatic potential V(z) (no macroscopic charge sheet at z_f).
- Phase order parameter amplitude |ψ(z)| (no first-order jump; tanh profile is smooth by
  construction).

**Permitted to be discontinuous:**
- Phase stiffness ρ_s (step from near-zero in CCR to ρ_s_bulk in CPR; this gives rise to CLG).
- Carrier mobility (steps from μ_CCR to effectively zero in the CPR bulk, where carriers are
  condensed into the phase-ordered state).
- Effective dielectric permittivity (different in Tier 1 vs. Tier 2 material).

A sharp discontinuity in ρ_s at z_f is energetically costly; the system responds by rounding the
ρ_s(z) profile over a length scale ~ξ_TGI. For ideal interfaces (ξ_TGI → L_c), this rounding is
minimal. For damaged interfaces (IC << 1), the rounding extends into the CPR bulk and degrades
SC_eff.

### 7.2 Multi-Zone Boundary Conditions

At a zone boundary within the SCR, the phase order must be maintained at a consistent reference across
the boundary. This is enforced by the ZBI protocol (SCR Specification §7). At the physical level,
this requires that the committed phase at a zone boundary site satisfies:

```
φ_committed(r_boundary, zone A) − φ_ref(zone A) = φ_committed(r_boundary, zone B) − φ_ref(zone B)
```

This condition is satisfiable if and only if the phase stiffness at the boundary site is sufficient
to maintain the committed phase against the cross-zone coupling perturbation within one coherence
time (~τ_relax). The SCR handoff latency L_handoff (SCR Specification, §7.3) must satisfy:

```
L_handoff × T_c < τ_relax × (1 − ε_handoff)
```

where ε_handoff is the maximum allowed fractional phase drift during handoff. For SC-I material,
ε_handoff ≤ 0.05 is typically achievable; for SC-II, ε_handoff ≤ 0.15.

### 7.3 Thermal Boundary Conditions

A zone-to-zone temperature gradient ΔT produces a mismatch in effective TSH:

```
ΔTSH / TSH ≈ (E_a / (k_B T²)) × ΔT
```

For E_a = 0.4 eV and T = 300 K, each 1 K of cross-zone gradient produces approximately 5% TSH
mismatch. SCR zone design must account for this when specifying zone boundary placement relative to
thermal management infrastructure.

---

## 8. Derivation of Observable Parameters

### 8.1 AER Contrast Curve Derivation

The Address Error Rate at a given Δτ spacing is the probability that a readback of a committed phase
state is assigned to the wrong address. Assuming total phase noise is Gaussian with variance σ_phase²
and the discrimination threshold is at the phase midpoint between two target addresses
(ΔΦ/2 = π Δτ), the error probability is:

```
AER(Δτ) = (1/2) erfc(π Δτ / (σ_phase × sqrt(2)))
```

For Δτ >> σ_phase: AER → 0 (perfect discrimination).
For Δτ << σ_phase: AER → 1/2 = AER_sat (chance-level discrimination).

The logistic sigmoid model used in TCT Protocol §8.2:

```
AER_model(Δτ) = AER_sat / (1 + exp(k(Δτ − Δτ_50)))
```

is the standard Fermi-function approximation to the complementary error function. The correspondence
between sigmoid parameters and the physical model is:

```
Δτ_50  ≈ σ_phase × sqrt(2) × erfinv(0.5) / π   [≈ 0.477 σ_phase / π]
k      ≈ π / (σ_phase × sqrt(2) × ln(3))         [≈ π / (1.317 σ_phase)]
AER_sat ≈ 1/2                                    [exact in Gaussian model]
```

The R² ≥ 0.98 fit requirement (TCT Protocol R-AER-09) is met whenever actual phase noise is
well-described by a single-component Gaussian. Bimodal or non-Gaussian distributions (arising from
mixed-regime material or inhomogeneous doping) produce curve shapes that fail the R² criterion; this
is the physical origin of the non-standard curve classification in TCT Protocol §8.3.

### 8.2 SC Rating Derivation

Substituting Δτ_ref = 1/256 into the AER formula and normalizing by AER_sat:

```
SC = 1 − AER(Δτ_ref) / AER_sat
   = erf(π / (256 × σ_phase × sqrt(2)))
```

SC is a monotonically decreasing function of σ_phase. SC = 1 corresponds to σ_phase → 0 (ideal
material). SC = 0 corresponds to complete loss of CPR order.

The SC class boundaries (0.92 for SC-I/SC-II; 0.75 for SC-II/SC-III) correspond to the following
σ_phase thresholds:

```
σ_phase at SC = 0.92:  π / (256 × sqrt(2) × erfinv(0.92)) ≈ 0.00425
σ_phase at SC = 0.75:  π / (256 × sqrt(2) × erfinv(0.75)) ≈ 0.00801
```

Materials with σ_phase > 0.00801 are SC-III and cannot support temporal manufacturing.

### 8.3 Coherence Length Extraction from TCT Data

The TCT Protocol generates an FSCP contrast curve across seven spacing levels S1–S7. At large Δτ
spacings (S1, S2), inter-site interaction is negligible (d_pair >> L_c) and σ_L_c ≈ 0. At small
spacings (S6, S7), inter-site coupling is significant and σ_L_c adds to the total. The difference
in σ_phase² between large-Δτ and small-Δτ regimes isolates σ_L_c, from which L_c is extracted:

```
L_c = d_pair,ref / ln(σ_L_c,ref² / σ_L_c,target²)
```

where d_pair,ref is the pair separation at a reference spacing. This extraction is performed as part
of full TCT data reduction and is reported as a material characterization output alongside the SC
rating.

### 8.4 Coherence Layer Gradient Derivation

The CLG measured by the ISP instrument is the depth-resolved gradient of the normalized SC:

```
CLG(z_i) = (SC_norm(z_{i+1}) − SC_norm(z_{i−1})) / (z_{i+1} − z_{i−1})
```

where SC_norm(z) = SC(z) / SC_bulk. In the MRSM, SC_norm(z) = |ψ(z)| / ψ_bulk. CLG peaks at
z_mid with CLG_max = 1/(2ξ_TGI). The TGI Metrology Standard penalty function derives from:

```
SC_eff = SC_bulk × exp(−κ × CLG_max × Δz_TGI)
```

where κ is a dimensionless coupling coefficient and Δz_TGI = z_c − z_f. The penalty function
parameters (SC-I: threshold 0.010, k = 15.0; SC-II: threshold 0.020, k = 8.0) are empirical fits
to this exponential evaluated at representative Δz_TGI values for each SC class.

### 8.5 Temporal Density Limit Derivation

The Temporal Density TD = N_ops / (A_substrate × C_cycle) is bounded at the physical level by the
address spacing requirement. The minimum allowable address spacing Δτ_eff sets a maximum number of
distinguishable addresses per coherence cycle:

```
N_addr_max = floor(1 / Δτ_eff)
```

Each substrate area element hosting one address is (3 L_c)² (from ASR-001: r_int = 3 L_c).
Therefore:

```
TD_max = floor(1/Δτ_eff) / (9 L_c² × C_cycle)
```

This formula closes the loop between material parameters and the design-space limit. A material with
larger L_c has fewer address sites per unit area, directly reducing TD_max despite potentially
superior SC.

---

## 9. SC Class as a Regime Indicator

### 9.1 SC Class and Regime Dominance

The SC class is not merely a measurement outcome; it is a regime indicator. The three classes map to
distinct physical regimes and operating envelopes:

| SC Class | SC Range | σ_phase Range | t_red Typical | Regime at Tier 2 | TSH Range |
|----------|----------|--------------|--------------|------------------|-----------|
| SC-I | > 0.92 | < 0.00425 | ≤ 0.25 | CPR fully dominant | 8–32+ cycles |
| SC-II | 0.75–0.92 | 0.00425–0.00801 | 0.25–0.45 | CPR dominant with TR residual | 4–12 cycles |
| SC-III | < 0.75 | > 0.00801 | > 0.45 or CCR-dominated | CPR marginal or absent | Not rated |

SC-II materials are physically distinct from SC-I not merely by degree but by character. The 20%
Δτ_margin requirement for SC-II (vs. 15% for SC-I) in the PDK Specification is calibrated to the
higher σ_doping and σ_inter contributions typical of SC-II materials at elevated t_red, where the
phase-order free-energy landscape is shallower and more susceptible to dopant-induced distortion.

### 9.2 Why SC-III Materials Cannot Support Temporal Manufacturing

In SC-III materials, one or more of the following conditions holds:

1. **T ≥ T_c_mat (t_red ≥ 1).** The CPR order is completely suppressed by temperature. ψ_bulk = 0.
   No phase encoding is possible.
2. **Severe doping inhomogeneity.** σ_doping is so large that even at full CPR order, AER at
   Δτ_ref = 1/256 exceeds the SC-II floor. The material cannot be processed to SC-II even with
   perfect thermal control.
3. **L_c < λ_D.** The CPR coherence length is shorter than the CCR Debye screening length. Carrier
   screening from the Tier 1 layer penetrates the entire Tier 2 bulk, suppressing phase order
   everywhere. Increasing Tier 2 thickness does not recover temporal encoding capability; the
   screening is determined by λ_D of Tier 1, not by Tier 2 geometry.

Condition 3 is the regime-conflict condition: the CCR boundary condition wins over the CPR bulk order.
It imposes a minimum L_c requirement on any candidate Tier 2 material as a function of the Tier 1
process node.

### 9.3 SC Lot-Level vs. Site-Level Properties

The TCT Protocol assigns SC class at the lot level, with spatial uniformity characterized by the 5×5
subregion grid (SC_mean, SC_range, SC_σ). Since ρ_s, E_a, and n_s are bulk material properties
determined by the growth process, they are expected to be spatially uniform within a lot. However,
z_f and z_c (TGI boundary positions) are determined by the Tier 1/Tier 2 deposition process and can
vary across the wafer due to step coverage and etch uniformity.

This is why SC_eff can be spatially non-uniform even within an SC-I lot, and why the TGI Metrology
Standard requires die-level spatial characterization in addition to the bulk SC rating.

---

## 10. Multi-Regime Interactions and Failure Modes

### 10.1 Regime Interaction Mechanisms

The three regimes interact at their boundaries through three physical mechanisms:

**Electrostatic coupling (CCR → TR).** Mobile carriers in the CCR layer screen the TR region.
Elevated carrier density (due to overimplant, junction leakage, or proximity to a charge trap layer)
extends λ_D upward into the TGI zone, compressing the available CPR zone.

**Thermal phonon coupling (CCR ↔ CPR).** Phonons generated by switching activity in the CCR
(Joule heating, capacitive discharge) propagate into the Tier 2 layer and elevate the local
temperature. Since τ_relax decreases exponentially with T, localized Joule heating events cause
temporary TSH reduction at nearby temporal address sites.

**Phase boundary pinning (TR ↔ CPR).** At the TGI ceiling z_c, the rapidly rising phase order can
become pinned to interface defects (dangling bonds, contamination sites, crystallographic
dislocations). A pinned site anchors the local phase to a fixed value regardless of the commit
operation, producing a stuck-address failure mode that cannot be distinguished from a valid committed
state by the ARS.

### 10.2 Regime Failure Mode Catalog

| ID | Failure Mode | Physical Origin | Observable Symptom | Detection Method |
|----|--------------|-----------------|-------------------|------------------|
| RFM-01 | CCR Encroachment | Elevated carrier density extending λ_D into TGI | CLG increase; IC_R reduction; SC_eff drop | TGI metrology CLG measurement |
| RFM-02 | Thermal Dephasing | Localized Joule heating from CCR switching | TSH shortfall; increased AER at short spacings | TCT repeat; CMA cycle-level monitoring |
| RFM-03 | Phase Pinning | Interface defects at z_c anchoring phase | Stuck-address fault; SC_range exceedance | FSCP spatial uniformity; SC_range |
| RFM-04 | Coherence Collapse | T_c_mat exceeded transiently | Sudden global SC degradation across wafer | CMA L2 alarm; SC measurement post-event |
| RFM-05 | Inter-Zone Phase Skew | Cross-zone τ_relax mismatch from thermal gradient | ZBI retransmission failures; TSH underrun | CMA inter-zone; TGI TAOE GDC metric |
| RFM-06 | Dopant Gradient Drift | Thermally-driven dopant redistribution | Progressive SC_σ increase; TAOE_sys drift | TGI GDC tracking; TCT lot requalification |

RFM-01 through RFM-05 have direct counterparts in the SCR Specification failure mode table (§9).
RFM-06 is a long-timescale effect managed through the TGI production monitoring tier structure (TGI
Metrology Standard §11.3).

### 10.3 Failure Mode Interaction

The most damaging failure scenarios involve coupled modes:

**RFM-02 + RFM-04 cascade.** A localized thermal event (RFM-02) that exceeds T_c_mat at a hot spot
triggers RFM-04 within the heated zone. Recovery requires the zone to cool below T_c_mat, at which
point phase order re-nucleates — but with a random initial phase angle. This permanently corrupts any
address that was held through the collapse. This scenario motivates the SCR L3 severity classification
(Coherence Collapse) and the requirement for full re-qualification following such an event.

**RFM-01 + RFM-03 co-occurrence.** CCR encroachment that reaches z_c simultaneously with surface
defect pinning produces a phase-trapped zone where committed state is controlled by defect pinning
rather than by the commit operation. Such zones cannot be corrected by PIMC because TAOE_sys
correction assumes a smooth spatial function; a defect-pinned zone is stochastic in character.

---

## 11. Process Effects on Regime Structure

### 11.1 Epitaxial Growth and ρ_s

Phase stiffness ρ_s is primarily set during Tier 2 epitaxial growth.

| Growth Variable | Effect on ρ_s | Direction |
|-----------------|---------------|-----------|
| Growth temperature | Higher T: higher crystalline perfection | Positive |
| Growth rate | Faster: more point defect incorporation | Negative |
| Dopant concentration n_d | Optimal n_d for CPR activation (non-monotonic) | Non-monotonic |
| Precursor purity | Impurity incorporation lowers ρ_s | Negative |
| Substrate miscut angle | Small miscut promotes step-flow growth | Positive (small miscut) |

Because ρ_s directly determines σ_thermal and (through L_c) σ_L_c, growth optimization is the
primary lever for achieving SC-I classification. Post-growth process steps can only degrade ρ_s, not
enhance it.

### 11.2 Activation Anneal and E_a

The activation energy E_a is set by the dopant activation anneal following ion implantation. The
anneal conditions control three competing effects:

1. **Dopant site occupation.** Dopants must occupy the specific substitutional or interstitial sites
   that provide CPR coupling. Under-annealed lots have partially activated dopants with lower E_a.
2. **Defect annihilation.** Implant damage (vacancies, interstitials) provides trapping sites that
   reduce E_a. Higher anneal temperature removes these defects, but at the expense of increased
   dopant redistribution risk.
3. **Activation competition.** High-temperature anneals can cause dopant diffusion into the TGI zone,
   shifting z_f upward and compressing the CPR bulk.

The MRSM predicts that optimal anneal temperature maximizes E_a subject to the constraint that dopant
redistribution does not shift z_f by more than Δz_TGI/4.

### 11.3 TGI Formation: z_f and z_c Control

**z_f** is controlled by:
- The endpoint of Tier 1 deposition.
- The Tier 1 top-surface preparation (oxide removal, cleaning protocol): contamination at this surface
  increases ξ_TGI and lowers IC.
- The first atomic layers of Tier 2 deposition: a nucleation layer with higher defect density than
  the bulk Tier 2 shifts z_f upward.

**z_c** is controlled by:
- The total Tier 2 layer thickness at deposition.
- Post-deposition planarization processes: over-polishing reduces Tier 2 thickness and may bring z_c
  inside the minimum CPR bulk zone requirement.

A common failure mode is symmetric shrinkage: contamination that simultaneously raises z_f and reduces
Tier 2 thickness. Both effects compress the available CPR bulk, degrade IC, and increase ξ_TGI. The
TGI Uniformity Index (TUI) measurement is specifically designed to catch this and its asymmetric
variants.

### 11.4 Thermal Budget and τ_relax Stability

Every thermal step in the process sequence following Tier 2 deposition perturbs τ_relax. The
accumulated effect is tracked using a thermal budget integral:

```
ΔΘ_thermal = Σ_steps [t_step × exp(−E_a_relax / (k_B T_step))]
```

where E_a_relax is the effective activation energy for permanent τ_relax modification (distinct from
E_a for state decay; typically higher). Thermal steps with ΔΘ_thermal above a process-node-specific
threshold cause irreversible reduction of τ_relax. This constraint motivates the post-ASML trend
toward low-thermal-budget back-end processes for any layer deposited above z_c.

---

## 12. Model Validation and Calibration

### 12.1 Validation Strategy

MRSM validation operates at three levels, each with increasing experimental effort and diagnostic
specificity.

**Level 1 — Internal consistency.** Verify that TCT-derived L_c, τ_relax, and SC values are mutually
consistent with model predictions given the measured T. If SC(measured) and σ_phase derived from L_c
and T disagree by more than ±0.02, the single-Gaussian noise model is suspect and Level 2
decomposition is required.

**Level 2 — Component decomposition.** Separately measure each σ_phase component:

- σ_thermal: on high-symmetry samples at multiple temperatures; extrapolate to T → 0 to isolate
  non-thermal terms.
- σ_doping: on samples with intentionally varied dopant dose; extract slope vs. n_d.
- σ_L_c: from Δτ-dependent AER data as described in §8.3.
- σ_inter: by varying d_pair at fixed Δτ; extract the coupling decay constant vs. d_pair.

**Level 3 — Cross-document consistency.** Verify that parameters extracted from TCT data are
consistent with TGI metrology observations:

| Prediction | Measured by | Expected Relationship |
|-----------|-------------|----------------------|
| CLG_max = 1/(2 L_c sqrt(IC)) | ISP (CLG) and CGS (L_c) | ±15% after IC correction |
| SC_eff = SC_bulk × IC × f(CLG_max) | TGI metrology direct | Formula evaluated with above params |
| TSH = floor(τ_relax / (Δτ_eff × T_c)) | Logic Folding verification suite | ±1 cycle (SC-I); ±2 cycles (SC-II) |
| TD_max = floor(1/Δτ_eff) / (9 L_c² × C_cycle) | PDK CBT and tapeout density data | Within 5% of achieved density |

### 12.2 Calibration Reference Hierarchy

MRSM parameters are anchored through the calibration hierarchy established in the TCT Protocol:

```
National Standard (τ_n, Δτ_n)
    └─ RLSS (Reference Lot Standard Set)
          └─ FTRC (Fab Transfer Reference Coupon)
                └─ TAIS + ARS session calibration
                      └─ Per-lot TCT measurements
                            └─ MRSM parameter extraction
```

The critical calibration tie point is the FTRC, which establishes the absolute temporal address scale
in units of T_c. All MRSM formulas involving the dimensional form of Δτ depend on this calibration
tie being current. The FTRC recalibration interval (TCT Protocol §12.3) ensures this tie remains
valid to the tolerance required for Level 1 consistency checks.

### 12.3 Model Update Triggers

| Trigger | Updated Parameters | Update Protocol |
|---------|-------------------|-----------------|
| New material system qualification | All bulk CPR parameters | Full Level 1–3 validation |
| Process node change | z_f, z_c, E_a, ρ_s | Level 2 + Level 3 cross-check |
| Fab thermal profile change | τ_relax (via thermal budget) | Level 1 consistency check |
| Persistent Level 3 disagreement (>15%) | All parameters affecting discrepant check | Full Level 1–3 validation |
| T_c_mat revision by material supplier | T_c_mat, L_c, σ_thermal | Level 1 + TSH re-verification |

Model updates are logged in the MRSM revision history and trigger a PDK minor version increment when
any parameter change propagates to a TDR rule or CBT value.

---

## 13. Design Implications

### 13.1 Summary of Model-to-Design Parameter Paths

| MRSM Physical Insight | Design Consequence | Governing Document |
|-----------------------|-------------------|--------------------|
| L_c sets minimum site separation | ASR-001: r_int = 3 L_c | PDK Specification §5.1 |
| ρ_s determines σ_phase and hence SC | Δτ_margin: 15% (SC-I), 20% (SC-II) | PDK Specification §4.2 |
| τ_relax sets state persistence | TSH = floor(τ_relax / (Δτ_eff × T_c)); refresh at N_hold > TSH | Logic Folding §5 |
| Thermal sensitivity of τ_relax | Cross-zone TSH mismatch budget | Logic Folding §7; SCR Spec §8 |
| Inter-site coupling decays as exp(−d/L_ref) | TCRS crosstalk rule; K_xtalk tier multipliers | PDK Specification §8 |
| CLG_max = 1/(2 L_c sqrt(IC)) | TPR: 5 nm ceiling clearance; 10 nm CLG exclusion | PDK Specification §5.3 |
| σ_doping → position-dependent TAOE_sys | PIMC activation threshold at GDC ≥ 0.85 | TGI Metrology §9 |
| Debye screening compresses CPR zone | Minimum Tier 2 thickness per SC class | Process qualification |
| RFM-02: Joule heating raises local T | CCR switching constraints near TRF placement | Logic Folding §6.4 |

### 13.2 SC-Class Selection as a Design Decision

The MRSM makes clear that SC class selection is a physical commitment, not a performance grade. An
SC-II material has a genuinely different physical regime structure from SC-I:

- The TR zone is relatively larger (shorter L_c → smaller ξ_TGI), making TGI placement constraints
  tighter in absolute terms.
- σ_phase is higher, requiring larger Δτ_margin and thus fewer usable addresses per cycle.
- τ_relax is shorter, requiring more aggressive TR refresh scheduling.
- Thermal sensitivity of all three quantities is greater (higher t_red → closer to T_c_mat).

Designs that target SC-I material must not be adapted for SC-II by simply applying more conservative
Δτ_margins. The full set of changes — L_c-driven ASR rules, TSH recomputation, CBT rebalancing, and
CLG penalty revalidation — must be applied as a coordinated PDK migration.

### 13.3 Multi-Zone Designs and Regime Uniformity

In Zone-Distributed architectures (Logic Folding §4.4), the MRSM establishes that regime uniformity
across zones is a physical requirement, not a design preference:

- All zones in a multi-zone architecture must use the same SC class. Mixing SC-I and SC-II zones
  creates a fundamental asymmetry in TSH and Δτ_eff that cannot be bridged by the ZBI protocol
  without either leaving SC-I margin on the table or violating SC-II refresh requirements.
- Zone boundary placement must respect the thermal boundary condition derived in §7.3: a 1 K
  temperature gradient produces ~5% TSH mismatch per zone. Zones should be placed to minimize
  cross-zone thermal gradients, or the TSH budget must be explicitly de-rated by the expected
  gradient.
- The cross-zone coherence budget fraction default of 0.20 (PDK Specification §6) corresponds, in
  the MRSM, to the fractional reduction in effective B_cycle caused by the L_handoff-induced dead
  time. For SC-II material at maximum L_handoff, this fraction may need to be increased to 0.25–0.30
  to maintain functional timing closure.

---

## 14. Glossary

| Term | Definition |
|------|------------|
| AER | Address Error Rate. Fraction of readback events returning an incorrect temporal address. Defined in TCT Protocol §7. |
| AER_sat | Saturation AER at Δτ → 0; equals 0.5 in the Gaussian noise model. Fitted parameter in the logistic sigmoid curve. |
| CCR | Classical Carrier Regime. The electronic regime in which band-conduction charge transport dominates and temporal address encoding is not supported. Governs Tier 1 structural layers. |
| CLG | Coherence Layer Gradient. The depth derivative of the normalized phase order amplitude; observable via ISP instrument. Defined in TGI Metrology Standard §4.5. |
| CPR | Coherent Phase Regime. The electronic regime in which a collective phase-coherent electronic order supports temporal address encoding. Governs Tier 2 temporal layers. |
| d_pair | Physical separation between two substrate sites in an FSCP address pair. |
| E_a | Activation energy for phase state decay. Sets the Arrhenius slope of τ_relax vs. 1/T. |
| IC | Interface Continuity. Composite metrology score quantifying the structural quality of the TGI zone. Defined in TGI Metrology Standard §4.2. |
| K_xtalk | Temporal crosstalk multiplier. Density-tier-dependent coefficient in the Δτ_xtalk formula. Tabulated in PDK Specification §8.2. |
| L_c | Coherence length. The characteristic spatial distance over which inter-site phase coupling decays. Derived from ρ_s, k_B T, and n_s. |
| L_ref | Material interaction reference length. L_ref ≈ L_c × β_geo; used in FSCP address spacing and TCRS crosstalk formula. Defined in TCT Protocol §3. |
| MRSM | Multi-Regime Semiconductor Model. This document. The physical theory underpinning all empirical parameters in the post-ASML era series. |
| n_s | Phase-active site density [m⁻²]. The areal concentration of CPR-capable sites in the Tier 2 material. |
| ρ_s | Phase stiffness [J m⁻¹]. Energetic cost per unit squared phase gradient; the primary determinant of L_c and σ_thermal. |
| RFM | Regime Failure Mode. A failure classification in the MRSM catalog (§10.2); cross-referenced to SCR Specification failure mode table. |
| SC | Substrate Clarity. The primary material quality metric for temporal manufacturing; SC = erf(π / (256 × σ_phase × sqrt(2))). Defined in TCT Protocol §9. |
| SC_eff | Effective Substrate Clarity. SC degraded by TGI interface effects; SC_eff = SC_bulk × IC × f(CLG_max). Defined in TGI Metrology Standard §4.7. |
| σ_phase | Total normalized phase noise. Quadrature sum of σ_thermal, σ_doping, σ_L_c, and σ_inter, divided by 2π. The primary determinant of SC. |
| t_red | Reduced temperature. t_red = T / T_c_mat. A dimensionless indicator of regime proximity to the CPR critical point. |
| T_c_mat | CPR critical temperature. The temperature above which bulk phase order vanishes in a given Tier 2 material. |
| T_c | Coherence cycle period. The clock period of the SCR zone within which a single commit cycle must complete. |
| τ_0 | Relaxation prefactor. Pre-exponential factor in the Arrhenius formula for τ_relax; ~10⁻¹² to 10⁻¹³ s for qualifying materials. |
| τ_relax | Phase state relaxation time. The time constant for decay of a committed phase state toward the uncommitted background. Arrhenius: τ_relax = τ_0 × exp(E_a / (k_B T)). |
| TGI | Temporal-Geometric Interface. The transition zone (z_f to z_c) between the CCR-dominant Tier 1 and the CPR-dominant Tier 2. |
| TR | Transitional Regime. The coexistence zone at the TGI where neither CCR nor CPR is fully dominant. Corresponds to the region z_f ≤ z ≤ z_c. |
| TSH | Temporal State Hold. The maximum number of coherence cycles a committed phase state may be held without refresh before error probability exceeds the design margin. TSH = floor(τ_relax / (Δτ_eff × T_c)). Defined in Logic Folding Architecture Guide §5. |
| ξ_0 | Bare coherence length. The coherence length extrapolated to T = 0 K; L_c(T) = ξ_0 × (1 − T/T_c_mat)^(−ν). |
| ξ_TGI | Order-parameter rise half-width. The characteristic length of the tanh profile across the TGI zone; ξ_TGI ≈ L_c × sqrt(IC). |
| λ_D | Debye screening length. The electrostatic shielding length of the CCR layer that compresses effective phase stiffness at the TGI lower boundary. |
| ψ_bulk | Bulk CPR order parameter amplitude. The equilibrium value of |ψ| deep in the Tier 2 CPR zone at operating temperature. |

---

## 15. Related Documents

| Document | Path | Relationship |
|----------|------|--------------|
| The Temporal Manufacturing Primer | `../The_Temporal_Manufacturing_Primer.md` | Establishes SC classes, TD, TRS layers, and equipment tiers that MRSM grounds in physical theory |
| The SCR Specification | `../The_SCR_Specification.md` | Normative requirements for SCR zone architecture; MRSM explains physical basis for zone sizing, L_handoff constraint, and CMA alarm thresholds |
| The TGI Metrology Standard | `../The_TGI_Metrology_Standard.md` | Normative metrology for the TGI zone; MRSM provides derivations for CLG, IC, SC_eff, and TAOE_sys |
| TCT Protocol | `../TCT_Protocol.md` | Root of the SC measurement chain; MRSM explains the physical basis for AER(Δτ), the sigmoid model, τ_relax correction, and L_c extraction |
| The TRS-Aware PDK Specification | `../The_TRS-Aware_PDK_Specification.md` | Normative PDK spec consuming MRSM-derived parameters; MRSM grounds ASR r_int = 3 L_c, Δτ_margin class values, and TCRS K_xtalk formula |
| The Logic Folding Architecture Guide | `../The_Logic_Folding_Architecture_Guide.md` | Design methodology document; MRSM grounds TSH formula, cross-zone TSH mismatch budget, and Joule heating constraints near TRF |
| Temporal Address Mapping Specification | `../../design/Temporal_Address_Mapping_Spec.md` | Stub. Downstream document specifying how Φ_τ = 2π × τ is implemented as a design convention; governs address-value mapping schemes, discrimination-safe encoding, and the binary threshold / thermometer / grey-code choices referenced in Logic Folding Architecture Guide §3.1 |
| Substrate Clarity Classification Standard | `../../materials/SC_Classification.md` | Stub. Normative classification of substrate material systems against SC class thresholds; directly references MRSM σ_phase boundaries and the t_red operating envelope for each class |
| TRS Stack Qualification Procedure | `../../fab/TRS_Qualification.md` | Stub. Qualification procedure for the TRS equipment stack; consumes MRSM-derived L_c and τ_relax values to set Δτ_min, W_apod, and T_seq |
| SCR Zone Configuration Guide | `../../fab/SCR_Zone_Config.md` | Stub. Zone sizing and layout guidance; MRSM §7.3 provides the thermal boundary condition governing cross-zone TSH mismatch budget used in zone placement decisions |
| TTF Reference | `../../eda/TTF_Reference.md` | Stub. Normative Temporal Timing Format specification; MRSM grounds the DDA derating curve (density-dependent τ_relax reduction) that the DDA arc encodes |
| TLMF Schema | `../../data-formats/TLMF_Schema.md` | Stub. Schema for SC Class Layer Maps; MRSM explains why SC_design = min(SC_bulk, SC_eff) is correct: SC_eff can only reduce SC_bulk, never increase it, because ξ_TGI ≥ L_c always |
| TCT Data Exchange Format Schema | `../../data-formats/TCT_DEF_Schema.md` | Stub. Machine-parseable TCT Report format; MRSM defines the physical meaning of all field values that the schema encodes |

---

*This document is INFORMATIVE. It does not impose normative requirements. All
normative requirements are located in the documents listed above in §15. Where
this document's formulas and the normative documents' rules appear to conflict,
the normative documents take precedence and this document should be reviewed for
revision.*

*Proposed revisions to the MRSM should be submitted via pull request with a linked
issue. Because this document is the physical foundation for normative parameters
in multiple downstream documents, any revision that changes a formula result by
more than 5% at an SC class boundary requires a cross-impact analysis spanning
the TCT Protocol, TGI Metrology Standard, PDK Specification, and Logic Folding
Architecture Guide before the revision is merged. The cross-impact analysis must
be included in the pull request body.*
