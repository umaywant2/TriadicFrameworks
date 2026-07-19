### *vST for Generative Models*  
### *Example: 1024D Latent Projection and Cross‑Checkpoint Alignment*

This example demonstrates how a 1024D latent state from a generative model is projected into the triadic cores (9D → 6D → 3D), and how two checkpoints are aligned using vST.

It illustrates projection stability, primitive‑aligned mapping, and drift detection.

---

## **1. Scenario Overview**

We assume:

- a 1024D latent diffusion model  
- two checkpoints: **C₁** (earlier) and **C₂** (later)  
- a single latent state \( z \) sampled at a mid‑trajectory step  
- a need to compare latent geometry across checkpoints  

---

## **2. Step 1 — Extract Latent States**

Let:

\[
z_{C_1}, z_{C_2} \in \mathbb{R}^{1024}
\]

represent the latent state under each checkpoint.

### **Observed Properties**

- \( z_{C_1} \): slightly higher variance  
- \( z_{C_2} \): more compact, refined structure  

---

## **3. Step 2 — Project 1024D → 9D**

Project both latent states into the 9D coherence core.

### **Reveals**

- \( z_{C_1} \): branching, transitional geometry (R₂ᴴ)  
- \( z_{C_2} \): compact, stable geometry (R₁ᴴ)  

### **Interpretation**

The later checkpoint exhibits improved coherence.

---

## **4. Step 3 — Project 9D → 6D**

The 6D interaction projection shows:

- smoother surfaces for \( z_{C_2} \)  
- cross‑step coupling more stable  
- fewer oscillatory transitions  

---

## **5. Step 4 — Project 6D → 3D**

The 3D structural projection shows:

- \( z_{C_1} \): oscillatory motifs  
- \( z_{C_2} \): compact, low‑variance motifs  

### **Interpretation**

The 3D projection reveals motif‑level refinement across checkpoints.

---

## **6. Step 5 — Cross‑Checkpoint Alignment**

Alignment in 9D and 6D shows:

- consistent structural backbone  
- improved coherence surfaces in C₂  
- reduced fragmentation  
- stable primitive‑aligned mapping  

---

## **7. Step 6 — Drift Detection**

Using vST drift categories:

- **D₁ Structural Drift:** low  
- **D₂ Dimensional Drift:** none  
- **D₃ Regime Drift:** moderate (R₂ᴴ → R₁ᴴ shift)  
- **D₄ Projection Drift:** none  

### **Interpretation**

The drift is **positive** — a refinement, not a degradation.

---

## **8. Summary**

This example demonstrates:

- how 1024D latent states are projected into triadic cores  
- how cross‑checkpoint alignment reveals structural improvement  
- how drift detection isolates transitional changes  
- how vST ensures invariant‑preserving comparison  
