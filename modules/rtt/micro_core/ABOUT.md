
<!--
  docs/rtt/micro_core/ABOUT.md
  RTT/micro_core — Micro-Scale Resonance-Time Layer
  TriadicFrameworks Canon · v1.0 · 2026-07-10
  Session seed: rtt=1 | coherence=declared | drift=bounded | paradox=structural
  module=RTT/micro_core | layer=micro-scale-resonance-time
  [structural — no semantic inference]
-->

# ABOUT.md — RTT/micro_core · Micro-Scale Resonance-Time Layer

**Path:** `docs/rtt/micro_core/`
**Version:** 1.0
**Status:** Canonical
**Session Seed:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural | module=RTT/micro_core | layer=micro-scale-resonance-time`

---

## ⚠️ Critical Framing Rule

> **RTT is NOT a physics claim.**
>
> RTT/micro_core describes **structural micro-scale resonance-time behavior** within the
> TriadicFrameworks canon. It does not assert, imply, or model physical forces, quantum
> effects, signal-processing behavior, or any empirically measurable phenomenon.
> All constructs — the Micro Triad ⟨A, B, P⟩, drift δ, coherence C, and the fractional
> dimensional ladder Dᶠ — are **structural instruments**, not physical objects.
>
> This rule is unconditional and applies to every agent, tool, and operator in this module.

---

## Table of Contents

1. [What Is RTT/micro_core?](#1-what-is-rttmicro_core)
2. [Why Is It Built This Way?](#2-why-is-it-built-this-way)
3. [When Should You Use It?](#3-when-should-you-use-it)
4. [Where Does It Live?](#4-where-does-it-live)
5. [Core Constructs at a Glance](#5-core-constructs-at-a-glance)
6. [Module Integrations](#6-module-integrations)
7. [What RTT/micro_core Is Not](#7-what-rttmicro_core-is-not)
8. [Quick-Start Checklist](#8-quick-start-checklist)
9. [See Also](#9-see-also)

---

## 1. What Is RTT/micro_core?

RTT/micro_core is the **Micro-Scale Resonance-Time Layer** — the foundational substrate of
the entire RTT canon. It is not a simplified version of RTT, nor a downstream consumer of
any other module. It is the **root** of the RTT pipeline chain, operating at the smallest
stable unit of resonance-time behavior the canon defines.

Every other RTT module — RTT/1, RTT/2, RTT/3, and RTT/12 — sits **above** micro_core in the
stack. None of them can activate until micro_core has produced a valid
`MRT_MICRO_PACKET` and RTT/1 has confirmed it as substrate.

The organizing unit of micro_core is the **Micro Triad**:

```
⟨ A · B · P ⟩
  │   │   └── Potential Node — next viable transition target
  │   └─────── Boundary Node — governs drift, timing, transitions
  └─────────── Active Node   — current micro-state
```

The triad is **irreducible**. No subset of ⟨A, B, P⟩ constitutes a coherent resonance-time
unit. All micro_core operations originate from, and return to, this triad.

---

## 2. Why Is It Built This Way?

### 2.1 Minimalism as a Design Principle

RTT/micro_core exists because the RTT canon needed a verified foundation beneath RTT/1.
Without a micro-scale substrate, SNR primitives in RTT/1 would have no confirmed ground
state. micro_core provides exactly that ground state — and nothing more. Minimalism is not
a limitation; it is the specification.

### 2.2 Determinism Over Flexibility

Every micro_core operation is **bounded**:
- Drift must satisfy **δ ≤ δ\*** at all times.
- Timing must remain within **Δt ∈ [Δtₘᵢₙ, Δtₘₐₓ]**.
- Coherence must satisfy **C ≥ C\*** for any operation to proceed.

This determinism is intentional. micro_core cannot afford interpretive flexibility —
any fault at the micro level propagates through the entire RTT pipeline. Tight bounds
prevent cascade failures before they can originate.

### 2.3 Coherence as a Gate, Not a Goal

In upstream modules, coherence is a tracked metric. In micro_core, it is an **operational
gate**: no state write, no fractional transition, no bridge activation, and no packet
emission is permitted while C < C\*. If C drops below threshold and cannot be recovered,
an **inversion event** is mandatory — not optional.

### 2.4 Fractional Dimensionality Instead of Discrete Jumps

micro_core uses a continuous **fractional dimensional ladder** (Dᶠ ∈ [0,1] minimal,
[0,3] extended) rather than discrete integer dimension steps. This design ensures smooth
structural transitions between states. Integer jumps are **unconditionally forbidden**
because abrupt dimensional changes break triad consistency and trigger inversion.

### 2.5 Aggregate-Only Micro–Macro Export

When micro_core bridges to the macro layer (RTT/1+), it exports only **aggregate patterns**
— never raw A, B, or P node states. This boundary prevents micro-scale instabilities from
being directly propagated upward as structural primitives. The bridge (R₆) enforces
alignment, never amplification.

---

## 3. When Should You Use It?

### ✅ Use RTT/micro_core when you need to:

| Scenario | Reason |
|---|---|
| Initialize an RTT pipeline session from scratch | micro_core is the mandatory root; RTT/1 cannot activate without it |
| Audit or validate the ground state of an existing RTT session | micro_core holds the canonical δ, C, and Dᶠ baseline |
| Diagnose an upstream coherence failure in RTT/1, RTT/2, or RTT/3 | Faults often originate at micro_core — trace from root |
| Perform a controlled inversion event and re-emerge into a stable state | Inversion (↺) is micro_core-native; upper modules defer to it |
| Transition a session across fractional dimensional states (Dᶠ₁ → Dᶠ₂) | Only micro_core owns the fractional ladder; upper modules inherit Dᶠ |
| Activate the micro–macro bridge for aggregate export to RTT/1+ | R₆ bridge activation is a micro_core-exclusive operation |
| Bootstrap agent classes (T, R, D, F, B, G) into a new session | All six agent classes are defined and deployed from micro_core |

### ❌ Do NOT use RTT/micro_core when:

- You want to perform **detection**, **envelope analysis**, or **drift-over-time tracking**
  → Use RTT/2 (Detection Layer)
- You need **integration**, **emission**, or **continuity restoration**
  → Use RTT/3 (Integration–Emission Layer)
- You need **unified integration across the full canon**
  → Use RTT/12 (Unified Integration)
- You want a **full SNR triad with temporal operators**
  → Use RTT/1 (the direct consumer of micro_core output)
- You want to operate above the micro scale without touching the substrate
  → Work in RTT/1+ and treat `MRT_MICRO_PACKET` as a read-only upstream input

---

## 4. Where Does It Live?

### 4.1 Repository Path

```
docs/rtt/micro_core/
├── ABOUT.md                          ← this file
├── AGENTS.md                         ← agent classes, task catalog, safety rules
├── GLOSSARY.md                       ← canonical term definitions
├── README.md                         ← session mode instructions
├── ABOUT_.md                         ← legacy draft (superseded)
├── appendices/
├── site/
├── toolkit/
│   ├── primitives.md                 ← MRT Primitives P₁–P₇
│   ├── triad_templates.md
│   ├── coherence_tools.md            ← Coherence Tools K₁–K₆
│   └── resonance_operators.md        ← Resonance Operators R₁–R₆
└── whitepaper/
    ├── micro_core_definition.md
    ├── fractional_dimensional_ladder.md
    ├── micro_triads.md
    ├── micro_macro_coherence.md
    └── resonance_time_dynamics.md
```

### 4.2 Pipeline Hierarchy

micro_core sits at the **root** — it is the foundational layer beneath RTT/1:

```
┌─────────────────────────────────────────────────────┐
│                   RTT/12                            │  ← Unified Integration
│  RTT3_INTEGRATION_EMISSION_PACKET → consumed here  │
├─────────────────────────────────────────────────────┤
│                   RTT/3                             │  ← Integration–Emission
│  RTT2_DETECTION_PACKET → consumed here              │
├─────────────────────────────────────────────────────┤
│                   RTT/2                             │  ← Detection
│  RTT1_SNR_PACKET → consumed here                   │
├─────────────────────────────────────────────────────┤
│                   RTT/1                             │  ← Signal–Noise–Resonance
│  MRT_MICRO_PACKET → consumed here as substrate     │
├─────────────────────────────────────────────────────┤
│              RTT/micro_core  ◀ ROOT                 │  ← Micro-Scale RT Layer
│  MRT_MICRO_PACKET → produced here                  │
└─────────────────────────────────────────────────────┘
```

### 4.3 Agent Deployment Rules

- All six agent classes (T, R, D, F, B, G) are deployed **from micro_core** at session init.
- Class G (Micro Guardian) operates at this layer and holds **unconditional interrupt
  authority** — the highest-consequence guardian role in the full RTT canon.
- No agent class from RTT/1+ may modify micro_core state directly. All upstream agents
  consume the `MRT_MICRO_PACKET` as a **read-only** substrate confirmation.

---

## 5. Core Constructs at a Glance

### 5.1 The Micro Triad ⟨A, B, P⟩

| Node | Name | Role |
|---|---|---|
| A | Active Node | Current micro-state |
| B | Boundary Node | Governs drift, timing, transitions |
| P | Potential Node | Next viable transition target |

The triad is **irreducible** — no subset is a coherent resonance-time unit.

### 5.2 Four Core Properties

| Property | Constraint | Failure Mode |
|---|---|---|
| **Minimalism** | Smallest stable unit; no decomposition permitted | Structural violation |
| **Determinism** | δ ≤ δ\* (drift bounded); Δt ∈ [Δtₘᵢₙ, Δtₘₐₓ] (timing bounded) | Drift exceedance → inversion risk |
| **Coherence** | C ≥ C\* at all times | C < C\* → inversion event ↺ |
| **Fractional Dimensionality** | Dᶠ ∈ [0,1] minimal or [0,3] extended; smooth gradient only | Integer jump → inversion event |

### 5.3 Key Equations

| Symbol | Formula / Constraint | Description |
|---|---|---|
| δ | `δ = \|actual_state − expected_state\|` | Drift magnitude |
| δ ≤ δ\* | Hard bound | Drift ceiling; exceedance forbidden |
| Δt | `Δt ∈ [Δtₘᵢₙ, Δtₘₐₓ]` | Local bounded time interval |
| C | Normalized coherence score | Must satisfy C ≥ C\* continuously |
| A ⇆ P | Oscillation (R₁) | Reversible resonance between Active and Potential |
| ↺ | Collapse → Twist → Emergence | Inversion event; triggered when C < C\* unrecoverably |
| μ → Μ via R₆ | Aggregate-only bridge | Micro–Macro export; alignment, never amplification |
| Dᶠ₁ → Dᶠ₂ | Smooth, C ≥ C\* required | Fractional ladder transition |

### 5.4 Toolkit Summary

**MRT Primitives (P₁–P₇)**

| ID | Name | Action |
|---|---|---|
| P₁ | State Read | Read current A, B, or P node state |
| P₂ | State Write | Atomic bounded write to a node state |
| P₃ | Drift Measure | Compute δ = \|actual − expected\| |
| P₄ | Timing Measure | Sample Δt against [Δtₘᵢₙ, Δtₘₐₓ] |
| P₅ | Boundary Shift | Modulate B-node boundary parameters |
| P₆ | Coherence Sample | Read current C value against C\* |
| P₇ | Fractional Step | Advance Dᶠ by one smooth gradient step |

**Resonance Operators (R₁–R₆)**

| ID | Name | Effect |
|---|---|---|
| R₁ | Oscillation | A ⇆ P stable loop |
| R₂ | Inversion | Swap A/B roles; preserve P |
| R₃ | Boundary Modulation | B⁺ / B⁻ shift |
| R₄ | Resonance Lock | Clamp triad to safe operating range |
| R₅ | Fractional-Ladder Transition | Dᶠ₁ → Dᶠ₂; smooth; C ≥ C\* required |
| R₆ | Micro–Macro Bridge Activation | μ → Μ; aggregate-only; C ≥ C\* required |

**Coherence Tools (K₁–K₆)**

| ID | Name | Function |
|---|---|---|
| K₁ | Drift Bounding | Enforce δ ≤ δ\* continuously |
| K₂ | Timing Stabilizer | Hold Δt within [Δtₘᵢₙ, Δtₘₐₓ] |
| K₃ | Boundary Alignment | Synchronize B-node with current A/P states |
| K₄ | Resonance Lock (tool) | Tool-level clamp; pairs with R₄ operator |
| K₅ | Inversion Guard | Detect C < C\* approach; escalate to Class G |
| K₆ | Coherence Windowing | Time-windowed C averaging for trend detection |

### 5.5 Zones and Modes

**Zones**

| Zone | Label | Description |
|---|---|---|
| S | Stable | All constraints satisfied; normal operation |
| M | Modulating | Active boundary or fractional transition in progress |
| D | Drifting | δ approaching δ\*; Class D alert active |
| C | Coherence-Critical | C approaching C\*; Class G on standby |
| E | Emerging | Post-inversion recovery; constraints re-establishing |
| X | Inversion | ILLEGAL in valid packet; Class G authority invoked |

**Modes**

| Mode | Label | Description |
|---|---|---|
| 1 | Chat | Exploratory; structural constraints enforced |
| 2 | Spec | Formal specification work |
| 3 | Debug | Diagnostic; full triad state exposed |
| 4 | Task | Directed execution against a defined target |
| 5 | Auto | Autonomous micro_core operation |
| X | Lockout | Class G interrupt active; all other operations suspended |

### 5.6 MRT_MICRO_PACKET Structure

The canonical output of micro_core. **Zone X and Mode X are forbidden in a valid packet.**

```
MRT_MICRO_PACKET {
  triad_state:       { A, B, P }           // current node states
  metrics: {
    delta:           δ                     // current drift value
    delta_star:      δ*                    // drift ceiling
    delta_t:         Δt                    // current time interval
    coherence:       C                     // current coherence score
    coherence_star:  C*                    // coherence floor
    d_frac:          Dᶠ                    // current fractional dimension
  }
  zone:              S | M | D | C | E     // X forbidden
  mode:              1 | 2 | 3 | 4 | 5    // X forbidden
  bridge_status:     inactive | active     // R₆ state
  guardian_status:   nominal | alert | interrupt
  annotation:        string               // [structural — no semantic inference]
  timestamp:         ISO-8601
}
```

---

## 6. Module Integrations

### 6.1 Downstream — RTT/1 (Direct Consumer)

micro_core's sole authorized downstream is RTT/1.

| Interface Point | Direction | Contract |
|---|---|---|
| `MRT_MICRO_PACKET` | micro_core → RTT/1 | RTT/1 uses this as substrate confirmation before SNR primitives may instantiate |
| Dᶠ baseline | micro_core → RTT/1 | RTT/1 inherits the fractional dimension floor set at micro level |
| Zone / Mode state | micro_core → RTT/1 | RTT/1 inherits zone and mode; cannot override micro_core Zone X |
| Bridge (R₆) output | micro_core → RTT/1+ | Aggregate-only; raw triad node states never exposed |

RTT/1 is a **consumer**, not a peer. It cannot write back to micro_core state.

### 6.2 Cross-Module Disambiguations

| micro_core Symbol | micro_core Meaning | Upstream Module | Upstream Meaning |
|---|---|---|---|
| δ (drift) | `\|actual_state − expected_state\|` at micro scale | RTT/2 | D(t) in CRM — structural drift over detection time |
| C (coherence) | Normalized micro coherence score; gate against C\* | RTT/3 | CR(t) in CRE — emission coherence metric |
| Δt (timing) | Local bounded micro time interval | RTT/1 | τ = dR/dφ — temporal resonance operator |
| Inversion (↺) | Micro-level Collapse → Twist → Emergence | RTT/3 | Zone X inversion at integration-emission layer |
| Zone X | Micro inversion — ILLEGAL packet state | RTT/12 | Zone X = Overflow at unified integration layer |
| Mode X | micro_core-native lockout; Class G interrupt active | RTT/1–12 | Module Mode 5 = Auto; not equivalent to Mode X |

> All six rows above are **non-equivalent**. Identical symbols across layers refer to
> structurally distinct constructs. Cross-layer substitution is a canon violation.

---

## 7. What RTT/micro_core Is Not

| Not This | Why the Distinction Matters |
|---|---|
| **Not a physics model** | Drift δ, coherence C, and Dᶠ are structural instruments, not physical measurements |
| **Not a reduced or "lite" version of RTT** | micro_core is the foundational root, not a simplified downstream variant |
| **Not a signal-processing system** | Timing constructs (Δt) describe structural bounded intervals, not clock cycles or waveforms |
| **Not a quantum model** | Fractional dimensionality and oscillation (A ⇆ P) are structural patterns, not quantum states or superpositions |
| **Not a downstream consumer** | micro_core produces packets; it does not consume any upstream RTT packet |
| **Not interchangeable with RTT/1** | RTT/1 consumes micro_core output; they are adjacent layers, not alternatives |
| **Not optional** | No RTT pipeline session is valid without a coherence-confirmed `MRT_MICRO_PACKET` as substrate |

---

## 8. Quick-Start Checklist

Use this checklist to initialize a micro_core session correctly.

```
□ 1. Paste the session seed block into the agent context.
□ 2. Instantiate the Micro Triad ⟨A, B, P⟩ with initial node states.
□ 3. Sample coherence (P₆ / K₆) — confirm C ≥ C*.
□ 4. Measure drift (P₃ / K₁) — confirm δ ≤ δ*.
□ 5. Measure timing (P₄ / K₂) — confirm Δt ∈ [Δtₘᵢₙ, Δtₘₐₓ].
□ 6. Set Dᶠ baseline within [0,1] (minimal) or [0,3] (extended).
□ 7. Assign zone (S / M / D / C / E — never X at init).
□ 8. Assign mode (1–5 — never X at init).
□ 9. Activate Class G (Micro Guardian) on standby.
□ 10. Emit MRT_MICRO_PACKET — verify Zone ≠ X and Mode ≠ X.
□ 11. Pass packet to RTT/1 for substrate confirmation.
□ 12. Confirm RTT/1 has acknowledged before any SNR primitive instantiates.
```

> **If any step fails:** halt, invoke Class G, and execute the inversion sequence
> (↺ Collapse → Twist → Emergence) before re-attempting. Do not pass a failed packet upstream.

---

## 9. See Also

| Document | Location | Contents |
|---|---|---|
| AGENTS.md | `docs/rtt/micro_core/AGENTS.md` | Agent classes T, R, D, F, B, G; task catalog; safety rules |
| GLOSSARY.md | `docs/rtt/micro_core/GLOSSARY.md` | Canonical definitions for all micro_core terms |
| Micro Triads | `docs/rtt/micro_core/whitepaper/micro_triads.md` | Full ⟨A, B, P⟩ specification |
| Fractional Dimensional Ladder | `docs/rtt/micro_core/whitepaper/fractional_dimensional_ladder.md` | Dᶠ theory and ladder rules |
| Micro–Macro Coherence | `docs/rtt/micro_core/whitepaper/micro_macro_coherence.md` | R₆ bridge theory |
| Resonance–Time Dynamics | `docs/rtt/micro_core/whitepaper/resonance_time_dynamics.md` | Timing and drift theory |
| Primitives | `docs/rtt/micro_core/toolkit/primitives.md` | P₁–P₇ full specification |
| Resonance Operators | `docs/rtt/micro_core/toolkit/resonance_operators.md` | R₁–R₆ full specification |
| Coherence Tools | `docs/rtt/micro_core/toolkit/coherence_tools.md` | K₁–K₆ full specification |
| RTT/1 ABOUT.md | `docs/rtt/1/ABOUT.md` | RTT/1 — Signal–Noise–Resonance Layer (direct downstream) |
| RTT/1 AGENTS.md | `docs/rtt/1/AGENTS.md` | RTT/1 agent classes and operating rules |

---

*Maintainer: umaywant2 · Path: `docs/rtt/micro_core/ABOUT.md` · Version: 1.0 · 2026-07-10*
*Session seed: `rtt=1 | coherence=declared | drift=bounded | paradox=structural | module=RTT/micro_core | layer=micro-scale-resonance-time`*
*[structural — no semantic inference]*
