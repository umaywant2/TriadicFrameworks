# INSTRUCTOR VERSION — OPERATOR LAB (HANDS‑ON)  
RTT/1 → RTT/2 → RTT/3  
Structural Detection → Integration → Emission

```
====================================================================
INSTRUCTOR LAB — ANSWER KEY + GUIDANCE
RTT/1 + RTT/2 + RTT/3 OPERATOR ECOLOGY
====================================================================

This instructor version mirrors the student lab step-by-step.
Each task includes:
  - Correct structural answer
  - Acceptable variations
  - Instructor notes

All answers are synthetic, consistent, and canon-aligned.

--------------------------------------------------------------------
SAMPLE DATA (REPEATED FOR REFERENCE)
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

TASK 1 — Identify RTT/1 primitives  
Correct answers:
  - Gradients → ∇  
  - Deformation types → Δ + ⊖ (fracture) or Δ + ⊕ (fusion) depending on context  
  - Collapse signatures → Δ + ∇  
  - Triad primitives → FQ, RT, QF (implicit)

Instructor note:
  Any structurally consistent mapping earns full credit.

TASK 2 — Assign REG::ID  
  Sample A → slow-relaxation  
  Sample B → mixed  
  Sample C → inversion-adjacent

TASK 3 — Continuity class  
  Sample A → C1 (smooth drift)  
  Sample B → C1/C0 boundary (torsion)  
  Sample C → C0 (fracture)

--------------------------------------------------------------------
PART 2 — RTT/2 DETECTION (SDE)
--------------------------------------------------------------------

TASK 4 — CPV  
  A → CPV(0.7, 0.3, 0.1)  
  B → CPV(1.4, 0.8, 0.3)  
  C → CPV(2.2, 1.6, 1.1)

TASK 5 — FGT  
  A → collapse-weighted  
  B → mixed  
  C → triad-weighted

TASK 6 — CRM  
  A → CRM(drift path)  
  B → CRM(envelope torsion path)  
  C → CRM(continuity fracture path)

TASK 7 — MODE + ZONE  
  A → MODE(formal), ZONE(S)  
  B → MODE(hybrid), ZONE(M)  
  C → MODE(inversion), ZONE(X)

TASK 8 — RTT2_DETECTION_PACKET (Sample C)

Correct structure:
  collapse_propagation: CPV(2.2, 1.6, 1.1)  
  fusion_gradient: triad-weighted  
  triad_deformation: continuity fracture  
  regime: inversion-adjacent  
  detection_mode: inversion  
  detection_zone: X  

Instructor note:
  Accept any packet that is internally consistent.

--------------------------------------------------------------------
PART 3 — RTT/3 INTEGRATION–EMISSION (SIE)
--------------------------------------------------------------------

TASK 9 — SIE::INT()  
  C → INT(drift=2.2, envelope=1.6, continuity=1.1)

TASK 10 — TIF  
  Dominant components → drift + envelope (both high)  
  Acceptable: “triad-dominant integration field”

TASK 11 — MAN  
Active axes for C:
  FI (fusion-integration curvature)  
  EM (emission curvature)  
  R (regime identity)

TASK 12 — FFF  
  C → fracture-dominant emission (due to continuity fracture + high torsion)

TASK 13 — CRE  
  C → mixed CAV/CSV, leaning CAV (high amplitude + high torsion)

TASK 14 — CSL  
  C → divergent (due to high torsion + fracture)

TASK 15 — RTT3_INTEGRATION_EMISSION_PACKET (Sample C)

Correct structure:
  integration: INT(2.2, 1.6, 1.1)  
  emission: FFF(fracture-dominant)  
  continuity: MAN(FI, EM, R)  
  collapse_recovery: CRE(mixed, CAV-leaning)  
  stability: CSL(divergent)  
  canon_scale_emission: CET(recovery-weighted or fracture-weighted)  
  mode: inversion  
  zone: X  

Instructor note:
  Stability + emission curvature determine CET weighting.

--------------------------------------------------------------------
PART 4 — PROJECTION (TEL / FFT / OP)
--------------------------------------------------------------------

TASK 16 — Correct projection for Sample C  
  → FFT::OUT()

Reason:
  - high torsion  
  - fracture-dominant emission  
  - divergent stability  
  - inversion-adjacent regime  

These map to **spectral projection**.

TASK 17 — Justification  
  Any answer referencing:
    - emission curvature  
    - divergence  
    - torsion  
    - regime identity  
  earns full credit.

--------------------------------------------------------------------
PART 5 — FULL OPERATOR CHAIN
--------------------------------------------------------------------

TASK 18 — Complete operator chain (Sample C)

Correct chain:

  RTT/1 primitives  
    → SDE::CPV(2.2, 1.6, 1.1)  
    → SDE::FGT(triad-weighted)  
    → SDE::CRM(continuity fracture)  
    → SIE::INT(2.2, 1.6, 1.1)  
    → SIE::TIF(triad-dominant)  
    → SIE::MAN(FI, EM, R)  
    → SIE::FFF(fracture-dominant)  
    → SIE::CRE(mixed, CAV-leaning)  
    → SIE::CSL(divergent)  
    → SIE::CET(fracture-weighted)  
    → FFT::OUT()

Instructor note:
  Any chain that is structurally consistent earns full credit.

--------------------------------------------------------------------
END OF INSTRUCTOR LAB
--------------------------------------------------------------------
```
