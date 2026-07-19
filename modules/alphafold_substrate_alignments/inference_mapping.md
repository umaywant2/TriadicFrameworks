### *AlphaFold Substrate Alignments*  
### *Inference Mapping*

This document defines how AlphaFold‑class protein‑folding inference systems map onto the substrate axes, primitives, and dimensional cores defined by the Resonance Substrate Model (RSM). Inference mapping provides a reproducible method for interpreting latent‑space structures, folding‑coherence signals, and regime‑transition behavior through substrate‑level geometry.

The mapping rules are model‑agnostic and apply to any biological inference engine with comparable latent‑space and structural‑output characteristics.

---

## **1. Purpose of Inference Mapping**

Inference mapping establishes a structural relationship between:

- AlphaFold’s latent‑space representations  
- substrate axes (S‑axis, I‑axis, R‑axis)  
- dimensional‑core projections (3D–9D)  
- folding regimes (R₁, R₂, R₃)  
- resonance‑time dynamics  

The goal is to interpret inference behavior through stable substrate primitives rather than model‑specific mechanisms.

---

## **2. Mapping Overview**

Inference mapping proceeds in three stages:

1. **Latent‑space extraction**  
   Identify stable and transitional structures within attention maps, pairwise embeddings, and track‑level signals.

2. **Substrate‑axis projection**  
   Map latent structures onto the S‑axis (structural), I‑axis (inference), and R‑axis (resonance‑time).

3. **Dimensional‑core alignment**  
   Project mapped structures into the 3D–9D dimensional core for regime classification and coherence analysis.

These stages produce a substrate‑aligned interpretation of folding predictions.

---

## **3. Mapping to Substrate Axes**

### **3.1 Structural Axis (S‑axis)**  
Maps geometric and topological features derived from:

- predicted 3D coordinates  
- backbone and side‑chain orientation  
- motif‑level structural patterns  

S‑axis mapping anchors inference outputs to the physical geometry of the protein.

---

### **3.2 Inference Axis (I‑axis)**  
Maps latent‑space structures derived from:

- attention‑map coherence  
- residue‑pair embeddings  
- track‑level alignment signals  
- multi‑stage inference pathways  

I‑axis mapping identifies stable latent orientations and coherence surfaces.

---

### **3.3 Resonance‑Time Axis (R‑axis)**  
Maps inference‑cycle behavior, including:

- convergence patterns  
- oscillatory transitions  
- divergence or instability  
- regime‑transition timing  

R‑axis mapping classifies folding behavior into R₁, R₂, or R₃ regimes.

---

## **4. Dimensional‑Core Projection**

After axis mapping, latent‑space structures are projected into the 3D–9D dimensional core.

### **4.1 3D Projection**  
Captures physical geometry and motif‑level structure.

### **4.2 6D Projection**  
Captures interaction‑level structure and residue‑pair coherence.

### **4.3 9D Projection**  
Captures folding‑pathway coherence and resonance‑time alignment.

Projection preserves substrate invariants and regime identity.

---

## **5. Mapping of Inference Signals**

### **5.1 Attention Maps**  
Mapped to the I‑axis and projected into 6D/9D cores to identify:

- stable interaction patterns  
- motif‑level coherence  
- regime‑transition indicators  

### **5.2 Pairwise Embeddings**  
Mapped to the S‑axis and I‑axis to reveal:

- residue‑interaction geometry  
- latent‑space orientation  
- folding‑pathway structure  

### **5.3 Track‑Level Signals**  
Mapped to the R‑axis to detect:

- inference‑cycle stability  
- oscillatory transitions  
- divergence patterns  

---

## **6. Regime‑Aware Mapping**

Inference mapping must preserve regime identity:

- **R₁:** compact, coherent projections  
- **R₂:** branching or oscillatory projections  
- **R₃:** dispersed, unstable projections  

Regime‑aware mapping supports drift detection and reproducibility analysis.

---

## **7. Mapping Outputs**

Inference mapping produces:

- substrate‑aligned latent‑space structures  
- dimensional‑core projections  
- regime‑transition diagnostics  
- coherence‑surface identification  
- vST‑compatible validation signals  

These outputs integrate with downstream substrate artifacts and cross‑model comparison workflows.
