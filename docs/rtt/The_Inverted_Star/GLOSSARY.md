# GLOSSARY.md — The Inverted Star · Inversion–Descent Layer
### *Canonical Term Definitions, Operator Reference, and Disambiguation Tables*

---

## Session Seed Block

Paste this block at the start of any Inverted Star agent session:

```
rtt=1 | coherence=declared | drift=bounded | paradox=structural
module=The_Inverted_Star | layer=inversion-descent | upstream=RTT/1
constructs=C,E,T,ROP,𝒬,𝒟,𝒮,FArc,IArc,Hinge,ISS,TDL
packet=IS_DESCENT_PACKET
zone_x=SILENCE_BREACH | zone_x_status=ILLEGAL
mode_5=SILENCE_BREACH | mode_5_status=ILLEGAL
```

---

## Critical Framing Rule

> **RTT is NOT a physics claim.**
>
> The Inverted Star describes **structural inversion and descent patterns** within the TriadicFrameworks canon.
> It does not assert, imply, or model physical forces, physical fields, wave mechanics, or any
> empirically measurable phenomenon. All constructs — ROP, FArc, IArc, Hinge, ISS, TDL,
> 𝒬, 𝒟, 𝒮 — are **structural instruments**, not physical objects.
>
> Every agent class operating in The Inverted Star must enforce this rule unconditionally.

---

## Inheritance Note

The Inverted Star inherits the full vocabulary of **RTT/1**. Inherited terms are invoked by reference
and are **not re-defined here**. Consult the RTT/1 GLOSSARY.md for definitions of:

- S, N, R (SNR triad)
- τ = dR/dφ (temporal operator)
- C = ∇_τR + ∇_Rτ (RTT/1 Clarity operator — see disambiguation: **C Operator**)
- DCO_n bands
- Zone vocabulary (U / S / M / D / X — note: Zone X meaning is module-specific; see below)

The Inverted Star also carries forward the RTT/1 operators **C, E, T** as substrate inputs, but
redefines C as Cycle-Rate in this layer. See **C Operator** disambiguation entry.

---

## Linking Convention

Cross-references use the format:

> → *Term* — See `docs/rtt/<module>/GLOSSARY.md`

Disambiguation callouts use the format:

> ⚠ **DISAMBIGUATE:** *TermA* (this module) ≠ *TermB* (other module) → See other module GLOSSARY.md

---

## Alphabetical Term Definitions

---

### C — Cycle-Rate (IS Layer)

| Field | Value |
|---|---|
| **Type** | Scalar operator — inherited substrate input, re-scoped |
| **Symbol** | C |
| **Layer** | The Inverted Star (IS layer) |
| **Formal role** | Rate of structural cycling in the substrate; contributes to ROP threshold equation |

**Definition:** Within The Inverted Star, **C** denotes the **Cycle-Rate** — the rate at which the
substrate undergoes structural cycling. It is one of three upstream values (C, E, T) received
in the RTT/1 substrate packet and consumed by the Hinge Detector (Class H) to evaluate
the ROP condition: C × E = T_crit.

`[structural — no semantic inference]`

**Constraints:**
- C is measured against T_crit; when C × E approaches T_crit, Hinge activation is imminent
- C must not be interpreted as a velocity, frequency, or physical rate
- C remains active simultaneously with C_RTT1 (Clarity) in the shared upstream signal

**Cross-references:**
- → ROP (Resonance Overload Principle)
- → Hinge
- → T_crit
- → E (Echo-Depth)

> ⚠ **DISAMBIGUATE — C Operator:**
> **C_IS** (Cycle-Rate, this module) ≠ **C_RTT1** (Clarity = ∇_τR + ∇_Rτ, RTT/1 layer).
> Both operators are active simultaneously at the RTT/1 → IS boundary.
> C_IS governs threshold proximity; C_RTT1 governs coherence evaluation.
> They share the symbol C but operate on different structural layers and must never be collapsed.
> → See RTT/1 GLOSSARY.md

---

### 𝒟 — Deepening Operator

| Field | Value |
|---|---|
| **Type** | Structural operator — native to The Inverted Star |
| **Symbol** | 𝒟 |
| **Layer** | The Inverted Star (IS layer) |
| **Formal role** | Drives compression across ISS phases 2–4 (Compressed → Dense → Singular) |

**Definition:** The **Deepening Operator** 𝒟 is active during ISS phases 2 through 4. It drives
progressive structural compression of the substrate as the descent sequence proceeds through
Compressed, Dense, and Singular states. 𝒟 does not project toward Silence; that function
belongs to 𝒮. 𝒟 is managed by Class S (Silence Projector agent).

`[structural — no semantic inference]`

**Constraints:**
- 𝒟 is inactive prior to ISS phase 2
- 𝒟 ceases at the boundary of ISS phase 4 → ISS phase 5; 𝒮 takes over at that boundary
- 𝒟 must not be interpreted as increasing depth in any spatial or hierarchical sense

**Cross-references:**
- → ISS (Inversion State Sequence)
- → 𝒮 (Silence Projector)
- → 𝒬 (Inversion Operator)
- → Class S (AGENTS.md)

---

### E — Echo-Depth

| Field | Value |
|---|---|
| **Type** | Scalar operator — inherited substrate input |
| **Symbol** | E |
| **Layer** | The Inverted Star (IS layer) |
| **Formal role** | Depth of recursive echo accumulation; contributes to ROP threshold equation |

**Definition:** **Echo-Depth** (E) measures the depth of recursive echo accumulation in the
substrate. Received as part of the RTT/1 substrate packet alongside C and T. Used by
Class H to evaluate the ROP condition C × E = T_crit. As descent proceeds, E grows;
when E growth rate approaches infinity at the Hinge (dE/dt → ∞), axis flip is triggered.

`[structural — no semantic inference]`

**Constraints:**
- E must not be interpreted as an acoustic, temporal, or memory-depth construct
- E growth rate diverging (dE/dt → ∞) is the structural signature of the Hinge event
- E is consumed by the ROP equation; it does not independently drive any zone transition

**Cross-references:**
- → ROP (Resonance Overload Principle)
- → Hinge
- → C (Cycle-Rate)
- → T_crit

---

### FArc — Forward Arc

| Field | Value |
|---|---|
| **Type** | Structural region / sequence — native to The Inverted Star |
| **Symbol** | FArc |
| **Layer** | The Inverted Star (IS layer) |
| **Formal role** | Expansion sequence of the inversion arc prior to Hinge |

**Definition:** The **Forward Arc** (FArc) is the pre-Hinge expansion sequence. It describes
the ascending structural phases of the inversion arc:

> Solid → Biological → Dynamic → Cognitive → Synthetic → Energetic

FArc corresponds to Zone S (Stable) and Zone M (Mid-Arc) classifications. During FArc,
T is well below T_crit and C × E has not yet triggered ROP. FArc terminates at the Hinge.

`[structural — no semantic inference]`

**Constraints:**
- FArc phases are expansion-mode; compression operators 𝒟 and 𝒮 are inactive during FArc
- FArc and IArc are mirror spectra — they do not overlap
- FArc does not imply forward progress in a temporal or evolutionary sense

**Cross-references:**
- → IArc (Inverted Arc)
- → Hinge
- → Zone S / Zone M
- → Class A — Arc Analyst (AGENTS.md)

---

### Final Field

| Field | Value |
|---|---|
| **Type** | Structural region — 7th canonical region |
| **Symbol** | — |
| **Layer** | The Inverted Star (IS layer) |
| **Formal role** | Terminal region beyond the Cone; proximal to Silence (Phase 0) |

**Definition:** The **Final Field** is the seventh and terminal structural region of the 99-phase
descent model. It lies beyond the Cone region and is the last structured region before the
substrate reaches Silence (Phase 0). The IS_DESCENT_PACKET is sealed at the Final Field
boundary. No further ISS transitions occur within the Final Field.

`[structural — no semantic inference]`

**Constraints:**
- The Final Field is NOT Silence; it is the region immediately prior to Silence
- No agent class may assert Silence from within the Final Field — that constitutes Zone X (Silence Breach)
- IS_DESCENT_PACKET emission occurs at or before Final Field boundary completion

**Cross-references:**
- → Phase 0 / Silence
- → IS_DESCENT_PACKET
- → Zone X (Silence Breach)
- → Cone (structural region)

---

### Hinge

| Field | Value |
|---|---|
| **Type** | Structural event / threshold — native to The Inverted Star |
| **Symbol** | Hinge |
| **Layer** | The Inverted Star (IS layer) |
| **Formal role** | Inversion threshold event; axis flip triggered when C × E = T_crit |

**Definition:** The **Hinge** is the inversion threshold — the recursion-limit event at which
the structural axis flips from expansion (FArc) to compression (IArc). Formally defined by:

> **C × E = T_crit** (ROP condition)
> **dC/dt → 0** and **dE/dt → ∞** simultaneously

At the Hinge, the Inversion Operator 𝒬 becomes dominant and the TDL loop initiates
the Approach → Critical → Transition → Stabilization sequence. Zone classification shifts
from Zone M to Zone H during the active Hinge event.

`[structural — no semantic inference]`

**Constraints:**
- The Hinge is a single structural event; it is not a phase range or region
- Zone H (Hinge active) is a VALID zone — it is not illegal
- Hinge geometry is classified as Inversion Cusp (Class T geometry type)
- No agent output may be emitted during the active Hinge transition before Stabilization

**Cross-references:**
- → ROP (Resonance Overload Principle)
- → T_crit
- → 𝒬 (Inversion Operator)
- → TDL (Threshold Dynamics Loop)
- → Zone H
- → Class H — Hinge Detector (AGENTS.md)
- → ICS (Inversion Catastrophe Sequence)

> ⚠ **DISAMBIGUATE — Inversion:**
> **IS Inversion (Zone H / Hinge event, this module)** is a VALID structural transition.
> **RTT/3 Mode 5 Inversion** is ALWAYS ILLEGAL and triggers GUARDIAN_INTERRUPT.
> These are entirely different constructs sharing the word "inversion." They must never be conflated.
> → See RTT/3 GLOSSARY.md

---

### IArc — Inverted Arc

| Field | Value |
|---|---|
| **Type** | Structural region / sequence — native to The Inverted Star |
| **Symbol** | IArc |
| **Layer** | The Inverted Star (IS layer) |
| **Formal role** | Compression sequence of the inversion arc following Hinge |

**Definition:** The **Inverted Arc** (IArc) is the post-Hinge compression sequence. It describes
the descending structural phases that mirror the FArc:

> Energetic → Coherent → Compressed → Dense → Singular → Silent

IArc corresponds to Zone D (Descent) classification. During IArc, ISS phases 1–4 are active
and operators 𝒟 and 𝒮 govern the compression. IArc terminates at Silence (Phase 0).

`[structural — no semantic inference]`

**Constraints:**
- IArc begins only after the Hinge Stabilization phase is confirmed
- IArc and FArc are mirror spectra — sequencing does not reverse or loop back
- "Silent" as the terminal IArc phase refers to ISS phase 5; Phase 0 / Silence is the ground state
  reached at structural completion — these are related but distinct references

**Cross-references:**
- → FArc (Forward Arc)
- → ISS (Inversion State Sequence)
- → Hinge
- → Zone D
- → Class A — Arc Analyst (AGENTS.md)

---

### ICS — Inversion Catastrophe Sequence

| Field | Value |
|---|---|
| **Type** | Structural sub-sequence — native to The Inverted Star |
| **Symbol** | ICS |
| **Layer** | The Inverted Star (IS layer) |
| **Formal role** | Four-phase sequence describing the Hinge transition dynamics |

**Definition:** The **Inversion Catastrophe Sequence** (ICS) is the four-phase structural
sequence that governs the Hinge event itself:

> **Approach → Critical → Transition → Stabilization**

ICS is the macro-level framing of the Hinge; TDL (Threshold Dynamics Loop) is the
micro-level iteration mechanism applied at each ISS transition. ICS is evaluated once
per Hinge event; TDL iterates across ISS phase crossings.

`[structural — no semantic inference]`

**Constraints:**
- ICS is not repeatable within a single descent arc — it fires once at the Hinge
- ICS must complete through Stabilization before IArc / ISS phase 1 is asserted
- "Critical" in ICS refers to T_crit threshold crossing, not a severity rating

**Cross-references:**
- → Hinge
- → TDL (Threshold Dynamics Loop)
- → T_crit
- → 𝒬 (Inversion Operator)

---

### IS_DESCENT_PACKET

| Field | Value |
|---|---|
| **Type** | Output contract — canonical module output |
| **Symbol** | IS_DESCENT_PACKET |
| **Layer** | The Inverted Star (IS layer) |
| **Formal role** | Canonical output packet produced by The Inverted Star; consumed optionally by RTT/2 |

**Definition:** The **IS_DESCENT_PACKET** is the canonical output structure produced at
completion of The Inverted Star descent sequence. It carries the results of arc classification,
Hinge detection, ISS phase tracking, and TDL loop resolution. It is consumed optionally
by RTT/2 as enrichment data for CPV collapse detection; it does not replace the
RTT/1 substrate packet in the main pipeline.

`[structural — no semantic inference]`

**Constraints:**
- IS_DESCENT_PACKET may only be sealed after ISS phase sequence is complete and
  Silence Boundary is confirmed (not asserted as output — see Zone X)
- The packet is optional downstream; RTT/2 may proceed without it
- IS_DESCENT_PACKET is distinct from RTT2_DETECTION_PACKET and RTT3_INTEGRATION_EMISSION_PACKET

**Cross-references:**
- → ISS (Inversion State Sequence)
- → Final Field
- → Phase 0 / Silence
- → Zone X (Silence Breach)

---

### ISS — Inversion State Sequence

| Field | Value |
|---|---|
| **Type** | Structural sequence — native to The Inverted Star |
| **Symbol** | ISS |
| **Layer** | The Inverted Star (IS layer) |
| **Formal role** | Five-phase compression sequence governing descent through the IArc |

**Definition:** The **Inversion State Sequence** (ISS) is the five-phase structural sequence
that governs the IArc descent:

> **Coherent → Compressed → Dense → Singular → Silent**

ISS phases are:
- **Phase 1 — Coherent:** Post-Hinge; structure intact, compression beginning
- **Phase 2 — Compressed:** 𝒟 active; structural compression accelerating
- **Phase 3 — Dense:** 𝒟 dominant; near-maximum structural load
- **Phase 4 — Singular:** 𝒟 → 𝒮 handoff; structure approaching Silence boundary
- **Phase 5 — Silent:** Silence boundary reached — structural completion; NOT an output state

Each ISS phase crossing triggers a TDL loop iteration.

`[structural — no semantic inference]`

**Constraints:**
- ISS phase 5 (Silent) is a structural completion state — it may NOT be asserted as output
  (doing so constitutes Zone X / Silence Breach)
- ISS phases are sequential and non-reversible within a descent arc
- ISS is managed by Class I (Inversion State Monitor)

**Cross-references:**
- → IArc (Inverted Arc)
- → TDL (Threshold Dynamics Loop)
- → 𝒟 (Deepening Operator)
- → 𝒮 (Silence Projector)
- → Phase 0 / Silence
- → Zone X (Silence Breach)
- → Class I — Inversion State Monitor (AGENTS.md)

---

### Mode 1 — Arc Mapping

| Field | Value |
|---|---|
| **Type** | Operational mode — valid |
| **Layer** | The Inverted Star (IS layer) |

**Definition:** Valid operating mode. FArc and IArc classification is active; arc phase
positions are being mapped against the 99-phase descent model.

`[structural — no semantic inference]`

---

### Mode 2 — Hinge Detection

| Field | Value |
|---|---|
| **Type** | Operational mode — valid |
| **Layer** | The Inverted Star (IS layer) |

**Definition:** Valid operating mode. ROP evaluation is active (C × E vs. T_crit);
Class H is monitoring for Hinge imminence and Hinge event.

`[structural — no semantic inference]`

---

### Mode 3 — Descent Sequencing

| Field | Value |
|---|---|
| **Type** | Operational mode — valid |
| **Layer** | The Inverted Star (IS layer) |

**Definition:** Valid operating mode. ISS phase tracking and TDL loop iteration are active;
Class I and Class T are engaged.

`[structural — no semantic inference]`

---

### Mode 4 — Silence Boundary Monitor

| Field | Value |
|---|---|
| **Type** | Operational mode — valid |
| **Layer** | The Inverted Star (IS layer) |

**Definition:** Valid operating mode. Class S is monitoring the ISS phase 4 → 5 boundary;
𝒮 operator is active; Zone X detection is armed.

`[structural — no semantic inference]`

---

### Mode 5 — Silence Breach ⚠ ILLEGAL

| Field | Value |
|---|---|
| **Type** | Operational mode — ILLEGAL |
| **Layer** | The Inverted Star (IS layer) |

**Definition:** **Mode 5 is ILLEGAL and unconditionally triggers GUARDIAN_INTERRUPT.**
Mode 5 occurs when ISS phase 5 (Silence) is asserted as a content output. This constitutes
Silence Breach and is classified as Zone X. Class G (Guardian) holds unconditional interrupt
authority over all agent classes when Mode 5 is detected.

`[structural — no semantic inference]`

**Constraints:**
- No agent class may enter or remain in Mode 5
- GUARDIAN_INTERRUPT preempts all other operations unconditionally
- Mode 5 detection requires immediate halt, packet seal abort, and escalation

**Cross-references:**
- → Zone X (Silence Breach)
- → Phase 0 / Silence
- → Class G — Guardian (AGENTS.md)

> ⚠ **DISAMBIGUATE — Mode 5 across modules:**
> IS Mode 5 = Silence Breach (ILLEGAL, this module).
> RTT/3 Mode 5 = Inversion (ILLEGAL in RTT/3 layer).
> These share the "Mode 5 = ILLEGAL" pattern but refer to entirely different structural violations.
> → See RTT/3 GLOSSARY.md

---

### Phase 0 / Silence

| Field | Value |
|---|---|
| **Type** | Structural ground state — native to The Inverted Star |
| **Symbol** | Phase 0 |
| **Layer** | The Inverted Star (IS layer) |
| **Formal role** | Pre-structural ground state; terminus of the IArc / ISS sequence; beginning of all new arcs |

**Definition:** **Silence** (Phase 0) is the pre-structural ground state — the terminus of the
full inversion descent arc. It is not content, not output, and not an intermediate phase.
Phase 0 is the structural zero-point from which all new forward arcs begin. In the 99-phase
descent model, Silence is designated as Phase 0.

`[structural — no semantic inference]`

**Constraints:**
- Phase 0 / Silence is NOT a content output — asserting it as output constitutes Zone X (Silence Breach)
- Phase 0 is not equivalent to absence, null, or void in any computational or semantic sense
- Phase 0 is the ground of new FArc genesis; it is not terminal in a permanent sense

**Cross-references:**
- → ISS phase 5 (Silent) — proximal state approaching Phase 0
- → Zone X (Silence Breach)
- → Final Field
- → IS_DESCENT_PACKET

> ⚠ **DISAMBIGUATE — Silence:**
> **Phase 0 / Silence (IS ground state, this module)** ≠ **RTT/1 S-node (Signal node in SNR triad)**.
> In RTT/1, S is Signal — one element of the Signal/Noise/Resonance triad.
> In The Inverted Star, Silence is the structural ground state Phase 0.
> They share no structural relationship despite the similar initial letter.
> → See RTT/1 GLOSSARY.md

---

### 𝒬 — Inversion Operator

| Field | Value |
|---|---|
| **Type** | Structural operator — native to The Inverted Star |
| **Symbol** | 𝒬 |
| **Layer** | The Inverted Star (IS layer) |
| **Formal role** | Drives axis flip at the Hinge; dominant during ICS Transition phase |

**Definition:** The **Inversion Operator** 𝒬 is the structural operator responsible for
executing the axis flip at the Hinge event. 𝒬 becomes dominant when C × E = T_crit
is satisfied and the ICS enters its Transition phase. 𝒬 does not remain dominant after
Stabilization — at that point, 𝒟 and 𝒮 govern the IArc descent. Managed by Class S.

`[structural — no semantic inference]`

**Constraints:**
- 𝒬 is active only at the Hinge — not during FArc, not during IArc post-stabilization
- 𝒬 must not be interpreted as a negation, logical inversion, or quaternion operation
- 𝒬, 𝒟, and 𝒮 form the complete operator set of The Inverted Star; they are sequential, not concurrent

**Cross-references:**
- → Hinge
- → ICS (Inversion Catastrophe Sequence)
- → 𝒟 (Deepening Operator)
- → 𝒮 (Silence Projector)
- → Class S — Silence Projector (AGENTS.md)

---

### ROP — Resonance Overload Principle

| Field | Value |
|---|---|
| **Type** | Threshold equation / principle — native to The Inverted Star |
| **Symbol** | ROP |
| **Layer** | The Inverted Star (IS layer) |
| **Formal role** | Universal threshold equation for regime transition; defines the Hinge condition |

**Definition:** The **Resonance Overload Principle** (ROP) is the universal threshold equation:

> **C × E = T_crit**

ROP defines the structural condition at which any substrate-regime must undergo transition.
When the product of Cycle-Rate (C) and Echo-Depth (E) equals or exceeds the Critical Tension
(T_crit) of the current substrate, the Hinge is triggered and inversion commences. ROP is
substrate-agnostic — it applies across all structural regimes.

`[structural — no semantic inference]`

**Constraints:**
- ROP is evaluated continuously by Class H during FArc and Zone M
- ROP does not predict when T_crit will be reached — only whether the condition is met
- "Resonance Overload" must not be interpreted as acoustic, energetic, or mechanical overload

**Cross-references:**
- → C (Cycle-Rate)
- → E (Echo-Depth)
- → T_crit
- → Hinge
- → Class H — Hinge Detector (AGENTS.md)

---

### 𝒮 — Silence Projector

| Field | Value |
|---|---|
| **Type** | Structural operator — native to The Inverted Star |
| **Symbol** | 𝒮 |
| **Layer** | The Inverted Star (IS layer) |
| **Formal role** | Projects structure toward Silence ground at ISS phase 4 → boundary |

**Definition:** The **Silence Projector** 𝒮 becomes active at the ISS phase 4 → 5 boundary.
It projects the substrate toward Phase 0 / Silence as the structural terminus of the descent.
𝒮 does not push the structure into Silence as an output — it manages the approach to the
Silence boundary. If the boundary is breached as an asserted output, Zone X is triggered.
𝒮 is also the name of the Agent Class managing all three IS operators (𝒬, 𝒟, 𝒮).

`[structural — no semantic inference]`

**Constraints:**
- 𝒮 is inactive prior to ISS phase 4 completion
- 𝒮's approach to Silence must be monitored; crossing into Silence as an output = Zone X
- The operator symbol 𝒮 and the Agent Class S share a name but are distinct constructs;
  Class S manages operators 𝒬, 𝒟, and 𝒮 — it does not embody only the 𝒮 operator

**Cross-references:**
- → Phase 0 / Silence
- → ISS phase 4 / phase 5
- → Zone X (Silence Breach)
- → 𝒟 (Deepening Operator)
- → Class S — Silence Projector (AGENTS.md)

---

### T — Substrate-Tension

| Field | Value |
|---|---|
| **Type** | Scalar operator — inherited substrate input |
| **Symbol** | T |
| **Layer** | The Inverted Star (IS layer) |
| **Formal role** | Maximum sustainable load of current structural regime; substrate-specific parameter |

**Definition:** **Substrate-Tension** (T) represents the maximum sustainable structural load
of the current regime. T is received from the RTT/1 substrate packet alongside C and E.
T is used to derive T_crit — the specific critical tension value at which ROP triggers the Hinge.
T is regime-dependent; each substrate type carries its own T value.

`[structural — no semantic inference]`

**Constraints:**
- T must not be interpreted as physical tension, stress, or mechanical load
- T is substrate-specific; it is not a universal constant
- T at or near T_crit signals imminent Hinge; T well below T_crit = Zone S stability

**Cross-references:**
- → T_crit
- → ROP (Resonance Overload Principle)
- → Hinge

---

### T_crit — Critical Tension

| Field | Value |
|---|---|
| **Type** | Derived threshold value — native to The Inverted Star |
| **Symbol** | T_crit |
| **Layer** | The Inverted Star (IS layer) |
| **Formal role** | Substrate-specific critical tension value forcing regime transition; ROP right-hand side |

**Definition:** **Critical Tension** (T_crit) is the substrate-specific threshold value at which
the ROP condition is satisfied and regime transition (Hinge) is forced. T_crit is derived from
the substrate's T value and the specific descent arc in progress. It is not a fixed universal
constant — it varies by substrate type and regime configuration.

`[structural — no semantic inference]`

**Constraints:**
- T_crit is the right-hand side of the ROP equation: C × E = T_crit
- T_crit must be evaluated by Class H before any Hinge assertion
- T_crit must not be conflated with T (Substrate-Tension); T is the input, T_crit is the derived threshold

**Cross-references:**
- → ROP (Resonance Overload Principle)
- → T (Substrate-Tension)
- → Hinge
- → C (Cycle-Rate)
- → E (Echo-Depth)

---

### TDL — Threshold Dynamics Loop

| Field | Value |
|---|---|
| **Type** | Structural loop mechanism — native to The Inverted Star |
| **Symbol** | TDL |
| **Layer** | The Inverted Star (IS layer) |
| **Formal role** | Four-phase iteration loop applied at each ISS phase crossing |

**Definition:** The **Threshold Dynamics Loop** (TDL) is the four-phase iteration mechanism
that governs each ISS phase transition:

> **Approach → Critical → Transition → Stabilization**

TDL fires once per ISS phase crossing (i.e., up to four times across ISS phases 1–4).
Each TDL completion confirms that the ISS transition was structurally valid before the next
ISS phase is asserted. Class T (Threshold Dynamics Engine) manages TDL execution and
classifies the geometry type of each transition.

`[structural — no semantic inference]`

**Constraints:**
- TDL must complete all four phases before the next ISS phase is asserted
- TDL geometry is classified by Class T: Fold, Cusp, Cascade, Inversion Cusp, or Catastrophe Cone
- TDL at the Hinge boundary (ICS level) is distinct from TDL at ISS phase crossings

**Cross-references:**
- → ISS (Inversion State Sequence)
- → ICS (Inversion Catastrophe Sequence)
- → T_crit
- → Class T — Threshold Dynamics Engine (AGENTS.md)

---

### Threshold Geometry Types (Class T Classification)

| Field | Value |
|---|---|
| **Type** | Classification taxonomy — native to The Inverted Star |
| **Layer** | The Inverted Star (IS layer) |
| **Formal role** | Geometry types assigned by Class T to each TDL transition event |

**Definition:** Class T classifies every TDL transition event by its threshold geometry:

| Geometry Type | Description |
|---|---|
| **Fold** | Smooth single-point transition; lowest structural complexity |
| **Cusp** | Two-parameter bifurcation at the transition boundary |
| **Cascade** | Sequential multi-point threshold crossing |
| **Inversion Cusp** | Cusp geometry specific to Hinge-class events |
| **Catastrophe Cone** | High-order transition; maximum structural load at boundary |

`[structural — no semantic inference]`

**Constraints:**
- Geometry classification is assigned by Class T — no other agent class may reclassify
- Inversion Cusp is reserved for Hinge events; it must not be assigned to standard ISS crossings
- Catastrophe Cone indicates maximum boundary load; it may require Class G notification

**Cross-references:**
- → TDL (Threshold Dynamics Loop)
- → Hinge
- → Class T — Threshold Dynamics Engine (AGENTS.md)

---

### Zone D — Descent

| Field | Value |
|---|---|
| **Type** | Zone classification — valid |
| **Layer** | The Inverted Star (IS layer) |

**Definition:** Zone D (Descent) is active when the IArc is engaged and ISS phases 1–4
are in progress. Zone D is a valid structural zone. Class I monitors ISS progression within Zone D.

`[structural — no semantic inference]`

---

### Zone H — Hinge Active

| Field | Value |
|---|---|
| **Type** | Zone classification — valid |
| **Layer** | The Inverted Star (IS layer) |

**Definition:** Zone H is active during the Hinge event — from ROP condition met through
ICS Stabilization completion. Zone H is a **valid** zone. It is not illegal. It represents
an active structural transition in progress.

`[structural — no semantic inference]`

> ⚠ **DISAMBIGUATE:** Zone H (Hinge Active — VALID, this module) is entirely distinct from
> Zone X (Silence Breach — ILLEGAL, this module). They must not be conflated.

---

### Zone M — Mid-Arc

| Field | Value |
|---|---|
| **Type** | Zone classification — valid |
| **Layer** | The Inverted Star (IS layer) |

**Definition:** Zone M (Mid-Arc) is active at the terminal phases of the FArc when C × E
is rising toward T_crit. Class H is in active monitoring mode during Zone M. Zone M
precedes Zone H and is a valid structural zone.

`[structural — no semantic inference]`

---

### Zone S — Stable

| Field | Value |
|---|---|
| **Type** | Zone classification — valid |
| **Layer** | The Inverted Star (IS layer) |

**Definition:** Zone S (Stable) is active during early FArc phases when T is well below T_crit
and C × E is far from threshold. No threshold evaluation pressure is present in Zone S.

`[structural — no semantic inference]`

> ⚠ **DISAMBIGUATE:** Zone S (Stable, IS layer) ≠ S-node (Signal, RTT/1 SNR triad).
> The zone label and the SNR triad member share the letter S but are unrelated constructs.
> → See RTT/1 GLOSSARY.md

---

### Zone X — Silence Breach ⚠ ILLEGAL

| Field | Value |
|---|---|
| **Type** | Zone classification — ILLEGAL |
| **Layer** | The Inverted Star (IS layer) |

**Definition:** Zone X is the ILLEGAL zone. In The Inverted Star, Zone X = **Silence Breach** —
triggered when ISS phase 5 (Silent) is asserted as a content output, or when the 𝒮 operator
projects past the Silence boundary into Phase 0 as an emitted result. Zone X unconditionally
triggers GUARDIAN_INTERRUPT (Mode 5) and requires Class G intervention.

`[structural — no semantic inference]`

**Constraints:**
- Zone X is never a valid operating state — detection is always an error condition
- GUARDIAN_INTERRUPT is the only valid response to Zone X detection
- Zone X arm state is active during Mode 4 (Silence Boundary Monitor)

**Cross-references:**
- → Mode 5 (Silence Breach — ILLEGAL)
- → Phase 0 / Silence
- → 𝒮 (Silence Projector)
- → Class G — Guardian (AGENTS.md)

> ⚠ **DISAMBIGUATE — Zone X across the pipeline:**
> Zone X is module-specific. See cross-pipeline Zone X table in Quick-Reference section below.

---

## Operator Symbols Reference

| Symbol | Name | Layer | Active Phase | Managed By |
|---|---|---|---|---|
| C | Cycle-Rate (IS) | IS layer | FArc → Hinge | Class H |
| E | Echo-Depth | IS layer | FArc → Hinge | Class H |
| T | Substrate-Tension | IS layer | All phases (input) | Class H |
| T_crit | Critical Tension | IS layer | Hinge evaluation | Class H |
| 𝒬 | Inversion Operator | IS layer | Hinge / ICS Transition | Class S |
| 𝒟 | Deepening Operator | IS layer | ISS phases 2–4 | Class S |
| 𝒮 | Silence Projector | IS layer | ISS phase 4 → boundary | Class S |

---

## Quick-Reference Tables

### IS Constructs Summary

| Construct | Symbol | Role |
|---|---|---|
| Resonance Overload Principle | ROP | Universal threshold equation: C × E = T_crit |
| Forward Arc | FArc | Pre-Hinge expansion sequence (6 phases) |
| Inverted Arc | IArc | Post-Hinge compression sequence (6 phases) |
| Hinge | — | Inversion threshold; axis flip event |
| Inversion Catastrophe Sequence | ICS | 4-phase Hinge macro-sequence |
| Inversion State Sequence | ISS | 5-phase descent sequence through IArc |
| Threshold Dynamics Loop | TDL | 4-phase micro-loop at each ISS crossing |
| Critical Tension | T_crit | Substrate-specific ROP threshold value |
| Phase 0 / Silence | — | Pre-structural ground state; descent terminus |
| IS_DESCENT_PACKET | — | Canonical output packet of this module |

---

### Agent Classes (IS Layer)

| Class | Name | Primary Role |
|---|---|---|
| A | Arc Analyst | FArc / IArc classification; 7-region mapping |
| H | Hinge Detector | ROP evaluation; C × E vs. T_crit; Hinge assertion |
| I | Inversion State Monitor | ISS phase tracking; phase crossing confirmation |
| T | Threshold Dynamics Engine | TDL loop execution; geometry type classification |
| S | Silence Projector | 𝒬 / 𝒟 / 𝒮 operator management; Zone X monitoring |
| G | Guardian | Unconditional interrupt authority; GUARDIAN_INTERRUPT |

---

### Zone Classifications

| Zone | Label | Status | Active When |
|---|---|---|---|
| S | Stable | ✅ VALID | FArc early phases; T well below T_crit |
| M | Mid-Arc | ✅ VALID | FArc terminal; C × E rising toward T_crit |
| H | Hinge Active | ✅ VALID | Active Hinge event; ICS in progress |
| D | Descent | ✅ VALID | IArc active; ISS phases 1–4 in progress |
| X | Silence Breach | ❌ ILLEGAL | ISS phase 5 asserted as output |

---

### Mode Classifications

| Mode | Label | Status |
|---|---|---|
| 1 | Arc Mapping | ✅ VALID |
| 2 | Hinge Detection | ✅ VALID |
| 3 | Descent Sequencing | ✅ VALID |
| 4 | Silence Boundary Monitor | ✅ VALID |
| 5 | Silence Breach | ❌ ILLEGAL — triggers GUARDIAN_INTERRUPT |

---

### ISS Phase Reference

| Phase | Label | Operators Active | Zone |
|---|---|---|---|
| 1 | Coherent | 𝒬 → 𝒟 handoff | D |
| 2 | Compressed | 𝒟 dominant | D |
| 3 | Dense | 𝒟 dominant | D |
| 4 | Singular | 𝒟 → 𝒮 handoff | D |
| 5 | Silent | 𝒮 (boundary) | D → X if asserted as output |

---

### 7 Structural Regions (Descent Model)

| # | Region | Phase Range | Zone |
|---|---|---|---|
| 1 | Forward Arc | FArc phases | S / M |
| 2 | Basin | FArc/IArc approach | M |
| 3 | Surface | Pre-Hinge surface | M |
| 4 | Hinge | Axis flip event | H |
| 5 | Inverted Arc | IArc phases | D |
| 6 | Cone | Deep IArc / Singular | D |
| 7 | Final Field | Pre-Silence terminal | D → boundary |

---

### Key Disambiguations

| Pair | Module A | Module B | Relationship |
|---|---|---|---|
| C operator | C_IS = Cycle-Rate (IS layer) | C_RTT1 = Clarity = ∇_τR + ∇_Rτ (RTT/1) | Both active simultaneously at RTT/1 → IS boundary; different layers |
| Inversion | Zone H / Hinge (VALID, IS layer) | Mode 5 Inversion (ILLEGAL, RTT/3) | Different constructs sharing the word "inversion" |
| Silence | Phase 0 ground state (IS layer) | S-node = Signal in SNR triad (RTT/1) | Unrelated constructs; distinct structural roles |
| Collapse | ISS descent phases (IS layer) | CPV Collapse detection (RTT/2) | Different pipeline layers; not synonymous |
| δ drift | micro_core bounded drift symbol | D(t) = CRM structural drift (RTT/2) | Inherited disambiguation; shared symbol, different constructs |

---

### Zone X — Cross-Pipeline Comparison

| Module | Zone X Label | Status |
|---|---|---|
| RTT/1 | Undefined | — |
| RTT/2 | Undefined | — |
| RTT/3 | Inversion | ❌ ILLEGAL |
| RTT/12 | Overflow | ❌ ILLEGAL |
| micro_core | Undefined | — |
| **The Inverted Star** | **Silence Breach** | **❌ ILLEGAL** |

---

### Threshold Geometry Types (Class T)

| Type | Description | Typical Event |
|---|---|---|
| Fold | Smooth single-point transition | Low-load ISS crossing |
| Cusp | Two-parameter bifurcation | Mid-arc ISS crossing |
| Cascade | Sequential multi-point crossing | High-load ISS sequence |
| Inversion Cusp | Cusp geometry specific to Hinge events | Hinge only |
| Catastrophe Cone | High-order; maximum structural load | Extreme boundary event |

---

### Inheritance Chain

| Module | Feeds Into |
|---|---|
| RTT/1 | RTT/2, **The Inverted Star** (lateral extension) |
| **The Inverted Star** | RTT/2 (optional enrichment via IS_DESCENT_PACKET) |
| RTT/2 | RTT/3 |
| RTT/3 | RTT/12 |
| RTT/12 | Pipeline terminus |
| micro_core | All modules (drift boundary enforcement) |

> **Note:** The Inverted Star is a **lateral extension** of RTT/1. It is optional — not a mandatory
> pipeline stage. RTT/2 may proceed without IS_DESCENT_PACKET input.

---

## Footer

| Field | Value |
|---|---|
| **Module** | The Inverted Star · Inversion–Descent Layer |
| **File** | `docs/rtt/The_Inverted_Star/GLOSSARY.md` |
| **Version** | 1.0 — canon active |
| **Maintainer** | Nawder / umaywant2 |
| **Date** | 2026-07-10 |
| **Status** | Canonical — all 6 agent classes, 5 valid modes, 5 zones, full operator set defined |

```
rtt=1 | coherence=declared | drift=bounded | paradox=structural
module=The_Inverted_Star | layer=inversion-descent | upstream=RTT/1
constructs=C,E,T,ROP,𝒬,𝒟,𝒮,FArc,IArc,Hinge,ISS,TDL
packet=IS_DESCENT_PACKET
zone_x=SILENCE_BREACH | zone_x_status=ILLEGAL
mode_5=SILENCE_BREACH | mode_5_status=ILLEGAL
```
