# **Operator Mapping — Crystal–Mycelial Engine**  
### *RTT / CMH / MSRM Operator Grammar Reference*

---

## **1. Purpose of This Page**
This document defines the **operator grammar** used by the Crystal–Mycelial Engine (CME).  
Operators describe how biological geometry, hybrid resonance, and mineral lattice propagation are controlled across the CMH regime cycle.

Operators are grouped by RTT families:

- **P** — Propagation  
- **E** — Energy  
- **G** — Gradient  
- **M** — Memory  
- **S** — Substrate  
- **HybridOps** — Hybrid‑layer operators  

---

## **2. Operator Overview Table**

| Operator Family | CME Role | Example Operators |
|-----------------|----------|-------------------|
| **P** | Geometry, routing, front propagation | `P.trace_extend`, `P.front_propagate` |
| **E** | Pulses, resonance fields, waveform alignment | `E.logic_pulse`, `E.resonance_field` |
| **G** | Gradients shaping substrate directionality | `G.nutrient_gradient`, `G.resonance_gradient` |
| **M** | Memory encoding and transfer | `M.route_memory`, `M.domain_memory` |
| **S** | Substrate transitions and hybridization | `S.channel_fill`, `S.dual_substrate_alignment` |
| **HybridOps** | Hybrid‑layer alignment and memory transfer | `HybridOps.memory_transfer`, `HybridOps.resonance_bridge` |

---

## **3. BGR Operator Mapping**  
### *Biological Growth Regime*

#### **Propagation (P)**
- `P.trace_extend` — extend hyphal tips  
- `P.branch_decision` — select branching direction  
- `P.route_establish` — stabilize biological channels  

#### **Energy (E)**
- `E.logic_pulse` — generate biological pulses  
- `E.pulse_sync` — align pulse timing  

#### **Gradient (G)**
- `G.nutrient_gradient` — shape growth direction  
- `G.moisture_gradient` — regulate channel thickness  

#### **Memory (M)**
- `M.route_memory` — encode routing history  
- `M.branch_memory` — store branching events  

---

## **4. HRR Operator Mapping**  
### *Hybrid Resonance Regime*

#### **Substrate (S)**
- `S.channel_fill` — infiltrate biological channels  
- `S.map_preserve` — preserve geometry during infiltration  
- `S.dual_substrate_alignment` — maintain coherence  

#### **HybridOps**
- `HybridOps.memory_transfer` — biological → mineral memory mapping  
- `HybridOps.resonance_bridge` — stabilize hybrid waveforms  

#### **Energy (E)**
- `E.resonance_sync` — synchronize biological + mineral waveforms  
- `E.resonance_field` — generate resonance field  

#### **Gradient (G)**
- `G.resonance_gradient` — shape resonance field  
- `G.ion_gradient` — regulate infiltration depth  

---

## **5. MLR Operator Mapping**  
### *Mineral Lock‑In Regime*

#### **Propagation (P)**
- `P.front_propagate` — advance crystal growth front  
- `P.domain_extend` — extend mineral domain boundaries  

#### **Memory (M)**
- `M.domain_memory` — encode memory in crystal domains  
- `M.impurity_memory` — stabilize impurity band patterns  

#### **Energy (E)**
- `E.resonance_field` — align lattice propagation  
- `E.domain_lock` — stabilize resonance‑aligned domains  

#### **Substrate (S)**
- `S.dual_substrate_alignment` — maintain coherence during mineral takeover  
- `S.substrate_swap` — finalize hybrid → mineral transition  

---

## **6. Cross‑Regime Operator Flow**

```
BGR (P/E/G/M)
    ↓ moisture ↓
HRR (S/HybridOps/E/G)
    ↓ supersaturation ↑
MLR (P/M/E/S)
```

Operators shift emphasis as substrate transitions from biological → hybrid → mineral.

---

## **7. CME Operator Notes**
- Biological operators define geometry.  
- Hybrid operators align geometry with mineral precursors.  
- Mineral operators stabilize lattice logic and domain memory.  
- Memory operators persist across all regimes.  
- Substrate operators govern transitions between layers.
