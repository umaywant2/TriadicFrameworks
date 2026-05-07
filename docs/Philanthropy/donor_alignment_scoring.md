# Donor Alignment Scoring — Philanthropy & Funding Transparency Module

This file defines the RTT-aligned donor alignment scoring model.  
The goal is to measure how closely a donor’s **intent**, **flows**, and **outcomes** match across the entire philanthropic chain.

This scoring model is structural, not moral.  
It evaluates alignment using RTT operators, SET load, governance substrate, and the triadic observer.

---

# 1. Purpose of Donor Alignment Scoring

Donors often have clear intentions, but the philanthropic system introduces:

- multi-layer routing  
- overhead  
- narrative distortion  
- governance asymmetry  
- incentive misalignment  
- drift at every layer  

The Donor Alignment Score (DAS) reveals:

- how much of the donor’s intent becomes real outcomes  
- where alignment is strong  
- where drift occurs  
- where structural corrections are needed  

---

# 2. Core Alignment Components

The Donor Alignment Score is built from four pillars:

1. **Intent Clarity** — what the donor wants  
2. **Flow Integrity** — how money moves  
3. **Outcome Coherence** — what actually happens  
4. **Regime Stability** — what incentives shape the flow  

Each pillar is evaluated using RTT operators.

---

# 3. Intent Clarity (INTENT)

Intent is extracted from:

- donor mission statements  
- grant agreements  
- public commitments  
- thematic priorities  
- stated values  

Operator:
```
INTENT(donor)
```

Intent clarity is high when:

- goals are specific  
- constraints are explicit  
- time horizons are defined  
- metrics are measurable  

---

# 4. Flow Integrity (FLOW + TRACE)

Flow integrity measures:

- routing transparency  
- leakage  
- overhead  
- conversion efficiency  
- governance substrate stability  

Operators:
```
FLOW(src → dst)
TRACE(path)
LEAK(node)
CONVERT(input → output)
```

Flow integrity is high when:

- routing is simple  
- leakage is low  
- overhead is justified  
- funds reach intended nodes  

---

# 5. Outcome Coherence (SIG + COH)

Outcome coherence measures:

- measurable results  
- alignment with intent  
- structural impact  
- community benefit  

Operators:
```
SIG(data)
COH(system)
IMPACT(flow)
```

Outcome coherence is high when:

- outputs match intent  
- outcomes match outputs  
- community feedback aligns with results  

---

# 6. Regime Stability (REG + DRF)

Regime stability measures:

- authority balance  
- narrative accuracy  
- emotional cycles  
- structural governance  

Operators:
```
REG(type)
DRF(type)
ASYM(node)
OPA(node)
```

Regime stability is high when:

- authority is accountable  
- narrative matches signal  
- emotional cycles do not distort flows  
- governance is transparent  

---

# 7. Donor Alignment Score (DAS)

The Donor Alignment Score is computed as:

```
DAS =
  w1 * IntentClarity
+ w2 * FlowIntegrity
+ w3 * OutcomeCoherence
+ w4 * RegimeStability
```

Where each component is normalized to 0–1.

Example:
```
DAS(DonorA) = 0.72 (strong alignment)
```

---

# 8. Component Scoring (0–1 Scale)

### **8.1 Intent Clarity**
- 0.9–1.0 → highly specific, measurable  
- 0.6–0.8 → moderately clear  
- 0.3–0.5 → vague or broad  
- 0.0–0.2 → undefined or contradictory  

---

### **8.2 Flow Integrity**
- 0.9–1.0 → minimal leakage, transparent routing  
- 0.6–0.8 → moderate leakage, clear routing  
- 0.3–0.5 → high leakage, complex routing  
- 0.0–0.2 → opaque or broken flows  

---

### **8.3 Outcome Coherence**
- 0.9–1.0 → outcomes strongly match intent  
- 0.6–0.8 → partial alignment  
- 0.3–0.5 → weak alignment  
- 0.0–0.2 → outcomes contradict intent  

---

### **8.4 Regime Stability**
- 0.9–1.0 → structural regime dominant  
- 0.6–0.8 → mixed regimes  
- 0.3–0.5 → narrative/emotional dominance  
- 0.0–0.2 → authority/narrative distortion  

---

# 9. Donor Alignment Report (AI-Generated)

The AI Process Manager Agent (PMA) produces a donor alignment report:

```
Donor: DonorA
Intent: education access + community empowerment

Flow Integrity:
  leakage: 18%
  routing: 4 layers
  overhead: moderate

Outcome Coherence:
  outputs: 12 programs delivered
  outcomes: 8 aligned, 4 partial

Regime Stability:
  REG(NAR) at IntermediaryX
  REG(STR) at LocalPartnerD
  DRF(financial) at FoundationB

DAS = 0.72
```

---

# 10. Drift Detection in Donor Alignment

Drift types:

- **mission drift** — intent vs program mismatch  
- **financial drift** — funds not reaching intended nodes  
- **governance drift** — authority imbalance  
- **reporting drift** — narrative inflation  

Operators:
```
DRF(type)
GAP(intent ↔ impact)
```

---

# 11. Structural Corrections (FIX)

The PMA recommends corrections:

```
FIX(IntermediaryX) → reduce overhead
FIX(FoundationB) → increase payout rate
FIX(NGO_C) → improve reporting clarity
```

---

# 12. Summary

The Donor Alignment Score provides:

- a structural measure of donor alignment  
- a triadic view of intent, flow, outcome, and regime  
- a neutral, AI-parsable scoring model  
- a foundation for donor clarity reports  
- a mechanism for correcting drift  

This scoring model transforms donor evaluation from **narrative** to **structure**, enabling clarity, accountability, and alignment across the philanthropic ecosystem.
