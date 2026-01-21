# Dimensional Substrate Regime Scanning Protocol (dsrsp/0.1)

## 1. Purpose
Provide a minimal, standards‑friendly wire format for regime‑aware scanning that 
integrates cleanly with RSM and vST engines.

## 2. Input Envelope
Defines how raw sensor streams are wrapped for processing.

## 3. Output Regime Profile
A structured summary using the triadic axes:
- structural_regime
- sensory_regime
- environmental_regime
- drift_indicators

## 4. Alignment Layer

### 4.1 RSM Structural Envelope
A compact summary for RSM engines:

rsm_structural_envelope:
  coherence_signature: <vector or hash>
  drift_signature: <vector or hash>
  stability_signature: <vector or hash>
  resonance_profile: <optional spectral summary>

### 4.2 vST Validation Block
A richer feature set for vST engines:

vst_validation_block:
  v1_structural_features: [...]
  v2_dimensional_features: [...]
  v3_transition_features: [...]
  v4_alignment_features: [...]

### 4.3 Engine Compatibility Declaration
engine_compatibility:
  rsm: true
  vst: true
  vst_version: "1.x"

## 5. Processing Pipeline
1. ingest
2. feature extraction
3. regime inference
4. profile emission
5. optional ILP analysis

## 6. Extensions
- ILP module (optional)
- planetary regime profiles
- synthetic regime detection
