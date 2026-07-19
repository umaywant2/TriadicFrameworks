### *AlphaFold Substrate Alignments*  
### *Substrate Definition*

This document defines the substrate axes, primitives, and structural invariants used to align the Resonance Substrate Model (RSM) with AlphaFold‑class protein‑folding inference systems. The substrate formalizes the stable structures, dimensional cores, and resonance‑time behaviors that govern folding coherence within high‑dimensional biological inference models.

---

## **1. Substrate Purpose**

The substrate provides a reproducible structural framework for interpreting protein‑folding inference systems through RSM primitives. It identifies stable axes within AlphaFold’s latent space, defines the resonance‑time regimes relevant to folding transitions, and establishes substrate‑level invariants that support validation, drift detection, and cross‑model comparison.

---

## **2. Substrate Axes**

The AlphaFold substrate is defined across three primary axes:

### **2.1 Structural Axis (S‑axis)**  
Represents geometric and topological features of protein conformations, including backbone orientation, side‑chain positioning, and motif‑level coherence.  
This axis anchors the 3D–9D dimensional core used for folding interpretation.

### **2.2 Inference Axis (I‑axis)**  
Captures the latent‑space representations used by AlphaFold’s internal inference mechanisms.  
Includes attention‑map coherence, pairwise residue embeddings, and multi‑track alignment signals.

### **2.3 Resonance‑Time Axis (R‑axis)**  
Encodes the temporal and regime‑transition behavior of folding predictions.  
Tracks stability, transition, and uncertainty regimes across iterative inference cycles.

Together, these axes form the **SIR substrate triad**, the minimal structure required to align RSM with biological inference systems.

---

## **3. Substrate Primitives**

The substrate uses the following primitives:

- **Dimensional Core (DC)**  
  The 3D–9D structural substrate used to represent folding geometry and motif‑level coherence.

- **Resonance Primitive (RP)**  
  The triadic resonance unit governing stability, transition, and uncertainty regimes in folding predictions.

- **Inference Projection (IP)**  
  A mapping from AlphaFold’s latent representations onto substrate axes.

- **Coherence Surface (CS)**  
  A stable region within the substrate where folding predictions converge.

These primitives are domain‑agnostic and compatible with the broader RSM canon.

---

## **4. Substrate Invariants**

The following invariants hold across all folding regimes:

- **Dimensional invariance:**  
  Folding coherence remains stable under projection from 3D–9D cores into higher‑dimensional inference spaces.

- **Resonance‑time invariance:**  
  Regime transitions follow predictable resonance‑time patterns independent of model architecture.

- **Structural invariance:**  
  Motif‑level coherence persists across inference iterations and model variants.

These invariants support reproducibility and cross‑model alignment.

---

## **5. Substrate Boundaries**

The substrate applies to:

- AlphaFold‑class protein‑folding inference systems  
- High‑dimensional latent‑space models with structural outputs  
- Regime‑based folding predictions  
- Systems with iterative inference cycles

The substrate does **not** define biological mechanisms or biochemical energetics; it describes the structural behavior of inference models.

---

## **6. Substrate Outputs**

The substrate produces:

- aligned structural axes  
- regime‑aware folding interpretations  
- dimensional projections  
- substrate‑level validation signals  
- drift‑detection indicators  
- reproducible folding‑coherence surfaces

These outputs integrate with vST validation layers and downstream substrate artifacts.
