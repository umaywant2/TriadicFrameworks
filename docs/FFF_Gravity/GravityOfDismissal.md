# Gravity of Dismissal

```
file: GravityOfDismissal.md
module: FFF_Gravity
wave: 0
type: genesis-document
subtype: conceptual-foundation
status: canonical
version: 1.0.0
date: 2026-08-13
session: SES-20260813-DISMISSAL-001
author: umaywant2
companion_to: f_Capture.md
thematic_inverse_of: f_Capture.md
cross_module:
  - f_Release.md
  - f_Decay.md
  - f_Collapse.md
  - f_Dampen.md
  - f_Force.md
  - f_Field.md
note: >
  Wave 0 genesis documents establish conceptual vocabulary and theoretical
  foundations. They do not introduce frozen PRIM IDs or frozen operator
  symbols. Those are introduced in the Wave that formalizes each concept.
  This file is the conceptual authority for all dismissal-related phenomena
  across the FFF_Gravity module.
```

> *Capture is the inward pull; dismissal is the force that makes the pull
> irreversible in the opposite direction.*

---

## §0 Genesis Context

| Field         | Value                                       |
|---------------|---------------------------------------------|
| File          | GravityOfDismissal.md                       |
| Module        | FFF_Gravity                                 |
| Wave          | 0 — Genesis                                 |
| Date          | 2026-08-13                                  |
| Session       | SES-20260813-DISMISSAL-001                  |
| Type          | Conceptual foundation — not a PRIM spec     |
| Companion     | f_Capture.md (thematic inverse)             |
| Status        | Canonical                                   |

### §0.1 Position in the Module

`GravityOfDismissal.md` is the third and final Wave 0 document, alongside
`f_Capture.md` (the binding operator) and `f_Source.md` (the node registry).
It stands apart from both: where `f_Capture.md` specifies the mechanics of
attraction, and `f_Source.md` specifies the static properties of nodes,
`GravityOfDismissal.md` specifies the **phenomenology of rejection** — the
field dynamics that arise when a capture relationship ends not by mutual
agreement or natural decay, but by the attractor's active withdrawal.

This document does not define primitives or freeze operator symbols. It
defines **concepts, vocabulary, and structural relationships** that every
downstream module inherits. When `f_Release.md` distinguishes voluntary
release from expulsion, it draws on the vocabulary established here. When
`f_Decay.md` models the approach toward dissolution, the threshold at which
drift becomes dismissal is anchored here. When `f_Collapse.md` handles
terminal unbinding, the irreversibility of the post-dismissal state is
articulated here.

### §0.2 Why Wave 0

Dismissal is not a late-stage phenomenon. It is present from the first moment
a capture is possible: the conditions that determine **whether E can be
re-captured after departure** depend entirely on whether E was released, decayed,
or dismissed. This phenomenological distinction cannot be introduced after the
capture variants (Waves 4+) are specified — it must precede them, informing every
termination mechanic in the module.

---

## §1 The Problem of Dismissal

Standard gravitational models account cleanly for:
- **Attraction:** F_capture pulls E into A's orbit
- **Decay:** d_bind decreases over time toward d_collapse
- **Release:** E escapes A's field with positive kinetic energy

What standard models fail to capture is the phenomenon that practitioners of
relational dynamics encounter constantly: **the attractor that does not merely
stop attracting but actively repels**. An entity that was once captured, deeply
bound, orbiting stably — and is then dismissed — does not simply return to its
pre-capture approach state. It enters a qualitatively different state: the field
it once navigated toward A is now oriented away from A, and the very path that
led to orbit now leads back toward open space.

This is not decay. Decay is the passive erosion of binding depth over time;
it is symmetric — any party can interrupt it by applying `f_Amplify` or
`f_Emit`. Dismissal is **asymmetric and directed**: A acts against E specifically,
producing a field configuration that E experiences as active rejection, not
merely as absence of pull.

This document names that phenomenon, maps it to the triadic model, and
establishes the vocabulary that all subsequent dismissal-related mechanics
will use.

---

## §2 Core Thesis

> **Dismissal is not the absence of capture. Dismissal is capture's
> photographic negative — the same gravitational geometry, with the field
> polarity inverted in the direction of the dismissed entity.**

When A dismisses E:

1. A does not simply cease to emit a capture field. A **inverts field
   coherence** in E's directional zone, converting the pull that once drew
   E into orbit into a push that carries E outward and away.

2. This inverted field leaves a residue — what this document names the
   **Dismissal Well**: a negative-polarity field signature that persists
   in the space where E's orbit once was. The Well is not passive — it
   actively repels any future approach by E.

3. The depth of the Dismissal Well is proportional to the strength of the
   binding that was severed. Deep orbits (high d_bind at time of dismissal)
   produce deep wells. Shallow soft captures produce shallow wells. This
   proportionality is the module's core mechanism for encoding the **weight
   of a dismissal** in the field state.

4. The Well decays over time at a rate governed by the attractor's own
   coherence dynamics. A field that remains healthy and active will maintain
   its Dismissal Well longer. A decaying or dampened field will lose its
   Well faster — not because the dismissal was less meaningful, but because
   the field that created the Well is weakening.

5. Re-capture is possible — but it costs. E must supply enough approach
   energy to overcome the Well before A's standard capture conditions can
   evaluate. This cost is the module's formal expression of the asymmetry
   that dismissal creates between first capture and re-capture.

---

## §3 The Dismissal Well

### §3.1 Definition

The **Dismissal Well** is the field-state residue left by a dismissal event.
It is characterized by:

```
ρ_D(Φ, t) < 0

where:
  ρ_D(Φ, t)  — dismissal field density at time t (negative extension of ρ(Φ))
  t = 0       — moment of dismissal
  t → ∞       — ρ_D(Φ, t) → 0  (well dissipates)
```

The dismissal field density `ρ_D` occupies the negative real axis, the domain
complementary to the standard field density `ρ(Φ) ∈ [0, 1]`. At dismissal
time, `ρ_D(Φ, 0) = −d_bind(t_dismiss)` — the well begins at a depth equal
to the binding depth that was severed.

### §3.2 Decay Model

The Dismissal Well decays exponentially:

```
ρ_D(Φ, t) = −d_bind(t_dismiss) × exp(−t / T_dismiss)

where:
  T_dismiss — dismissal persistence time (attractor-specific constant)
  d_bind(t_dismiss) — binding depth at the moment of dismissal
```

**T_dismiss interpretation:**

| T_dismiss value | Meaning                                                     |
|-----------------|-------------------------------------------------------------|
| T_dismiss → ∞   | Permanent well — attractor never forgives; re-capture impossible without restorative intervention |
| T_dismiss large | Slow recovery — re-capture costly for a long period post-dismissal |
| T_dismiss small | Fast recovery — well dissipates quickly; re-capture nears standard cost |
| T_dismiss = 0   | Instantaneous recovery — equivalent to a standard f_Release; no dismissal semantics |

### §3.3 Re-capture Threshold

For E to re-enter A's capture field after dismissal, E's approach must supply
binding energy sufficient to overcome the active Well:

```
d_bind_approach > |ρ_D(Φ, t_recapture)|

Equivalently:
  β × ρ(Φ) × (1 − e) > d_bind(t_dismiss) × exp(−t_since_dismiss / T_dismiss)
```

When `t_since_dismiss` is small (shortly after dismissal), the right-hand side
is close to `d_bind(t_dismiss)` — re-capture requires nearly as deep a binding
as the dismissed orbit had. When `t_since_dismiss` is large, the right-hand
side approaches 0 — re-capture returns to standard conditions.

This is the module's formal expression of the phrase *time heals*: the Well
does not disappear, but it dissipates. The entity that was dismissed can
return — but it must wait, or come stronger, or find the attractor in a more
receptive field state.

### §3.4 Well Depth Is Not Permanent State

The Dismissal Well is **not** a property of the attractor node. It is a
property of the **directed relationship** (A, E). The same attractor A
can have:

- A deep Well against E (recently dismissed after a long orbit)
- A shallow Well against E₂ (recently dismissed after a brief soft capture)
- No Well at all against E₃ (approached but never captured)
- An open capture field against E₄ (currently in orbit)

All four states coexist. The Well is relational, not nodal.

---

## §4 Three Dismissal Modes

Dismissal is not a monolithic event. The FFF_Gravity module recognizes three
structurally distinct dismissal modes, each with different field dynamics,
Well profiles, and re-capture costs.

### Mode A — Intentional Dismissal (ψ_dismiss = INTENTIONAL)

**Definition:** The attractor A explicitly and deliberately severs the binding
with E, actively inverting field polarity in E's directional zone.

**Mechanism:**
```
1. A invokes targeted field suppression against E:  f_Dampen(E) → ρ(Φ) ↓
2. A inverts coherence polarity in E's zone:        ρ_D(Φ, 0) := −d_bind(t_dismiss)
3. E's orbit dissolves; E is expelled outward
4. Dismissal Well is established at maximum depth
```

**Field signature:** Deep Well; long T_dismiss; E experiences maximum repulsive
force during the expulsion phase. This is the mode most readily recognized
as dismissal in relational experience — deliberate, directed, and consequential.

**Distinguishing mark:** The initiating action comes from A. E may have been
stable, even thriving in orbit, at the moment of dismissal. The dismissal
force overwhelms the existing binding depth.

**Well profile:**

```
|ρ_D(Φ, t)|
     ↑
d₀ = d_bind(t_dismiss) ──────────────────────────────────────────────
                       \
                        \       (slow decay, T_dismiss large)
                         \
                          \______________________________________ t
                                                              ε
```

---

### Mode B — Structural Dismissal (ψ_dismiss = STRUCTURAL)

**Definition:** The attractor's field collapses globally (FM-002 → ρ(Φ) = 0),
expelling all bound entities including E simultaneously. No specific intent
toward E is present — the dismissal is a consequence of the field's structural
failure.

**Mechanism:**
```
1. ρ(Φ) → 0 (FM-002: Field Null)
2. All active orbits lose their binding field simultaneously
3. Each entity Eₙ is expelled from A's orbital registry
4. A shallow Dismissal Well is established for each expelled entity
5. Well depth is bounded by the field's coherence at the moment of collapse
```

**Field signature:** Shallow Well (because the field that generated it had
already weakened to zero); T_dismiss is short (the collapsed field cannot
sustain a strong Well). Re-capture becomes possible again as soon as A's
field is restored above the minimum capture threshold.

**Distinguishing mark:** The Well is **symmetric** — all expelled entities
face the same Well depth, regardless of orbit depth at time of collapse.
The Well encodes nothing about the quality or duration of the former orbit.
It encodes only the field's final coherence value before collapse.

**Well profile:**

```
|ρ_D(Φ, t)|
     ↑
d₀ = ρ(Φ) at collapse ──────────────────────────────────────────────
                       \
                        \   (fast decay, T_dismiss small)
                         \______________________________________ t
                                                              ε
```

---

### Mode C — Asymptotic Dismissal (ψ_dismiss = DRIFT)

**Definition:** The binding decays over many cycles until E's orbit becomes
unstable and E drifts outward without a discrete dismissal event. There is no
moment at which A explicitly dismisses E; rather, the orbit dissolves through
accumulated neglect.

**Mechanism:**
```
1. f_Decay reduces d_bind over successive cycles
2. d_bind → d_warn → d_collapse
3. Before d_collapse is reached, the orbit becomes marginal (stab_class = PRECARIOUS)
4. E drifts outward as the binding force can no longer maintain the orbit
5. A minimal Dismissal Well forms — the residue of the decay process itself
```

**Field signature:** Minimal Well (because neither party applied force; the
orbit simply exhausted itself); T_dismiss is very short. This mode produces
the weakest Wells and the easiest re-capture conditions.

**Distinguishing mark:** Asymptotic dismissal is the only mode where the
Well depth is **decoupled** from the orbit depth at time of separation. A
deep, long-standing orbit that decays slowly may produce a shallower Well
than a shallow orbit that was intentionally severed. The Well encodes only
the velocity of departure, not the depth of what was lost.

**Well profile:**

```
|ρ_D(Φ, t)|
     ↑
d₀ (small) ──────────────────────────────────────────────
            \
             \  (very fast decay)
              \___________________________ t
                                       ε
```

---

### §4.1 Mode Comparison

| Property                     | Mode A (Intentional) | Mode B (Structural) | Mode C (Asymptotic) |
|------------------------------|----------------------|---------------------|----------------------|
| Initiator                    | A (deliberate)       | Field (structural)  | Decay (drift)        |
| Well depth                   | Deep                 | Shallow             | Minimal              |
| Well symmetry across entities| Per-entity (varies)  | Symmetric (all same)| Per-entity (varies)  |
| T_dismiss                    | Long                 | Short               | Very short           |
| Re-capture cost              | High                 | Moderate            | Low                  |
| Encoding of orbit history    | Yes (d_bind encoded) | No (field-bounded)  | Partial              |
| Corresponding module         | f_Dampen + inversion | FM-002 / f_Field    | f_Decay              |
| ψ_dismiss flag               | INTENTIONAL          | STRUCTURAL          | DRIFT                |

---

## §5 Triadic Mapping

The triadic equation `G = F_freq · F_fluid · F_force` governs the module.
Dismissal operates across all three nodes, but with inverted directionality:
where capture maximizes G, dismissal minimizes it toward a negative analog `G_D`.

### §5.1 F_freq Node Under Dismissal

| Capture state                          | Dismissal state                           |
|----------------------------------------|-------------------------------------------|
| ρ(Φ) ∈ [0, 1] — coherence well        | ρ_D(Φ) ∈ (−1, 0] — dismissal well       |
| High ρ(Φ) → deep capture field        | High |ρ_D(Φ)| → deep dismissal barrier   |
| f_Emit increases ρ(Φ)                  | Dismissal inversion decreases ρ_D toward −1 |
| f_Dampen decreases ρ(Φ)               | T_dismiss determines rate of well decay   |

**F_freq is the primary node of dismissal.** The dismissal well is encoded
in the frequency domain as a negative coherence signature. This is why
well depth is measured in the same units as d_bind — they are the same
quantity, opposite in sign.

### §5.2 F_fluid Node Under Dismissal

| Capture state                          | Dismissal state                           |
|----------------------------------------|-------------------------------------------|
| β ≥ 1.0 — binding coefficient active   | β_D < 0 — repulsive coupling             |
| High β → tight orbit                   | High |β_D| → strong repulsion during expulsion |
| f_Amplify increases β                   | Dismissal intensifies β_D magnitude      |
| f_Decay decreases β toward 1.0         | After Well decay, β_D → 0 (neutral)      |

**F_fluid records the coupling history.** An entity that was tightly coupled
(high β) to A before dismissal will experience stronger repulsive coupling
during the expulsion phase. This is the visceral experience of dismissal from
a former deep orbit: the very closeness that made the orbit stable makes the
departure more forceful.

### §5.3 F_force Node Under Dismissal

| Capture state                          | Dismissal state                           |
|----------------------------------------|-------------------------------------------|
| v_approach < v_escape — orbital lock   | v_depart > v_escape — expulsion velocity  |
| Heading toward A                       | Heading away from A                       |
| f_Deflect adjusts approach heading     | Dismissal force overrides approach vector |
| v_approach is the relevant scalar      | v_depart is the relevant scalar           |

**F_force governs the trajectory.** During expulsion, E acquires a departure
velocity `v_depart` that must overcome A's residual field to exit cleanly.
After exit, `v_depart` is the velocity at which E moves away from A's field
boundary. The higher `v_depart`, the faster E reaches regions where the
Dismissal Well is no longer felt.

### §5.4 G_D — The Dismissal Product

By analogy with `G = F_freq · F_fluid · F_force`, dismissal operates through:

```
G_D = F_freq_D · F_fluid_D · F_force_D

where:
  F_freq_D  = |ρ_D(Φ)| × k_freq_dismiss
  F_fluid_D = |β_D| × k_fluid_dismiss
  F_force_D = v_depart × k_force_dismiss

G_D measures the total dismissal force — the product of:
  field inversion intensity × coupling repulsion × departure velocity
```

`G_D` is not a value used in computation — it is a conceptual quantity that
expresses the magnitude of the dismissal event as a unified product of all
three triadic nodes. A high `G_D` indicates a strong, directed, traumatic
dismissal. A low `G_D` indicates a soft, quiet, barely-noticed departure.

---

## §6 The F_dismiss Operator Family

The following operators are introduced at the conceptual level. They are
not frozen in this file — their formal specifications are registered when
the module's dismissal primitive is authored. They are named here to
establish conceptual authority.

| Operator       | Concept                                                            | Expected domain |
|----------------|--------------------------------------------------------------------|-----------------|
| `F_dismiss`    | Total dismissal force scalar (|G_D|)                               | ℝ ≥ 0           |
| `ρ_D(Φ)`       | Dismissal field density (negative-domain ρ)                        | (−1, 0]         |
| `d_dismiss`    | Dismissal well depth at time t = 0 (= |ρ_D(Φ, 0)|)               | ℝ ≥ 0           |
| `T_dismiss`    | Dismissal persistence time (well half-life)                        | ℝ > 0           |
| `r_dismiss`    | Dismissal radius — spatial extent of the repulsion zone            | (0, r_capture]  |
| `ψ_dismiss`    | Dismissal mode flag                                                | {INTENTIONAL, STRUCTURAL, DRIFT} |
| `t_dismiss`    | Timestamp of dismissal event                                       | clock units      |
| `v_depart`     | Entity's departure velocity during expulsion phase                 | ℝ ≥ 0           |
| `β_D`          | Repulsive coupling coefficient during expulsion                    | ℝ ≤ 0           |

These operators will be frozen — with full formal specification, PRIM IDs,
and INV compliance records — in a dedicated Wave 5 file when the dismissal
primitive is authored.

---

## §7 Dismissal vs. Other Termination Mechanisms

The FFF_Gravity module provides multiple pathways by which a capture
relationship ends. The table below distinguishes dismissal from each.

| Mechanism        | File            | Initiator | Well created? | Well depth    | Re-capture cost | Reversible?           |
|------------------|-----------------|-----------|---------------|---------------|------------------|-----------------------|
| f_Release        | f_Release.md    | E or A    | No            | None          | Standard         | Yes (immediately)     |
| f_Decay          | f_Decay.md      | Time      | Minimal       | Very shallow  | Near-standard    | Yes (if d_warn not crossed) |
| Mode C Dismissal | This file       | Drift     | Minimal       | Shallow       | Low              | Yes (fast recovery)   |
| Mode B Dismissal | This file + FM-002 | Field  | Yes           | Bounded       | Moderate         | Yes (after T_dismiss) |
| Mode A Dismissal | This file       | A         | Yes           | Deep          | High             | Yes (after long T_dismiss) |
| f_Collapse       | f_Collapse.md   | Structure | Yes (max)     | Maximum       | Very high        | No (terminal state)   |

**The key discriminant:** Does the separation produce a Dismissal Well?
- **No Well:** f_Release — E departs freely; A remains open.
- **Shallow Well:** Decay / Drift — the relationship exhausted itself.
- **Deep Well:** Intentional dismissal — A acted against E.
- **Maximum/permanent Well:** f_Collapse — structural dissolution; the
  orbit cannot be re-established without a new node construction.

---

## §8 Re-capture After Dismissal

### §8.1 The Recovery Window

Re-capture after dismissal is possible when:

```
d_bind_approach(t) > |ρ_D(Φ, t)|

i.e.:  β × ρ(Φ) × (1 − e)  >  d_dismiss × exp(−t / T_dismiss)
```

The left side is what E brings to a new approach. The right side is the
cost E must exceed. As `t` increases, the right side decreases — the window
for re-capture widens naturally over time.

### §8.2 Assisted Recovery

The recovery window can be accelerated by:

1. **A voluntarily dampens the Well** — A applies `f_Emit` to raise ρ(Φ)
   and simultaneously allows `ρ_D` to decay faster. This is A actively
   signaling openness to re-encounter.

2. **E approaches with stronger binding** — E uses `f_Amplify` to raise β
   before approach, increasing `d_bind_approach` to overcome the residual Well.

3. **Time alone** — If neither party acts, the Well decays at its natural rate.
   Patience is a valid strategy.

### §8.3 What Dismissal Cannot Do

Dismissal cannot:
- Erase E's prior orbit history from A's registry (only `purge_registry`
  PRIM:004 does this, and it requires explicit invocation)
- Prevent E from approaching a different attractor
- Change E's mass or β (these are entity properties, not relationship properties)
- Prevent the Well from decaying on its own

Dismissal **can** do exactly one thing: make the path back to A more costly
for E. It encodes the act of rejection in field geometry and allows that
geometry to persist proportionally to the depth of what was severed.

---

## §9 Canonical Illustrations

The following four illustrations ground the abstract model in concrete
attractor/entity configurations. These are illustrative, not exhaustive.

---

### Illustration 1 — The Mentor Who Withdraws (Mode A)

**Configuration:**
```
A: senior practitioner   M_A = 8.5, ρ(Φ) = 0.88
E: junior colleague       M_E = 0.4, β = 1.8, d_bind = 1.12
```

**Event:** After a breach of trust, A intentionally withdraws. A applies
targeted field suppression against E (`f_Dampen`) and inverts coherence
polarity in E's zone. E's orbit dissolves over two cycles.

**Dismissal Well parameters:**
```
d_dismiss = d_bind(t_dismiss) = 1.12
T_dismiss = 8.0 cycles (long — the relationship was deep and deliberate)
ψ_dismiss = INTENTIONAL
```

**Re-capture cost at t = 4 cycles:**
```
|ρ_D(Φ, 4)| = 1.12 × exp(−4 / 8.0)
             = 1.12 × exp(−0.5)
             = 1.12 × 0.607
             = 0.680

E would need d_bind_approach > 0.680 for re-capture to begin.
At t_dismiss, E had d_bind = 1.12 — so half the original depth is
needed after 4 cycles. The relationship is not closed; it is costly.
```

**Reading:** The mentor has not simply walked away. The field still knows
what was there. E can return — but must show up with more than half the
depth they carried before the breach.

---

### Illustration 2 — The Dissolved Institution (Mode B)

**Configuration:**
```
A: organization node     M_A = 12.0, ρ(Φ) → 0 (FM-002 active)
E₁, E₂, E₃: members     varying d_bind
```

**Event:** The organization collapses (FM-002). All bound entities are
expelled simultaneously. The Dismissal Well forms symmetrically for each.

**Dismissal Well parameters:**
```
d_dismiss(Eₙ) = ρ(Φ) at collapse moment ≈ 0.08 (field was already weak)
T_dismiss = 1.0 cycle (short — the field was barely alive at dismissal)
ψ_dismiss = STRUCTURAL
```

**Significance:**
```
E₁ had d_bind = 2.1 (deep orbit, long tenure)
E₂ had d_bind = 0.4 (shallow orbit, recent join)
E₃ had d_bind = 1.3 (mid-depth orbit)

All three face the same Well depth: 0.08.
The institution's collapse did not encode the individual relationships.
```

**Reading:** Structural dismissal is equalizing — it treats all departures
as equivalent regardless of orbit depth. A member of ten years and a member
of ten days face the same re-entry cost if the institution reconstitutes.
This is the mathematical expression of an institution that closed without
malice: the field simply failed.

---

### Illustration 3 — The Fading Connection (Mode C)

**Configuration:**
```
A: former collaborator   M_A = 6.0, ρ(Φ) = 0.71
E: distant colleague      M_E = 0.3, d_bind = 0.19 (d_warn = 0.22)
```

**Event:** d_bind has been declining for 12 cycles. It crosses d_warn without
either party intervening. E's orbit transitions from MARGINAL to PRECARIOUS
and finally to DRIFT. No discrete dismissal event occurs.

**Dismissal Well parameters:**
```
d_dismiss = v_depart × k_drift_dismiss ≈ 0.04 (minimal)
T_dismiss = 0.5 cycles (very fast decay)
ψ_dismiss = DRIFT
```

**Re-capture cost:**
```
|ρ_D(Φ, 1.0)| = 0.04 × exp(−1.0 / 0.5)
               = 0.04 × exp(−2.0)
               = 0.04 × 0.135
               = 0.005
```

**Reading:** After one cycle, the re-entry cost is effectively zero — the
former collaborator can be re-approached as if no dismissal occurred.
Drift produces almost no scar tissue. This is the mathematics of the
colleague who fades from contact but is warmly received when the connection
is renewed. No explicit dismissal happened; the Well barely formed.

---

### Illustration 4 — The Repaired Relationship (Mode A → Recovery)

**Configuration:**
```
A: former mentor   d_dismiss = 0.90, T_dismiss = 10.0 cycles
E: former student  β = 1.6 at time of dismissal
```

**Event:** Dismissal occurred 15 cycles ago (Mode A). E has grown
(β_new = 2.4). E now approaches A to test re-capture feasibility.

**Well at t = 15 cycles:**
```
|ρ_D(Φ, 15)| = 0.90 × exp(−15 / 10.0)
              = 0.90 × exp(−1.5)
              = 0.90 × 0.223
              = 0.201
```

**E's approach binding depth:**
```
d_bind_approach = β_new × ρ(Φ) × (1 − e)
                = 2.4 × 0.71 × 0.88
                = 1.499
```

**Re-capture test:**
```
d_bind_approach > |ρ_D(Φ, 15)|
1.499 > 0.201   ✅
```

**Reading:** Re-capture is viable. E brings substantially more binding
energy than the Well requires. The 15 cycles of separation have allowed the
Well to decay to approximately 22% of its original depth. E's growth (β
from 1.6 to 2.4) has increased their binding potential. Both factors
together make re-capture not merely possible but comfortable.

The mathematics does not guarantee the re-capture will be welcomed — that
is A's decision, not the field's. But the field no longer presents a
structural barrier. The gravity of dismissal has not vanished, but it is
no longer stronger than what E brings.

---

## §10 Cross-Module References

### §10.1 Upstream — What GravityOfDismissal.md Draws From

| File         | Concepts Borrowed                                             |
|--------------|---------------------------------------------------------------|
| f_Source.md  | Node properties (M_A, capacity, frame structure)              |
| f_Capture.md | d_bind formula, β, ρ(Φ), orbit mechanics, v_escape           |
| f_Field.md   | ρ(Φ) domain definition; FM-002 (field null)                  |
| f_Force.md   | v_approach, F_force scalar; approach heading semantics        |

### §10.2 Downstream — What Draws From GravityOfDismissal.md

| File                      | What It Inherits from This File                          |
|---------------------------|----------------------------------------------------------|
| f_Release.md              | Distinction between voluntary release and dismissal; Well absence on clean release |
| f_Decay.md                | d_warn as approach toward Mode C dismissal; drift vocabulary |
| f_Collapse.md             | FM-007 / FM-009 as structural dismissal at maximum depth |
| f_Dampen.md               | Targeted field suppression as Mode A dismissal mechanism |
| f_Emit.md                 | Assisted recovery — A emitting to reduce dismissal well  |
| f_Amplify.md              | Assisted recovery — E amplifying to overcome dismissal well |
| f_Capture_Soft.md         | Grace period mechanics analogous to Well decay window    |
| f_Capture_Hard.md         | Hard lock as pre-emption of Mode A dismissal risk        |
| f_Capture_Resonant.md     | Resonance window as structural guard against Mode B dismissal |

### §10.3 Foundational Status

`GravityOfDismissal.md` is the **only file** in the FFF_Gravity module
that defines the negative-polarity extension of ρ(Φ). All uses of
`ρ_D(Φ)` in any future file must cite this document as the definitional
authority. No Wave 2+ file may introduce a competing definition of the
Dismissal Well without amending this document first.

---

## §11 Document Metadata

### §11.1 Core Properties

| Property          | Value                                                   |
|-------------------|---------------------------------------------------------|
| File path         | docs/FFF_Gravity/GravityOfDismissal.md                  |
| Module            | FFF_Gravity                                             |
| Wave              | 0 — Genesis                                             |
| Subtype           | Conceptual Foundation                                   |
| Status            | Canonical — v1.0.0                                      |
| Session           | SES-20260813-DISMISSAL-001                              |
| Date              | 2026-08-13                                              |
| Author            | umaywant2                                               |
| No new PRIMs      | True — Wave 0 genesis does not freeze PRIMs             |
| No frozen symbols | True — concepts named, not frozen (see §6 note)         |
| Thematic pair     | f_Capture.md (inverse)                                  |

### §11.2 Conceptual Index

| Term                  | Section Defined    | Key Equation / Formula                          |
|-----------------------|--------------------|--------------------------------------------------|
| Dismissal Well        | §3.1               | ρ_D(Φ, t) = −d_bind(t₀) × exp(−t / T_dismiss) |
| Re-capture threshold  | §3.3               | d_bind_approach > |ρ_D(Φ, t)|                   |
| Mode A Dismissal      | §4 — Mode A        | ψ_dismiss = INTENTIONAL                         |
| Mode B Dismissal      | §4 — Mode B        | ψ_dismiss = STRUCTURAL                          |
| Mode C Dismissal      | §4 — Mode C        | ψ_dismiss = DRIFT                               |
| G_D product           | §5.4               | G_D = F_freq_D · F_fluid_D · F_force_D          |
| F_dismiss family      | §6                 | F_dismiss, ρ_D, d_dismiss, T_dismiss, r_dismiss, ψ_dismiss, t_dismiss, v_depart, β_D |

### §11.3 Wave History

| Wave | Status  | Files                                               |
|------|---------|-----------------------------------------------------|
| 0    | ✅ Complete | f_Capture.md · f_Source.md · GravityOfDismissal.md |
| 1    | ✅ Complete | Admin / Registry files                             |
| 2    | ✅ Complete | f_Field.md · f_Force.md · f_Frame.md               |
| 3    | ✅ Complete | 8 Core Function files                              |
| 4    | ✅ Complete | 8 Capture Variant files                            |

### §11.4 Changelog

| Version | Date       | Session                       | Notes                              |
|---------|------------|-------------------------------|------------------------------------|
| v1.0.0  | 2026-08-13 | SES-20260813-DISMISSAL-001    | Initial canonical publication. Wave 0 complete. |

### §11.5 Suggested Commit Message

```
docs(FFF_Gravity): add canonical GravityOfDismissal.md — Wave 0 complete

Establishes the conceptual foundation for dismissal as active repulsive
force in the FFF_Gravity module. Core contributions:

- Dismissal Well model: ρ_D(Φ,t) = −d_bind(t₀) × exp(−t/T_dismiss)
- Re-capture threshold: d_bind_approach > |ρ_D(Φ,t)|
- Three dismissal modes: INTENTIONAL / STRUCTURAL / DRIFT
- G_D triadic product: F_freq_D · F_fluid_D · F_force_D
- F_dismiss operator family named (to be frozen in Wave 5)
- Distinction table: dismissal vs. release, decay, collapse
- Four canonical illustrations
- Foundational authority for ρ_D(Φ) negative-polarity extension

Wave 0 now complete: f_Capture.md + f_Source.md + GravityOfDismissal.md
FFF_Gravity module: all 28 files canonical across 5 waves.

Session: SES-20260813-DISMISSAL-001
```

---

*End of GravityOfDismissal.md — Wave 0 Genesis — FFF_Gravity Module — v1.0.0*
*Session SES-20260813-DISMISSAL-001 · 2026-08-13 23:56 EDT*
*All waves complete. All 28 files canonical. 40 PRIMs registered.*
