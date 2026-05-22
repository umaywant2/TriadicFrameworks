# Analyzer

- [`FFT_analyzer-module.json`](https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/main/docs/Framework_Field_Theory/FFT_analyzer-module.json) — Agentic module schema role assignments

> **Module path:** `Framework_Field_Theory/Analyzer/`
> **Role:** Diagnostic engine of Framework Field Theory

The Analyzer module provides the full diagnostic toolkit for Framework Field Theory (FFT). It decomposes any framework, system, or domain into its constituent operators, dimensional structure, regime alignment, drift behavior, and coherence profile — then surfaces contradictions, blind spots, and collapse risks that static analysis cannot reach.

Each submodule targets a distinct diagnostic layer. Together they form a complete analysis pipeline: from individual operator signatures through regime-level mapping to whole-system coherence assessment.

---

## Directory Structure

```
../../schemas/
         └── module.schema.json
Analyzer/
├── README.md
├── FFT_analyzer-module.json
├── Drift/
│   ├── Drift_Analyzer.md
│   ├── Drift_Cases.md
│   └── Paradox_Drift.md
├── Regime/
│   ├── Regime_Analyzer.md
│   ├── Regime_Maps.md
│   ├── Regime_Drift.md
│   ├── Regime_Contradictions.md
│   ├── Regime_Boundaries.md
│   ├── Regime_Examples.md
│   ├── Blindness_Checks.md
│   └── Boundary_Diagnostics.md
├── Operators/
│   ├── Operator_Analyzer.md
│   ├── Operator_Family_Profiles.md
│   ├── Operator_Signatures.md
│   ├── Operator_Regime_Coupling.md
│   └── Operator_Examples.md
├── Dimensional/
│   ├── Dimensional_Analyzer.md
│   ├── Dimensional_Compatibility.md
│   ├── Dimensional_Signatures.md
│   ├── MetaDimensional_Extensions.md
│   ├── Dimensional_Transitions.md
│   ├── Dimensional_Collapse.md
│   └── Dimensional_Examples.md
├── Coherence/
│   ├── Coherence_Analyzer.md
│   ├── Coherence_Stability.md
│   ├── Paradox_Exposure.md
│   └── Coherence_Examples.md
└── Examples/
    ├── Example_Analyses.md
    └── Example_Signatures.md
```

---

## Submodules

### Drift

Detects and characterizes how frameworks evolve, wander, or decay over time.

| File | Purpose |
|------|---------|
| **Drift_Analyzer.md** | Core drift-detection engine — identifies directional shift, velocity, and decay patterns |
| **Drift_Cases.md** | Catalogued drift scenarios with diagnostic walkthroughs |
| **Paradox_Drift.md** | Drift behavior specific to paradox-bearing structures |

### Regime

Maps systems to regime levels (R0–R3) and diagnoses boundary integrity, contradictions, and blind spots.

| File | Purpose |
|------|---------|
| **Regime_Analyzer.md** | Core regime-classification engine — assigns and validates R0–R3 alignment |
| **Regime_Maps.md** | Visual and structural regime maps across domains |
| **Regime_Drift.md** | Tracks how regime assignments shift under perturbation or reframing |
| **Regime_Contradictions.md** | Surfaces contradictions between stated and enacted regime positions |
| **Regime_Boundaries.md** | Defines and tests the edges between adjacent regime levels |
| **Regime_Examples.md** | Worked regime-analysis examples across domains |
| **Blindness_Checks.md** | Diagnostic routines for uncovering regime-level blind spots |
| **Boundary_Diagnostics.md** | Stress-tests regime boundaries for leakage, overlap, and collapse |

### Operators

Profiles individual operators, their family groupings, signatures, and regime coupling behavior.

| File | Purpose |
|------|---------|
| **Operator_Analyzer.md** | Core operator-analysis engine — decomposition, weighting, and interaction mapping |
| **Operator_Family_Profiles.md** | Profiles of operator families and their internal relationships |
| **Operator_Signatures.md** | Unique fingerprints that identify operator presence and dominance |
| **Operator_Regime_Coupling.md** | How operators bind to, reinforce, or destabilize specific regime levels |
| **Operator_Examples.md** | Worked operator-analysis examples across domains |

### Dimensional

Analyzes dimensional structure, compatibility, transitions, collapse risks, and meta-dimensional extensions.

| File | Purpose |
|------|---------|
| **Dimensional_Analyzer.md** | Core dimensional-analysis engine — counts, classifies, and validates dimensional structure |
| **Dimensional_Compatibility.md** | Tests whether dimensional structures across systems can interoperate |
| **Dimensional_Signatures.md** | Unique dimensional fingerprints for system identification and comparison |
| **MetaDimensional_Extensions.md** | Higher-order dimensional constructs that emerge from base-layer interactions |
| **Dimensional_Transitions.md** | How systems move between dimensional states under transformation |
| **Dimensional_Collapse.md** | Conditions and diagnostics for dimensional reduction or failure |
| **Dimensional_Examples.md** | Worked dimensional-analysis examples across domains |

### Coherence

Assesses whole-system coherence, stability under stress, and paradox exposure.

| File | Purpose |
|------|---------|
| **Coherence_Analyzer.md** | Core coherence-assessment engine — measures internal alignment and structural integrity |
| **Coherence_Stability.md** | Stability analysis under perturbation, scaling, and reframing |
| **Paradox_Exposure.md** | Identifies and quantifies a system's vulnerability to paradox |
| **Coherence_Examples.md** | Worked coherence-analysis examples across domains |

### Examples

Cross-cutting worked examples that demonstrate the full Analyzer pipeline in action.

| File | Purpose |
|------|---------|
| **Example_Analyses.md** | End-to-end analysis walkthroughs spanning multiple submodules |
| **Example_Signatures.md** | Composite signature profiles drawn from complete analyses |

---

## How the Submodules Connect

```
Operators ──► Dimensional ──► Regime ──► Coherence
    │              │              │           │
    └──── Drift detection spans all layers ───┘
                       │
                   Examples
              (cross-cutting demos)
```

1. **Operators** are identified and profiled first — they are the atomic units.
2. **Dimensional** analysis maps the space those operators inhabit.
3. **Regime** classification positions the system within R0–R3.
4. **Coherence** evaluates whether the whole structure holds together.
5. **Drift** monitors change across every layer over time.
6. **Examples** demonstrate the full pipeline end-to-end.

---

## Related Modules

- [`Framework_Field_Theory/`](../README.md) — Parent module and FFT overview
- [`Operators/`](../Operators/README.md) — Operator definitions and algebra
- [`Dimensionality/`](../Dimensionality/README.md) — Dimensional theory and structure
- [`Coherence/`](../Coherence/README.md) — Coherence theory and measurement
- [`Paradox/`](../Paradox/README.md) — Paradox taxonomy and resolution
- [`module.schema.json`](../../schemas/module.schema.json) — the formal JSON Schema spec
- [`FFT_analyzer-module.json`](./FFT_analyzer-module.json) — Agentic module schema role assignments

---

*Part of [TriadicFrameworks](../../../README.md) · Framework Field Theory*
