# 🟣 **SDE‑ONLY LAB — INSTRUCTOR RUBRIC**  
### Structural Detection Engine (RTT/2)  
*(Print‑ready, text‑only)*

```
====================================================================
INSTRUCTOR RUBRIC — SDE LAB
STRUCTURAL DETECTION ENGINE (RTT/2)
====================================================================

This rubric evaluates student mastery of RTT/2 detection:
  - collapse signatures
  - fusion‑gradient tensors
  - collapse→reassembly mapping
  - mode + zone classification
  - RTT2_DETECTION_PACKET construction

Total: 50 points

--------------------------------------------------------------------
SECTION 1 — COLLAPSE SIGNATURES (10 points)
--------------------------------------------------------------------

1. CPV Computation (6 pts)
   - Correct extraction of A, K, T for all samples (2 pts each)
   - Minor formatting differences allowed

2. Collapse Severity Ranking (4 pts)
   - Correct order: A → B → C
   - Partial credit for correct reasoning but incorrect order

--------------------------------------------------------------------
SECTION 2 — FUSION‑GRADIENT TENSORS (10 points)
--------------------------------------------------------------------

3. FGT Classification (6 pts)
   - A: collapse-weighted
   - B: mixed
   - C: triad-weighted

4. First Triad-Dominant Gradient (4 pts)
   - Correct answer: Sample C

--------------------------------------------------------------------
SECTION 3 — COLLAPSE→REASSEMBLY MAPPING (10 points)
--------------------------------------------------------------------

5. CRM Path Mapping (6 pts)
   - A: drift path
   - B: envelope torsion path
   - C: continuity fracture path

6. First Irreversible Continuity Break (4 pts)
   - Correct answer: Sample C

--------------------------------------------------------------------
SECTION 4 — MODE + ZONE CLASSIFICATION (10 points)
--------------------------------------------------------------------

7. SDE::MODE (5 pts)
   - A: formal
   - B: hybrid
   - C: inversion

8. SDE::ZONE (5 pts)
   - A: S
   - B: M
   - C: X

--------------------------------------------------------------------
SECTION 5 — RTT2_DETECTION_PACKET (10 points)
--------------------------------------------------------------------

9. Packet Construction (10 pts)
   Must include:
     - collapse_propagation
     - fusion_gradient
     - triad_deformation
     - regime
     - detection_mode
     - detection_zone
   - Full credit for internal consistency
   - Partial credit for missing fields but correct structure

--------------------------------------------------------------------
SCORING GUIDE
--------------------------------------------------------------------

45–50: Mastery  
35–44: Proficient  
25–34: Developing  
0–24: Needs Support

--------------------------------------------------------------------
END OF SDE RUBRIC
--------------------------------------------------------------------
```
