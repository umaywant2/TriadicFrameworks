# RUBRIC — COMBINED SDE + SIE LAB  
RTT/2 Detection → RTT/3 Integration–Emission  
(Print‑ready, text‑only)

```
====================================================================
INSTRUCTOR RUBRIC — COMBINED SDE + SIE LAB
RTT/2 DETECTION → RTT/3 INTEGRATION–EMISSION
====================================================================

This rubric evaluates mastery across the full RTT/2 → RTT/3 pipeline:
  - collapse signatures
  - fusion‑gradient tensors
  - collapse→reassembly mapping
  - mode + zone classification
  - RTT2_DETECTION_PACKET
  - triad integration
  - integration fields
  - manifold axes
  - emission classification
  - collapse→recovery stabilization
  - continuity–stability classification
  - RTT3_INTEGRATION_EMISSION_PACKET
  - cross‑layer mapping
  - projection routing
  - full operator chain

Total: 100 points

====================================================================
SECTION 1 — RTT/2 DETECTION (SDE) — 40 points
====================================================================

--------------------------------------------------------------------
1. Collapse Signatures (10 pts)
--------------------------------------------------------------------

1A. CPV Computation (6 pts)
  - Correct extraction of A, K, T for A/B/C (2 pts each)
  - Minor formatting differences allowed

1B. Collapse Severity Ranking (4 pts)
  - Correct order: A → B → C
  - Partial credit for correct reasoning but incorrect order

--------------------------------------------------------------------
2. Fusion‑Gradient Tensors (10 pts)
--------------------------------------------------------------------

2A. FGT Classification (6 pts)
  - A: collapse-weighted
  - B: mixed
  - C: triad-weighted

2B. First Triad-Dominant Gradient (4 pts)
  - Correct answer: Sample C

--------------------------------------------------------------------
3. Collapse→Reassembly Mapping (10 pts)
--------------------------------------------------------------------

3A. CRM Path Mapping (6 pts)
  - A: drift path
  - B: envelope torsion path
  - C: continuity fracture path

3B. First Irreversible Continuity Break (4 pts)
  - Correct answer: Sample C

--------------------------------------------------------------------
4. Mode + Zone Classification (10 pts)
--------------------------------------------------------------------

4A. SDE::MODE (5 pts)
  - A: formal
  - B: hybrid
  - C: inversion

4B. SDE::ZONE (5 pts)
  - A: S
  - B: M
  - C: X

====================================================================
SECTION 2 — RTT/3 INTEGRATION–EMISSION (SIE) — 40 points
====================================================================

--------------------------------------------------------------------
5. Triad Integration (10 pts)
--------------------------------------------------------------------

5A. SIE::INT() (6 pts)
  - Correct triad integration for A/B/C (2 pts each)

5B. Strongest Integration Field (4 pts)
  - Correct answer: Sample C

--------------------------------------------------------------------
6. Triadic Integration Field (TIF) (10 pts)
--------------------------------------------------------------------

6A. Dominant Components (6 pts)
  - A: drift-dominant
  - B: drift + envelope balanced
  - C: triad-dominant

6B. First Triad-Dominant Sample (4 pts)
  - Correct answer: Sample C

--------------------------------------------------------------------
7. Integration–Emission Manifold (MAN) (10 pts)
--------------------------------------------------------------------

7A. Active Axes (6 pts)
  - A: FI
  - B: FI + EM
  - C: FI + EM + R

7B. First Regime-Dominant Sample (4 pts)
  - Correct answer: Sample C

--------------------------------------------------------------------
8. Emission + CRE + CSL (10 pts)
--------------------------------------------------------------------

8A. Emission Type (3 pts)
  - A: fusion
  - B: flow
  - C: fracture

8B. CRE Dominance (3 pts)
  - A: CSV-dominant
  - B: mixed
  - C: CAV-dominant

8C. CSL Stability (3 pts)
  - A: stable
  - B: mixed
  - C: divergent

8D. First Divergent Stability (1 pt)
  - Correct answer: Sample C

====================================================================
SECTION 3 — PACKETS + PIPELINE SYNTHESIS — 20 points
====================================================================

--------------------------------------------------------------------
9. RTT2_DETECTION_PACKET (10 pts)
--------------------------------------------------------------------

Must include:
  - collapse_propagation
  - fusion_gradient
  - triad_deformation
  - regime
  - detection_mode
  - detection_zone

Scoring:
  - 10 pts: all fields present + internally consistent  
  - 7–9 pts: minor omissions  
  - 4–6 pts: partial structure  
  - 0–3 pts: incoherent or missing

--------------------------------------------------------------------
10. RTT3_INTEGRATION_EMISSION_PACKET (10 pts)
--------------------------------------------------------------------

Must include:
  - integration
  - emission
  - continuity
  - collapse_recovery
  - stability
  - canon_scale_emission
  - mode
  - zone

Scoring:
  - 10 pts: all fields present + consistent  
  - 7–9 pts: minor omissions  
  - 4–6 pts: partial structure  
  - 0–3 pts: incoherent or missing

====================================================================
SECTION 4 — CROSS‑LAYER + PROJECTION — 20 points
====================================================================

--------------------------------------------------------------------
11. Cross‑Layer Mapping (10 pts)
--------------------------------------------------------------------

Correct mapping:
  - CPV → INT (triad strength)  
  - FGT → TIF (gradient weighting → integration dominance)  
  - CRM → MAN (deformation → manifold axes)

Scoring:
  - 10 pts: all three correct  
  - 7–9 pts: two correct  
  - 4–6 pts: one correct  
  - 0–3 pts: none correct

--------------------------------------------------------------------
12. Projection + Full Operator Chain (10 pts)
--------------------------------------------------------------------

Projection:
  - Correct answer for Sample C: FFT::OUT()

Full operator chain:
  - Must include all steps from RTT/1 → SDE → SIE → Projection

Scoring:
  - 10 pts: correct projection + full chain  
  - 7–9 pts: correct projection + partial chain  
  - 4–6 pts: incorrect projection but chain mostly correct  
  - 0–3 pts: major omissions

====================================================================
SCORING GUIDE
====================================================================

90–100: Mastery  
  - Full structural correctness  
  - Accurate packet construction  
  - Strong cross‑layer reasoning  

75–89: Proficient  
  - Mostly correct  
  - Minor packet or mode/zone errors  

60–74: Developing  
  - Partial operator understanding  
  - Incomplete packet fields  
  - Projection inconsistencies  

0–59: Needs Support  
  - Major gaps in RTT/2 or RTT/3 reasoning  
  - Missing operator chains  
  - Incorrect or incoherent packet structures

--------------------------------------------------------------------
END OF COMBINED LAB RUBRIC
--------------------------------------------------------------------
```
