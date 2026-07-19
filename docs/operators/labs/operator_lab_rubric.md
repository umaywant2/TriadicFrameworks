# INSTRUCTOR RUBRIC — OPERATOR LAB  
RTT/1 → RTT/2 → RTT/3  
(Printable, text‑only)

```
====================================================================
INSTRUCTOR RUBRIC — OPERATOR LAB
RTT/1 + RTT/2 + RTT/3 OPERATOR ECOLOGY
====================================================================

This rubric evaluates student mastery across the full operator chain:
  RTT/1 primitives
  RTT/2 detection (SDE)
  RTT/3 integration–emission (SIE)
  projection (TEL / FFT / OP)

Scoring is structural, not semantic.  
Any internally consistent operator chain earns full credit.

Total: 100 points

--------------------------------------------------------------------
SECTION 1 — RTT/1 FOUNDATIONS (15 points)
--------------------------------------------------------------------

1. Primitive Identification (5 pts)
   - Correct mapping of ∇, Δ, ⊕, ⊖, FQ, RT, QF
   - Partial credit for structurally consistent reasoning

2. Regime Assignment (5 pts)
   - Correct REG::ID for each sample
   - Accept slow-relaxation, mixed, inversion-adjacent, etc.

3. Continuity Classification (5 pts)
   - Correct C0 / C1 / C∞ classification
   - Must justify using deformation + gradient

--------------------------------------------------------------------
SECTION 2 — RTT/2 DETECTION (SDE) (30 points)
--------------------------------------------------------------------

4. CPV Computation (5 pts)
   - Correct extraction of amplitude, curvature, torsion
   - Must use SDE::CPV(A, K, T)

5. FGT Classification (5 pts)
   - collapse-weighted, mixed, triad-weighted
   - Must match sample gradient descriptions

6. CRM Path Mapping (5 pts)
   - drift → envelope torsion → continuity fracture
   - Accept any structurally consistent mapping

7. MODE + ZONE Assignment (5 pts)
   - Correct mode (formal/emergent/hybrid/chaotic/inversion)
   - Correct zone (U/S/M/D/X)

8. RTT2_DETECTION_PACKET (10 pts)
   - Includes all required fields:
       collapse_propagation
       fusion_gradient
       triad_deformation
       regime
       detection_mode
       detection_zone
   - Must be internally consistent

--------------------------------------------------------------------
SECTION 3 — RTT/3 INTEGRATION–EMISSION (SIE) (35 points)
--------------------------------------------------------------------

9. Triad Integration (5 pts)
   - Correct SIE::INT(drift, envelope, continuity)

10. TIF Application (5 pts)
   - Identifies dominant integration components
   - Accept drift-dominant, envelope-dominant, triad-dominant

11. MAN Axes (5 pts)
   - Correct identification of FI, EM, R axes

12. FFF Emission Type (5 pts)
   - fusion / fracture / flow
   - Must match deformation + torsion

13. CRE Path (5 pts)
   - CAV-dominant / CSV-dominant / mixed
   - Must match collapse signature

14. CSL Stability (5 pts)
   - stable / mixed / divergent
   - Must match torsion + emission curvature

15. RTT3_INTEGRATION_EMISSION_PACKET (5 pts)
   - Includes:
       integration
       emission
       continuity
       collapse_recovery
       stability
       canon_scale_emission
       mode
       zone
   - Must be structurally coherent

--------------------------------------------------------------------
SECTION 4 — PROJECTION (TEL / FFT / OP) (10 points)
--------------------------------------------------------------------

16. Projection Selection (5 pts)
   - TEL → lattice behavior
   - FFT → spectral behavior
   - OP → boundary behavior
   - Must match emission curvature + stability + regime

17. Projection Justification (5 pts)
   - Must reference:
       emission curvature
       stability
       recovery weighting
       regime identity

--------------------------------------------------------------------
SECTION 5 — FULL OPERATOR CHAIN (10 points)
--------------------------------------------------------------------

18. Complete Operator Chain (10 pts)
   - Must include all steps:
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
   - Minor variations allowed if structurally correct

--------------------------------------------------------------------
SCORING GUIDE
--------------------------------------------------------------------

90–100: Mastery  
  - Full structural correctness
  - Clear operator reasoning
  - Accurate packet construction

75–89: Proficient  
  - Mostly correct operator chains
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
END OF RUBRIC
--------------------------------------------------------------------
```
