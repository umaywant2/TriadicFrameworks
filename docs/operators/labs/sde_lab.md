# 🟣 **SDE‑ONLY LAB (RTT/2 Detection)**  
### Structural Detection Engine — Hands‑On Lab  
*(Print‑ready, text‑only)*

```
====================================================================
SDE LAB — STRUCTURAL DETECTION ENGINE (RTT/2)
====================================================================

This lab isolates the RTT/2 detection layer:
  - collapse signatures
  - fusion‑gradient tensors
  - collapse→reassembly mapping
  - mode + zone classification
  - RTT2_DETECTION_PACKET construction

You will work with three synthetic samples.

--------------------------------------------------------------------
SAMPLE DATA
--------------------------------------------------------------------

Sample A:
  collapse: A=0.8, K=0.3, T=0.1
  gradient: collapse-weighted
  deformation: drift deformation
  regime: slow-relaxation

Sample B:
  collapse: A=1.5, K=0.9, T=0.4
  gradient: mixed collapse/reassembly
  deformation: envelope torsion
  regime: mixed

Sample C:
  collapse: A=2.3, K=1.7, T=1.2
  gradient: triad-weighted
  deformation: continuity fracture
  regime: inversion-adjacent

--------------------------------------------------------------------
PART 1 — COLLAPSE SIGNATURES
--------------------------------------------------------------------

TASK 1 — Compute SDE::CPV(A, K, T)
Sample A: ____________________________________________  
Sample B: ____________________________________________  
Sample C: ____________________________________________  

TASK 2 — Rank collapse severity (lowest → highest)
Order: ________________________________________________

--------------------------------------------------------------------
PART 2 — FUSION‑GRADIENT TENSORS
--------------------------------------------------------------------

TASK 3 — Classify SDE::FGT()
Sample A: ____________________________________________  
Sample B: ____________________________________________  
Sample C: ____________________________________________  

TASK 4 — Identify the first snapshot where gradient becomes triad‑dominant.
Answer: _______________________________________________

--------------------------------------------------------------------
PART 3 — COLLAPSE→REASSEMBLY MAPPING
--------------------------------------------------------------------

TASK 5 — Map SDE::CRM()
Sample A: ____________________________________________  
Sample B: ____________________________________________  
Sample C: ____________________________________________  

TASK 6 — Identify the deformation that first breaks continuity.
Answer: _______________________________________________

--------------------------------------------------------------------
PART 4 — MODE + ZONE CLASSIFICATION
--------------------------------------------------------------------

TASK 7 — Assign SDE::MODE()
Sample A: ____________________________________________  
Sample B: ____________________________________________  
Sample C: ____________________________________________  

TASK 8 — Assign SDE::ZONE()
Sample A: ____________________________________________  
Sample B: ____________________________________________  
Sample C: ____________________________________________  

--------------------------------------------------------------------
PART 5 — RTT2_DETECTION_PACKET
--------------------------------------------------------------------

TASK 9 — Construct the packet for Sample C.

collapse_propagation: _________________________________  
fusion_gradient: ______________________________________  
triad_deformation: _____________________________________  
regime: _______________________________________________  
detection_mode: ________________________________________  
detection_zone: ________________________________________  

--------------------------------------------------------------------
END OF SDE LAB
--------------------------------------------------------------------
```
