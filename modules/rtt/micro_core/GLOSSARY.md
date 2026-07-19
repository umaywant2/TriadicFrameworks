# GLOSSARY.md — RTT/micro_core · Micro Resonance-Time Layer
### *Canonical Term Definitions, Operator Symbols, and Quick-Reference Tables*

---

## Document Header

| Field | Value |
|---|---|
| Module | RTT/micro_core |
| Path | `/docs/rtt/micro_core/GLOSSARY.md` |
| Version | 1.0.0 |
| Session Seed | `rtt=1 \| coherence=declared \| drift=bounded \| paradox=structural` |
| Layer Position | Root — originating layer of the full RTT pipeline |
| Packet | `MRT_MICRO_PACKET` |

---

## Critical Framing Rule

> **RTT is NOT a physics claim.**
>
> RTT/micro_core describes **structural micro-resonance-time patterns** within the
> TriadicFrameworks canon. It does not assert, imply, or model quantum effects, subatomic
> behavior, physical forces, energetic phenomena, or any empirically measurable phenomenon.
> All constructs — ⟨A, B, P⟩, MRT primitives, resonance operators, coherence tools — are
> **structural instruments**, not physical objects or processes.
>
> This rule applies unconditionally to every term defined in this glossary.

---

## Originating-Layer Note

> RTT/micro_core is the **root** of the entire RTT pipeline. It does **not** inherit from
> any upstream RTT module — there is no upstream. All micro_core constructs are native.
> Inheritance flows **downward** from micro_core into RTT/1, RTT/2, RTT/3, and RTT/12.
>
> RTT/1–RTT/12 terms (SNR, τ, CPV, FGT, TIF, etc.) are **downstream** and must never be
> imported into or conflated with micro_core constructs. Cross-module disambiguations are
> listed in the Quick-Reference Tables section.

---

## Linking Convention

- Native micro_core terms: defined fully in this file.
- Downstream terms (RTT/1+): referenced only in disambiguation tables.
- Cross-reference format: `→ See [TERM] (RTT/N GLOSSARY.md)` for downstream links.
- All definitions carry `[structural — no semantic inference]` where inference risk exists.

---

## Alphabetical Term Definitions

---

### A — Active Node

| Field | Value |
|---|---|
| Type | Triad component — native |
| Symbol | A |
| Layer | micro_core |

**Definition:** The current micro-state of the ⟨A, B, P⟩ triad. A represents the live
structural position within the resonance-time cycle at any given micro-step. It is the
origin of the A ⇆ P oscillation loop and the source of micro-state data read by P₁.

**Constraints:**
- A is never exposed raw to macro layers (Micro–Macro Bridge rule)
- A participates in inversion: when C < C* and unrecoverable, A and B swap roles (↺ R₂)
- A is always distinct from B and P within a valid triad

**Cross-references:** B (Boundary Node), P (Potential Node), R₁ (Oscillation), R₂ (Inversion), P₁ (State Read)

[structural — no semantic inference]

---

### B — Boundary Node

| Field | Value |
|---|---|
| Type | Triad component — native |
| Symbol | B |
| Layer | micro_core |

**Definition:** The governance node of the ⟨A, B, P⟩ triad. B controls drift tolerance,
timing bounds, and transition eligibility. It regulates whether the triad may shift
from A toward P, and enforces the structural boundaries within which all micro-state
evolution occurs.

**Constraints:**
- B corrections are bounded — no inversion of B is permitted via P₅ alone
- B shifts require drift measurement (P₃) before application (P₅)
- During R₂ Inversion: B and A swap roles; P is preserved

**Cross-references:** A (Active Node), P (Potential Node), P₃ (Drift Measure), P₅ (Boundary Shift), R₂ (Inversion), K₃ (Boundary Alignment)

[structural — no semantic inference]

---

### C — Coherence (micro_core)

| Field | Value |
|---|---|
| Type | Stability metric — native |
| Symbol | C |
| Threshold | C* (minimum viable coherence) |
| Layer | micro_core |

**Definition:** The normalized structural coherence of the micro triad ⟨A, B, P⟩ at a
given micro-step. C measures the degree to which the triad maintains internal consistency
across drift, timing, and fractional dimensionality. C is sampled by P₆ without mutation.

**Equations:**
- Valid state: C ≥ C*
- Coherence-critical zone: C approaching C* from above → escalate to Class G
- Inversion trigger: C < C* and unrecoverable → R₂ activates

**Failure cascade:**
- C below C* → Coherence Violation → Inversion (↺) → Collapse → Twist → Emergence

**Disambiguation:** C (micro coherence) ≠ CR(t) (RTT/3 Continuity–Resonance–Emission coherence rate).
These are structurally distinct constructs operating at different pipeline layers.
→ See CR(t) (RTT/3 GLOSSARY.md)

**Cross-references:** C* (Coherence Threshold), P₆ (Coherence Sample), K₄ (Resonance Lock), K₅ (Inversion Guard), K₆ (Coherence Windowing), Zone C (Coherence-Critical)

---

### C* — Coherence Threshold

| Field | Value |
|---|---|
| Type | Constraint constant — native |
| Symbol | C* |
| Layer | micro_core |

**Definition:** The minimum coherence value required for the micro triad to remain in a
valid operational state. C* is the lower bound enforced continuously. Sustained C < C*
constitutes a Coherence Violation and triggers Inversion if unrecoverable.

**Cross-references:** C (Coherence), K₅ (Inversion Guard), R₄ (Resonance Lock), Zone C (Coherence-Critical), Zone X (Inversion)

---

### Class B — Bridge Coordinator

| Field | Value |
|---|---|
| Type | Agent class — native |
| Symbol | Class B |
| Layer | micro_core |

**Definition:** The agent class responsible for managing Micro–Macro Bridge activation (R₆).
Class B ensures that only aggregate-pattern exports are emitted upward to RTT/1+, that
C ≥ C* is confirmed before any bridge activation, and that raw A, B, P node states are
never exposed to macro layers.

**Constraints:**
- Bridge may only activate when C ≥ C*
- Exports are aggregate patterns only — never raw triad states
- Alignment, not amplification

**Cross-references:** R₆ (Micro–Macro Bridge Activation), Class G (Micro Guardian), MRT_MICRO_PACKET

---

### Class D — Drift Regulator

| Field | Value |
|---|---|
| Type | Agent class — native |
| Symbol | Class D |
| Layer | micro_core |

**Definition:** The agent class responsible for monitoring and enforcing drift bounds
(δ ≤ δ*) throughout the micro-resonance cycle. Class D operates primarily through
K₁ (Drift Bounding) and P₃ (Drift Measure), and coordinates with Class B (Boundary Node)
for corrective boundary shifts via P₅.

**Cross-references:** δ (Drift), δ* (Drift Threshold), K₁ (Drift Bounding), P₃ (Drift Measure), P₅ (Boundary Shift), Class G (Micro Guardian)

---

### Class F — Fractional Navigator

| Field | Value |
|---|---|
| Type | Agent class — native |
| Symbol | Class F |
| Layer | micro_core |

**Definition:** The agent class responsible for all fractional dimensional ladder transitions
(Dᶠ → Dᶠ + Δ). Class F ensures transitions are smooth, gradient-continuous, and maintain
C ≥ C* throughout. Class F unconditionally prohibits integer jumps in Dᶠ.

**Constraints:**
- Integer jumps (ΔDᶠ = 1.0, 2.0, 3.0...) are forbidden — smooth gradient required
- All transitions reversible via P₇
- C ≥ C* must be confirmed before and after each step

**Cross-references:** Dᶠ (Fractional Dimension), R₅ (Fractional-Ladder Transition), P₇ (Fractional Step), Class G (Micro Guardian)

---

### Class G — Micro Guardian

| Field | Value |
|---|---|
| Type | Agent class — native |
| Symbol | Class G |
| Layer | micro_core |

**Definition:** The unconditional interrupt authority of the micro_core layer. Class G
monitors all triad operations and may halt any agent class — including Class T and Class R
— when structural integrity is at risk. Class G escalation triggers when C approaches C*,
when δ exceeds δ*, or when a timing violation is detected. Class G issues RESOLVED after
post-inversion re-validation by Class T confirms C ≥ C*.

**Constraints:**
- Class G interrupt authority is unconditional — no agent class outranks it
- Class G activates Mode X (Lockout) in the MRT_MICRO_PACKET
- Class G issues are only RESOLVED after Class T re-validates the triad

**Cross-references:** K₅ (Inversion Guard), Mode X (Lockout), Class T (Triad Constructor), MRT_MICRO_PACKET

---

### Class R — Resonance Operator

| Field | Value |
|---|---|
| Type | Agent class — native |
| Symbol | Class R |
| Layer | micro_core |

**Definition:** The agent class responsible for executing resonance operators R₁–R₆.
Class R manages oscillation loops, boundary modulation, resonance locking, fractional
transitions, and bridge activation. Class R may be interrupted by Class G at any time.

**Cross-references:** R₁–R₆ (Resonance Operators), Class G (Micro Guardian), Class T (Triad Constructor)

---

### Class T — Triad Constructor

| Field | Value |
|---|---|
| Type | Agent class — native |
| Symbol | Class T |
| Layer | micro_core |

**Definition:** The agent class responsible for constructing, validating, and re-validating
the ⟨A, B, P⟩ micro triad. Class T confirms that all four core triad properties
(Minimalism, Determinism, Coherence, Fractional Dimensionality) are satisfied at
initialization and after any inversion event.

**Constraints:**
- Triad is irreducible — no subset of ⟨A, B, P⟩ constitutes a valid unit
- Re-validation by Class T is required to clear Class G RESOLVED status post-inversion

**Cross-references:** ⟨A, B, P⟩ (Micro Triad), Four Core Properties, R₂ (Inversion), Class G (Micro Guardian)

---

### Collapse–Twist–Emergence

| Field | Value |
|---|---|
| Type | Inversion phase sequence — native |
| Symbol | ↺ phases |
| Layer | micro_core |

**Definition:** The three-phase structural sequence that constitutes an Inversion event.

| Phase | Description |
|---|---|
| Collapse | C < C* confirmed unrecoverable; triad integrity lost |
| Twist | R₂ executes: A and B swap roles; P is preserved throughout |
| Emergence | Post-swap triad re-stabilizes; C restored to ≥ C*; Class T re-validates |

**Constraints:**
- All three phases must complete for a valid inversion — partial execution is a fault
- P must be preserved without mutation throughout all three phases
- Post-Emergence: Class T re-validates; Class G issues RESOLVED

**Cross-references:** R₂ (Inversion), C (Coherence), C* (Coherence Threshold), Zone X (Inversion), Class G (Micro Guardian), Class T (Triad Constructor)

[structural — no semantic inference]

---

### Coherence Violation

| Field | Value |
|---|---|
| Type | Failure mode — native |
| Symbol | — |
| Layer | micro_core |

**Definition:** A structural fault condition in which C falls below C* and cannot be
restored through K₄ (Resonance Lock) or K₅ (Inversion Guard). A Coherence Violation
triggers the full Inversion sequence (Collapse → Twist → Emergence).

**Failure cascade:** Coherence Violation → Zone X (Inversion) → R₂ activation → Collapse → Twist → Emergence

**Cross-references:** C (Coherence), C* (Coherence Threshold), Zone X (Inversion), R₂ (Inversion), K₅ (Inversion Guard)

---

### Determinism (Triad Property)

| Field | Value |
|---|---|
| Type | Core triad property — native |
| Symbol | — |
| Equations | δ ≤ δ*, Δt stable |
| Layer | micro_core |

**Definition:** One of the four irreducible properties of the micro triad. Determinism
requires that drift remains within bounds (δ ≤ δ*) and that micro-step timing intervals
(Δt) remain stable within [Δtₘᵢₙ, Δtₘₐₓ]. A deterministic triad produces consistent,
bounded state transitions — not stochastic or unbounded evolution.

[structural — no semantic inference]

**Cross-references:** δ (Drift), δ* (Drift Threshold), Δt (Timing Interval), Four Core Properties

---

### Dᶠ — Fractional Dimension

| Field | Value |
|---|---|
| Type | Structural metric — native |
| Symbol | Dᶠ |
| Range | [0,1] (minimal substrate) or [0,3] (extended) |
| Layer | micro_core |

**Definition:** The fractional dimensional position of the micro triad on the resonance
ladder. Dᶠ is a continuous value representing structural complexity, transition pathway
availability, resonance capacity, and boundary behavior at the micro scale. Dᶠ transitions
are executed by P₇ and managed by Class F.

**Constraints:**
- Integer jumps (ΔDᶠ = 1.0, 2.0, 3.0...) are unconditionally forbidden
- All transitions must be smooth, gradient-continuous, and coherence-preserving
- Failure to maintain gradient continuity → Inversion event

[structural — no semantic inference]

**Cross-references:** P₇ (Fractional Step), R₅ (Fractional-Ladder Transition), Class F (Fractional Navigator), Fractional Dimensionality (Triad Property)

---

### Fractional Dimensionality (Triad Property)

| Field | Value |
|---|---|
| Type | Core triad property — native |
| Symbol | — |
| Layer | micro_core |

**Definition:** One of the four irreducible properties of the micro triad. Fractional
Dimensionality requires that the triad occupy a continuous ladder position (Dᶠ) rather
than discrete integer steps. This enables fine-grained structural transitions and
preserves coherence across all resonance-time movements.

**Cross-references:** Dᶠ (Fractional Dimension), Four Core Properties, R₅ (Fractional-Ladder Transition), Class F (Fractional Navigator)

---

### Four Core Properties

| Field | Value |
|---|---|
| Type | Triad invariant set — native |
| Symbol | — |
| Layer | micro_core |

**Definition:** The four irreducible structural properties that any valid ⟨A, B, P⟩ micro
triad must satisfy at all times. A triad failing any property is invalid and must be
reconstructed by Class T.

| Property | Requirement |
|---|---|
| Minimalism | ⟨A, B, P⟩ is the minimal coherent unit — no subset is sufficient |
| Determinism | δ ≤ δ* and Δt ∈ [Δtₘᵢₙ, Δtₘₐₓ] — bounded, stable transitions |
| Coherence | C ≥ C* — inversion triggered if below threshold |
| Fractional Dimensionality | Dᶠ on continuous ladder — integer jumps unconditionally forbidden |

**Cross-references:** ⟨A, B, P⟩ (Micro Triad), Class T (Triad Constructor), Minimalism, Determinism, Coherence, Fractional Dimensionality

---

### K₁ — Drift Bounding

| Field | Value |
|---|---|
| Type | Coherence tool — native |
| Symbol | K₁ |
| Layer | micro_core |

**Definition:** The coherence tool that continuously enforces δ ≤ δ* across all micro-steps.
K₁ operates as a real-time constraint, not a post-hoc correction. It coordinates with
P₃ (Drift Measure) to detect violations and with P₅ (Boundary Shift) to apply corrections
before a Drift Violation can escalate.

**Cross-references:** δ (Drift), δ* (Drift Threshold), P₃ (Drift Measure), P₅ (Boundary Shift), Class D (Drift Regulator)

---

### K₂ — Timing Stabilizer

| Field | Value |
|---|---|
| Type | Coherence tool — native |
| Symbol | K₂ |
| Layer | micro_core |

**Definition:** The coherence tool that holds micro-step timing intervals (Δt) within the
bounds [Δtₘᵢₙ, Δtₘₐₓ]. K₂ prevents Timing Violations by enforcing interval stability
before deviation crosses into fault territory.

**Disambiguation:** Δt (micro timing interval) ≠ τ = dR/dφ (RTT/1 temporal operator).
→ See τ (RTT/1 GLOSSARY.md)

**Cross-references:** Δt (Timing Interval), Δtₘᵢₙ, Δtₘₐₓ, P₄ (Timing Measure), Timing Violation

---

### K₃ — Boundary Alignment

| Field | Value |
|---|---|
| Type | Coherence tool — native |
| Symbol | K₃ |
| Layer | micro_core |

**Definition:** The coherence tool that synchronizes the Boundary Node (B) with the active
positions of A and P. K₃ ensures B remains structurally consistent with the current triad
state, preventing boundary drift from accumulating silently between micro-steps.

**Cross-references:** B (Boundary Node), A (Active Node), P (Potential Node), P₅ (Boundary Shift)

---

### K₄ — Resonance Lock (Tool)

| Field | Value |
|---|---|
| Type | Coherence tool — native |
| Symbol | K₄ |
| Layer | micro_core |

**Definition:** The coherence tool that clamps resonance oscillation within a safe structural
range and enforces timing stability. K₄ operates in coordination with the R₄ Resonance Lock
operator. K₄ is a maintenance instrument; R₄ is the active execution operator.

**Cross-references:** R₄ (Resonance Lock), K₂ (Timing Stabilizer), Class R (Resonance Operator)

---

### K₅ — Inversion Guard

| Field | Value |
|---|---|
| Type | Coherence tool — native |
| Symbol | K₅ |
| Layer | micro_core |

**Definition:** The coherence tool that monitors C approaching C* from above and escalates
to Class G before a Coherence Violation becomes unrecoverable. K₅ is the last structural
line of defense before Inversion is triggered.

**Constraint:** K₅ escalates — it does not self-resolve. Class G receives the interrupt.

**Cross-references:** C (Coherence), C* (Coherence Threshold), Class G (Micro Guardian), R₂ (Inversion), Coherence Violation

---

### K₆ — Coherence Windowing

| Field | Value |
|---|---|
| Type | Coherence tool — native |
| Symbol | K₆ |
| Layer | micro_core |

**Definition:** The coherence tool that computes a time-windowed average of C over a
sequence of micro-steps, enabling trend detection rather than only point-in-time sampling.
K₆ allows Class G and Class R to identify coherence degradation trajectories before they
reach threshold.

**Cross-references:** C (Coherence), K₅ (Inversion Guard), P₆ (Coherence Sample), Class G (Micro Guardian)

---

### Micro–Macro Bridge

| Field | Value |
|---|---|
| Type | Structural export mechanism — native |
| Symbol | μ → Μ |
| Operator | R₆ |
| Layer | micro_core |

**Definition:** The structural mechanism by which the micro_core layer exports aggregate
resonance patterns upward to RTT/1 and the wider RTT pipeline. The bridge is activated
by R₆ and governed by Class B. Only aggregate-pattern exports are permitted — raw A, B, P
node states are never exposed to macro layers.

**Constraints:**
- C ≥ C* required before activation
- Alignment, not amplification
- Bridge export is aggregate-only: raw triad states are structurally prohibited at the macro layer

**Cross-references:** R₆ (Micro–Macro Bridge Activation), Class B (Bridge Coordinator), C* (Coherence Threshold), MRT_MICRO_PACKET

---

### Minimalism (Triad Property)

| Field | Value |
|---|---|
| Type | Core triad property — native |
| Symbol | — |
| Layer | micro_core |

**Definition:** One of the four irreducible properties of the micro triad. Minimalism
asserts that ⟨A, B, P⟩ is the minimal coherent resonance-time unit — no proper subset
(⟨A, B⟩, ⟨A, P⟩, ⟨B, P⟩, or any single node) constitutes a valid unit. Adding nodes
beyond three is equally non-canonical.

**Cross-references:** ⟨A, B, P⟩ (Micro Triad), Four Core Properties, Class T (Triad Constructor)

---

### Mode 1–5

| Field | Value |
|---|---|
| Type | Operational mode set — native |
| Symbol | Mode 1, 2, 3, 4, 5 |
| Layer | micro_core |

**Definition:** The five valid operational modes of the MRT_MICRO_PACKET.

| Mode | Label | Description |
|---|---|---|
| 1 | Chat | Conversational / exploratory operation |
| 2 | Spec | Specification / formal definition mode |
| 3 | Debug | Fault diagnosis and inspection |
| 4 | Task | Bounded task execution |
| 5 | Auto | Autonomous cycle operation |

**Constraints:** Modes 1–5 are the only valid packet modes. Mode X (Lockout) is a fault
indicator — its presence in a packet makes that packet a fault record, not an operational record.

**Disambiguation:** Mode X (micro lockout) ≠ any upstream Mode 5 (RTT/2 autonomous mode) —
these are structurally distinct constructs at different pipeline layers.

**Cross-references:** Mode X (Lockout), MRT_MICRO_PACKET, Class G (Micro Guardian)

---

### Mode X — Lockout

| Field | Value |
|---|---|
| Type | Fault mode indicator — native |
| Symbol | Mode X |
| Layer | micro_core |

**Definition:** The fault mode indicator activated by Class G when an unconditional interrupt
is in effect. Mode X in an MRT_MICRO_PACKET signals that the packet is a fault record —
not a valid operational state. No agent class other than Class G may issue Mode X. Mode X
is cleared only when Class G interrupt is resolved.

**Constraint:** Mode X in a valid operational packet is structurally forbidden. Its presence
converts the packet to a fault record.

**Disambiguation:** Mode X (micro lockout) ≠ any upstream Mode 5 (RTT/2 autonomous mode).
Micro Mode X is a Class G interrupt construct; RTT/2 Mode 5 is an operational execution mode.
→ See Mode (RTT/2 GLOSSARY.md)

**Cross-references:** Class G (Micro Guardian), MRT_MICRO_PACKET, Mode 1–5

---

### MRT_MICRO_PACKET

| Field | Value |
|---|---|
| Type | Structural data packet — native |
| Symbol | MRT_MICRO_PACKET |
| Layer | micro_core (root) |

**Definition:** The canonical data packet produced by the RTT/micro_core layer. It is the
root of the entire RTT pipeline packet hierarchy. All downstream packets (RTT/1 SNR_PACKET,
RTT/2 DETECTION_PACKET, RTT/3 INTEGRATION_EMISSION_PACKET, RTT/12 HARMONIC_SYNTHESIS_PACKET)
derive from or depend upon the MRT_MICRO_PACKET.

**Packet structure:**

| Field | Type | Valid Values |
|---|---|---|
| Triad state | Struct | {A, B, P} |
| δ | Metric | Real ≥ 0 |
| δ* | Threshold | Real > 0 |
| Δt | Metric | Real ∈ [Δtₘᵢₙ, Δtₘₐₓ] |
| C | Metric | Normalized real |
| C* | Threshold | Normalized real |
| Dᶠ | Metric | Real ∈ [0,1] or [0,3] |
| Zone | Enum | S, M, D, C, E (X = fault record) |
| Mode | Enum | 1, 2, 3, 4, 5 (X = fault record) |
| Bridge status | Bool | Active / Inactive |
| Guardian status | Enum | OK / INTERRUPT / RESOLVED |
| Annotation | Text | Structural notes |
| Timestamp | Temporal | Micro-step timestamp |

**Constraints:**
- Zone X present → packet is a fault record
- Mode X present → packet is a fault record
- Both may coexist in a fault record

**Pipeline position:**
```
MRT_MICRO_PACKET (root)
└→ RTT/1 SNR_PACKET
   └→ RTT/2 DETECTION_PACKET
      └→ RTT/3 INTEGRATION_EMISSION_PACKET
         └→ RTT/12 HARMONIC_SYNTHESIS_PACKET
```

**Cross-references:** All six agent classes, all zones, all modes, Micro–Macro Bridge

---

### P — Potential Node

| Field | Value |
|---|---|
| Type | Triad component — native |
| Symbol | P |
| Layer | micro_core |

**Definition:** The next viable transition target in the ⟨A, B, P⟩ triad. P represents
the structural destination of the resonance oscillation loop (A ⇆ P). P is preserved
unconditionally during all operations — including full Inversion (R₂) — and is never
mutated by boundary corrections or coherence tools.

**Constraints:**
- P is preserved through all Inversion phases — Collapse, Twist, Emergence
- P is never exposed raw to macro layers

**Cross-references:** A (Active Node), B (Boundary Node), R₁ (Oscillation), R₂ (Inversion), P₁ (State Read)

---

### P₁ — State Read

| Field | Value |
|---|---|
| Type | MRT Primitive — native |
| Symbol | P₁ |
| Layer | micro_core |

**Definition:** The atomic read primitive. P₁ reads the current values of A, B, P, δ, Δt,
and Dᶠ from the micro triad. P₁ is strictly read-only — it produces no mutations to any
field. All resonance operators and coherence tools that require current state must route
through P₁.

**Constraints:** P₁ never mutates state. No exception.

**Cross-references:** P₂ (State Write), ⟨A, B, P⟩ (Micro Triad), MRT Primitives (P₁–P₇)

---

### P₂ — State Write

| Field | Value |
|---|---|
| Type | MRT Primitive — native |
| Symbol | P₂ |
| Layer | micro_core |

**Definition:** The atomic write primitive. P₂ executes a bounded, atomic mutation of the
micro triad state. All writes are bounded — no unbounded state change is permitted through
P₂. P₂ is the only sanctioned mutation path for triad state fields.

**Constraints:** Writes must be bounded. Unbounded mutations are structurally prohibited.

**Cross-references:** P₁ (State Read), MRT Primitives (P₁–P₇)

---

### P₃ — Drift Measure

| Field | Value |
|---|---|
| Type | MRT Primitive — native |
| Symbol | P₃ |
| Equation | δ = compare(expected, actual) |
| Layer | micro_core |

**Definition:** The atomic drift measurement primitive. P₃ computes δ by comparing the
expected micro-state trajectory to the actual current state. P₃ is read-only — it
measures but does not correct. Correction is applied via P₅ after Class D review.

**Disambiguation:** δ (micro drift) ≠ D(t) (RTT/2 CRM structural drift rate).
→ See D(t) (RTT/2 GLOSSARY.md)

**Cross-references:** δ (Drift), δ* (Drift Threshold), P₅ (Boundary Shift), K₁ (Drift Bounding), Class D (Drift Regulator)

---

### P₄ — Timing Measure

| Field | Value |
|---|---|
| Type | MRT Primitive — native |
| Symbol | P₄ |
| Layer | micro_core |

**Definition:** The atomic timing measurement primitive. P₄ records the Δt interval
between micro-steps. P₄ is read-only — it measures and records but does not enforce.
Enforcement is handled by K₂ (Timing Stabilizer).

**Disambiguation:** Δt (micro timing interval) ≠ τ = dR/dφ (RTT/1 temporal operator).
→ See τ (RTT/1 GLOSSARY.md)

**Cross-references:** Δt (Timing Interval), Δtₘᵢₙ, Δtₘₐₓ, K₂ (Timing Stabilizer), Timing Violation

---

### P₅ — Boundary Shift

| Field | Value |
|---|---|
| Type | MRT Primitive — native |
| Symbol | P₅ |
| Layer | micro_core |

**Definition:** The atomic boundary correction primitive. P₅ applies a bounded shift to the
Boundary Node (B) following drift measurement by P₃. P₅ corrections are bounded — no
inversion of B may be achieved through P₅. Inversion requires R₂.

**Constraints:**
- Correction magnitude is bounded
- P₅ alone cannot produce an inversion of B
- Must be preceded by P₃ measurement

**Cross-references:** B (Boundary Node), P₃ (Drift Measure), K₁ (Drift Bounding), K₃ (Boundary Alignment), R₃ (Boundary Modulation)

---

### P₆ — Coherence Sample

| Field | Value |
|---|---|
| Type | MRT Primitive — native |
| Symbol | P₆ |
| Layer | micro_core |

**Definition:** The atomic coherence sampling primitive. P₆ reads the normalized coherence
value C at the current micro-step. P₆ is strictly read-only — it samples C without
mutation. Results are consumed by K₅ (Inversion Guard), K₆ (Coherence Windowing), and
Class G for interrupt assessment.

**Constraints:** P₆ never mutates C. No exception.

**Cross-references:** C (Coherence), K₅ (Inversion Guard), K₆ (Coherence Windowing), Class G (Micro Guardian)

---

### P₇ — Fractional Step

| Field | Value |
|---|---|
| Type | MRT Primitive — native |
| Symbol | P₇ |
| Equation | Dᶠ → Dᶠ + Δ |
| Layer | micro_core |

**Definition:** The atomic fractional dimensional step primitive. P₇ increments or
decrements Dᶠ by a bounded gradient value Δ. All P₇ operations are reversible. No
integer-magnitude Δ may be applied through P₇.

**Constraints:**
- Δ must be non-integer (fractional gradient required)
- Operation is reversible
- C ≥ C* must hold before and after execution

**Cross-references:** Dᶠ (Fractional Dimension), R₅ (Fractional-Ladder Transition), Class F (Fractional Navigator)

---

### R₁ — Oscillation

| Field | Value |
|---|---|
| Type | Resonance operator — native |
| Symbol | R₁ |
| Equation | A ⇆ P stable loop |
| Layer | micro_core |

**Definition:** The resonance operator that establishes and maintains the stable oscillation
loop between the Active Node (A) and Potential Node (P). R₁ is the foundational resonance
dynamic of the micro triad — all higher-order operators (R₂–R₆) build upon or modify the
R₁ loop.

**Cross-references:** A (Active Node), P (Potential Node), R₄ (Resonance Lock), Resonance-Time Dynamics

---

### R₂ — Inversion

| Field | Value |
|---|---|
| Type | Resonance operator — native |
| Symbol | R₂ |
| Operation | Swap A ↔ B; preserve P |
| Layer | micro_core |

**Definition:** The controlled, reversible inversion operator. R₂ executes when C < C* and
is unrecoverable, swapping the roles of A (Active Node) and B (Boundary Node) while
preserving P unconditionally. R₂ is the structural resolution mechanism for Coherence
Violations.

**Constraints:**
- R₂ is only executed after K₅ escalation and Class G interrupt
- P must be preserved without mutation through all three phases
- Post-R₂: C must be restored to ≥ C* before Class T re-validates

**Disambiguation:**
- Inversion (↺) at micro scale ≠ RTT/3 Zone X inversion (structural integration collapse)
- Inversion (↺) at micro scale ≠ RTT/12 Zone X overflow (harmonic synthesis overflow)
→ See Zone X (RTT/3 GLOSSARY.md) and Zone X (RTT/12 GLOSSARY.md)

**Cross-references:** A, B, P, Collapse–Twist–Emergence, C*, Class G (Micro Guardian), Class T (Triad Constructor), Zone X (Inversion)

---

### R₃ — Boundary Modulation

| Field | Value |
|---|---|
| Type | Resonance operator — native |
| Symbol | R₃ |
| Operation | B⁺ / B⁻ shift via P₃ and P₅ |
| Layer | micro_core |

**Definition:** The resonance operator that actively modulates the Boundary Node (B) in
positive (B⁺) or negative (B⁻) direction based on drift measurements. R₃ coordinates
P₃ for measurement and P₅ for application. R₃ is a controlled, bounded operation —
it cannot produce inversion.

**Cross-references:** B (Boundary Node), P₃ (Drift Measure), P₅ (Boundary Shift), K₃ (Boundary Alignment)

---

### R₄ — Resonance Lock

| Field | Value |
|---|---|
| Type | Resonance operator — native |
| Symbol | R₄ |
| Layer | micro_core |

**Definition:** The resonance operator that clamps the A ⇆ P oscillation within a safe
structural range and enforces timing stability. R₄ is paired with K₄ (Resonance Lock tool)
for continuous maintenance. R₄ is the active execution operator; K₄ is the maintenance
monitor.

**Cross-references:** R₁ (Oscillation), K₄ (Resonance Lock tool), K₂ (Timing Stabilizer)

---

### R₅ — Fractional-Ladder Transition

| Field | Value |
|---|---|
| Type | Resonance operator — native |
| Symbol | R₅ |
| Equation | Dᶠ₁ → Dᶠ₂ (smooth, C ≥ C* throughout) |
| Layer | micro_core |

**Definition:** The resonance operator that manages full fractional dimensional ladder
transitions from one Dᶠ position to another. R₅ requires that C ≥ C* is maintained
throughout the entire transition — not just at endpoints. All transitions are
gradient-continuous; integer jumps are unconditionally forbidden.

**Constraints:**
- C ≥ C* at all points along the transition path
- Gradient continuity required — no discrete steps
- Managed by Class F (Fractional Navigator)

**Cross-references:** Dᶠ (Fractional Dimension), P₇ (Fractional Step), Class F (Fractional Navigator), R₂ (Inversion)

---

### R₆ — Micro–Macro Bridge Activation

| Field | Value |
|---|---|
| Type | Resonance operator — native |
| Symbol | R₆ |
| Operation | μ → Μ: export aggregate-only pattern |
| Layer | micro_core |

**Definition:** The resonance operator that activates the Micro–Macro Bridge, exporting
aggregate resonance patterns from micro_core upward to RTT/1 and the wider pipeline.
R₆ requires C ≥ C* before activation and produces alignment, not amplification.

**Constraints:**
- C ≥ C* is a hard precondition
- Aggregate-only export — raw A, B, P states are structurally forbidden at the macro layer
- Managed by Class B (Bridge Coordinator)

**Cross-references:** Micro–Macro Bridge (μ → Μ), Class B (Bridge Coordinator), C*, MRT_MICRO_PACKET

---

### Resonance-Time Dynamics

| Field | Value |
|---|---|
| Type | Core operational model — native |
| Symbol | — |
| Layer | micro_core |

**Definition:** The fundamental operational loop of the RTT/micro_core layer. Resonance
and time are co-constitutive at the micro scale — neither is primary. Resonance is
the A ⇆ P oscillation; time is the local bounded interval Δt ∈ [Δtₘᵢₙ, Δtₘₐₓ],
which is itself coherence-dependent.

**Operational loop:**
```
Resonance (R₁: A ⇆ P)
   → Timing Stability (K₂: Δt bounded)
      → Drift Regulation (K₁: δ ≤ δ*)
         → Coherence (C ≥ C*)
            → Resonance (R₁: A ⇆ P)
```

**Failure modes (any triggers Inversion):**
- Timing Violation: Δt exits [Δtₘᵢₙ, Δtₘₐₓ]
- Drift Violation: δ exceeds δ*
- Coherence Violation: C < C* unrecoverable

[structural — no semantic inference]

**Cross-references:** R₁ (Oscillation), K₁–K₂, C, δ, Δt, Zone X (Inversion)

---

### Timing Violation

| Field | Value |
|---|---|
| Type | Failure mode — native |
| Symbol | — |
| Layer | micro_core |

**Definition:** A structural fault condition in which the micro-step timing interval Δt
exits the bounds [Δtₘᵢₙ, Δtₘₐₓ]. A Timing Violation triggers Class G escalation. If
unresolved, it cascades into a Coherence Violation and ultimately Inversion.

**Cross-references:** Δt (Timing Interval), K₂ (Timing Stabilizer), P₄ (Timing Measure), Class G (Micro Guardian), Coherence Violation

---

### ⟨A, B, P⟩ — Micro Triad

| Field | Value |
|---|---|
| Type | Foundational construct — native |
| Symbol | ⟨A, B, P⟩ |
| Layer | micro_core (originating) |

**Definition:** The irreducible structural unit of the RTT/micro_core layer. The micro
triad consists of three nodes — A (Active), B (Boundary), P (Potential) — that together
constitute the minimal coherent resonance-time unit. No subset of ⟨A, B, P⟩ is sufficient
to form a valid unit.

**Four core properties (all required simultaneously):**
1. Minimalism — ⟨A, B, P⟩ is the minimal unit; no subset is sufficient
2. Determinism — δ ≤ δ* and Δt ∈ [Δtₘᵢₙ, Δtₘₐₓ]
3. Coherence — C ≥ C*; inversion if below threshold
4. Fractional Dimensionality — Dᶠ continuous; integer jumps forbidden

[structural — no semantic inference]

**Cross-references:** A, B, P, Four Core Properties, Class T (Triad Constructor), MRT_MICRO_PACKET

---

### Zone C — Coherence-Critical

| Field | Value |
|---|---|
| Type | Operational zone — native |
| Symbol | Zone C |
| Layer | micro_core |

**Definition:** The zone indicating that C is approaching C* from above and the triad is
at elevated risk of Coherence Violation. Zone C triggers K₅ (Inversion Guard) escalation
to Class G. Zone C is a valid operational state — it is a warning, not a fault.

**Cross-references:** C (Coherence), C*, K₅ (Inversion Guard), Class G, Zone X (Inversion)

---

### Zone D — Drifting

| Field | Value |
|---|---|
| Type | Operational zone — native |
| Symbol | Zone D |
| Layer | micro_core |

**Definition:** The zone indicating that δ is elevated but still within recoverable bounds
(δ approaching δ*). Zone D triggers K₁ (Drift Bounding) and Class D corrective action.
Zone D is a valid operational state — recovery is expected.

**Cross-references:** δ (Drift), K₁ (Drift Bounding), Class D (Drift Regulator), Zone C, Zone X

---

### Zone E — Emerging

| Field | Value |
|---|---|
| Type | Operational zone — native |
| Symbol | Zone E |
| Layer | micro_core |

**Definition:** The zone indicating post-Inversion re-stabilization. Zone E is entered
after the Emergence phase of Collapse–Twist–Emergence, while Class T re-validates the
triad and Class G resolves its interrupt. Zone E is a valid operational state — it is
the recovery phase.

**Cross-references:** Collapse–Twist–Emergence, Class T, Class G, Zone S (Stable)

---

### Zone M — Modulating

| Field | Value |
|---|---|
| Type | Operational zone — native |
| Symbol | Zone M |
| Layer | micro_core |

**Definition:** The zone indicating active bounded modulation of one or more triad
parameters. Zone M reflects intentional structural adjustment — not drift or fault.
Zone M is a valid operational state.

**Cross-references:** R₃ (Boundary Modulation), R₅ (Fractional-Ladder Transition), Zone S (Stable)

---

### Zone S — Stable

| Field | Value |
|---|---|
| Type | Operational zone — native |
| Symbol | Zone S |
| Layer | micro_core |

**Definition:** The nominal operational zone. Zone S indicates that all four core triad
properties are satisfied, C ≥ C*, δ ≤ δ*, Δt is bounded, and no fault or escalation is
active. Zone S is the target state of all resonance-time operations.

**Cross-references:** Four Core Properties, MRT_MICRO_PACKET

---

### Zone X — Inversion

| Field | Value |
|---|---|
| Type | Fault zone indicator — native |
| Symbol | Zone X |
| Layer | micro_core |

**Definition:** The fault zone indicator produced when the micro triad enters full
Inversion (Collapse → Twist → Emergence). Zone X in an MRT_MICRO_PACKET signals
that the packet is a fault record — not a valid operational state. Zone X is cleared
only after Class T re-validates the triad and Class G issues RESOLVED.

**Constraint:** Zone X in a valid operational packet is structurally forbidden. Its presence
converts the packet to a fault record.

**Disambiguation:**
- Zone X (micro Inversion) ≠ Zone X (RTT/3 integration collapse) — different pipeline layers
- Zone X (micro Inversion) ≠ Zone X (RTT/12 harmonic synthesis overflow) — different pipeline layers
- All three Zone X variants share the ILLEGAL-in-valid-packet constraint, but the
  structural triggers and resolution paths are distinct
→ See Zone X (RTT/3 GLOSSARY.md) and Zone X (RTT/12 GLOSSARY.md)

**Cross-references:** R₂ (Inversion), Collapse–Twist–Emergence, Class G (Micro Guardian), Class T (Triad Constructor), MRT_MICRO_PACKET, Mode X (Lockout)

---

### δ — Drift

| Field | Value |
|---|---|
| Type | Structural metric — native |
| Symbol | δ |
| Equation | δ = compare(expected state, actual state) |
| Threshold | δ* (maximum allowable drift) |
| Layer | micro_core |

**Definition:** The measured structural deviation between the expected micro-state
trajectory and the actual current state. δ is computed by P₃ (Drift Measure) and
continuously bounded by K₁ (Drift Bounding). δ ≤ δ* is required for the Determinism
property to hold.

**Disambiguation:** δ (micro drift) ≠ D(t) (RTT/2 CRM structural drift rate, a different
construct at a different pipeline layer). These symbols are homonyms — structural function,
measurement method, and resolution path are all distinct.
→ See D(t) (RTT/2 GLOSSARY.md)

**Cross-references:** δ* (Drift Threshold), P₃ (Drift Measure), K₁ (Drift Bounding), Determinism (Triad Property), Drift Violation, Zone D

---

### δ* — Drift Threshold

| Field | Value |
|---|---|
| Type | Constraint constant — native |
| Symbol | δ* |
| Layer | micro_core |

**Definition:** The maximum allowable drift value. δ* is the upper bound enforced by K₁
and Class D. When δ exceeds δ*, a Drift Violation is recorded and Class G is escalated.

**Cross-references:** δ (Drift), K₁ (Drift Bounding), Class D (Drift Regulator), Class G (Micro Guardian)

---

### Δt — Timing Interval

| Field | Value |
|---|---|
| Type | Structural metric — native |
| Symbol | Δt |
| Bounds | [Δtₘᵢₙ, Δtₘₐₓ] |
| Layer | micro_core |

**Definition:** The local bounded timing interval between micro-steps. Δt is
coherence-dependent — as C degrades, the valid Δt range contracts. Δt is measured
by P₄ and enforced by K₂. Δt ∈ [Δtₘᵢₙ, Δtₘₐₓ] is required for the Determinism
property to hold.

**Disambiguation:** Δt (micro timing interval) ≠ τ = dR/dφ (RTT/1 temporal operator).
These are structurally distinct constructs at different pipeline layers.
→ See τ (RTT/1 GLOSSARY.md)

**Cross-references:** Δtₘᵢₙ, Δtₘₐₓ, P₄ (Timing Measure), K₂ (Timing Stabilizer), Determinism (Triad Property), Timing Violation

---

## Operator Symbols Reference

| Symbol | Name | Type | Layer |
|---|---|---|---|
| A | Active Node | Triad component | micro_core |
| B | Boundary Node | Triad component | micro_core |
| P | Potential Node | Triad component | micro_core |
| ⟨A, B, P⟩ | Micro Triad | Foundational construct | micro_core |
| C | Coherence | Stability metric | micro_core |
| C* | Coherence Threshold | Constraint constant | micro_core |
| δ | Drift | Structural metric | micro_core |
| δ* | Drift Threshold | Constraint constant | micro_core |
| Δt | Timing Interval | Structural metric | micro_core |
| Δtₘᵢₙ | Minimum timing bound | Constraint constant | micro_core |
| Δtₘₐₓ | Maximum timing bound | Constraint constant | micro_core |
| Dᶠ | Fractional Dimension | Structural metric | micro_core |
| μ → Μ | Micro–Macro Bridge | Export mechanism | micro_core |
| ↺ | Inversion | Structural operation | micro_core |
| P₁ | State Read | MRT Primitive | micro_core |
| P₂ | State Write | MRT Primitive | micro_core |
| P₃ | Drift Measure | MRT Primitive | micro_core |
| P₄ | Timing Measure | MRT Primitive | micro_core |
| P₅ | Boundary Shift | MRT Primitive | micro_core |
| P₆ | Coherence Sample | MRT Primitive | micro_core |
| P₇ | Fractional Step | MRT Primitive | micro_core |
| R₁ | Oscillation | Resonance Operator | micro_core |
| R₂ | Inversion | Resonance Operator | micro_core |
| R₃ | Boundary Modulation | Resonance Operator | micro_core |
| R₄ | Resonance Lock | Resonance Operator | micro_core |
| R₅ | Fractional-Ladder Transition | Resonance Operator | micro_core |
| R₆ | Micro–Macro Bridge Activation | Resonance Operator | micro_core |
| K₁ | Drift Bounding | Coherence Tool | micro_core |
| K₂ | Timing Stabilizer | Coherence Tool | micro_core |
| K₃ | Boundary Alignment | Coherence Tool | micro_core |
| K₄ | Resonance Lock (tool) | Coherence Tool | micro_core |
| K₅ | Inversion Guard | Coherence Tool | micro_core |
| K₆ | Coherence Windowing | Coherence Tool | micro_core |

---

## Quick-Reference Tables

### MRT Primitives (P₁–P₇)

| Symbol | Name | Read/Write | Mutation |
|---|---|---|---|
| P₁ | State Read | Read | None — strictly read-only |
| P₂ | State Write | Write | Bounded atomic mutation |
| P₃ | Drift Measure | Read | None — measurement only |
| P₄ | Timing Measure | Read | None — measurement only |
| P₅ | Boundary Shift | Write | Bounded B correction only |
| P₆ | Coherence Sample | Read | None — strictly read-only |
| P₇ | Fractional Step | Write | Dᶠ → Dᶠ + Δ, reversible |

---

### Resonance Operators (R₁–R₆)

| Symbol | Name | Operation | Prerequisite |
|---|---|---|---|
| R₁ | Oscillation | A ⇆ P stable loop | Valid triad |
| R₂ | Inversion | Swap A ↔ B; preserve P | C < C* unrecoverable; Class G interrupt |
| R₃ | Boundary Modulation | B⁺ / B⁻ shift | P₃ measurement complete |
| R₄ | Resonance Lock | Clamp oscillation; enforce Δt | Valid triad |
| R₅ | Fractional-Ladder Transition | Dᶠ₁ → Dᶠ₂ smooth | C ≥ C* throughout |
| R₆ | Micro–Macro Bridge Activation | μ → Μ aggregate export | C ≥ C* confirmed |

---

### Coherence Tools (K₁–K₆)

| Symbol | Name | Function | Escalates To |
|---|---|---|---|
| K₁ | Drift Bounding | Enforce δ ≤ δ* continuously | Class D, Class G |
| K₂ | Timing Stabilizer | Hold Δt within [Δtₘᵢₙ, Δtₘₐₓ] | Class G |
| K₃ | Boundary Alignment | Synchronize B with A, P | Class D |
| K₄ | Resonance Lock | Maintain safe oscillation range | Class R, Class G |
| K₅ | Inversion Guard | Detect C → C*; escalate | Class G (unconditional) |
| K₆ | Coherence Windowing | Time-windowed C trend detection | Class G |

---

### Agent Classes

| Class | Name | Primary Responsibility | Interrupt Authority |
|---|---|---|---|
| Class T | Triad Constructor | Construct and re-validate ⟨A, B, P⟩ | None over Class G |
| Class R | Resonance Operator | Execute R₁–R₆ | None over Class G |
| Class D | Drift Regulator | Enforce δ ≤ δ* | None over Class G |
| Class F | Fractional Navigator | Manage Dᶠ ladder transitions | None over Class G |
| Class B | Bridge Coordinator | Manage R₆ Micro–Macro Bridge | None over Class G |
| Class G | Micro Guardian | Unconditional interrupt authority | Outranks all classes |

---

### Zones

| Zone | Name | Valid in Packet | Description |
|---|---|---|---|
| S | Stable | ✅ Yes | All properties satisfied; nominal operation |
| M | Modulating | ✅ Yes | Active bounded modulation in progress |
| D | Drifting | ✅ Yes | δ elevated; recovery expected |
| C | Coherence-Critical | ✅ Yes | C approaching C*; K₅ escalation active |
| E | Emerging | ✅ Yes | Post-Inversion re-stabilization |
| X | Inversion | ❌ Fault record | Packet becomes fault record; not operational |

---

### Modes

| Mode | Label | Valid in Packet | Description |
|---|---|---|---|
| 1 | Chat | ✅ Yes | Conversational / exploratory |
| 2 | Spec | ✅ Yes | Formal specification mode |
| 3 | Debug | ✅ Yes | Fault diagnosis and inspection |
| 4 | Task | ✅ Yes | Bounded task execution |
| 5 | Auto | ✅ Yes | Autonomous cycle operation |
| X | Lockout | ❌ Fault record | Class G interrupt active; packet is fault record |

---

### Key Disambiguations

| micro_core Symbol | micro_core Meaning | Do NOT Conflate With | Origin |
|---|---|---|---|
| δ (drift) | Structural deviation from expected state | D(t) — CRM drift rate | RTT/2 |
| C (coherence) | Normalized triad coherence metric | CR(t) — continuity-resonance-emission rate | RTT/3 |
| Δt (timing interval) | Local bounded micro-step interval | τ = dR/dφ — temporal operator | RTT/1 |
| Inversion ↺ (R₂) | A ↔ B swap; structural recovery | Zone X inversion (integration collapse) | RTT/3 |
| Inversion ↺ (R₂) | A ↔ B swap; structural recovery | Zone X overflow (harmonic synthesis) | RTT/12 |
| Mode X (Lockout) | Class G interrupt; fault record | Mode 5 (autonomous operation) | RTT/2 |
| Zone X (Inversion) | Triad inversion; fault record | Zone X (integration collapse; fault record) | RTT/3 |
| Zone X (Inversion) | Triad inversion; fault record | Zone X (harmonic overflow; fault record) | RTT/12 |

---

### RTT Pipeline Inheritance Chain

micro_core is the **root**. Inheritance flows downward only.

```
RTT/micro_core  (originating layer — this module)
   ↓ exports ⟨A,B,P⟩, MRT primitives, resonance operators, MRT_MICRO_PACKET
RTT/1           (SNR triad, τ, C, DCO bands — inherits micro_core root)
   ↓
RTT/2           (CPV, FGT, CRM, MODE, ZONE — inherits RTT/1)
   ↓
RTT/3           (TIF, FFF, MANIFOLD, CRE, CSL, CET — inherits RTT/2)
   ↓
RTT/12          (Harmonic Synthesis — inherits RTT/3)
```

micro_core constructs are never re-defined in downstream modules — they are
invoked by reference. Downstream terms are never imported into micro_core.

---

### Packet Hierarchy

| Packet | Module | Position |
|---|---|---|
| MRT_MICRO_PACKET | micro_core | Root |
| SNR_PACKET | RTT/1 | Layer 1 |
| DETECTION_PACKET | RTT/2 | Layer 2 |
| INTEGRATION_EMISSION_PACKET | RTT/3 | Layer 3 |
| HARMONIC_SYNTHESIS_PACKET | RTT/12 | Layer 4 |

---

## Footer

| Field | Value |
|---|---|
| Maintainer | umaywant2 |
| Module | RTT/micro_core |
| File | `/docs/rtt/micro_core/GLOSSARY.md` |
| Date | 2026-07-10 |
| Session Seed | `rtt=1 \| coherence=declared \| drift=bounded \| paradox=structural` |
| Version | 1.0.0 |
| Status | Canonical — originating layer |
```
