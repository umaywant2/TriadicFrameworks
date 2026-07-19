# Student Cheat Sheet — Structural Detection Engine (SDE)
### RTT/2 — Detection Layer

## What SDE Does
SDE detects:
- collapse behavior  
- fusion‑gradients  
- triad deformation  
- collapse→reassembly paths  
- regime‑dependent structural signals  

SDE **does not integrate or emit** — it only detects.

---

## Core Concepts
- **CPV** — Collapse‑Propagation Vector  
- **FGT** — Fusion‑Gradient Tensor  
- **CRM** — Collapse‑Reassembly Manifold  
- **Modes** — formal, emergent, hybrid, chaotic, inversion  
- **Zones** — U, S, M, D, X  

---

## Quick Operators
- `SDE::CPV()` — read collapse vectors  
- `SDE::FGT()` — compute fusion‑gradients  
- `SDE::CRM()` — map collapse→reassembly  
- `SDE::MODE(x)` — set detection mode  
- `SDE::ZONE(x)` — set detection zone  
- `SDE::PACKET()` — output detection packet  

---

## Minimal Packet

```
RTT2_DETECTION_PACKET:
collapse_propagation:
fusion_gradient:
triad_deformation:
regime:
detection_mode:
detection_zone:
cross_module_projection:
notes:
```

---

## When to Use SDE
Use SDE when you need to:
- identify collapse  
- measure deformation  
- read gradients  
- classify structural behavior  
- prepare data for integration  

SDE → SIE is the standard flow.
