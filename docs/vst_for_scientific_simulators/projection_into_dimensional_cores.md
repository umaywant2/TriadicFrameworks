### *vST for Scientific Simulators*  
### *Projection of High‑Dimensional Simulation States into Triadic Dimensional Cores*

This document defines how high‑dimensional simulation states are projected into the **triadic dimensional cores** (3D–9D). Projection enables interpretable, invariant‑preserving analysis of state‑space trajectories, dynamical regimes, solver behavior, and cross‑version drift in scientific simulators.

Projection is the interpretability mechanism of the substrate; alignment is the comparison mechanism. Together, they form the backbone of vST analysis for simulators.

---

## **1. Purpose of Projection in Scientific Simulators**

Projection allows us to:

- interpret high‑dimensional simulation states through 3D–9D cores  
- identify stable, transitional, and dispersed dynamical regimes  
- map coherence surfaces across time and space  
- compare states across solver iterations, grid resolutions, or model versions  
- detect drift or fragmentation in state‑space structure  
- support vST validation (V₁–V₄)  

Simulation states are structured, physical, and often multi‑field.  
Projection reveals this structure in a compact, interpretable form.

---

## **2. Projection Overview**

Simulation state‑spaces often inhabit 64D–10⁶D regions.  
The substrate projects these states into:

- **9D Coherence Core**  
- **6D Interaction Core**  
- **3D Structural Core**

Projection must remain:

- **invertible**  
- **primitive‑aligned**  
- **regime‑aware**  
- **invariant‑preserving**

These properties ensure that high‑dimensional physical signals remain interpretable.

---

## **3. Projection Steps**

### **3.1 High‑Dimensional → 9D (Coherence Projection)**  
This step extracts pathway‑level coherence across time, space, or solver iterations.

**Preserves**

- regime identity (R₁ᴴ, R₂ᴴ, R₃ᴴ)  
- resonance‑time behavior  
- primitive‑level structure (DP, TDP, SP, CP)  
- coherence‑surface continuity  

**Reveals**

- stable vs. unstable dynamical regions  
- transitions between physical phases  
- dispersion in chaotic or poorly conditioned regions  

**Interpretation**  
The 9D projection exposes the “shape” of the simulation’s dynamical evolution.

---

### **3.2 9D → 6D (Interaction Projection)**  
This step compresses coherence pathways into interaction surfaces.

**Preserves**

- relational geometry across fields or particles  
- solver‑driven coupling behavior  
- regime‑transition indicators  

**Reveals**

- interaction‑driven reorientation  
- multi‑field coupling patterns  
- boundary behavior between dynamical phases  

**Interpretation**  
The 6D projection highlights how the simulator integrates physical interactions.

---

### **3.3 6D → 3D (Structural Projection)**  
This step reduces interaction surfaces into geometric motifs.

**Preserves**

- motif‑level geometry  
- spatial or particle‑level continuity  
- stable structural invariants  

**Reveals**

- compact motifs in R₁ᴴ  
- oscillatory geometry in R₂ᴴ  
- diffuse patterns in R₃ᴴ  

**Interpretation**  
The 3D projection provides the minimal interpretable representation of the simulation state.

---

## **4. Alignment Overview**

Alignment compares projected structures across:

- solver iterations  
- spatial or particle domains  
- grid resolutions  
- solver configurations  
- model versions  
- multi‑field couplings  

Alignment must remain:

- **primitive‑aligned**  
- **regime‑aware**  
- **projection‑consistent**  
- **scaling‑invariant**

Alignment is evaluated in 3D–9D space for interpretability and stability.

---

## **5. Alignment Types**

### **5.1 Iteration‑to‑Iteration Alignment**  
Compares state trajectories across solver steps.

Reveals:

- where regime transitions occur  
- how coherence surfaces evolve  
- which solver stages stabilize or destabilize the system  

---

### **5.2 Spatial/Particle Alignment**  
Compares states across spatial regions or particle subsets.

Reveals:

- coherent vs. divergent regions  
- phase boundaries  
- localized instabilities  

---

### **5.3 Cross‑Resolution Alignment**  
Compares states across grid refinements or timestep reductions.

Reveals:

- scaling‑law continuity  
- resolution‑dependent drift  
- stability of coherence surfaces  

---

### **5.4 Cross‑Version Alignment**  
Compares states across simulator versions or parameterizations.

Reveals:

- drift introduced by code changes  
- solver‑conditioning effects  
- changes in regime behavior  

---

## **6. Projection Stability and Failure Modes**

Projection stability is a key indicator of simulator health.

### **Stable Projection**

- compact 3D motifs  
- smooth 6D surfaces  
- coherent 9D pathways  

### **Unstable Projection**

- fragmented surfaces  
- non‑invertible mappings  
- regime‑transition discontinuities  

Unstable projection indicates drift, scaling‑law violations, or numerical instability.

---

## **7. Outputs of Projection and Alignment**

Projection and alignment produce:

- temporal or spatial coherence maps  
- cross‑iteration and cross‑resolution alignment surfaces  
- cross‑version drift‑detection signals  
- scaling‑law diagnostics  
- vST validation outputs  
- interpretable 3D–9D projections  

These outputs support reproducible, substrate‑level analysis of scientific simulators.
