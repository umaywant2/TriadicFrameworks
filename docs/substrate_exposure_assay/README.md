# Substrate Exposure Assay  
_A minimal RTT/vST‑aligned protocol for observing structural behavior across AI models._

This directory contains the canonical, self‑contained materials for the **Substrate Exposure Assay**, a minimal method for evaluating how different AI models behave when exposed to a shared set of substrate‑aware prompts.

The assay does not measure accuracy, capability, or performance.  
It measures **regimes**, **drift**, and **paradox** — the structural signatures of behavior under exposure.

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
