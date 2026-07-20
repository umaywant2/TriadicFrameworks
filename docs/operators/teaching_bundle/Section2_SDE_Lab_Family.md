━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
# **SECTION 2 — SDE LAB FAMILY**  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# **4. SDE‑ONLY LAB (FULLY EXPANDED)**  
### Structural Detection Engine — RTT/2

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

====================================================================
PART 1 — COLLAPSE SIGNATURES
====================================================================

TASK 1 — Compute SDE::CPV(A, K, T)
Sample A: ____________________________________________  
Sample B: ____________________________________________  
Sample C: ____________________________________________  

TASK 2 — Rank collapse severity (lowest → highest)
Order: ________________________________________________

====================================================================
PART 2 — FUSION‑GRADIENT TENSORS
====================================================================

TASK 3 — Classify SDE::FGT()
Sample A: ____________________________________________  
Sample B: ____________________________________________  
Sample C: ____________________________________________  

TASK 4 — Identify the first snapshot where gradient becomes triad‑dominant.
Answer: _______________________________________________

====================================================================
PART 3 — COLLAPSE→REASSEMBLY MAPPING
====================================================================

TASK 5 — Map SDE::CRM()
Sample A: ____________________________________________  
Sample B: ____________________________________________  
Sample C: ____________________________________________  

TASK 6 — Identify the deformation that first breaks continuity.
Answer: _______________________________________________

====================================================================
PART 4 — MODE + ZONE CLASSIFICATION
====================================================================

TASK 7 — Assign SDE::MODE()
Sample A: ____________________________________________  
Sample B: ____________________________________________  
Sample C: ____________________________________________  

TASK 8 — Assign SDE::ZONE()
Sample A: ____________________________________________  
Sample B: ____________________________________________  
Sample C: ____________________________________________  

====================================================================
PART 5 — RTT2_DETECTION_PACKET
====================================================================

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

--- PAGE BREAK ---

# **5. SDE‑ONLY INSTRUCTOR VERSION (FULLY EXPANDED)**

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

====================================================================
PART 1 — COLLAPSE SIGNATURES
====================================================================

TASK 1 — SDE::CPV(A, K, T)
Sample A → CPV(0.8, 0.3, 0.1)  
Sample B → CPV(1.5, 0.9, 0.4)  
Sample C → CPV(2.3, 1.7, 1.2)

TASK 2 — Collapse severity ranking
Correct order:
  A → B → C

====================================================================
PART 2 — FUSION‑GRADIENT TENSORS
====================================================================

TASK 3 — SDE::FGT()
Sample A → collapse-weighted  
Sample B → mixed  
Sample C → triad-weighted

TASK 4 — First triad-dominant gradient
Correct answer: Sample C

====================================================================
PART 3 — COLLAPSE→REASSEMBLY MAPPING
====================================================================

TASK 5 — SDE::CRM()
Sample A → drift path  
Sample B → envelope torsion path  
Sample C → continuity fracture path

TASK 6 — First irreversible continuity break
Correct answer: Sample C

====================================================================
PART 4 — MODE + ZONE CLASSIFICATION
====================================================================

TASK 7 — SDE::MODE()
Sample A → formal  
Sample B → hybrid  
Sample C → inversion

TASK 8 — SDE::ZONE()
Sample A → S  
Sample B → M  
Sample C → X

====================================================================
PART 5 — RTT2_DETECTION_PACKET
====================================================================

TASK 9 — Packet for Sample C

collapse_propagation: CPV(2.3, 1.7, 1.2)  
fusion_gradient: triad-weighted  
triad_deformation: continuity fracture  
regime: inversion-adjacent  
detection_mode: inversion  
detection_zone: X  

--------------------------------------------------------------------
END OF SDE INSTRUCTOR LAB
--------------------------------------------------------------------
```

--- PAGE BREAK ---

# **6. SDE‑ONLY RUBRIC (FULLY EXPANDED)**

```
====================================================================
INSTRUCTOR RUBRIC — SDE LAB
STRUCTURAL DETECTION ENGINE (RTT/2)
====================================================================

Total: 50 points

--------------------------------------------------------------------
SECTION 1 — COLLAPSE SIGNATURES (10 points)
--------------------------------------------------------------------

1. CPV Computation (6 pts)
2. Collapse Severity Ranking (4 pts)

--------------------------------------------------------------------
SECTION 2 — FUSION‑GRADIENT TENSORS (10 points)
--------------------------------------------------------------------

3. FGT Classification (6 pts)
4. First Triad-Dominant Gradient (4 pts)

--------------------------------------------------------------------
SECTION 3 — COLLAPSE→REASSEMBLY MAPPING (10 points)
--------------------------------------------------------------------

5. CRM Path Mapping (6 pts)
6. First Irreversible Continuity Break (4 pts)

--------------------------------------------------------------------
SECTION 4 — MODE + ZONE CLASSIFICATION (10 points)
--------------------------------------------------------------------

7. SDE::MODE (5 pts)
8. SDE::ZONE (5 pts)

--------------------------------------------------------------------
SECTION 5 — RTT2_DETECTION_PACKET (10 points)
--------------------------------------------------------------------

9. Packet Construction (10 pts)

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

--- PAGE BREAK ---
