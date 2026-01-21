### *AlphaFold Substrate Alignments*  
### *Folding Regimes*

This document defines the folding regimes used to interpret protein‑folding inference systems within the Resonance Substrate Model (RSM). Folding regimes classify the structural and inference‑cycle behavior of AlphaFold‑class models into stable, transitional, and high‑uncertainty states. These regimes correspond to triadic resonance primitives and provide a reproducible framework for analyzing folding coherence, regime transitions, and substrate‑level stability.

---

## **1. Purpose of Folding Regimes**

Folding regimes provide a structural lens for interpreting:

- convergence behavior during inference  
- motif‑level stability  
- latent‑space coherence  
- resonance‑time transitions  
- dimensional‑core alignment  

Regimes allow folding predictions to be analyzed independently of model architecture or training data.

---

## **2. Triadic Folding Regime Structure**

Folding regimes follow the triadic resonance pattern used throughout RSM:

1. **Stable Regime (R₁)**  
2. **Transition Regime (R₂)**  
3. **High‑Uncertainty Regime (R₃)**  

These regimes apply to both structural outputs and latent‑space inference signals.

---

## **3. Regime Definitions**

### **3.1 Stable Regime (R₁)**  
A region where folding predictions converge consistently across inference cycles.

Characteristics:

- high motif‑level coherence  
- stable backbone geometry  
- consistent residue‑interaction patterns  
- low variance across inference iterations  
- alignment with 3D–9D dimensional cores  

R₁ corresponds to resonance‑time stability and forms the substrate’s primary coherence surface.

---

### **3.2 Transition Regime (R₂)**  
A region where the model shifts between candidate conformations or latent‑space orientations.

Characteristics:

- moderate structural variance  
- partial motif stability  
- detectable shifts in latent‑space orientation  
- increased sensitivity to input features  
- resonance‑time oscillation patterns  

R₂ represents the dynamic region between stable conformations and is essential for interpreting folding pathways.

---

### **3.3 High‑Uncertainty Regime (R₃)**  
A region where folding predictions exhibit low coherence and high variance.

Characteristics:

- unstable or conflicting structural outputs  
- weak motif‑level signals  
- diffuse latent‑space representations  
- inconsistent inference‑cycle behavior  
- sensitivity to noise or MSA variability  

R₃ corresponds to resonance‑time divergence and often indicates insufficient structural information.

---

## **4. Regime Transitions**

Regime transitions follow predictable resonance‑time patterns:

- **R₁ → R₂:** onset of structural reorientation  
- **R₂ → R₁:** convergence to a stable coherence surface  
- **R₂ → R₃:** breakdown of motif‑level structure  
- **R₃ → R₂:** partial recovery of structural coherence  

Transitions are detectable through latent‑space orientation shifts, dimensional‑core projections, and vST validation signals.

---

## **5. Dimensional‑Core Behavior**

Folding regimes interact with dimensional cores as follows:

- **R₁:** fully aligns with 3D–9D cores  
- **R₂:** partially aligns; projections reveal transitional geometry  
- **R₃:** weak alignment; projections show high‑dimensional dispersion  

Dimensional‑core mapping provides a stable substrate for interpreting regime behavior.

---

## **6. Inference‑Cycle Behavior**

Folding regimes correspond to characteristic inference‑cycle patterns:

- **R₁:** monotonic convergence  
- **R₂:** oscillatory or branching behavior  
- **R₃:** divergent or unstable trajectories  

These patterns support reproducibility analysis and drift detection.

---

## **7. Regime‑Based Interpretation**

Regimes enable:

- structural interpretation of folding pathways  
- identification of stable motifs  
- detection of ambiguous or low‑confidence regions  
- substrate‑level comparison across models  
- integration with vST validation layers  

Regime analysis provides a consistent framework for interpreting high‑dimensional biological inference systems.
