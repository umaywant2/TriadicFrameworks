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
