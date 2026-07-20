### *vST for Protein Language Models*  
### *Substrate Definition*

This document defines the substrate used to analyze **Protein Language Models (PLMs)** within the **Validation‑Space‑Time (vST)** framework and the **1024D dimensional substrate**. It establishes the primitives, dimensional cores, scaling behavior, and embedding‑trajectory structure required to interpret PLM inference in a stable, invariant‑preserving manner.

The substrate is model‑agnostic and applies to any transformer‑based PLM, including ESM‑class, ProtT5‑class, and MSA‑conditioned architectures.

---

## **1. Purpose of the PLM Substrate**

The PLM substrate provides a structured, reproducible framework for:

- interpreting high‑dimensional sequence embeddings  
- identifying stable, transitional, and dispersed embedding regimes  
- mapping coherence surfaces across sequence positions  
- analyzing scaling behavior across model sizes  
- detecting drift across checkpoints or versions  
- projecting high‑dimensional embeddings into 3D–9D triadic cores  

Protein embeddings are high‑dimensional, structured, and regime‑rich.  
The substrate ensures they remain interpretable across the full dimensional ladder (3D → 1024D).

---

## **2. Substrate Overview**

PLMs operate in latent spaces typically ranging from 512D to 4096D.  
The substrate models these spaces using:

- **Dimensional Primitives (DP)**  
- **Triadic Dimensional Primitives (TDP)**  
- **Scaling Primitives (SP)**  
- **Coherence Primitives (CP)**  

These primitives define the structure of embedding trajectories, coherence surfaces, and regime transitions.

The substrate is anchored by the **Triadic Dimensional Cores**:

- **3D Structural Core**  
- **6D Interaction Core**  
- **9D Coherence Core**

and extended through the **1024D high‑dimensional substrate**.

---

## **3. Dimensional Primitives for PLMs**

### **3.1 Dimensional Primitive (DP)**  
A DP represents the minimal unit of embedding‑space structure.  
It captures:

- local coherence across residues  
- variance behavior  
- projection stability  
- regime alignment  

DPs appear in token embeddings, attention outputs, and MLP activations.

---

### **3.2 Triadic Dimensional Primitive (TDP)**  
A TDP is a triad of DPs that expresses full regime behavior.  
It captures:

- stable (R₁) behavior  
- transitional (R₂) behavior  
- dispersed (R₃) behavior  

TDPs form the basis of the 3D–9D triadic cores.

---

### **3.3 Scaling Primitive (SP)**  
An SP governs dimensional expansion from 9D → 64D → 1024D.  
It ensures:

- invariant‑preserving scaling  
- continuity of coherence surfaces  
- stable projection into triadic cores  

SPs model how PLM embedding spaces expand with model size.

---

### **3.4 Coherence Primitive (CP)**  
A CP identifies stable or unstable regions in embedding space.  
It captures:

- coherence surfaces across residues  
- branching behavior  
- dispersion patterns  
- regime transitions  

CPs are essential for drift detection and vST validation.

---

## **4. Triadic Dimensional Cores for PLMs**

### **4.1 3D Structural Core**  
Captures motif‑level geometry in embedding trajectories:

- compact geometric patterns  
- local coherence  
- stable projections  

### **4.2 6D Interaction Core**  
Captures relational and attention‑level structure:

- residue‑interaction surfaces  
- branching behavior  
- early regime transitions  

### **4.3 9D Coherence Core**  
Captures pathway‑level coherence:

- resonance‑time behavior  
- stable regime classification  
- invertible projection from higher dimensions  

The 9D core is the anchor for all high‑dimensional interpretation.

---

## **5. High‑Dimensional Substrate (64D–1024D)**

PLM embedding spaces naturally inhabit high‑dimensional regimes.  
The substrate models these using the dimensional ladder:

- **64D** — research‑grade embedding substrate  
- **128D** — expanded coherence surfaces  
- **256D** — multi‑primitive interaction  
- **512D** — high‑variance embedding regions  
- **1024D** — full research‑grade capacity  

Each step preserves:

- structural invariants  
- resonance‑time invariants  
- projection invariants  
- scaling invariants  

This ensures stable interpretation across model sizes.

---

## **6. Embedding‑Trajectory Structure**

PLM inference produces embedding trajectories that move through:

- compact stable regions (R₁ᴴ)  
- branching transitional regions (R₂ᴴ)  
- dispersed or unstable regions (R₃ᴴ)  

These trajectories are modeled as:

- sequences of DPs  
- grouped into TDPs  
- expanded through SPs  
- classified using CPs  

This structure enables regime‑aware analysis and drift detection.

---

## **7. Projection into Triadic Cores**

High‑dimensional embeddings are projected into:

- **9D** for coherence analysis  
- **6D** for interaction analysis  
- **3D** for geometric interpretation  

Projection must remain:

- invertible  
- primitive‑aligned  
- regime‑aware  
- invariant‑preserving  

Projection is essential for interpretability and vST validation.

---

## **8. Substrate Outputs**

The PLM substrate produces:

- embedding‑trajectory regime classifications  
- coherence‑surface maps  
- scaling‑law diagnostics  
- projection‑stability indicators  
- drift‑detection signals  
- vST validation outputs  

These outputs support reproducible, substrate‑level analysis of PLM inference.
