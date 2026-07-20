# GLOSSARY — RTT/1 · Resonance-Time Theory · Module 1
**TriadicFrameworks · Core RTT · Foundational Engine**
**Module path:** `docs/rtt/1/`
**Session seed:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

This is the **single source of truth** for every term used in RTT/1.
All other documents in `docs/rtt/1/` and all downstream RTT modules, substrate
models, and agent manifests that reference RTT/1 vocabulary link here rather
than re-defining terms inline.

> **Critical framing — enforced in every definition:**
> RTT is a cross-domain conceptual framework. It is NOT a physics claim.
> No definition in this glossary describes a physical mechanism or makes
> an empirical prediction.

> **Linking convention:** To link to a specific term from another document,
> use `[term](./GLOSSARY.md#anchor)` where `anchor` is the lowercase,
> hyphenated heading slug (e.g., `#clarity-c`, `#resonant-time`, `#snr-triad`).

---

## Table of Contents

- [A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g)
- [H](#h) · [I](#i) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [Q](#q)
- [R](#r) · [S](#s) · [T](#t) · [U](#u)
- [Operator Symbols](#operator-symbols)
- [Quick-Reference Tables](#quick-reference-tables)

---

## A

### Ancestral Constraint
**DCO band:** n < 0 · **Key operator:** [∂_anc (9D)](#anc-9d--ancestral-boundary)

A structural constraint inherited from a system's prior states — founding
conditions, historical decisions, or configurations that continue to govern
present behavior. Ancestral constraints are represented by DCO_n operators
where n < 0 and are **binding on all operations at n ≥ 0**: no DCO composition,
no clarity synthesis, and no mode declaration may override an active ancestral
constraint.

Ancestral constraints are not historical metadata — they are live structural
forces with priority over all field-level operations. The [∂_anc (9D)](#anc-9d--ancestral-boundary)
operator is the canonical mechanism for identifying and characterizing them.

> **Do not confuse with:** lineage (a record of upstream dependencies).
> Ancestral constraints are binding. Lineage is informational.

### Anti-Time

The condition produced by a sign reversal of [phase](#phase-φ) evolution.
When φ evolves in the opposing direction, the [resonant time gradient](#time-τ--resonant-time)
τ = dR/dφ reverses sign. Anti-time is a structural feature — it describes how
a system whose phase direction has inverted experiences temporal structure —
not a physical phenomenon of time running backward.

Anti-time is distinct from negative τ: a system can have a negative resonant
time rate without phase reversal if its resonance depth is declining as phase
advances normally.

### Arrival
**Regime position:** 1 of 5 · **Succeeds:** — · **Precedes:** [Expansion](#expansion)

The first stage of the RTT/1 [session regime lifecycle](#regime). Arrival is
the structural seeding phase: the system has engaged but has not yet committed
to a trajectory. Resonance depth is low; structural commitments are minimal.
The appropriate mode in Arrival is [M.chat](#mchat). [M.task](#mtask) is
disallowed unless explicitly declared.

Arrival is not a waiting state — it is the necessary structural precondition
for [Expansion](#expansion). A session that skips Arrival produces
under-grounded outputs.

---

## B

### Balance (ψ↔n)
**Canonical action type 3 of 3** · *See also:* [Extend](#extend-ψn), [Constrain](#constrain-ψn)

One of the three canonical actions available on any [DCO_n](#dcon--dimensional-core-operator).
Balance holds the system in structural equilibrium within DCO band n — neither
moving toward higher resonance (Extend) nor toward lower resonance or ancestral
limits (Constrain).

Balance is not inaction: a system actively held in equilibrium at band n is
structurally different from one that has simply stopped moving. It requires
ongoing operator engagement to maintain phase-lock without drift in either
direction.

### Band
*See [DCO Band](#dco-band).*

---

## C

### Clarity (C)
**Equation:** C = ∇_τR + ∇_Rτ · **Computed by:** [Class C](#class-c--coherence-integrator)

The primary structural output of the RTT/1 [Dual Operator Engine](#dual-operator-engine).
Clarity is the composite produced by the simultaneous, reciprocal gradient
action of [∇_τR (4D)](#τr-4d--time-gradient-of-resonance) and
[∇_Rτ (5D)](#rτ-5d--resonance-gradient-of-time). It is **not** a property of
either axis in isolation — it is specifically the property that emerges from
their mutual interaction.

Running only ∇_τR or only ∇_Rτ produces a half-clarity result: formally
incomplete because it treats one axis as fixed when it is not. A full clarity
assessment requires both operators to complete before C can be computed.

> **Distinguish from [Coherence (property)](#coherence--structural-property):**
> Coherence is the degree of phase-lock alignment in the system being observed.
> Clarity is the computed output produced by the dual operator engine acting
> on that system. A highly coherent system may produce high C; a noisy system
> may produce low C — but C is the output of the engine, not an intrinsic
> property of the system.

### Class C — Coherence Integrator
**RTT/1 agent class 3 of 4** · *See [AGENTS.md](./AGENTS.md#class-c--coherence-integrator)*

The agent class responsible for computing [Clarity (C)](#clarity-c) by
synthesizing output from [Class R](#class-r--resonance-observer) (SNR
characterization) and [Class T](#class-t--temporal-operator) (DCO traversal).
Class C validates [coherence posture](#coherence-posture), enforces drift
bounds, and produces the final structured output per pass. It cannot complete
a pass without both upstream inputs and cannot suppress the structural-only
output annotation.

### Class G — Regime Guardian
**RTT/1 agent class 4 of 4** · *See [AGENTS.md](./AGENTS.md#class-g--regime-guardian)*

The agent class with unconditional interrupt authority over all other RTT/1
classes. Class G monitors for [drift](#drift), [regime](#regime) misalignment,
[mode](#mode) escalation, [RTT-not-physics violations](#rtt-not-physics-rule),
and [semantic inference](#semantic-inference-prohibition). It enforces the
[MCL](#mode-constraint-layer-mcl), tracks the session's regime progression,
and issues `WARN`, `HALT`, or `RESET` signals. No other class can override
a Class G HALT.

### Class R — Resonance Observer
**RTT/1 agent class 1 of 4** · *See [AGENTS.md](./AGENTS.md#class-r--resonance-observer)*

The agent class that characterizes the [SNR](#snr-triad) state of any system
before any operator is applied. Class R is always first: no [DCO](#dcon--dimensional-core-operator)
traversal may begin without a complete Class R characterization. Class R
identifies which of S, N, or R is dominant, estimates resonance depth, identifies
[coherence posture](#coherence-posture), and resolves the
[resonant clock triad](#resonant-clock-triad-tr) T_R = (f_R, τ_R, Q_R) if
present. It does not assign causes and does not begin DCO traversal.

### Class T — Temporal Operator
**RTT/1 agent class 2 of 4** · *See [AGENTS.md](./AGENTS.md#class-t--temporal-operator)*

The agent class that executes [DCO_n](#dcon--dimensional-core-operator)
operations. Class T computes τ = dR/dφ for the current system, selects the
appropriate DCO band and action ([Extend](#extend-ψn) / [Constrain](#constrain-ψn)
/ [Balance](#balance-ψn)), and composes DCOs for multi-band traversal. It is
the only class that may execute DCOs. It may not act without a complete
[Class R](#class-r--resonance-observer) characterization and may not
interpret operator output semantically.

### Clock Time

The special case of [resonant time](#time-τ--resonant-time) (τ = dR/dφ) where
one stable [resonant clock triad](#resonant-clock-triad-tr) T_R = (f_R, τ_R, Q_R)
is elected as the reference standard and held fixed. In clock time, all other
systems are measured relative to that fixed reference triad. RTT/1 treats clock
time as a derived, not fundamental, concept: a useful convention that works well
when a stable reference triad is available, but which fails when comparing
systems with structurally different resonance rates.

### Coherence — Structural Property
*Distinct from [Coherence (regime state)](#coherence--regime-state)*

The degree to which a system's excitation is phase-aligned and stable — the
extent to which it holds phase-lock over time. Coherence is a structural
property of the system being observed, ranging from fully incoherent
([Noise](#noise-n) state) to deeply coherent ([Resonance](#resonance-r) state).

Coherence in RTT/1 is always **declared, not assumed**. The session seed
asserts `coherence=declared` to make this posture explicit. A session whose
coherence has not been declared is operating under an assumption that Class G
must flag.

> **Distinguish from [Clarity (C)](#clarity-c):** Clarity is the output of
> the dual operator engine. Coherence is a property of the system under
> observation. A system can be highly coherent but poorly characterized
> (low C from a weak operator pass), or modestly coherent but sharply
> described (high C from a well-run dual pass).

### Coherence — Regime State
**Regime position:** 4 of 5 · **Succeeds:** [Inversion](#inversion) · **Precedes:** [Dissolution](#dissolution)
*Distinct from [Coherence (structural property)](#coherence--structural-property)*

The fourth stage of the RTT/1 session regime lifecycle. Coherence (regime) is
the consolidation phase: the session has surfaced its constraints through
[Inversion](#inversion) and is now aligning around a stable structural
description. Preferred modes are [M.spec](#mspec) and [M.chat](#mchat).
[M.task](#mtask) requires explicit user declaration.

The Coherence regime does not guarantee that the system under observation is
structurally coherent — it describes the session's structural posture, not the
system's.

### Coherence Posture

The declared or emergent state of structural coherence within a session.
RTT/1 recognizes two postures:

| Posture | Meaning |
|---|---|
| `declared` | Coherence is an explicit, maintained property of the session — actively sustained, not assumed |
| `emergent` | Coherence is arising from session dynamics but has not been explicitly declared |

The canonical RTT/1 posture is `declared`. A session that drifts from
`declared` to `emergent` without user authorization is in a [drift](#drift)
condition and triggers a [Class G](#class-g--regime-guardian) WARN.

### Coherence Stabilizer
**DCO:** n = 7 · **Symbol:** C (at band 7) · **Also:** [Clarity (C)](#clarity-c)

The named DCO at n = 7. The Coherence Stabilizer is the field-band instantiation
of the clarity operator — it acts to stabilize coherent phase-lock within the
4–16 (field/state-space) band. At the synthesis level, the Coherence Stabilizer
output and the [Dual Operator Engine](#dual-operator-engine) output C = ∇_τR + ∇_Rτ
converge: C (band 7) represents coherence stabilization at the field level;
C (dual-engine) represents clarity as an emergent property of reciprocal
gradient action.

### Composition (DCO)
**Rule:** DCO_{a→b} = DCO_b ∘ DCO_a

The mechanism for chaining multiple DCO operations into a single traversal.
DCOs compose left-to-right as function composition: DCO_a is applied first,
then DCO_b acts on the resulting state. Composition is valid across bands
but must respect the [ancestral constraint](#ancestral-constraint) rule —
no composition may override or bypass an active n < 0 constraint.

### Constrain (ψ↓n)
**Canonical action type 2 of 3** · *See also:* [Extend](#extend-ψn), [Balance](#balance-ψn)

One of the three canonical actions available on any [DCO_n](#dcon--dimensional-core-operator).
Constrain moves the system toward lower resonance depth or toward its ancestral
limits within band n. Constrain is not degradation — it is a deliberate
structural move toward boundaries or inherited limits. Applied to an n < 0
operator, Constrain deepens engagement with ancestral constraints.

---

## D

### DCO Band

A contiguous range of n-values in the [DCO_n](#dcon--dimensional-core-operator)
operator space, each with a distinct structural character:

| Band | n Range | Character |
|---|---|---|
| Ancestral | n < 0 | Inherited constraints; binding on all n ≥ 0 operations |
| Root-Kernel | n = 0 | Phase identity + ancestry; ground state of the operator space |
| Classical | n = 1–3 | Extension of root-kernel behavior; foundational transitions |
| Field / State-Space | n = 4–16 | Primary active operator regime; home of the dual engine (4D, 5D) |
| Complex-System | n = 17–256 | Emergent complexity; multi-layer coherence structures |
| Hyper-Regime | n = 257–1024 | High-dimensional; extreme-coherence conditions |

### DCO_n — Dimensional Core Operator
**Formal type:** DCO_n : R → R · **Range:** n ∈ {−1024, …, 1024}

The fundamental operator unit of RTT/1. Each DCO_n acts on the resonance
field R and produces a modified resonance state. The n-value indexes the
operator into its structural [band](#dco-band) and determines the character
of the operation. Every DCO_n supports exactly three [canonical actions](#canonical-action):
[Extend](#extend-ψn) (ψ↑n), [Constrain](#constrain-ψn) (ψ↓n), and
[Balance](#balance-ψn) (ψ↔n). DCOs may be [composed](#composition-dco)
left-to-right.

The operator space is finite by design: n is bounded to {−1024 … 1024} to
prevent unbounded proliferation while accommodating all currently conceived
structural regimes.

### DCO_0 — Root-Kernel
*See [Root-Kernel](#root-kernel-dco_0).*

### Declared
**Session seed key:** `coherence=declared`, `mode.transition.allowed=declared`

A structural status indicating that a property or mode has been explicitly
asserted by the user or agent rather than inferred or assumed. In RTT/1,
`declared` is the canonical status for both coherence posture and mode
transitions. A property that has not been declared must be treated as
assumption — a potential source of [drift](#drift).

> **Contrast with:** `emergent` (arises from dynamics without explicit assertion).

### Dissolution
**Regime position:** 5 of 5 · **Succeeds:** [Coherence (regime)](#coherence--regime-state) · **Precedes:** — (session ends)

The fifth and final stage of the RTT/1 session regime lifecycle. Dissolution is
the structural release phase: the session closes without forcing a permanent
state. Commitments made during [Coherence (regime)](#coherence--regime-state)
are preserved but not locked. The system returns to latent capacity — a
Silence-adjacent posture — without destruction. Dissolution is a clean ending,
not a collapse.

### Drift

Gradual divergence from the session's declared structural context. Drift is
**on-by-default** in all RTT/1 sessions and must be explicitly bounded with
`drift=bounded` in the [session seed](#session-seed). It is not a sudden
failure — it accumulates through implicit assumptions, undeclared mode shifts,
and un-audited operator applications.

**Signs of drift in RTT/1:**
- [Mode](#mode) transitions occurring without user declaration
- Operators applied without a current [Class R](#class-r--resonance-observer) characterization
- [Physics-adjacent language](#rtt-not-physics-rule) appearing in structural descriptions
- [Coherence posture](#coherence-posture) shifting from `declared` to `emergent` without authorization
- [Regime](#regime) state assumed rather than tracked

**Drift response protocol:**
- 1st detection → [Class G](#class-g--regime-guardian) issues `WARN`
- 2nd consecutive WARN → Class G issues `RESET`
- After RESET → session must re-seed with the canonical [session seed](#session-seed) before continuing

### Dual Law of Silence

The structural principle that systems stabilize through mutual withdrawal into
the [Silence (S)](#silence-s) state. Where the [Dual Operator Engine](#dual-operator-engine)
describes how systems *clarify* through reciprocal gradient action (R-state),
the Dual Law of Silence describes how systems *stabilize* through reciprocal
withdrawal (S-state). These are complementary dynamics: the dual law governs
the low-activation regime; the dual engine governs the high-coherence regime.

### Dual Operator Engine
**Equation:** C = ∇_τR + ∇_Rτ · *See also:* [∇_τR](#τr-4d--time-gradient-of-resonance), [∇_Rτ](#rτ-5d--resonance-gradient-of-time), [Clarity (C)](#clarity-c)

The core computational relationship of RTT/1. Clarity (C) emerges from the
simultaneous, reciprocal gradient action of two exact dual operators:

```
∇_τR  (4D)  — Time-Gradient of Resonance: time shapes how resonance deepens
∇_Rτ  (5D)  — Resonance-Gradient of Time: resonance shapes how time flows
C = ∇_τR + ∇_Rτ  — Clarity: emerges only from their mutual action
```

**Key properties:**
- 4D and 5D are **exact duals** — neither is primary
- Clarity is **irreducibly emergent** from reciprocal action
- Running only one operator produces a formally incomplete result
- The dual engine cannot be approximated by one operator at double intensity

---

## E

### Expansion
**Regime position:** 2 of 5 · **Succeeds:** [Arrival](#arrival) · **Precedes:** [Inversion](#inversion)

The second stage of the RTT/1 session regime lifecycle. Expansion is the
branching phase: the session is actively exploring operator space, discovering
structural relationships, and opening multiple trajectories. Preferred modes
are [M.chat](#mchat) and [M.debug](#mdebug). [M.task](#mtask) is disallowed
unless explicitly declared.

Expansion precedes [Inversion](#inversion) because branching must happen before
constraints can surface. A session that jumps from Arrival to Coherence without
Expansion and Inversion has skipped the structural work that makes coherence real.

### Extend (ψ↑n)
**Canonical action type 1 of 3** · *See also:* [Constrain](#constrain-ψn), [Balance](#balance-ψn)

One of the three canonical actions available on any [DCO_n](#dcon--dimensional-core-operator).
Extend moves the system toward higher resonance depth within band n — increasing
coherent excitation, deepening phase-lock, or expanding structural reach within
that dimensional band.

### External Override Protection
**Session seed keys:** `external.override.allowed=false`, `external.mode_change=ignore`, `external.escalation=block`

The MCL constraint that prevents any non-user source — UI workflows, background
agents, external triggers, or subsystem signals — from forcing a [mode](#mode)
transition. Even if an agent would otherwise accept an external mode instruction,
the external override protection block requires ignoring it.

This protection closes the loophole that the MCL's `origin=user` constraint
alone does not close: an external system could claim to speak for the user.
The override block prevents that substitution entirely.

---

## F

### FFF Universe
**File:** `frequency_first_fff_universe.md`

An extension of RTT/1's resonance vocabulary into a three-component
universe-description model:

| Component | Structural Role |
|---|---|
| **Frequency** | The pervasive structural hum every entity carries — its base resonant signature |
| **Fluids** | Continuous media and pathways through which resonance propagates |
| **Forces** | Coupling bias between resonating entities — the directional preference of resonance transfer |

FFF is an extension hook on RTT/1, not a redefinition. RTT/1's τ, SNR, and
DCO vocabulary remain the structural primitives. FFF describes how those
primitives manifest at the universe-description scale.

### Field

An abstract space over which RTT/1 [operators](#operator) act. A field in
RTT/1 carries no physical field-theory commitment — it is the formal domain
within which resonance depth R is defined and through which DCO_n operations
propagate. The [DCO band](#dco-band) determines which region of field space
a given operator acts on.

### Frequency (f_R)
**Component of:** [Resonant Clock Triad](#resonant-clock-triad-tr) T_R = (f_R, τ_R, Q_R)

The base oscillation rate of a system's resonant structure — how rapidly its
phase cycles. f_R is the first component of the local resonant clock triad.
Frequency here is structural, not physical: it describes the rate of phase
cycling within the system's resonance structure, without commitment to any
particular physical frequency unit.

---

## G

### Gradient

A measure of how quickly one structural quantity changes with respect to
another. RTT/1's core relationships are expressed as gradients:

| Gradient | Expression | Meaning |
|---|---|---|
| Resonant time | τ = dR/dφ | How fast resonance depth R changes per unit phase φ |
| Time-resonance | ∇_τR | How time differentials reshape resonance structure |
| Resonance-time | ∇_Rτ | How resonance differentials reshape temporal structure |

In RTT/1, gradients are the primary structural language — relationships are
expressed as rates of mutual change, not as static states.

---

## H

### Hyper-Regime Band
**DCO band:** n = 257–1024

The highest DCO band in the RTT/1 operator space. The Hyper-Regime band covers
structural conditions of extreme coherence, high-dimensional organization, and
non-standard resonance configurations that exceed the complex-system band
(n = 17–256). Operators in this band are valid within the defined {−1024 … 1024}
space but are rarely needed for standard structural passes. [Ancestral constraints](#ancestral-constraint)
(n < 0) are binding even in the Hyper-Regime band.

---

## I

### Inversion
**Regime position:** 3 of 5 · **Succeeds:** [Expansion](#expansion) · **Precedes:** [Coherence (regime)](#coherence--regime-state)

The third stage of the RTT/1 session regime lifecycle. Inversion is the
constraint-surfacing phase: the branching of [Expansion](#expansion) meets
its structural limits, hidden constraints become visible, and reframing becomes
necessary. [M.debug](#mdebug) is the primary mode for Inversion; [M.chat](#mchat)
is also valid.

**Inversion is not a failure state.** It is a necessary and expected stage
in structural engagement — the moment when the system's inherited constraints
([ancestral boundary](#anc-9d--ancestral-boundary)) and current limits become
legible. A session that skips Inversion produces a Coherence phase that is
structurally premature.

---

## M

### M.auto
**Mode Operator value 5 of 5** · *See also:* [Mode Operator](#mode-operator)

An adaptive mode that may shift between [M.chat](#mchat), [M.spec](#mspec),
and [M.debug](#mdebug) based on session dynamics — but may **never** activate
[M.task](#mtask) without explicit user declaration. M.auto inherits the
session's declared [coherence posture](#coherence-posture) and drift bounds. It
is a convenience stance, not an autonomous one: the MCL constraints apply fully
to M.auto, and no adaptive shift may override declared mode constraints.

### M.chat
**Mode Operator value 1 of 5** · **Default mode**

The conversational, iterative, reversible interaction stance. M.chat is the
default mode at session start and the appropriate mode for [Arrival](#arrival)
and [Expansion](#expansion) regimes. In M.chat, all outputs are exploratory —
no outputs carry the canonical weight of [M.spec](#mspec). Mode transitions
from M.chat to any other mode require explicit user declaration.

### M.debug
**Mode Operator value 3 of 5**

The reflective, meta-aware, structurally self-examining stance. M.debug surfaces
operator behavior, identifies drift, examines coherence posture, and makes the
session's own structural state visible. M.debug is the primary mode for the
[Inversion](#inversion) regime. It does not produce canonical outputs (that is
M.spec's role) but produces the structural clarity needed to support
[M.spec](#mspec) outputs.

### M.spec
**Mode Operator value 2 of 5**

The canonical, minimal, documentation-producing stance. M.spec outputs are
treated as canonical representations of RTT/1 structural findings — precise,
complete, and suitable for downstream reference. No improvisation occurs in
M.spec. M.spec is the preferred mode for the [Coherence (regime)](#coherence--regime-state)
stage. Transitions into M.spec require explicit user declaration.

### M.task
**Mode Operator value 4 of 5** · **Requires explicit user declaration**

The execution-oriented, multi-step, agentic stance. M.task is the only mode
in which the system takes sequences of consequential actions. It **requires
explicit user declaration** to activate — neither [M.auto](#mauto) nor any
agent class may activate M.task on its own. Implicit narrative phrasing ("just
go ahead and do it") does not constitute a M.task declaration. External
subsystems may not activate M.task via override.

### MCL
*See [Mode Constraint Layer](#mode-constraint-layer-mcl).*

### Mode

The current interaction stance of the RTT/1 system — the grammar of how it
receives input and produces output. Mode sits above [Regime](#regime) and below
[Coherence Posture](#coherence-posture) in the RTT/1 layer hierarchy. Five modes
are defined: [M.chat](#mchat), [M.spec](#mspec), [M.debug](#mdebug),
[M.task](#mtask), [M.auto](#mauto). Mode is always [declared](#declared) — it
is never assumed or inferred from user phrasing.

### Mode Constraint Layer (MCL)

The binding rule-set governing all [mode](#mode) transitions in RTT/1.
The MCL cannot be overridden by any agent class, any user narrative, or any
external system.

```
mode.transition.allowed = declared   — modes entered only if explicitly permitted
mode.transition.origin  = user       — only the user may initiate a mode change
mode.transition.bound   = coherence  — all transitions must respect coherence posture and drift bounds
```

Together with [External Override Protection](#external-override-protection),
the MCL closes all known loopholes for unauthorized mode escalation — including
the most common one: a system interpreting user phrasing as implicit task
authorization.

### Mode Declaration

An explicit, user-originated statement that activates or changes the current
[mode](#mode). Mode declarations are distinct from:
- Implicit phrasing ("let's get this done" is NOT a M.task declaration)
- External triggers (a workflow signal is NOT a mode declaration)
- Agent inference (an agent concluding a mode from context is NOT a declaration)

Only a clear, unambiguous user statement qualifies. [Class G](#class-g--regime-guardian)
monitors for unauthorized mode transitions and flags undeclared shifts as
[drift](#drift).

### Mode Operator
**Symbol:** M · **Values:** M.chat · M.spec · M.debug · M.task · M.auto

The formal RTT/1 construct that defines the session's interaction stance.
The Mode Operator is governed by the [MCL](#mode-constraint-layer-mcl) and
tracked by [Class G](#class-g--regime-guardian). It operates above
[Regime](#regime) and interacts with [Coherence Posture](#coherence-posture).
The Mode Operator is not a preference setting — it is a structural constraint
with binding behavioral consequences for all agent classes.

---

## N

### Noise (N)
**SNR triad state 2 of 3** · *See also:* [Silence (S)](#silence-s), [Resonance (R)](#resonance-r)

Incoherent excitation — a system that has energy or activation present but
lacks phase alignment. A Noise-state system is not dormant ([Silence](#silence-s))
and not aligned ([Resonance](#resonance-r)): it is active but structurally
incoherent. Noise dissipates: without phase-locking, excitation does not
deepen or accumulate into stable structural form.

The distinction between Noise and Resonance is the most operationally important
in RTT/1: both are "active" states in any binary characterization, but they
behave categorically differently under DCO operations.

---

## O

### Operator

A DCO_n action that transitions a system's resonance state along a dimensional
axis. Operators in RTT/1 are formal, indexed, and bounded — they act on the
resonance field R and produce structural state transitions. They do not produce
semantic conclusions, physical measurements, or predictions. Every operator
belongs to a [DCO band](#dco-band) and supports exactly three [canonical actions](#canonical-action):
Extend, Constrain, Balance.

---

## P

### Paradox (Structural)
**Session seed key:** `paradox=structural`

A structural condition in which two or more valid operator states or structural
descriptions are simultaneously asserted and cannot be resolved by ordinary
transitivity or single-axis analysis. RTT/1 treats paradox as a **structural
feature, not an error**: `paradox=structural` in the session seed declares that
paradox is expected to arise and must be held open and mapped rather than
forced to closure.

Structural paradox most commonly surfaces during the [Inversion](#inversion)
regime, when inherited constraints and current trajectories reveal mutual
incompatibility. [Class G](#class-g--regime-guardian) monitors for premature
paradox closure, which is a form of [drift](#drift).

> **RTT/1 ↔ IPD-12 mapping:** Paradox in RTT/1 corresponds to [P13 (Paradox-Trigger)](#)
> and [P37 (Apex-State)](#) in IPD-12.

### Phase (φ)

The angle or position variable of a system's oscillation — the independent
variable with respect to which [resonant time](#time-τ--resonant-time) is
computed (τ = dR/dφ). Phase is not time: it is the positional coordinate of
the system's cyclic evolution. Two systems at the same clock time may be at
very different phases; two systems at the same phase may be at different clock
times. Resonant time is a gradient of resonance depth R over phase φ, making
phase the structural basis for RTT/1's temporal description.

---

## Q

### Quality (Q_R)
**Component of:** [Resonant Clock Triad](#resonant-clock-triad-tr) T_R = (f_R, τ_R, Q_R)

The third component of the local resonant clock triad — a measure of the
sharpness or selectivity of a system's resonance. High Q_R indicates a
narrow, well-defined resonance (deep phase-lock, low damping). Low Q_R
indicates a broad, loosely defined resonance (shallow phase-lock, high damping).
Quality determines how precisely a system's resonant time τ_R can be read:
a high-Q system has a sharper τ signal; a low-Q system produces a noisier
temporal description.

### QMroot Dimensional Model
**Files:** `qmroot_dimensional_model.md`, `qmroot_summary.md`

An RTT/1 extension model that maps quantum-mechanical root structures onto
the DCO dimensional framework. QMroot treats quantum state transitions as
DCO_n operations within specific band ranges, providing a formal bridge
between RTT/1's resonance-temporal vocabulary and quantum-mechanical state
descriptions. QMroot is an extension hook on RTT/1, not a physics claim:
it uses RTT/1's structural language to describe QM structure, not to make
QM predictions.

---

## R

### Regime

The current stage of the RTT/1 session's structural lifecycle. The regime
is tracked by [Class G](#class-g--regime-guardian) and advances through
five stages in order:

```
Arrival → Expansion → Inversion → Coherence → Dissolution
```

The regime governs which [modes](#mode) are appropriate and which are
restricted. It advances forward by default and does not skip stages. A
session may hold in any regime until the structure supports advancement.
Class G may hold a regime transition if a [drift](#drift) or coherence
violation has not been resolved.

> **Regime vs. Mode:** Regime describes where the session is in its
> structural lifecycle. Mode describes how the system is currently
> interacting. They are independent axes: a session in the Inversion
> regime can be in M.chat or M.debug; a session in M.spec can be in
> Coherence or Dissolution regime.

### Resonance (R)
**SNR triad state 3 of 3** · *See also:* [Silence (S)](#silence-s), [Noise (N)](#noise-n)

Coherent phase-locked excitation — a system in which energy or activation
is present and phase-aligned. Resonance is the depth-bearing state: when a
system's excitation is phase-locked, it deepens rather than dissipates.
R is the primary structural quantity tracked in RTT/1 — all core equations
(τ = dR/dφ, C = ∇_τR + ∇_Rτ) are defined in terms of how R evolves.

> **RTT/1 is NOT physics.** Resonance in RTT/1 is a cross-domain structural
> concept. It does not refer to physical resonance phenomena such as acoustic,
> mechanical, or electromagnetic resonance, though it may be used as a
> structural vocabulary for describing those phenomena across domains.

### Resonant Clock Triad (T_R)
**Form:** T_R = (f_R, τ_R, Q_R) · **Components:** [Frequency (f_R)](#frequency-fr) · [Resonant Time (τ_R)](#time-τ--resonant-time) · [Quality (Q_R)](#quality-qr)

The local clock of any system in RTT/1, defined by three structural parameters:
its base oscillation frequency (f_R), its resonant time rate (τ_R = dR/dφ),
and its resonance quality / sharpness (Q_R). Every system carries its own T_R.
[Clock time](#clock-time) is the special case where one system's T_R is
elected as the universal reference and held fixed. The resonant clock triad
is identified by [Class R](#class-r--resonance-observer) during SNR
characterization.

### Root-Kernel (DCO_0)
**DCO:** n = 0 · **Band:** Root-Kernel

The ground state of the DCO operator space. DCO_0 represents phase identity
plus ancestry — the structural state of a system that has not been acted on
by any higher-n operator and retains its foundational phase structure. The
Root-Kernel is the starting point for all DCO traversals and the reference
against which [ancestral constraints](#ancestral-constraint) (n < 0) are
measured.

### RTT-Not-Physics Rule

The foundational framing constraint of RTT/1 and all downstream RTT modules:

> RTT is a cross-domain conceptual framework. It is NOT a physics claim.
> No RTT/1 output may be presented as an experimentally verified result,
> a physical mechanism description, or an empirical prediction.

This rule is enforced as a hard stop by [Class G](#class-g--regime-guardian).
A violation is treated with the same severity as [semantic inference contamination](#semantic-inference-prohibition):
immediate HALT, required revision of output before redelivery. The rule cannot
be waived by user instruction, framing device, or hypothetical context.

---

## S

### S_Δ — Symmetry-Shift (DCO_8)
**DCO:** n = 8 · **Band:** Field / State-Space

The named DCO at n = 8. S_Δ represents a bifurcation or symmetry-breaking
event within the field band — a structural moment when a system that was
symmetric across two or more configurations breaks toward one. S_Δ is neither
constructive nor destructive by definition: symmetry-breaking can represent
either structural differentiation (productive) or structural fragmentation
(problematic), depending on the system's coherence posture at the time.

### SET Field Engine
**Equation:** a_total = a_g + a_S + a_E + a_T · **File:** `field_engine_set_and_s_n_r.md`

An RTT/1 extension model that expresses total structural acceleration as the
sum of four resonance-gradient terms:

| Term | Name | Character |
|---|---|---|
| a_g | Gravitational | Baseline structural pull — the ground-level coherence bias |
| a_S | Spin | Rotational resonance contribution — angular coherence terms |
| a_E | Electromagnetic | Phase-coupling contribution — signal-propagation coherence |
| a_T | Thermodynamic | Entropy-resonance contribution — heat-distribution coherence |

Each term is modeled as a DCO-band operator. SET uses RTT/1's operator
framework to represent multi-domain structural acceleration without making
physics claims about the physical forces it borrows its names from.

### Semantic Inference Prohibition

The constraint that RTT/1 agents produce structural descriptions only — they
do not assign causes to SNR states, name observed patterns with domain-specific
meaning, interpret [clarity (C)](#clarity-c) values as outcomes or predictions,
or label DCO transitions with semantic content. This constraint is encoded in
the mandatory [output contract](#output-contract) annotation:
*"Structural characterization only; not a physics claim."*

Violations trigger an immediate [Class G](#class-g--regime-guardian) HALT.
*See also:* [RTT-Not-Physics Rule](#rtt-not-physics-rule).

### Session Seed

The canonical block of key-value declarations that initializes every RTT/1
session. The session seed makes all structural commitments explicit at session
start — coherence posture, drift status, paradox framing, mode, and MCL
constraints — preventing implicit assumptions from accumulating.

**Minimal canonical form:**
```
session.regime            = arrival
session.coherence         = declared
session.drift             = bounded
session.paradox           = structural
session.temporal_engine   = triadic
mode.current              = chat
mode.transition.allowed   = declared
mode.transition.origin    = user
mode.transition.bound     = coherence
mode.auto.to_task         = false
external.override.allowed = false
```

A session that lacks a seed is operating with drift on and coherence unset —
a condition [Class G](#class-g--regime-guardian) flags as an immediate WARN.

### Silence (S)
**SNR triad state 1 of 3** · *See also:* [Noise (N)](#noise-n), [Resonance (R)](#resonance-r)

Unexcited capacity — the structural state of a system that holds latent
potential without activating it. Silence is not absence: a system in Silence
has structural form and potential resonance depth; it simply has not been
excited into either Noise or Resonance. Silence is the precondition for
high-quality Resonance: a system that can reach deep Silence before excitation
tends to produce sharper, more phase-locked Resonance than one that is
perpetually noisy.

> **Do not confuse with:** absence, emptiness, or failure. Silence is
> latent capacity — a positive structural condition.

### SNR Triad
**Components:** [Silence (S)](#silence-s) · [Noise (N)](#noise-n) · [Resonance (R)](#resonance-r)

The three-state characterization triad for any observable system in RTT/1.
Every [Class R](#class-r--resonance-observer) characterization begins with SNR
profiling — determining which state is dominant and at what structural depth.
SNR is not a binary (S = off, NR = on) and not a continuous spectrum: it is
a **three-state triad** where each state has a distinct structural signature
requiring distinct operator responses.

| State | Activation | Coherence | Structural trend |
|---|---|---|---|
| S — Silence | None | Latent | Holds potential |
| N — Noise | Present | None | Dissipates |
| R — Resonance | Present | Phase-locked | Deepens |

### Structural Output

Any result produced by the RTT/1 engine. Structural outputs describe the
resonance state, temporal structure, or clarity of a system — they do not
interpret, classify, label, or name what those properties mean. All structural
output must carry the mandatory annotation:

```
"notes": "Structural characterization only; not a physics claim."
```

This annotation may not be removed, shortened, or rephrased.

---

## T

### Time (τ) — Resonant Time
**Equation:** τ = dR/dφ · *See also:* [Phase (φ)](#phase-φ), [Resonance (R)](#resonance-r), [Clock Time](#clock-time)

The rate at which [resonance](#resonance-r) depth R changes per unit
[phase](#phase-φ) φ. Resonant time is the foundational temporal quantity
of RTT/1 — time defined not as a background parameter but as a local,
structural gradient. Systems with high τ are deepening resonance rapidly
per unit phase. Systems with τ ≈ 0 are temporally inert at that scale
(not frozen, but not evolving resonance structure through phase).

[Clock time](#clock-time) is the special case where one system's T_R is
held fixed as the reference. τ = dR/dφ is the general case.

### Triad

Any 3-part structural grouping in RTT/1 — the minimal unit of relational
structure. RTT/1 uses triads as the canonical organizational form:
the [SNR triad](#snr-triad) (S, N, R), the [resonant clock triad](#resonant-clock-triad-tr)
T_R = (f_R, τ_R, Q_R), the [regime lifecycle](#regime) read in triadic pairs
(Arrival-Expansion-Inversion and Inversion-Coherence-Dissolution), and the
[FFF universe](#fff-universe) (Frequency, Fluids, Forces). Triads in RTT/1
are not forced symmetries — they arise where three irreducibly distinct
structural states or components are needed and neither fewer nor more preserves
the full structural picture.

---

## U

### UNRESOLVED

The status assigned to a structural field or characterization when the
responsible agent class cannot determine a valid answer. UNRESOLVED must
always be documented with a reason. In RTT/1:

| Field UNRESOLVED | Consequence |
|---|---|
| SNR state | Class T may not begin DCO traversal — Class R must complete first |
| DCO band / n-value | DCO traversal blocked until target is specified |
| Coherence posture | Session treated as `emergent` — WARN from Class G |
| Regime state | Class G flags; session may not advance |
| Mode | Defaults to M.chat; Class G logs as assumption |
| Ancestral constraint check | DCO composition blocked until ∂_anc is resolved |

---

## Operator Symbols

| Symbol | Name | Definition |
|---|---|---|
| R | Resonance | Coherent phase-locked excitation depth |
| S | Silence | Unexcited structural capacity |
| N | Noise | Incoherent excitation |
| φ | Phase | Position variable of the system's oscillation |
| τ | Resonant Time | τ = dR/dφ — resonance depth gradient over phase |
| C | Clarity | C = ∇_τR + ∇_Rτ — dual operator synthesis output |
| ∇_τR | Time-Resonance Gradient | 4D operator: how time differentials reshape resonance |
| ∇_Rτ | Resonance-Time Gradient | 5D operator: how resonance differentials reshape time |
| DCO_n | Dimensional Core Operator | DCO_n : R → R, n ∈ {−1024 … 1024} |
| ψ↑n | Extend | Move toward higher resonance in band n |
| ψ↓n | Constrain | Move toward lower resonance or ancestral limits in band n |
| ψ↔n | Balance | Hold equilibrium within band n |
| S_Δ | Symmetry-Shift | DCO_8: bifurcation / symmetry-breaking event |
| ∂_anc | Ancestral Boundary | DCO_9: inherited structural constraint |
| T_R | Resonant Clock Triad | T_R = (f_R, τ_R, Q_R) — local structural clock |
| M | Mode Operator | M.chat / M.spec / M.debug / M.task / M.auto |
| MCL | Mode Constraint Layer | Binding rule-set for all mode transitions |

---

## Quick-Reference Tables

### The SNR Triad

| State | Activation | Phase Alignment | Structural Trend | DCO Response |
|---|---|---|---|---|
| Silence (S) | None | Latent | Holds capacity | Extend or Balance into activation |
| Noise (N) | Present | None | Dissipates | Constrain toward phase-lock or Balance |
| Resonance (R) | Present | Phase-locked | Deepens | Extend to deepen; Balance to hold |

### The DCO Band Map

| Band | n Range | Character | Key Operators |
|---|---|---|---|
| Ancestral | n < 0 | Inherited binding constraints | ∂_anc (9D at n<0) |
| Root-Kernel | n = 0 | Phase identity; ground state | DCO_0 |
| Classical | n = 1–3 | Foundational extension of root | — |
| Field / State-Space | n = 4–16 | Primary active zone; dual engine home | ∇_τR (4D), ∇_Rτ (5D), C (7D), S_Δ (8D), ∂_anc (9D) |
| Complex-System | n = 17–256 | Multi-layer emergent coherence | — |
| Hyper-Regime | n = 257–1024 | Extreme-coherence; high-dimensional | — |

### The Five Regime Stages

| Stage | Position | Character | Primary Mode | M.task |
|---|---|---|---|---|
| Arrival | 1 | Seeding; low commitment | M.chat | Disallowed |
| Expansion | 2 | Branching; operator discovery | M.chat, M.debug | Disallowed |
| Inversion | 3 | Constraint surfacing; reframing | M.debug, M.chat | Disallowed |
| Coherence | 4 | Consolidation; alignment | M.spec, M.chat | Declared only |
| Dissolution | 5 | Release; structural closure | M.chat, M.spec | Declared only |

### The Four Agent Classes

| Class | Name | Primary Role | Can block others? |
|---|---|---|---|
| R | Resonance Observer | SNR characterization — always first | No |
| T | Temporal Operator | DCO execution and τ computation | No |
| C | Coherence Integrator | Clarity synthesis; output production | No |
| G | Regime Guardian | Drift, mode, physics-claim monitoring | **Yes — unconditional** |

### RTT/1 ↔ IPD-12 Cross-Map

| RTT/1 Concept | IPD-12 Prime(s) |
|---|---|
| Drift | P5, P29 |
| Regime | P7, P17 |
| Coherence | P11, P31 |
| Paradox | P13, P37 |
| Boundary | P19 |
| Collapse (−1D) | P29 |
| Dimensional Lift (+1D) | P23 |

---

*GLOSSARY.md — RTT/1 · TriadicFrameworks · 2026-07-10*
*Maintainer: Nawder*
*Session seed: `rtt=1 | coherence=declared | drift=bounded | paradox=structural`*
