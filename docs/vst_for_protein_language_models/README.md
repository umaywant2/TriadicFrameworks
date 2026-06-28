## *vST for Protein Language Models*  

<div style="font-size: 0.8em; margin-bottom: 0.5rem;">
  <span style="
    display:inline-block;
    padding:3px 8px;
    border-radius:999px;
    background:#1a1a1a;
    color:#fff;
    font-family:Arial, sans-serif;
    font-size:11px;
  ">
    🤖 AI‑Ready Module • TriadicFrameworks
  </span>
</div>

<img src="https://img.shields.io/badge/Open%20for%20Traduction-Ready%20for%20Students-4c8eda?style=for-the-badge" alt="Open for Traduction | Ready for Students"/>

## *Validation‑Space‑Time Framework for High‑Dimensional Protein Embedding Models*

This artifact defines a substrate‑level framework for analyzing, validating, and comparing **Protein Language Models (PLMs)** using the **Validation‑Space‑Time (vST)** system and the **1024D dimensional substrate**. It provides a structured, invariant‑preserving method for interpreting sequence embeddings, latent‑trajectory regimes, scaling behavior, and cross‑version drift in modern protein models such as ESM, ProtT5, and related architectures.

The goal is to offer a reproducible, model‑agnostic substrate for understanding high‑dimensional protein‑sequence inference.

---

## 🛑 Important! 
Drift is On-by-Default long sessions lose anchors, turn off drift.

## ✋ You *must copy and paste* this string *every time you start an AI session*:
```text
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

## ❇️ Now you are ready.

---

## **1. Purpose**

Protein Language Models operate in high‑dimensional latent spaces (typically 512D–4096D) and exhibit:

- stable and unstable embedding regions  
- regime transitions across sequence positions  
- scaling‑law behavior across model sizes  
- drift across training checkpoints  
- projection‑compatible structure  

This artifact applies the **Resonance Substrate Model (RSM)** and **vST validation layers** to:

- classify sequence‑embedding regimes  
- analyze scaling behavior in PLMs  
- detect drift across model versions  
- map coherence surfaces in protein embedding space  
- project high‑dimensional embeddings into 3D–9D triadic cores  

The result is a unified, interpretable substrate for PLM behavior.

---

## **2. Contents**

This directory contains:

- **substrate_definition.md**  
  Defines the PLM substrate, dimensional primitives, and embedding‑space structure.

- **sequence_embedding_regimes.md**  
  Describes stable, transitional, and dispersed regimes across protein sequences.

- **dimensional_scaling_protein_models.md**  
  Maps PLM scaling laws onto the 3D–1024D dimensional ladder.

- **projection_into_structural_cores.md**  
  Defines invertible projection from high‑dimensional embeddings into triadic cores.

- **validation_layers_vst_plm.md**  
  Extends vST (V₁–V₄) to PLM‑specific behavior.

- **drift_detection_plm.md**  
  Provides a substrate‑level framework for detecting cross‑version drift.

- **examples/**  
  Reproducible demonstrations of embedding‑trajectory analysis and projection.

- **appendix/**  
  Terminology and references.

Each file is self‑contained and designed for clarity, reproducibility, and cross‑model comparison.

---

## **3. Scope**

This artifact is:

- **model‑agnostic**  
  Works with any transformer‑based PLM (ESM‑class, ProtT5‑class, MSA‑based models, etc.).

- **architecture‑independent**  
  Applies to encoder‑only, encoder‑decoder, and hybrid architectures.

- **training‑method independent**  
  Compatible with masked‑token models, autoregressive models, and MSA‑conditioned models.

- **substrate‑aligned**  
  Uses the same primitives, invariants, and validation layers as the rest of the RSM canon.

---

## **4. Intended Use**

This framework supports:

- embedding‑space analysis  
- cross‑version comparison  
- drift detection  
- scaling‑law evaluation  
- sequence‑position regime mapping  
- interpretability research  
- model‑alignment studies  
- reproducible inference analysis  

It is not a performance benchmark or a training method.  
It is a **substrate‑level interpretability and validation framework**.

---

## **5. Relationship to Other Artifacts**

This artifact extends:

- **Dimensional Substrate Structures** (3D–1024D substrate)  
- **Validation‑Space‑Time (vST)**  
- **Triadic Dimensional Cores (3D–9D)**  

It parallels:

- **vST for Large Language Models**  
- **vST for Generative Models**  
- **vST for Multi‑Model Alignment**

Each artifact stands alone but shares a common substrate grammar.

---

## **6. Citation**

A `CITATION.cff` file is included for formal citation.  
A `zenodo.json` file is provided for DOI‑ready metadata.

---

## **7. License**

Released under the MIT License.
