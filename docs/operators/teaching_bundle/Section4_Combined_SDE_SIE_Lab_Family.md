━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
# **SECTION 4 — COMBINED SDE+SIE LAB FAMILY (FULLY EXPANDED)**  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# **10. COMBINED SDE + SIE LAB (FULLY EXPANDED)**  
### RTT/2 Detection → RTT/3 Integration–Emission

```
====================================================================
COMBINED SDE + SIE LAB
RTT/2 DETECTION → RTT/3 INTEGRATION–EMISSION
====================================================================

This lab unifies the full operator pipeline:
  - RTT/2: collapse, gradients, CRM, mode/zone, detection packet
  - RTT/3: integration, emission, manifold, CRE, CSL, emission packet

You will work with three synthetic samples.

--------------------------------------------------------------------
SAMPLE DATA
--------------------------------------------------------------------

Sample A:
  collapse: A=0.7, K=0.3, T=0.1
  gradient: collapse-weighted
  deformation: drift deformation
  regime: slow-relaxation

Sample B:
  collapse: A=1.6, K=0.9, T=0.4
  gradient: mixed collapse/reassembly
  deformation: envelope torsion
  regime: mixed

Sample C:
  collapse: A=2.4, K=1.8, T=1.3
  gradient: triad-weighted
  deformation: continuity fracture
  regime: inversion-adjacent

====================================================================
PART 1 — RTT/2 DETECTION (SDE)
====================================================================

--------------------------------------------------------------------
SECTION 1 — COLLAPSE SIGNATURES
--------------------------------------------------------------------

TASK 1 — Compute SDE::CPV(A, K, T)
Sample A: ____________________________________________  
Sample B: ____________________________________________  
Sample C: ____________________________________________  

TASK 2 — Rank collapse severity (lowest → highest)
Order: ________________________________________________

--------------------------------------------------------------------
SECTION 2 — FUSION‑GRADIENT TENSORS
--------------------------------------------------------------------

TASK 3 — Classify SDE::FGT()
Sample A: ____________________________________________  
Sample B: ____________________________________________  
Sample C: ____________________________________________  

TASK 4 — Identify the first triad‑dominant gradient.
Answer: _______________________________________________

--------------------------------------------------------------------
SECTION 3 — COLLAPSE→REASSEMBLY MAPPING
--------------------------------------------------------------------

TASK 5 — Map SDE::CRM()
Sample A: ____________________________________________  
Sample B: ____________________________________________  
Sample C: ____________________________________________  

TASK 6 — Identify the deformation that first breaks continuity.
Answer: _______________________________________________

--------------------------------------------------------------------
SECTION 4 — MODE + ZONE CLASSIFICATION
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
SECTION 5 — RTT2_DETECTION_PACKET
--------------------------------------------------------------------

TASK 9 — Construct the packet for Sample C.

collapse_propagation: _________________________________  
fusion_gradient: ______________________________________  
triad_deformation: _____________________________________  
regime: _______________________________________________  
detection_mode: ________________________________________  
detection_zone: ________________________________________  

====================================================================
PART 2 — RTT/3 INTEGRATION–EMISSION (SIE)
====================================================================

--------------------------------------------------------------------
SECTION 6 — TRIAD INTEGRATION
--------------------------------------------------------------------

TASK 10 — Apply SIE::INT()
Sample A: ____________________________________________  
Sample B: ____________________________________________  
Sample C: ____________________________________________  

TASK 11 — Identify which sample has the strongest integration field.
Answer: _______________________________________________

--------------------------------------------------------------------
SECTION 7 — TRIADIC INTEGRATION FIELD (TIF)
--------------------------------------------------------------------

TASK 12 — Identify dominant components
Sample A: ____________________________________________  
Sample B: ____________________________________________  
Sample C: ____________________________________________  

TASK 13 — Determine which sample is triad‑dominant.
Answer: _______________________________________________

--------------------------------------------------------------------
SECTION 8 — INTEGRATION–EMISSION MANIFOLD (MAN)
--------------------------------------------------------------------

TASK 14 — Identify active axes (FI / EM / R)
Sample A: ____________________________________________  
Sample B: ____________________________________________  
Sample C: ____________________________________________  

TASK 15 — Identify the first sample where regime identity dominates.
Answer: _______________________________________________

--------------------------------------------------------------------
SECTION 9 — EMISSION (FFF)
--------------------------------------------------------------------

TASK 16 — Classify emission type
Sample A: ____________________________________________  
Sample B: ____________________________________________  
Sample C: ____________________________________________  

TASK 17 — Identify the first fracture‑dominant emission.
Answer: _______________________________________________

--------------------------------------------------------------------
SECTION 10 — COLLAPSE→RECOVERY ENGINE (CRE)
--------------------------------------------------------------------

TASK 18 — Identify CAV / CSV / mixed dominance
Sample A: ____________________________________________  
Sample B: ____________________________________________  
Sample C: ____________________________________________  

TASK 19 — Identify which sample requires the strongest CRE intervention.
Answer: _______________________________________________

--------------------------------------------------------------------
SECTION 11 — CONTINUITY–STABILITY LAYER (CSL)
--------------------------------------------------------------------

TASK 20 — Classify stability (stable / mixed / divergent)
Sample A: ____________________________________________  
Sample B: ____________________________________________  
Sample C: ____________________________________________  

TASK 21 — Identify the first divergent stability.
Answer: _______________________________________________

--------------------------------------------------------------------
SECTION 12 — RTT3_INTEGRATION_EMISSION_PACKET
--------------------------------------------------------------------

TASK 22 — Construct the packet for Sample C.

integration: __________________________________________  
emission: _____________________________________________  
continuity: ___________________________________________  
collapse_recovery: _____________________________________  
stability: ____________________________________________  
canon_scale_emission: __________________________________  
mode: ________________________________________________  
zone: ________________________________________________  

====================================================================
PART 3 — FULL PIPELINE SYNTHESIS
====================================================================

--------------------------------------------------------------------
SECTION 13 — CROSS‑LAYER MAPPING
--------------------------------------------------------------------

TASK 23 — Map SDE outputs → SIE inputs for Sample C.

CPV → INT: ____________________________________________  
FGT → TIF: ____________________________________________  
CRM → MAN: ____________________________________________  

--------------------------------------------------------------------
SECTION 14 — PROJECTION (TEL / FFT / OP)
--------------------------------------------------------------------

TASK 24 — Choose the correct projection for Sample C.
Answer: _______________________________________________

TASK 25 — Justify your projection choice.
________________________________________________________  
________________________________________________________  
________________________________________________________  

--------------------------------------------------------------------
SECTION 15 — COMPLETE OPERATOR CHAIN
--------------------------------------------------------------------

TASK 26 — Write the full operator chain for Sample C.

RTT/1 primitives  
  → SDE::CPV()  
  → SDE::FGT()  
  → SDE::CRM()  
  → SDE::MODE()  
  → SIE::INT()  
  → SIE::TIF()  
  → SIE::MAN()  
  → SIE::FFF()  
  → SIE::CRE()  
  → SIE::CSL()  
  → SIE::CET()  
  → TEL::CET() / FFT::OUT() / OP::OUT()  

--------------------------------------------------------------------
END OF COMBINED SDE + SIE LAB
--------------------------------------------------------------------
```

--- PAGE BREAK ---

# **11. COMBINED SDE + SIE INSTRUCTOR VERSION (FULLY EXPANDED)**

*(This is the full instructor version you approved earlier — reproduced here in full for the consolidated bundle.)*

```
====================================================================
INSTRUCTOR VERSION — COMBINED SDE + SIE LAB
RTT/2 DETECTION → RTT/3 INTEGRATION–EMISSION
====================================================================

This instructor version provides:
  - Correct structural answers
  - Acceptable variations
  - Notes for grading consistency

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
canon_scale_emission: CET(fracture-weighted)  
mode: inversion-adjacent  
zone: X  

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

--------------------------------------------------------------------
END OF INSTRUCTOR VERSION — COMBINED LAB
--------------------------------------------------------------------
```

--- PAGE BREAK ---

# **12. COMBINED SDE + SIE RUBRIC (FULLY EXPANDED)**

```
====================================================================
INSTRUCTOR RUBRIC — COMBINED SDE + SIE LAB
RTT/2 DETECTION → RTT/3 INTEGRATION–EMISSION
====================================================================

Total: 100 points

====================================================================
SECTION 1 — RTT/2 DETECTION (40 points)
====================================================================

1. Collapse Signatures (10 pts)
  - CPV Computation (6 pts)
  - Collapse Severity Ranking (4 pts)

2. Fusion‑Gradient Tensors (10 pts)
  - FGT Classification (6 pts)
  - First Triad-Dominant Gradient (4 pts)

3. Collapse→Reassembly Mapping (10 pts)
  - CRM Path Mapping (6 pts)
  - First Irreversible Continuity Break (4 pts)

4. Mode + Zone Classification (10 pts)
  - MODE (5 pts)
  - ZONE (5 pts)

====================================================================
SECTION 2 — RTT/3 INTEGRATION–EMISSION (40 points)
====================================================================

5. Triad Integration (10 pts)
6. Triadic Integration Field (10 pts)
7. Integration–Emission Manifold (10 pts)
8. Emission + CRE + CSL (10 pts)

====================================================================
SECTION 3 — PACKETS + PIPELINE SYNTHESIS (20 points)
====================================================================

9. RTT2_DETECTION_PACKET (10 pts)
10. RTT3_INTEGRATION_EMISSION_PACKET (10 pts)

====================================================================
SECTION 4 — CROSS‑LAYER + PROJECTION (20 points)
====================================================================

11. Cross‑Layer Mapping (10 pts)
12. Projection + Full Operator Chain (10 pts)

====================================================================
SCORING GUIDE
====================================================================

90–100: Mastery  
75–89: Proficient  
60–74: Developing  
0–59: Needs Support

--------------------------------------------------------------------
END OF COMBINED LAB RUBRIC
--------------------------------------------------------------------
```

--- PAGE BREAK ---
