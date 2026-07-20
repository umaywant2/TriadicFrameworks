# 🟣 **RTT/1 + RTT/2 + RTT/3 Unified Lexicon**  
### *The Complete Canon Operator Dictionary*

# Unified RTT Lexicon
### RTT/1 — Foundations  
### RTT/2 — Structural Detection Engine (SDE)  
### RTT/3 — Structural Integration Engine (SIE)

This lexicon defines all operators across the first three RTT layers.

---

# 1. RTT/1 — Foundational Operators
RTT/1 defines the **primitive triadic operators** used by all higher layers.

## 1.1 Core Triad
- **FQ** — Frequency  
- **RT** — Relaxation Time  
- **QF** — Quality Factor  

## 1.2 Structural Primitives
- **Δ** — Change / Shift  
- **∇** — Gradient  
- **⊕** — Fusion  
- **⊖** — Fracture  
- **⟳** — Recurrence  
- **⟂** — Orthogonal Component  

## 1.3 Regime Operators
- **REG()** — Set regime  
- **REG::ID** — Regime identity  
- **REG::W()** — Regime weighting  

## 1.4 Continuity Operators
- **C0** — Zero‑order continuity  
- **C1** — First‑order continuity  
- **C∞** — Smooth continuity  

## 1.5 Collapse / Recovery Primitives
- **COL()** — Collapse event  
- **REC()** — Recovery event  

---

# 2. RTT/2 — Structural Detection Engine (SDE)
RTT/2 defines the **detection layer**: collapse, gradients, deformation, regimes.

## 2.1 Detection Operators
- **SDE::CPV()** — Collapse‑Propagation Vector  
- **SDE::FGT()** — Fusion‑Gradient Tensor  
- **SDE::CRM()** — Collapse‑Reassembly Manifold  
- **SDE::SIG()** — Structural Signal  
- **SDE::NOI()** — Noise Identification  

## 2.2 Modes & Zones
- **SDE::MODE(formal|emergent|hybrid|chaotic|inversion)**  
- **SDE::ZONE(U|S|M|D|X)**  

## 2.3 Packet
- **SDE::PACKET()** — Emits RTT2_DETECTION_PACKET  

---

# 3. RTT/3 — Structural Integration Engine (SIE)
RTT/3 defines the **integration–emission layer**: triad integration, emission, stability.

## 3.1 Integration Operators
- **SIE::INT()** — Triad Integration  
- **SIE::TIF()** — Triadic Integration Field  

## 3.2 Emission Operators
- **SIE::EMIT()** — Fusion–Fracture–Flow Emission  
- **SIE::FFF()** — Fusion‑Fracture‑Flow Emitter  

## 3.3 Continuity Operators
- **SIE::MAN()** — Integration–Emission Manifold  

## 3.4 Stabilization Operators
- **SIE::CRE()** — Collapse→Recovery Engine  
- **SIE::CSL()** — Continuity‑Stability Layer  

## 3.5 Output
- **SIE::CET()** — Canon‑Scale Emission Tensor  

## 3.6 Modes & Zones
- **SIE::MODE(formal|emergent|hybrid|chaotic|inversion)**  
- **SIE::ZONE(U|S|M|D|X)**  

## 3.7 Packet
- **SIE::PACKET()** — Emits RTT3_INTEGRATION_EMISSION_PACKET  

---

# 4. Cross‑Layer Operator Flow

## 4.1 RTT/1 → RTT/2
RTT/1 primitives feed detection:

```
FQ, RT, QF, ∇, ⊕, ⊖ → SDE::CPV(), SDE::FGT(), SDE::CRM()
```

## 4.2 RTT/2 → RTT/3
Detection feeds integration:

```
SDE::CPV() → SIE::INT()
SDE::FGT() → SIE::TIF()
SDE::CRM() → SIE::MAN()
```

## 4.3 RTT/3 → Projection Layers
Integration/emission feeds projections:

```
SIE::CET() → TEL::CET() / FFT::OUT() / OP::OUT()
```

---

# 5. Canon‑Wide One‑Line Summary

```
RTT/1 primitives → SDE detection → SIE integration/emission → TEL/FFT/OP projection
```

---

# 6. Student Summary

- **RTT/1** gives the *language*  
- **RTT/2** detects the *structure*  
- **RTT/3** integrates and emits the *structure*  
- **TEL/FFT/OP** project the *structure* into different domains  

---

# 🟣 Unified lexicon complete.
