### *vST for Embedding Stores & Vector Databases*  
### *Terminology*

This appendix defines the terminology used throughout the *vST for Embedding Stores & Vector Databases* artifact. Terms are presented in a substrate‑agnostic, model‑independent manner and apply to any embedding store or vector database operating across the full dimensional ladder (3D → 1024D). Definitions emphasize primitive‑level structure, cluster regimes, scaling continuity, retrieval‑path geometry, and invariant preservation.

---

## **1. Substrate Terms**

### **Embedding‑Store Substrate**  
A structured, invariant‑preserving framework for representing and interpreting embedding spaces across 64D–1024D.

### **Embedding Space**  
The high‑dimensional vector space representing embeddings produced by a model.

### **Coherence Surface**  
A stable region in embedding space where vectors maintain structural continuity across clusters, neighborhoods, or index partitions.

---

## **2. Primitive Terms**

### **Dimensional Primitive (DP)**  
The minimal unit of embedding‑space structure, capturing local coherence, variance behavior, and projection stability.

### **Triadic Dimensional Primitive (TDP)**  
A triad of DPs forming the smallest unit capable of expressing full cluster‑regime behavior (R₁, R₂, R₃).

### **Scaling Primitive (SP)**  
A rule‑based expansion unit that preserves invariants during dimensional scaling (e.g., embedding‑model dimensionality, index‑structure complexity).

### **Coherence Primitive (CP)**  
A minimal unit identifying stable, transitional, or dispersed regions in high‑dimensional embedding space.

---

## **3. Core Terms**

### **Triadic Dimensional Core (TDC)**  
The 3D–9D substrate composed of one or more TDPs, used for interpretable projection of embedding states.

### **3D Structural Core**  
Captures motif‑level geometry in cluster interiors.

### **6D Interaction Core**  
Captures relational and cross‑cluster structure across boundaries and index partitions.

### **9D Coherence Core**  
Captures pathway‑level coherence across retrieval neighborhoods.

---

## **4. Regime Terms**

### **High‑Dimensional Regimes (R₁ᴴ, R₂ᴴ, R₃ᴴ)**  
The triadic regime structure expressed in 64D–1024D embedding spaces.

### **Stable Regime (R₁ / R₁ᴴ)**  
Compact, coherent, low‑variance cluster behavior.

### **Boundary/Transition Regime (R₂ / R₂ᴴ)**  
Branching, oscillatory, or reorientation behavior across cluster boundaries or semantic‑overlap zones.

### **Dispersed/Outlier Regime (R₃ / R₃ᴴ)**  
Diffuse, fragmented, or unstable embedding behavior.

---

## **5. Scaling Terms**

### **Scaling Behavior**  
The structured expansion of embedding‑space capacity as dimensionality, model complexity, or index size increases.

### **Scaling Regimes (S₁, S₂, S₃)**  
Triadic scaling behavior describing stable, transitional, and dispersion‑prone scaling phases.

### **Dimensional Continuity**  
The requirement that embedding‑space expansion remains smooth and invariant‑preserving across the dimensional ladder.

---

## **6. Projection Terms**

### **Invertible Projection**  
A projection from high‑dimensional embedding space into 3D–9D that preserves primitive‑level structure and regime identity.

### **Regime‑Aware Projection**  
A projection that maintains correct mapping of R₁, R₂, and R₃ behaviors.

### **Primitive‑Aligned Projection**  
A projection that preserves DP, TDP, SP, and CP structure.

---

## **7. Alignment Terms**

### **Cross‑Index Alignment**  
Comparison of embedding‑space structure across different index structures (HNSW, IVF, PQ, etc.).

### **Cross‑Version Alignment**  
Comparison of embeddings across model updates or dimensionality changes.

### **Cross‑Partition Alignment**  
Comparison of retrieval behavior across index partitions.

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
