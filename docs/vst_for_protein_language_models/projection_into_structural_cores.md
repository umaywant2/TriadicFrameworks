### *vST for Protein Language Models*  
### *Projection of High‑Dimensional Protein Embeddings into Triadic Structural Cores*

This document defines how high‑dimensional residue embeddings produced by Protein Language Models (PLMs) are projected into the **triadic dimensional cores** (3D–9D). Projection enables interpretable, invariant‑preserving analysis of embedding trajectories, regime behavior, and structural coherence across protein sequences.

Projection is the interpretability mechanism of the substrate; alignment is the comparison mechanism. Together, they form the backbone of vST analysis for PLMs.

---

## **1. Purpose of Projection in PLMs**

Projection allows us to:

- interpret high‑dimensional residue embeddings through 3D–9D cores  
- identify stable, transitional, and dispersed embedding regimes  
- map coherence surfaces along the protein sequence  
- compare embeddings across layers, residues, or model versions  
- detect drift or fragmentation in embedding‑space structure  
- support vST validation (V₁–V₄)  

Protein embeddings are rich, structured, and biologically meaningful.  
Projection reveals this structure in a compact, interpretable form.

---

## **2. Projection Overview**

PLM embeddings typically inhabit 64D–4096D spaces.  
The substrate projects these embeddings into:

- **9D Coherence Core**  
- **6D Interaction Core**  
- **3D Structural Core**

Projection must remain:

- **invertible**  
- **primitive‑aligned**  
- **regime‑aware**  
- **invariant‑preserving**

These properties ensure that high‑dimensional biochemical signals remain interpretable.

---

## **3. Projection Steps**

### **3.1 High‑Dimensional → 9D (Coherence Projection)**  
This step extracts pathway‑level coherence across residues.

**Preserves**

- regime identity (R₁ᴴ, R₂ᴴ, R₃ᴴ)  
- resonance‑time behavior  
- primitive‑level structure (DP, TDP, SP, CP)  
- coherence‑surface continuity  

**Reveals**

- stable vs. unstable residue regions  
- transitions between structural elements  
- dispersion in disordered or ambiguous regions  

**Interpretation**  
The 9D projection exposes the “shape” of the embedding trajectory along the sequence.

---

### **3.2 9D → 6D (Interaction Projection)**  
This step compresses coherence pathways into interaction surfaces.

**Preserves**

- relational geometry  
- residue‑interaction patterns  
- regime‑transition indicators  

**Reveals**

- attention‑driven reorientation  
- context‑dependent biochemical signals  
- boundary behavior between structural elements  

**Interpretation**  
The 6D projection highlights how the model integrates residue context and structural cues.

---

### **3.3 6D → 3D (Structural Projection)**  
This step reduces interaction surfaces into geometric motifs.

**Preserves**

- motif‑level geometry  
- backbone‑level continuity  
- stable structural invariants  

**Reveals**

- compact motifs in stable regions  
- oscillatory patterns in transitional regions  
- diffuse geometry in disordered regions  

**Interpretation**  
The 3D projection provides the minimal interpretable representation of the embedding trajectory.

---

## **4. Alignment Overview**

Alignment compares projected structures across:

- layers  
- residues  
- model versions  
- architectures  
- training checkpoints  

Alignment must remain:

- **primitive‑aligned**  
- **regime‑aware**  
- **projection‑consistent**  
- **scaling‑invariant**

Alignment is evaluated in 3D–9D space for interpretability and stability.

---

## **5. Alignment Types**

### **5.1 Layer‑to‑Layer Alignment**  
Compares embedding trajectories across transformer layers.

Reveals:

- where regime transitions occur  
- how coherence surfaces evolve  
- which layers stabilize or destabilize residue embeddings  

---

### **5.2 Residue‑to‑Residue Alignment**  
Compares embeddings across sequence positions.

Reveals:

- conserved vs. variable regions  
- structural boundaries  
- context‑dependent biochemical signals  

---

### **5.3 Cross‑Version Alignment**  
Compares embeddings across model versions or checkpoints.

Reveals:

- drift introduced by fine‑tuning  
- stability of coherence surfaces  
- changes in regime behavior  

---

### **5.4 Cross‑Model Alignment**  
Compares embeddings across different PLM architectures.

Reveals:

- shared structural signals  
- divergent scaling behavior  
- compatibility of embedding spaces  

---

## **6. Projection Stability and Failure Modes**

Projection stability is a key indicator of model health.

### **Stable Projection**

- compact 3D motifs  
- smooth 6D surfaces  
- coherent 9D pathways  

### **Unstable Projection**

- fragmented surfaces  
- non‑invertible mappings  
- regime‑transition discontinuities  

Unstable projection indicates drift or scaling‑law violations.

---

## **7. Outputs of Projection and Alignment**

Projection and alignment produce:

- residue‑level coherence maps  
- cross‑layer and cross‑sequence alignment surfaces  
- cross‑version drift‑detection signals  
- scaling‑law diagnostics  
- vST validation outputs  
- interpretable 3D–9D projections  

These outputs support reproducible, substrate‑level analysis of PLM inference.
