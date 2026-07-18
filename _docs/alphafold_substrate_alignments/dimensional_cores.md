### *AlphaFold Substrate Alignments*  
### *Dimensional Cores*

This document defines the dimensional cores used to interpret protein‑folding inference systems within the Resonance Substrate Model (RSM). Dimensional cores provide the structural basis for projecting high‑dimensional latent‑space representations into stable, interpretable geometric substrates. For AlphaFold‑class models, dimensional cores anchor folding coherence, motif‑level structure, and regime‑transition behavior.

---

## **1. Purpose of Dimensional Cores**

Dimensional cores serve three primary functions:

- provide a stable geometric substrate for folding interpretation  
- preserve motif‑level structure during projection from high‑dimensional latent spaces  
- support regime classification and resonance‑time analysis  

The cores ensure that folding predictions remain interpretable across inference cycles and model variants.

---

## **2. Core Dimensional Structure**

The AlphaFold substrate uses a **3D–9D triadic dimensional core**, defined as follows:

### **2.1 3D Structural Core**  
Represents the physical geometry of protein conformations.  
Includes:

- backbone coordinates  
- side‑chain orientation  
- local motif geometry  

This core anchors all structural projections.

### **2.2 6D Interaction Core**  
Extends the 3D core to capture interaction‑level structure.  
Includes:

- residue‑pair relationships  
- orientation‑pair embeddings  
- local‑to‑global interaction patterns  

This core corresponds to the latent‑space structures used in folding inference.

### **2.3 9D Coherence Core**  
Represents the minimal dimensional substrate required to capture folding‑pathway coherence.  
Includes:

- motif‑level stability signals  
- regime‑transition indicators  
- resonance‑time alignment patterns  

The 9D core is the highest‑resolution substrate used for folding interpretation.

---

## **3. Projection Principles**

Dimensional projection follows three rules:

### **3.1 Structure‑Preserving Projection**  
Projections from high‑dimensional latent space into 3D–9D cores must preserve:

- motif‑level geometry  
- backbone continuity  
- residue‑interaction coherence  

### **3.2 Regime‑Aware Projection**  
Projection must maintain regime identity:

- R₁ → stable geometric surfaces  
- R₂ → transitional structures  
- R₃ → dispersed or unstable projections  

### **3.3 Invariant‑Aligned Projection**  
Projection must preserve substrate invariants, including:

- resonance‑time patterns  
- motif‑level stability  
- latent‑space orientation consistency  

---

## **4. High‑Dimensional Extensions**

Although the core substrate is 3D–9D, AlphaFold’s latent space often operates in higher dimensions (e.g., 32D–128D).  
High‑dimensional extensions follow these principles:

- projections must remain invertible at the motif level  
- coherence surfaces must remain identifiable  
- regime transitions must remain detectable  
- substrate invariants must remain stable  

These extensions allow the substrate to interpret complex inference behaviors without losing structural clarity.

---

## **5. Dimensional‑Core Behavior Across Regimes**

Dimensional cores interact with folding regimes as follows:

- **R₁ (Stable):** full alignment with 3D–9D cores; projections are compact and coherent  
- **R₂ (Transition):** partial alignment; projections show branching or oscillatory structure  
- **R₃ (High‑Uncertainty):** weak alignment; projections disperse across higher‑dimensional space  

This behavior supports regime classification and drift detection.

---

## **6. Integration with Substrate Primitives**

Dimensional cores integrate with:

- **Structural Axis (S‑axis):** geometric projection  
- **Inference Axis (I‑axis):** latent‑space mapping  
- **Resonance‑Time Axis (R‑axis):** regime‑transition interpretation  

Together, these axes form the SIR substrate triad used throughout this artifact.

---

## **7. Outputs of Dimensional‑Core Analysis**

Dimensional‑core analysis produces:

- stable structural projections  
- regime‑aware folding interpretations  
- coherence‑surface identification  
- high‑dimensional alignment diagnostics  
- substrate‑level validation signals  

These outputs integrate with vST validation layers and downstream substrate artifacts.
