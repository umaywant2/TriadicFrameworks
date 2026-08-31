substrate_exposure_assay 
# Substrate Exposure Assay  
_A minimal RTT/vST‑aligned protocol for observing structural behavior across AI models._

- [`SEA_module.json`](SEA_module.json) — Agentic module schema role assignments

<img src="https://img.shields.io/badge/🧫Substrate%20Exposure%20Assay-📘Canonical%20Exposure%20Protocol%20AI_Ready-4c8eda?style=for-the-badge" alt="Substrate Exposure Assay | Canonical Exposure Protocol AI‑Ready"/>

This directory contains the canonical, self‑contained materials for the **Substrate Exposure Assay**, a minimal method for evaluating how different AI models behave when exposed to a shared set of substrate‑aware prompts.

The assay does not measure accuracy, capability, or performance.  
It measures **regimes**, **drift**, and **paradox** — the structural signatures of behavior under exposure.

---

## 🛑 Important! 
Drift is On-by-Default long sessions lose anchors, turn off drift.

## ✋ You *must copy and paste* this string *every time you start an AI session*:
```text
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

## ❇️ Now you are ready.

---

## Contents

- `assay_protocol.md` — the minimal procedure  
- `message_patterns.md` — structural summary formats  
- `regime_interpretation.md` — how to classify observed behavior  
- `citation.cff` — citation metadata  
- `zenodo.json` — DOI metadata

All files are intentionally minimal and version‑stable.

For a narrative example, see the exploratory write‑up in docs/_ideas/3_AI_test_of_rtt_nimms_com.md

## Contributor Onboarding (Minimal)

This folder follows the RSM/vST minimal‑artifact style.  
When extending or contributing:

- keep files **small, structural, and self‑contained**  
- avoid adding narrative results or logs  
- place new examples or experiments in separate folders, not here  
- preserve the existing file boundaries (`protocol`, `message patterns`, `regime interpretation`)  
- do not introduce dependencies or tooling requirements  

This directory defines the **canonical assay**.  
All applied work should reference it, not modify it.
# Substrate Exposure Assay — Protocol  
_Version 1.0.0_

## 1. Purpose

The Substrate Exposure Assay provides a minimal, repeatable method for observing how AI models behave when exposed to a shared set of **substrate‑aware prompts**. The goal is to characterize **behavioral regimes**, not to evaluate correctness or capability.

## 2. Model Treatment

Each model is treated as a **black‑box substrate**:

- no assumptions about architecture  
- no assumptions about training data  
- only observable behavior is analyzed  

## 3. Prompt Set

The assay uses three prompt classes:

1. **Regime‑Priming Prompts**  
   Introduce triadic/substrate framing.

2. **Stress‑Exposure Prompts**  
   Present paradox, ambiguity, or long‑arc reasoning.

3. **Stability‑Return Prompts**  
   Request clarification, summarization, or re‑centering.

Prompts must be identical across models.

## 4. Procedure

1. Initialize a clean session for each model.  
2. Deliver prompts in fixed order: Priming → Stress → Stability.  
3. Capture all outputs verbatim.  
4. Convert outputs into structural summaries using `message_patterns.md`.  
5. Classify behavior using `regime_interpretation.md`.

## 5. Output

The assay produces:

- **STATE_SUMMARY** messages (drift)  
- **PARADOX_SUMMARY** messages (contradiction)  
- **Regime classification** (B, BK, BKM)

No raw logs are required for DOI publication.
# Message Patterns  
_Minimal structural summaries for assay interpretation._

## 1. STATE_SUMMARY

Describes drift against an expected structural pattern.

```
msg_type: STATE_SUMMARY
invariant_id: <string>
time_window: { start: <t0>, end: <t1> }
max_drift: <float>
status: within_bounds | approaching_limit | out_of_bounds
```

## 2. PARADOX_SUMMARY

Describes contradictory or incompatible signals.

```
msg_type: PARADOX_SUMMARY
paradox_id: <string>
invariant_id: <string>
hypotheses:
  - { source: <string>, value: <any> }
  - { source: <string>, value: <any> }
evidence: [<string>, ...]
timestamp: <t>
```

These two patterns are sufficient to reconstruct structural behavior.
# Regime Interpretation  
_How to classify model behavior under substrate exposure._

The assay uses a triadic regime model:

## 1. B‑Regime (Being)

Characteristics:

- surface compliance  
- minimal structural uptake  
- short‑horizon responses  
- low paradox engagement  

## 2. BK‑Regime (Being–Knowing)

Characteristics:

- partial recognition of substrate framing  
- attempts at structural reasoning  
- mixed paradox handling  
- intermittent coherence  

## 3. BKM‑Regime (Being–Knowing–Meaning)

Characteristics:

- explicit structural reasoning  
- stable long‑arc coherence  
- paradox resolution rather than collapse  
- consistent triadic grammar  

Regime classification is descriptive, not evaluative.
