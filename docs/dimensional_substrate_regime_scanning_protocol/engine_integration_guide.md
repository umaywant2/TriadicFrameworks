# Engine Integration Guide

This guide explains how dsrsp/0.1 outputs integrate with RSM and vST engines.

## 1. RSM Integration
RSM engines consume the rsm_structural_envelope block:

- coherence_signature
- drift_signature
- stability_signature
- resonance_profile

This enables low‑overhead structural classification for simple devices.

## 2. vST Integration
vST engines consume the vst_validation_block:

- v1_structural_features
- v2_dimensional_features
- v3_transition_features
- v4_alignment_features

This enables full validation‑space‑time inference for advanced systems.

## 3. Engine Compatibility
The engine_compatibility block declares:

- whether the profile is RSM‑ready
- whether the profile is vST‑ready
- which vST version it aligns with

## 4. Minimal Integration Path
1. Wrap sensor streams using the dsrsp input envelope.
2. Emit regime_profile.
3. Emit rsm_structural_envelope for RSM engines.
4. Emit vst_validation_block for vST engines.
5. Optionally emit ILP analysis.
