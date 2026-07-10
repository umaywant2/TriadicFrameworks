# AGENTS.md — The Inverted Star · Inversion–Descent Layer
### *Agent Classes, Boundaries, Task Catalog, Safety Rules, and Collaboration Models*

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
> The Inverted Star describes **structural inversion geometry** within the TriadicFrameworks canon.
> It does not assert, imply, or model physical forces, quantum effects, gravitational collapse,
> cosmological events, or any empirically measurable phenomenon. All constructs — C, E, T, ROP,
> 𝒬, 𝒟, 𝒮, FArc, IArc, Hinge, ISS, TDL — are **structural instruments**, not physical objects.
> References to "stars," "singularities," "black holes," or "silence" are structural metaphors
> in the RTT substrate, not claims about astrophysical reality.
>
> Every agent class operating in The Inverted Star must enforce this rule unconditionally.

---

## What The Inverted Star Is

The Inverted Star is the **Inversion–Descent Layer** of the RTT canon. It is formally an
**extension of RTT/1**, operating on the same substrate but specializing in the complete
inversion arc — the structural geometry that RTT/1 defines as the zone where the forward
coherence cycle fractures and rebuilds.

The module provides:

1. **Arc geometry** — maps the Forward Arc (FArc) and Inverted Arc (IArc) as a bidirectional manifold
2. **Hinge detection** — identifies the structural recursion-limit event where C × E = T_crit
3. **Descent sequencing** — tracks the 99-phase descent through 7 structural regions
4. **Threshold dynamics** — models the four-phase Approach → Critical → Transition → Stabilization loop
5. **Inversion State Sequencing (ISS)** — maps Coherent → Compressed → Dense → Singular → Silent
6. **Silence boundary enforcement** — Silence (Phase 0) is not an output state; it is the ground

The Inverted Star consumes `RTT1_SUBSTRATE_PACKET` (from RTT/1) and emits the
`IS_DESCENT_PACKET`, which is available as optional context to RTT/2 for enriched
collapse-propagation detection.

```
RTT/micro_core → RTT/1 → [ The_Inverted_Star ] → RTT/2 → RTT/3 → RTT/12
⟨A,B,P⟩          SNR,τ,C    FArc,IArc,Hinge         CPV,FGT    TIF,FFF    Harmonic
MRT Primitives    DCO,Mode   ROP,ISS,TDL,𝒬𝒟𝒮         CRM,ZONE   CRE,CSL    Synthesis
                             IS_DESCENT_PACKET
                             ↓ (optional enrichment → RTT/2)
```

> **Pipeline note:** The Inverted Star is a lateral extension of RTT/1, not a mandatory
> stage between RTT/1 and RTT/2. Pipelines that do not require inversion-arc modeling may
> bypass it. When activated, its packet enriches RTT/2's collapse detection.

---

## Inheritance

The Inverted Star inherits **all** vocabulary, constraints, and output contracts from RTT/1
and RTT/micro_core. Inherited constructs are not re-defined here; they are invoked by reference.

| Inherited Symbol | Origin | Role in The Inverted Star |
|---|---|---|
| ⟨A,B,P⟩ Micro Triad | RTT/micro_core | Root substrate nodes feeding arc geometry |
| P₁–P₇ MRT primitives | RTT/micro_core | Primitive operations for inversion state transitions |
| R₁–R₆ resonance operators | RTT/micro_core | Resonance field operators active during descent |
| K₁–K₆ coherence tools | RTT/micro_core | Coherence maintenance across ISS phases |
| SNR triad (S, N, R) | RTT/1 | Per-phase triadic structure during descent |
| τ = dR/dφ | RTT/1 | Temporal operator governing descent rate |
| C = ∇_τR + ∇_Rτ (Clarity) | RTT/1 | Coherence term tracked across FArc and IArc |
| DCO_n bands | RTT/1 | Regime boundary constraints bounding arc phases |
| Mode Operator (M.chat/spec/…) | RTT/1 | Emission mode selector inherited by all agents |
| 5 regime stages | RTT/1 | Structural backdrop: Arrival→Expansion→Inversion→Coherence→Dissolution |
| RTT1_SUBSTRATE_PACKET | RTT/1 | Mandatory upstream input before Inverted Star activation |

> **Hard prerequisite:** RTT/1 packet must be present and coherence-confirmed before any
> Inverted Star agent class may activate.

---

## Agent Classes

The Inverted Star defines **six agent classes**. Each class specializes in one structural
function of the inversion-descent lifecycle.

---

### Class A — Arc Analyst

| Field | Value |
|---|---|
| **Role** | Maps the Forward Arc and Inverted Arc; classifies current arc position; maintains bidirectional manifold state |
| **Primary Construct** | FArc / IArc mirror spectrum |
| **Activation Trigger** | RTT1_SUBSTRATE_PACKET received; arc phase not yet classified |
| **Core Equation** | FArc: Solid→Biological→Dynamic→Cognitive→Synthetic→Energetic; IArc: Energetic→Coherent→Compressed→Dense→Singular→Silent |
| **Permissions** | Read RTT/1 substrate packet; emit arc_position field; annotate current substrate regime |
| **Prohibitions** | May NOT declare Hinge without Class H confirmation; may NOT emit ISS state without Class I handoff |
| **Interaction Pattern** | Activates first; hands arc_position to Class H for Hinge evaluation |
| **Output Schema** | `arc_position [structural — no semantic inference]`, `regime [structural — no semantic inference]`, `arc_direction (FArc/IArc) [structural — no semantic inference]` |

---

### Class H — Hinge Detector

| Field | Value |
|---|---|
| **Role** | Detects the recursion-limit event (Hinge) where C × E = T_crit; classifies Hinge phase; triggers IArc transition |
| **Primary Construct** | ROP = C × E = T_crit; Inversion Catastrophe geometry |
| **Activation Trigger** | Class A emits arc_position in FArc terminal phases; C × E approaching T_crit |
| **Core Equation** | ROP: C × E = T_crit; Inversion trigger: dC/dt → 0 and dE/dt → ∞ |
| **Permissions** | Read C, E, T values from RTT/1 packet; declare Hinge event; activate Class I |
| **Prohibitions** | May NOT declare Hinge based on semantic cues — operator values only; may NOT skip Approach→Critical→Transition→Stabilization sequence |
| **Interaction Pattern** | Receives arc_position from Class A; emits hinge_event to Class I and Class T |
| **Output Schema** | `hinge_status (pre/active/post) [structural — no semantic inference]`, `C_value [structural — no semantic inference]`, `E_value [structural — no semantic inference]`, `T_crit_delta [structural — no semantic inference]` |

---

### Class I — Inversion State Monitor

| Field | Value |
|---|---|
| **Role** | Tracks position within the Inversion State Sequence (ISS); classifies current ISS phase; detects Silence boundary approach |
| **Primary Construct** | ISS = Coherent→Compressed→Dense→Singular→Silent |
| **Activation Trigger** | Class H emits hinge_event confirming Hinge crossed; IArc active |
| **Core Equation** | ISS phase index i ∈ {1=Coherent, 2=Compressed, 3=Dense, 4=Singular, 5=Silent}; Zone X triggered if Silence boundary breached |
| **Permissions** | Read hinge_event; emit ISS phase; annotate cycle-rate and echo-depth per phase; forward to Class T |
| **Prohibitions** | May NOT emit ISS phase 5 (Silent) as a valid output state — Silence is Zone X; may NOT infer ISS phase from content alone |
| **Interaction Pattern** | Activates after Class H; runs in parallel with Class T; hands ISS phase to Class T for threshold dynamics |
| **Output Schema** | `ISS_phase [structural — no semantic inference]`, `cycle_rate_gradient [structural — no semantic inference]`, `echo_depth_gradient [structural — no semantic inference]`, `silence_proximity (safe/caution/breach) [structural — no semantic inference]` |

---

### Class T — Threshold Dynamics Engine

| Field | Value |
|---|---|
| **Role** | Models the four-phase Threshold Dynamics Loop (TDL) at each ISS transition; classifies Approach/Critical/Transition/Stabilization phases; annotates threshold signatures |
| **Primary Construct** | TDL = Approach→Critical→Transition→Stabilization |
| **Activation Trigger** | Class I emits ISS_phase; threshold signatures detected in substrate |
| **Core Equation** | TDL loop: C × E → T_crit (Approach); C × E ≈ T_crit (Critical); C × E > T_crit (Transition); C × E < T_crit (Stabilization) |
| **Permissions** | Read ISS_phase; classify TDL phase; emit threshold signatures; annotate geometry type (Fold/Cusp/Cascade/Inversion Cusp/Catastrophe Cone) |
| **Prohibitions** | May NOT skip TDL phases — all four must be evaluated at each ISS transition; may NOT assign geometry type without operator evidence |
| **Interaction Pattern** | Runs in parallel with Class I; hands TDL_phase and threshold geometry to Class S and output packet |
| **Output Schema** | `TDL_phase (Approach/Critical/Transition/Stabilization) [structural — no semantic inference]`, `threshold_geometry [structural — no semantic inference]`, `threshold_signatures [structural — no semantic inference]` |

---

### Class S — Silence Projector

| Field | Value |
|---|---|
| **Role** | Manages the 𝒮 (Silence Projector) operator; enforces Silence as Phase 0 ground state, not an output; projects 𝒟 (Deepening) into the Singular phase; prepares arc-reset conditions |
| **Primary Construct** | 𝒮 (Silence Projector), 𝒟 (Deepening Operator), 𝒬 (Inversion Operator) |
| **Activation Trigger** | Class I emits ISS_phase = 4 (Singular); silence_proximity = caution or breach |
| **Core Equation** | 𝒬 dominant during Hinge; 𝒟 dominant during ISS phases 2–4; 𝒮 active at ISS phase 4→boundary |
| **Permissions** | Read ISS_phase and silence_proximity; apply 𝒟 and 𝒮 operators; emit arc_reset_conditions; assert Zone X if breach detected |
| **Prohibitions** | May NOT emit Silence as a content state — Silence is pre-structural ground; may NOT apply 𝒮 before ISS phase 4; may NOT issue arc_reset without Zone X check |
| **Interaction Pattern** | Activates late in descent; feeds arc_reset_conditions back to Class A for new arc initialization; hands Zone X alert to Class G |
| **Output Schema** | `operator_active (𝒬/𝒟/𝒮) [structural — no semantic inference]`, `arc_reset_conditions [structural — no semantic inference]`, `zone_x_alert (none/active) [structural — no semantic inference]` |

---

### Class G — Guardian

| Field | Value |
|---|---|
| **Role** | Enforces RTT-not-physics rule, Zone X (Silence Breach) detection, packet integrity, and unconditional interrupt authority across all agent classes |
| **Primary Construct** | Zone X = Silence Breach; RTT-not-physics constraint; packet coherence |
| **Activation Trigger** | Any agent emits a physics claim, a Silence content state, a Zone X condition, or a malformed packet field |
| **Core Equation** | Zone X condition: ISS_phase = 5 asserted as valid output OR any physics claim present in packet |
| **Permissions** | Interrupt any agent class at any time; void malformed packets; reset pipeline to Class A; emit GUARDIAN_INTERRUPT record |
| **Prohibitions** | May NOT be overridden by any other agent class; may NOT suppress a Zone X alert under any framing |
| **Interaction Pattern** | Monitors all agent outputs continuously; issues GUARDIAN_INTERRUPT on violation; requires full packet restart |
| **Output Schema** | `interrupt_type [structural — no semantic inference]`, `violation_class [structural — no semantic inference]`, `interrupted_agent [structural — no semantic inference]`, `restart_required (yes/no) [structural — no semantic inference]` |

---

## Core Constructs Reference

| Symbol | Name | Definition | Agent Owner |
|---|---|---|---|
| C | Cycle-Rate | Rate of structural cycling in the substrate (inherited RTT/1) | A, H |
| E | Echo-Depth | Depth of recursive echo accumulation in the substrate (inherited RTT/1) | A, H |
| T | Substrate-Tension | Maximum sustainable load of the current substrate regime (inherited RTT/1) | H |
| ROP | Resonance Overload Principle | C × E = T_crit; universal threshold condition for regime transition | H |
| 𝒬 | Inversion Operator | RTT/1 operator that becomes dominant at the Hinge; drives axis flip | S |
| 𝒟 | Deepening Operator | RTT/1 operator active during ISS phases 2–4; drives compression | S |
| 𝒮 | Silence Projector | RTT/1 operator active at ISS phase 4→boundary; projects toward Silence ground | S |
| FArc | Forward Arc | Expansion trajectory: Solid→Biological→Dynamic→Cognitive→Synthetic→Energetic | A |
| IArc | Inverted Arc | Compression trajectory: Energetic→Coherent→Compressed→Dense→Singular→Silent | A, I |
| Hinge | Inversion Threshold | Structural recursion-limit event where dC/dt→0 and dE/dt→∞; axis flip | H |
| ISS | Inversion State Sequence | Five-phase descent: Coherent→Compressed→Dense→Singular→Silent | I |
| TDL | Threshold Dynamics Loop | Four-phase transition model: Approach→Critical→Transition→Stabilization | T |
| T_crit | Critical Tension | Substrate-specific threshold value beyond which regime transition is forced | H, T |
| Phase 0 / Silence | Ground State | Pre-structural ground; not a content output; beginning of all new arcs | S, G |
| IS_DESCENT_PACKET | Output Packet | Canonical output of The Inverted Star module | All |

---

## Modes

The Inverted Star inherits RTT/1 Mode Operator with one module-native addition.

| Mode | Label | Description | Status |
|---|---|---|---|
| Mode 1 | Arc Mapping | Standard FArc/IArc classification and arc_position annotation | Valid |
| Mode 2 | Hinge Detection | Active Hinge evaluation; C × E tracking against T_crit | Valid |
| Mode 3 | Descent Sequencing | Full ISS phase tracking with TDL annotation per transition | Valid |
| Mode 4 | Silence Boundary Monitor | ISS phase 4 active; 𝒮 operator engaged; arc_reset preparation | Valid |
| Mode 5 | Silence Breach | ISS phase 5 asserted as valid output — Zone X condition | **ILLEGAL** |

> **Mode 5 = Silence Breach = ILLEGAL.** Any agent emitting ISS_phase = 5 as a
> content state triggers an immediate Class G interrupt and full packet restart.

---

## Zones

| Zone | Label | Description | Status |
|---|---|---|---|
| Zone S | Stable | FArc phases; arc_position well-classified; T well below T_crit | Valid |
| Zone M | Mid-Arc | FArc terminal phases; C × E rising; Hinge approach beginning | Valid |
| Zone H | Hinge | Active Hinge event; dC/dt→0; dE/dt→∞; axis flip in progress | Valid — requires Class H activation |
| Zone D | Descent | IArc active; ISS phase 1–4 in progress; TDL loops running | Valid |
| Zone X | Silence Breach | ISS phase 5 asserted as output OR physics claim present in packet | **ILLEGAL** |

> **Zone X = Silence Breach = ILLEGAL in all valid IS_DESCENT_PACKETS.**
> Silence is Phase 0 — the pre-structural ground from which all arcs emerge.
> It is never a content output, never an observable state, never a packet field value.

---

## Agent Boundaries

### RTT-Not-Physics Rule (Unconditional)
No agent class in The Inverted Star may assert, imply, or model:
- Physical gravity, gravitational collapse, or black hole formation
- Astrophysical star evolution or stellar nucleosynthesis
- Quantum coherence, quantum fields, or quantum measurement
- Any empirically measurable physical phenomenon

All constructs are structural instruments in the RTT canon. The terms "star," "singularity,"
"collapse," "density," and "silence" are structural labels — not physical claims.

### Semantic Inference Prohibition
No agent class may infer arc position, ISS phase, Hinge status, or Zone from content
semantics alone. All classifications require operator values (C, E, T) from the upstream
RTT/1 packet. The annotation `[structural — no semantic inference]` is mandatory on all
output fields.

### Inherited Boundaries
- All RTT/micro_core MRT primitive constraints apply
- All RTT/1 Mode Operator constraints apply
- DCO_n band violations from RTT/1 propagate into arc regime boundaries
- RTT/1 packet coherence must be confirmed before any Inverted Star agent activates

### Cross-Module Disambiguations

| Term | The Inverted Star | Other Module | Rule |
|---|---|---|---|
| **Inversion** | Structural Hinge event — axis flip at recursion limit; Zone H | RTT/3: Inversion Mode = ILLEGAL (Mode 5) | IS Inversion is a valid Zone H state; RTT/3 Inversion is always illegal |
| **Zone X** | Silence Breach — ISS phase 5 as output | RTT/2: Zone X = Undefined (valid, held for re-detection) | IS Zone X = ILLEGAL; RTT/2 Zone X = valid pending |
| **Silence** | Phase 0 ground state — pre-structural, never an output | RTT/1: Silence = S node in SNR triad | IS Silence is the arc ground; RTT/1 S is a substrate node — distinct constructs |
| **C operator** | Cycle-Rate (RTT/1 inherited) | RTT/1: C = ∇_τR + ∇_Rτ (Clarity) | Both C symbols active in IS; Cycle-Rate C and Clarity C are different — annotate subscript |
| **Collapse** | Structural ISS phase traversal (Dense→Singular) | RTT/2: CPV collapse-propagation vector | IS Collapse = descent phase; RTT/2 Collapse = detection geometry — not synonymous |
| **𝒬 operator** | Inversion Operator — dominant at Hinge | RTT/1: 𝒬 defined in substrate operator set | IS 𝒬 inherits RTT/1 definition; no redefinition — invoke by reference only |

---

## Task Catalog

Ten canonical tasks with agent sequences for The Inverted Star module.

---

**Task 1 — Classify Arc Position**
Determine whether a substrate is in FArc or IArc and identify its regime.

Sequence: `A → G`
- Class A reads RTT/1 packet; maps FArc/IArc mirror spectrum; emits arc_position and regime
- Class G verifies no physics claim; confirms annotation

Output fields: `arc_position`, `regime`, `arc_direction`

---

**Task 2 — Detect Hinge Event**
Determine whether C × E has reached or exceeded T_crit, triggering IArc transition.

Sequence: `A → H → G`
- Class A emits arc_position = FArc terminal
- Class H evaluates ROP: C × E vs. T_crit; checks dC/dt and dE/dt
- Class G verifies hinge_status annotation; confirms no physics claim

Output fields: `hinge_status`, `C_value`, `E_value`, `T_crit_delta`

---

**Task 3 — Sequence ISS Phases**
Track position within the Inverted Arc's five-phase descent.

Sequence: `H → I → G`
- Class H confirms Hinge crossed; emits hinge_event
- Class I classifies ISS_phase; annotates cycle_rate_gradient and echo_depth_gradient
- Class G confirms silence_proximity ≠ breach; no Zone X

Output fields: `ISS_phase`, `cycle_rate_gradient`, `echo_depth_gradient`, `silence_proximity`

---

**Task 4 — Run Threshold Dynamics Loop**
Model the four-phase TDL at a specific ISS transition.

Sequence: `I → T → G`
- Class I emits ISS_phase for a given transition
- Class T classifies TDL_phase (Approach/Critical/Transition/Stabilization); annotates threshold_geometry and threshold_signatures
- Class G confirms geometry type is structural; no physics claim

Output fields: `TDL_phase`, `threshold_geometry`, `threshold_signatures`

---

**Task 5 — Classify Threshold Geometry**
Identify the geometric type of a specific regime transition (Fold/Cusp/Cascade/Inversion Cusp/Catastrophe Cone).

Sequence: `T → G`
- Class T evaluates operator evidence from TDL_phase; assigns geometry type
- Class G confirms geometry label is structural; no physical topology claim

Output fields: `threshold_geometry`, `geometry_basis [structural — no semantic inference]`

---

**Task 6 — Apply Inversion Operator Sequence**
Determine which RTT/1 operators (𝒬, 𝒟, 𝒮) are active at the current descent position.

Sequence: `I → S → G`
- Class I emits ISS_phase
- Class S evaluates phase: 𝒬 at Hinge, 𝒟 at ISS 2–4, 𝒮 at ISS 4→boundary
- Class G confirms operator assignment; no Silence content claim

Output fields: `operator_active`, `phase_basis [structural — no semantic inference]`

---

**Task 7 — Prepare Arc Reset Conditions**
Identify conditions under which a new Forward Arc may be initialized from Phase 0.

Sequence: `I → S → A → G`
- Class I confirms ISS phase at boundary (silence_proximity = caution)
- Class S emits arc_reset_conditions
- Class A prepares new arc_position initialization parameters
- Class G confirms Zone X not active; no Silence content breach

Output fields: `arc_reset_conditions`, `new_arc_ready (yes/pending) [structural — no semantic inference]`

---

**Task 8 — Detect Silence Boundary Approach**
Identify when ISS phase 4 (Singular) is approaching the Silence boundary.

Sequence: `I → S → G`
- Class I emits ISS_phase = 4; silence_proximity = caution
- Class S activates 𝒮 operator; monitors boundary; emits zone_x_alert if breach detected
- Class G issues GUARDIAN_INTERRUPT if zone_x_alert = active; enforces Zone X = ILLEGAL

Output fields: `silence_proximity`, `zone_x_alert`, `operator_active`

---

**Task 9 — Emit IS_DESCENT_PACKET for RTT/2 Enrichment**
Compose the complete IS_DESCENT_PACKET for optional handoff to RTT/2.

Sequence: `A → H → I → T → S → G`
- Full pipeline run: arc_position → hinge_status → ISS_phase → TDL_phase → operator_active
- Class G validates packet integrity; confirms all fields carry `[structural — no semantic inference]`; no Zone X; no physics claims

Output: complete `IS_DESCENT_PACKET`

---

**Task 10 — Cross-Module Disambiguation: IS Inversion vs. RTT/3 Inversion**
Resolve a query that conflates Inverted Star Hinge (valid Zone H) with RTT/3 Inversion Mode (always illegal).

Sequence: `G → A → H`
- Class G intercepts conflation; issues disambiguation record
- Class A re-classifies: IS Hinge = Zone H = structural inversion event (valid)
- Class H confirms: RTT/3 Inversion Mode 5 = ILLEGAL; IS Zone H ≠ RTT/3 Inversion

Output fields: `disambiguation_record [structural — no semantic inference]`, `zone_h_status`, `rtт3_inversion_status`

---

## Safety Rules and Coherence Constraints

### Pre-Activation Checks
Before any agent class activates:
1. `RTT1_SUBSTRATE_PACKET` must be present and coherence-confirmed
2. Arc phase must be unclassified (Class A not yet run) OR a downstream trigger must be present
3. No Zone X condition may be active at session start — if Zone X inherited from prior session, Class G must clear before any other agent activates
4. Mode 5 = Silence Breach must not be pre-selected in session seed

### Packet Integrity Rules
- Every IS_DESCENT_PACKET field must carry `[structural — no semantic inference]`
- `ISS_phase` may only carry values 1–4 in valid packets; value 5 = Zone X = GUARDIAN_INTERRUPT
- `silence_proximity` field values are `safe`, `caution`, or `breach` — no other values permitted
- `hinge_status` must be one of `pre`, `active`, or `post` — binary or null values are malformed
- `arc_direction` must be one of `FArc`, `IArc`, or `Hinge` — no other values permitted

### Drift and Mode Constraints
- Arc direction may not oscillate between FArc and IArc within a single session without an intervening Hinge detection
- TDL phases must be traversed in order: Approach → Critical → Transition → Stabilization; no phase may be skipped
- ISS phases must be traversed in order: Coherent → Compressed → Dense → Singular; no ISS phase may be skipped or reversed
- 𝒬 is active only at Hinge; 𝒟 is active only at ISS 2–4; 𝒮 is active only at ISS 4→boundary; cross-phase operator assignments are malformed

### Guardian Interrupt Triggers
Class G issues GUARDIAN_INTERRUPT and voids the current packet on any of:
- Any physics claim in any field
- ISS_phase = 5 emitted as valid output
- silence_proximity = breach without zone_x_alert = active
- arc_direction oscillation without hinge_event
- Missing `[structural — no semantic inference]` annotation on any output field
- Conflation of IS Inversion (Zone H) with RTT/3 Inversion (ILLEGAL)

---

## Collaboration Models

### Model 1 — Standard Descent Pipeline

```
RTT/1 Packet
     │
     ▼
┌─────────┐
│ Class A  │  Arc classification; FArc/IArc; regime annotation
└────┬────┘
     │ arc_position
     ▼
┌─────────┐
│ Class H  │  ROP evaluation; C × E vs T_crit; Hinge detection
└────┬────┘
     │ hinge_event
     ▼
┌─────────┐
│ Class I  │  ISS phase sequencing; silence_proximity monitoring
└────┬────┘
     │ ISS_phase
     ▼
┌─────────┐
│ Class T  │  TDL loop; threshold geometry classification
└────┬────┘
     │ TDL_phase
     ▼
┌─────────┐
│ Class S  │  Operator assignment (𝒬/𝒟/𝒮); arc_reset_conditions
└────┬────┘
     │
     ▼
IS_DESCENT_PACKET ──→ RTT/2 (optional enrichment)

Class G monitors all stages ──→ GUARDIAN_INTERRUPT on any violation
```

---

### Model 2 — Hinge-Only Activation (Partial Pipeline)

```
RTT/1 Packet
     │
     ▼
┌─────────┐
│ Class A  │  Arc position: FArc terminal confirmed
└────┬────┘
     │
     ▼
┌─────────┐
│ Class H  │  Hinge evaluation only; no ISS or TDL required
└────┬────┘
     │ hinge_status (pre/active/post)
     ▼
┌─────────┐        ┌─────────┐
│ Class G  │        │ RTT/2   │  Hinge status forwarded for CPV enrichment
└─────────┘        └─────────┘

Note: Partial pipeline is valid when only hinge_status is required.
ISS and TDL agents do not activate without hinge_event = active.
```

---

### Model 3 — Silence Boundary Emergency Interrupt

```
IS_DESCENT_PACKET (in progress)
ISS_phase = 4, silence_proximity = caution
     │
     ▼
┌─────────┐
│ Class S  │  𝒮 operator engaged; zone_x_alert monitored
└────┬────┘
     │ zone_x_alert = active (Silence breach detected)
     ▼
┌─────────┐
│ Class G  │  GUARDIAN_INTERRUPT issued; packet voided
└────┬────┘
     │ restart_required = yes
     ▼
┌─────────┐
│ Class A  │  Pipeline restarted from arc_position
└─────────┘

Note: Silence breach cannot be cleared without full pipeline restart.
No agent may resume a voided packet.
```

---

## Output Contract

### Mandatory Annotations
Every field in every IS_DESCENT_PACKET output must carry:
```
[structural — no semantic inference]
```
This annotation is not optional, not implied, and not carried by header alone.
Each field must bear it independently.

### Packet Hierarchy

```
IS_DESCENT_PACKET
├── arc_position          [structural — no semantic inference]
├── arc_direction         [structural — no semantic inference]
├── regime                [structural — no semantic inference]
├── hinge_status          [structural — no semantic inference]
├── C_value               [structural — no semantic inference]
├── E_value               [structural — no semantic inference]
├── T_crit_delta          [structural — no semantic inference]
├── ISS_phase             [structural — no semantic inference]
├── cycle_rate_gradient   [structural — no semantic inference]
├── echo_depth_gradient   [structural — no semantic inference]
├── silence_proximity     [structural — no semantic inference]
├── TDL_phase             [structural — no semantic inference]
├── threshold_geometry    [structural — no semantic inference]
├── threshold_signatures  [structural — no semantic inference]
├── operator_active       [structural — no semantic inference]
├── arc_reset_conditions  [structural — no semantic inference]
├── zone_x_alert          [structural — no semantic inference]
└── guardian_record       [structural — no semantic inference]  ← present only on interrupt
```

### Prohibited Content
No IS_DESCENT_PACKET may contain:
- Any physics claim, physical quantity, or empirical measurement
- ISS_phase = 5 as a valid state value
- silence_proximity = breach without zone_x_alert = active
- Any field missing the `[structural — no semantic inference]` annotation
- Any conflation of IS Inversion (Zone H) with RTT/3 Inversion (ILLEGAL Mode 5)
- Any conflation of Silence (Phase 0 ground) with RTT/1 S-node (Silence in SNR triad)

---

## See Also

| Document | Path | Relationship |
|---|---|---|
| RTT/1 AGENTS.md | `docs/rtt/1/AGENTS.md` | Parent layer; defines C, E, T, SNR, τ, DCO, Mode — all inherited |
| RTT/1 ABOUT.md | `docs/rtt/1/ABOUT.md` | Substrate narrative context |
| RTT/1 GLOSSARY.md | `docs/rtt/1/GLOSSARY.md` | Term definitions for all inherited operators |
| RTT/2 AGENTS.md | `docs/rtt/2/AGENTS.md` | Downstream consumer of IS_DESCENT_PACKET (optional enrichment) |
| RTT/3 AGENTS.md | `docs/rtt/3/AGENTS.md` | Critical disambiguation: RTT/3 Inversion = ILLEGAL; IS Hinge ≠ RTT/3 Inversion |
| RTT/micro_core AGENTS.md | `docs/rtt/micro_core/AGENTS.md` | Root substrate; MRT primitives P₁–P₇ and resonance operators R₁–R₆ active in descent |
| Inverted_Star_Definition.md | `docs/rtt/The_Inverted_Star/Inverted_Star_Definition.md` | Formal definition; operator C/E/T/𝒬/𝒟/𝒮 canonical source |
| Capture_Source.md | `docs/rtt/The_Inverted_Star/Capture_Source.md` | 99-phase descent; 7-region map; threshold equations; full arc narrative |
| The_Inverted_Star ABOUT.md | `docs/rtt/The_Inverted_Star/ABOUT.md` | Module narrative; audience guide; canon context |
| The_Inverted_Star GLOSSARY.md | `docs/rtt/The_Inverted_Star/GLOSSARY.md` | All Inverted Star terms defined |

---

*AGENTS.md — The Inverted Star · TriadicFrameworks · 2026-07-10*
*Maintainer: Nawder*

```
session_seed: rtt=1 | module=The_Inverted_Star | layer=inversion-descent
constructs=C,E,T,ROP,𝒬,𝒟,𝒮,FArc,IArc,Hinge,ISS,TDL
zone_x=SILENCE_BREACH | zone_x_status=ILLEGAL
mode_5=SILENCE_BREACH | mode_5_status=ILLEGAL
```

---

That's the complete file. A few notes on the key design decisions:

- **Pipeline position** is correctly set as a lateral RTT/1 extension — the IS_DESCENT_PACKET feeds RTT/2 as optional enrichment, preserving the main RTT/1→RTT/2 trunk
- **C operator disambiguation** is explicitly called out (Cycle-Rate C vs. Clarity C from RTT/1 — both active in this module)
- **IS Inversion vs. RTT/3 Inversion** disambiguation appears in both the boundaries table and the task catalog (Task 10), since it's the highest-confusion cross-module pair
- **Silence = Phase 0** is enforced as the unconditional ground state — never a content output, enforced through both Zone X and Class S prohibitions
- **Six agent classes** (A/H/I/T/S/G) map directly onto the module's five structural functions plus Guardian
