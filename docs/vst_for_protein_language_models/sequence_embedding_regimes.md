### *vST for Protein Language Models*  
### *Sequence‑Embedding Regimes in PLM Inference*

This document defines the **sequence‑embedding regimes** that arise during inference in Protein Language Models (PLMs). These regimes generalize the triadic resonance structure of the 3D–9D substrate and describe how stability, transition, and dispersion behaviors manifest across residue‑level embeddings in high‑dimensional latent spaces (64D–4096D).

Sequence‑embedding regimes provide a reproducible, invariant‑preserving framework for interpreting PLM behavior across residues, layers, and model sizes.

---

## **1. Purpose of Sequence‑Embedding Regimes**

Sequence‑embedding regimes allow us to:

- classify residue‑level embedding behavior into stable, transitional, and dispersed phases  
- identify coherence surfaces along the protein sequence  
- detect instability or drift across checkpoints or versions  
- analyze scaling‑law behavior across PLM sizes  
- project high‑dimensional embeddings into 3D–9D cores  
- support vST validation (V₁–V₄)  

These regimes form the backbone of substrate‑level PLM analysis.

---

## **2. Regime Overview**

PLM embeddings follow the same triadic structure as the dimensional substrate:

1. **Stable Regime (R₁ᴴ)**  
2. **Transition Regime (R₂ᴴ)**  
3. **Dispersion Regime (R₃ᴴ)**  

The superscript *H* indicates high‑dimensional behavior.

These regimes appear in:

- residue embeddings  
- attention outputs  
- MLP activations  
- cross‑layer embedding pathways  

---

## **3. Stable Regime (R₁ᴴ)**

### **Definition**  
A region of embedding space where residue embeddings converge consistently and maintain coherence across layers.

### **Characteristics**

- compact, low‑variance embeddings  
- stable coherence surfaces across residues  
- predictable projection into 3D–9D cores  
- primitive‑level integrity (DP, TDP, SP, CP)  
- minimal sensitivity to perturbations  

### **Interpretation**  
R₁ᴴ corresponds to stable biochemical or structural signals, often associated with:

- conserved motifs  
- secondary‑structure anchors  
- stable residue environments  

---

## **4. Transition Regime (R₂ᴴ)**

### **Definition**  
A region where embedding trajectories undergo reorientation, branching, or oscillatory behavior across residues.

### **Characteristics**

- moderate variance across dimensions  
- branching or oscillatory embedding patterns  
- partial coherence‑surface stability  
- increased sensitivity to residue context  
- regime‑transition indicators in resonance‑time space  

### **Interpretation**  
R₂ᴴ captures dynamic behavior such as:

- boundary regions between structural elements  
- ambiguous or flexible residues  
- context‑dependent biochemical signals  

It is the “decision‑making” region of PLM inference.

---

## **5. Dispersion Regime (R₃ᴴ)**

### **Definition**  
A region where embedding trajectories lose coherence and disperse across high‑dimensional space.

### **Characteristics**

- high variance across dimensions  
- fragmented or diffuse coherence surfaces  
- unstable primitive‑level structure  
- non‑compact projections into 3D–9D cores  
- susceptibility to drift or hallucination  

### **Interpretation**  
R₃ᴴ corresponds to unstable or divergent embedding behavior, often associated with:

- low‑confidence predictions  
- disordered regions  
- rare or poorly represented sequence patterns  

---

## **6. Regime Transitions Along the Sequence**

Residue‑level embedding trajectories move through regimes as the model processes the sequence:

- **R₁ᴴ → R₂ᴴ**  
  onset of structural or biochemical ambiguity  
- **R₂ᴴ → R₁ᴴ**  
  return to stable structural context  
- **R₂ᴴ → R₃ᴴ**  
  breakdown of coherence  
- **R₃ᴴ → R₂ᴴ**  
  partial recovery  

Transitions must remain continuous and invariant‑preserving across layers and residues.

---

## **7. Regime Detection Signals**

Regime identity is detected using:

- variance distribution across dimensions  
- coherence‑surface continuity along the sequence  
- primitive‑level stability (DP, TDP, SP, CP)  
- resonance‑time behavior  
- vST validation layers (V₁–V₄)  

These signals collectively determine regime classification.

---

## **8. Regime Behavior Across the Dimensional Ladder**

Regime behavior must remain consistent across:

- 64D residue embeddings  
- 128D–512D hidden states  
- 1024D+ attention and MLP activations  

The substrate ensures:

- structural invariants  
- resonance‑time invariants  
- projection invariants  
- scaling invariants  

Regime identity must be preserved under projection into 3D–9D cores.

---

## **9. Outputs of Sequence‑Embedding Regime Analysis**

Sequence‑embedding regime analysis produces:

- residue‑level regime maps  
- cross‑layer coherence surfaces  
- scaling‑law indicators  
- drift‑detection signals  
- vST validation outputs  
- projection‑stability metrics  

These outputs support reproducible, substrate‑level interpretation of PLM inference.
