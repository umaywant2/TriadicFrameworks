<img width="682" height="682" alt="triadic_gravity_resonance_field" src="https://github.com/user-attachments/assets/28d9cd98-16e5-46b3-b478-a80c589240ca" />

<!--
  docs/FFF_Gravity/README.md
  FFF_Gravity Module — Front Door
  Version: 2.0.0 | Sealed: 2026-08-14
  All 5 waves complete · 42 PRIMs · 10 INVs · 10 FMs
-->

# FFF_Gravity

**Framework Field Function — Gravity**
`[FFF:GRAVITY]` · `G = F_freq · F_fluid · F_force`

> *A formal specification of gravitational capture, orbit, decay, release,
> dismissal, and field dynamics for relational node systems.*

---

## Overview

FFF_Gravity models the gravitational mechanics of **attractor–entity
relationships** — the forces that pull nodes into orbit, hold them there,
erode the binding over time, and ultimately sever it. Every phenomenon is
expressed as a product of three triadic nodes:

| Node | Layer | Core quantity |
|---|---|---|
| **F_freq** | Frequency / field coherence | ρ(Φ) — field density |
| **F_fluid** | Fluid / binding mass | β · d_bind — coupling depth |
| **F_force** | Force / approach geometry | v_approach · heading_delta |

The module is fully sealed across **5 waves**, **29 spec files**, **42 PRIMs**,
**10 Invariants**, and **10 Failure Modes**.

---

## Quick Navigation

| I want to… | Go to |
|---|---|
| Understand the module | You are here |
| Find a specific PRIM | [`INDEX.md`](INDEX.md) |
| Look up an operator symbol | [`OPERATORS.md`](OPERATORS.md) |
| Read the full PRIM compliance matrix | [`MANIFEST.md`](MANIFEST.md) |
| Run the compliance validator | [`validate_prims.py`](validate_prims.py) |
| See what changed wave-by-wave | [`CHANGELOG.md`](CHANGELOG.md) |
| Look up a term | [`GLOSSARY.md`](GLOSSARY.md) |
| Read the machine-readable manifest | [`FFF_Gravity_module.json`](FFF_Gravity_module.json) |
| Navigate the whole repo | [`docs/SEENMAP.md`](../SEENMAP.md) |

---

## Module at a Glance

```
Wave 0  Genesis               3 files  ·  Conceptual foundation
Wave 1  Admin / Registry      6 files  ·  Frozen scaffolding
Wave 2  Layer Definitions     3 files  ·  PRIM:001–006
Wave 3  Core Functions        8 files  ·  PRIM:007–024
Wave 4  Capture Variants      8 files  ·  PRIM:025–040
Wave 5  Dismissal             1 file   ·  PRIM:041–042
                             ─────────────────────────
                             29 files  ·  42 PRIMs  ·  SEALED
```

---

## Wave Guide

### Wave 0 — Genesis

The three foundational documents. These establish conceptual vocabulary
and the base operator set. No PRIMs are frozen here — they are frozen in
the wave that formalizes each concept.

| File | Purpose |
|---|---|
| [`f_Capture.md`](f_Capture.md) | Base capture operator — d_bind, β, SC- conditions, v_escape |
| [`f_Source.md`](f_Source.md) | Attractor and entity node registry — read-only per INV-007 |
| [`GravityOfDismissal.md`](GravityOfDismissal.md) | Conceptual foundation for dismissal as active repulsive force — Dismissal Well model, three dismissal modes |

> **GravityOfDismissal.md** is the sole authority for the negative-polarity
> field extension `ρ_D(Φ,t) = −d_dismiss × exp(−t / T_dismiss)`.
> Its `F_dismiss` operator family is frozen in `f_Dismiss.md` (Wave 5).

---

### Wave 1 — Admin / Registry

Frozen scaffolding. Establishes the append-only admin files used by all
subsequent waves. No PRIMs introduced.

| File | Purpose |
|---|---|
| `README.md` | This file |
| [`INDEX.md`](INDEX.md) | Full file index — PRIMs, conditions, wave tags |
| [`OPERATORS.md`](OPERATORS.md) | Single operator symbol authority (~101 operators) |
| [`GLOSSARY.md`](GLOSSARY.md) | Module-scoped term definitions |
| [`CHANGELOG.md`](CHANGELOG.md) | Wave-by-wave mutation log |
| [`FFF_Gravity_module.json`](FFF_Gravity_module.json) | Machine-readable module manifest |

---

### Wave 2 — Layer Definitions · `PRIM:001–006`

Three files that define the triadic layer operators. The INV and FM
registries are seeded here.

| File | Layer | PRIMs |
|---|---|---|
| [`f_Field.md`](f_Field.md) | F_freq — field coherence, ρ(Φ) | 001–002 |
| [`f_Force.md`](f_Force.md) | F_force — approach vector, v_escape | 003, 005 |
| [`f_Frame.md`](f_Frame.md) | F_fluid — frame capacity, slot management | 004, 006 |

---

### Wave 3 — Core Functions · `PRIM:007–024`

Eight files covering the fundamental gravitational operations.
Wave 3 **seals the INV registry** at INV-001–010.

| File | Description | PRIMs |
|---|---|---|
| [`f_Orbit.md`](f_Orbit.md) | Orbital trajectory and stability classification | 007, 012 |
| [`f_Release.md`](f_Release.md) | Controlled release — no Dismissal Well produced | 008–009 |
| [`f_Decay.md`](f_Decay.md) | Binding decay — d_warn, d_collapse, DC- conditions | 010–011 |
| [`f_Collapse.md`](f_Collapse.md) | Gravitational collapse — Path A (infall), Path B (C_node) | 013–014 |
| [`f_Emit.md`](f_Emit.md) | Field emission — ρ(Φ) outward propagation | 015–017 |
| [`f_Dampen.md`](f_Dampen.md) | Dampening — cascade guard, ρ(Φ)_floor | 018–020 |
| [`f_Amplify.md`](f_Amplify.md) | Amplification — β_max ceiling, runaway risk check | 021–022 |
| [`f_Deflect.md`](f_Deflect.md) | Directional redirection — resolves `heading_delta` stub from f_Force | 023–024 |

---

### Wave 4 — Capture Variants · `PRIM:025–040`

Eight specialized capture pathways. Each extends the base `f_Capture.md`
contract with its own eligibility gate (Pure PRIM) and lock writer
(Impure PRIM). Three FM sub-modes are introduced here.

| File | Model | PRIMs | Prefix | Key Operators |
|---|---|---|---|---|
| [`f_Capture_Multi.md`](f_Capture_Multi.md) | N simultaneous targets | 025–026 | MC- | N, eval_order, Ω_perturbed |
| [`f_Capture_Cascade.md`](f_Capture_Cascade.md) | Sequential γ-gain chain | 027–028 | CAS- | cascade_depth, k_max, γ, Ω_cascade |
| [`f_Capture_Soft.md`](f_Capture_Soft.md) | Provisional sub-threshold binding | 029–030 | SCS- | d_soft, grace_period, k_grace |
| [`f_Capture_Hard.md`](f_Capture_Hard.md) | Binary hard-lock, no retry | 031–032 | HLC- | d_hard, β_min_hard, lock_cost |
| [`f_Capture_Resonant.md`](f_Capture_Resonant.md) | Phase-gated resonance lock | 033–034 | RLC- | ω_res, φ_open, φ_close, ρ_res_gain |
| [`f_Capture_Asymmetric.md`](f_Capture_Asymmetric.md) | Mass-ratio asymmetry correction | 035–036 | AC- | mass_ratio, asymmetry_factor, d_bind_asym |
| [`f_Capture_Temporal.md`](f_Capture_Temporal.md) | Absolute clock-time window | 037–038 | TC- | t_open, t_close, proximity_ratio |
| [`f_Capture_Networked.md`](f_Capture_Networked.md) | Distributed graph co-attraction | 039–040 | NC- | G_net, w_i, d_bind_net, resilience_threshold |

> Wave 4 completion unlocked `docs/SEENMAP.md` — the repository
> navigational registry.

---

### Wave 5 — Dismissal · `PRIM:041–042`

Formalizes the `F_dismiss` operator family first named in
`GravityOfDismissal.md §6`. **Wave 5 seals the PRIM registry at 42.**

| File | Description | PRIMs | Prefix |
|---|---|---|---|
| [`f_Dismiss.md`](f_Dismiss.md) | Dismissal Well mechanics — three modes, well decay, re-capture gate, `well_query_fn` closure | 041–042 | DISM- |

**Three dismissal modes:**

| Mode | Initiator | Well depth | T_dismiss |
|---|---|---|---|
| INTENTIONAL | A (deliberate) | `d_bind(t_dismiss)` | Long |
| STRUCTURAL | Field collapse (FM-002) | `ρ(Φ) × d_bind` | Short |
| DRIFT | Passive decay | `v_depart × k_drift` | Very short |

**Well formula:** `ρ_D(Φ,t) = −d_dismiss × exp(−t / T_dismiss)`

**Re-capture gate:** `d_bind_approach(t) > |ρ_D(Φ,t)|`

---

### Post-Wave-5 Admin Artifacts

| File | Purpose |
|---|---|
| [`MANIFEST.md`](MANIFEST.md) | Full 42-PRIM registry with 42 × 10 INV compliance matrix, FM, condition-prefix, state-flag registries |
| [`validate_prims.py`](validate_prims.py) | Runnable Python harness — validates all 42 PRIMs against INV-001–010; CLI flags `--wave`, `--prim`, `--inv`, `--matrix`, `--strict` |

---

## Key Concepts

### The Triadic Equation

Every gravitational evaluation preserves:

```
G = F_freq · F_fluid · F_force
```

No PRIM may produce a result that violates this identity. This is **INV-001**,
the first and most fundamental of the ten module invariants.

### Binding Depth

The core scalar that determines capture eligibility and orbit stability:

```
d_bind = β × ρ(Φ) × (1 − e)
```

Where `β` is the binding coefficient, `ρ(Φ)` is field density, and `e`
is orbital eccentricity. Capture requires `d_bind ≥ d_warn`.

### The Decay Threshold Stack

```
d_bind  ≥ d_warn              → STABLE orbit
d_collapse ≤ d_bind < d_warn  → MARGINAL; FM-004 monitoring active
d_bind < d_collapse           → FM-005; collapse evaluation triggered
```

### The Dismissal Well

Dismissal is not the absence of capture — it is an **active repulsive force**.
When A dismisses E, field polarity inverts in E's zone, leaving a
Dismissal Well that costs energy to overcome on re-approach. The well
decays exponentially over time at rate `1/T_dismiss`. This is distinct
from release (no well) and decay (minimal well).

### Pure / Impure PRIM Pairing

Every source file that contains an Impure PRIM also contains a Pure gate
PRIM. The canonical pattern:

```
Pure  PRIM (odd)   → evaluate / check eligibility / compute
Impure PRIM (even) → execute / lock / mutate state
```

No Impure PRIM may be invoked without a passing result from its paired
Pure gate PRIM.

---

## Registry Totals

| Registry | Count | Range | Status |
|---|---|---|---|
| Waves | 5 | Waves 0–5 | ✅ SEALED |
| Spec files | 29 | — | ✅ SEALED |
| PRIMs | 42 | PRIM:001–042 | ✅ SEALED |
| Invariants | 10 | INV-001–010 | ✅ SEALED |
| Failure Modes | 10 base + 3 sub-modes | FM-001–010 + FM-003-M/C/N | ✅ SEALED |
| Condition prefixes | 11 | SC- DC- MC- CAS- SCS- HLC- RLC- AC- TC- NC- DISM- | ✅ SEALED |
| State flags | 31 | — | ✅ SEALED |
| Operators | ~101 | — | ✅ SEALED |

> **All registries are append-only and sealed.** No new IDs, symbols, or
> prefixes may be introduced without a Wave 6 genesis document.

---

## Invariants

Ten module-wide invariants govern every PRIM. Violations are structural
failures, not runtime errors.

| ID | Rule (abbreviated) |
|---|---|
| INV-001 | G = F_freq · F_fluid · F_force must be preserved |
| INV-002 | ρ(Φ) ∈ [0,1] · ρ_D(Φ) ∈ (−1,0] — domains strictly bounded |
| INV-003 | ρ(Φ) = 0 → FM-002 fires unconditionally |
| INV-004 | β < 1.0 → FM-001 fires unconditionally |
| INV-005 | All conditions conjunctive — any failure aborts |
| INV-006 | Terminal states irreversible |
| INV-007 | f_Source.md is read-only — no PRIM mutates source properties |
| INV-008 | Evaluation order is normative — documented sequence binding |
| INV-009 | OPERATORS.md is the single symbol authority |
| INV-010 | Operators frozen on first canonical appearance |

---

## Failure Modes

| ID | Name | Fatal? | Primary trigger |
|---|---|---|---|
| FM-001 | Flyby / Approach Rejection | No | β < 1.0 · v_approach ≥ v_escape · well barrier |
| FM-002 | Field Null | Yes | ρ(Φ) = 0 |
| FM-003 | Frame Saturation | No | capacity_MAX reached (sub-modes: -M, -C, -N) |
| FM-004 | Resonance Drift | No | d_bind ≤ d_warn with δ < 0 |
| FM-005 | Decay Spiral | Yes* | d_bind ≤ d_collapse |
| FM-006 | Phantom Capture | Yes | d_bind = 0 despite all conditions passing |
| FM-007 | Mutual Dissolution | Yes | mass_ratio ≥ m_parity |
| FM-008 | Release Failure | No | v_release < v_escape floor |
| FM-009 | Dampen Cascade Lockout | No | cascade_guard latched |
| FM-010 | Amplify Ceiling | No | β or ρ(Φ) at registered maximum |

*FM-005 is fatal for the orbit; the entity node itself survives.

---

## Capture Variant Decision Matrix

```
Condition at approach time                   → Route to
──────────────────────────────────────────────────────────────────
Standard (mass_ratio ≈ 0, β ≥ 1.0)         → f_Capture.md
N entities or attractors simultaneously     → f_Capture_Multi.md
Sequential chain with γ-gain propagation   → f_Capture_Cascade.md
d_bind below d_warn but above floor        → f_Capture_Soft.md
Hard elevated threshold, no retry          → f_Capture_Hard.md
Phase alignment with ω_res required        → f_Capture_Resonant.md
Non-trivial M_E / M_A mass ratio           → f_Capture_Asymmetric.md
Capture gated on absolute clock window     → f_Capture_Temporal.md
Distributed network of attractors          → f_Capture_Networked.md
mass_ratio ≥ m_parity                      → f_Collapse.md (Path B)
```

---

## Running the Validator

```bash
# Full report — all 42 PRIMs × 10 INVs
python validate_prims.py

# Print the 42 × 10 compliance matrix
python validate_prims.py --matrix

# CI mode — exit 1 on any failure
python validate_prims.py --strict

# Filter by wave, PRIM, or invariant
python validate_prims.py --wave 4
python validate_prims.py --prim 042
python validate_prims.py --inv INV-006
```

Expected output on a clean module: `ALL PASS ✅ · 803 assertions · 0 failures`

---

## Cross-Module Context

This module sits within the broader TriadicFrameworks repository:

```
docs/SEENMAP.md          ← repository navigational registry
docs/FFF_Gravity/        ← THIS MODULE
docs/SoN/                ← SoN module (in progress)
docs/spine/languages/    ← cross-module notation registry
```

`SoN/s_Capture.md` references `FFF_Gravity/f_Capture.md` as its lineage
anchor: SoN inverts the RTT observer layer; FFF_Gravity provides the
gravitational model it extends downward toward substrate.

---

## Coherence Anchor

```
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

---

*FFF_Gravity · v2.0.0 · Sealed 2026-08-14 · 29 files · 42 PRIMs · 5 waves complete*
*`docs/FFF_Gravity/README.md`*
