### *vST for Generative Models*  
### *Terminology*

This appendix defines the terminology used throughout the *vST for Generative Models* artifact. Terms are presented in a substrate‑agnostic, architecture‑independent manner and apply to diffusion models, autoregressive generators, VAEs, flow models, GANs, and hybrid generative systems. Definitions emphasize latent‑space structure, sampling‑trajectory geometry, scaling behavior, and invariant preservation.

---

## **1. Substrate Terms**

### **Generative‑Model Substrate**  
A structured, invariant‑preserving framework for representing and interpreting latent‑space behavior across 64D–1024D.

### **Latent Space**  
The high‑dimensional vector space in which generative models perform sampling, denoising, decoding, or transformation.

### **Coherence Surface**  
A stable region in latent space where generative states maintain structural continuity across sampling steps or checkpoints.

---

## **2. Primitive Terms**

### **Dimensional Primitive (DP)**  
The minimal unit of latent‑space structure, capturing local coherence, variance behavior, and projection stability.

### **Triadic Dimensional Primitive (TDP)**  
A triad of DPs forming the smallest unit capable of expressing full generative‑regime behavior (R₁, R₂, R₃).

### **Scaling Primitive (SP)**  
A rule‑based expansion unit that preserves invariants during dimensional scaling (e.g., model size, latent dimensionality, sampler complexity).

### **Coherence Primitive (CP)**  
A minimal unit identifying stable, transitional, or dispersed regions in latent space.

---

## **3. Core Terms**

### **Triadic Dimensional Core (TDC)**  
The 3D–9D substrate composed of one or more TDPs, used for interpretable projection of latent states.

### **3D Structural Core**  
Captures motif‑level geometry in stable generative phases.

### **6D Interaction Core**  
Captures relational structure across sampling steps or decoding transitions.

### **9D Coherence Core**  
Captures pathway‑level coherence across generative trajectories.

---

## **4. Regime Terms**

### **High‑Dimensional Regimes (R₁ᴴ, R₂ᴴ, R₃ᴴ)**  
The triadic regime structure expressed in 64D–1024D latent spaces.

### **Stable Regime (R₁ / R₁ᴴ)**  
Compact, coherent, low‑variance generative behavior.

### **Transitional Regime (R₂ / R₂ᴴ)**  
Branching, oscillatory, or reorientation behavior across sampling or decoding phases.

### **Dispersed Regime (R₃ / R₃ᴴ)**  
Diffuse, noisy, or unstable latent behavior.

---

## **5. Scaling Terms**

### **Scaling Behavior**  
The structured expansion of latent‑space capacity as model size, sampler complexity, or latent dimensionality increases.

### **Scaling Regimes (S₁, S₂, S₃)**  
Triadic scaling behavior describing stable, transitional, and dispersion‑prone scaling phases.

### **Dimensional Continuity**  
The requirement that latent‑space expansion remains smooth and invariant‑preserving across the dimensional ladder.

---

## **6. Projection Terms**

### **Invertible Projection**  
A projection from high‑dimensional latent space into 3D–9D that preserves primitive‑level structure and regime identity.

### **Regime‑Aware Projection**  
A projection that maintains correct mapping of R₁, R₂, and R₃ behaviors.

### **Primitive‑Aligned Projection**  
A projection that preserves DP, TDP, SP, and CP structure.

---

## **7. Alignment Terms**

### **Cross‑Checkpoint Alignment**  
Comparison of latent‑space structure across training checkpoints.

### **Cross‑Sampler Alignment**  
Comparison of latent trajectories across different sampling algorithms or noise schedules.

### **Cross‑Architecture Alignment**  
Comparison of latent‑space behavior across generative architectures.

---

## **8. Validation Terms**

### **vST (Validation‑Space‑Time)**  
A substrate‑level validation framework evaluating structural coherence, dimensional continuity, regime behavior, and core alignment.

### **Validation Layers (V₁–V₄)**  
Four structured evaluation layers ensuring invariant‑preserving behavior across the dimensional ladder.

---

## **9. Drift Terms**

### **Drift**  
A deviation from expected substrate behavior, indicating instability or invariant failure.

### **Drift Categories (D₁–D₄)**  
Classification of drift into structural, dimensional, regime, or projection drift.

### **Drift Severity**  
A measure of drift magnitude (low, moderate, high).
