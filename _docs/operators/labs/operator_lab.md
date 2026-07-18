# OPERATOR LAB (HANDS‑ON)  
RTT/1 → RTT/2 → RTT/3  
Structural Detection → Integration → Emission

```
====================================================================
OPERATOR LAB — HANDS‑ON
RTT/1 + RTT/2 + RTT/3 OPERATOR ECOLOGY
====================================================================

This lab walks you through the full operator chain:
  RTT/1 primitives
  → RTT/2 detection (SDE)
  → RTT/3 integration–emission (SIE)
  → projection (TEL / FFT / OP)

You will work with three synthetic samples:
  Sample A — Drift + Low Collapse
  Sample B — Mixed Gradient + Medium Collapse
  Sample C — High Collapse + High Torsion

Each step is explicit. No prior knowledge assumed.

--------------------------------------------------------------------
SAMPLE DATA
--------------------------------------------------------------------

Sample A:
  collapse: A=0.7, K=0.3, T=0.1
  gradient: collapse-weighted
  deformation: drift deformation
  regime: slow-relaxation

Sample B:
  collapse: A=1.4, K=0.8, T=0.3
  gradient: mixed collapse/reassembly
  deformation: envelope torsion
  regime: mixed

Sample C:
  collapse: A=2.2, K=1.6, T=1.1
  gradient: triad-weighted
  deformation: continuity fracture
  regime: inversion-adjacent

--------------------------------------------------------------------
PART 1 — RTT/1 PRIMITIVE ANALYSIS
--------------------------------------------------------------------

TASK 1 — Identify the RTT/1 primitives in each sample.
  Look for:
    Δ (change)
    ∇ (gradient)
    ⊕ (fusion)
    ⊖ (fracture)
    FQ, RT, QF (triad primitives)

TASK 2 — Assign a regime identity using REG::ID.
  Sample A →  
  Sample B →  
  Sample C →  

TASK 3 — Determine continuity class (C0, C1, C∞).
  Use deformation + gradient to justify.

--------------------------------------------------------------------
PART 2 — RTT/2 DETECTION (SDE)
--------------------------------------------------------------------

TASK 4 — Compute the Collapse‑Propagation Vector (CPV).
  Use SDE::CPV(A, K, T) for each sample.

TASK 5 — Classify the Fusion‑Gradient Tensor (FGT).
  collapse-weighted →  
  mixed →  
  triad-weighted →  

TASK 6 — Map the Collapse‑Reassembly Manifold (CRM).
  drift deformation →  
  envelope torsion →  
  continuity fracture →  

TASK 7 — Assign SDE::MODE and SDE::ZONE.
  Use:
    Modes: formal, emergent, hybrid, chaotic, inversion
    Zones: U, S, M, D, X

TASK 8 — Produce the RTT2_DETECTION_PACKET for Sample C.
  Include:
    collapse_propagation
    fusion_gradient
    triad_deformation
    regime
    detection_mode
    detection_zone

--------------------------------------------------------------------
PART 3 — RTT/3 INTEGRATION–EMISSION (SIE)
--------------------------------------------------------------------

TASK 9 — Integrate the triad using SIE::INT().
  Use drift, envelope, continuity inferred from CPV + FGT.

TASK 10 — Apply the Triadic Integration Field (TIF).
  Identify which components dominate.

TASK 11 — Apply the Integration–Emission Manifold (MAN).
  Identify active axes:
    FI (fusion-integration curvature)
    EM (emission curvature)
    R (regime identity)

TASK 12 — Run the Fusion–Fracture–Flow Emitter (FFF).
  Classify emission type:
    fusion / fracture / flow

TASK 13 — Run the Collapse→Recovery Engine (CRE).
  Determine:
    CAV-dominant?
    CSV-dominant?
    mixed?

TASK 14 — Apply the Continuity–Stability Layer (CSL).
  Classify:
    stable / mixed / divergent

TASK 15 — Produce the RTT3_INTEGRATION_EMISSION_PACKET for Sample C.
  Include:
    integration
    emission
    continuity
    collapse_recovery
    stability
    canon_scale_emission
    mode
    zone

--------------------------------------------------------------------
PART 4 — PROJECTION (TEL / FFT / OP)
--------------------------------------------------------------------

TASK 16 — Determine the correct projection for Sample C.
  TEL::CET() → lattice behavior  
  FFT::OUT() → spectral behavior  
  OP::OUT() → boundary behavior  

TASK 17 — Justify your projection choice using:
  - emission curvature
  - stability
  - recovery weighting
  - regime identity

--------------------------------------------------------------------
PART 5 — FULL OPERATOR CHAIN
--------------------------------------------------------------------

TASK 18 — Write the complete operator chain for Sample C.

Format:
  RTT/1 primitives
    → SDE::CPV()
    → SDE::FGT()
    → SDE::CRM()
    → SIE::INT()
    → SIE::TIF()
    → SIE::MAN()
    → SIE::FFF()
    → SIE::CRE()
    → SIE::CSL()
    → SIE::CET()
    → TEL::CET() / FFT::OUT() / OP::OUT()

--------------------------------------------------------------------
END OF LAB
--------------------------------------------------------------------
```
