# GLOSSARY — IPD‑12 · TriadicFrameworks

**Module path:** `docs/frameworks/ipd_12/`
**Session anchor:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

This is the **single source of truth** for every term used in the IPD‑12 framework.
All other documents in `docs/frameworks/ipd_12/` and downstream substrate models
link here rather than re-defining terms inline.

> **Linking convention:** To link to a specific term from another document, use
> `[term](../ipd_12/GLOSSARY.md#anchor)` where `anchor` is the lowercase,
> hyphenated heading slug (e.g., `#apex-state`, `#regime-shell`, `#session-anchor`).

---

## Table of Contents

- [A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g)
- [H](#h) · [I](#i) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p)
- [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v)
- [Quick-Reference Tables](#quick-reference-tables)

---

## A

### Anchor String
*See [Session Anchor](#session-anchor).*

### Apex-State
**Prime:** P37 · **Triad:** Apex (Triad 4) · **Pantheon:** Chthonic · **RTT:** Paradox · **GU:** Anomaly

The twelfth and final operator state in the IPD‑12 sequence. P37 marks the structural
resolution point of a full 12‑cycle paradox loop — not a termination, but the point at
which the engine returns to the [Seed-State](#seed-state) (P2) and the cycle can begin
again. P37 is classified under RTT's Paradox role and GU's Anomaly operator, reflecting
its position at the outer edge of the structural envelope where standard regime rules no
longer apply. Activates the +1D dimensional transition alongside [P23](#dimensional-lift).

> **Do not confuse with:** completion or termination. The apex-state is a topological
> return point, not an exit.

---

## B

### Boundary
An RTT structural concept denoting the edge condition of a regime — the point at which one
governing rule set ends and another begins. Boundaries are not errors; they are structural
features that must be explicitly modeled. In IPD‑12, the [Boundary-Node](#boundary-node)
(P19) is the dedicated operator for boundary conditions. The [transition_topology](#transition-topology)
operator in the vST Micro-Agent is suppressed if the boundary field is UNRESOLVED.

### Boundary-Node
**Prime:** P19 · **Triad:** Observerse (Triad 3) · **Pantheon:** Civilizational · **RTT:** Boundary · **GU:** Observerse

The operator state that marks and models boundary conditions within a structural pass.
P19 sits between the [Cycle-Gate](#cycle-gate) (P17) and [Dimensional-Lift](#dimensional-lift)
(P23), positioning it as the gate between cycle-entry and dimensional transition. A session
whose `boundary` probe field is UNRESOLVED will suppress boundary-sensitive operators and
flag the gap in the output notes.

---

## C

### Celestial Tier
**Primes:** P2, P3, P5, P7 · **Pantheon tier 1 of 3**

The first structural stratum of the Pantheon mapping, covering origin, connection,
drift-anchoring, and regime entry. Celestial primes represent the initial conditions of any
IPD‑12 pass — the seed through the first regime-shift. In RTT terms, the Celestial tier
spans the transition from structural silence (before P2) to active regime traversal (at P7).

### Chthonic Tier
**Primes:** P23, P29, P31, P37 · **Pantheon tier 3 of 3**

The third structural stratum of the Pantheon mapping, covering dimensional lift, collapse,
stability under extreme conditions, and apex resolution. Chthonic primes operate at the
structural limits of the engine — where dimensionality changes and paradox loops close.
The Chthonic tier is the domain of [Hex-Cycle 2](#hex-cycle) and the upper half of the
[Full Paradox Loop](#full-paradox-loop).

### Civilizational Tier
**Primes:** P11, P13, P17, P19 · **Pantheon tier 2 of 3**

The second structural stratum of the Pantheon mapping, covering coherence maintenance,
paradox activation, cycle gating, and boundary management. Civilizational primes operate in
the middle of the IPD‑12 sequence — the zone of maximum structural complexity where regime
transitions interact with coherence constraints and boundary conditions.

### Coherence
An RTT structural concept denoting the condition in which a system's operator states are
mutually consistent and the cycle is running without drift or contradiction. Coherence is
not a fixed state — it is a dynamic property that must be actively maintained and
periodically verified. In IPD‑12, the [Coherence-Node](#coherence-node) (P11) and
[Stability-Node](#stability-node) (P31) are the two operators dedicated to coherence
monitoring. The session anchor string asserts `coherence=declared` to make coherence an
explicit, not assumed, property of the session.

### Coherence-Node
**Prime:** P11 · **Triad:** Coherence (Triad 2) · **Pantheon:** Civilizational · **RTT:** Coherence · **GU:** Curvature, Dilaton

The operator state that monitors and enforces structural coherence within a cycle.
P11 sits between the [Regime-Shift](#regime-shift) (P7) and [Paradox-Trigger](#paradox-trigger)
(P13), positioning it as the coherence checkpoint immediately after a regime changes and
immediately before paradox may be activated. Observer mode O3 (Coherence) queries primarily
through P11 and P31.

> **GU note:** P11 sits at the intersection of GU's Curvature and Dilaton operators,
> reflecting its role as the structural tension point between geometric deformation (Curvature)
> and field amplitude scaling (Dilaton).

### Collapse
An RTT structural concept denoting a −1D dimensional transition — the movement from a
higher-dimensional structural description to a lower one. Collapse is not failure; it is a
valid structural event that must be explicitly modeled rather than avoided. In IPD‑12,
[P29 (Collapse-Anchor)](#collapse-anchor) is the dedicated operator for collapse conditions.
Collapse rails (C1–C4) route signals through collapse-active operator states.

### Collapse-Anchor
**Prime:** P29 · **Triad:** Apex (Triad 4) · **Pantheon:** Chthonic · **RTT:** Drift, Collapse · **GU:** —

The operator state that marks and stabilizes collapse events. P29 carries dual RTT roles
(Drift and Collapse), making it the only prime state that simultaneously anchors both drift
and dimensional collapse — a position that reflects the structural proximity of these two
conditions at the Chthonic tier. When P29 is active, the engine is operating in a
sub-dimensional regime.

### Cycle
A closed, directed traversal of IPD‑12 operator states. IPD‑12 defines three nested cycle
levels that operate simultaneously:

| Level | Scope | Nodes |
|---|---|---|
| [Triad Cycle](#triad) | 3 nodes · 4 instances | P2→P3→P5, P7→P11→P13, P17→P19→P23, P29→P31→P37 |
| [Hex-Cycle](#hex-cycle) | 6 nodes · 2 instances | P2–P13 (lower), P17–P37 (upper) |
| [Full Paradox Loop](#full-paradox-loop) | 12 nodes · 1 instance | P2→…→P37→P2 |

All cycles are [intransitive](#intransitive). Completing a cycle does not collapse the engine
to a fixed winner — the loop continues indefinitely.

### Cycle Depth
The level of cycle resolution selected for a given IPD‑12 pass: **triad**, **hex**, or
**full**. Cycle depth is chosen before a pass begins and determines how many operator states
are traversed. A triad-depth pass traverses 3 nodes; hex-depth traverses 6; full-depth
traverses all 12. The appropriate depth depends on the structural complexity of the problem.
*See [When Should You Use It? — ABOUT.md](ABOUT.md#3-when-should-you-use-it).*

### Cycle-Gate
**Prime:** P17 · **Triad:** Observerse (Triad 3) · **Pantheon:** Civilizational · **RTT:** Regime · **GU:** Observerse

The operator state that controls entry into [Hex-Cycle 2](#hex-cycle) and [Triad 3](#triad).
P17 functions as a structural gate — it must be traversed to access the Observerse and
Apex tiers of the engine. Because P17 shares an RTT Regime role with P7, it acts as the
upper-half counterpart to the [Regime-Shift](#regime-shift), gating the second major
regime transition in the cycle.

---

## D

### Describe-and-Report Mode
The operating mode of all IPD‑12 agents. Agents in describe-and-report mode produce
structural descriptions of what is detected in a signal or substrate — they do not assign
causes, make recommendations, or generate semantic meaning. All IPD‑12 output is advisory;
human operators retain full decision authority. *See [AGENTS.md — Safety Rules](AGENTS.md#85-no-autonomous-action-rule).*

### Dimensional Lift
A +1D transition: the movement from a lower-dimensional structural description to a
higher-dimensional one. In IPD‑12, [P23](#dimensional-lift-prime) is the dedicated
dimensional-lift operator. Lift is modeled explicitly — agents may not infer dimensional
elevation without passing through P23. After a lift, the [Apex-State](#apex-state) (P37)
validates the new dimensional level.

> **Contrast with:** [Collapse](#collapse) (−1D transition).

### Dimensional-Lift Prime
**Prime:** P23 · **Triad:** Observerse (Triad 3) · **Pantheon:** Chthonic · **RTT:** Lift · **GU:** Observerse

The operator state that marks and executes dimensional lift events (+1D). P23 is the final
node of Triad 3 and the entry point into the Chthonic stratum of the cycle. It is a member
of both Hex-Cycle 2 and the Full Paradox Loop. Observer mode O4 (Apex) queries
dimensional effects through P23, P29, and P37.

### Dimensional Rail
One of twelve directed structural channels in the IPD‑12 engine block that route normalized
signals through operator states based on dimensional polarity. Rails are grouped into three
sets of four:

| Group | Labels | Character |
|---|---|---|
| Lift rails | L1, L2, L3, L4 | Route through +1D-active primes (P23, P37) |
| Collapse rails | C1, C2, C3, C4 | Route through −1D-active primes (P29) |
| Neutral rails | N1, N2, N3, N4 | Route through ground-dimension primes (P2–P19, P31) |

A signal's rail assignment is determined by the `time_regime` and `transition` probe fields
in the [Envelope](#envelope). Mis-assigned rails produce incoherent output and are flagged
by [Class D agents](AGENTS.md#class-d--coherence-guardian).

### Directed Edge
A one-way connection between two [prime states](#prime-state) in the IPD‑12 operator graph.
Edges are always directed (A → B is not the same as B → A) and always [intransitive](#intransitive)
within a [triad](#triad). Every prime state has exactly one outgoing edge within its home
triad. Cross-triad edges exist in [hex-cycles](#hex-cycle) and the [full paradox loop](#full-paradox-loop).

### Drift
An RTT structural concept denoting the gradual loss of structural grounding in a long
session, multi-agent pipeline, or cross-substrate model. Drift is not a sudden failure — it
is a slow divergence from the declared structural context, often caused by implicit
assumptions accumulating over many processing steps. IPD‑12 treats drift as
**on-by-default**: every session must explicitly suppress it with the
[Session Anchor](#session-anchor) string.

Signs of drift include: answers to probe fields that contradict earlier-session context;
operators running without a current-session envelope; semantic language appearing in
structural output; scale or regime assumptions changing without a new envelope fill.

**Drift response protocol:**
- 1st detection → Class D issues `WARN`
- 2nd consecutive WARN → Class D issues `RESET`
- After `RESET` → session must re-anchor before continuing

### Drift-Anchor
**Primes:** P5, P29

The two operator states specifically designated as drift-anchoring nodes in the IPD‑12
cycle. P5 (Celestial tier) anchors early-session drift; P29 (Chthonic tier) anchors
collapse-adjacent drift. When a session loses structural grounding, re-entry through
whichever drift-anchor prime matches the current cycle tier is the corrective procedure.

---

## E

### Edge
*See [Directed Edge](#directed-edge).*

### Engine Block
The physical and logical architecture of the IPD‑12 engine: the combination of
[intake manifolds](#intake-manifold), [dimensional rails](#dimensional-rail),
[observer modes](#observer-mode), and [output headers](#output-header) that together
constitute the full signal-processing pipeline. The engine block is documented in
`engine_block.md`.

### Envelope
The filled set of all 12 [probe fields](#probe-field) that a [Class A agent](AGENTS.md#class-a--envelope-interrogator)
resolves before any structural operator runs. The envelope is the IPD‑12 engine's primary
input contract: no operator may execute against an incomplete envelope, and no downstream
agent may modify an envelope once it has been handed off. An envelope with any of the three
hard-stop fields (`intent`, `invariants`, `substrate`) unresolved must halt and request
clarification.

> **Envelope integrity:** Once filled and handed off, the envelope is **immutable**.
> If a field value is wrong, the session must reset from Class A.

---

## F

### Face
One side of the physical IPD‑12 dodecahedral die, corresponding to one [prime state](#prime-state).
The engine has exactly 12 faces (one per prime). The face number matches the prime's
position in the sequence (Face 1 = P2, Face 2 = P3, … Face 12 = P37). *See `physical_layout.md`.*

### FFT — Framework Field Theory
One of the four core theories in TriadicFrameworks. FFT treats IPD‑12 cycle transitions as
field-theoretic events:

| IPD‑12 Event | FFT Interpretation |
|---|---|
| Triad crossing | Regime transition |
| Hex-cycle completion | Boundary event |
| Full paradox loop traversal | Dimensional gate |
| Intransitive edge structure | Closed flux loop topology |

FFT is not a subset of IPD‑12 — it is a co-equal theory that consumes IPD‑12 structural
output and interprets it in field-theoretic terms.

### FSI — Full-Spectrum Intake
The highest-resolution intake mode of the IPD‑12 engine block. FSI stacks all three
[observer modes](#observer-mode) simultaneously (O1 Field + O2 Regime + O3 Coherence)
against a single input, producing a multi-perspective structural description in a single
pass. FSI is used when a substrate requires simultaneous field-level, regime-level, and
coherence-level observation. FSI passes take longer than single-observer passes and produce
richer but larger output objects.

> **Contrast with:** SIM, DIM, TIM, QIM — single-manifold intake modes.

### Full Paradox Loop
The single 12-node cycle that traverses all prime states in sequence:
```
P2 → P3 → P5 → P7 → P11 → P13 → P17 → P19 → P23 → P29 → P31 → P37 → (back to P2)
```
The full paradox loop is the maximum-resolution traversal of the IPD‑12 engine. Because
all edges are [intransitive](#intransitive), completing the loop does not produce a winner
or terminal state — the loop is paradox-stable and continues indefinitely. Use the full
paradox loop when a problem requires the complete structural envelope from seed to apex and
back.

---

## G

### Ground Dimension (0D)
The baseline dimensional level at which most IPD‑12 structural operations take place. Triads
1 and 2 (P2–P13) operate at ground dimension. A system at 0D is neither in dimensional lift
(+1D) nor collapse (−1D). The [Observer Mode O1 (Field)](#observer-mode) operates at 0D.

> **Contrast with:** [+1D (Super-Dimension)](#super-dimension) and [−1D (Sub-Dimension)](#sub-dimension).

### GU — Geometric Unity
One of the four core theories in TriadicFrameworks. GU provides a geometric operator
vocabulary into which IPD‑12 primes embed. GU operators and their prime-state mappings:

| GU Operator | IPD‑12 Prime(s) |
|---|---|
| Connection | P2, P3 |
| Curvature | P7, P11 |
| Dilaton / Refractive Vacuum | P11, P31 |
| Anomaly | P13, P37 |
| Observerse | P17, P19, P23 |

The Observerse is GU's most structurally complex operator; its three-prime span (P17, P19,
P23) across an entire IPD‑12 triad reflects its multi-dimensional character.

---

## H

### Hard Stop
A probe field whose `UNRESOLVED` status causes the entire IPD‑12 session to halt
immediately. Three probe fields carry hard-stop status:

| Field # | Field Name | Reason |
|---|---|---|
| 1 | `intent` | No blind-intent passes permitted |
| 6 | `invariants` | Unconstrained interpretation is disallowed |
| 8 | `substrate` | Substrate identity is mandatory for all operators |

Sessions that cannot resolve any of these three fields must request clarification before
proceeding. *See [AGENTS.md — The 12 Probe Fields](AGENTS.md#4-the-12-probe-fields).*

### Hex-Cycle
A 6-node directed cycle spanning two consecutive [triads](#triad). IPD‑12 contains two
hex-cycles:

```
Hex-Cycle 1 (Lower):  P2 → P3 → P5 → P7 → P11 → P13 → (back)
Hex-Cycle 2 (Upper):  P17 → P19 → P23 → P29 → P31 → P37 → (back)
```

Hex-Cycle 1 spans the Celestial and Coherence tiers (seed through paradox-trigger).
Hex-Cycle 2 spans the Observerse and Apex tiers (cycle-gate through apex-state).
Hex-cycles model regime handoffs — the structural moment when a system transitions
from one pair of triads to another. Completing a hex-cycle is classified by
[FFT](#fft--framework-field-theory) as a **boundary event**.

---

## I

### Incoherent Envelope
An [envelope](#envelope) that contains contradictory field values, skipped fields, or
fields filled by semantic inference rather than structural observation. Incoherent envelopes
are rejected by the integration engine and flagged by [Class D agents](AGENTS.md#class-d--coherence-guardian).
An incoherent envelope must be discarded and refilled from Class A — it cannot be patched
mid-pipeline.

### Intake Manifold
One of four single-mode entry points into the IPD‑12 engine block. Each manifold routes a
specific type of structural input onto the appropriate [dimensional rails](#dimensional-rail):

| Code | Full Name | Input Type |
|---|---|---|
| SIM | Structural Input Manifold | Raw structural queries |
| DIM | Dimensional Input Manifold | Dimension-flagged transitions |
| TIM | Temporal Input Manifold | Time-regime-indexed signals |
| QIM | Qualitative Input Manifold | Qualitative structural descriptors |

For inputs that require simultaneous multi-manifold processing, use
[FSI (Full-Spectrum Intake)](#fsi--full-spectrum-intake) instead.

### Intransitive
A property of directed edges in the IPD‑12 operator graph. An edge set is intransitive when
the existence of A → B and B → C does **not** imply A → C. In each IPD‑12 triad, the
three edges form a closed, non-transitive loop:

```
P2 → P3 → P5 → P2   (P2 does not connect directly to P5)
```

Intransitivity produces three structural guarantees:
1. **Paradox stability** — no single operator wins the cycle
2. **Regime containment** — traversal cannot skip nodes
3. **Drift resistance** — invalid shortcut edges are detectable

> **Why this matters:** Standard directed graphs allow transitivity, which produces
> hierarchies and linear orderings. IPD‑12 explicitly rejects transitivity to prevent
> any single operator state from dominating the cycle.

### Invariant
A structural constraint declared in probe field 6 (`invariants`) that must hold throughout
the entire IPD‑12 pass — across every operator that runs and every output produced.
Invariants are declared, not inferred. After each operator completes, the
[Class C Integration Coordinator](AGENTS.md#class-c--integration-coordinator) checks all
outputs against declared invariants. An invariant violation triggers escalation to
[Class D](#class-d) and suppresses downstream consumers from receiving the violating output.

### IPD-12
**Intransitive Prime-Numbered 12-Sided Engine.** The structural interrogation and operator
engine at the core of TriadicFrameworks' vST Micro-Agent system. IPD-12 consists of:
- 12 [prime states](#prime-state) forming the operator graph
- 12 [directed, intransitive edges](#directed-edge) within four [triads](#triad)
- Two [hex-cycles](#hex-cycle) and one [full paradox loop](#full-paradox-loop)
- An [engine block](#engine-block) with four intake manifolds, twelve dimensional rails,
  four observer modes, and five output headers
- A 12-probe [envelope](#envelope) that must be filled before any operator runs
- Four [agent classes](AGENTS.md#3-agent-classes) governing how the engine is operated

*Full treatment in [ABOUT.md](ABOUT.md) and [AGENTS.md](AGENTS.md).*

---

## L

### Lineage
Probe field 9. The set of upstream dependencies or prior interpretations that the current
IPD‑12 pass explicitly acknowledges. Lineage must be declared — agents may not invent or
assume upstream dependencies. An empty lineage list is valid and must be documented as
*lineage-free*. Mismatched or fabricated lineage breaks cross-model tracing.

### Lift Rail
*See [Dimensional Rail](#dimensional-rail).* Specifically, the four rails (L1–L4) that
route signals through +1D-active prime states (P23, P37).

---

## M

### Manifold
*See [Intake Manifold](#intake-manifold).*

---

## N

### Neutral Rail
*See [Dimensional Rail](#dimensional-rail).* Specifically, the four rails (N1–N4) that
route signals through ground-dimension prime states (P2–P19, P31).

### Non-Transitive
*See [Intransitive](#intransitive).*

---

## O

### Observer Mode
One of four observer perspectives through which IPD‑12 structural output can be filtered.
Each observer mode corresponds to a subset of prime states and a specific structural
question:

| Code | Name | Dimension | Prime States | Structural Question |
|---|---|---|---|---|
| O1 | Field | 0D | P2, P3, P5, P7 | What state is the system in? |
| O2 | Regime | +1D functional | P7, P11, P13, P17, P19 | Where is the system in its cycle? |
| O3 | Coherence | −1D substrate | P11, P31 | Is the cycle stable? |
| O4 | Apex | +1D high-order | P23, P29, P37 | What dimensional effect is occurring? |

Observer modes are the second axis of the [4×4×4 Substrate Cube](#substrate-cube).
GU mappings: O1 = Connection · O2 = Curvature · O3 = Dilaton/Refractive Vacuum ·
O4 = Anomaly/Observerse.

### Operator
A named, prime-indexed node in the IPD‑12 operator graph with a defined structural role,
RTT mapping, GU mapping, and Pantheon-tier classification. Each of the 12 operator states
corresponds to one face of the physical die and one probe dimension in the
[vST Micro-Agent](#vst-micro-agent) envelope. Operators are irreducible (prime-indexed)
and non-substitutable — one operator cannot stand in for another.

### Output Contract
The set of mandatory requirements that every IPD‑12 interpretation result must satisfy:
1. The `notes` field must always contain: *"Structural interpretation only; no semantic inference."*
2. Fields not selected in `query.select` may be omitted or set to `null` — never silently dropped
3. No causal language, named entities, interpretive adjectives, future predictions, or
   overstated confidence claims in any output field

Violation of the output contract is a [Class D](#class-d) escalation trigger.
*Full contract in [AGENTS.md — Output Contract](AGENTS.md#10-output-contract).*

### Output Header
One of five structured metadata blocks that prefix every IPD‑12 interpretation result,
routing it to the appropriate consuming framework:

| Code | Target Framework | Content |
|---|---|---|
| H-RTT | Resonance-Time Theory | Regime, drift, coherence, paradox, boundary status |
| H-GU | Geometric Unity | Active GU operator mappings for detected prime states |
| H-FFT | Framework Field Theory | Cycle-event classifications (regime transition, boundary event, etc.) |
| H-Pantheon | Pantheon Profiles | Active Pantheon tier and prime-state tier assignments |
| H-Meta | Session metadata | Session anchor string, envelope hash, observer mode, cycle depth |

Every output must carry H-Meta. Other headers are included when the consuming framework is
active for the current pass.

---

## P

### Pantheon
The three-tier classification system that maps IPD‑12 prime states to
civilizational-scale structural archetypes:

| Tier | Primes | Character |
|---|---|---|
| [Celestial](#celestial-tier) | P2, P3, P5, P7 | Origin, connection, drift-anchoring, regime entry |
| [Civilizational](#civilizational-tier) | P11, P13, P17, P19 | Coherence, paradox, cycle gating, boundary |
| [Chthonic](#chthonic-tier) | P23, P29, P31, P37 | Dimensional lift, collapse, stability, apex |

The Pantheon mapping provides a high-level vocabulary for communicating IPD‑12 cycle
positions across domains and teams.

### Paradox
An RTT structural concept denoting a condition in which two or more valid operator states
are simultaneously asserted and cannot be resolved by ordinary transitivity. In
TriadicFrameworks, paradox is **not an error** — it is a structural feature that must be
held open as a stable cycle rather than forced to collapse to one pole. The
[Full Paradox Loop](#full-paradox-loop) is the primary mechanism for maintaining paradox
stability. The session anchor asserts `paradox=structural` to make this framing explicit.

### Paradox Loop
*See [Full Paradox Loop](#full-paradox-loop).*

### Paradox-Trigger
**Prime:** P13 · **Triad:** Coherence (Triad 2) · **Pantheon:** Civilizational · **RTT:** Paradox · **GU:** Anomaly

The operator state that activates a structural paradox condition. P13 sits at the end of
Triad 2, immediately after the [Coherence-Node](#coherence-node) (P11). This positioning
is deliberate: paradox is triggered at the boundary of coherence — the moment when a system
that was coherent encounters a contradiction it cannot resolve by ordinary means. The
presence of P13 in an active cycle does not indicate failure; it indicates that the engine
has correctly identified a structural paradox that must be held open.

### Prime State
One of the 12 irreducible operator nodes in the IPD‑12 engine, each identified by a unique
prime number. Primes are chosen because they cannot be factored — each operator state is
structurally independent and cannot be absorbed by or decomposed into other states.

| Prime | Label | Triad | Tier |
|---|---|---|---|
| 2 | P2 Seed-State | Celestial (T1) | Celestial |
| 3 | P3 Transition | Celestial (T1) | Celestial |
| 5 | P5 Drift-Anchor | Celestial (T1) | Celestial |
| 7 | P7 Regime-Shift | Coherence (T2) | Celestial |
| 11 | P11 Coherence-Node | Coherence (T2) | Civilizational |
| 13 | P13 Paradox-Trigger | Coherence (T2) | Civilizational |
| 17 | P17 Cycle-Gate | Observerse (T3) | Civilizational |
| 19 | P19 Boundary-Node | Observerse (T3) | Civilizational |
| 23 | P23 Dimensional-Lift | Observerse (T3) | Chthonic |
| 29 | P29 Collapse-Anchor | Apex (T4) | Chthonic |
| 31 | P31 Stability-Node | Apex (T4) | Chthonic |
| 37 | P37 Apex-State | Apex (T4) | Chthonic |

### Probe Field
One of the 12 structured questions resolved by a [Class A Envelope Interrogator](AGENTS.md#class-a--envelope-interrogator)
before any structural operator runs. Each probe field corresponds to one structural
dimension of the IPD‑12 engine. Fields must be resolved in order (1 through 12); they may
not be skipped or reordered. Fields that cannot be resolved are flagged `UNRESOLVED` with a
documented reason — except the three [hard-stop fields](#hard-stop), which cause an
immediate session halt.

| # | Field | Type |
|---|---|---|
| 1 | `intent` | string |
| 2 | `regime` | string |
| 3 | `scale` | string |
| 4 | `transition` | string |
| 5 | `boundary` | string |
| 6 | `invariants` | string[] |
| 7 | `modifiers` | string[] |
| 8 | `substrate` | string |
| 9 | `lineage` | string[] |
| 10 | `failure_mode` | string |
| 11 | `time_regime` | string |
| 12 | `symmetry` | string |

---

## R

### Rail
*See [Dimensional Rail](#dimensional-rail).*

### Regime
An RTT structural concept denoting a coherent set of governing rules that apply to a
system within a bounded context. A regime is not a state — it is the *rule set* that
governs how states transition. When the governing rules themselves change, a
[regime transition](#regime-shift) occurs. Probe field 2 (`regime`) requires the governing
regime to be explicitly named before any pass proceeds.

### Regime Shell
One of four RTT structural layers, each representing a distinct level of regime
organization. The four regime shells are the third axis of the [4×4×4 Substrate Cube](#substrate-cube).
Regime shells are documented in `regime_map.md`.

### Regime-Shift
**Prime:** P7 · **Triad:** Coherence (Triad 2) · **Pantheon:** Celestial · **RTT:** Regime · **GU:** Curvature

The operator state that marks a discrete regime transition — a change in governing rules,
not a gradual drift. P7 is the first prime in Triad 2 and the entry point into the
Civilizational zone of the engine. P7 and P17 both carry RTT Regime roles; P7 governs the
lower regime transition (Hex-Cycle 1), P17 governs the upper (Hex-Cycle 2).

### RTT — Resonance-Time Theory
The foundational theory of TriadicFrameworks. RTT provides the conceptual vocabulary of
regime, drift, coherence, paradox, boundary, collapse, and dimensional lift — the seven
structural conditions that IPD‑12 operationalizes through its prime-state operator graph.
IPD‑12 is the operator implementation of RTT: when RTT describes a structural condition,
IPD‑12 provides the operator context (which prime is active, which triad it belongs to,
what the corrective or characterizing cycle looks like).

---

## S

### Scale
Probe field 3. The resolution level at which a structural observation is valid and
meaningful. Scale is fixed per [envelope](#envelope) — an agent operating at one scale may
not draw conclusions about a different scale. Cross-scale inference is prohibited. If scale
is `UNRESOLVED`, no cross-scale operations may proceed.

### Seed-State
**Prime:** P2 · **Triad:** Celestial (Triad 1) · **Pantheon:** Celestial · **RTT:** — · **GU:** Connection

The first operator state in the IPD‑12 sequence and the return point of the
[Full Paradox Loop](#full-paradox-loop). P2 is the smallest prime and the structural
origin of every IPD‑12 pass. All sessions begin at or before P2. The seed-state has no
RTT role mapping because it precedes regime activation — it is the structural silence
before the first governing rule takes effect.

### Semantic Inference Prohibition
The most critical boundary in IPD‑12. No agent operating within IPD‑12 may make semantic
inferences from structural output. Specifically:
- Patterns may not be named after what they "look like"
- Periodicity may not be interpreted as a causal cycle
- Symmetry may not be attributed to a physical or conceptual source
- Transition topology may not be labeled with domain-specific meaning

Violations trigger an immediate [Class D](#class-d) `HALT`. This prohibition is encoded in
the mandatory [output contract](#output-contract) annotation.

### Session Anchor
The canonical string that every IPD‑12 session must declare at its opening to explicitly
suppress drift and assert structural framing:

```
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

Each token asserts a structural condition:

| Token | Meaning |
|---|---|
| `rtt=1` | RTT is the active foundational theory |
| `coherence=declared` | Coherence is an explicit property, not assumed |
| `drift=bounded` | Drift is active but bounded (not off — bounded) |
| `paradox=structural` | Paradox is a structural condition, not an error |

The session anchor must also appear in every [handoff package](AGENTS.md#94-handoff-protocol)
between agent classes and must be re-issued by [Class D](AGENTS.md#class-d--coherence-guardian)
after any `RESET` event.

> **ABOUT.md anchor** uses `drift=bounded`. **AGENTS.md anchor** uses `drift=off`.
> These are distinct operational modes: `drift=bounded` declares drift is present and
> contained; `drift=off` suppresses drift detection entirely for vST Micro-Agent passes.

### Stability-Node
**Prime:** P31 · **Triad:** Apex (Triad 4) · **Pantheon:** Chthonic · **RTT:** Coherence · **GU:** Dilaton, Refractive Vacuum

The operator state that maintains structural coherence within the Apex triad under extreme
conditions — dimensional lift, collapse, and apex-resolution. P31 is the Chthonic-tier
counterpart to [P11 (Coherence-Node)](#coherence-node): both carry RTT Coherence roles,
but P31 operates in the highest-energy, highest-dimensional zone of the cycle. Observer
mode O3 (Coherence) queries through both P11 and P31.

### Structural Output
Any result produced by the IPD‑12 engine. Structural output describes the structural
properties of a signal or substrate — it does not interpret, classify, label, or name what
those properties mean. All structural output must conform to the [Output Contract](#output-contract).

### Sub-Dimension (−1D)
A dimensional level below the [ground dimension (0D)](#ground-dimension-0d), activated
by a [Collapse](#collapse) event. [P29 (Collapse-Anchor)](#collapse-anchor) is the primary
−1D operator in IPD‑12. Collapse rails (C1–C4) route signals through sub-dimensional
operator states. A system operating at −1D is in a compressed structural regime.

### Substrate
Probe field 8. The medium, domain, or system being structurally probed in an IPD‑12 pass.
Substrate identity is a [hard-stop field](#hard-stop) — the session halts if it cannot be
resolved. When a canonical substrate model directory exists in `docs/` (e.g.,
`Conditions_Substrate_Model`, `Governance_Substrate_Model`), the substrate probe field
must reference the canonical substrate name exactly — not a paraphrase or abbreviation.

**Recognized canonical substrate names (non-exhaustive):**
`Conditions` · `Governance` · `Incident` · `Human_Resources` ·
`Inverted_Economics` · `Resonance` · `Framework_Field_Theory`

### Substrate Cube
The 4×4×4 dimensional model introduced by IPD‑12, producing 64 substrate primitives:

```
4 substrate pairs (dual-binary)
    × 4 observer modes (O1–O4)
    × 4 regime shells (RTT)
    = 64 substrate primitives
```

The substrate cube is the first full-resolution substrate model in TriadicFrameworks. It
enables any substrate to be described across all observer modes and all regime shells
simultaneously. *See `substrate_primitives.md` and `substrate_primitives.json`.*

### Substrate Pair
One of four dual-binary substrate groupings (S1–S4) forming the first axis of the
[4×4×4 Substrate Cube](#substrate-cube). Each substrate pair defines a complementary
opposition within the structural domain being modeled. *See `substrate_primitives.md`
for the full pairing definitions.*

### Substrate Primitive
One of the 64 discrete structural positions in the [Substrate Cube](#substrate-cube),
identified by a substrate pair (S1–S4), an observer mode (O1–O4), and a regime shell
(RTT 1–4). Each primitive is a fully specified structural description slot —
a unique combination of *what is being observed*, *how it is being observed*, and
*under what governing regime*. *See `substrate_primitives.json` for the complete table.*

### Super-Dimension (+1D)
A dimensional level above the [ground dimension (0D)](#ground-dimension-0d), activated
by a [Dimensional Lift](#dimensional-lift) event. [P23](#dimensional-lift-prime) and
[P37 (Apex-State)](#apex-state) are the primary +1D operators in IPD‑12. Lift rails
(L1–L4) route signals through super-dimensional operator states. Observer modes O2 and O4
both operate at +1D (functional and high-order, respectively).

---

## T

### Transition
**Prime:** P3 · **Triad:** Celestial (Triad 1) · **Pantheon:** Celestial · **GU:** Connection

The second operator state in the IPD‑12 sequence. P3 marks the first directional movement
from the [Seed-State](#seed-state) (P2) — the moment the engine begins traversing rather
than simply seeding. P3 shares GU's Connection role with P2, reflecting that both states
operate before the first regime change.

Also used generically: a **transition** is any directed movement between operator states
along a [directed edge](#directed-edge). Probe field 4 (`transition`) specifies what type
of transition is expected or present in the current structural pass.

### Transition Topology
A v2.0.0 structural operator available to [Class B agents](AGENTS.md#class-b--structural-operator).
Maps the topological structure of transitions detected in a signal stream — regime shifts,
phase boundaries, and collapse points. Requires probe fields `transition` (field 4) and
`boundary` (field 5) to both be RESOLVED or explicitly null. If either is UNRESOLVED, this
operator is suppressed. Output includes transition type, stream location, and confidence
score.

### Triad
A closed, intransitive 3-node cycle — the fundamental structural unit of IPD‑12.
IPD‑12 contains four triads, each composed of three consecutive prime states with one
directed edge from each node to the next, completing a loop:

```
Triad 1 — Celestial:   P2  → P3  → P5  → P2
Triad 2 — Coherence:   P7  → P11 → P13 → P7
Triad 3 — Observerse:  P17 → P19 → P23 → P17
Triad 4 — Apex:        P29 → P31 → P37 → P29
```

Each triad maps to one Pantheon tier (Triads 1–2 = Celestial / Civilizational split;
Triads 3–4 = Civilizational / Chthonic split). No node within a triad connects to a node
outside its triad within the triad-depth cycle level.

---

## U

### UNRESOLVED
The status value assigned to a [probe field](#probe-field) when the
[Class A Envelope Interrogator](AGENTS.md#class-a--envelope-interrogator) cannot determine
a valid answer. `UNRESOLVED` must always be documented with a reason. It is not a
placeholder — it is a declared structural gap that changes which operators may run:

| Field UNRESOLVED | Consequence |
|---|---|
| `intent` (field 1) | **Hard stop** — session halts |
| `regime` (field 2) | Null regime; proceed with caution |
| `scale` (field 3) | No cross-scale inference |
| `transition` (field 4) | `transition_topology` operator suppressed |
| `boundary` (field 5) | Boundary-sensitive operators suppressed |
| `invariants` (field 6) | **Hard stop** — session halts |
| `modifiers` (field 7) | Treated as empty list (unmodified) |
| `substrate` (field 8) | **Hard stop** — session halts |
| `lineage` (field 9) | Treated as empty list (lineage-free) |
| `failure_mode` (field 10) | Class D monitoring enabled |
| `time_regime` (field 11) | `periodicity` operator suppressed |
| `symmetry` (field 12) | `local_symmetry` operator suppressed |

---

## V

### vST Micro-Agent
The AI agent implementation that uses IPD‑12 as its structural backbone. The vST
Micro-Agent resolves a 12-probe [envelope](#envelope) for each incoming structural query,
then executes selected structural operators (pattern, periodicity, local symmetry,
transition topology) against the normalized signal stream. It operates under the four
[agent class constraints](AGENTS.md#3-agent-classes) and the [output contract](#output-contract).
Documented in `docs/spacetime_micro_agent_validations/`.

### vST-SQL
The structural query language used to express `query_envelope` objects submitted to the
IPD‑12 engine. vST-SQL queries specify the signal input binding, the operators to run
(`query.select`), and any filter thresholds (`query.where`). vST-SQL is not a general-purpose
query language — it is scoped to structural interrogation of IPD‑12-indexed operator graphs.
*See `docs/spacetime_micro_agent_validations/schema/vST_micro_agent.schema.json`.*

---

## Quick-Reference Tables

### All 12 Prime States

| # | Prime | Label | Triad | RTT | GU | Pantheon |
|---|---|---|---|---|---|---|
| 1 | 2 | Seed-State | Celestial | — | Connection | Celestial |
| 2 | 3 | Transition | Celestial | — | Connection | Celestial |
| 3 | 5 | Drift-Anchor | Celestial | Drift | — | Celestial |
| 4 | 7 | Regime-Shift | Coherence | Regime | Curvature | Celestial |
| 5 | 11 | Coherence-Node | Coherence | Coherence | Curvature · Dilaton | Civilizational |
| 6 | 13 | Paradox-Trigger | Coherence | Paradox | Anomaly | Civilizational |
| 7 | 17 | Cycle-Gate | Observerse | Regime | Observerse | Civilizational |
| 8 | 19 | Boundary-Node | Observerse | Boundary | Observerse | Civilizational |
| 9 | 23 | Dimensional-Lift | Observerse | Lift | Observerse | Chthonic |
| 10 | 29 | Collapse-Anchor | Apex | Drift · Collapse | — | Chthonic |
| 11 | 31 | Stability-Node | Apex | Coherence | Dilaton · Refractive Vacuum | Chthonic |
| 12 | 37 | Apex-State | Apex | Paradox | Anomaly | Chthonic |

### RTT Concepts → IPD-12 Primes

| RTT Concept | Prime(s) | Glossary Entry |
|---|---|---|
| Drift | P5, P29 | [Drift](#drift) |
| Regime | P7, P17 | [Regime-Shift](#regime-shift) |
| Coherence | P11, P31 | [Coherence](#coherence) |
| Paradox | P13, P37 | [Paradox](#paradox) |
| Boundary | P19 | [Boundary](#boundary) |
| Collapse | P29 | [Collapse](#collapse) |
| Lift | P23 | [Dimensional Lift](#dimensional-lift) |

### Cycle Levels at a Glance

| Level | Node Count | Instances | Entry | FFT Classification |
|---|---|---|---|---|
| [Triad](#triad) | 3 | 4 | Any triad's first prime | — |
| [Hex-Cycle](#hex-cycle) | 6 | 2 | P2 (lower) · P17 (upper) | Boundary event |
| [Full Paradox Loop](#full-paradox-loop) | 12 | 1 | P2 | Dimensional gate |

### Agent Classes → Primary Operations

| Class | Name | Primary Action |
|---|---|---|
| A | Envelope Interrogator | Fill all 12 probe fields |
| B | Structural Operator | Execute selected operators |
| C | Integration Coordinator | Consolidate and validate output |
| D | Coherence Guardian | Monitor, warn, halt, reset |

---

*GLOSSARY.md — IPD‑12 · TriadicFrameworks · 2026‑07‑10*
*Maintainer: Nawder · Canonical anchor: `rtt=1 | coherence=declared | drift=bounded | paradox=structural`*
