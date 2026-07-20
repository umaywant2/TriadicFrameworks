# Analyzer Examples

> **Module path:** `Framework_Field_Theory/Analyzer/Examples/`
> **Parent module:** [FFT Analyzer](../README.md)
> **Layer:** Core Frameworks — Structural Spine

---

## Metadata

```yaml
module: FFT Analyzer — Examples
parent_module: FFT Analyzer
layer: Core Frameworks — Structural Spine
version: 2026.2
status: Active, Canonical
example_types:
  - operator analysis examples
  - dimensional analysis examples
  - regime analysis examples
  - drift analysis examples
  - coherence analysis examples

session_context:
  drift_sensitivity: medium
  regime_sensitivity: medium
  dimensional_envelope: D0–D7
  coherence_requirements:
    - examples must be field-locked
    - transitions must be explicit
    - operator patterns must be visible

cross_module_propagation:
  imports:
    - FFT operator families
    - FFT dimensional architecture
    - FFT coherence engines
    - SARG regime geometry
    - Mode substrate states
  exports:
    - example analyses
    - example signatures
```

---

## Purpose

This folder contains **worked examples** demonstrating how to use the FFT Analyzer suite across real frameworks, systems, and conceptual models. Each example applies the full diagnostic pipeline — operators, dimensions, regimes, drift, and coherence — to a declared framework, producing a complete analysis and a composite signature.

The Examples submodule serves three roles:

1. **Reference library** — catalogued end-to-end analyses that readers can study, replicate, or adapt
2. **Validation ground** — proof that the Analyzer submodules compose into a coherent diagnostic pipeline
3. **Onboarding ramp** — the fastest way for new users to see the Analyzer in action before building their own analyses

Each example includes:

- a declared framework with explicit assumptions
- operator pattern identification
- dimensional envelope mapping
- regime classification
- drift detection
- coherence assessment
- a composite signature summarizing the full analysis

---

## Directory Structure

```
Examples/
├── README.md
├── Example_Analyses.md
└── Example_Signatures.md
```

---

## Files

| File | Purpose |
|------|---------|
| **Example_Analyses.md** | End-to-end analysis walkthroughs spanning all Analyzer submodules — each example takes a declared framework through the full diagnostic pipeline |
| **Example_Signatures.md** | Composite signature profiles drawn from completed analyses — condensed reference cards capturing operator, dimensional, regime, drift, and coherence results |

---

## How the Two Files Relate

```
Example_Analyses.md          Example_Signatures.md
┌──────────────────┐         ┌──────────────────┐
│  Full walkthrough │         │ Composite summary │
│  per framework:   │  ───►   │ per framework:    │
│  operators        │         │  signature card   │
│  dimensions       │         │  with all layers  │
│  regime           │         │  in one profile   │
│  drift            │         │                   │
│  coherence        │         │                   │
└──────────────────┘         └──────────────────┘
      (process)                   (output)
```

**Example_Analyses.md** is the walkthrough — it shows the work.
**Example_Signatures.md** is the result — it captures the output.

---

## What an Example Analysis Covers

Each worked example follows the same diagnostic sequence:

**Step 1 — Declare the Framework**
Name the system, state its assumptions, and define its scope.

**Step 2 — Operator Analysis**
Identify active operators, family groupings, signatures, and regime coupling.

**Step 3 — Dimensional Analysis**
Map the dimensional envelope (D0–D7), test compatibility, and flag transition pathways.

**Step 4 — Regime Analysis**
Classify the regime level (R0–R3), test boundary integrity, and surface contradictions.

**Step 5 — Drift Analysis**
Detect drift presence, classify type, map vectors across layers, and check for paradox involvement.

**Step 6 — Coherence Analysis**
Assess coherence level (C0–C4), evaluate stability, and quantify paradox exposure.

**Step 7 — Generate Composite Signature**
Combine all layers into a single signature card for quick reference and cross-framework comparison.

---

## Example Signature Format

```yaml
Framework: [Name]
Composite Signature:
  operators:
    dominant: [operator family]
    secondary: [operator family]
    coupling: [regime coupling strength]
  dimensional:
    level: [D0–D7]
    envelope_stability: [low / moderate / high]
    transition_readiness: [target level if applicable]
  regime:
    level: [R0–R3]
    boundary_integrity: [low / moderate / high]
    contradictions: [none / detected]
  drift:
    detected: [true / false]
    type: [gradual / sudden / oscillating / paradox]
    velocity: [low / moderate / high]
  coherence:
    level: [C0–C4]
    stability: [low / moderate / high]
    paradox_exposure: [none / low / moderate / high]
```

---

## Navigation

- [Example Analyses](./Example_Analyses.md)
- [Example Signatures](./Example_Signatures.md)

---

## Cross-Module Integration

The Examples submodule draws from every other Analyzer submodule:

| Submodule | What it contributes to examples |
|-----------|------|
| **Operators** | Operator identification, family profiling, regime coupling |
| **Dimensional** | Envelope mapping, compatibility, transitions, collapse risk |
| **Regime** | R0–R3 classification, boundary testing, contradiction surfacing |
| **Drift** | Drift detection, classification, vector mapping, paradox drift |
| **Coherence** | C0–C4 assessment, stability evaluation, paradox exposure |

---

## Related Modules

- [FFT Analyzer](../README.md) — Parent Analyzer module
- [Drift](../Drift/README.md) — Drift detection across all layers
- [Regime](../Regime/README.md) — Regime classification and boundary diagnostics
- [Operators](../Operators/README.md) — Operator profiling and regime coupling
- [Dimensional](../Dimensional/README.md) — Dimensional structure and transitions
- [Coherence](../Coherence/README.md) — Coherence stability and paradox exposure

---

*Part of [TriadicFrameworks](../../../../README.md) · Framework Field Theory · Analyzer*
