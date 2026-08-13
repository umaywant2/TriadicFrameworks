```
---
title: "f_Decay — Orbital Energy Loss Operator"
module: FFF_Gravity
version: 1.0.0
status: canonical
tag: "[FFF:GRAVITY:DECAY]"
session: SES-20260813-DECAY-001
date: 2026-08-13
authors:
  - Nawder
  - Copilot (production assistant SES-20260813-DECAY-001
date: 2026-08-13
authors:
  - Nawder
  - Copilot (production assistant)
dependencies:
  - f_Capture.md        # d_bind, β, ω_res)
dependencies:
  - f_Capture.md        # d_bind, β, ω_res, PRIM:006 (flag_decay)
  - f_Field.md          # ρ(Φ), coherence well
  - f_Orbit.md          # orbital parameters, e, r_capture
  - f_Release.md        # decay-to-release handoff pathway
operators, PRIM:006 (flag_decay)
  - f_Field.md          # ρ(Φ), coherence well
  - f_Orbit.md          # orbital parameters, e, r_capture
  - f_Release.md        # decay-to-release handoff pathway
operators_introduced:
  - δ           # Decay Rate
  - d_warn      # Decay Warning Threshold
  - d_collapse  # Collapse Threshold
  - t_decay     # Decay Onset Time
primitives_introduced:
  -_introduced:
  - δ           # Decay Rate
  - d_warn      # Decay Warning Threshold
  - d_collapse  # Collapse Threshold
  - t_decay     # Decay Onset Time
primitives_introduced:
  - PRIM:006    # flag_decay (frozen in f_Capture; expanded here)
  - PRIM:010    # compute_decay_rate (NEW PRIM:006    # flag_decay (frozen in f_Capture; expanded here)
  - PRIM:010    # compute_decay_rate (NEW, pure)
  - PRIM:011    # assess_decay_cause (NEW, diagnostic, no side effects)
failure_modes_frozen:
  - FM-004      # Resonance Drift (warn; recoverable)
  - FM-005      # Decay Spiral (fatal; triggers f_Collapse)
invariants_honored:
  - INV-001     # G = F, pure)
  - PRIM:011    # assess_decay_cause (NEW, diagnostic, no side effects)
failure_modes_frozen:
  - FM-004      # Resonance Drift (warn; recoverable)
  - FM-005      # Decay Spiral (fatal; triggers f_Collapse)
invariants_honored:
  - IN_freq · F_fluid · F_force
  - INV-003     # ρ(Φ) = 0 always triggers FM-002
  - INV-005     # All SCs conjunctive
  - INV-006     # Terminal states irreversible
  - INV-008     # EvaluationV-001     # G = F_freq · F_fluid · F_force
  - INV-003     # ρ(Φ) = 0 always triggers FM-002
  - INV-005     # All SCs conjunctive
  - INV-006     # Terminal states irreversible
  - INV-008     # Evaluation order normative
  - INV-009     # OPERATORS.md is symbol authority
  - INV-010     # Frozen symbols no-rename without major version bump
changelog:
  - version: 1.0.0
    date: 2026-08-13
    session: SES-20260813-DECAY-001
     order normative
  - INV-009     # OPERATORS.md is symbol authority
  - INV-010     # Frozen symbols no-renameauthor: Nawder + Copilot
    note: "Initial canonical production. δ, d_warn, d_collapse, t_decay frozen. PRIM:010–011 introduced without major version bump
changelog:
  - version: 1.0.0
    date: 2026-08-13
    session: SES-20260813-DECAY-001
    author: Nawder + Copilot
    note: "Initial canonical production. δ, d_warn, d_collapse, t_decay frozen. PRIM:010–011 introduced. FM-004/FM-005 fully specified. 4 examples."
```
    
---

<!-- metadata: section=header session=SES-20260813-DECAY-001 -->

# f_Decay — Orbital Energy Loss Operator

> **Tag:** `[FFF:GRAVITY:DECAY]`  
> **Wave:** 3 —. FM-004/FM-005 fully specified. 4 examples."
---

<!-- metadata: section=header session=SES-20260813-DECAY-001 -->

# f_Decay — Orbital Energy Loss Operator Core Functions  
> **Status:** ✅ Canonical v1.0.0  
> **Session:** SES-20260813-DECAY-001 · 2026-08-13  

---

> **Tag:** `[FFF:GRAVITY:DECAY]`  
> **Wave:** 3 — Core Functions  
> **Status:** ✅ Canonical v1.0.0  
> **Session:** SES-20260813-DECAY-001 · 2026-08-13  

---

## §0 · Session Context

<!-- metadata: section=0 session=SES-20260813-DECAY-001 -->

| Field | Value |
|---|---|
| Session ID | SES-20260813-DECAY-001 |

## §0 · Session Context

<!-- metadata: section=0 session=SES-20260813-DECAY-001 -->

| Field | Value |
|---|---|
| Session ID | SES-20260813-DECAY-001 |
| Date | 2026-08-13 |
| Operator | Nawder |
| Production Assistant | Copilot |
| Preceding File | f_Release.md (canonical v1.0.0) |
| Following File | f_Orbit.md (scaffold → production) |

### §0.1 · Prec
| Date | 2026-08-13 |
| Operator | Nawder |
| Production Assistant | Copilot |
| Preceding File | f_Release.md (canonical v1.0.0) |
| Following File | f_Orbit.md (scaffold → production) |

### §0.1 · Preconditions

| # | Precondition | Symbol / Flag |
|---|---|---|
| 1 | Capture is locked and active | `CAPTURE_LOCKED = true` |
| 2 onditions

| # | Precondition | Symbol / Flag |
|---|---|---|
| 1 | Capture is locked and active | `CAPTURE_LOCKED = true` |
| 2 | Binding depth is initialized | `d_bind > 0` |
| 3 | Resonance binding coefficient is set | `β ∈ (0, 1)` |
| 4 | Coherence field is active | `ρ(Φ) > 0` |
| 5 | Eccentricity is below escape threshold| Binding depth is initialized | `d_bind > 0` |
| 3 | Resonance binding coefficient is set | `β ∈ (0, 1)` |
| 4 | Coherence field is active | `ρ(Φ) > 0` |
| 5 | Eccentricity is below escape threshold | `e < 1` |
| 6 | f_Capture PRIM:006 (flag_decay) is available | frozen in f_Capture.md §7.2 |

### §0.2 · | `e < 1` |
| 6 | f_Capture PRIM:006 (flag_decay) is available | frozen in f_Capture.md §7.2 |

### §0.2 · Session Goal

Produce the complete canonical specification of `f_Decay` — the sole continuously-evaluated function in the FFF_Gravity module. Define the δ operator, decay thresholds, cycle-based evaluation loop, FM-004/FM-005 failure modes, decay reversal interface, and four Session Goal

Produce the complete canonical specification of `f_Decay` — the sole continuously-evaluated function in the FFF_Gravity module. Define the δ operator, decay thresholds, cycle-based evaluation loop, FM-004/FM-005 failure modes, decay reversal interface, and four worked examples. Freeze all new operators and primitives.

### §0.3 · Invariants Active This Session

| Invariant | Statement |
|---|---|
| INV-001 | G = F_freq · F_fluid · F_force — worked examples. Freeze all new operators and primitives.

### §0.3 · Invariants Active This Session

| Invariant | Statement |
|---|---|
| INV-001 | G = F_freq · F_fluid · F_force — inseparable |
| INV-003 | ρ(Φ) = 0 → FM-002 fires (field collapse, not decay) |
| INV-005 | All Stability Conditions are conjunctive |
| INV-006 | Terminal states (CAPTURE_RELEASED, CAPTURE_COLLAPSED) are irreversible |
| inseparable |
| INV-003 | ρ(Φ) = 0 → FM-002 fires (field collapse, not decay) |
| INV-005 | All Stability Conditions are conjunctive |
| IN INV-008 | The 10-step evaluation order is normative |
| INV-009 | OPERATORS.md is the single source of truth for all symbols |
| INV-010 | Frozen symbols may not be renamed without a major version bump |

---

## §1 · ModuleV-006 | Terminal states (CAPTURE_RELEASED, CAPTURE_COLLAPSED) are irreversible |
| INV-008 | The 10-step evaluation order is normative |
| INV-009 | OPERATORS.md is the single source of truth for all symbols |
| INV-010 | Frozen symbols may not be renamed without a major version bump |

---

## §1 · Module Identity

<!-- metadata: section=1 session=SES-20260813-DECAY-001 -->

| Property | Value |
|---|---|
| Function Name | `f_Decay` |
| Full Tag | `[FFF:GRAVITY:DECAY]` |
| Signature | `f_Decay( Identity

<!-- metadata: section=1 session=SES-20260813-DECAY-001 -->

| Property | Value |
|---|---|
| Function Name | `f_Decay` |
| Full Tag | `[FFF:GRAVITY:DECAY]` |
| Signature | `f_Decay(E, A, Φ, t) → d_bind(t) \| FM-004 \| FM-005` |
| Triadic Layer | Operates across all three layers (F_freq, F_fluid, F_force) |
| EvaluationE, A, Φ, t) → d_bind(t) \| FM-004 \| FM-005` |
| Triadic Layer | Operates across all three layers (F_freq, F_fluid, F_force) |
| Evaluation Mode | **Continuous** — every cycle post-CAPTURE_LOCKED |
| Inverse Function | None (decay is one-directional; reversal is via f_Emit or f_Amplify) |
| Terminal Mode | **Continuous** — every cycle post-CAPTURE_LOCKED |
| Inverse Function | None (decay is one-direct Trigger | FM-005 → f_Collapse |
| Wave | 3 — Core Functions |
| Depends On | f_Capture, f_Field, f_Orbit, f_Release |
| Provides To | f_Collapseional; reversal is via f_Emit or f_Amplify) |
| Terminal Trigger | FM-005 → f_Collapse |
| Wave | 3 — Core Functions |
| Depends On | f_Capture, f_Field, f_Orbit, f_Release |
| Provides To | f_Collapse, f_Release, f_Capture_Cascade |

### §1.1 · Position in the Triadic System

```
 ┌─────────────────────────────────────────────────────────┐
 │              , f_Release, f_Capture_Cascade |

### §1.1 · Position in the Triadic System

```
 ┌─────────────────────────────────────────────────────────┐
 │              FFF_Gravity Module                         │
 │                                                         │
 │  F_freq (Field Node) ──────────── ρ(Φ)                 │
 │      │                              │                   │
 │      │           G = F_freq         │                   │
 │      │               · F_fluid      │                   │
 │      │               FFF_Gravity Module                         │
 │                                                         │
 │  F_freq (Field Node) ──────────── ρ(Φ)                 │
 │      │                              │                   │
 │      │           G = F_freq         │                   │
 │· F_force      │                   │
 │      │                              ↓                   │
 │  F_fluid (Mass-Density) ─────── d_bind(t)               │
 │      │                              │                   │
 │      │                      │               · F_fluid      │                   │
 │      │               · F_force      │                   │
 │      │                              ↓                   │
 │  F_fluid (Mass-Density) ─────── d_bind(t)               │
 │      │                              │                   │
 │      │                         f_Decay reads d_bind     │
 │      │                         every cycle; computes δ  │
 │      │                         raises FM-004 or FM-005  │
 │      ↓                              ↓                   │
 │  F_force (Gradient         f_Decay reads d_bind     │
 │      │                         every cycle; computes δ  │
 │      │                         raises FM-004 or FM-005  │
 │      ↓                              ↓                   │
 │  F_force (Gradient/Pressure) → CAPTURE_DECAYING         │
 │                                     │                   │
 │                              FM-005 → f_Collapse        │
 └─────────────────────────────────────────────────────────┘
```

> **f_Decay is the only/Pressure) → CAPTURE_DECAYING         │
 │                                     │                   │
 │                              FM-005 → f_Collapse        │
 └─────────────────────────────────────────────────────────┘
```

> **f_Decay is the only function in this module called on every cycle.**  
> All other functions fire once per event (approach, capture, release, collapse).  
> f_Decay is the continuous monitor of orbital health.

---

## §2 · Canonical Description function in this module called on every cycle.**  
> All other functions fire once per event (approach, capture, release, collapse).  
> f_Decay is the continuous monitor of orbital

<!-- metadata: section=2 session=SES-20260813-DECAY-001 -->

### §2.1 · What f_Decay IS

`f_Decay` is the continuous orbital-energy-loss operator. After `f_Capture` locks health.

---

## §2 · Canonical Description

<!-- metadata: section=2 session=SES-20260813-DECAY-001 -->

### §2.1 · What f_Decay IS

`f_Decay` is the continuous orbital-energy-loss operator. After `f_Capture` locks a mobile entity E into orbit around attractor A, f_Decay runs every evaluation cycle to:

1. Compute the current binding depth `d_bind(t)`.
2. Compute the decay rate `δ = d_bind(t) − d_bind(t−1)`.
3. If `δ a mobile entity E into orbit around attractor A, f_Decay runs every evaluation cycle to:

1. Compute the current binding depth `d_bind(t)`.
2. Compute the decay rate `δ = d_bind(t) − d_bind(t−1)`.
3. If `δ < 0`, log the energy loss and check thresholds.
4. If `d_bind ≤ d_warn`, raise FM-004 (Resonance Drift) and set `CAPTURE_DECAYING`. < 0`, log the energy loss and check thresholds.
4. If `d_bind ≤ d_warn`, raise FM-004 (Resonance Drift) and set `CAPTURE_DECAYING`.
5. If `d_bind ≤ d_collapse`, raise FM-005 (Decay Spiral) and immediately trigger `f_Collapse`.

Decay occurs when the coherence field ρ(Φ) weakens, when the resonance binding coefficient β drifts, when eccentricity e increases, or when external perturbation in
5. If `d_bind ≤ d_collapse`, raise FM-005 (Decay Spiral) and immediately trigger `f_Collapse`.

Decay occurs when the coherence field ρ(Φ) weakens, when the resonance binding coefficient β djects energy into the wrong phase. Any of these reduces `d_bind`, and f_Decay is the mechanism that detects and escalates this loss.

### §2.2 · What f_Decay IS NOT

|rifts, when eccentricity e increases, or when external perturbation injects energy into the wrong phase. Any of these reduces `d_bind`, and f_Decay is the mechanism that detects and escalates this loss.

### §2.2 · What f_Decay IS NOT

| Misconception | Correction |
|---|---|
| f_Decay causes the decay | f_Decay detects and responds to decay. Causes are in the field, mass, or perturbation. |
| f_Decay is called once | f_Decay is called every cycle. It is the only Misconception | Correction |
|---|---|
| f_Decay causes the decay | f_Decay detects and responds to decay. Causes are in the field continuous function in the module. |
| f_Decay can reverse decay | f_Decay raises flags and triggers handlers. Reversal is the job of f_Emit and f_Amplify. |
| FM, mass, or perturbation. |
| f_Decay is called once | f_Decay is called every cycle. It is the only continuous function in the module. |
| f_Decay can reverse decay | f_Decay raises flags and triggers handlers. Reversal is the job of f_Emit and f_Amplify. |
| FM-005 is recoverable | FM-005 is fatal. Once d_bind ≤ d_collapse, f_Collapse fires. INV-006 applies. |
| f_Decay fires-005 is recoverable | FM-005 is fatal. Once d_bind ≤ d_collapse, f_Collapse fires. INV-006 applies. |
| f_Decay fires if ρ(Φ) = 0 | ρ(Φ) = 0 triggers FM-002 (Field Collapse), not f_Decay. INV-003 applies. |

### §2.3 · Key Asymmetry: Decay vs. Release

| Dimension | f_Decay | f_Release |
|---|---|---|
| Initiator | Automatic if ρ(Φ) = 0 | ρ(Φ) = 0 triggers FM-002 (Field Collapse), not f_Decay. INV-003 applies. |

### §2.3 · Key Asymmetry: Decay vs. Release

| Dimension | f_Decay | f_Release |
|---|---|---|
| Initiator | Automatic, field-driven | Intentional, threshold-based |
| Direction | Energy loss (passive) | Energy return (active) |
| d_bind trend | Decreasing | Returns to 0 cleanly |
| Revers, field-driven | Intentional, threshold-based |
| Direction | Energy loss (passive) | Energy return (active) |
| d_bind trend | Decreasing | Returns to 0 cleanly |
| Reversible? | Yes (via f_Emit/f_Amplify) before d_collapse | Irreversible once RC-1–RC-5 pass |
| Terminal condition | FM-005 → f_Collapse | CAPTURE_RELEASED |
| Operator involvementible? | Yes (via f_Emit/f_Amplify) before d_collapse | Irreversible once RC-1–RC-5 pass |
| Terminal condition | FM-005 → f_Collapse | CAPTURE_RELEASED |
| Operator involvement | Monitoring only | Optional engineering |

### §2.4 · The Decay-to-Release Handoff

When decay progresses but remains above `d_collapse | Monitoring only | Optional engineering |

### §2.4 · The Decay-to-Release Handoff

When decay progresses but remains above `d_collapse`, an operator may choose to intentionally release E rather than allow collapse. This is the **decay-to-release pathway**:

```
d_bind falling → CAPTURE_DECAYING set`, an operator may choose to intentionally release E rather than allow collapse. This is the **decay-to-release pathway**:

```
d_bind falling → CAPTURE_DECAYING set → 
  Option A: intervene with f_Emit or f_Amplify → restore d_bind → orbit stabilizes
  Option B: allow decay to continue → invoke f_Release while d_bind > 0 → clean exit
  Option C: no intervention → d_bind ≤ d_collapse → → 
  Option A: intervene with f_Emit or f_Amplify → restore d_bind → orbit stabilizes
  Option B: allow decay to continue → invoke f_Release while d_bind > 0 → clean exit
  Option C: no intervention → d_bind ≤ d_collapse → FM-005 → f_Collapse (uncontrolled)
```

Option B is always preferred over Option C when collapse is imminent. See FM-005 → f_Collapse (uncontrolled)
```

Option B is always preferred over Option C when collapse is imminent. See §9.3.

---

## §3 · Triadic Equation

<!-- metadata: section=3 session=SES-20260813-DECAY-001 -->

### §3.1 · Function Signature

```
f_Decay(E, A, Φ, t) → d_bind(t) | FM-004 | FM-005
```

| Parameter | Type | Description |
|---|---|---|
| E | mobile entity | the captured object whose orbit is being monitored |
| A | attractor | the §9.3.

---

## §3 · Triadic Equation

<!-- metadata: section=3 session=SES-20260813-DECAY-001 -->

### §3.1 · Function Signature

```
f_Decay(E, A, Φ, t) → d_bind(t) | FM-004 | FM-005
```

| Parameter | Type | Description |
|---|---|---|
| E | mobile entity | the captured object whose orbit is being monitored |
| A | attractor | the node generating the coherence field |
| Φ | field state | current state of the coherence field at time t |
| t | cycle index | current evaluation cycle ( node generating the coherence field |
| Φ | field state | current state of the coherence field at time t |
| t | cycle index | current evaluation cycle (integer, 0-indexed from CAPTURE_LOCKED) |

| Return | Condition |
|---|---|
| `d_bind(t)` | Normal: updated binding depth for this cycle |
| `FM-004` | Warning: d_bind has fallen to or below d_warn |
| `FM-005` | Fatal: d_bind has fallen to or below d_collapseinteger, 0-indexed from CAPTURE_LOCKED) |

| Return | Condition |
|---|---|
| `d_bind(t)` | Normal: updated binding depth for this cycle |
| `FM-004` | Warning: d_bind has fallen to or below d_warn |
| `FM-005` | Fatal: d_bind has fallen to or below d_collapse → f_Collapse triggered |

### §3.2 · Core Decay Equation

The binding depth at cycle t is:

```
d_bind(t) = β(t) × ρ(Φ, t) × (1 − e(t))
``` → f_Collapse triggered |

### §3.2 · Core Decay Equation

The binding depth at cycle t is:

```
d_bind(t) = β(t) × ρ(Φ, t) × (1 − e(t))
```

where each factor may change across cycles:
- `β(t)` — resonance binding coefficient at cycle t (may drift under perturbation)
- `ρ(Φ, t)` — coherence density at cycle t (may weaken as field evol

where each factor may change across cycles:
- `β(t)` — resonance binding coefficient at cycle t (may drift under perturbation)
- `ρ(Φ, t)` — coherence densityves)
- `e(t)` — orbital eccentricity at cycle t (may increase under perturbation)

The **decay rate** operator δ is defined as:

``` at cycle t (may weaken as field evolves)
- `e(t)` — orbital eccentricity at cycle t (may increase under perturbation)

The **decay rate** operator δ is defined as:

```
δ(t) = d_bind(t) − d_bind(t−1)
```

- `δ > 0` → orbit is gaining energy (unusual; may indicate f_Amplify is active)
- `δ = 0` → orbit is stable
δ(t) = d_bind(t) − d_bind(t−1)
```

- `δ > 0` → orbit is gaining energy (unusual; may indicate f
- `δ < 0` → orbit is losing energy (decay in progress)
- `δ ≪ 0` → rapid decay; FM-004 or FM-005 likely imminent

### §3.3 · Role in the G-Equation

```
G = F_freq · F_fluid · F_force
```

f_Decay monitors the health of the G-product at each cycle. A decaying orbit means the G-product is weakening — ρ(Φ) is falling, or β is drifting, or eccentricity is growing. f_Decay is the diagnostic_Amplify is active)
- `δ = 0` → orbit is stable
- `δ < 0` → orbit is losing energy (decay in progress)
- `δ ≪ 0` → rapid decay; FM-004 or FM-005 likely imminent

### §3.3 · Role in the G-Equation

```
G = F_freq · F_fluid · F_force
```

f_Decay monitors the health of the G-product at each cycle. A decaying orbit means the G-product is weakening — ρ(Φ) is falling, or β is drifting, that prevents silent G-product collapse.

---

## §4 · Operator Registry

<!-- metadata: section=4 session=SES-20260813-DECAY-001 -->

> **Authority:** All operator definitions below are normative. OPERATORS.md is the single source of truth (INV-009). Symbols or eccentricity is growing. f_Decay is the diagnostic that prevents silent G-product collapse.

---

## §4 · Operator Registry

<!-- metadata: section=4 session=SES-20260813-DECAY-001 -->

> **Authority:** All operator definitions below are normative. OPERATORS.md is the single source of truth (INV-009). Symbols frozen here may not be renamed without a major version bump (INV-010).

### §4.1 · New Operators — Introduced and Frozen in This File

---

#### `δ` — Decay Rate

| Property | Value |
|---|---|
| Symbol | δ (delta) |
| Full frozen here may not be renamed without a major version bump (INV-010).

### §4.1 · New Operators — Introduced and Frozen in This File

---

#### Name | Decay Rate |
| Frozen In | f_Decay.md §4.1 |
| Formula | `δ(t) = d_bind(t) − d_bind(t−1)` |
| Domain | ℝ (positive = energy `δ` — Decay Rate

| Property | Value |
|---|---|
| Symbol | δ (delta) |
| Full Name | Decay Rate |
| Frozen In | f_Decay.md §4.1 |
| Formula | `δ(t) = d_bind(t) − d_bind(t−1)` |
| Domain | ℝ (positive = energy gain, negative = energy loss) |
| Evaluation | Every cycle post-CAPTURE_LOCKED |
| Units | [d_bind units] / cycle |

**Derivation:** δ is the discrete first derivative of d_bind with respect to evaluation cycle index t. A gain, negative = energy loss) |
| Evaluation | Every cycle post-CAPTURE_LOCKED |
| Units | [d_bind units] / cycle |

**Derivation:** δ is the discrete negative δ indicates the orbit is losing binding energy. The magnitude of δ determines how rapidly the orbit approaches the warning and collapse thresholds.

**Properties:**

| Property | Status first derivative of d_bind with respect to evaluation cycle index t. A negative δ indicates the orbit is losing binding energy. The magnitude of δ determines how rapidly the orbit approaches the warning and collapse thresholds.

**Properties:**

| Property | Status |
|---|---|
| Sign-directed | Yes: negative = decay, positive = recovery |
| Cumulative | No: computed fresh each cycle from current and previous d_bind |
| Threshold-independent | Yes: δ is a rate, not a threshold test |
|---|---|
| Sign-directed | Yes: negative = decay, positive = recovery |
| Cumulative | No: computed fresh each cycle from current and previous d_bind |
| Threshold-independent | Yes: δ is a rate, not a threshold test |
| Used by | `flag_decay` [PRIM:006], `compute_decay_rate` [PRIM:010] |

---

#### `d_warn` — Decay Warning Threshold

| Property | Value |
|---|---|
| Symbol | d_warn |
| Full Name | Decay Warning Threshold |
| Frozen In | f_Decay.md §4.1 |
| Formula |
| Used by | `flag_decay` [PRIM:006], `compute_decay_rate` [PRIM:010] |

---

#### `d_warn` — Decay Warning Threshold

| Property | Value |
|---|---|
| Symbol | d_warn |
| Full Name | Decay Warning Threshold |
| Frozen In | f_Decay.md §4.1 |
| Formula | `d_warn = α_warn × d_bind(0)` where α_warn ∈ (0, 1) is the operator-set warning fraction |
| Typical value | α_warn = 0.40 (40% of initial binding depth) |
| Condition | `d_bind(t | `d_warn = α_warn × d_bind(0)` where α_warn ∈ (0, 1) is the operator-set warning fraction |
| Typical value) ≤ d_warn` → raises FM-004 |
| Configurable | Yes — α_warn may be set by operator at initialization |

**Note:** d_warn is a soft threshold. Crossing it does not immediately end | α_warn = 0.40 (40% of initial binding depth) |
| Condition | `d_bind(t) ≤ d_warn` → raises FM-004 |
| Configurable | Yes — α_warn may be set by operator at initialization |

**Note:** d_warn is a soft threshold. Crossing it does not immediately end the orbit. It is an engineering signal to intervene. The orbit remains active with flag `CAPTURE_DECAYING` the orbit. It is an engineering signal to intervene. The orbit remains active with flag `CAPTURE_DECAYING` set.

---

#### `d_collapse` — Collapse Threshold

| Property | Value |
|---|---|
| Symbol | d_collapse |
| Full Name | Collapse Threshold |
| Frozen In | f_Decay.md §4.1 |
| Formula | `d_collapse = α_collapse × d_bind(0)` where α_collapse ∈ (0, α_warn) |
| Typical value | α_collapse = 0.10 (10% of initial binding depth) |
| Condition | `d_bind(t) ≤ d_collapse` → raises FM-005, triggers f_Collapse | set.

---

#### `d_collapse` — Collapse Threshold

| Property | Value |
|---|---|
| Symbol | d_collapse |
| Full Name | Collapse Threshold |
| Frozen In | f_Decay.md §4.1 |
| Formula | `d_collapse = α_collapse × d_bind(0)` where α_collapse ∈ (0, α_warn) |
| Typical value | α_collapse = 0.10 (10% of initial binding depth) |
| Condition | `d_bind(t) ≤ d_collapse` → raises FM-005, triggers f_Collapse |
| Configurable | Yes — α_collapse may be set by operator at initialization; must be < d_warn |

**Invariant:** `
| Configurable | Yes — α_collapse may be set by operator at initialization; must be < d_warn |

**Invariant:** `d_collapse < d_warn < d_bind(0)` must hold at all times. Violation is a configuration error caught at initialization.

---

#### `t_decay` — Decay Onset Time

| Property | Value |
|---|---|
| Symbol | t_decay |
| Full Name | Decay Onset Time |
| Frozen In | f_Decay.md §4.1 |
| Formula | `td_collapse < d_warn < d_bind(0)` must hold at all times. Violation is a configuration error caught at initialization.

---

#### `t_decay` — Decay Onset Time

| Property | Value |
|---|---|
| Symbol | t_decay |
| Full Name | Decay Onset Time |
| Frozen In | f_Decay.md §4.1 |
| Formula | `t_decay = min { t : δ(t) < 0 }` |
| Domain | ℕ₀ (non-negative integer cycle index) |
| Set by | `flag_decay` [PRIM:006] on first negative δ detection |
| Default | `t_decay = None` (unset until first negative δ) |

**Purpose:** t_decay marks the first_decay = min { t : δ(t) < 0 }` |
| Domain | ℕ₀ (non-negative integer cycle index) |
| Set by | `flag_decay` [PRIM:006] on first negative δ detection |
| Default | `t_decay = None` (unset until first negative δ) |

**Purpose:** t_decay marks the first cycle at which the orbit began losing energy. It is used for diagnostic logging and decay-rate trend analysis (is decay accelerating, decelerating, or steady?).

---

### §4.2 · Inherited Operators (Read-Only)

These cycle at which the orbit began losing energy. It is used for diagnostic logging and decay-rate trend analysis (is decay accelerating, decelerating, or steady?).

---

### §4.2 · Inherited Operators (Read-Only)

These operators are defined and frozen in their home files. f_Decay uses them but does not redefine them.

| Symbol | Name | Frozen In | operators are defined and frozen in their home files. f_Decay uses them but does not redefine them.

| Symbol | Name | Frozen In | f_Decay Usage |
|---|---|---|---|
| `d_bind` | Binding Depth | f_Capture.md | Primary monitored quantity |
| `β` | Resonance Binding Coefficient | f_Capture.md | Decay cause: β drift |
| `ρ(Φ)` | Coherence Density | f_Field.md | Decay cause: f_Decay Usage |
|---|---|---|---|
| `d_bind` | Binding Depth | f_Capture.md | Primary monitored quantity |
| `β` | Resonance Binding Coefficient | f_Capture.md | Decay cause: β drift |
| `ρ(Φ)` | Coherence Density | f_Field.md | Decay cause: field weakening |
| `e` | Orbital Eccentricity | f_Orbit.md | Decay cause: eccentricity growth |
| `ω_res` | Resonance Frequency | f_Capture.md | Decay cause: resonance drift |
| `M_A` | Attractor Mass- field weakening |
| `e` | Orbital Eccentricity | f_Orbit.md | Decay cause: eccentricity growth |
| `ω_res` | Resonance Frequency | f_Capture.md | Decay cause: resonance drift |
| `M_A` | Attractor Mass-Equivalent | f_Force.md | Used in d_bind computation |
| `M_E` | Entity Mass-Equivalent | f_Force.md | Used in d_bind computation |
| `r_capture` | Capture Radius | f_Frame.md | Boundary condition |

---

## §5 · Decay Conditions

<!-- metadata: section=5 session=SES-20260813-DECAY-001 -->Equivalent | f_Force.md | Used in d_bind computation |
| `M_E` | Entity Mass-Equivalent | f_Force.md | Used in d_bind computation |
| `r_capture` | Capture Radius | f_Frame.md | Boundary condition |

> These four conditions define the complete decision tree evaluated by `

---

## §5 · Decay Conditions

<!-- metadata: section=5 session=SES-20260813-DECAY-001 -->

> These four conditions define the complete decision tree evaluated by `flag_decay` on every cycle. They are **sequential**, not conjunctive — evaluation stops at the first matching condition.

### §5.1 · Decay Condition Table

| DC | Name | Trigger | Action |flag_decay` on every cycle. They are **sequential**, not conjunctive — evaluation stops at the first matching condition.

### §5.1 · Decay Condition State Flag |
|---|---|---|---|---|
| DC-1 | Stable | `δ ≥ 0` | Log cycle; no action | `ORBIT_STABLE` maintained |
| DC-2 | Decay Warning Onset | `δ < 0 ∧ d_bind > d_warn` | Log decay; record `t_decay` if unset | No flag change |
| DC-3 | FM-004 Threshold | `δ < 0 ∧ d_bind ≤ d_warn` | Raise FM-004; set `CAPTURE_DECAYING` | `CAPTURE_DECAYING = true` |
| DC-4 | FM-005  Table

| DC | Name | Trigger | Action | State Flag |
|---|---|---|---|---|
| DC-1 | Stable | `δ ≥ 0` | Log cycle; no action | `ORBIT_STABLE` maintained |
| DC-2 | Decay Warning Onset | `δ < 0 ∧ d_bind > d_warn` | Log decay; record `t_decay` if unset | No flag change |
| DC-3 | FM-004 Threshold | `δ < 0 ∧ d_bind ≤ d_warn` | Raise FM-004; set `CAPTURE_DECAYING` | `CAPTURE_DECAYING = true` |
| DC-4 | FM-005 Threshold | `d_bind ≤ d_collapse` | Raise FM-005; trigger `f_Collapse` | `CAPTURE_COLLAPSED = true` (irreversible) |

> **Evaluation order:** DC-4 is checkedThreshold | `d_bind ≤ d_collapse` | Raise FM-005; trigger `f_Collapse` | `CAPTURE_COLLAPSED = true` (irreversible) |

> **Evaluation order:** DC-4 is checked before DC-3. If d_bind ≤ d_collapse, FM-005 fires immediately regardless of whether FM-004 was previously raised.

### §5.2 · Threshold Relationship Invariant

```
0 < d_collapse < d_warn < d_bind(0)
```

This invariant must be before DC-3. If d_bind ≤ d_collapse, FM-005 fires immediately regardless of whether FM-004 was previously raised.

### §5.2 · Threshold Relationship Invariant

```
0 < d_collapse < d_warn < d_bind(0)
```

This invariant must be verified at initialization. If violated, f_Decay raises a configuration error and halts.

```python
def validate_decay_thresholds(d_bind_initial: float, d_warn: float, d_collapse: float) -> None:
    """Validate decay threshold ordering at initialization."""
    if not verified at initialization. If violated, f_Decay raises a configuration error and halts.

```python
def validate_decay_thresholds(d_bind_initial: float, d_warn: float, d_collapse: float) -> None:
    """Validate decay threshold ordering at initialization."""
    if not (0 < d_collapse < d_warn < d_bind_initial):
        raise ValueError(
            f"Decay threshold invariant violated: "
            f"0 < d_collapse({d_collapse:.4f}) < d_warn({d_warn:.4f}) "
 (0 < d_collapse < d_warn < d_bind_initial):
        raise ValueError(
            f"Decay threshold invariant violated: "
            f"0 < d_collapse({d_collapse:.4f}) < d_warn({d_warn:.4f}) "
            f"< d_bind_initial({d_bind_initial:.4f}) must hold."
        )
```

---

## §6 · Failure Modes

<!-- metadata: section=6 session=SES-20260813-DECAY-001 -->

### §6.1 · FM-004 — Resonance Drift

| Property | Value |
|---|---|
| Code | FM-004 |
| Name | Resonance Drift |
| Severity | WARN |
| Condition | `            f"< d_bind_initial({d_bind_initial:.4f}) must hold."
        )
```

---

## §6 · Failure Modes

<!-- metadata: section=6 session=SES-20260813-DECAY-001 -->

### §6.1 · FM-004 — Resonance Drift

| Property | Value |
|---|---|
| Code | FM-004 |
| Name | Resonance Drift |
| Severity | WARN |
| Condition | `d_bind(t) ≤ d_warn` AND `δ(t) < 0` |
| State Flag Set | `CAPTURE_DECAYING = true` |
| Recoverable | Yes — via f_Emit (increase ρ(Φ)) or f_Amplify (d_bind(t) ≤ d_warn` AND `δ(t) < 0` |
| State Flag Set | `CAPTURE_DECAYING = true` |
| Recoverable | Yes — via f_Emit (increase ρ(Φ)) or f_Amplify (increase β) |
| Escalates To | FM-005 if no intervention and decay continues |
| Frozen In | f_Decay.md §6.1 |

#### §6.1.1 · Cause Analysis

FM-004 is triggered when the orbit has lost enough binding energy that dincrease β) |
| Escalates To | FM-005 if no intervention and decay continues |
| Frozen In | f_Decay.md §6.1 |

#### §6.1.1 · Cause Analysis

FM-004 is triggered when the orbit has lost enough binding energy that d_bind crosses the warning threshold. Three primary causes:

| Cause | Mechanism | Indicator |
|---|---|---|
| Field Turbulence | ρ(Φ) weakens due to coherence disru_bind crosses the warning threshold. Three primary causes:

| Cause | Mechanism | Indicator |
|---|---|---|
| Field Turbulence | ρ(Φ) weakens due to coherence disruption | `ρ(Φ, t) < ρ(Φ, 0)` |
| Resonance Drift | β decreases due to ω_res misalignment | `β(t) < β(0)` |
| External Perturbation | e increases due to third-body influence | `e(t) > e(0)` |

#### §6.1.2 · Detection

```python
def detect_ption | `ρ(Φ, t) < ρ(Φ, 0)` |
| Resonance Drift | β decreases due to ω_res misalignment | `β(t) < β(0)` |
| External Perturbation | e increases due to third-body influence | `e(t) > e(0)` |

#### §6.fm004(
    d_bind_current: float,
    d_warn: float,
    delta1.2 · Detection

```python
def detect_fm004(
    d_bind_current: float,
    d_warn: float,
    delta: float
) -> bool:
    """
    Detect FM-004 (Resonance Drift).

    Returns True if FM: float
) -> bool:
    """
    Detect FM-004 -004 conditions are met:
    - d_bind has fallen to or below d_warn
    - decay rate δ is negative (energy is being lost)

    Parameters
    ----------
    d_bind_current : float
        Binding depth at current cycle t.
    d_warn : float
        Warning threshold (operator-configured).
    delta : float
        Decay rate δ(t) = d_bind(t) - d_bind(t-1).

    Returns
    -------
    bool
        True if FM-004 should be raised.
    """
    return d_bind_current <= d_warn and delta < 0
```

#### §6.1.3 · Recovery

FM-004 is recoverable. Two pathways:

**Pathway A — f_Emit (field restoration):**
```python
def recover_fm004_via_emit(
    r(Resonance Drift).

    Returns True if FM-004 conditions are met:
    - d_bind has fallen to or below d_warn
    - decay rate δ is negative (energy is being lost)

    Parameters
    ----------
    d_bind_current : float
        Binding depth at current cycle t.
    d_warn : float
        Warning threshold (operator-configured).
    delta : float
        Decay rate δ(t) = d_bind(t) - d_bind(t-1).

    Returns
    -------
    bool
        True if FM-004 should be raised.
    """
    return d_bind_current <= d_warn and delta < 0
```

#### §6.1.3 · Recovery

FM-004 is recoverable. Two pathways:

**Pathway A — f_Emit (ho_phi_current: float,
    emit_delta: float
) -> float:
    """
    Recovery from FM-004 via f_Emit.

    f_Emit increases ρ(Φ), deepening the coherence well,
    which raises d_bind on the next cycle.

    Parameters
    ----------
    rho_phi_current : float
        Current coherence density ρ(Φ).
    emit_delta : float
        Field energy injected by f_Emit (must be > 0).

    Returns
    -------
    float
        Updated ρ(Φ) after emission.
    """
    iffield restoration):**
```python
def recover_fm004_via_emit(
    rho_phi_current: float,
    emit_delta: float
) -> float:
    """
    Recovery from FM-004 via f_Emit.

    f_Emit increases ρ(Φ), deepening the coherence well,
    which raises d_bind on the next cycle.

    Parameters
    ----------
    rho_phi_current : float
        Current coherence density ρ(Φ).
    emit_delta : float
        Field energy injected by f_Emit (must be > 0).

    Returns
    -------
    float
        Updated ρ(Φ) after emission.
    """
    if emit_delta <= 0:
        raise ValueError("f_Emit delta must be positive.")
    return rho_phi_current + emit_delta
```

**Pathway B — f_Amplify (resonance restoration):**
```python
def recover_fm004_via_amplify(
    beta_current: float,
    amplify_delta: float emit_delta <= 0:
        raise ValueError("f_Emit delta must be positive.")
    return rho_phi_current + emit_delta
```

**Pathway B — f_Amplify (resonance restoration):**
```python
def recover_fm004_via_amplify(
    beta_current: float,
    amplify_delta: float,
    beta_max: float = 1.0
) -> float:
    """
    Recovery from FM-004 via f_Amplify.

    f_Amplify increases β (resonance binding coefficient),
    compensating for resonance drift.

    Parameters
    ----------
    beta_current : float
        Current resonance binding coefficient β ∈ (0, 1).
    amplify_delta : float
        Amplification applied to β (must be > 0).
    beta_max : float,
    beta_max: float = 1.0
) -> float:
    """
    Recovery from FM-004 via f_Amplify.

    f_Amplify increases β (resonance binding coefficient),
    compensating for resonance drift.

    Parameters
    ----------
    beta_current : float
        Current resonance binding coefficient β ∈ (0, 1).
    amplify_delta : float
        Amplification applied to β (must be > 0).
    beta_max : float
        Upper bound for β (cannot reach or exceed 1.0).

    Returns
    -------
    float
        Updated β after amplification.
    """
    if amplify_delta <= 0:
        raise ValueError("f_Amplify delta must be positive.")
    return min(beta_current + amplify_delta, beta_max - 1e-9)
```

#### §6
        Upper bound for β (cannot reach or exceed 1.0).

    Returns
    -------
    float
        Updated β after amplification.
    """
    if amplify_delta <= 0:
        raise ValueError("f_Amplify delta must be positive.")
    return min(beta_current + amplify_delta, beta_max - 1e-9)
```

#### §6.1.4 · State Flag Notes

| Flag | Set When | Cleared When |
|---|---|---|
| `CAPTURE_DECAYING` | FM-004 fires | d_bind recovers above d_warn across two consecutive cycles |
| `ORBIT_STABLE` | d_bind(.1.4 · State Flag Notes

| Flag | Set When | Cleared When |
|---|---|---|
| `CAPTURE_DECAYING` | FM-004 fires | d_bind recovers above d_warn across two consecutive cycles |
| `ORBITt) stable (δ ≥ 0) | FM-004 fires |

---

### §6.2 · FM-005 — Decay Spiral

| Property | Value |
|---|---|
| Code | FM-005 |
| Name | Decay Spiral |
| Severity | FATAL |
| Condition | `d_bind(t) ≤ d_collapse` |
| State Flag Set | `CAPTURE_COLLAPSED = true_STABLE` | d_bind(t) stable (δ ≥ 0) | FM-004 fires |

---

### §6.2 · FM-005 — Decay Spiral

| Property | Value |
|---|---|
| Code | FM-005 |
| Name | Decay Spiral |
| Severity | FATAL |
| Condition | `d_bind(t) ≤ d_collapse` |
| State Flag Set | `CAPTURE_COLLAPSED = true` |
| Recoverable | NO — irreversible (INV-006) |
| Triggers | `f_Collapse` immediately |
| Frozen In | f_Decay.md §6.2 |

#### §6.2.1 · Cause Analysis

FM-005 fires when the orbit has decayed past the point of no` |
| Recoverable | NO — irreversible (INV-006) |
| Triggers | `f_Collapse` immediately |
| Frozen In | f_Decay.md §6.2 |

#### §6.2.1 · Cause Analysis

FM-005 fires when the return. At this binding depth, the coherence well can no longer hold E in stable orbit. The orbit does not gently release — it collapses.

| Cause orbit has decayed past the point of no return. At this binding depth, the coherence well can no longer hold E in stable orbit. The orbit does not gently release — it collapses.

| Cause | Mechanism |
|---|---|
| Unchecked FM-004 | FM-004 was raised but no intervention occurred |
| Sudden field collapse | ρ(Φ) dropped catastrophically in a single cycle |
| Rapid | Mechanism |
|---|---|
| Unchecked FM-004 | FM-004 was raised but no intervention occurred |
| Sudden field collapse | ρ(Φ) dropped catastrophically in a single cycle |
| Rapid perturbation | External force drove e → 1 faster than δ tracking |
| Cascade from f_Capture_Cascade | Upstream capture disruption perturbation | External force drove e → 1 faster than δ tracking |
| Cascade from f_Capture_Cascade | Upstream capture disruption propagated to this orbit |

#### §6.2.2 · Detection

```python
def detect_fm005(d_bind_current: float, d_collapse: float) -> bool:
    """
    Detect FM-005 (Decay Spiral).

    FM-005 does not require propagated to this orbit |

#### §6.2.2 · Detection

```python
def detect_fm005(d_bind_current: float, d_collapse: float) -> bool:
    """
    Detect FM-005 (Decay Spiral).

    FM-005 does not require a negative δ check — it fires purely
    on d_bind threshold. Even if δ were zero at exactly d_collapse,
    the orbit is in terminal state.

    Parameters
    ----------
    d_bind_current : float
        Binding depth at current cycle t.
    d_collapse : float
         a negative δ check — it fires purely
    on d_bind threshold. Even if δ were zero at exactly d_collapse,
    the orbit is in terminal state.

    Parameters
    ----------
    d_bind_current : float
        Binding depth at current cycle t.
    d_collapse : float
        Collapse threshold (operator-configured).

    Returns
    -------
    bool
        True if FM-005 should be raised (triggers f_Collapse).
    Collapse threshold (operator-configured).

    Returns
    -------
    bool
        True if FM-005 should be raised"""
    return d_bind_current <= d_collapse
```

#### §6.2.3 · Collapse Trigger

```python
def trigger_collapse(
    entity_id: str,
    attractor_id: str,
    d_bind_at_collapse: float,
    cycle: int
) -> dict:
    """
    Trigger f_Collapse upon FM-005.

    This function is called immediately (triggers f_Collapse).
    """
    return d_bind_current <= d_collapse
```

#### §6.2.3 · Collapse Trigger

```python
def trigger_collapse(
    entity_id: str,
    attractor_id: str,
    d_bind_at_collapse: float,
    cycle: int
) -> dict:
    """
    Trigger f_Collapse upon FM-005.

    This when FM-005 fires.
    It sets CAPTURE_COLLAPSED and passes collapse parameters
    to f_Collapse for handling.

    Parameters
    ----------
    entity_id : str
        Identifier of the collapsing mobile entity E.
    attractor_id : str
        Identifier of the attractor A.
    d_bind_at_collapse : float
        The d_bind value at the function is called immediately when FM-005 fires.
    It sets CAPTURE_COLLAPSED and passes collapse parameters
    to f_Collapse for handling.

    Parameters
    ----------
    entity_id : str
        Identifier of the collapsing mobile entity E.
    attractor_id : str
        Identifier of the attractor A.
    d_bind_at_collapse : float
        The d_bind value at the cycle FM-005 fired.
    cycle : int
        The cycle index at which collapse occurred.

    Returns
    -------
    dict
        Collapse event record passed to f_Collapse.
    """
    collapse_record = {
        "event": "FM-005",
        "entity_id": entity_id,
        "attractor_id": attractor cycle FM-005 fired.
    cycle : int
        The cycle index at which collapse occurred.

    Returns
    -------
    dict
        Collapse event record passed to f_Collapse.
    """
    collapse_record = {
        "event": "FM-005",
        "entity_id": entity_id,
        "attractor_id": attractor_id,
        "d_bind_at_collapse": d_bind_at_collapse,
        "cycle": cycle,
        "state": "CAPTURE_COLLAPSED",
        "recoverable": False,
    }
    # State flag — irreversible (INV-006)
    # CAPTURE_COLLAPSED =_id,
        "d_bind_at_collapse": d_bind_at_collapse,
        "cycle": cycle,
        "state": "CAPTURE_COLLAPSED",
        "recoverable": False,
    }
    # State flag — irreversible (INV-006)
    # CAPTURE_COLLAPSED = True — no further f_Decay cycles run
    return collapse_record
    # → hand to f_Collapse(collapse_record)
```

#### §6.2.4 · State Flag Notes

| Flag | Set When | Cleared When |
|---|---|---|
| `CAPTURE_COLLAPSED` | FM-005 fires | Never — terminal, irreversible ( True — no further f_Decay cycles run
    return collapse_record
    # → hand to f_Collapse(collapse_record)
```

#### §6.2.4 · State Flag Notes

| Flag | Set When | Cleared When |
|---|---|---|
| `CAPTURE_COLLAPSED` | FM-005 fires | Never — terminal, irreversible (INV-006) |
| `CAPTURE_DECAYING` | FM-004 fires | Superseded by CAPTURE_COLLAPSED |

---

## §7 · Engineering Primitives

<!-- metadata: section=7 session=SES-20260813-DECAY-001 -->

> Primitives areINV-006) |
| `CAPTURE_DECAYING` | FM-004 fires | Superseded by CAPTURE_COLLAPSED |

---

## §7 · Engineering Primitives

<!-- metadata: section=7 session=SES-20260813-DECAY-001 -->

> Primitives are the lowest-level callable units in f_Decay. Pure primitives have no side effects. Impure primitives modify state. Frozen primitives may not be altered without a major version bump (INV-010).

### §7.1 · PRIM:006 — flag the lowest-level callable units in f_Decay. Pure primitives have no side effects. Impure primitives modify state. Frozen primitives may not be altered without a major version bump (INV-010).

### §7.1 · PRIM:006 — flag_decay (Frozen in f_Capture; Expanded Here)

| Property | Value |
|---|---|
| Primitive ID | PRIM:006 |
| Name | flag_decay |
| Type | Impure (modifies state flags_decay (Frozen in f_Capture; Expanded Here)

| Property | Value |
|---|---|
| Primitive ID | PRIM:006 |
| Name | flag_decay |
| Type | Impure (modifies state flags, logs events) |
| Frozen In | f_Capture.md §7.2 |
| Expanded In | f_Decay.md §7.1 (cycle-based logic) |
| Evaluation | Every cycle while CAPTURE_LOCKED = true |

`flag_decay` is the main loop body of f_Decay. It calls, logs events) |
| Frozen In | f_Capture.md §7.2 |
| Expanded In | f_Decay.md §7.1 (cycle-based logic) |
| Evaluation | Every cycle while CAPTURE_LOCKED = true |

`flag_decay` is the main loop body of f_Decay. It calls `compute_decay_rate` [PRIM:010] and `assess_decay_cause` [PRIM:011], applies the DC-1 through DC-4 decision tree, sets state flags, and triggers FM-004 or FM-005 as required.

```python
def flag_decay(
    entity_id: str `compute_decay_rate` [PRIM:010] and `assess_decay_cause` [PRIM:011], applies the DC-1 through DC-4 decision tree, sets state,
    attractor_id: str,
    d_bind_history: list[float],
    d_warn: float,
    d_collapse: float,
    rho_phi: float,
    beta: float,
    eccentricity: float,
    cycle: int,
    t_decay: int flags, and triggers FM-004 or FM-005 as required.

```python
def flag_decay(
    entity_id: str,
    attractor_id: str,
    d_bind_history: list[float],
    d_warn: float,
    d_collapse: float,
    rho_phi: float,
    beta: float,
    eccentricity: float,
    cycle: int,
    t_decay: int | None
) -> dict:
    """
    [PRIM:006] flag_decay — Continuous orbital decay monitor.

    Called every cycle while CAPTURE_LOCKED = True.
    Computes decay rate δ, applies decay condition | None
) -> dict:
    """
    [PRIM:006] flag_decay — Continuous orbital decay monitor.

    Called every cycle while CAPTURE_LOCKED = True.
    Computes decay rate δ, applies decay condition decision tree,
    sets state flags, and triggers failure modes.

    Parameters
    ----------
    entity_id : str
        Mobile entity identifier.
    attractor_id : str
        Attractor identifier.
    d_bind_history : list[float]
        Full history of d_bind values; d_bind_history[-1] = d_bind(t-1).
    d_warn : float
        Warning threshold. FM-004 fires when d_bind ≤ d_warn. decision tree,
    sets state flags, and triggers failure modes.

    Parameters
    ----------
    entity_id : str
        Mobile entity identifier.
    attractor_id : str
        Attractor identifier.
    d_bind_history : list[float]
        Full history of d_bind values; d_bind_history[-1] = d_bind(t-1).
    d_warn : float
        Warning threshold. FM-004 fires when d_bind ≤ d_warn.
    d_collapse : float
        Collapse threshold. FM-005 fires when d_bind ≤ d_collapse.
    rho_phi : float
        Current coherence density ρ(Φ, t).
    beta : float
        Current resonance binding coefficient β(t).
    eccentricity : float
        Current orbital eccentricity e(t).
    cycle : int
        Current evaluation cycle index (0-indexed from CAPTURE_LOCKED).
    t_decay : int | None
        Cycle
    d_collapse : float
        Collapse threshold. FM-005 fires when d_bind ≤ d_collapse.
    rho_phi : float
        Current coherence density ρ(Φ, t).
    beta : float
        Current resonance binding coefficient β(t).
    eccentricity : float
        Current orbital eccentricity e(t).
    cycle : int
        Current evaluation index of first negative δ; None if not yet set.

    Returns
    -------
    dict
        Result record with fields:
        - d_bind_current: float
        - delta: float
        - decay cycle index (0-indexed from CAPTURE_LOCKED).
    t_decay : int | None
        Cycle index of first negative δ; None if not yet set.

    Returns
    -------
    dict
        Result record with fields:
        - d_bind_current: float
        - delta: float
        - decay_condition: str  ("DC-1" | "DC-2" | "DC-3" | "DC-4")
        - failure_mode: str | None  (None | "FM-004" | "FM-005")
        -_condition: str  ("DC-1" | "DC-2" | "DC-3" | "DC-4")
        - failure_mode: str | None  (None | "FM-004" | "FM-005")
        - t_decay: int | None
        - state_flag: str
        - collapse_record: dict | None  (populated only on FM-005)
    """
    # Compute current d_bind
    d_bind_current = beta * rho_phi * (1 - eccentricity)

    # Compute decay rate δ
    delta = compute_decay_rate(d_bind_current, d_bind_history[-1]) t_decay: int | None
        - state_flag: str
        - collapse_record: dict | None  (populated only on FM-005)
    """
    # Compute current d_bind
    d_bind_current = beta * rho_phi * (1 - eccentricity)

    # Compute decay rate δ
    delta = compute_decay_rate(d_bind_current, d_bind_history[-1])

    # Update t_decay if this is the first negative δ
    if delta < 0 and t_decay is None:
        t_decay = cycle

    # --- Decision Tree (DC-4 checked first) ---

    # DC-4: Collapse threshold

    # Update t_decay if this is the first negative δ
    if delta < 0 and t_decay is None:
        t_decay = cycle

    # --- Decision Tree (DC-4 checked first) ---

    # DC-4 (fatal, irreversible)
    if detect_fm005(d_bind_current, d_collapse):
        collapse_record = trigger_collapse(
            entity_id, attractor_id, d_bind_current, cycle
        )
        return {
            "d_bind_current": d_bind_current,
            "delta": delta,
            "decay_condition": "DC-4",
            "failure_mode": "FM-005",
            "t_decay": t_decay,
            : Collapse threshold (fatal, irreversible)
    if detect_fm005(d_bind_current, d_collapse):
        collapse_record = trigger_collapse(
            entity_id, attractor_id, d_bind_current, cycle
        )
        return {
            "d_bind_current": d_bind_current,
            "delta": delta,
            "decay_condition": "DC-4",
            "failure_mode": "FM-005",
            "t_decay": t_decay,
            "state_flag": "CAPTURE_COLLAPSED",
            "collapse_record": collapse_record,
        }

    # DC-3: Warning threshold
    if detect_fm004(d_bind_current, d_warn, delta):
        return {
            "d_bind_current": d_bind_current,
            "delta": delta,
            "decay_condition": "DC-3",
            "failure_mode": "FM-004",
            "t"state_flag": "CAPTURE_COLLAPSED",
            "collapse_record": collapse_record,
        }

    # DC-3: Warning threshold
    if detect_fm004(d_bind_current, d_warn, delta):
        return {
            "d_bind_current": d_bind_current,
            "delta": delta,
            "decay_condition": "DC-3",
            "failure_mode": "FM_decay": t_decay,
            "state_flag": "CAPTURE_DECAYING",
            "collapse_record": None,
        }

    # DC-2: Decay onset (δ < 0 but above d_warn)
    if delta < 0:
        return {
            "d_bind_current": d_bind_current,
            "delta": delta,
            "decay_condition": "DC-2",
            "failure_mode": None,
            -004",
            "t_decay": t_decay,
            "state_flag": "CAPTURE_DECAYING",
            "collapse_record": None,
        }

    # DC-2: Decay onset (δ < 0 but above d_warn)
    if delta < 0:
        return {
            "d_bind_current": d_bind_current,
            "delta": delta,
            "decay_condition": "DC-2",
            "failure_mode": None,
            "t_decay": t_decay,
            "state_flag": "CAPTURE_LOCKED",
            "collapse_record": None,
        }

    # DC-1: Stable
    return {
        "d_bind_current": d_bind_current,
        "delta": delta,
        "decay_condition": "DC-1",
        "failure_mode": None,
        "t_decay": t_decay,
        "state_flag": "ORBIT_STABLE",
        "collapse_record": None,
    }
```

---

### §7.2 · PRIM:010 — compute_decay_rate ("t_decay": t_decay,
            "state_flag": "CAPTURE_LOCKED",
            "collapse_record": None,
        }

    # DC-1: Stable
    return {
        "d_bind_current": d_bind_current,
        "delta": delta,
        "decay_condition": "DC-1",
        "failure_mode": None,
        "t_decay": t_decay,
        "state_flag": "ORBIT_STABLE",
        "collapse_record": None,
    }
```

---

### §7.2 · PRIM:010 — compute_decay_rate (New, Pure)

| Property | Value |
|---|---|
| Primitive ID | PRIM:010 |
| Name | compute_decay_rate |
| Type | Pure (no side effects) |
| Frozen In | f_Decay.md §7.2 |
| Formula | `δ(t) = d_bind(t) − d_bind(t−1)` |

```python
def compute_decay_rate(
    d_bind_current: float,
    d_bind_previous: float
) -> float:
    """
    [PRIM:010] compute_decay_rate — Pure decay rate calculator.

    New, Pure)

| Property | Value |
|---|---|
| Primitive ID | PRIM:010 |
| Name | compute_decay_rate |
| Type | Pure (no side effects) |
| Frozen In | f_Decay.md §7.2 |
| Formula | `δ(t) = d_bind(t) − d_bind(t−1)` |

```python
def compute_decay_rate(
    d_bind_current: float,
    d_bind_previous: float
) -> float:Computes the discrete first derivative of binding depth
    with respect to evaluation cycle index.

    Parameters
    ----------
    d_bind_current : float
        Binding depth at current cycle t.
    d_bind_previous : float
        Binding depth at previous cycle t-1.

    Returns
    -------
    float
        δ(t) = d_bind(t) - d_bind(t-1).
        Negative values indicate energy loss (decay).
        Zero indicates stability.
        Positive indicates energy gain (recovery or amplification).

    Notes
    -----
    This primitive has no side effects. It is safe to call at any
    point without modifying module state.
    """
    return d_bind_current - d_bind_previous
```

---

### §7.3 · PRIM:011 — assess_decay_cause (New, Diagnostic)

| Property | Value |
|---|---|
| Primitive ID | PRIM:
    """
    [PRIM:010] compute_decay_rate — Pure decay rate calculator.

    Computes the discrete first derivative of binding depth
    with respect to evaluation cycle index.

    Parameters
    ----------
    d_bind_current : float
        Binding depth at current cycle t.
    d_bind_previous : float
        Binding depth at previous cycle t-1.

    Returns
    -------
    float
        δ(t) = d_bind(t) - d_bind(t-1).
        Negative values indicate energy loss (decay).
        Zero indicates stability.
        Positive indicates energy gain (recovery or amplification).

    Notes
    -----
    This primitive has no side effects. It is safe to call at any
    point without modifying module state.
    """
    return d_bind_current - d_bind_previous
```

---

### §7.3 · PRIM:011 — assess_decay_cause (New, Diagnostic)

| Property | Value |
|---|---|
| Primitive ID | PRIM:011 |
| Name | assess_decay_cause |
| Type | Diagnostic (no side effects; read-only analysis) |
| Frozen In | f_Decay.md §7.3 |
| Returns | Cause classification string |

```python
def assess_decay_cause(
    rho_phi_initial: float,
    rho_phi_current: float,
    beta_initial: float,
    beta_current: float,
    eccentricity_initial: float,
    eccentricity_current: float,
    rho_threshold: float = 0.05,
    beta_threshold: float = 0.05,
    ecc_threshold: float = 011 |
| Name | assess_decay_cause |
| Type | Diagnostic (no side effects; read-only analysis) |
| Frozen In | f_Decay.md §7.3 |
| Returns | Cause classification string |

```python
def assess_decay_cause(
    rho_phi_initial: float,
    rho_phi_current: float,
    beta_initial: float,
    beta_current: float,
    eccentricity_initial: float,
    eccentricity_current: float,
    rho_threshold: float = 0.05,
    beta_threshold: float = 0.05,
    ecc_threshold: float = 0.05
) -> dict:
    """
    [PRIM:011] assess_decay_cause — Diagnostic decay cause classifier.

    Compares current field, resonance, and eccentricity values
    against their initial values to determine0.05
) -> dict:
    """
    [PRIM:011] assess_decay_cause — Diagnostic decay cause classifier.

    Compares current field, resonance, and eccentricity values
    against their initial values to determine the primary cause
    of observed decay. No side effects — purely analytical.

    Parameters
    ----------
    rho_phi_initial : float
        Coherence density  the primary cause
    of observed decay. No side effects — purely analytical.

    Parameters
    ----------
    rho_phi_initial : float
        Coherence density ρ(Φ) at CAPTURE_LOCKED.
    rho_phi_current : float
        Current coherence density ρ(Φ, t).
    beta_initial : float
        Resonance binding coefficient β at CAPTURE_LOCKED.
    beta_current : float
        Current β(t).
    eccentricity_initial : float
        Orbital eccentricity e at CAPTURE_LOCKED.
    eccentricity_current : float
        Current e(t).
    rho_threshold : float
        Minimumρ(Φ) at CAPTURE_LOCKED.
    rho_phi_current : float
        Current coherence density ρ(Φ, t).
    beta_initial : float
        Resonance binding coefficient β at CAPTURE_LOCKED.
    beta_current : float
        Current β(t).
    eccentricity_initial : float
        Orbital eccentricity e at CAPTURE_LOCKED.
    eccentricity_current : float
        Current e(t).
    rho_threshold : float
        Minimum fractional drop in ρ(Φ) to classify as field cause.
    beta_threshold : float
        Minimum fractional drop in β to classify as resonance cause.
    ecc_threshold : float
        Minimum fractional increase in e to classify as perturbation cause.

    Returns
    -------
    dict
        {
          "primary_cause": str,     # "field_turbulence" | "resonance_drift" |
                                    # "external_perturbation" | "combined" | "unknown"
          "rho_delta_frac": float,  # fractional change in ρ(Φ)
          "beta_delta_frac": float, # fractional change in β
          "ecc_delta_frac": float,  # fractional change in e
          "causes": list[str]       # all contributing causes
        }
    """
    rho_delta_frac = (rho_phi_initial - rho_phi_current) / rho_phi_initial \
        if rho_phi_initial > 0 else 0.0
    beta_delta_frac = (beta_initial - beta_current) / beta_initial \
        if beta_initial > 0 else 0.0
    ecc_delta_frac = (eccentricity_current - eccentricity_initial) / (1.0 - eccentricity_initial) \
        if eccentricity_initial < 1.0 else 0.0

    causes = []
    if rho_delta_frac >= rho_threshold:
        causes.append("field_turbulence")
    if beta_delta_frac >= beta_threshold:
        causes.append("resonance_drift")
    if ecc_delta_frac >= ecc_threshold:
        causes.append("external_perturbation")

    if len(causes) == 0:
        primary fractional drop in ρ(Φ) to classify as field cause.
    beta_threshold : float
        Minimum fractional drop in β to classify as resonance cause.
    ecc_threshold : float
        Minimum fractional increase in e to classify as perturbation cause.

    Returns
    -------
    dict
        {
          "primary_cause": str,     # "field_turbulence" | "resonance_drift" |
                                    # "external_perturbation" | "combined" | "unknown"
          "rho_delta_frac": float,  # fractional change in ρ(Φ)
          "beta_delta_frac": float, # fractional change in β
          "ecc_delta_frac": float,  # fractional change in e
          "causes": list[str]       # all contributing causes
        }
    """
    rho_delta_frac = (rho_phi_initial - rho_phi_current) / rho_phi_initial \
        if rho_phi_initial > 0 else 0.0
    beta_delta_frac = (beta_initial - beta_current) / beta_initial \
        if beta_initial > 0 else 0.0
    ecc_delta_frac = (eccentricity_current - eccentricity_initial) / (1.0 - eccentricity_initial) \
        if eccentricity_initial < 1.0 else 0.0

    causes = []
    if rho_delta_frac >= rho_threshold:
        causes.append("field_turbulence")
    if beta_delta_frac >= beta_threshold:
        causes.append("resonance_drift")
    if ecc_delta_frac >= ecc_threshold:
        causes.append("external_perturbation")

    if len(causes) == 0:
        primary = "unknown"
    elif len(causes) == 1:
        primary = causes[0]
    else:
        primary = "combined"

    return {
        "primary_cause": primary,
        "rho_delta_frac": rho_delta_frac,
        "beta_delta_frac": beta_delta_frac,
        "ecc_delta_frac": ecc_delta_frac,
        "causes": causes,
    } = "unknown"
    elif len(causes) == 1:
        primary = causes[0]
    else:
        primary = "combined"

    return {
        "primary_cause": primary,
        "rho_delta_frac": rho_delta_frac,
        "beta_delta_frac": beta_delta_frac,
        "ecc_delta_frac": ecc_delta_frac,
        "causes": causes,
    }
```

---

### §7.4 · Primitive Summary Table

| ID | Name | Type | Frozen In | Formula / Purpose |
|---|---|---|---|---|
| PRIM:006 | flag_decay | Impure | f_Capture.md §7.2 | Full decay cycle: compute δ, apply
```

---

### §7.4 · Primitive Summary Table

| ID | Name | Type | Frozen In | Formula / Purpose |
|---|---|---|---|---|
| PRIM:006 | flag_decay | Impure | f_Capture.md §7.2 | Full decay cycle: compute δ, apply DC-1–DC-4, set flags, fire FMs |
| PRIM:010 | compute_decay_rate | Pure | f_Decay.md §7.2 | `δ(t) = d_bind(t) − d_bind(t−1)` |
| PRIM:011 | assess_decay_cause | Diagnostic | f DC-1–DC-4, set flags, fire FMs |
| PRIM:010 | compute_decay_rate | Pure | f_Decay.md §7.2 | `δ(t) = d_bind(t) − d_bind(t−1)` |
| PRIM:011 | assess_decay_cause | Diagnostic | f_Decay.md §7.3 | Classify decay cause: field / resonance / perturbation / combined |

---

## §8 · Canonical Examples

<!-- metadata: section=8 session=SES-20260813-DECAY-001 -->

### EX-D-001 · Slow Decay → FM-004 → Intervention_Decay.md §7.3 | Classify decay cause: field / resonance / perturbation / combined |

---

## §8 · Canonical Examples

<!-- metadata: section=8 session=SES-20260813-DECAY-001 -->

### EX-D-001 · Slow Decay → FM-004 → Intervention → Orbit Restored

**Scenario:** A satellite in low orbit around a coherence-dense attractor experiences gradual field weak → Orbit Restored

**Scenario:** A satellite in low orbit around a coherence-dense attractor experiences gradual field weakening. The operator detects FM-004 and responds with f_Emit to restore ρ(Φ).

**Initial Parameters:**

| Parameter | Value |
|ening. The operator detects FM-004 and responds with f_Emit to restore ρ(Φ).

**Initial Parameters:**

| Parameter | Value |
|---|---|
| β₀ | 0.72 |
| ρ(Φ, 0) | 1.20 |
| e₀ | 0.08 |
| d_bind(0) | 0.72 × 1.20 × (1 − 0.08---|---|
| β₀ | 0.72 |
| ρ(Φ, 0) | 1.20 |
| e₀ | 0.08 |
| d_bind(0) | 0.72 × 1.20 × (1 − 0.08) = **0.7949** |
| d_warn) = **0.7949** |
| d_warn | 0.40 × 0.7949 = **0.3180** |
| d_collapse | 0.10 × 0.7949 = **0.0795** |

**Cycle | 0.40 × 0.7949 = **0.3180** |
| d_collapse | 0.10 × 0.7949-by-Cycle Evolution:**

| Cycle | ρ(Φ) | β | e | d_bind | δ | Condition | Flag |
|---|---|---|---|---|---|---|---|
| 0 | 1.2000 | 0.72 | 0.080 | 0.7949 | — | — | ORBIT_STABLE |
| 5 | 1.1500 | 0.72 | 0.082 | 0.7577 | −0.0074 | DC-2 | CAPTURE_LOCKED |
| 15 | 1.0200 | 0.71 | 0.088 | 0.6600 | −0.0098 | DC-2 | CAPTURE_LOCKED |
| 28 | 0.8800 | 0.70 | 0.095 | 0.5571 | −0.0102 | DC-2 | CAPTURE_LOCKED |
| 41 | 0.7200 | 0.68 | 0.105 | 0.4378 | −0.0119 | DC-2 | CAPTURE_LOCKED |
| 52 | 0.6100 | 0.67 | 0.110 | 0.3643 | −0.0123 | DC-2 | CAPTURE_LOCKED |
| 58 | 0.5400 | 0.66 | 0.115 | **0.3151** | −0.0130 | **DC-3 → FM-004** | **CAPTURE_DECAYING** |

**Intervention = **0.0795** |

**Cycle-by-Cycle Evolution:**

| Cycle | ρ(Φ) | β | e | d_bind | δ | Condition | Flag |
|---|---|---|---|---|---|---|---|
| 0 | 1.2000 | 0.72 | 0.080 | 0.7949 | — | — | ORBIT_STABLE |
| 5 | 1.1500 | 0.72 | 0.082 | 0.7577 | −0.0074 | DC-2 | CAPTURE_LOCKED |
| 15 | 1.0200 | 0.71 | 0.088 | 0.6600 | −0.0098 | DC-2 | CAPTURE_LOCKED |
| 28 | 0.8800 | 0.70 | 0.095 | 0.5571 | −0.0102 | DC-2 | CAPTURE_LOCKED | at cycle 60:** f_Emit injected; ρ(Φ) raised from 0.5400 → 0.7800.

| Cycle | ρ(Φ) | β | e | d_bind | δ | Condition | Flag |
|---|---|---|---|---|---|---|---|
| 60 | 0.7800 | 0.67 | 0.112 | 0.4621 | +0.1470 | DC-1 | ORBIT_STABLE |
| 70 | 0.8200 | 0.68 | 0.108 | 0.4971 | +0.0035 | DC-1 | ORBIT_STABLE |
| 80 | 0.8500 | 0.69 | 0.105 | 0.5249
| 41 | 0.7200 | 0.68 | 0.105 | 0.4378 | −0.0119 | DC-2 | CAPTURE_LOCKED |
| 52 | 0.6100 | 0.67 | 0.110 | 0.3643 | −0.0123 | DC-2 | CAPTURE_LOCKED |
| 58 | 0.5400 | 0.66 | 0.115 | **0.3151** | −0.0130 | **DC-3 → FM-004** | **CAPTURE_DECAYING** |

**Intervention at cycle 60:** f_Emit injected; ρ(Φ) raised from 0.5400 → 0.7800.

| Cycle | ρ(Φ) | β | e | d_bind | δ | Condition | Flag |
|---|---|---|---|---|---|---|---|
| 60 | 0.7800 | 0.67 | 0.112 | 0.4621 | +0.1470 | DC-1 | ORBIT_STABLE |
| 70 | 0.8200 | 0.68 | 0.108 | 0.4971 | +0.0035 | DC-1 | ORBIT_STABLE |
| 80 | 0.8500 | 0.69 | 0.105 | 0.5249 | +0.0028 | DC-1 | ORBIT_STABLE |

**Result:** FM-004 raised at cycle 58. f_Emit intervention at cycle 60 restored d_bind above d_warn. CAPTURE_DECAYING cleared. Orbit stabilized.

---

### EX-D-002 · Fast Decay → FM-004  | +0.0028 | DC-1 | ORBIT_STABLE |

**Result:** FM-004 raised at cycle 58. f_Emit intervention at cycle 60 restored d_bind above d_warn. CAPTURE_DECAYING cleared. Orbit stabilized.

---

### EX-D-002 · Fast Decay → FM-004 → FM-005 → f_Collapse

**Scenario:** An entity approaches a turbulent attractor. Field coherence drops rapidly. No intervention is made. Decay spir→ FM-005 → f_Collapse

**Scenario:** An entity approaches a turbulent attractor. Field coherence drops rapidly. No intervention is made. Decay spirals to collapse.

**Initial Parameters:**

| Parameter | Value |
|---|---|
| β₀ | 0.65 |
| ρ(Φ, 0) | 0.95 |
| e₀ | 0.12 |
| d_bind(0) | 0.65 × 0.95 × (1 − als to collapse.

**Initial Parameters:**

| Parameter | Value |
|---|---|
| β₀ | 0.65 |
| ρ(Φ, 0) | 0.95 |
| e₀ | 0.12 |
| d_bind(0) | 0.65 × 0.95 × (1 − 0.12) = **0.5434** |
| d_warn | 0.40 × 0.5434 = **0.2174** |
| d_collapse | 0.10 × 0.5434 = **0.0543** |

**Cycle-by-Cycle Evolution:**

| Cycle | ρ(Φ) | β | e | d_bind | δ | Condition | Flag |
|---|---|---|---|---|---|---|---|
| 0 | 0.9500 | 0.65 | 0.120 | 0.54340.12) = **0.5434** |
| d_warn | 0.40 × 0.5434 = **0.2174** |
| d_collapse | 0.10 × 0.5434 = **0.0543** |

**Cycle-by-Cycle Evolution:**

| Cycle | ρ(Φ) | β | e | d_bind | δ | Condition | Flag |
|---|---|---|---|---|---|---|---|
| 0 | 0.9500 | 0.65 | 0.120 | 0.5434 | — | — | ORBIT_STABLE |
| 3 | 0.8800 | 0.64 | 0.130 | 0.4895 | −0.0180 | DC-2 | CAPTURE_LOCKED |
| 8 | 0.7200 | 0.62 | 0.145 | 0.3817 | −0.0216 | DC-2 | CAPTURE_LOCKED |
| 12 | 0.5500 | 0.60 | — | — | ORBIT_STABLE |
| 3 | 0.8800 | 0.64 | 0.130 | 0.4895 | −0.0180 | DC-2 | CAPTURE_LOCKED |
| 8 | 0.7200 | 0.62  | 0.160 | **0.2772** | −0.0261 | DC-2 | CAPTURE_LOCKED |
| 15 | 0.4200 | 0.58 | 0.175 | **0.2012** | −0.0253 | **| 0.145 | 0.3817 | −0.0216 | DC-2 | CAPTURE_LOCKED |
| 12 | 0.5500 | 0.60 | 0.160 | **0.2772** | −0.0261 | DC-2 | CAPTURE_LOCKED |
| 15 | 0.4200 | 0.58 | 0.175 | **0.2012** | −0.0253 | **DC-3 → FM-004** | **CAPTURE_DECAYING** |
| 18 | 0.3000 | 0.55 | 0.200 | **0.1320** | −0.0231 | DC-3 | CAPTURE_DECAYING |
| 21 | 0.1800 | 0.52 | 0.230 | **0.0720** | −0.0200 | DC-3 | CAPTURE_DECAYING |DC-3 → FM-004** | **CAPTURE_DECAYING** |
| 18 | 0.3000 | 0.55 | 0.200 | **0.1320** | −0.0231 | DC-3 | CAPTURE_DECAYING |
| 21 | 0.1
| 23 | 0.1000 | 0.50 | 0.260 | **0.0370** | −0.0175 | **DC-4 → FM-005** | **CAPTURE_COLLAPSED** |

**FM-005 fires at cycle 23.** `trigger_collapse()` called800 | 0.52 | 0.230 | **0.0720** | −0.0200 | DC-3 | CAPTURE_DECAYING |
| 23 | 0.1000 | 0.50 | 0.260 | **0.0370** | −0.0175 | **DC-4 → FM-005** | **CAPTURE_COLLAPSED** |

**FM-005 fires at cycle 23.** `trigger_collapse()` called immediately. f_Collapse receives the collapse record. CAPTURE_COLLAPSED set — irreversible.

**Collapse Record:**
```json
{
  "event": "FM-005",
  "entity_id": "E immediately. f_Collapse receives the collapse record. CAPTURE_COLLAPSED set — irreversible.

**Collapse Record:**
```json
{
  "event": "FM-005",
  "entity_id": "E-TURB-02",
  "attractor_id": "A-TURB-01",
  "d_bind_at_collapse": 0.0370,
  "cycle": 23,
  "state": "CAPTURE_COLLAPSED",
  "recoverable": false
}
```

**Result:** FM-004 raised at cycle 15. No intervention. FM-005 fired at cycle 23. f_Collapse triggered. Orbit destroyed.

---

### EX-D-003 · External Perturbation → Sudden-TURB-02",
  "attractor_id": "A-TURB-01",
  "d_bind_at_collapse": 0.0370,
  "cycle": 23,
  "state": "CAPTURE_COLLAPSED",
  "recoverable": false
}
```

**Result:** FM-004 raised at cycle 15. No intervention. FM-005 fired at cycle 23. f_Collapse triggered. Orbit destroyed.

---

### EX-D-003 · External Perturbation → Sudden δ Spike → Recovery

**Scenario:** A stable orbit is disrupted by a sudden external perturbation (third-body gravitational influence) at cycle 30, which δ Spike → Recovery

**Scenario:** A stable orbit is disrupted by a sudden external perturbation (third-body gravitational influence) at cycle 30, which causes a large negative δ spike in a single cycle. The orbit is above d_warn and recovers naturally over subsequent cycles.

**Initial Parameters:**

| Parameter | Value |
|---|---|
| β₀ | 0.80 |
| ρ(Φ, 0) | 1.40 |
| e₀ | 0.05 |
| d_bind(0) | 0. causes a large negative δ spike in a single cycle. The orbit is above d_warn and recovers naturally over subsequent cycles.

**Initial Parameters:**

| Parameter | Value |
|---|---|
| β₀ | 0.80 |
| ρ(Φ, 0) | 1.40 |
| e₀ | 0.05 |
| d_bind(0) | 0.80 × 1.40 × 0.95 = **1.0640** |
| d_warn | 0.40 × 1.0640 = **0.4256** |
| d_collapse | 0.10 × 1.0640 = **0.1064** |

**Evolution:**

| Cycle | ρ(Φ) | β | e | d_bind | δ | Condition | Flag |
|---|---|80 × 1.40 × 0.95 = **1.0640** |
| d_warn | 0.40 × 1.0640 = **0.4256** |
| d_collapse | 0.10 × 1.0640 = **0.1064** |

**Evolution:**

| Cycle | ρ(Φ) | β | e | d_bind | δ | Condition | Flag |
|---|---|---|---|---|---|---|---|
| 0–29 | 1.4000 | 0.80 | 0.050 | 1.0640 | 0.0000 | DC-1 | ORBIT_STABLE |
| 30 (perturbation) | 1.3500 | 0.78 | 0.120 | **0.9245** | **---|---|---|---|---|---|
| 0–29 | 1.4000 | 0.80 | 0.050 | 1.0640 | 0.0000 | DC-1 | ORBIT_STABLE |
| 30 (perturbation) | 1.3500 | 0.78 | 0.120 | **0.9245** | **−0.1395** | DC-2 | CAPTURE_LOCKED |
| 31 | 1.3600 | 0.79 | 0.108 | **0.9596** | +0.0351 | DC-1 | ORBIT_STABLE |
| 35 | 1.3900−0.1395** | DC-2 | CAPTURE_LOCKED |
| 31 | 1.3600 | 0.79 | 0.108 | **0.9596** | +0.0351 | DC-1 | ORBIT_STABLE |
| 35 | 1.3900 | 0.80 | 0.060 | **1.0466** | +0.0174 | DC-1 | ORBIT_STABLE |
| 40 | 1.4000 | 0.80 | 0.050 | **1.0640** | +0.0035 | DC-1 | ORBIT_STABLE |

**Cause Assessment (cycle 30):**
```python
assess_decay_cause(
    rho_phi_initial= | 0.80 | 0.060 | **1.0466** | +0.0174 | DC-1 | ORBIT_STABLE |
| 40 | 1.4000 | 0.80 | 0.050 | **1.0640** | +0.0035 | DC-1 | ORBIT_STABLE |

**Cause Assessment (cycle 30):**
```python
assess_decay_cause(
    rho_phi_initial=1.40, rho_phi_current=1.35,
    beta_initial=0.80, beta_current=0.78,
    eccentricity_initial=0.05, eccentricity_current=0.120
)
# Returns: primary_cause = "external_perturbation"
#          rho_delta_f1.40, rho_phi_current=1.35,
    beta_initial=0.80, beta_current=0.78,
    eccentricity_initial=0.05, eccentricity_current=0.120
)
# Returns: primary_cause = "external_perturbation"
#          rho_delta_frac = 0.036  (below threshold → not field)
#          beta_delta_frac = 0.025 (below threshold → not resonance)
#          ecc_delta_frac  = 0.074 (above threshold → pertrac = 0.036  (below threshold → not field)
#          beta_delta_frac = 0.025 (below threshold → not resonance)
#          ecc_delta_frac  = 0.074 (above threshold → perturbation)
```

**Result:** δ spike of −0.1395 at cycle 30 detected by flag_decay as DC-2 (above d_warn). No FM-004 raised. Orbit self-corrected by cycle 31. assess_decay_cause correctly classified the causeurbation)
```

**Result:** δ spike of −0.1395 at cycle 30 detected by flag_decay as DC-2 (above d_warn). No FM-004 raised. Orbit self-corrected by cycle 31. assess_decay_cause correctly classified the cause as external perturbation.

---

### EX-D-004 · Decay Reversal via f_Emit + f_Amplify (Combined Intervention)

**Scenario:** An orbit is in FM-004 ( as external perturbation.

---

### EX-D-004 · Decay Reversal via f_Emit + f_Amplify (Combined Intervention)

**Scenario:** An orbit is in FM-004 (CAPTURE_DECAYING) with both ρ(Φ) weakening and β drifting simultaneously. A combined f_Emit + f_Amplify intervention is required to restore d_bind.

**State at FM-004 detection (cycle 45):**

| Parameter | Value at t=0 | Value at t=45 |
|---|---|---|
|CAPTURE_DECAYING) with both ρ(Φ) weakening and β drifting simultaneously. A combined f_Emit + f_Amplify intervention is required to restore d_bind.

**State at FM-004 detection (cycle 45):**

| Parameter | Value at t=0 | Value at t=45 |
|---|---|---|
| β | 0.75 | 0.60 |
| ρ(Φ) | 1.10 | 0.62 |
| e | 0.09 | 0.11 |
| d_bind | 0.7492 | **0.3 β | 0.75 | 0.60 |
| ρ(Φ) | 1.10 | 0.62 |
| e | 0.09 | 0.11 |
| d_bind | 0.7492 | **0.3062** |
| d_warn | 0.2997 | (d_bind just crossed) |
| d_collapse | 0.0749 | (safe margin: 0.2313) |

**Cause Assessment:**
```python
assess_decay_cause(
    rho_phi_initial=1.10, rho_phi_current=0062** |
| d_warn | 0.2997 | (d_bind just crossed) |
| d_collapse | 0.0749 | (safe margin: 0.2313) |

**Cause Assessment:**
```python
assess_decay_cause(
    rho_phi_initial=1.10, rho_phi_current=0.62,
    beta_initial=0.75, beta_current=0.60,
    eccentricity_initial=0.09, eccentricity_current=0.11
)
# Returns: primary_cause = "combined"
#          rho_delta_frac = 0.436 → field_turbulence
#          beta_delta_frac =.62,
    beta_initial=0.75, beta_current=0.60,
    eccentricity_initial=0.09, eccentricity_current=0.11
)
# Returns: primary_cause = "combined"
#          rho_delta_frac = 0.436 → field_turbulence
#          beta_delta_frac = 0.200 → resonance_drift
#          causes = ["field_turbulence", "resonance_drift"]
```

**Intervention:**
- f_Emit: inject Δρ(Φ) = +0.40 → ρ(Φ) = 0.62 + 0.40 = **1.02**
- f_Amplify: inject Δβ = +0.10 → β = 0.60 + 0.10 = **0.70** 0.200 → resonance_drift
#          causes = ["field_turbulence", "resonance_drift"]
```

**Intervention:**
- f_Emit: inject Δρ(Φ) = +0.40 → ρ(Φ) = 0.62 + 0.40 = **1.02**
- f_Amplify: inject Δβ = +0.10 → β = 0.60 + 0.10 = **0.70**

**Post-intervention d_bind:**
```
d_bind = 0.70 × 1.02 × (1 − 0.11) = 0.70 × 1.02 × 0.89 = 0.6353
```

**Recovery

**Post-intervention d_bind:**
```
d_bind = 0.70 × 1.02 × (1 − 0.11) = 0.70 × 1.02 × 0.89 = 0.6353
```

**Recovery Trajectory:**

| Cycle | ρ(Φ) | β | e | d_bind | δ | Condition | Flag |
|---|---|---|---|---|---|---|---|
| 45 | 0.6200 | 0.60 | 0.110 | 0.3062 | −0.0108 | DC-3 FM-004 | CAPTURE_DECAYING |
| 46 (post-intervention) | 1 Trajectory:**

| Cycle | ρ(Φ) | β | e | d_bind | δ | Condition | Flag |
|---|---|---|---|---|---|---|---|
| 45 | 0.6200 | 0.60 | 0.110 | 0.3062 | −0.0108 | DC-3 FM-004 | CAPTURE_DECAYING |
| 46 (post-intervention) | 1.0200 | 0.70 | 0.110 | 0.6353 | +0.3291 | DC-1 | ORBIT_STABLE |
| 55 | 1.0500 | 0.0200 | 0.70 | 0.110 | 0.6353 | +0.3291 | DC-1 | ORBIT_STABLE |
| 55 | 1.0500 | 0.71 | 0.098 | 0.6733 | +0.0038 | DC-1 | ORBIT_STABLE |
| 65 | 1.0800 | 0.72 | 0.090 | 0.7076 | +0.0034 | DC-1 | ORBIT_STABLE |

**Result:** Combined f_Emit + f_Amplify intervention at cycle 46 restored d_bind from 0.3062 to 0.6353 — above d_warn by.71 | 0.098 | 0.6733 | +0.0038 | DC-1 | ORBIT_STABLE |
| 65 | 1.0800 | 0.72 | 0.090 | 0.7076 | +0.0034 | DC-1 | ORBIT_STABLE |

**Result:** Combined f_Emit + f_Amplify intervention at cycle 46 restored d_bind from 0.3062 to 0.6353 — above d_warn by a factor of 2.12. CAPTURE_DECAYING cleared. Orbit stabilized and trending positive. assess_decay_cause enabled targeted intervention by correctly identifying a factor of 2.12. CAPTURE_DECAYING cleared. Orbit stabilized and trending positive. assess_decay_cause enabled targeted intervention by correctly identifying both causes.

---

## §9 · Cross-Module References

<!-- metadata: section=9 session=SES-20260813-DECAY-001 -->

### §9.1 · Dependency Table

| File | Direction | Interface Used | Notes |
|---|---|---|---|
| f_Capture.md | **Depends on** | `d_bind`, both causes.

---

## §9 · Cross-Module References

<!-- metadata: section=9 session=SES-20260813-DECAY-001 -->

### §9.1 · Dependency Table

| File | Direction | Interface Used | Notes |
|---|---|---|---|
| f_Capture.md | **Depends on** | `d_bind`, `β`, `ω_res`, PRIM:006 (flag_decay) | f_Decay reads these every cycle |
| f_Field.md | **Depends on `β`, `ω_res`, PRIM:006 (flag_decay) | f_Decay reads these every cycle |
| f_Field.md | **Depends on** | `ρ(Φ)`, coherence well model, FM-002 | Field state is primary decay driver |
| f_Orbit.md | **Depends on** | `e`, `r_capture`, orbital parameters | Eccentricity growth** | `ρ(Φ)`, coherence well model, FM-002 | Field state is primary decay driver |
| f_Orbit.md | **Depends on** | `e`, `r_capture`, orbital parameters | Eccentricity growth signals perturbation decay |
| f_Release.md | **Provides to** | Decay-to-release pathway (§9.3) | Preferred signals perturbation decay |
| f_Release.md | **Provides to** | Decay-to-release pathway (§9.3) | Preferred over collapse when d_bind > 0 |
| f_Collapse.md | **Provides to** | FM-005 collapse record | f_Collapse is triggered by f_Decay on FM over collapse when d_bind > 0 |
| f_Collapse.md | **Provides to** | FM-005 collapse record | f_Collapse is triggered by f_Decay on FM-005 |
| f_Emit.md | **Recovery interface** | `emit_delta` → `ρ(Φ)` increase | FM-004 recovery pathway A |
| f_Amplify.md | **Recovery interface** | `amplify_delta` → `β` increase | FM-004 recovery pathway B |
| f_Capture_Cascade.md | **Provides-005 |
| f_Emit.md | **Recovery interface** | `emit_delta` → `ρ(Φ)` increase | FM-004 recovery pathway A |
| f_Amplify.md | **Recovery interface** | `amplify_delta` → `β` increase | FM-004 recovery pathway B |
| f_Capture_Cascade.md | **Provides to** | Perturbation signal | Large δ spikes may trigger cascade re-evaluation |

### §9.2 · Invariants Provided to Downstream Files

| Invariant | Downstream Consumer |
|---|---|
| FM to** | Perturbation signal | Large δ spikes may trigger cascade re-evaluation |

### §9.2 · Invariants Provided to-005 fires before d_bind reaches 0 | f_Collapse.md |
| CAPTURE_COLLAPSED is irreversible (INV-006) | f_Collapse. Downstream Files

| Invariant | Downstream Consumer |
|---|---|
| FM-005 fires before d_bind reaches 0 | f_Collapse.md |
| CAPTURE_COLLAPSED is irreversible (INV-006) | f_Collapse.md, OPERATORS.md |
| δ is defined as discrete, not continuous | f_Orbit.md (orbital integration) |

### §9.3 · Decay-to-Release Handmd, OPERATORS.md |
| δ is defined as discrete, not continuous | f_Orbit.md (orbital integration) |

### §9.3 · Decay-to-Release Handoff

When FM-004 is active and d_bind is falling but remains above d_collapse, an operator may invoke `f_Release` instead of waitingoff

When FM-004 is active and d_bind is falling but remains above d_collapse, an operator may invoke `f_Release` for collapse. This is the preferred engineering exit:

```
CAPTURE_DECAYING = true
d_bind ∈ (d_collapse, d_warn]
  → Operator evaluates: intervene or release?
    → Intervene: f_Emit instead of waiting for collapse. This is the preferred engineering exit:

```
CAPTURE_DECAYING = true
d_bind ∈ (d_collapse, d_warn]
  → Operator evaluates: intervene or release?
    → Intervene: f_Emit and/or f_Amplify (see §6.1.3)
    → Release: invoke f_Release while RC-1–RC-5 can still be satisfied
      → CAPTURE_RELEASED (clean exit)
     and/or f_Amplify (see §6.1.3)
    → Release: invoke f_Release while RC-1–RC-5 can still be satisfied
      → CAPTURE_RELEASED (clean exit)
    → Neither: f_Decay continues cycling
      → d_bind ≤ d_collapse → FM-005 → f_Collapse (uncontrolled)
```→ Neither: f_Decay continues cycling
      → d_bind ≤ d_collapse → FM-005 → f_Collapse (uncontrolled)
```

The release pathway is always preferred over collapse. Once FM-005 fires, the release pathway is closed (INV-006).

---

## §10 · Evaluation Order

<!-- metadata: section=10 session=SES-20260813-DECAY-001 -->

The release pathway is always preferred over collapse. Once FM-005 fires, the release pathway is closed (INV-006).

---

## §10 

The 10-step normative evaluation order (INV-008) mapped to f_Decay's cycle execution:

| Step | Action | f_Decay Role |
|---|---|---|· Evaluation Order

<!-- metadata: section=10 session=SES-20260813-DECAY-001 -->

The 10-step normative evaluation order (INV-008) mapped to f_Decay's cycle execution:

| Step | Action | f_Decay Role |
|---|---|---|
| 1 | Initialize field state: compute ρ(Φ, t) | Input to d_bind(t) computation |
| 2 | Compute approach/orbital parameters | e(t), r(t) updated
| 1 | Initialize field state: compute ρ(Φ, t) | Input to d_bind(t) computation |
| 2 | Compute approach by f_Orbit |
| 3 | Evaluate stability conditions SC-1–SC-5 | Must all hold for cycle to proceed |
| 4 | Compute binding depth: d_bind(t/orbital parameters | e(t), r(t) updated by f_Orbit |
| 3 | Evaluate stability conditions SC-1–SC-5 | Must all hold for cycle to proceed |
| 4 | Compute binding depth: d_bind(t) = β × ρ(Φ) × (1−e) | Core computation this cycle |
| 5 | Compute decay rate: δ(t) = d_bind(t) − d_bind(t−1) | PRIM:010 called |
| 6 | Assess decay cause (diagnostic) | PRIM:011 called (no side effects) |
| 7 | Apply decay condition) = β × ρ(Φ) × (1−e) | Core computation this cycle |
| 5 | Compute decay rate: δ(t) = d_bind(t) − d_bind(t−1) | PRIM:010 called |
| 6 | Assess decay cause (diagnostic decision tree DC-1 → DC-4 | PRIM:006 flag_decay main body |
| 8 | Set state flags and raise failure modes) | PRIM:011 called (no side effects) |
| 7 | Apply decay condition decision tree DC-1 → DC-4 | PRIM:006 flag_decay main body |
| 8 | Set state flags and raise failure modes if indicated | FM-004 or FM-005 fired as needed |
| 9 | Trigger downstream handlers if FM-005 | f_Collapse handed collapse record |
| 10 | Log cycle result and advance t | d if indicated | FM-004 or FM-005 fired as needed |
| 9 | Trigger downstream handlers if FM-005 | f_Collapse handed_bind_history updated; t incremented |

---

## §11 · Document Metadata

<!-- metadata: section=11 session=SES-20260813-DECAY-001 -->

### §11.1 · Invariant Compliance

| Invariant | Statement collapse record |
| 10 | Log cycle result and advance t | d_bind_history updated; t incremented |

---

## §11 · Document Metadata

<!-- metadata: section=11 session=SES-20260813-DECAY-001 -->

### §11.1 · Invariant Compliance

| Invariant | Statement | Compliance |
|---|---|---|
| INV-001 | G = F_freq · F_fluid · F_force | ✅ d | Compliance |
|---|---|---|
| INV-001 | G = F_freq · F_fluid · F_force | ✅ d_bind = β × ρ(Φ) × (1−e) respects all three layers |
| INV-002 | f_Capture signature frozen | ✅ f_Decay reads but does not modify f_Capture operators |
| INV-003 | ρ(Φ) = 0 → FM-002 | ✅ FM_bind = β × ρ(Φ) × (1−e) respects all three layers |
| INV-002 | f_Capture signature frozen | ✅ f_Decay reads but does not modify f_Capture operators |
| INV-003 | ρ(Φ) = 0 → FM-002 | ✅ FM-002 precedes f_Decay; ρ(Φ) = 0 never reaches decay loop |
| INV-004-002 precedes f_Decay; ρ(Φ) = 0 never reaches decay loop |
| INV-004 | β < 1.0 → flyby | ✅ f_Decay only runs post-CAPTURE_LOCKED (β already validated) |
| INV-005 | All SCs conjunctive | ✅ SC-1–SC-5 checked before each cycle in evaluation | β < 1.0 → flyby | ✅ f_Decay only runs post-CAPTURE_LOCKED (β already validated) |
| INV-005 | All SCs conjunctive | ✅ SC-1–SC-5 checked before each cycle in evaluation order step 3 |
| INV-006 | Terminal states irreversible | ✅ CAPTURE_COLLAPSED never cleared; FM-005 closes release pathway |
| INV-007 | f order step 3 |
| INV-006 | Terminal states irreversible | ✅ CAPTURE_COLLAPSED never cleared; FM-005 closes release pathway |
| INV-007 | f_Source.md read-only | ✅ Not accessed |
| INV-008 | Evaluation order normative | ✅ §10 maps f_Decay to all 10 steps |
| INV-009 | OPERATORS.md is symbol authority | ✅ All symbols frozen via OPERATORS.md;_Source.md read-only | ✅ Not accessed |
| INV-008 | Evaluation order normative | ✅ §10 maps f_Decay to all 10 steps |
| INV-009 | OPERATORS.md is defined locally for context only |
| INV-010 | Frozen symbols no-rename without major bump | ✅ All new operators symbol authority | ✅ All symbols frozen via OPERATORS.md; defined locally for context only |
| INV-010 | Frozen symbols no-rename without major bump | ✅ All new operators (δ, d_warn, d_collapse, t_decay) frozen here at v1.0.0 |

### §11.2 · Wave Status

| Wave | Files | Status |
|---|---|---|
| 0 — Pre-existing | f_Capture.md, f_Source (δ, d_warn, d_collapse, t_decay) frozen here at v1.0.0 |

### §11.2 · Wave Status

| Wave | Files | Status |
|---|---|.md, GravityOfDismissal.md | ✅ |
| 1 — Admin | README, INDEX, OPERATORS, GLOSSARY, CHANGELOG, module.json | ✅ |
| 2 — Layer---|
| 0 — Pre-existing | f_Capture.md, f_Source.md, GravityOfDismissal.md | ✅ |
| 1 — Admin | README, INDEX, OPERATORS, GLOSSARY, CHANGELOG, module.json | ✅ |
| 2 — Layer Definitions | f_Field.md, f_Force.md, f_Frame.md | ✅ |
| 3 — Core Functions | f_Release.md ✅ · **f_Decay.md ✅** · f_Orbit Definitions | f_Field.md, f_Force.md, f_Frame.md | ✅ |
| 3 — Core Functions | f_Release.md ✅ · **f_Decay.md ✅** · f_Orbit · f_Collapse · f_Emit · f_Dampen · f_Amplify · f_Deflect | 2/8 |
| 4 — Capture Variants | 6 files | 0/6 |

### §11.3 · Operators Frozen · f_Collapse · f_Emit · f_Dampen · f_Amplify · f_Deflect | 2/8 |
| 4 — Capture Variants | 6 files | 0/6 |

### §11.3 · Operators Frozen This File

| Symbol | Name | Formula | Frozen In |
|---|---|---|---|
| δ | Decay Rate | `d_bind(t) − d_bind(t−1)` | f_Decay.md §4.1 |
| d_warn | Decay Warning Threshold | `α_ This File

| Symbol | Name | Formula | Frozen In |
|---|---|---|---|
| δ | Decay Rate | `d_bind(t) − d_bind(t−1)` | f_Decay.md §4.1 |
| d_warn | Decay Warning Threshold | `α_warn × d_bind(0)` | f_Decay.md §4.1 |
| d_collapse | Collapse Threshold | `α_collapse × d_bind(0)` | f_Decay.md §4.1 |
| t_decay | Decay Onset Time | `min{t : δ(t) < 0}` | f_Decay.md §4.1 |

### §11.4 · Primitives Frozen This File

|warn × d_bind(0)` | f_Decay.md §4.1 |
| d_collapse | Collapse Threshold | `α_collapse × d_bind(0)` | f_Decay.md §4.1 |
| t_decay | Decay Onset Time | `min{t : δ(t) < 0}` | f_Decay.md §4.1 |

### §11.4 · Primitives Frozen This File

| ID | Name | Type | Formula / Purpose |
|---|---|---|---|
| PRIM:006 | flag_decay | Impure | Cycle loop: compute δ, apply DC-1–DC-4, fire FMs ( ID | Name | Type | Formula / Purpose |
|---|---|---|---|
| PRIM:006 | flag_decay | Impure | Cycle loop: compute δ, apply DC-1–DC-4, fire FMs (expanded here) |
| PRIM:010 | compute_decay_rate | Pure | `δ(t) = d_bind(t) − d_bind(t−1)` |
| PRIM:011 | assess_decay_cause | Diagnostic | Classify decay cause across field / resonance / perturbation |

### §11.5 · Failure Modes Frozen This File

| Code | Name | Severity | Condition | Trigger |
|---|---|---|---|expanded here) |
| PRIM:010 | compute_decay_rate | Pure | `δ(t) = d_bind(t) − d_bind(t−1)` |
| PRIM:011 | assess_decay_cause | Diagnostic | Classify decay cause across field / resonance / perturbation |

### §11.5 · Failure Modes Frozen This File

| Code | Name | Severity | Condition | Trigger |
|---|---|---|---|---|
| FM-004 | Resonance Drift | WARN | `d_bind ≤ d_warn ∧ δ < 0` | Set CAPTURE_DECAYING; alert operator |
| FM-005 | Decay---|
| FM-004 | Resonance Drift | WARN | `d_bind ≤ d_warn ∧ δ < 0` | Set CAPTURE_DECAYING; alert operator |
| FM-005 | Decay Spiral | FATAL | `d_bind ≤ d_collapse` | Trigger f_Collapse; set CAPTURE_COLLAPSED (irreversible) |

### §11.6 · Changelog Entry

```
## v1.0.0 — 2026-08-13 — SES-20260813-DECAY-001

### Added Spiral | FATAL | `d_bind ≤ d_collapse` | Trigger f_Collapse; set CAPTURE_COLLAPSED (irreversible) |

### §11.6 · Changelog Entry

```
## v1.0.0 — 2026-08-13 — SES-20260813-DECAY-001

### Added
