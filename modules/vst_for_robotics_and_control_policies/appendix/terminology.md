### *vST for Robotics and Control Policies*  
### *Terminology*

This appendix defines the terminology used throughout the *vST for Robotics and Control Policies* artifact. Terms are presented in a substrate‑agnostic, model‑independent manner and apply to any control‑policy system operating across the full dimensional ladder (3D → 1024D). Definitions emphasize primitive‑level structure, latent‑space dynamics, regime behavior, scaling continuity, and invariant preservation.

---

## **1. Substrate Terms**

### **Control‑Policy Substrate**  
A structured, invariant‑preserving framework for representing and interpreting policy latent spaces across 64D–1024D.

### **Latent‑Space**  
The high‑dimensional vector space representing the internal state of a control policy at a given timestep.

### **Coherence Surface**  
A stable region in latent space where trajectories maintain structural continuity across time or sensor variation.

---

## **2. Primitive Terms**

### **Dimensional Primitive (DP)**  
The minimal unit of latent‑space structure, capturing local coherence, variance behavior, and projection stability.

### **Triadic Dimensional Primitive (TDP)**  
A triad of DPs forming the smallest unit capable of expressing full control‑regime behavior (R₁, R₂, R₃).

### **Scaling Primitive (SP)**  
A rule‑based expansion unit that preserves invariants during dimensional scaling (e.g., architecture width, recurrent depth, modality count).

### **Coherence Primitive (CP)**  
A minimal unit identifying stable, transitional, or dispersed regions in high‑dimensional latent space.

---

## **3. Core Terms**

### **Triadic Dimensional Core (TDC)**  
The 3D–9D substrate composed of one or more TDPs, used for interpretable projection of latent states.

### **3D Structural Core**  
Captures motif‑level geometry in latent activations.

### **6D Interaction Core**  
Captures relational and sensor‑to‑action structure across modalities.

### **9D Coherence Core**  
Captures pathway‑level coherence across time and sensorimotor loops.

---

## **4. Regime Terms**

### **High‑Dimensional Regimes (R₁ᴴ, R₂ᴴ, R₃ᴴ)**  
The triadic regime structure expressed in 64D–1024D latent spaces.

### **Stable Regime (R₁ / R₁ᴴ)**  
Compact, coherent, low‑variance latent behavior.

### **Transition Regime (R₂ / R₂ᴴ)**  
Branching, oscillatory, or reorientation behavior across time or sensor conditions.

### **Dispersion Regime (R₃ / R₃ᴴ)**  
Diffuse, fragmented, or unstable latent behavior.

---

## **5. Scaling Terms**

### **Scaling Behavior**  
The structured expansion of latent‑space capacity as policy size, architecture depth, or modality count increases.

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

### **Timestep‑to‑Timestep Alignment**  
Comparison of latent states across time.

### **Cross‑Checkpoint Alignment**  
Comparison of latent‑space structure across training checkpoints.

### **Cross‑Architecture Alignment**  
Comparison of latent‑space geometry across different policy architectures.

### **Cross‑Hardware Alignment**  
Comparison of policy behavior across different embodiments or sensor configurations.

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
