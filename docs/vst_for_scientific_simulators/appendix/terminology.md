### *vST for Scientific Simulators*  
### *Terminology*

This appendix defines the terminology used throughout the *vST for Scientific Simulators* artifact. Terms are presented in a substrate‑agnostic, model‑independent manner and apply to any high‑dimensional simulator operating across the full dimensional ladder (3D → 1024D). Definitions emphasize primitive‑level structure, regime behavior, scaling continuity, and invariant preservation.

---

## **1. Substrate Terms**

### **Simulator Substrate**  
A structured, invariant‑preserving framework for representing and interpreting simulation state‑spaces across 64D–1024D.

### **State‑Space**  
The high‑dimensional vector space representing the simulator’s physical, numerical, or multi‑field state at a given timestep or solver iteration.

### **Coherence Surface**  
A stable region in state‑space where trajectories maintain structural continuity across time, space, or solver iterations.

---

## **2. Primitive Terms**

### **Dimensional Primitive (DP)**  
The minimal unit of simulation‑state structure, capturing local coherence, variance behavior, and projection stability.

### **Triadic Dimensional Primitive (TDP)**  
A triad of DPs forming the smallest unit capable of expressing full dynamical regime behavior (R₁, R₂, R₃).

### **Scaling Primitive (SP)**  
A rule‑based expansion unit that preserves invariants during dimensional scaling (e.g., grid refinement, timestep reduction, solver‑order changes).

### **Coherence Primitive (CP)**  
A minimal unit identifying stable, transitional, or dispersed regions in high‑dimensional simulation state‑space.

---

## **3. Core Terms**

### **Triadic Dimensional Core (TDC)**  
The 3D–9D substrate composed of one or more TDPs, used for interpretable projection of simulation states.

### **3D Structural Core**  
Captures motif‑level geometry in spatial or particle‑level fields.

### **6D Interaction Core**  
Captures relational and solver‑driven structure across fields, particles, or spatial domains.

### **9D Coherence Core**  
Captures pathway‑level coherence across time, space, or solver iterations.

---

## **4. Regime Terms**

### **High‑Dimensional Regimes (R₁ᴴ, R₂ᴴ, R₃ᴴ)**  
The triadic regime structure expressed in 64D–1024D simulation state‑spaces.

### **Stable Regime (R₁ / R₁ᴴ)**  
Compact, coherent, low‑variance state behavior.

### **Transition Regime (R₂ / R₂ᴴ)**  
Branching, oscillatory, or reorientation behavior across time or space.

### **Dispersion Regime (R₃ / R₃ᴴ)**  
Diffuse, fragmented, or unstable state behavior.

---

## **5. Scaling Terms**

### **Scaling Behavior**  
The structured expansion of state‑space capacity as grid resolution, timestep refinement, or solver complexity increases.

### **Scaling Regimes (S₁, S₂, S₃)**  
Triadic scaling behavior describing stable, transitional, and dispersion‑prone scaling phases.

### **Dimensional Continuity**  
The requirement that state‑space expansion remains smooth and invariant‑preserving across the dimensional ladder.

---

## **6. Projection Terms**

### **Invertible Projection**  
A projection from high‑dimensional state‑space into 3D–9D that preserves primitive‑level structure and regime identity.

### **Regime‑Aware Projection**  
A projection that maintains correct mapping of R₁, R₂, and R₃ behaviors.

### **Primitive‑Aligned Projection**  
A projection that preserves DP, TDP, SP, and CP structure.

---

## **7. Alignment Terms**

### **Iteration‑to‑Iteration Alignment**  
Comparison of simulation states across solver iterations or timesteps.

### **Spatial/Particle Alignment**  
Comparison of states across spatial regions or particle subsets.

### **Cross‑Resolution Alignment**  
Comparison of state‑space structure across grid refinements or timestep reductions.

### **Cross‑Version Alignment**  
Comparison of simulation behavior across code revisions, solver changes, or parameterizations.

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
