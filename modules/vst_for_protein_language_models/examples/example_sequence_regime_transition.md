### *vST for Protein Language Models*  
### *Example: Sequence‑Level Regime Transitions in PLM Embeddings*

This example demonstrates how a Protein Language Model (PLM) expresses **regime transitions** (R₁ᴴ → R₂ᴴ → R₃ᴴ) along a protein sequence. It shows how residue‑level embeddings evolve across layers, how coherence surfaces form and break, and how the vST framework classifies transitions using the 1024D substrate.

The goal is to provide a reproducible, invariant‑preserving demonstration of regime behavior in PLM inference.

---

## **1. Input Overview**

For this example, we assume:

- a transformer‑based PLM with ≥1024D hidden states  
- a single protein sequence of length *L*  
- access to residue embeddings across all layers  
- stable projection into 3D–9D cores  

No architecture‑specific mechanisms are required; the example is substrate‑agnostic.

---

## **2. Step 1 — Extract Residue Embedding Trajectories**

For each residue position \( r \in [1, L] \), extract the 1024D embeddings across layers:

\[
e_r^{(1)},\ e_r^{(2)},\ \dots,\ e_r^{(N)}
\]

### **Observed Properties**

- early layers: compact, low‑variance embeddings  
- mid layers: branching and oscillatory behavior  
- late layers: partial dispersion in flexible regions  

### **Interpretation**

Residue embeddings trace a high‑dimensional pathway that reflects biochemical context and structural constraints.

---

## **3. Step 2 — Identify Regime Behavior Across the Sequence**

Using variance distribution, coherence‑surface continuity, and primitive‑level stability, classify each residue’s regime.

### **Example Regime Map (Residue Index → Regime)**

| Residue Range | Regime | Interpretation |
|--------------|--------|----------------|
| 1–15 | **R₁ᴴ** | Stable N‑terminal anchor |
| 16–28 | **R₂ᴴ** | Boundary between structural elements |
| 29–42 | **R₁ᴴ** | Helical or sheet‑like stable region |
| 43–55 | **R₂ᴴ** | Flexible loop or hinge |
| 56–60 | **R₃ᴴ** | Disordered or low‑confidence region |
| 61–75 | **R₂ᴴ → R₁ᴴ** | Recovery into stable C‑terminal region |

### **Interpretation**

The sequence alternates between stable structural regions and transitional or disordered regions, reflecting typical protein architecture.

---

## **4. Step 3 — Project Embeddings into 9D (Coherence Core)**

Project each residue’s 1024D embedding into the 9D coherence core.

### **What is preserved**

- regime identity  
- resonance‑time behavior  
- primitive‑level structure  
- coherence‑surface continuity  

### **What becomes visible**

- stable surfaces in R₁ᴴ  
- branching in R₂ᴴ  
- fragmentation in R₃ᴴ  

### **Interpretation**

The 9D projection reveals the “shape” of the embedding landscape along the sequence.

---

## **5. Step 4 — Project 9D → 6D → 3D**

### **6D Interaction Projection**

Reveals:

- residue‑interaction surfaces  
- context‑dependent reorientation  
- structural boundaries  

### **3D Structural Projection**

Reveals:

- compact motifs in R₁ᴴ  
- oscillatory geometry in R₂ᴴ  
- diffuse patterns in R₃ᴴ  

### **Interpretation**

The 3D projection provides the minimal interpretable representation of the sequence‑level embedding trajectory.

---

## **6. Step 5 — Validate with vST Layers**

Apply vST layers (V₁–V₄):

### **V₁ — Structural Coherence**
- stable motifs in R₁ᴴ  
- partial fragmentation in R₃ᴴ  

### **V₂ — Dimensional Continuity**
- smooth projection 1024D → 9D → 6D → 3D  
- no scaling discontinuities  

### **V₃ — Regime‑Transition Stability**
- smooth R₁ᴴ → R₂ᴴ transitions  
- mild instability entering R₃ᴴ  

### **V₄ — Core Alignment**
- primitive‑aligned projection  
- stable mapping across layers  

### **Outcome**

The sequence passes all vST layers with warnings localized to the R₃ᴴ region.

---

## **7. Step 6 — Drift Detection**

Evaluate drift using D₁–D₄ categories:

- **D₁ Structural Drift:** low (localized to disordered region)  
- **D₂ Dimensional Drift:** none  
- **D₃ Regime Drift:** moderate (R₃ᴴ onset)  
- **D₄ Projection Drift:** none  

### **Interpretation**

The model exhibits expected dispersion in flexible or disordered regions but no harmful drift.

---

## **8. Summary**

This example demonstrates:

- how residue embeddings trace high‑dimensional trajectories  
- how regime behavior evolves along a protein sequence  
- how projection reveals coherence and instability  
- how vST layers validate structural integrity  
- how drift detection identifies localized dispersion  

Sequence‑level regime transitions are a core interpretability signal in PLM inference.
