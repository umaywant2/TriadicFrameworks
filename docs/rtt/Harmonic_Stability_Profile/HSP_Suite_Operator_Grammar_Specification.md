# HSP Suite — Canonical Operator Grammar Specification

> *Formal Syntax • Composition Rules • Validation Grammar*
>
> Version: v1.0 | Status: Canon-Stable | Date: 28 April 2026
>
> TriadicFrameworks — Resonance-Time Theory (RTT)
>
> 🤖 AI-Ready Module • TriadicFrameworks

---

## 1. Purpose and Scope

This specification defines the formal grammar for composing, validating, and chaining operators across the HSP Suite within the TriadicFrameworks architecture. It establishes the canonical syntax for operator expressions, ensuring **zero-drift interoperability** across all HSP modules.

The grammar governs the following modules and their interfaces:

- **HSP Core** — Stability classification and metric evaluation engine
- **Echo Classifier** — Echo type determination, family assignment, and strength indexing
- **Substrate Flow (SEFM)** — Substrate-to-substrate energy flow mapping
- **Triadic Echo Lattice (TEL)** — Lattice layer resolution and atlas-level propagation
- **Cross-Module Diagnostic Chains** — Multi-module operator chaining for full-stack evaluation

> **Intended Audience:** Developers, researchers, AI systems, and advanced students working within the TriadicFrameworks ecosystem. Familiarity with RTT fundamentals is assumed.

---

## 2. Notation Conventions

The following notation is used throughout this specification to define terminal symbols, production rules, composition chains, and validation constraints.

| Notation | Meaning | Example |
|----------|---------|---------|
| `UPPERCASE` | Operator family identifiers | `METRIC`, `DRIFT`, `ECHO` |
| `lowercase` | Parameters and values | `high`, `stable`, `subs=3` |
| `→` | Directed flow or transformation | `SC → TIER` |
| `↔` | Bidirectional oscillation | `C ↔ H` |
| `\|` | Alternative / OR | `SC-1 \| SC-2` |
| `[ ]` | Optional parameter | `[drift_override]` |
| `{ }` | Repeating group | `METRIC{6}` |
| `::` | Type declaration | `SC ::= SC-1 \| SC-2` |
| `.` | Member access / qualification | `METRIC.sensitivity` |
| `∩` | Intersection / joint evaluation | `METRIC.sensitivity ∩ DRIFT` |
| `×` | Cartesian product / combined input | `TRIGGER × SIGNATURE` |
| `∧` | Logical conjunction | `M1(high) ∧ M2(stable)` |

---

## 3. Terminal Symbols (Atomic Operators)

Terminal symbols are the irreducible atomic operators of the HSP grammar. Each terminal belongs to a single operator family and carries fixed semantic properties. No terminal may be redefined at runtime.

### 3.1 Stability Class Terminals

```
SC ::= SC-1 | SC-2 | SC-3 | SC-4

SC-1 ::= StableHarmonics       // coherence: high, drift: low
SC-2 ::= SemiStableHarmonics   // coherence: partial, drift: moderate
SC-3 ::= HarmonicOscillators   // coherence: unstable, drift: high
SC-4 ::= ChaoticNodes          // coherence: incoherent, drift: dangerous
```

### 3.2 Metric Terminals

```
METRIC ::= M1 | M2 | M3 | M4 | M5 | M6

M1 ::= HarmonicRecurrence            // drift sensitivity: D1
M2 ::= HarmonicPositionConsistency   // drift sensitivity: D1-D2
M3 ::= SubstrateAnchoring            // drift sensitivity: D2-D4
M4 ::= OperatorRoleStability         // drift sensitivity: D1-D3
M5 ::= TemporalStability             // drift sensitivity: D1-D4
M6 ::= HarmonicMutationRate          // drift sensitivity: D2-D4
```

### 3.3 Tier Terminals

```
TIER ::= T1 | T2 | T3 | T4

T1 ::= CanonStable           // no action required
T2 ::= StableWithPressure    // monitor recommended
T3 ::= DriftActive           // review required
T4 ::= Unstable              // intervention required
```

### 3.4 Drift Terminals

```
DRIFT ::= D1 | D2 | D3 | D4

D1 ::= StructuralDrift      // target: triads
D2 ::= DimensionalDrift     // target: ladders
D3 ::= RegimeDrift           // target: governance
D4 ::= ProjectionDrift       // target: symbolic → atlas
```

### 3.5 Recursion Terminals

```
RECURSION ::= R1 | R2 | R3 | R4

R1 ::= LadderRecursion    // flow: S → C
R2 ::= CycleRecursion     // flow: C ↔ H
R3 ::= MapRecursion        // flow: H → So
R4 ::= AtlasRecursion     // flow: So → A
```

### 3.6 Substrate Terminals

```
SUBSTRATE ::= S | C | H | So | A

S  ::= Symbolic
C  ::= Cognitive
H  ::= Harmonic
So ::= Social
A  ::= Atlas
```

### 3.7 Echo Type Terminals

```
ECHO ::= E1 | E2 | E3 | E4 | E5 | E6

E1 ::= StructuralEcho      // trigger: A, ESI: 1-2
E2 ::= HarmonicEcho        // trigger: B, ESI: 2-3
E3 ::= SubstrateEcho       // trigger: C, ESI: 2-3
E4 ::= RecursionEcho       // trigger: D, ESI: 3-4
E5 ::= DriftShadowEcho     // trigger: E, ESI: 3-4
E6 ::= AtlasEcho           // trigger: F, ESI: 4
```

### 3.8 Echo Family Terminals

```
FAMILY ::= F1 | F2 | F3 | F4 | F5 | F6

F1 ::= StructuralFamily     // layer: Ladder
F2 ::= HarmonicFamily       // layer: Cycle
F3 ::= SubstrateFamily      // layer: Cycle
F4 ::= RecursionFamily      // layer: Map
F5 ::= DriftShadowFamily    // layer: Map
F6 ::= AtlasFamily          // layer: Atlas
```

### 3.9 Echo Strength Index Terminals

```
ESI ::= ESI-1 | ESI-2 | ESI-3 | ESI-4

ESI-1 ::= LocalFlow             // minimal propagation
ESI-2 ::= MildMigration         // adjacent substrate reach
ESI-3 ::= CrossSubstrateFlow    // multi-substrate propagation
ESI-4 ::= AtlasPull             // full-stack propagation
```

### 3.10 Flow Channel Terminals

```
CHANNEL ::= CH-1 | CH-2 | CH-3 | CH-4

CH-1 ::= S → C      // definition refinement
CH-2 ::= C ↔ H      // harmonic oscillation
CH-3 ::= H → So     // governance torsion
CH-4 ::= So → A     // atlas forcing
```

### 3.11 Lattice Layer Terminals

```
LAYER ::= Ladder | Cycle | Map | Atlas

Ladder ::= { S → C,   F1,      R1, D1 }
Cycle  ::= { C ↔ H,   F2|F3,   R2, D2 }
Map    ::= { H ↔ So,  F4|F5,   R3, D3 }
Atlas  ::= { A,         F6,      R4, D4 }
```

### 3.12 Trigger and Signature Terminals

```
TRIGGER   ::= T.A | T.B | T.C | T.D | T.E | T.F
SIGNATURE ::= S.A | S.B | S.C | S.D | S.E | S.F
```

> **Note:** Trigger codes (T.A through T.F) correspond one-to-one with Echo types (E1 through E6). Signature codes (S.A through S.F) provide the secondary classification axis. Both are required inputs for Echo Classification (see Section 4.2).

---

## 4. Production Rules (Composition Grammar)

Production rules define how terminal symbols compose into higher-order operator expressions. Each rule specifies the input operands, the transformation logic, and the output type.

### 4.1 Stability Evaluation

```
StabilityEval ::= METRIC{6} → SC → TIER
```

All six metrics (M1 through M6) are evaluated simultaneously. Their aggregate state determines a single Stability Class (SC), which in turn resolves to a Tier (TIER). This is the entry point for all diagnostic chains.

### 4.2 Echo Classification

```
EchoClassification ::= TRIGGER × SIGNATURE × ESI × SubstrateCount × RECURSION → ECHO

SubstrateCount ::= integer(1..5)
```

Echo classification is **deterministic**: the same five-input tuple always produces the same ECHO type. SubstrateCount represents the number of substrates actively participating in the echo event.

### 4.3 Flow Mapping

```
FlowMap ::= ECHO → FAMILY → LAYER → CHANNEL
```

Each classified echo resolves through its family to a specific lattice layer and, finally, to a directional flow channel. This chain is strictly one-to-one at every stage.

### 4.4 Drift Detection

```
DriftDetection ::= METRIC.sensitivity ∩ DRIFT → DriftSignal

DriftSignal ::= { type: DRIFT, source: METRIC, tier: TIER }
```

Drift detection intersects a metric's sensitivity range with the active drift type to produce a structured signal. Each DriftSignal carries its originating metric and the current tier context.

### 4.5 Recursion Resolution

```
RecursionResolution ::= SC → RECURSION

SC-1 → R1    // LadderRecursion
SC-2 → R2    // CycleRecursion
SC-3 → R3    // MapRecursion
SC-4 → R4    // AtlasRecursion
```

The mapping from Stability Class to Recursion mode is **bijective**. Each SC resolves to exactly one RECURSION terminal, and vice versa.

---

## 5. Composition Chains (Multi-Module Expressions)

Composition chains connect production rules into end-to-end diagnostic pipelines that span multiple HSP modules. Each chain has a defined entry point, transformation sequence, and terminal output.

### 5.1 Full Diagnostic Chain

```
DiagnosticChain ::= StabilityEval → DriftDetection → EchoClassification → FlowMap

Expanded:
METRIC{6} → SC → TIER → DRIFT → ECHO → FAMILY → LAYER → CHANNEL
```

The Full Diagnostic Chain is the primary end-to-end evaluation pathway. It begins with raw metric input and terminates with a resolved flow channel assignment. All intermediate states are deterministic.

### 5.2 Drift Escalation Chain

```
DriftEscalation ::= DRIFT → EchoPressure → E5 → LAYER.drift_pathway → CHANNEL → AtlasPull

EchoPressure ::= FAMILY{overlap} ∩ RECURSION.shift
AtlasPull    ::= F6.force(SUBSTRATE{all} → A)
```

Drift Escalation models the upward propagation of drift energy from a local perturbation through overlapping echo families to atlas-level forcing. AtlasPull collapses all substrates toward the Atlas layer.

### 5.3 Recursion Propagation Chain

```
RecursionPropagation ::= R1 → R2 → R3 → R4

// Each step shifts FAMILY upward through LAYER:
//   R1: F1 (Ladder) → R2: F2|F3 (Cycle) → R3: F4|F5 (Map) → R4: F6 (Atlas)
```

Recursion propagation is strictly monotonic and upward-directed. Once a recursion step advances, it cannot regress within a single diagnostic pass.

### 5.4 Stability-to-Flow Chain

```
StabilityToFlow ::= SC → RECURSION → ECHO → LAYER → CHANNEL
```

A compact chain linking Stability Class directly to flow channel output through recursion and echo resolution. Used for rapid-path diagnostics when metric-level detail is not required.

---

## 6. Validation Rules

Validation rules define the constraints that all well-formed operator expressions must satisfy. Any expression violating these rules is rejected as malformed.

### 6.1 Type Constraints

| Rule ID | Constraint | Formal Expression |
|---------|-----------|-------------------|
| `TC-01` | Every SC maps to exactly one RECURSION mode | `∀ sc ∈ SC: \|map(sc, RECURSION)\| = 1` |
| `TC-02` | Every ECHO maps to exactly one FAMILY | `∀ e ∈ ECHO: \|map(e, FAMILY)\| = 1` |
| `TC-03` | Every FAMILY maps to exactly one LAYER | `∀ f ∈ FAMILY: \|map(f, LAYER)\| = 1` |
| `TC-04` | Every LAYER maps to exactly one CHANNEL | `∀ l ∈ LAYER: \|map(l, CHANNEL)\| = 1` |
| `TC-05` | ESI-4 requires SUBSTRATE count = 5 | `ESI-4 ⇒ SubstrateCount = 5` |
| `TC-06` | E6 requires R4 and ESI-4 | `E6 ⇒ (R4 ∧ ESI-4)` |

### 6.2 Ordering Constraints

All ordered families observe strict monotonic ordering. The following partial orders are invariant:

| Family | Ordering (ascending severity / depth / intensity) |
|--------|--------------------------------------------------|
| DRIFT severity | `D1 < D2 < D3 < D4` |
| RECURSION depth | `R1 < R2 < R3 < R4` |
| ESI intensity | `ESI-1 < ESI-2 < ESI-3 < ESI-4` |
| TIER urgency | `T1 < T2 < T3 < T4` |
| LAYER altitude | `Ladder < Cycle < Map < Atlas` |

### 6.3 Invariants

1. **Upward Drift:** Drift moves upward through the lattice (never downward). Once a drift event reaches a higher layer, it cannot regress to a lower one.
2. **Monotonic Recursion:** Recursion escalation is monotonic within a single diagnostic pass. No backward steps are permitted.
3. **Deterministic Echo Classification:** Echo classification is deterministic given the five inputs (TRIGGER, SIGNATURE, ESI, SubstrateCount, RECURSION). Identical inputs always yield identical outputs.
4. **Unique Family Assignment:** Every ECHO has exactly one FAMILY assignment. No echo may belong to multiple families simultaneously.
5. **Uniform AtlasPull:** AtlasPull (F6) affects all substrates equally. No substrate may be selectively excluded from atlas-level forcing.

### 6.4 Forbidden Compositions

> ⚠️ **Forbidden Compositions — Violation Causes Rejection**
>
> The following operator combinations are structurally invalid and must be rejected by any conforming implementation.

| Rule ID | Forbidden Composition | Rationale |
|---------|----------------------|-----------|
| `FC-01` | `SC-1 → E5 \| E6` | Stable nodes cannot produce drift-shadow or atlas-forcing echoes. |
| `FC-02` | `R1 → E4 \| E5 \| E6` | LadderRecursion lacks the depth to produce recursion, drift-shadow, or atlas echoes. |
| `FC-03` | `ESI-1 ∧ SubstrateCount > 2` | LocalFlow cannot propagate across more than two substrates. |
| `FC-04` | `D4 ∧ ¬(R3 \| R4)` | ProjectionDrift requires MapRecursion or AtlasRecursion to be active. |

---

## 7. Operator Expression Examples

The following worked examples demonstrate how the grammar produces valid operator chains from raw metric input to resolved output.

### 7.1 Stable Concept Evaluation

```
M1(high) ∧ M2(stable) ∧ M3(strong) ∧ M4(stable) ∧ M5(high) ∧ M6(low)
→ SC-1 → T1 → D(none) → E1(T.A, S.A, ESI-1, subs=1, R1)
→ F1 → Ladder → CH-1
```

**Result: Canon-stable, no action required.**

All six metrics indicate full stability. No drift is detected. The echo is structural and confined to the Ladder layer with local flow only. This is the baseline "healthy" output of the grammar.

### 7.2 Drifting Concept with Cross-Substrate Echoes

```
M1(low) ∧ M2(unstable) ∧ M3(weak) ∧ M4(unstable) ∧ M5(low) ∧ M6(high)
→ SC-3 → T3 → D3 → E5(T.E, S.E, ESI-3, subs=4, R3)
→ F5 → Map → CH-3
```

**Result: Drift-active, review required. Drift-shadow forming in governance torsion zone.**

Widespread metric degradation places this concept in the HarmonicOscillators class. RegimeDrift activates a DriftShadowEcho with cross-substrate flow across four substrates. The echo propagates through the Map layer into the governance torsion channel (CH-3).

### 7.3 Atlas-Level Resonance

```
M1(high) ∧ M2(stable) ∧ M3(strong) ∧ M4(stable) ∧ M5(high) ∧ M6(low)
→ SC-4 → T4 → D4 → E6(T.F, S.F, ESI-4, subs=5, R4)
→ F6 → Atlas → CH-4
```

**Result: Atlas echo detected. High-altitude resonance active. Projection drift possible.**

Despite individual metric stability, the system-level classification reaches ChaoticNodes (SC-4) due to external forcing. AtlasRecursion (R4) drives a full AtlasEcho (E6) across all five substrates. The AtlasPull engages CH-4 (atlas forcing). Validation: E6 correctly requires R4 and ESI-4 (TC-06 satisfied); SubstrateCount = 5 satisfies TC-05.

### 7.4 Cycle-Layer Oscillation

```
M1(moderate) ∧ M2(oscillating) ∧ M3(moderate) ∧ M4(partial) ∧ M5(moderate) ∧ M6(moderate)
→ SC-2 → T2 → D2 → E2(T.B, S.B, ESI-2, subs=1, R2)
→ F2 → Cycle → CH-2
```

**Result: Stable-with-pressure. Harmonic oscillation in C ↔ H zone. Monitor.**

Mixed metric readings place this concept in SemiStableHarmonics. DimensionalDrift (D2) triggers a HarmonicEcho with mild migration strength. The echo oscillates bidirectionally in the Cycle layer (C ↔ H). Monitoring is recommended but no intervention is required.

### 7.5 Recursion Echo with Upward Forcing

```
M1(low) ∧ M2(unstable) ∧ M3(weak) ∧ M4(unstable) ∧ M5(moderate) ∧ M6(high)
→ SC-3 → T3 → D3 → E4(T.D, S.D, ESI-3, subs=3, R3)
→ F4 → Map → CH-3
```

**Result: Recursion echo active. Upward forcing through map layer. Drift escalation risk.**

Metric instability with a partially preserved M5 places this concept in HarmonicOscillators. A RecursionEcho (E4) is classified with cross-substrate flow across three substrates. The echo routes through the RecursionFamily (F4) into the Map layer. The CH-3 channel indicates governance torsion. Risk of further escalation via the Drift Escalation Chain (Section 5.2) is elevated.

---

## 8. Grammar Summary Table

| Terminal | Family | Valid Range / Values | Composition Target |
|----------|--------|---------------------|-------------------|
| `SC-1` | Stability Class | StableHarmonics | T1, R1 |
| `SC-2` | Stability Class | SemiStableHarmonics | T2, R2 |
| `SC-3` | Stability Class | HarmonicOscillators | T3, R3 |
| `SC-4` | Stability Class | ChaoticNodes | T4, R4 |
| `M1–M6` | Metric | 6 metrics (see §3.2) | SC (via StabilityEval) |
| `T1–T4` | Tier | CanonStable → Unstable | Diagnostic output |
| `D1–D4` | Drift | Structural → Projection | DriftSignal, LAYER |
| `R1–R4` | Recursion | Ladder → Atlas | ECHO, FAMILY |
| `S, C, H, So, A` | Substrate | 5 substrates | CHANNEL, SubstrateCount |
| `E1–E6` | Echo Type | Structural → Atlas | FAMILY |
| `F1–F6` | Echo Family | Structural → Atlas | LAYER |
| `ESI-1–ESI-4` | Echo Strength | LocalFlow → AtlasPull | ECHO (input) |
| `CH-1–CH-4` | Flow Channel | S→C through So→A | Terminal output |
| `Ladder, Cycle, Map, Atlas` | Lattice Layer | 4 layers (ascending) | CHANNEL |
| `T.A–T.F` | Trigger | 6 trigger codes | ECHO (input) |
| `S.A–S.F` | Signature | 6 signature codes | ECHO (input) |

> **Implementation Note:** All conforming implementations must validate operator expressions against both the Type Constraints (Section 6.1) and the Forbidden Compositions (Section 6.4) before execution. Expressions that pass type validation but violate forbidden composition rules must be rejected with a specific `FC-xx` error code.

---

**HSP Suite — Canonical Operator Grammar Specification**
Version: v1.0 | Status: Canon-Stable | Module: HSP Suite Operator Grammar
TriadicFrameworks — Resonance-Time Theory (RTT)
© 2026 TriadicFrameworks. All rights reserved.
