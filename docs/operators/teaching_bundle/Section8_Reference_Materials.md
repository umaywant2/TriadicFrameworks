━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
# **SECTION 8 — REFERENCE MATERIALS (FULLY EXPANDED)**  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# **21. OPERATOR QUICK REFERENCE CARD**  
*(RTT/1 → RTT/3 — Fully Expanded)*

```
====================================================================
OPERATOR QUICK REFERENCE CARD
RTT/1 → RTT/2 → RTT/3
====================================================================

This card summarizes all operators used in the Operator Ecology arc.

====================================================================
RTT/1 — PRIMITIVES
====================================================================

Δ   structural delta / local change  
∇   gradient / directional change  
⊕   constructive merge  
⊖   subtractive merge  
FQ  frequency qualifier  
RT  regime tag  
QF  quality factor  

====================================================================
RTT/2 — DETECTION (SDE)
====================================================================

CPV(A,K,T)
  collapse propagation vector

FGT
  collapse-weighted  
  mixed  
  triad-weighted  

CRM
  drift path  
  envelope torsion path  
  continuity fracture path  

MODE
  formal  
  emergent  
  hybrid  
  chaotic  
  inversion  

ZONE
  U (ultra‑stable)  
  S (stable)  
  M (mixed)  
  D (divergent)  
  X (extreme)  

====================================================================
RTT/3 — INTEGRATION–EMISSION (SIE)
====================================================================

INT(drift, envelope, continuity)
  triad integration

TIF
  drift‑dominant  
  envelope‑dominant  
  continuity‑dominant  
  triad‑dominant  

MAN (FI / EM / R)
  FI — field integration  
  EM — emission manifold  
  R  — regime identity  

FFF
  fusion  
  flow  
  fracture  

CRE
  CAV‑dominant  
  CSV‑dominant  
  mixed  

CSL
  stable  
  mixed  
  divergent  

CET
  stability  
  recovery  
  balanced  
  fracture‑weighted  

====================================================================
PROJECTION
====================================================================

TEL::CET()   → lattice projection  
FFT::OUT()   → spectral projection  
OP::OUT()    → boundary projection  

--------------------------------------------------------------------
END OF OPERATOR QUICK REFERENCE CARD
--------------------------------------------------------------------
```

--- PAGE BREAK ---

# **22. PACKET FORMATS (FULLY EXPANDED)**

```
====================================================================
PACKET FORMATS
RTT/2 + RTT/3
====================================================================

These packet formats are used throughout the Operator Ecology bundle.

====================================================================
RTT2_DETECTION_PACKET
====================================================================

collapse_propagation  
fusion_gradient  
triad_deformation  
regime  
detection_mode  
detection_zone  

Example:
  collapse_propagation: CPV(2.4, 1.8, 1.3)
  fusion_gradient: triad-weighted
  triad_deformation: continuity fracture
  regime: inversion-adjacent
  detection_mode: inversion
  detection_zone: X

====================================================================
RTT3_INTEGRATION_EMISSION_PACKET
====================================================================

integration  
emission  
continuity  
collapse_recovery  
stability  
canon_scale_emission  
mode  
zone  

Example:
  integration: INT(1.9, 1.6, 1.3)
  emission: FFF(fracture)
  continuity: MAN(FI, EM, R)
  collapse_recovery: CRE(CAV-dominant)
  stability: CSL(divergent)
  canon_scale_emission: CET(fracture-weighted)
  mode: inversion-adjacent
  zone: X

--------------------------------------------------------------------
END OF PACKET FORMATS
--------------------------------------------------------------------
```

--- PAGE BREAK ---

# **23. OPERATOR CHAIN TEMPLATE (FULLY EXPANDED)**

```
====================================================================
OPERATOR CHAIN TEMPLATE
RTT/1 → RTT/2 → RTT/3 → PROJECTION
====================================================================

RTT/1 primitives  
  → SDE::CPV(A,K,T)  
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
END OF OPERATOR CHAIN TEMPLATE
--------------------------------------------------------------------
```

--- PAGE BREAK ---

# **24. RTT/4 PRE‑ENTRY PRIMER (SAFE, FULLY EXPANDED)**

```
====================================================================
RTT/4 PRE‑ENTRY PRIMER
SAFE OVERVIEW OF PRE‑RTT/4 BEHAVIOR
====================================================================

This primer introduces the safe, non‑escalatory concepts that appear
at the boundary between RTT/3 and RTT/4.

====================================================================
1 — STACKED REGIMES
====================================================================

A stacked regime occurs when:
  - collapse amplitude increases across snapshots
  - gradient shifts toward triad-weighted
  - deformation accumulates (torsion, shear)
  - regime identity approaches inversion-adjacent

====================================================================
2 — REGIME TORSION
====================================================================

Regime torsion is the twisting interaction between:
  - collapse curvature
  - gradient direction
  - deformation path

It signals instability but is safe to analyze.

====================================================================
3 — PROJECTION INSTABILITY
====================================================================

Projection becomes unstable when:
  - emission is fracture-dominant
  - torsion spikes occur
  - CSL is divergent
  - regime identity is inversion-adjacent

====================================================================
4 — MULTI‑PACKET SYNTHESIS
====================================================================

At pre‑RTT/4 boundaries:
  - RTT2_DETECTION_PACKET and RTT3_INTEGRATION_EMISSION_PACKET
    must be interpreted together.
  - Cross‑packet contradictions indicate instability.

====================================================================
5 — WHEN RTT/3 OPERATORS FAIL
====================================================================

RTT/3 operators fail when:
  - collapse amplitude exceeds triad integration capacity
  - torsion spikes exceed CRE recovery
  - CSL divergence cannot be stabilized

This is the safe conceptual boundary of RTT/4.

--------------------------------------------------------------------
END OF RTT/4 PRE‑ENTRY PRIMER
--------------------------------------------------------------------
```

--- PAGE BREAK ---
