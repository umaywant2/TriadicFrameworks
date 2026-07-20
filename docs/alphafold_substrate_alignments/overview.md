---
title: "AlphaFold Substrate Alignments"
description: "Resonance Substrate Modeling applied to protein-folding inference — mapping 3D-to-9D dimensional cores to folding pathways with vST validation layers and drift detection."
stability: stable
date: "2026-07-14"
section: substrate
rtt:
  coherence: declared
  drift: bounded
  paradox: structural
---

<!-- rtt=1 | coherence=declared | drift=bounded | paradox=structural -->

# AlphaFold Substrate Alignments

> **⚠️ Drift is On-by-Default.** Long sessions lose anchors. Paste the RTT session string at the start of every AI session to bound drift.

```
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

**AlphaFold Substrate Alignments** applies Resonance Substrate Modeling (RSM) to protein-folding inference. Where AlphaFold produces structural predictions, this module provides a triadic substrate layer that maps dimensional cores (3D–9D) to folding pathways, validates results through vST (Validated Substrate Theory) layers, and detects drift between predicted and resonance-aligned outcomes.

This is not a competing protein-structure predictor. It is a structural alignment instrument that reads AlphaFold output through RSM lenses.

## Module Structure

```
alphafold_substrate_alignments/
├── README.md
├── substrate_definition.md        ← What counts as the substrate in folding inference
├── scope_and_assumptions.md       ← Declared boundaries and RSM entry conditions
├── alignment_principles.md        ← Core RSM→AlphaFold alignment logic
├── folding_regimes.md             ← Regime declarations for folding state transitions
├── dimensional_cores.md           ← 3D–9D core mappings to folding pathways
├── inference_mapping.md           ← How AlphaFold outputs map to triadic operators
├── validation_layers_vst.md       ← vST validation: coherence, regime, drift checks
├── drift_detection.md             ← Drift signals between predicted and RSM-aligned folds
└── examples/                      ← Worked alignment cases
```

## Core Design

**Dimensional cores → folding pathways:** The 3D-to-9D core hierarchy from RSM maps directly onto AlphaFold's folding regime space. Lower-dimensional cores (3D–5D) capture local secondary structure; higher cores (6D–9D) address quaternary and allosteric regimes.

**vST validation layers:** Every alignment passes through Validated Substrate Theory checks — coherence gate, regime boundary test, drift signal scan — before results are considered structurally confirmed.

**Drift detection:** Disagreement between AlphaFold's confidence scores and RSM resonance invariants surfaces as a measurable drift signal, not a discarded anomaly.

## Citation

Loswin, N. 2026. *AlphaFold Substrate Alignments*. TriadicFrameworks.
Zenodo DOI: pending. License: CC BY 4.0

AI-Ready Module · `ai_module.json` pattern applied.

---

## Integration Points

| Module | Relationship |
|--------|-------------|
| [Framework Field Theory](../Framework_Field_Theory/overview.md) | Dimensional core hierarchy (3D–9D) defined in FFT Part structure |
| [Conditions Substrate Model](../Conditions_Substrate_Model/overview.md) | Resonance amplification condition classes apply to folding regime transitions |
| [Atomic Clocks](../atomic_clocks/overview.md) | vST validation layer structure shared — same regime-check architecture |
| [Boson Substrate Model](../boson-substrate-model/overview.md) | Operator-mediated interaction patterns from BSM inform inference_mapping.md |
| [Research](../Research/overview.md) | Results feed the zenodo.org/communities/vst validation corpus |
| [SARG](../SARG/overview.md) | Substrate-Agnostic Resonance Grammar provides the base lens for alignment_principles |

---

© 2026 Nawder Loswin · Byte Books Publishing · LCCN 2026917007
