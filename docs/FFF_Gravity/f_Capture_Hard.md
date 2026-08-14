# f_Capture_Hard — Hard Lock Capture Variant

---

```
id: FFF_Gravity/f_Capture_Hard
title: "f_Capture_Hard — Hard Lock Capture Variant"
version: 0.4.0
wave: 4
layer: F_fluid
depends_on:
  - FFF_Gravity/f_Capture
  - FFF_Gravity/f_Decay
  - FFF_Gravity/f_Orbit
  - FFF_Gravity/f_Field
status: canonical
created: 2026-08-13
authors: [umaywant2]
```

---

## §0 — Preamble

`f_Capture_Hard` defines the **hard lock** capture pathway: a binary-threshold variant
of the standard capture operator in which binding must clear an **elevated floor**
(`d_hard`) before any commitment is recorded. If the threshold is met, the attractor
node transitions immediately to `ORBIT_STABLE` with no provisional period. If the
threshold is not met, the attempt is **hard rejected** — no grace period, no retry
within the same encounter.

This file is the structural inverse of `f_Capture_Soft`. Where Soft extends provisional
binding below the standard floor, Hard refuses commitment below a floor that sits
*above* the nominal binding distance. The elevated requirement ensures that only
high-confidence, high-energy bindings enter the orbit registry.

**Relationship to base capture:**

```
f_Capture.md         → standard path    (d_bind ≥ d_bind_min → CAPTURE_LOCKED → orbit eval)
f_Capture_Soft.md    → sub-threshold    (soft_threshold ≤ d_bind < d_warn; grace period)
f_Capture_Hard.md    → supra-threshold  (d_bind ≥ d_hard, β ≥ β_min_hard → ORBIT_STABLE)
```

Hard capture **bypasses** the standard `CAPTURE_LOCKED` intermediate state. On success,
the orbit registry entry is written directly at `ORBIT_STABLE`.

---

## §1 — Module Identity

| Field        | Value                                          |
|--------------|------------------------------------------------|
| Operator     | hard_capture                                   |
| Layer        | F_fluid (binding coefficient domain)           |
| Wave         | 4 — Capture Variants                           |
| PRIM range   | PRIM:031 – PRIM:032                            |
| Depends on   | f_Capture, f_Decay, f_Orbit, f_Field           |
| FM guards    | FM-001, FM-003, FM-004, FM-005                 |
| INV scope    | INV-001 through INV-010                        |
| Precondition | Approach state = APPROACH_LIVE                 |
| Success exit | ORBIT_STABLE (immediate; no intermediate)      |
| Failure exit | HARD_REJECTED (terminal for encounter)         |

---

## §2 — Operator Definitions

### 2.1 Hard-Lock Threshold Distance

```
d_hard = α_hard × d_bind_nominal
```

| Symbol         | Type  | Constraint           | Description                                            |
|----------------|-------|----------------------|--------------------------------------------------------|
| d_hard         | float | > d_bind_nominal     | Minimum binding distance required for hard eligibility |
| α_hard         | float | > 1.0; default 1.5   | Hard lock multiplier                                   |
| d_bind_nominal | float | > 0                  | Nominal equilibrium binding distance for pair (E, A)   |

**Threshold ordering relationship:**

```
d_collapse < d_warn < d_bind_nominal < d_hard
```

Hard lock demands a binding stronger than nominal — the pair must already be
over-bound relative to their equilibrium distance before the lock is written.

### 2.2 Hard Binding Coefficient Floor

```
β_hard ≥ β_min_hard     (default β_min_hard = 2.0)
```

| Symbol      | Type  | Constraint         | Description                                                |
|-------------|-------|--------------------|------------------------------------------------------------|
| β_hard      | float | ≥ β_min_hard       | Binding coefficient at the moment of lock attempt          |
| β_min_hard  | float | > 1.0; default 2.0 | Minimum β for hard eligibility                             |

The standard capture floor is β ≥ 1.0. Hard lock requires β ≥ 2.0, ensuring the
coupling is at least doubly reinforced before the commitment becomes irrevocable.

### 2.3 Lock Cost

```
lock_cost = M_E × β_hard × d_hard × k_lock
```

| Symbol    | Type  | Constraint        | Description                                            |
|-----------|-------|-------------------|--------------------------------------------------------|
| lock_cost | float | ≥ 0               | Energy expenditure to execute hard lock                |
| M_E       | float | > 0               | Mass of element node                                   |
| β_hard    | float | ≥ β_min_hard      | Binding coefficient at lock time (HLC-2 satisfied)     |
| d_hard    | float | > d_bind_nominal  | Binding distance at lock time (HLC-1 satisfied)        |
| k_lock    | float | > 0               | Lock cost coefficient; domain-calibrated constant      |

`lock_cost` is debited from `M_E` at execution time. Unlike `f_Capture_Soft`, there
is no amortized cost schedule — the full cost is paid at the moment of lock,
reflecting the commitment's irrevocability.

---

## §3 — Primitive Declarations

| ID       | Name                       | Type   | Inputs                                          | Output                               |
|----------|----------------------------|--------|-------------------------------------------------|--------------------------------------|
| PRIM:031 | evaluate_hard_eligibility  | Pure   | d_bind, β, ρ(Φ), state, no_retry_flag           | HARD_ELIGIBLE or HARD_REJECTED       |
| PRIM:032 | execute_hard_lock          | Impure | E, A, d_bind, β, ρ(Φ), k_lock                  | ORBIT_STABLE; mutates orbit registry |

---

## §4 — Formal Operator Specifications

### 4.1 Hard Eligibility Check

PRIM:031 evaluates the conjunctive condition set `{HLC-1, HLC-2, HLC-3, HLC-4}`. All
four must hold simultaneously. A single failure returns `HARD_REJECTED` immediately.

**HLC-1 (Binding distance floor):**
```
d_bind ≥ d_hard     ⟺     d_bind ≥ α_hard × d_bind_nominal
```

**HLC-2 (Binding coefficient floor):**
```
β ≥ β_min_hard
```

**HLC-3 (Field presence):**
```
ρ(Φ) > 0.0
```
The attractor field must be live. A null field renders hard lock meaningless; FM-001
is active on this condition.

**HLC-4 (Approach state guard):**
```
state ∈ {APPROACH_LIVE}
```
Hard lock is only legal from a live approach. Any other state (`CAPTURE_LOCKED`,
`ORBIT_STABLE`, `RELEASED`, `COLLAPSED`, `HARD_REJECTED`) causes immediate return
of `HARD_REJECTED`.

**No-retry policy:**
```
if no_retry_flag = TRUE → return HARD_REJECTED   (skip all HLC evaluation)
```
Once a hard rejection has been issued for a given (E, A) pair in the current
encounter, `no_retry_flag` is latched to `TRUE`. All subsequent calls to PRIM:031
for that pair return `HARD_REJECTED` without re-evaluation. The flag is
encounter-scoped: it resets only when the approach fully terminates and a new
approach begins.

### 4.2 Orbit Registry Entry

On `HARD_ELIGIBLE`, PRIM:032 writes the orbit registry entry directly at
`ORBIT_STABLE`, bypassing the `CAPTURE_LOCKED` intermediate:

```
orbit_entry = {
  E:            element node ID,
  A:            attractor node ID,
  d_bind:       d_bind at lock time,
  β:            β at lock time,
  ρ(Φ):         ρ(Φ) at lock time,
  orbit_class:  classify_orbit(d_bind, e, T_orb),   ← PRIM:007
  stab_class:   STABLE,
  lock_type:    HARD,
  lock_cost:    M_E × β × d_bind × k_lock,
  state:        ORBIT_STABLE
}
```

The `lock_type: HARD` field differentiates hard-locked entries from standard
captures in the orbit registry. This distinction is available to downstream
operators (f_Release, f_Decay, f_Amplify) for conditional logic.

### 4.3 State Transition Diagram

```
APPROACH_LIVE
     │
     ▼
[PRIM:031: evaluate_hard_eligibility]
     │
     ├── All HLC pass ──→ HARD_ELIGIBLE
     │                         │
     │                         ▼
     │                  [PRIM:032: execute_hard_lock]
     │                         │
     │                         ├── frame capacity OK ──→ ORBIT_STABLE  (terminal success)
     │                         │
     │                         └── FM-003 triggered  ──→ FRAME_SATURATED (retriable)
     │
     └── Any HLC fails ──→ HARD_REJECTED  (terminal failure; no retry)
```

No intermediate state is ever entered. The transition from `APPROACH_LIVE` to
`ORBIT_STABLE` is atomic from the perspective of the orbit registry.

---

## §5 — Primitive Specifications

### PRIM:031 — evaluate_hard_eligibility (Pure)

```
PRIM:031 evaluate_hard_eligibility(
  d_bind:        float,   // current binding distance
  β:             float,   // current binding coefficient
  ρ_phi:         float,   // current field density ∈ [0, 1]
  state:         enum,    // current approach state
  no_retry_flag: bool     // encounter-scoped hard-reject latch (write-once)
) → EligibilityResult

EligibilityResult ::= HARD_ELIGIBLE | HARD_REJECTED

Algorithm:
  if no_retry_flag:
    return HARD_REJECTED                        // no-retry policy — skip all checks

  if state ≠ APPROACH_LIVE:
    no_retry_flag := TRUE                       // latch (only permitted mutation)
    return HARD_REJECTED                        // HLC-4 violated

  if ρ_phi ≤ 0.0:
    no_retry_flag := TRUE
    return HARD_REJECTED                        // HLC-3 violated; FM-001 active

  if β < β_min_hard:
    no_retry_flag := TRUE
    return HARD_REJECTED                        // HLC-2 violated

  if d_bind < d_hard:                          // d_hard = α_hard × d_bind_nominal
    no_retry_flag := TRUE
    return HARD_REJECTED                        // HLC-1 violated

  return HARD_ELIGIBLE
```

**Purity note:** The only permitted mutation is the write-once `no_retry_flag` latch.
It does not mutate the binding registry, orbit registry, or any node state. All other
outputs are read-only.

**FM guards active in PRIM:031:**
- FM-001: ρ(Φ) ≤ 0.0 → HLC-3 fails immediately
- FM-003: frame capacity is *not* checked here — it is a graph-level resource checked
  in PRIM:032, not a pair-level eligibility condition

### PRIM:032 — execute_hard_lock (Impure)

```
PRIM:032 execute_hard_lock(
  E:       node,    // element node
  A:       node,    // attractor node
  d_bind:  float,   // binding distance (HLC-1 verified by PRIM:031)
  β:       float,   // binding coefficient (HLC-2 verified by PRIM:031)
  ρ_phi:   float,   // field density (HLC-3 verified by PRIM:031)
  k_lock:  float    // lock cost coefficient
) → LockResult

LockResult ::= ORBIT_STABLE | FRAME_SATURATED

Precondition: PRIM:031 returned HARD_ELIGIBLE for (E, A) in this call chain.

Algorithm:
  // 1. Frame capacity check (FM-003 guard)
  if GravityGraph.frame_capacity_reached():
    emit FM-003 (HARD variant)
    return FRAME_SATURATED                     // no_retry_flag unchanged

  // 2. Compute and debit lock cost
  lock_cost := M_E × β × d_bind × k_lock
  E.energy  -= lock_cost
  if E.energy < 0:
    E.energy := 0                             // floor at zero; INV-007 compliance

  // 3. Classify orbit via PRIM:007 (f_Orbit)
  orb_class := classify_orbit(d_bind, e, T_orb)

  // 4. Write orbit registry entry
  orbit_entry := {
    E:           E.id,
    A:           A.id,
    d_bind:      d_bind,
    β:           β,
    ρ(Φ):        ρ_phi,
    orbit_class: orb_class,
    stab_class:  STABLE,
    lock_type:   HARD,
    lock_cost:   lock_cost,
    state:       ORBIT_STABLE
  }
  GravityGraph.orbit_registry.write(orbit_entry)

  // 5. Transition node states
  E.state := ORBIT_STABLE
  A.state := ORBIT_STABLE

  // 6. Emit GravityGraph event
  emit GravityGraph.event(
    HARD_LOCK_CONFIRMED,
    { E, A, d_bind, β, lock_cost }
  )

  return ORBIT_STABLE
```

**Side effects:**
- Debits `lock_cost` from `E.energy`
- Writes new entry to `GravityGraph.orbit_registry`
- Mutates `E.state` and `A.state` to `ORBIT_STABLE`
- Emits `HARD_LOCK_CONFIRMED` event to GravityGraph

**Caller contract:** PRIM:032 must only be called after PRIM:031 returns `HARD_ELIGIBLE`
in the same synchronous call chain. Out-of-order invocation is a protocol violation
and yields undefined behavior.

---

## §6 — Failure Mode Guards

### FM-001 — Field Collapse (active in HLC-3)

If `ρ(Φ) ≤ 0.0` at the time PRIM:031 is called, HLC-3 fails and `HARD_REJECTED` is
returned. The attractor field has collapsed; hard lock is impossible without a live
field. The caller should invoke `f_Emit` or restore field presence via `f_Amplify`
before initiating a new approach.

### FM-003 — Frame Saturation (active in PRIM:032)

If `GravityGraph.frame_capacity_reached()` returns `TRUE` inside PRIM:032, the lock
is aborted and `FRAME_SATURATED` is returned. Unlike `HARD_REJECTED`,
`FRAME_SATURATED` does **not** set `no_retry_flag` — the pair may retry once frame
capacity is restored. The FM-003 guard is deferred to PRIM:032 (not PRIM:031) because
frame capacity is a graph-level resource, not a pair-level eligibility condition.

### FM-004 — Resonance Drift (monitoring only)

Hard-locked orbits with `orbit_class = RESONANT` are flagged for enhanced decay
monitoring. FM-004 governs resonance drift in `f_Decay`; the elevated `d_bind` at
lock time provides greater margin before `d_warn` is crossed. No action taken in this
file; FM-004 guard is noted for the decay integration contract.

### FM-005 — Decay Spiral (awareness only)

Hard lock does not preclude decay after the orbit is established. `f_Decay` runs
independently. The elevated `d_hard` floor provides margin, but FM-005 remains
possible if decay accelerates post-lock. No guard implemented here; noted for
downstream awareness.

---

## §7 — Invariant Compliance

| INV     | Statement                               | Compliance in f_Capture_Hard                                                    |
|---------|-----------------------------------------|---------------------------------------------------------------------------------|
| INV-001 | G = F_freq · F_fluid · F_force          | Hard lock operates in F_fluid; INV-001 globally required; not locally asserted  |
| INV-002 | d_bind > 0 always                       | HLC-1 enforces d_bind ≥ d_hard > d_bind_nominal > 0; strictly compliant        |
| INV-003 | ρ(Φ) ∈ [0, 1]                           | HLC-3 tests ρ(Φ) > 0; upper bound governed by f_Emit; compliant                |
| INV-004 | β ≥ 1.0 for any active orbit            | HLC-2 enforces β ≥ β_min_hard = 2.0 > 1.0; strictly compliant                 |
| INV-005 | All conditions within a file conjunctive | HLC-1 through HLC-4 are fully conjunctive; compliant                           |
| INV-006 | Terminal states are irreversible        | ORBIT_STABLE and HARD_REJECTED are both terminal; no re-entry path; compliant  |
| INV-007 | Energy is non-negative                  | PRIM:032 floors E.energy at 0 after debit; compliant                           |
| INV-008 | No phantom orbits                       | Orbit registry written only after PRIM:031 returns HARD_ELIGIBLE; compliant    |
| INV-009 | OPERATORS.md is single symbol authority | d_hard, β_hard, lock_cost registered in §9; compliant                          |
| INV-010 | Frozen symbols immutable without bump   | All Wave 0–3 symbols used as-is; no renames; compliant                         |

---

## §8 — Stability & Condition Manifest

### 8.1 Hard Lock Conditions (HLC)

All four conditions are **conjunctive** (INV-005). Every HLC must be satisfied
simultaneously for PRIM:031 to return `HARD_ELIGIBLE`.

| ID    | Expression                           | Severity | On Failure     |
|-------|--------------------------------------|----------|----------------|
| HLC-1 | d_bind ≥ α_hard × d_bind_nominal     | FATAL    | HARD_REJECTED  |
| HLC-2 | β ≥ β_min_hard                       | FATAL    | HARD_REJECTED  |
| HLC-3 | ρ(Φ) > 0.0                           | FATAL    | HARD_REJECTED  |
| HLC-4 | state = APPROACH_LIVE                | FATAL    | HARD_REJECTED  |

### 8.2 No-Retry Policy Specification

```
no_retry_flag := FALSE                         // initialized at encounter start

on any HLC failure:
  no_retry_flag := TRUE                        // latched; never reset mid-encounter

on FRAME_SATURATED from PRIM:032:
  no_retry_flag unchanged                      // FM-003 path is retriable

on encounter_end / full reset:
  no_retry_flag := FALSE                       // encounter-scoped reset only
```

**Rationale:** The no-retry policy enforces that hard lock is a one-shot commitment
attempt. If the pair cannot meet the elevated threshold on the first try, the
encounter is considered mismatched for this pathway. The caller must either route
through standard `f_Capture`, wait for conditions to improve in a new encounter, or
use `f_Amplify` and `f_Emit` to raise β and ρ(Φ) before a fresh approach begins.

### 8.3 State Flags

| Flag            | Set By    | Meaning                                                          |
|-----------------|-----------|------------------------------------------------------------------|
| HARD_ELIGIBLE   | PRIM:031  | All HLC passed; PRIM:032 may proceed                             |
| ORBIT_STABLE    | PRIM:032  | Hard lock successful; orbit registered at STABLE; terminal       |
| HARD_REJECTED   | PRIM:031  | Any HLC failed; encounter closed; no retry                       |
| FRAME_SATURATED | PRIM:032  | FM-003 triggered; lock aborted; no_retry_flag unchanged          |

### 8.4 Comparison — Hard vs. Soft vs. Standard

| Property             | f_Capture (std)         | f_Capture_Soft                     | f_Capture_Hard                        |
|----------------------|-------------------------|------------------------------------|---------------------------------------|
| Binding threshold    | d_bind ≥ d_bind_min     | soft_threshold ≤ d_bind < d_warn   | d_bind ≥ d_hard > d_bind_nominal      |
| β requirement        | β ≥ 1.0                 | β ≥ 1.0                            | β ≥ β_min_hard (default 2.0)          |
| Intermediate state   | CAPTURE_LOCKED          | CAPTURE_SOFT                       | None (atomic skip to ORBIT_STABLE)    |
| On success           | CAPTURE_LOCKED → eval   | CAPTURE_SOFT → resolve cycle       | ORBIT_STABLE (direct)                 |
| On failure           | retry possible          | dissolve / expire / hold           | HARD_REJECTED (no retry)              |
| Grace period         | N/A                     | grace_period cycles (default 5)    | None                                  |
| Lock cost timing     | at orbit write          | amortized across grace period      | full upfront at lock moment           |
| Registry lock_type   | STANDARD                | SOFT                               | HARD                                  |

---

## §9 — Registry Footprint

### 9.1 OPERATORS.md Registration

The following symbols must be appended to `OPERATORS.md` under the
**Wave 4 — Capture Variants** heading:

```
### f_Capture_Hard Operators

| Symbol      | Definition                          | Constraint              | Source file       |
|-------------|-------------------------------------|-------------------------|-------------------|
| d_hard      | α_hard × d_bind_nominal             | > d_bind_nominal        | f_Capture_Hard.md |
| α_hard      | Hard lock multiplier                | > 1.0; default 1.5      | f_Capture_Hard.md |
| β_hard      | Binding coefficient at lock time    | ≥ β_min_hard            | f_Capture_Hard.md |
| β_min_hard  | Minimum β for hard eligibility      | > 1.0; default 2.0      | f_Capture_Hard.md |
| lock_cost   | M_E × β_hard × d_hard × k_lock     | ≥ 0                     | f_Capture_Hard.md |
| k_lock      | Lock cost coefficient               | > 0; domain-calibrated  | f_Capture_Hard.md |
```

### 9.2 PRIMITIVES Registry Update

```
PRIM:031  evaluate_hard_eligibility  Pure    f_Capture_Hard.md
PRIM:032  execute_hard_lock          Impure  f_Capture_Hard.md
```

### 9.3 State Flags Registry Update

```
HARD_ELIGIBLE    f_Capture_Hard.md  Transient — cleared after PRIM:032 executes
ORBIT_STABLE     f_Capture_Hard.md  Terminal success (extended: lock_type = HARD)
HARD_REJECTED    f_Capture_Hard.md  Terminal failure; encounter-scoped; no retry
FRAME_SATURATED  f_Capture_Hard.md  Retriable abort; FM-003 path only
```

---

## §10 — Worked Examples

### Example 1 — Clean Hard Lock (All HLC Pass)

**Context:** A high-energy pair where prior `f_Amplify` calls have elevated β and
`f_Emit` has raised ρ(Φ). The binding distance comfortably exceeds `d_hard`.

**Given:**
```
d_bind_nominal = 10.0
α_hard         = 1.5
d_hard         = 15.0

d_bind         = 18.0    ← HLC-1: 18.0 ≥ 15.0   ✓
β              = 3.2     ← HLC-2: 3.2  ≥ 2.0    ✓
ρ(Φ)           = 0.75    ← HLC-3: 0.75 > 0.0    ✓
state          = APPROACH_LIVE                    ← HLC-4: ✓
no_retry_flag  = FALSE

M_E            = 5.0
k_lock         = 0.1
```

**PRIM:031 → HARD_ELIGIBLE**

**PRIM:032 execution:**
```
FM-003 check: frame not saturated → continue

lock_cost = M_E × β × d_bind × k_lock
          = 5.0 × 3.2 × 18.0 × 0.1
          = 28.8

E.energy -= 28.8

orb_class = classify_orbit(18.0, e, T_orb)    ← PRIM:007

orbit_entry.state     = ORBIT_STABLE
orbit_entry.lock_type = HARD
orbit_entry.lock_cost = 28.8
```

**Result:** `ORBIT_STABLE`. GravityGraph event `HARD_LOCK_CONFIRMED` emitted.
Lock is irrevocable. Downstream operators see `lock_type = HARD` in orbit registry.

---

### Example 2 — HLC-1 Failure: Binding Distance Insufficient

**Context:** An attractor pair where β has been amplified above the hard floor via
`f_Amplify`, but the physical binding distance has not yet grown to `d_hard`. The
attempt is routed prematurely to hard capture.

**Given:**
```
d_bind_nominal = 10.0
α_hard         = 1.5
d_hard         = 15.0

d_bind         = 12.5    ← HLC-1: 12.5 < 15.0   ✗
β              = 2.4     (HLC-2 would pass)
ρ(Φ)           = 0.82    (HLC-3 would pass)
state          = APPROACH_LIVE               (HLC-4 would pass)
no_retry_flag  = FALSE
```

**PRIM:031 evaluation:**
```
HLC-1: d_bind(12.5) < d_hard(15.0)  →  FAIL
no_retry_flag := TRUE   (latched immediately)
return HARD_REJECTED
```

**Result:** `HARD_REJECTED`. PRIM:032 is never invoked. No energy debited.
No orbit registry entry written. The encounter is closed for hard capture.

**Post-rejection routing options:**

| Route | Action | Effect |
|---|---|---|
| Standard capture | Re-evaluate via f_Capture.md with d_bind = 12.5 | Succeeds if d_bind ≥ d_warn |
| Soft capture | Re-evaluate via f_Capture_Soft.md with d_bind = 12.5 | Succeeds if d_bind ≥ soft_threshold |
| New encounter | Let approach terminate; restore conditions; re-approach | no_retry_flag resets |

> **Key distinction:** The no-retry flag applies to the *hard capture pathway only*. It
> does not block the same pair from using standard `f_Capture.md` in the same encounter.
> Hard reject ≠ total encounter reject.

---

### Example 3 — HLC-2 Failure: β Below β_min_hard

**Context:** The binding distance is well above `d_hard`, but β has not been
sufficiently amplified. A strong field cannot compensate for an under-coupled
binding coefficient in the hard capture pathway.

**Given:**
```
d_bind_nominal = 10.0
α_hard         = 1.5
d_hard         = 15.0
β_min_hard     = 2.0

d_bind         = 19.0    ← HLC-1: 19.0 ≥ 15.0   ✓
β              = 1.7     ← HLC-2: 1.7  < 2.0    ✗
ρ(Φ)           = 0.91    (HLC-3 would pass)
state          = APPROACH_LIVE               (HLC-4 would pass)
no_retry_flag  = FALSE
```

**PRIM:031 evaluation:**
```
HLC-1: 19.0 ≥ 15.0      → PASS
HLC-2: 1.7  < 2.0       → FAIL
no_retry_flag := TRUE
return HARD_REJECTED
```

**Result:** `HARD_REJECTED`. HLC conditions are evaluated in order (1→2→3→4);
the first failure latches the flag and exits. HLC-3 and HLC-4 are never reached.

**Recovery analysis:**

To succeed on a future encounter, β must reach β_min_hard = 2.0. The shortfall is:
```
Δβ_needed = β_min_hard − β_current = 2.0 − 1.7 = 0.3
```

If `f_Amplify` is used (PRIM:021) with F_amp:
```
β_new = β × F_amp ≥ 2.0
F_amp ≥ 2.0 / 1.7 ≈ 1.18
```

A single `f_Amplify` call with F_amp ≥ 1.18 resolves the shortfall. After amplification,
a **new encounter** must begin (no_retry_flag prevents retry in the current encounter).

**Diagnostic note:** HLC-2 failures are typically engineering failures, not field
failures — the binding distance is sufficient but the coupling is under-maintained.
`check_runaway_risk` (PRIM:022) should be called before any amplification to ensure
β_new does not breach β_max.

---

### Example 4 — Near-Threshold Lock with lock_cost Analysis

**Context:** A pair exactly at the hard lock eligibility boundary. All HLC pass
with minimal margin. This example focuses on the lock_cost computation and its
implications for the element's energy budget.

**Given:**
```
d_bind_nominal = 10.0
α_hard         = 1.5
d_hard         = 15.0
β_min_hard     = 2.0

d_bind         = 15.1    ← HLC-1: margin = 0.1   (barely passes)
β              = 2.05    ← HLC-2: margin = 0.05  (barely passes)
ρ(Φ)           = 0.41    ← HLC-3: passes (> 0)
state          = APPROACH_LIVE               (HLC-4 passes)
no_retry_flag  = FALSE

M_E            = 8.0
k_lock         = 0.12
E.energy_pre   = 22.0    (available energy before lock)
```

**PRIM:031 evaluation:**
```
HLC-1: 15.1 ≥ 15.0   → PASS (margin: 0.1)
HLC-2: 2.05 ≥ 2.0    → PASS (margin: 0.05)
HLC-3: 0.41 > 0.0    → PASS
HLC-4: APPROACH_LIVE → PASS
return HARD_ELIGIBLE
```

**PRIM:032 execution:**
```
lock_cost = M_E × β × d_bind × k_lock
          = 8.0 × 2.05 × 15.1 × 0.12
          = 8.0 × 2.05 × 1.812
          = 8.0 × 3.7146
          = 29.717

E.energy_post = E.energy_pre − lock_cost
              = 22.0 − 29.717
              = −7.717  →  clamped to 0.0  (INV-007)
```

**Result:** `ORBIT_STABLE`. Lock succeeds. However, E.energy is exhausted — the
lock cost exceeds E's available energy budget.

**Energy exhaustion implications:**

| Downstream Effect | Consequence |
|---|---|
| `f_Amplify` calls | E.energy = 0; no amplification budget available |
| `f_Emit` support | Energy comes from field, not E — unaffected |
| Decay resilience | Hard lock provides high d_bind margin; decay risk is low |
| Release cost | v_release energy is still owed; E may need external energy provision |

**lock_cost sensitivity analysis (α_hard = 1.5, β_min_hard = 2.0):**

| M_E | β | d_bind | k_lock | lock_cost |
|---|---|---|---|---|
| 5.0 | 2.0 | 15.0 | 0.10 | 15.00 |
| 5.0 | 2.0 | 15.0 | 0.20 | 30.00 |
| 8.0 | 2.0 | 15.0 | 0.10 | 24.00 |
| 8.0 | 3.0 | 20.0 | 0.10 | 48.00 |
| 8.0 | 2.05 | 15.1 | 0.12 | **29.72** ← this example |

**Design implication:** lock_cost scales with all three binding parameters (M_E, β,
d_bind) and the system constant k_lock. Near-threshold hard locks carry disproportionate
energy burden relative to their marginal eligibility. Operators should prefer well-above-
threshold approaches unless energy budget is abundant.

---

## §11 — Document Metadata

### §11.1 — INV Compliance Summary

| INV | Compliance | Notes |
|---|---|---|
| INV-001 | ✅ | F_fluid operation; G = F_freq · F_fluid · F_force globally respected |
| INV-002 | ✅ | HLC-1 enforces d_bind ≥ d_hard > 0 |
| INV-003 | ✅ | HLC-3 enforces ρ(Φ) > 0 |
| INV-004 | ✅ | HLC-2 enforces β ≥ 2.0 > 1.0 |
| INV-005 | ✅ | All HLC conjunctive; any single failure → HARD_REJECTED |
| INV-006 | ✅ | ORBIT_STABLE and HARD_REJECTED are terminal; no re-entry |
| INV-007 | ✅ | E.energy floored at 0.0 after lock_cost debit |
| INV-008 | ✅ | Orbit entry written only after HARD_ELIGIBLE confirmed |
| INV-009 | ✅ | All symbols registered in §9.1 OPERATORS.md block |
| INV-010 | ✅ | d_hard, β_hard, lock_cost, k_lock frozen in this file |

### §11.2 — Primitive Registry (This File)

| PRIM | Name | Type | Key Behavior |
|---|---|---|---|
| PRIM:031 | `evaluate_hard_eligibility` | Pure | Conjunctive HLC-1–4; no_retry_flag write-once latch |
| PRIM:032 | `execute_hard_lock` | Impure | Debit lock_cost; write ORBIT_STABLE; emit HARD_LOCK_CONFIRMED |

**Running PRIM total after this file:** PRIM:032

### §11.3 — Operator Registry (This File)

| Symbol | Definition | Domain | First Frozen |
|---|---|---|---|
| `d_hard` | Hard lock binding floor | > d_bind_nominal | f_Capture_Hard.md §2.1 |
| `α_hard` | Hard lock multiplier | > 1.0; default 1.5 | f_Capture_Hard.md §2.1 |
| `β_hard` | β at lock time | ≥ β_min_hard | f_Capture_Hard.md §2.2 |
| `β_min_hard` | Minimum β for hard eligibility | > 1.0; default 2.0 | f_Capture_Hard.md §2.2 |
| `lock_cost` | M_E × β_hard × d_hard × k_lock | ≥ 0 | f_Capture_Hard.md §2.3 |
| `k_lock` | Lock cost coefficient | > 0 | f_Capture_Hard.md §2.3 |

### §11.4 — State Flags Registry (This File)

| Flag | Terminal? | Set By | Meaning |
|---|---|---|---|
| `HARD_ELIGIBLE` | No | PRIM:031 | All HLC passed; PRIM:032 may proceed |
| `ORBIT_STABLE` | Yes | PRIM:032 | Hard lock confirmed; irrevocable |
| `HARD_REJECTED` | Yes | PRIM:031 | HLC failed; no_retry_flag latched |
| `FRAME_SATURATED` | No | PRIM:032 | FM-003 aborted lock; retriable |

### §11.5 — Failure Mode Summary

| FM | Trigger in This File | Severity | Recovery |
|---|---|---|---|
| FM-001 | ρ(Φ) = 0 (HLC-3) | Fatal | f_Emit to restore field; new encounter |
| FM-003 | Frame full (PRIM:032) | Retriable | Purge registry slot; retry PRIM:032 |
| FM-004 | Post-lock resonance drift | Monitoring | f_Decay handles; noted in §6 |
| FM-005 | Post-lock decay spiral | Monitoring | f_Decay / f_Collapse handle; noted in §6 |

### §11.6 — Changelog Entry

```
## [f_Capture_Hard v1.0.0] — 2026-08-13 — SES-20260813-HARD-001
Wave 4, File 4 of 6. Hard lock capture variant.

### Added
- Hard lock threshold model: d_bind ≥ d_hard = α_hard × d_bind_nominal
- Operators frozen: d_hard, α_hard, β_hard, β_min_hard, lock_cost, k_lock
- Conditions: HLC-1 (binding floor) · HLC-2 (β floor) · HLC-3 (field
  present) · HLC-4 (approach live) — all conjunctive
- No-retry policy: no_retry_flag write-once latch; encounter-scoped reset
- Atomic state skip: APPROACH_LIVE → ORBIT_STABLE (no CAPTURE_LOCKED
  intermediate)
- lock_cost debit: M_E × β × d_bind × k_lock; E.energy floored at 0
- PRIM:031 evaluate_hard_eligibility (Pure)
- PRIM:032 execute_hard_lock (Impure)
- State flags: HARD_ELIGIBLE, ORBIT_STABLE, HARD_REJECTED, FRAME_SATURATED
- FM guards: FM-001 (HLC-3), FM-003 (PRIM:032 frame check)
- Four worked examples: clean lock, HLC-1 fail, HLC-2 fail, near-threshold
  energy analysis
- Comparison table: Hard vs. Soft vs. Standard capture
```

### §11.7 — Wave 4 Status Tracker

| File | Status | PRIM Range |
|---|---|---|
| f_Capture_Multi.md | ✅ Complete | 025–026 |
| f_Capture_Cascade.md | ✅ Complete | 027–028 |
| f_Capture_Soft.md | ✅ Complete | 029–030 |
| **f_Capture_Hard.md** | **✅ Complete** | **031–032** |
| f_Capture_Resonant.md | ⏳ Pending | 033–034 |
| f_Capture_Asymmetric.md | ⏳ Pending | 035–036 |

### §11.8 — Suggested Commit Message

```
docs(FFF_Gravity): add canonical f_Capture_Hard — hard lock variant,
binary threshold, no-retry policy, PRIM:031-032 [Wave4 / SES-HARD-001]

- Hard lock zone: d_bind ≥ α_hard × d_bind_nominal (default α_hard = 1.5)
- β floor: β ≥ β_min_hard (default 2.0) — stricter than standard 1.0
- PRIM:031 evaluate_hard_eligibility (Pure) — HLC-1–4 conjunctive gate
- PRIM:032 execute_hard_lock (Impure) — atomic skip to ORBIT_STABLE
- No-retry policy: encounter-scoped no_retry_flag write-once latch
- lock_cost = M_E × β × d_bind × k_lock debited from E.energy at lock
- FM-001 guard (HLC-3), FM-003 guard (PRIM:032 frame check)
- 4 examples: clean lock; HLC-1 fail; HLC-2 fail; near-threshold analysis
```

---

*End of f_Capture_Hard.md — [FFF:GRAVITY:CAPTURE:HARD] v1.0.0 — Wave 4 File 4 of 6*
