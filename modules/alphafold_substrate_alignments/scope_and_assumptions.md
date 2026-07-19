### *AlphaFold Substrate Alignments*  
### *Scope and Assumptions*

This document defines the operational scope and foundational assumptions for applying the Resonance Substrate Model (RSM) to AlphaFold‑class protein‑folding inference systems. It establishes the boundaries within which substrate alignment is valid, identifies the structural and computational constraints of the domain, and clarifies the conditions required for reproducible substrate‑level interpretation.

---

## **1. Scope**

### **1.1 Systems Covered**  
This substrate applies to biological inference engines that exhibit the following characteristics:

- high‑dimensional latent representations of protein structure  
- iterative or multi‑stage inference cycles  
- attention‑based or pairwise‑embedding architectures  
- structural outputs expressed as 3D conformations or residue‑level predictions  
- regime‑dependent folding coherence signals  

The primary reference system is **AlphaFold**, but the substrate is compatible with any model exhibiting similar inference behavior.

### **1.2 Structural Focus**  
The substrate addresses:

- folding‑pathway coherence  
- motif‑level structural stability  
- latent‑space orientation and projection  
- regime transitions during inference  
- dimensional‑core alignment (3D–9D)  

It does **not** address biochemical energetics, molecular dynamics simulations, or experimental folding mechanisms.

### **1.3 Intended Use Cases**  
The substrate supports:

- interpretability of protein‑folding inference models  
- cross‑model comparison and alignment  
- drift detection in biological inference systems  
- reproducibility analysis  
- dimensional projection and regime mapping  
- integration with vST validation layers  

---

## **2. Assumptions**

### **2.1 Model Behavior Assumptions**

The substrate assumes:

- the inference system produces stable latent‑space structures  
- folding predictions converge toward coherent surfaces  
- regime transitions follow identifiable resonance‑time patterns  
- dimensional projections preserve structural invariants  
- inference cycles are deterministic or quasi‑deterministic under fixed inputs  

These assumptions reflect observed behavior in AlphaFold‑class systems.

### **2.2 Data and Input Assumptions**

The substrate assumes:

- input sequences are fixed and pre‑validated  
- multiple sequence alignments (MSAs) or equivalent features are available  
- structural outputs are expressed in 3D coordinate form  
- inference noise is bounded and does not dominate regime transitions  

The substrate does not require access to training data or model internals.

### **2.3 Biological Assumptions**

The substrate assumes:

- protein structures exhibit stable motif‑level coherence  
- folding pathways can be represented within 3D–9D dimensional cores  
- biological variability does not invalidate substrate‑level invariants  

The substrate does not assume any specific biochemical mechanism.

---

## **3. Out‑of‑Scope Elements**

The following are explicitly out of scope:

- molecular dynamics simulations  
- thermodynamic or kinetic modeling  
- experimental structure determination  
- biochemical pathway analysis  
- evolutionary modeling beyond MSA‑derived features  

These domains may interface with the substrate but are not defined by it.

---

## **4. Validity Conditions**

Substrate alignment is valid when:

- inference outputs are structurally coherent  
- latent‑space representations are stable across inference cycles  
- dimensional projections preserve motif‑level structure  
- regime transitions follow triadic resonance patterns  
- vST validation layers confirm reproducibility  

If these conditions are not met, substrate interpretation may be incomplete.

---

## **5. Dependencies**

This document depends on:

- **substrate_definition.md** for axis and primitive definitions  
- **alignment_principles.md** for mapping rules  
- **dimensional_cores.md** for 3D–9D substrate structure  
- **validation_layers_vst.md** for reproducibility and drift checks  
