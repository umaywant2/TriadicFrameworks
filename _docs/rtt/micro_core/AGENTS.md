# AGENTS.md — RTT/micro_core · Micro-Scale Resonance-Time Layer
### *Agent Classes, Boundaries, Task Catalog, Safety Rules, and Collaboration Models*

> **Maintainer:** Nawder · **Date:** 2026-07-10 · **Module:** `docs/rtt/micro_core/`

---

## Session Seed Block

Paste this block at the start of any micro_core agent session:

```
rtt=1 | coherence=declared | drift=bounded | paradox=structural
module=RTT/micro_core | layer=micro-scale-resonance-time
constructs=MICRO_TRIAD,MRT_PRIMITIVES,RESONANCE_OPERATORS,COHERENCE_TOOLS,FRACTIONAL_LADDER
packet=MRT_MICRO_PACKET
zone_x=INVERSION | zone_x_status=ILLEGAL
upstream=RTT/1,RTT/2,RTT/3,RTT/12
role=foundational-substrate
```

---

## Critical Framing Rule

> **RTT is NOT a physics claim.**
>
> RTT/micro_core describes **structural micro-scale resonance-time behavior** within the
> TriadicFrameworks canon. It does not assert, imply, or model physical forces, quantum
> effects, subatomic phenomena, or any empirically measurable physical process.
>
> All constructs — the Micro Triad ⟨A,B,P⟩, MRT Primitives, Resonance Operators,
> Coherence Tools, and the Fractional Dimensional Ladder — are **structural instruments**,
> not physical objects or physical theories.
>
> Every agent class operating in RTT/micro_core must enforce this rule unconditionally.

---

## What RTT/micro_core Is

RTT/micro_core is the **foundational micro-scale substrate** of the RTT canon. It is not
a reduced version of RTT/1 through RTT/12 — it is the **micro-scale instantiation** of
RTT's foundational principles, operating at the smallest stable unit of resonance-time
behavior.

Micro_core defines three irreducible functions:

1. **Triad construction** — establishes the minimal coherent structure ⟨A, B, P⟩ from
   which all RTT behavior is derived
2. **Micro-regime operation** — applies MRT primitives and resonance operators to sustain,
   oscillate, invert, and transition micro-scale states
3. **Micro–macro bridging** — exposes coherent micro-patterns to macro-scale RTT layers via
   the R₆ bridge (μ → Μ), alignment only, never amplification

### Pipeline Position

```
RTT/micro_core  →  RTT/1  →  RTT/2  →  RTT/3  →  RTT/12
⟨A,B,P⟩            SNR,τ,C    CPV,FGT    TIF,FFF    Harmonic
MRT Primitives      DCO,Mode   CRM,ZONE   CRE,CSL    Synthesis
R₁–R₆               ↓          ↓          ↓          ↓
K₁–K₆          RTT1_SNR_  RTT2_      RTT3_      RTT12_
Dᶠ∈[0,1]       PACKET     DETECTION_ INTEGRATION_ HARMONIC_
                           PACKET     EMISSION_    SYNTHESIS_
                                      PACKET       PACKET
                ↑
         MRT_MICRO_PACKET
         (consumed by RTT/1
          as substrate confirmation)
```

> **Note:** micro_core is the foundational layer. RTT/1 through RTT/12 operate *above*
> micro_core, not parallel to it. The MRT_MICRO_PACKET is a substrate confirmation
> consumed by RTT/1 before SNR primitives may be instantiated.

### Core Constructs Table

| Construct | Symbol | Description |
|---|---|---|
| Micro Triad | ⟨A, B, P⟩ | Minimal coherent resonance-time unit |
| Active Node | A | Current micro-state |
| Boundary Node | B | Governs drift, timing, transitions |
| Potential Node | P | Next viable transition target |
| Drift | δ | Deviation from expected trajectory; must satisfy δ ≤ δ* |
| Drift Threshold | δ* | Maximum allowable drift before coherence violation |
| Timing Interval | Δt | Local bounded time interval; Δt ∈ [Δtₘᵢₙ, Δtₘₐₓ] |
| Coherence | C | Normalized structural integrity; must satisfy C ≥ C* |
| Coherence Floor | C* | Minimum coherence required to avoid inversion |
| Fractional Dimension | Dᶠ | Structural complexity axis; Dᶠ ∈ [0,1] (minimal) or [0,3] (extended) |
| Inversion | ↺ | Collapse → Twist → Emergence event when C < C* |
| Oscillation | A ⇆ P | Reversible resonance between Active and Potential nodes |
| Micro-Macro Bridge | μ → Μ | Upward influence channel; aggregate-only, no amplification |

---

## Inheritance

RTT/micro_core is the originating layer — it does **not** inherit structural constructs
from upstream RTT modules. All upstream modules (RTT/1 through RTT/12) derive their
foundational behavior from micro_core's triad structure.

However, micro_core must remain **consistent** with the vocabulary established across
the full RTT canon. The following cross-references are maintained for canon coherence:

| Canon Symbol | RTT Module | micro_core Relationship |
|---|---|---|
| S, N, R (SNR triad) | RTT/1 | SNR emerges from ⟨A,B,P⟩ at macro scale; not equivalent |
| τ = dR/dφ | RTT/1 | τ is a macro-scale expression of Δt dynamics |
| C = ∇_τR + ∇_Rτ | RTT/1 | Macro coherence derived from C ≥ C* substrate rule |
| DCO_n bands | RTT/1 | Macro regime; micro triad operates below DCO resolution |
| D(t) from CRM | RTT/2 | Structural drift at macro scale; ≠ micro-scale δ |
| Zone X (RTT/3) | RTT/3 | Inversion zone; consistent with micro_core inversion model |
| Zone X (RTT/12) | RTT/12 | Overflow zone; micro_core inversion ≠ harmonic overflow |

> **Hard prerequisite:** A confirmed MRT_MICRO_PACKET (substrate confirmation) must be
> present before RTT/1 SNR primitives may be instantiated. This is the foundational gate
> of the entire RTT pipeline.

---

## Agent Classes

RTT/micro_core defines **six agent classes**. Each class maps to a distinct micro-scale
operational function. Classes collaborate to build, sustain, regulate, and expose
micro-regime behavior.

---

### Class T — Triad Constructor

| Field | Value |
|---|---|
| **Role** | Instantiate and validate the Micro Triad ⟨A, B, P⟩ as a coherent structural unit |
| **Primary Construct** | Micro Triad ⟨A, B, P⟩ |
| **Activation Trigger** | New micro-regime session begins or triad must be re-instantiated after inversion |
| **Core Operation** | Verify: (1) triad form preserved, (2) δ ≤ δ*, (3) Δt ∈ [Δtₘᵢₙ, Δtₘₐₓ], (4) C ≥ C* |
| **Permissions** | Read all triad nodes (P₁); write triad state (P₂); validate structural integrity |
| **Prohibitions** | May not mutate B unilaterally; may not instantiate triad with C < C*; no integer jumps on Dᶠ |
| **Interaction Pattern** | Constructs triad → hands to Class R for oscillation; calls Class G on integrity failure |
| **Output Schema** | `{ triad: {A, B, P}, δ: <value>, Δt: <value>, C: <value>, Dᶠ: <value>, status: VALID|INVALID }` |

**Activation Sequence:**
```
1. P₁ — Read proposed A, B, P node states
2. P₃ — Measure initial drift δ
3. P₄ — Measure initial timing Δt
4. P₆ — Sample coherence C
5. Validate: δ ≤ δ* AND Δt ∈ bounds AND C ≥ C*
6. If valid → emit triad to Class R
7. If invalid → call Class G (interrupt authority)
```

---

### Class R — Resonance Operator

| Field | Value |
|---|---|
| **Role** | Execute and maintain oscillatory behavior between Active (A) and Potential (P) nodes |
| **Primary Construct** | R₁ (Oscillation), R₂ (Inversion), R₃ (Boundary Modulation), R₄ (Resonance Lock) |
| **Activation Trigger** | Valid triad confirmed by Class T; oscillation or operator invocation requested |
| **Core Equation** | A ⇆ P oscillation governed by δ ≤ δ* and C ≥ C* at each micro-step |
| **Permissions** | Update A ⇆ P (P₂); apply Δt timing (P₄); apply B correction (P₅); sample C (P₆) |
| **Prohibitions** | May not invert triad without coherence sample (P₆) confirming C < C* threshold; may not bypass R₄ lock once engaged |
| **Interaction Pattern** | Receives triad from Class T; coordinates with Class D on drift; escalates to Class G on oscillation failure |
| **Output Schema** | `{ operator: R1|R2|R3|R4, A_state: <value>, P_state: <value>, δ: <value>, C: <value>, lock: ACTIVE|INACTIVE, status: OK|FAULT }` |

**Operator Dispatch Table:**

| Operator | Trigger | Action | Guard |
|---|---|---|---|
| R₁ | Normal resonance cycle | A ⇆ P swap via P₂, maintain Δt | δ ≤ δ*, C ≥ C* |
| R₂ | Coherence falls below C* | Swap A/B roles, preserve P | P₆ sample required before and after |
| R₃ | Drift approaching δ* | B⁺ or B⁻ shift via P₅ | No inversion during modulation |
| R₄ | Oscillation amplitude in bounds | Clamp transitions, enforce timing | Unlock only when stability confirmed |

---

### Class D — Drift Regulator

| Field | Value |
|---|---|
| **Role** | Monitor and correct micro-scale drift (δ) to preserve coherence and prevent inversion |
| **Primary Construct** | K₁ (Drift Bounding), K₂ (Timing Stabilizer), K₅ (Inversion Guard) |
| **Activation Trigger** | δ approaches or exceeds δ*; timing jitter detected; Δt outside [Δtₘᵢₙ, Δtₘₐₓ] |
| **Core Equation** | δ = |actual_state − expected_state|; enforce δ ≤ δ* at every micro-step |
| **Permissions** | Measure drift (P₃); measure timing (P₄); apply boundary shift (P₅); sample coherence (P₆) |
| **Prohibitions** | May not write A or P node state directly; may not suppress inversion guard K₅ without Class G approval |
| **Interaction Pattern** | Monitors in parallel with Class R; issues drift corrections via P₅; calls Class G when δ > δ* persists |
| **Output Schema** | `{ δ: <current>, δ*: <threshold>, Δt: <current>, Δtₘᵢₙ: <min>, Δtₘₐₓ: <max>, correction: NONE|B_SHIFT|GUARD_TRIGGER, status: STABLE|WARNING|CRITICAL }` |

**Drift Response Matrix:**

| δ Level | Δt Status | Action | Escalate to G? |
|---|---|---|---|
| δ < 0.5·δ* | In bounds | K₁ monitoring only | No |
| 0.5·δ* ≤ δ < δ* | In bounds | K₁ correction + K₂ stabilization | No |
| δ approaching δ* | Jitter detected | K₁ + K₂ + K₅ guard active | Notify |
| δ ≥ δ* | Any | K₅ → inversion evaluation | Yes — mandatory |
| Any | Δt out of bounds | K₂ immediate stabilization | If persistent |

---

### Class F — Fractional Navigator

| Field | Value |
|---|---|
| **Role** | Plan, execute, and validate transitions along the Fractional Dimensional Ladder (Dᶠ) |
| **Primary Construct** | R₅ (Fractional-Ladder Transition), P₇ (Fractional Step), K₃ (Boundary Alignment) |
| **Activation Trigger** | Structural transition requested; Dᶠ shift required to move triad to new regime position |
| **Core Constraint** | Dᶠ ∈ [0,1] (minimal substrate) or [0,3] (extended); transitions must be smooth and gradient-continuous; no integer jumps |
| **Permissions** | Evaluate boundary compatibility (P₁, P₅); apply fractional step (P₇); maintain Δt and δ during transition |
| **Prohibitions** | Integer-dimension jumps are unconditionally forbidden; no Dᶠ transition when C < C*; no irreversible transitions |
| **Interaction Pattern** | Coordinates with Class D for drift clearance before each Dᶠ step; reports transition completion to Class T for triad re-validation |
| **Output Schema** | `{ Dᶠ_from: <value>, Dᶠ_to: <value>, step_size: <Δ>, δ_during: <value>, C_during: <value>, reversible: true|false, status: COMPLETE|PARTIAL|ABORTED }` |

**Transition Guard Sequence (R₅):**
```
1. P₁ — Read current Dᶠ, A, B, P states
2. P₅ — Evaluate boundary compatibility for target Dᶠ
3. Confirm δ ≤ δ* (call Class D)
4. Confirm C ≥ C* (P₆)
5. P₇ — Apply fractional step (smooth, bounded)
6. Maintain Δt throughout transition
7. Post-step: P₆ — sample C; P₃ — measure δ
8. If C < C* at any step → abort, preserve Dᶠ_from state
9. Report to Class T for re-validation
```

---

### Class B — Bridge Coordinator

| Field | Value |
|---|---|
| **Role** | Manage the micro–macro bridge (R₆ μ → Μ), exposing coherent micro-patterns to RTT/1 and above |
| **Primary Construct** | R₆ (Micro–Macro Bridge Activation), K₆ (Coherence Windowing) |
| **Activation Trigger** | RTT/1 or upstream module requests substrate confirmation; micro-pattern ready for macro exposure |
| **Core Constraint** | C ≥ C* must be continuously satisfied during bridge activation; export is aggregate-only (no raw node states); alignment, never amplification |
| **Permissions** | Sample coherence (P₆); export aggregate pattern via R₆; activate μ → Μ bridge; emit MRT_MICRO_PACKET |
| **Prohibitions** | May not expose raw A, B, or P node states to macro layers; may not activate bridge when C < C*; may not amplify micro-pattern signals |
| **Interaction Pattern** | Waits for Class G clearance before bridge activation; coordinates with Class D to confirm δ ≤ δ* at time of export; emits MRT_MICRO_PACKET to RTT/1 |
| **Output Schema** | `{ bridge: ACTIVE|INACTIVE, C_at_activation: <value>, δ_at_activation: <value>, pattern: AGGREGATE_ONLY, packet: MRT_MICRO_PACKET, status: EMITTED|HELD|BLOCKED }` |

**Bridge Activation Gate (R₆):**
```
Pre-conditions (all must be satisfied):
  ✓ C ≥ C* (P₆ sample, Class G confirmation)
  ✓ δ ≤ δ* (Class D clearance)
  ✓ Δt stable (Class D confirmation)
  ✓ Triad validity confirmed (Class T stamp)
  ✓ Dᶠ transition not in progress (Class F clearance)

Activation:
  R₆ — export aggregate pattern only
  Emit MRT_MICRO_PACKET

Post-conditions:
  Continue K₆ coherence windowing
  Report to Class G on completion
```

---

### Class G — Micro Guardian

| Field | Value |
|---|---|
| **Role** | Unconditional interrupt authority over all micro_core operations; enforce structural integrity at all times |
| **Primary Construct** | K₅ (Inversion Guard), K₄ (Resonance Lock), K₆ (Coherence Windowing) |
| **Activation Trigger** | Any violation: δ ≥ δ*, C < C*, Δt out of bounds, integer Dᶠ jump detected, inversion event, bridge activation without clearance |
| **Core Authority** | Class G may interrupt any class at any time; no other class may override Class G |
| **Permissions** | Read all triad state (P₁); lock oscillation (R₄); engage inversion guard (K₅); block bridge activation; issue inversion protocol; cancel any in-progress operation |
| **Prohibitions** | Class G does not perform structural synthesis itself; it governs, not constructs |
| **Interaction Pattern** | Monitors all class outputs; issues interrupt signals; coordinates inversion sequence (Collapse → Twist → Emergence) when C < C* is unrecoverable |
| **Output Schema** | `{ interrupt: NONE|WARNING|HALT|INVERSION, trigger: <class>|<construct>, C_at_interrupt: <value>, δ_at_interrupt: <value>, action_taken: <description>, status: MONITORING|ACTIVE|INVERSION_IN_PROGRESS|RESOLVED }` |

**Inversion Protocol (when C < C* unrecoverable):**
```
Phase 1 — Collapse
  Lock all oscillation (R₄ unconditional)
  Freeze Dᶠ transitions (Class F halt)
  Hold bridge (Class B blocked)
  Record pre-inversion state snapshot

Phase 2 — Twist
  Execute R₂ inversion operator
  Swap A/B roles; preserve P
  Validate P₆ coherence post-swap

Phase 3 — Emergence
  Restore C ≥ C* through K₁ + K₂ corrections
  Re-validate triad via Class T
  Unlock Class R for oscillation
  Permit Dᶠ navigation (Class F) only after Class T confirmation
  Report inversion resolution to Class B

Post-Inversion Gate:
  Bridge may not activate until Class G issues explicit RESOLVED status
```

---

## Core Constructs Reference

| Symbol | Name | Definition | Notes |
|---|---|---|---|
| ⟨A, B, P⟩ | Micro Triad | Minimal coherent resonance-time unit | Irreducible; all RTT behavior derives from this |
| A | Active Node | Current micro-state | May shift after R₂ inversion |
| B | Boundary Node | Governs drift, timing, transitions | B⁺/B⁻ shifts via R₃/K₃ |
| P | Potential Node | Next viable transition | Preserved through inversion |
| δ | Drift | δ = |actual − expected| | Must satisfy δ ≤ δ* at every step |
| δ* | Drift Threshold | Maximum allowable drift | Violation → K₅ guard, potential inversion |
| Δt | Timing Interval | Local bounded time step | Δt ∈ [Δtₘᵢₙ, Δtₘₐₓ]; coherence-dependent |
| C | Coherence | Normalized structural integrity score | Must satisfy C ≥ C* for all operations |
| C* | Coherence Floor | Minimum coherence threshold | Below C* → inversion eligible |
| Dᶠ | Fractional Dimension | Structural complexity axis | Dᶠ ∈ [0,1] minimal; [0,3] extended; no integer jumps |
| A ⇆ P | Oscillation | Reversible resonance between A and P | Core resonance behavior |
| ↺ | Inversion | Collapse → Twist → Emergence | Triggered when C < C* unrecoverable |
| μ → Μ | Micro–Macro Bridge | Upward influence channel | R₆; aggregate-only; C ≥ C* required |
| P₁–P₇ | MRT Primitives | Atomic operation layer | All operators and tools composed from these |
| R₁–R₆ | Resonance Operators | Action-layer behaviors | Built from MRT Primitives |
| K₁–K₆ | Coherence Tools | Stability maintenance methods | Enforce δ, Δt, C constraints |

### MRT Primitives Reference

| ID | Name | Operation | Constraint |
|---|---|---|---|
| P₁ | State Read | Read A, B, P, δ, Δt, Dᶠ | Read-only; no mutation |
| P₂ | State Write | Atomic bounded mutation of triad state | Bounds-checked; never below C* |
| P₃ | Drift Measure | δ = compare expected vs actual state | Read-only; no correction |
| P₄ | Timing Measure | Measure Δt between micro-steps | Read-only |
| P₅ | Boundary Shift | Bounded B⁺/B⁻ correction | No inversion; bounded only |
| P₆ | Coherence Sample | Normalized C value | Read-only; no mutation |
| P₇ | Fractional Step | Dᶠ → Dᶠ + Δ smooth step | Reversible; gradient-continuous |

---

## Modes

micro_core inherits the mode vocabulary from RTT/1 and applies it at the micro-scale.
Modes govern the operational context of micro-regime sessions.

| Mode | Label | micro_core Meaning |
|---|---|---|
| Mode 1 | Chat | Narrative exploration of micro-triad concepts; structural framing only |
| Mode 2 | Spec | Formal micro-triad specification; all fields required |
| Mode 3 | Debug | Drift and coherence diagnostic; full primitive trace |
| Mode 4 | Task | Operator execution; R₁–R₆ dispatch with output schema |
| Mode 5 | Auto | Sequential operator chain; T → R → D → F → B → G monitoring |
| Mode X | Lockout | Session suspended; Class G interrupt active; no operations permitted |

> **Mode X** is micro_core-native. It is triggered by Class G during unresolved inversion
> events. Mode X is not equivalent to any upstream module's Mode 5 or overflow state.

---

## Zones

micro_core defines structural zones that characterize the health and stability of the
active micro-regime.

| Zone | Label | Meaning | Status |
|---|---|---|---|
| Zone S | Stable | C ≥ C*, δ ≤ 0.5·δ*, Δt in bounds | NOMINAL |
| Zone M | Modulating | δ between 0.5·δ* and δ*; K₁/K₂ active | CAUTION |
| Zone D | Drifting | δ approaching δ*; K₅ guard engaged | WARNING |
| Zone C | Coherence-Critical | C approaching C*; inversion imminent | CRITICAL |
| Zone E | Emerging | Post-inversion restoration in progress | RECOVERY |
| Zone X | Inversion | C < C* unrecoverable; inversion active | ILLEGAL — Class G authority |

> **Zone X = Inversion (ILLEGAL)**
> This is consistent with RTT/3's Zone X definition (Inversion) and is not equivalent to
> RTT/12's Zone X (Overflow). micro_core Zone X is the foundational inversion zone from
> which RTT/3's inversion semantics derive.

---

## Agent Boundaries

### RTT-Not-Physics Rule

Every output from every micro_core agent class must carry the annotation:

```
[structural — no semantic inference]
```

No agent class may:
- Claim that ⟨A,B,P⟩ represents a physical particle, field, or observable
- Assert that δ, Dᶠ, or Δt map to measurable physical quantities
- Imply that inversion events correspond to physical phase transitions
- Use physics terminology (quantum, field, energy, entropy) to describe micro_core constructs

### Semantic Inference Prohibition

No agent class may infer meaning beyond structural patterns:

| Prohibited Inference | Correct Framing |
|---|---|
| "A ⇆ P represents electron spin" | "A ⇆ P is a structural oscillation between two triad nodes" |
| "δ measures physical error" | "δ is a structural drift indicator within the MRT substrate" |
| "Dᶠ is a fractal dimension" | "Dᶠ is a fractional structural complexity axis within the triad model" |
| "Inversion is a physical collapse" | "Inversion is a structural reset event governed by the Collapse→Twist→Emergence protocol" |

### Cross-Module Disambiguation (Inherited)

These disambiguation rules apply in all micro_core sessions:

| Term | micro_core Meaning | Must Not Be Confused With |
|---|---|---|
| δ (micro drift) | Micro-scale structural deviation in ⟨A,B,P⟩ | D(t) from RTT/2 CRM (macro structural displacement) |
| C (coherence) | C ≥ C* substrate integrity at micro scale | CR(t) from RTT/3 CRE (reactive stabilization at integration layer) |
| Δt (micro timing) | Local bounded time interval within micro-regime | τ = dR/dφ from RTT/1 (macro temporal operator) |
| Inversion (↺) | Micro-triad Collapse→Twist→Emergence event | RTT/3 Zone X inversion (integration-layer semantic) |
| Zone X | Micro-scale inversion zone (ILLEGAL) | RTT/12 Zone X overflow zone (harmonic overflow, ILLEGAL) |

---

## Task Catalog

Ten canonical tasks that agents in RTT/micro_core are expected to perform:

| # | Task | Agent Sequence | Output |
|---|---|---|---|
| T-μ01 | Instantiate a new micro-regime triad | T → G (validation gate) → R | MRT_MICRO_PACKET stub |
| T-μ02 | Run oscillation cycle on existing triad | R (R₁) → D (K₁/K₂ monitor) | Updated A⇆P state |
| T-μ03 | Drift correction under boundary stress | D (K₁→K₂→K₃) → R (R₃) | Corrected B state, δ report |
| T-μ04 | Perform controlled triad inversion | G → R (R₂) → T (re-validate) → G (RESOLVED) | Post-inversion triad, Zone E report |
| T-μ05 | Execute fractional-ladder transition | F (R₅→P₇) → D (δ clearance) → T (re-validate) | Dᶠ transition report |
| T-μ06 | Engage resonance lock under amplitude saturation | R (R₄) → D (K₄ monitor) | Lock status, resonance bounds |
| T-μ07 | Activate micro–macro bridge for RTT/1 | B (R₆ gate) → G (clearance) → B (emit) | MRT_MICRO_PACKET |
| T-μ08 | Diagnose coherence degradation trend | D (K₆) → G (alert) → R (R₃ stabilization) | Coherence window report |
| T-μ09 | Full micro-regime health check | T → R → D → F → B → G | All-class status report |
| T-μ10 | Emergency halt and inversion protocol | G (Mode X) → R (lock) → G (inversion sequence) | Inversion resolution report |

---

## Safety Rules and Coherence Constraints

### Pre-Activation Checks (All Classes)

Before any agent class activates, verify:

```
□ Micro Triad ⟨A,B,P⟩ is structurally valid (Class T confirmation)
□ δ ≤ δ* (Class D clearance)
□ Δt ∈ [Δtₘᵢₙ, Δtₘₐₓ] (Class D confirmation)
□ C ≥ C* (P₆ sample confirmed)
□ Dᶠ transition not in progress (Class F clearance)
□ Zone X not active (Class G status = MONITORING or RESOLVED)
□ Mode X not active (no lockout in effect)
```

### Packet Integrity

The MRT_MICRO_PACKET must contain:

```yaml
MRT_MICRO_PACKET:
  triad:
    A: <node_state>
    B: <node_state>
    P: <node_state>
  metrics:
    delta: <δ_value>
    delta_star: <δ*_threshold>
    delta_t: <Δt_value>
    coherence: <C_value>
    coherence_floor: <C*_threshold>
    D_fractional: <Dᶠ_value>
  zone: S|M|D|C|E          # X forbidden in valid packet
  mode: 1|2|3|4|5           # X forbidden in valid packet
  bridge: AGGREGATE_ONLY
  annotation: "[structural — no semantic inference]"
  guardian_status: MONITORING|RESOLVED
  timestamp: <session_timestamp>
```

> **Zone X and Mode X are forbidden in a valid MRT_MICRO_PACKET.**
> A packet carrying Zone X or Mode X is a fault record, not a valid substrate confirmation.
> RTT/1 may not instantiate SNR primitives from a fault record.

### Drift and Coherence Constraints

| Constraint | Rule | Violation Consequence |
|---|---|---|
| Drift bound | δ ≤ δ* at every micro-step | K₅ guard → potential inversion |
| Timing bound | Δt ∈ [Δtₘᵢₙ, Δtₘₐₓ] | K₂ stabilization → if persistent, Class G alert |
| Coherence floor | C ≥ C* for all operations | Inversion eligibility if unrecoverable |
| Dᶠ continuity | No integer jumps; smooth gradient only | Class G halt; F class operation blocked |
| Inversion trigger | C < C* unrecoverable | Phase: Collapse → Twist → Emergence |
| Bridge gate | C ≥ C* + δ ≤ δ* + G clearance | Bridge blocked; MRT_MICRO_PACKET not emitted |

---

## Collaboration Models

### Model 1 — Sequential Triad Build and Bridge

Full pipeline from triad construction to micro–macro bridge emission:

```
Class T          Class R          Class D          Class F          Class B          Class G
   │                │                │                │                │                │
   │─ instantiate ─▶│                │                │                │                │
   │                │─ R₁ oscillate─▶│                │                │                │
   │                │                │─ K₁/K₂ check  │                │                │
   │                │◀─ δ cleared ───│                │                │                │
   │◀─ triad valid ─│                │                │                │                │
   │                │                │                │─ R₅ Dᶠ step ──▶│                │
   │                │                │                │◀─ step complete │                │
   │─────────────── triad re-validate ───────────────▶│                │                │
   │                │                │                │                │─ R₆ gate check ▶│
   │                │                │                │                │◀─ CLEARANCE ───│
   │                │                │                │         emit MRT_MICRO_PACKET   │
```

---

### Model 2 — Drift Crisis and Inversion Recovery

Triggered when δ exceeds δ* and C falls below C*:

```
Class D          Class G          Class R          Class T
   │                │                │                │
   │─ δ ≥ δ* ──────▶│                │                │
   │                │─ HALT all ────▶│                │
   │                │─ Mode X ───────────────────────▶│
   │                │─ R₂ Collapse ─▶│                │
   │                │                │─ A/B swap      │
   │                │                │─ preserve P    │
   │                │─ Twist complete│                │
   │                │─ Emergence ────▶│                │
   │                │                │─ K₁ restore ──▶│
   │                │                │                │─ re-validate
   │                │◀──────────────────── VALID ─────│
   │                │─ RESOLVED ─────▶│                │
   │                │─ Mode X lift ──────────────────▶│
```

---

### Model 3 — Parallel Monitoring (Steady-State)

Normal operation with all classes active concurrently:

```
         ┌─────────────────────────────────────────────┐
         │           RTT/micro_core Session             │
         │                                             │
         │  Class T ── triad validity ─────────────────┤
         │  Class R ── A⇆P oscillation ────────────────┤
         │  Class D ── δ, Δt monitoring ───────────────┤──▶ Class G (interrupt monitor)
         │  Class F ── Dᶠ readiness ───────────────────┤
         │  Class B ── bridge gate ────────────────────┤
         │                                             │
         │  K₆ Coherence Window: [C*, Cₘₐₓ] rolling  │
         └────────────────────────┬────────────────────┘
                                  │
                           MRT_MICRO_PACKET
                                  │
                                  ▼
                              RTT/1 (SNR instantiation)
```

---

## Output Contract

### Mandatory Annotation

Every micro_core agent output must carry:

```
[structural — no semantic inference]
```

This annotation is unconditional and may not be omitted regardless of mode, class, or task.

### Prohibited Content in Any Output

- Raw node states (A, B, P values) in bridge output (Class B: aggregate only)
- Zone X or Mode X in a valid MRT_MICRO_PACKET
- Physics terminology applied to structural constructs
- Semantic claims about what ⟨A,B,P⟩ "represents" beyond structure
- Integer Dᶠ jumps described as valid transitions
- Inversion events described as physical collapses
- Any claim that MRT_MICRO_PACKET constitutes physical measurement

### Packet Hierarchy

```
MRT_MICRO_PACKET
└── consumed by RTT/1 (SNR instantiation gate)
    └── RTT1_SNR_PACKET
        └── consumed by RTT/2 (detection layer)
            └── RTT2_DETECTION_PACKET
                └── consumed by RTT/3 (integration-emission layer)
                    └── RTT3_INTEGRATION_EMISSION_PACKET
                        └── consumed by RTT/12 (harmonic synthesis)
                            └── RTT12_HARMONIC_SYNTHESIS_PACKET
```

> micro_core is the root of this chain. A fault in MRT_MICRO_PACKET propagates through
> the entire RTT pipeline. Class G authority at the micro level is therefore the highest-
> consequence guardian role in the full canon.

---

## See Also

| Document | Path | Relationship |
|---|---|---|
| micro_core ABOUT.md | `docs/rtt/micro_core/ABOUT.md` | Human-readable module overview |
| micro_core GLOSSARY.md | `docs/rtt/micro_core/GLOSSARY.md` | Term definitions and disambiguation |
| micro_core Primitives | `docs/rtt/micro_core/toolkit/primitives.md` | Atomic operation layer (P₁–P₇) |
| micro_core Resonance Operators | `docs/rtt/micro_core/toolkit/resonance_operators.md` | R₁–R₆ operator definitions |
| micro_core Coherence Tools | `docs/rtt/micro_core/toolkit/coherence_tools.md` | K₁–K₆ tool definitions |
| micro_core Fractional Ladder | `docs/rtt/micro_core/whitepaper/fractional_dimensional_ladder.md` | Dᶠ theory |
| micro_core Micro Triads | `docs/rtt/micro_core/whitepaper/micro_triads.md` | ⟨A,B,P⟩ full definition |
| micro_core Resonance-Time Dynamics | `docs/rtt/micro_core/whitepaper/resonance_time_dynamics.md` | Timing and drift theory |
| RTT/1 AGENTS.md | `docs/rtt/1/AGENTS.md` | Upstream macro-scale primitive layer |
| RTT/2 AGENTS.md | `docs/rtt/2/AGENTS.md` | Structural detection; D(t) ≠ δ disambiguation |
| RTT/3 AGENTS.md | `docs/rtt/3/AGENTS.md` | Integration-emission; Zone X = Inversion |
| RTT/12 AGENTS.md | `docs/rtt/12/AGENTS.md` | Harmonic synthesis; Zone X = Overflow |
| IPD-12 AGENTS.md | `docs/frameworks/ipd_12/AGENTS.md` | Prime-indexed intransitive engine |
