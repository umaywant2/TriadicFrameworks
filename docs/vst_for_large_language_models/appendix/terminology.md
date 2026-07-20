### *vST for Large Language Models*  
### *Terminology*

This appendix defines the terminology used throughout the *vST for Large Language Models* artifact. Terms are presented in a substrate‑agnostic, model‑independent manner and apply to any transformer‑based LLM operating across the full dimensional ladder (3D → 1024D). Definitions emphasize primitive‑level structure, regime behavior, scaling continuity, and invariant preservation.

---

## **1. Substrate Terms**

### **LLM Substrate**  
A structured, invariant‑preserving framework for representing and interpreting LLM latent‑space behavior across 64D–4096D.

### **Dimensional Ladder**  
The ordered sequence of dimensional regimes used for projection and scaling analysis:  
3D → 6D → 9D → 64D → 128D → 256D → 512D → 1024D.

### **Coherence Surface**  
A stable region in latent space where trajectories converge and maintain structural continuity.

---

## **2. Primitive Terms**

### **Dimensional Primitive (DP)**  
The minimal unit of latent‑space structure, capturing local coherence and variance behavior.

### **Triadic Dimensional Primitive (TDP)**  
A triad of DPs forming the smallest unit capable of expressing full regime behavior (R₁, R₂, R₃).

### **Scaling Primitive (SP)**  
A rule‑based expansion unit that preserves invariants during dimensional scaling.

### **Coherence Primitive (CP)**  
A minimal unit identifying stable, transitional, or dispersed regions in high‑dimensional latent space.

---

## **3. Core Terms**

### **Triadic Dimensional Core (TDC)**  
The 3D–9D substrate composed of one or more TDPs, used for interpretable projection.

### **3D Structural Core**  
Captures motif‑level geometry and compact latent structure.

### **6D Interaction Core**  
Captures relational and attention‑driven structure.

### **9D Coherence Core**  
Captures pathway‑level coherence and resonance‑time behavior.

---

## **4. Regime Terms**

### **High‑Dimensional Regimes (R₁ᴴ, R₂ᴴ, R₃ᴴ)**  
The triadic regime structure expressed in 64D–1024D latent space.

### **Stable Regime (R₁ / R₁ᴴ)**  
Compact, coherent, low‑variance latent behavior.

### **Transition Regime (R₂ / R₂ᴴ)**  
Branching, oscillatory, or reorientation behavior.

### **Dispersion Regime (R₃ / R₃ᴴ)**  
Diffuse, fragmented, or unstable latent behavior.

---

## **5. Scaling Terms**

### **Scaling Behavior**  
The structured expansion of latent‑space capacity as model size increases.

### **Scaling Regimes (S₁, S₂, S₃)**  
Triadic scaling behavior describing stable, transitional, and dispersion‑prone scaling phases.

### **Dimensional Continuity**  
The requirement that latent‑space expansion remains smooth and invariant‑preserving.

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

### **Layer‑to‑Layer Alignment**  
Comparison of latent trajectories across transformer layers.

### **Token‑to‑Token Alignment**  
Comparison of latent states across positions in a sequence.

### **Cross‑Version Alignment**  
Comparison of latent‑space structure across model versions or checkpoints.

### **Cross‑Model Alignment**  
Comparison of latent‑space geometry across different architectures or model families.

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
