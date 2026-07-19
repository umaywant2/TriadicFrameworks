# Philanthropy API  
## Operator‑Level Interface (RTT/1)

This document defines the callable operators used in the **Philanthropy & Funding Transparency** module.  
All operators follow RTT grammar and integrate with SET load, governance substrate, drift detection, and the triadic observer.

Each operator includes:
- signature  
- description  
- inputs  
- outputs  
- structural notes  

---

# 1. Flow Operators

## **FLOW(src → dst)**
Moves funding from one node to another.

**Inputs:**  
- src (node)  
- dst (node)  
- amount (numeric)

**Outputs:**  
- updated flow state

**Notes:**  
Backbone of all philanthropic routing.

---

## **TRACE(path)**
Reveals the full funding chain.

**Inputs:**  
- ordered list of nodes

**Outputs:**  
- visibility map  
- missing segments

**Notes:**  
Used for transparency and auditability.

---

## **LEAK(node)**
Measures loss at a node.

**Inputs:**  
- node

**Outputs:**  
- leakage percentage

**Notes:**  
High leakage is a structural red indicator.

---

## **CONVERT(input → output)**
Transforms funding into outputs or outcomes.

**Inputs:**  
- input (funding)  
- output (deliverable)

**Outputs:**  
- conversion ratio

**Notes:**  
Used for outcome analysis.

---

# 2. SET Load Operators

## **SET_IN(node)**
Energy entering a node.

## **SET_OUT(node)**
Energy leaving a node.

## **SET_LEAK(node)**
Energy lost at a node.

## **SET_BAL(node)**
Efficiency ratio.

**Notes:**  
SET load is the energy model for philanthropic systems.

---

# 3. Governance Substrate Operators

## **GOV(node)**
Authority structure.

## **ACC(node)**
Accountability structure.

## **VIS(node)**
Visibility / transparency.

## **ASYM(node)**
Asymmetry of power or information.

## **OPA(node)**
Opacity level.

**Notes:**  
Weak substrate predicts drift.

---

# 4. Regime Operators

## **REG(node) = AUTH / NAR / EMO / STR**
Classifies the dominant regime.

**Notes:**  
- AUTH → authority  
- NAR → narrative  
- EMO → emotional  
- STR → structural  

---

# 5. Observer Operators

## **SIG(data)**
Extracts structural truth.

## **NOI(data)**
Extracts narrative/emotional noise.

## **CTX(node)**
Contextual metadata.

## **SYN(system)**
Synthesizes signal, noise, and regime.

**Notes:**  
Used for drift detection and alignment scoring.

---

# 6. Drift Operators

## **DRF(type)**
Detects drift.

**Types:**  
- mission  
- financial  
- governance  
- reporting  
- structural  
- regime

**Outputs:**  
- drift severity  
- drift signature

---

# 7. Alignment Operators

## **ALN(donor)**
Computes donor alignment score.

**Formula:**  
```
DAS =
  w1 * IntentClarity
+ w2 * FlowIntegrity
+ w3 * OutcomeCoherence
+ w4 * RegimeStability
```

---

## **COH(system)**
Measures coherence between flows, outcomes, and governance.

---

## **IMPACT(flow)**
Measures beneficiary‑level effect.

---

# 8. Red Indicator Operators

## **RED(flag)**
Flags structural anomalies.

**Flags:**  
- flow_break  
- opacity  
- overhead_spike  
- narrative_inflation  
- governance_asymmetry  
- leakage  

---

# 9. Correction Operators

## **FIX(node)**
Applies structural correction.

**Examples:**  
```
FIX(Foundation) → increase payout rate
FIX(Intermediary) → reduce overhead
FIX(NGO) → improve reporting clarity
```

---

# 10. API Usage Pattern

Standard RTT analysis loop:

```
1. FLOW + TRACE
2. SET_IN/OUT/LEAK/BAL
3. GOV/ACC/VIS/ASYM/OPA
4. REG + SIG/NOI/CTX/SYN
5. DRF classification
6. ALN scoring
7. FIX recommendations
```

---

# Summary

The Philanthropy API provides a complete operator‑level interface for analyzing:

- funding flows  
- governance substrate  
- SET load  
- regime patterns  
- drift  
- alignment  
- structural corrections  

All operators are minimal, composable, and fully RTT/1‑aligned.
