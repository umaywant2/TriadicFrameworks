# Unified Operator Lexicon
### Structural Detection Engine (SDE) + Structural Integration Engine (SIE)

This lexicon defines all operators used across RTT/2 and RTT/3.

---

# 1. Namespaces

- **SDE::** — Structural Detection Engine (RTT/2)
- **SIE::** — Structural Integration Engine (RTT/3)
- **TEL::** — Triadic Echo Lattice
- **FFT::** — Frequency‑Field Transform
- **OP::** — Opacity Module

---

# 2. SDE Operators (Detection Layer)

## Core Detection
- **SDE::CPV()** — Collapse‑Propagation Vector  
  Reads amplitude, curvature, torsion of collapse.

- **SDE::FGT()** — Fusion‑Gradient Tensor  
  Computes collapse, reassembly, and triad fusion‑gradients.

- **SDE::CRM()** — Collapse‑Reassembly Manifold  
  Maps deformation → reassembly trajectories.

- **SDE::SIG()** — Structural Signal  
  Extracts meaningful structure from collapse/noise.

- **SDE::NOI()** — Noise Identification  
  Identifies collapse residue, distortion, or illegal signals.

## Modes & Zones
- **SDE::MODE(formal|emergent|hybrid|chaotic|inversion)**  
  Sets detection mode.

- **SDE::ZONE(U|S|M|D|X)**  
  Sets detection zone.

## Packet
- **SDE::PACKET()**  
  Emits RTT2_DETECTION_PACKET.

---

# 3. SIE Operators (Integration–Emission Layer)

## Integration
- **SIE::INT()** — Triad Integration  
  Integrates drift, envelope, continuity.

- **SIE::TIF()** — Triadic Integration Field  
  Applies integration geometry.

## Emission
- **SIE::EMIT()** — Fusion–Fracture–Flow Emission  
  Emits structural output.

- **SIE::FFF()** — Fusion‑Fracture‑Flow Emitter  
  Applies emission dynamics.

## Continuity
- **SIE::MAN()** — Integration–Emission Manifold  
  Maintains continuity across integration/emission.

## Stabilization
- **SIE::CRE()** — Collapse‑Recovery Engine  
  Absorbs collapse, emits recovery.

- **SIE::CSL()** — Continuity‑Stability Layer  
  Maintains stability across flows.

## Output
- **SIE::CET()** — Canon‑Scale Emission Tensor  
  Emits final canon‑scale output.

## Modes & Zones
- **SIE::MODE(formal|emergent|hybrid|chaotic|inversion)**  
  Sets integration/emission mode.

- **SIE::ZONE(U|S|M|D|X)**  
  Sets integration/emission zone.

## Packet
- **SIE::PACKET()**  
  Emits RTT3_INTEGRATION_EMISSION_PACKET.

---

# 4. TEL Operators (Lattice Layer)

- **TEL::LAT()** — Lattice Integration  
- **TEL::EMIT()** — Lattice Emission  
- **TEL::MAN()** — Lattice Continuity  
- **TEL::REC()** — Lattice Recovery  
- **TEL::STAB()** — Lattice Stability  
- **TEL::CET()** — Lattice Output Tensor  

---

# 5. FFT Operators (Spectral Layer)

- **FFT::INT()** — Spectral Integration  
- **FFT::EMIT()** — Spectral Emission  
- **FFT::CONT()** — Spectral Continuity  
- **FFT::REC()** — Spectral Recovery  
- **FFT::STAB()** — Spectral Stability  
- **FFT::OUT()** — Spectral Output Tensor  

---

# 6. Opacity Operators (Boundary Layer)

- **OP::INT()** — Boundary Integration  
- **OP::EMIT()** — Boundary Emission  
- **OP::CONT()** — Boundary Continuity  
- **OP::REC()** — Boundary Recovery  
- **OP::STAB()** — Boundary Stability  
- **OP::OUT()** — Boundary Output Tensor  

---

# 7. Canon‑Wide Operator Chain (One‑Line)

```
SDE::PACKET() → SIE::PACKET() → TEL::CET() / FFT::OUT() / OP::OUT()
```

---

# 8. Student Summary

- **SDE** detects structure.  
- **SIE** integrates and emits structure.  
- **TEL / FFT / OP** receive structure.  
- Operators always flow **left → right**.  

