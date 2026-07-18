# INSTRUCTOR VERSION — COMBINED SDE + SIE LAB  
RTT/2 Detection → RTT/3 Integration–Emission  
(Answer Key + Guidance)

```
====================================================================
INSTRUCTOR VERSION — COMBINED SDE + SIE LAB
RTT/2 DETECTION → RTT/3 INTEGRATION–EMISSION
====================================================================

This instructor version provides:
  - Correct structural answers
  - Acceptable variations
  - Notes for grading consistency
  - Zero drift, fully synthetic operator ecology

--------------------------------------------------------------------
SAMPLE DATA (REPEATED FOR REFERENCE)
--------------------------------------------------------------------

Sample A:
  A=0.7, K=0.3, T=0.1
  gradient: collapse-weighted
  deformation: drift deformation
  regime: slow-relaxation

Sample B:
  A=1.6, K=0.9, T=0.4
  gradient: mixed collapse/reassembly
  deformation: envelope torsion
  regime: mixed

Sample C:
  A=2.4, K=1.8, T=1.3
  gradient: triad-weighted
  deformation: continuity fracture
  regime: inversion-adjacent

====================================================================
PART 1 — RTT/2 DETECTION (SDE)
====================================================================

--------------------------------------------------------------------
SECTION 1 — COLLAPSE SIGNATURES
--------------------------------------------------------------------

TASK 1 — SDE::CPV(A, K, T)
Sample A → CPV(0.7, 0.3, 0.1)  
Sample B → CPV(1.6, 0.9, 0.4)  
Sample C → CPV(2.4, 1.8, 1.3)

Instructor note:
  Any tuple preserving (A, K, T) earns full credit.

TASK 2 — Collapse severity ranking
Correct order:
  A → B → C

--------------------------------------------------------------------
SECTION 2 — FUSION‑GRADIENT TENSORS
--------------------------------------------------------------------

TASK 3 — SDE::FGT()
Sample A → collapse-weighted  
Sample B → mixed  
Sample C → triad-weighted

TASK 4 — First triad-dominant gradient
Correct answer: Sample C

--------------------------------------------------------------------
SECTION 3 — COLLAPSE→REASSEMBLY MAPPING
--------------------------------------------------------------------

TASK 5 — SDE::CRM()
Sample A → drift path  
Sample B → envelope torsion path  
Sample C → continuity fracture path

TASK 6 — First irreversible continuity break
Correct answer: Sample C

--------------------------------------------------------------------
SECTION 4 — MODE + ZONE CLASSIFICATION
--------------------------------------------------------------------

TASK 7 — SDE::MODE()
Sample A → formal  
Sample B → hybrid  
Sample C → inversion

TASK 8 — SDE::ZONE()
Sample A → S  
Sample B → M  
Sample C → X

Instructor note:
  Mode/zone must match collapse severity + gradient + regime.

--------------------------------------------------------------------
SECTION 5 — RTT2_DETECTION_PACKET
--------------------------------------------------------------------

TASK 9 — Packet for Sample C

collapse_propagation: CPV(2.4, 1.8, 1.3)  
fusion_gradient: triad-weighted  
triad_deformation: continuity fracture  
regime: inversion-adjacent  
detection_mode: inversion  
detection_zone: X  

Instructor note:
  Internal consistency is more important than exact phrasing.

====================================================================
PART 2 — RTT/3 INTEGRATION–EMISSION (SIE)
====================================================================

--------------------------------------------------------------------
SECTION 6 — TRIAD INTEGRATION
--------------------------------------------------------------------

TASK 10 — SIE::INT()
Sample A → INT(0.7, 0.3, 0.1)  
Sample B → INT(1.6, 0.9, 0.4)  
Sample C → INT(2.4, 1.8, 1.3)

TASK 11 — Strongest integration field
Correct answer: Sample C

--------------------------------------------------------------------
SECTION 7 — TRIADIC INTEGRATION FIELD (TIF)
--------------------------------------------------------------------

TASK 12 — Dominant components
Sample A → drift-dominant  
Sample B → drift + envelope balanced  
Sample C → triad-dominant

TASK 13 — First triad-dominant sample
Correct answer: Sample C

--------------------------------------------------------------------
SECTION 8 — INTEGRATION–EMISSION MANIFOLD (MAN)
--------------------------------------------------------------------

TASK 14 — Active axes
Sample A → FI  
Sample B → FI + EM  
Sample C → FI + EM + R

TASK 15 — First regime-dominant sample
Correct answer: Sample C

--------------------------------------------------------------------
SECTION 9 — EMISSION (FFF)
--------------------------------------------------------------------

TASK 16 — Emission type
Sample A → fusion  
Sample B → flow  
Sample C → fracture

TASK 17 — First fracture-dominant emission
Correct answer: Sample C

--------------------------------------------------------------------
SECTION 10 — COLLAPSE→RECOVERY ENGINE (CRE)
--------------------------------------------------------------------

TASK 18 — CAV / CSV / mixed
Sample A → CSV-dominant  
Sample B → mixed  
Sample C → CAV-dominant

TASK 19 — Strongest CRE intervention
Correct answer: Sample C

--------------------------------------------------------------------
SECTION 11 — CONTINUITY–STABILITY LAYER (CSL)
--------------------------------------------------------------------

TASK 20 — Stability
Sample A → stable  
Sample B → mixed  
Sample C → divergent

TASK 21 — First divergent stability
Correct answer: Sample C

--------------------------------------------------------------------
SECTION 12 — RTT3_INTEGRATION_EMISSION_PACKET
--------------------------------------------------------------------

TASK 22 — Packet for Sample C

integration: INT(2.4, 1.8, 1.3)  
emission: FFF(fracture)  
continuity: MAN(FI, EM, R)  
collapse_recovery: CRE(CAV-dominant)  
stability: CSL(divergent)  
canon_scale_emission: CET(fracture-weighted or recovery-weighted)  
mode: inversion-adjacent  
zone: X  

Instructor note:
  CET weighting must reflect emission curvature + stability.

====================================================================
PART 3 — FULL PIPELINE SYNTHESIS
====================================================================

--------------------------------------------------------------------
SECTION 13 — CROSS‑LAYER MAPPING
--------------------------------------------------------------------

TASK 23 — SDE → SIE mapping (Sample C)

CPV → INT:  
  High amplitude + high curvature + high torsion → strong triad integration

FGT → TIF:  
  Triad-weighted gradient → triad-dominant integration field

CRM → MAN:  
  Continuity fracture → FI + EM + R axes active

--------------------------------------------------------------------
SECTION 14 — PROJECTION (TEL / FFT / OP)
--------------------------------------------------------------------

TASK 24 — Correct projection for Sample C
Correct answer: FFT::OUT()

Reason:
  - fracture-dominant emission  
  - high torsion  
  - divergent stability  
  - inversion-adjacent regime  
  → spectral projection

TASK 25 — Justification
Any explanation referencing:
  - emission curvature  
  - torsion  
  - divergence  
  - regime identity  
earns full credit.

--------------------------------------------------------------------
SECTION 15 — COMPLETE OPERATOR CHAIN
--------------------------------------------------------------------

TASK 26 — Full operator chain (Sample C)

RTT/1 primitives  
  → SDE::CPV(2.4, 1.8, 1.3)  
  → SDE::FGT(triad-weighted)  
  → SDE::CRM(continuity fracture)  
  → SDE::MODE(inversion)  
  → SIE::INT(2.4, 1.8, 1.3)  
  → SIE::TIF(triad-dominant)  
  → SIE::MAN(FI, EM, R)  
  → SIE::FFF(fracture)  
  → SIE::CRE(CAV-dominant)  
  → SIE::CSL(divergent)  
  → SIE::CET(fracture-weighted)  
  → FFT::OUT()  

Instructor note:
  Structural coherence > exact wording.

--------------------------------------------------------------------
END OF INSTRUCTOR VERSION — COMBINED LAB
--------------------------------------------------------------------
```
