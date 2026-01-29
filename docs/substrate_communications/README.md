# Substrate Communications  
_A minimal structural framework for drift‑aware, paradox‑preserving messaging across heterogeneous systems._

This directory contains the canonical, self‑contained materials for **Substrate Communications**, a minimal message grammar designed for systems operating under:

- low bandwidth  
- high latency  
- intermittent connectivity  
- heterogeneous hardware  
- long‑term drift  

Substrate Communications does not transmit raw telemetry.  
It transmits **structural summaries** that preserve invariants, drift, and paradox.

## Contents

- `substrate_comms_core.md` — core concepts and framing  
- `message_types.md` — minimal message formats  
- `regime_mapping.md` — triadic interpretation across scales  
- `citation.cff` — citation metadata  
- `zenodo.json` — DOI metadata

All files are intentionally minimal and version‑stable.

For a narrative example, see the exploratory write‑up in docs/_ideas/0_Substrate_Communications.md

## Contributor Onboarding (Minimal)

This directory contains the canonical, minimal definition of Substrate Communications.  
To keep the structure stable:

- keep additions **conceptual, not implementation‑specific**  
- avoid adding domain‑specific examples directly to this folder  
- place applied or extended use‑cases in separate directories  
- preserve the minimal message types and triadic mapping  
- do not expand the grammar beyond what is defined here  

This folder anchors the **core substrate‑comms grammar**.  
Extensions should build outward, not modify the core.
