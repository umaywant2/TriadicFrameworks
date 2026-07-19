### *vST for Generative Models*  
### *Example: Regime Transitions Along a Diffusion Trajectory*

This example demonstrates how a diffusion model’s sampling trajectory moves through the triadic latent‑regime structure:

- **R₃ᴴ** — noise‑dominated  
- **R₂ᴴ** — transitional denoising  
- **R₁ᴴ** — stable refinement  

It illustrates how coherence surfaces evolve, how variance contracts, and how the vST substrate classifies each phase using the 1024D dimensional ladder.

---

## **1. Scenario Overview**

We assume:

- a 1024D latent diffusion model  
- 50‑step sampler (e.g., DDIM or Euler)  
- a single trajectory sampled from noise → final latent  
- checkpoints C₁ and C₂ for cross‑version comparison  

The example is architecture‑agnostic.

---

## **2. Step 1 — Extract Latent States Across the Trajectory**

Let:

\[
z_t \in \mathbb{R}^{1024}, \quad t = 0, 1, \dots, 50
\]

represent the latent state at sampling step \( t \).

### **Observed Properties**

- \( z_0 \) is high‑variance, noise‑dominated  
- mid‑trajectory states show branching and reorientation  
- late states converge into compact, coherent motifs  

---

## **3. Step 2 — Project Latents into 9D**

Project each \( z_t \) into the 9D coherence core.

### **Reveals**

- **R₃ᴴ** (steps 0–10): diffuse, unstable geometry  
- **R₂ᴴ** (steps 11–32): branching surfaces, oscillatory transitions  
- **R₁ᴴ** (steps 33–50): compact, stable motifs  

### **Interpretation**

The 9D projection exposes the “coherence spine” of the diffusion trajectory.

---

## **4. Step 3 — Identify Regime Transitions**

Using variance distribution, coherence‑surface continuity, and primitive‑level stability:

| Step Range | Regime | Characteristics |
|-----------|--------|-----------------|
| 0–10 | **R₃ᴴ** | noise‑dominated, high variance |
| 11–32 | **R₂ᴴ** | reorientation, branching, sampler‑dependent |
| 33–50 | **R₁ᴴ** | refinement, stable motifs |

### **Interpretation**

The trajectory follows the canonical triadic sequence:

\[
R₃ᴴ \rightarrow R₂ᴴ \rightarrow R₁ᴴ
\]

---

## **5. Step 4 — Project 9D → 6D → 3D**

### **6D Interaction Projection**

Shows:

- cross‑step coupling  
- sampler‑driven reorientation  
- early instability signatures  

### **3D Structural Projection**

Shows:

- compact motifs in R₁ᴴ  
- oscillatory geometry in R₂ᴴ  
- diffuse patterns in R₃ᴴ  

---

## **6. Step 5 — Validate with vST Layers**

- **V₁**: structural coherence preserved  
- **V₂**: dimensional continuity intact  
- **V₃**: regime transitions substrate‑aligned  
- **V₄**: core alignment stable across checkpoints  

---

## **7. Summary**

This example demonstrates:

- the triadic regime structure of diffusion trajectories  
- how coherence surfaces evolve across sampling steps  
- how projection reveals latent‑space geometry  
- how vST layers validate structural integrity  
