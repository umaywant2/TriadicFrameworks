# 🟣 **SDE‑ONLY LAB — INSTRUCTOR VERSION**  
### Structural Detection Engine (RTT/2)  
*(Print‑ready, text‑only)*

```
====================================================================
INSTRUCTOR VERSION — SDE LAB
STRUCTURAL DETECTION ENGINE (RTT/2)
====================================================================

This instructor version provides:
  - Correct structural answers
  - Acceptable variations
  - Notes for grading consistency

--------------------------------------------------------------------
SAMPLE DATA (REPEATED)
--------------------------------------------------------------------

Sample A:
  A=0.8, K=0.3, T=0.1
  gradient: collapse-weighted
  deformation: drift deformation
  regime: slow-relaxation

Sample B:
  A=1.5, K=0.9, T=0.4
  gradient: mixed collapse/reassembly
  deformation: envelope torsion
  regime: mixed

Sample C:
  A=2.3, K=1.7, T=1.2
  gradient: triad-weighted
  deformation: continuity fracture
  regime: inversion-adjacent

--------------------------------------------------------------------
PART 1 — COLLAPSE SIGNATURES
--------------------------------------------------------------------

TASK 1 — SDE::CPV(A, K, T)
Sample A → CPV(0.8, 0.3, 0.1)  
Sample B → CPV(1.5, 0.9, 0.4)  
Sample C → CPV(2.3, 1.7, 1.2)

Instructor note:
  Any equivalent tuple earns full credit.

TASK 2 — Rank collapse severity
Correct order:
  A → B → C

--------------------------------------------------------------------
PART 2 — FUSION‑GRADIENT TENSORS
--------------------------------------------------------------------

TASK 3 — SDE::FGT()
Sample A → collapse-weighted  
Sample B → mixed  
Sample C → triad-weighted

TASK 4 — First triad-dominant gradient
Answer: Sample C

--------------------------------------------------------------------
PART 3 — COLLAPSE→REASSEMBLY MAPPING
--------------------------------------------------------------------

TASK 5 — SDE::CRM()
Sample A → drift path  
Sample B → envelope torsion path  
Sample C → continuity fracture path

TASK 6 — First irreversible continuity break
Answer: Sample C

--------------------------------------------------------------------
PART 4 — MODE + ZONE CLASSIFICATION
--------------------------------------------------------------------

TASK 7 — SDE::MODE()
Sample A → formal  
Sample B → hybrid  
Sample C → inversion

TASK 8 — SDE::ZONE()
Sample A → S  
Sample B → M  
Sample C → X

--------------------------------------------------------------------
PART 5 — RTT2_DETECTION_PACKET
--------------------------------------------------------------------

TASK 9 — Packet for Sample C

collapse_propagation: CPV(2.3, 1.7, 1.2)  
fusion_gradient: triad-weighted  
triad_deformation: continuity fracture  
regime: inversion-adjacent  
detection_mode: inversion  
detection_zone: X  

Instructor note:
  Must be internally consistent.

--------------------------------------------------------------------
END OF SDE INSTRUCTOR LAB
--------------------------------------------------------------------
```

---

# 🟣 **SIE‑ONLY LAB — INSTRUCTOR VERSION**  
### Structural Integration Engine (RTT/3)  
*(Print‑ready, text‑only)*

```
====================================================================
INSTRUCTOR VERSION — SIE LAB
STRUCTURAL INTEGRATION ENGINE (RTT/3)
====================================================================

This instructor version provides:
  - Correct structural answers
  - Acceptable variations
  - Notes for grading consistency

--------------------------------------------------------------------
SAMPLE DATA (REPEATED)
--------------------------------------------------------------------

Sample A:
  drift=0.9, envelope=0.4, continuity=0.7
  deformation: drift deformation
  collapse: low amplitude, low torsion

Sample B:
  drift=1.3, envelope=1.0, continuity=0.6
  deformation: envelope torsion
  collapse: medium amplitude, medium torsion

Sample C:
  drift=2.1, envelope=1.8, continuity=1.4
  deformation: continuity fracture
  collapse: high amplitude, high torsion

--------------------------------------------------------------------
PART 1 — TRIAD INTEGRATION
--------------------------------------------------------------------

TASK 1 — SIE::INT()
Sample A → INT(0.9, 0.4, 0.7)  
Sample B → INT(1.3, 1.0, 0.6)  
Sample C → INT(2.1, 1.8, 1.4)

TASK 2 — Strongest integration field
Answer: Sample C

--------------------------------------------------------------------
PART 2 — TRIADIC INTEGRATION FIELD (TIF)
--------------------------------------------------------------------

TASK 3 — Dominant components
Sample A → drift-dominant  
Sample B → drift + envelope balanced  
Sample C → triad-dominant

TASK 4 — First triad-dominant sample
Answer: Sample C

--------------------------------------------------------------------
PART 3 — INTEGRATION–EMISSION MANIFOLD (MAN)
--------------------------------------------------------------------

TASK 5 — Active axes
Sample A → FI  
Sample B → FI + EM  
Sample C → FI + EM + R

TASK 6 — First regime-dominant sample
Answer: Sample C

--------------------------------------------------------------------
PART 4 — EMISSION (FFF)
--------------------------------------------------------------------

TASK 7 — Emission type
Sample A → fusion  
Sample B → flow  
Sample C → fracture

TASK 8 — First fracture-dominant emission
Answer: Sample C

--------------------------------------------------------------------
PART 5 — COLLAPSE→RECOVERY ENGINE (CRE)
--------------------------------------------------------------------

TASK 9 — CAV / CSV / mixed
Sample A → CSV-dominant  
Sample B → mixed  
Sample C → CAV-dominant

TASK 10 — Strongest CRE intervention
Answer: Sample C

--------------------------------------------------------------------
PART 6 — CONTINUITY–STABILITY LAYER (CSL)
--------------------------------------------------------------------

TASK 11 — Stability
Sample A → stable  
Sample B → mixed  
Sample C → divergent

TASK 12 — First divergent stability
Answer: Sample C

--------------------------------------------------------------------
PART 7 — RTT3_INTEGRATION_EMISSION_PACKET
--------------------------------------------------------------------

TASK 13 — Packet for Sample C

integration: INT(2.1, 1.8, 1.4)  
emission: FFF(fracture)  
continuity: MAN(FI, EM, R)  
collapse_recovery: CRE(CAV-dominant)  
stability: CSL(divergent)  
canon_scale_emission: CET(fracture-weighted or recovery-weighted)  
mode: inversion-adjacent  
zone: X  

Instructor note:
  CET weighting must match emission + stability.

--------------------------------------------------------------------
END OF SIE INSTRUCTOR LAB
--------------------------------------------------------------------
```
