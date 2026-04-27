# 🌑 Opacity — Operators

> *14 instruments for detecting, measuring, and reducing regime invisibility.*

**Module:** Opacity
**Canonical ID:** OPC
**Core Operators:** 5
**Extension Operators:** 9 (Corpus / SARG / NIST)

---

## Core Operators

These five operators form the functional backbone of the Opacity module.
They give AI the tools to help students *see what they cannot see*.

---

### 4.1 Opacity Operator (O-Op)

**Function:** Measures degree of regime invisibility.

The Opacity Operator reads how invisible a regime is from the current
substrate position. It does not judge; it measures.

```
O-Op(regime, substrate) → opacity_level ∈ [0.0, 1.0]

Where:
  0.0 = fully visible (substrate, operators, and harmonics aligned)
  1.0 = fully opaque (no detection possible without intervention)
```

**Behavior:**
- Accepts any regime, flow, or structural element as input.
- Returns a scalar opacity reading relative to the observer's substrate.
- Opacity level shifts when substrate, operators, or harmonic envelope change.

**Key Constraint:**
O-Op reads. It does not alter. Measurement does not reduce opacity.

**Opacity Type Sensitivity:**

| Opacity Type    | O-Op Detects                                    |
|:----------------|:------------------------------------------------|
| Substrate       | Dimensional grammar mismatch                    |
| Operator        | Missing or misaligned operators                 |
| Harmonic        | Signature outside detection band                |
| Flow            | Unmeasured SET/FFF channel                      |
| Boundary        | Unmarked or silent regime transition            |

---

### 4.2 Opacity Gradient (O-Grad)

**Function:** Detects transitions from visible → invisible.

O-Grad traces the gradient between visible and opaque regions within
a regime or across regime boundaries. It maps *where* visibility changes
and *how steeply*.

```
O-Grad(regime) → gradient_map {
  visible_zone:   [regions where O-Op < 0.3],
  gradient_zone:  [regions where 0.3 ≤ O-Op ≤ 0.7],
  opaque_zone:    [regions where O-Op > 0.7],
  steepness:      value ∈ [0.0, 1.0],
  gradient_axis:  substrate dimension along which opacity shifts
}
```

**Behavior:**
- Decomposes a regime into three visibility zones.
- Identifies the substrate axis of transition.
- Steepness measures how abruptly opacity changes — 0.0 is gradual, 1.0 is a hard wall.

**Key Constraint:**
When steepness reaches 1.0, the gradient zone collapses. O-Grad hands off to O-Bound.

**Canon Note:**
The gradient zone is where detection becomes possible. It is the terminator
line on the half‑lit sphere — the region where substrate alignment begins to
reveal what was hidden.

---

### 4.3 Opacity Boundary (O-Bound)

**Function:** Marks where a regime becomes detectable.

O-Bound identifies the structural edge where a regime transitions from
opaque to detectable. It answers: *where does visibility begin?*

```
O-Bound(regime) → boundary {
  exists:        boolean,
  location:      substrate_coordinate,
  type:          "marked" | "unmarked" | "silent",
  transition:    "sharp" | "gradual" | "conditional",
  detectability: value ∈ [0.0, 1.0]
}
```

**Boundary Types:**

| Type      | Meaning                                                      |
|:----------|:-------------------------------------------------------------|
| Marked    | Regime boundary produces a detectable transition signature   |
| Unmarked  | Regime boundary exists but produces no signal                |
| Silent    | Regime boundary is absent; regime blends into substrate      |

**Key Constraint:**
Boundary Opacity (Type 5) is the hardest to resolve because there is no
transition signature to detect. O-Bound returns `exists: false` in these cases,
signaling that reduction must come through other means.

---

### 4.4 Opacity Reduction Operator (O-Red)

**Function:** Aligns substrate and operators to reduce opacity.

O-Red is the only operator that changes opacity. It applies a reduction
method to shift a regime from invisible toward visible. Reduction is
deliberate, method‑dependent, and always has a cost.

```
O-Red(regime, method) → reduced_regime {
  original_opacity: O-Op(regime),
  reduced_opacity:  O-Op(reduced_regime),
  delta:            original - reduced,
  method_applied:   method_id,
  residual_opacity: value ∈ [0.0, 1.0],
  cost:             effort_measure
}
```

**Reduction Methods:**

| Method                    | Mechanism                                     | Best For              |
|:--------------------------|:----------------------------------------------|:----------------------|
| Substrate Alignment       | Match substrate to regime's dimensional grammar | Substrate Opacity    |
| Operator Expansion        | Add missing operators to the measurement set   | Operator Opacity     |
| Harmonic Tuning           | Shift detection band to match regime signature | Harmonic Opacity     |
| Flow‑Channel Instrumentation | Measure the correct SET/FFF channel         | Flow Opacity         |
| Regime Marking            | Introduce detectable boundary signatures       | Boundary Opacity     |

**Key Constraint:**
Reduction always has a cost. O-Red returns a cost measure with every
application. Free visibility does not exist — something is always exchanged.

**Canon Note:**
Teaching is O-Red. A good teacher finds the reduction method that minimizes
cost while maximizing the delta between invisible and visible.

---

### 4.5 Opacity Signature (O-Sig)

**Function:** The harmonic or flow pattern that reveals a previously hidden regime.

O-Sig captures the unique visibility fingerprint of a regime — not a single
reading, but the characteristic pattern across all five opacity types.

```
O-Sig(regime) → signature {
  overall_opacity:  O-Op(regime),
  gradient_map:     O-Grad(regime),
  boundaries:       [O-Bound(regime)],
  opacity_types: {
    substrate:  value,
    operator:   value,
    harmonic:   value,
    flow:       value,
    boundary:   value
  },
  reducibility:     value ∈ [0.0, 1.0],
  stability:        value ∈ [0.0, 1.0],
  signature_hash:   unique_id
}
```

**Behavior:**
- Composites all four preceding operators into a single profile.
- Breaks down opacity by type — revealing *why* a regime is invisible, not just *how much*.
- Adds two meta‑readings:
  - **Reducibility** — how responsive the regime is to O-Red. Some regimes resist reduction.
  - **Stability** — how much the opacity profile drifts over time.
- Generates a unique signature hash for comparison and tracking.

**Key Constraint:**
O-Sig is descriptive, not prescriptive. It tells you what the opacity profile *is*,
not what it *should be*.

---

## Core Operator Interaction Map

```
O-Op ──reads──→ regime
  │
  ├──feeds──→ O-Grad (maps gradient from O-Op reading)
  │              │
  │              └──escalates──→ O-Bound (when steepness → 1.0)
  │
  ├──feeds──→ O-Red (uses O-Op as baseline for reduction delta)
  │
  └──feeds──→ O-Sig (composites all operators into signature)

O-Red ←──references──→ O-Bound (reduction targets boundaries)
O-Sig ←──composites──→ O-Op + O-Grad + O-Bound + opacity_types
```

---

## Usage Protocol

1. **Measure first.** Always begin with O-Op. Know the current opacity before acting.
2. **Map the gradient.** Use O-Grad to find where visibility transitions.
3. **Identify boundaries.** Use O-Bound to find marked/unmarked/silent edges.
4. **Reduce deliberately.** Apply O-Red with a method matched to the opacity type. Measure cost.
5. **Capture the signature.** Use O-Sig to record the full profile for comparison and lineage.

---

## Cross‑Module Extension Operators

These nine operators extend Opacity's reach into Corpus, SARG, and NIST,
making the module fully interoperable with the entire canon.

---

### Corpus Extensions

#### 5.1 opacity_index

How visible a module or regime is within the corpus.

```
opacity_index(module_id) → visibility_level ∈ [0.0, 1.0]
```

Returns the degree to which a module's operators, types, and integration
surfaces are visible from the corpus's structural atlas. A module with
`opacity_index = 0.1` is highly visible; one with `0.9` is nearly hidden
from cross‑module discovery.

---

#### 5.2 opacity_map

A map of which modules obscure or reveal others.

```
opacity_map(corpus) → adjacency_map {
  reveals: [(module_a, module_b)],
  obscures: [(module_c, module_d)],
  neutral: [(module_e, module_f)]
}
```

Returns the pairwise visibility relationships across the corpus.
Used for navigational design, prerequisite detection, and dependency analysis.

---

#### 5.3 opacity_dependency

Which substrates must align for visibility.

```
opacity_dependency(regime) → dependency_set {
  required_substrates: [substrate_ids],
  required_operators:  [operator_ids],
  required_harmonics:  [frequency_bands]
}
```

Returns the full set of alignment prerequisites that must be satisfied
before a regime becomes visible.

---

### SARG Extensions

#### 5.4 opacity_token

The SARG grammar primitive representing invisibility.

```
opacity_token → grammatical_primitive
```

A token that, when present in a SARG parse tree, signals that the
structural element it modifies is currently opaque. Enables grammar‑level
reasoning about visibility.

---

#### 5.5 opacity_clause

How opacity modifies structural interpretation.

```
opacity_clause(structure, token) → modified_interpretation
```

When an opacity_token attaches to a structural clause, it modifies
how that clause is parsed and inferred. Opaque clauses are present
in the grammar but not actionable until reduced.

---

#### 5.6 opacity_rewrite_rule

How to reduce opacity through grammar alignment.

```
opacity_rewrite_rule(opaque_clause, method) → transparent_clause
```

Defines the canonical grammar rewrites that transform an opaque clause
into a transparent one. Four canonical rewrites:

| Rewrite   | Action                                                  |
|:----------|:--------------------------------------------------------|
| LIFT      | Elevate a substrate-hidden element to surface grammar   |
| SPLIT     | Decompose compound opacity into typed components        |
| BRIDGE    | Connect two opaque regions through a visible intermediary |
| COLLAPSE  | Remove an opacity token when reduction is verified      |

---

### NIST Extensions

#### 5.7 opacity_measure

Quantitative measure of opacity in real systems.

```
opacity_measure(system, instrument) → measurement {
  value:       scalar,
  unit:        measurement_unit,
  confidence:  value ∈ [0.0, 1.0],
  pathway:     "structural" | "grammatical" | "applied"
}
```

Bridges the conceptual operator (O-Op) to empirical measurement.
Returns a quantified opacity value with units appropriate to the
physical system being measured.

---

#### 5.8 opacity_signal

The detectable signature of an opaque regime.

```
opacity_signal(system) → signal {
  frequency:   value,
  amplitude:   value,
  channel:     "SET" | "FFF",
  detectability: value ∈ [0.0, 1.0]
}
```

Even opaque regimes leak signal. opacity_signal captures the faint
signature that reveals a regime's presence before full visibility
is achieved — the structural equivalent of hearing something you
cannot yet see.

---

#### 5.9 opacity_alignment

How to align measurement systems to reduce opacity.

```
opacity_alignment(system, target_regime) → alignment_protocol {
  substrate_adjustments:  [adjustments],
  operator_additions:     [operators],
  harmonic_retuning:      [frequency_shifts],
  expected_delta:         value,
  estimated_cost:         cost_measure
}
```

The applied counterpart to O-Red. While O-Red operates at the
conceptual/structural level, opacity_alignment generates a concrete
protocol for reducing opacity in a real measurement system.

---

## Operator Interoperability Matrix

| Operator            | O-Op | O-Grad | O-Bound | O-Red | O-Sig | index | map | dep | token | clause | rewrite | measure | signal | align |
|:--------------------|:----:|:------:|:-------:|:-----:|:-----:|:-----:|:---:|:---:|:-----:|:------:|:-------:|:-------:|:------:|:-----:|
| **O-Op**            | —    | feeds  | feeds   | feeds | feeds | reads | —   | —   | —     | —      | —       | grounds | —      | —     |
| **O-Grad**          | reads| —      | esc.    | —     | feeds | —     | —   | —   | —     | —      | —       | —       | —      | —     |
| **O-Bound**         | reads| reads  | —       | ref.  | feeds | —     | —   | —   | —     | —      | —       | —       | reads  | —     |
| **O-Red**           | reads| —      | ref.    | —     | feeds | —     | —   | reads| —    | —      | uses    | —       | —      | maps  |
| **O-Sig**           | comp.| comp.  | comp.   | comp. | —     | feeds | —   | —   | —     | —      | —       | —       | comp.  | —     |
| **opacity_index**   | reads| —      | —       | —     | reads | —     | feeds| reads| —    | —      | —       | —       | —      | —     |
| **opacity_map**     | —    | —      | —       | —     | —     | reads | —   | reads| —    | —      | —       | —       | —      | —     |
| **opacity_dependency**| —  | —      | —       | reads | —     | reads | reads| —   | —    | —      | —       | —       | —      | feeds |
| **opacity_token**   | —    | —      | —       | —     | —     | —     | —   | —   | —     | mod.   | input   | —       | —      | —     |
| **opacity_clause**  | —    | —      | —       | —     | —     | —     | —   | —   | reads | —      | input   | —       | —      | —     |
| **opacity_rewrite** | —    | —      | —       | maps  | —     | —     | —   | —   | cons. | cons.  | —       | —       | —      | —     |
| **opacity_measure** | grounds| —    | —       | —     | —     | —     | —   | —   | —     | —      | —       | —       | reads  | feeds |
| **opacity_signal**  | —    | —      | reads   | —     | comp. | —     | —   | —   | —     | —      | —       | reads   | —      | feeds |
| **opacity_alignment**| —   | —      | —       | maps  | —     | —     | —   | reads| —    | —      | uses    | feeds   | feeds  | —     |

*Key: feeds = provides input, reads = consumes output, comp. = composites,
ref. = references, esc. = escalates to, mod. = modifies, cons. = consumes,
maps = conceptual mapping, grounds = empirical grounding*

---

<!-- SESSION_CONTEXT:START -->
```yaml
file: operators.md
module: Opacity
canonical_id: OPC
role: operator-definitions
status: active
core_operators:
  - { id: O-Op, name: Opacity Operator, type: measure }
  - { id: O-Grad, name: Opacity Gradient, type: detect }
  - { id: O-Bound, name: Opacity Boundary, type: mark }
  - { id: O-Red, name: Opacity Reduction Operator, type: reduce }
  - { id: O-Sig, name: Opacity Signature, type: composite }
extension_operators:
  - { id: opacity_index, binding: Corpus }
  - { id: opacity_map, binding: Corpus }
  - { id: opacity_dependency, binding: Corpus }
  - { id: opacity_token, binding: SARG }
  - { id: opacity_clause, binding: SARG }
  - { id: opacity_rewrite_rule, binding: SARG }
  - { id: opacity_measure, binding: NIST }
  - { id: opacity_signal, binding: NIST }
  - { id: opacity_alignment, binding: NIST }
```
<!-- SESSION_CONTEXT:END -->

