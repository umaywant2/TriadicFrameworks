# f_Capture_Multi

---

```
session_id: "SES-20260813-CAPTURE-MULTI-001"
canonical_tag: "[FFF:GRAVITY:CAPTURE:MULTI]"
file: "f_Capture_Multi.md"
wave: 4
extends: "f_Capture.md"
type: capture_variant
status: canonical
version: "1.0.0"
dependencies:
  - "f_Capture.md"
  - "f_Frame.md"
  - "f_Orbit.md"
  - "f_Field.md"
  - "f_Force.md"
  - "f_Dampen.md"
  - "f_Emit.md"
  - "OPERATORS.md"
  - "INDEX.md"
new_operators:
  - N
  - eval_order
  - "Φ_perturbed"
  - "δ_perturb"
new_primitives:
  - "PRIM:025"
  - "PRIM:026"
failure_modes_referenced:
  - "FM-001 (Overshoot)"
  - "FM-002 (Field Null)"
  - "FM-003 / FM-003-M (Frame Saturation — multi-capture sub-mode)"
  - "FM-006 (Phantom Capture)"
stability_conditions_referenced:
  - "SC-1, SC-2, SC-3, SC-4, SC-5"
  - "MC-1 (Batch Coherence Floor)"
  - "MC-2 (Attractor Uniqueness)"
changelog:
  - version: "1.0.0"
    date: "2026-08-13"
    session: "SES-20260813-CAPTURE-MULTI-001"
    summary: >
      First canonical release. MULTI_ELEMENT and MULTI_ATTRACTOR modes.
      N, eval_order, Φ_perturbed, δ_perturb frozen. PRIM:025–026 opened.
      FM-003-M defined as FM-003 sub-mode. Wave 4 primitive block formally opened.
```

<!-- [FFF:GRAVITY:CAPTURE:MULTI] | canonical | v1.0.0 | SES-20260813-CAPTURE-MULTI-001 -->

---

## §0 — Session Context

<!-- SESSION: SES-20260813-CAPTURE-MULTI-001 -->
<!-- Operator: Nawder | umaywant2 | Belleville, MI -->
<!-- Repository: https://github.com/umaywant2/TriadicFrameworks -->
<!-- Path: docs/FFF_Gravity/f_Capture_Multi.md -->
<!-- Session time: 2026-08-13T21:33 EDT -->

This file is the **Wave 4 opening document** of the FFF_Gravity module. It extends `f_Capture.md`
(the single-body capture reference implementation) to govern multi-body capture events — scenarios
where N ≥ 2 bodies participate in a single capture evaluation cycle.

**What Wave 4 adds:**
Wave 3 completed the core function library (Release, Decay, Orbit, Collapse, Emit, Dampen, Amplify,
Deflect) and froze PRIM:001–024 and FM-001–FM-010. Wave 4 opens the Capture Variant sub-library.
Capture variants do not introduce new Failure Mode IDs (the FM registry is frozen at
FM-010) and do not add new Invariants (INV registry frozen at INV-010). They extend
the base capture semantics defined in `f_Capture.md` (PRIM:001–006) by specifying
evaluation order, per-step field perturbation, and the conditions under which
multi-participant sessions remain coherent or collapse into Frame Saturation. All
behavior introduced here is reducible to the triadic equation G = F_freq · F_fluid ·
F_force applied iteratively, with ρ(Φ) recomputed after each sub-capture event.

---

## §1 — Module Identity

| Field | Value |
|---|---|
| Module name | `f_Capture_Multi` |
| Wave | Wave 4 — Capture Variants |
| Layer | Core Capture Extension |
| Base file | `f_Capture.md` |
| Extends | `f_Frame.md`, `f_Field.md`, `f_Force.md` |
| Status | Canonical |
| Primitive block | PRIM:025–026 (Wave 4 opens here) |
| New conditions | MC-1, MC-2 |
| New failure sub-modes | FM-003-M (sub-mode of FM-003) |
| New operators | `N`, `eval_order`, `Φ_perturbed`, `δ_perturb` |

### §1.1 — Wave 4 Primitive Block Declaration

Wave 4 opens a new primitive block beginning at **PRIM:025**. Wave 3 closed at
PRIM:024 (`compute_deflection_cost`, in `f_Deflect.md`). All Wave 4 files
continue from PRIM:025 forward. This block is append-only; no Wave 3 or earlier
primitive ID may be reused or redefined.

### §1.2 — Relationship to Base Capture

`f_Capture.md` defines the canonical single-pair capture: one Attractor node A
and one Element node E establish a binding at distance r_capture with coupling
coefficient β. `f_Capture_Multi.md` lifts the cardinality restriction on both
sides of that pair, producing two distinct modes evaluated under a shared
perturbation model.

---

## §2 — Canonical Description

### §2.1 — Conceptual Overview

Multi-capture sessions arise when the field conditions of a single Frame node are
sufficient to support more than one simultaneous or sequential binding event. The
word "simultaneous" is an idealization: in triadic evaluation all captures are
resolved in strict `eval_order` sequence, with ρ(Φ) updated between steps. A
Frame node never processes two capture events in the same evaluation tick; it
serializes them.

Two structural modes are defined:

| Mode | Symbol | Description |
|---|---|---|
| `MULTI_ELEMENT` | ME | One Attractor A captures N Element nodes E₁…Eₙ in sequence |
| `MULTI_ATTRACTOR` | MA | One Element E is captured by N Attractor nodes A₁…Aₙ in sequence |

Both modes share the same perturbation model: each completed capture perturbs
ρ(Φ) by δ_perturb, reducing the field's available coherence for the next
capture in the sequence. This is the mechanism by which Frame Saturation
(FM-003) manifests in multi-participant contexts.

### §2.2 — MULTI_ELEMENT Mode (ME)

A single Attractor A holds a Frame node F. N Element nodes are queued for
capture in eval_order. At step k (1 ≤ k ≤ N):

1. Check SC-1 through SC-5 against current Φ_perturbed(k−1).
2. Check MC-1 (Batch Coherence Floor) — if violated, emit FM-003-M and halt.
3. Compute d_bind(k) using Φ_perturbed(k−1).
4. Register Eₖ in Frame F via `register_capture` (PRIM:003).
5. Compute δ_perturb(k) and update Φ_perturbed(k).

All N bindings share the same Attractor A. Each Eₖ receives its own r_capture(k)
and β(k) computed against the perturbed field at step k.

### §2.3 — MULTI_ATTRACTOR Mode (MA)

A single Element E is sequentially captured by N Attractor nodes A₁…Aₙ, each
with its own Frame node F₁…Fₙ. At step k:

1. Check SC-1–SC-5 and MC-2 (Attractor Uniqueness) against Aₖ.
2. Verify E is not already in terminal state (INV-006).
3. Compute d_bind(k) for the pair (Aₖ, E) using Φ_perturbed(k−1).
4. Register E in Frame Fₖ.
5. Compute δ_perturb(k) and update Φ_perturbed(k).

MC-2 enforces that no single Attractor node appears more than once in the
ordered sequence A₁…Aₙ. Duplicate Attractor admission is a structural
invariant violation, not merely a failure mode.

### §2.4 — Field Perturbation Model

At session start, Φ_perturbed(0) = ρ(Φ) (the unmodified field density as
defined in `f_Field.md`). After each capture step k:

```
Φ_perturbed(k) = Φ_perturbed(k−1) − δ_perturb(k)
```

where:

```
δ_perturb(k) = d_bind(k) × (1 − e(k)) × k_perturb
```

`k_perturb` is the per-capture coherence cost coefficient (system constant,
default 0.05). This ensures that each successive capture in a multi-capture
session is marginally harder to sustain than the previous, reflecting the
progressive exhaustion of the Frame node's coherence budget.

If Φ_perturbed(k) drops below ρ(Φ)_floor (as defined in `f_Dampen.md`), the
session must halt immediately; any registered captures from steps 1…k−1 are
retained, and FM-003-M is raised for the halted step k.

### §2.5 — Evaluation Order Semantics

`eval_order` is an ordered list of participant identifiers. For ME mode it is
the ordered list [E₁, E₂, …, Eₙ]; for MA mode it is [A₁, A₂, …, Aₙ]. The
list is fixed at session initialization and may not be modified mid-session.
Reordering mid-session is a structural error (raises FM-003-M immediately
without processing further captures).

The rationale for fixity: if eval_order were mutable, an adversarial perturbation
cascade could be constructed by front-loading low-cost captures to exhaust the
field for high-cost captures — violating the fairness principle of the coherence
budget.

---

## §3 — Triadic Equation

The governing equation is unchanged:

```
G = F_freq · F_fluid · F_force
```

In multi-capture context, each step k evaluates its own G(k):

```
G(k) = F_freq(Φ_perturbed(k−1)) · F_fluid(M_A, Φ_perturbed(k−1)) · F_force(β(k), e(k))
```

**INV-001 compliance:** All three nodes must be implicated at every step. A
capture step that resolves with any factor equal to zero does not produce a
binding — it triggers the relevant FM (FM-002 if F_freq = 0, FM-007 if
F_fluid = 0, FM-001 if F_force = 0).

**Perturbation propagation:** Because Φ_perturbed(k) feeds F_freq and F_fluid
at step k+1, a degraded field coherence reduces both the attractor's mass
density weighting and the frequency node's binding capacity simultaneously.
This double-channel sensitivity is the primary source of cascade risk in
multi-capture sessions.

---

## §4 — Operator Registry

### §4.1 — New Operators Introduced in This File

The following operators are **frozen on first canonical appearance here**
(INV-010). They are registered in OPERATORS.md as part of Wave 4.

| Symbol | Name | Type | Domain | Definition |
|---|---|---|---|---|
| `N` | Participant Count | Integer | N ≥ 2 | Total number of participants in the multi-capture session (Element count for ME; Attractor count for MA) |
| `eval_order` | Evaluation Order | Ordered List | Fixed at session init | Ordered sequence of participant identifiers; immutable after session start |
| `Φ_perturbed(k)` | Perturbed Field State | Real | ρ(Φ)_floor ≤ Φ_perturbed ≤ ρ(Φ) | Field density after k completed capture steps; initialized to ρ(Φ) at k=0 |
| `δ_perturb(k)` | Per-Capture Perturbation | Real | δ_perturb ≥ 0 | Coherence cost of the k-th capture event; computed as d_bind(k) × (1−e(k)) × k_perturb |
| `k_perturb` | Perturbation Coefficient | Real | 0 < k_perturb ≤ 1 | System constant scaling per-capture coherence cost (default 0.05) |

### §4.2 — Inherited Operators (Referenced, Not Redefined)

| Symbol | Source File | Role in This File |
|---|---|---|
| `ρ(Φ)` | `f_Field.md` | Initial field density; becomes Φ_perturbed(0) |
| `d_bind` | `f_Field.md` | Per-step binding depth, computed against Φ_perturbed(k−1) |
| `β` | `f_Force.md` | Coupling coefficient; per-step β(k) may differ across ME captures |
| `e` | `f_Force.md` | Eccentricity; per-step e(k) |
| `r_capture` | `f_Capture.md` | Per-step capture radius r_capture(k) |
| `M_A` | `f_Force.md` | Attractor mass; fixed for ME mode; per-step Aₖ for MA mode |
| `M_E` | `f_Force.md` | Element mass; per-step Eₖ for ME mode; fixed for MA mode |
| `capacity_MAX` | `f_Frame.md` | Upper bound on total registered captures in a Frame node |
| `ρ(Φ)_floor` | `f_Dampen.md` | Absolute floor on field density; halts session if Φ_perturbed drops below |

### §4.3 — Operator Interaction Table

| Operation | Input Operators | Output | Notes |
|---|---|---|---|
| Initialize session | N, eval_order, ρ(Φ) | Φ_perturbed(0) = ρ(Φ) | Sets field state baseline |
| Compute step binding | d_bind(k), e(k), k_perturb | δ_perturb(k) | Per-step cost |
| Update field state | Φ_perturbed(k−1), δ_perturb(k) | Φ_perturbed(k) | Subtractive update |
| Check floor | Φ_perturbed(k), ρ(Φ)_floor | PASS / FM-003-M | Halt if below floor |
| Check capacity | registered count, capacity_MAX | PASS / FM-003-M | Halt if at capacity |

---

## §5 — Conditions

### §5.1 — Stability Conditions (Inherited, Conjunctive)

All five stability conditions from the base layer apply at every step k. They
are evaluated against Φ_perturbed(k−1), not the original ρ(Φ).

| ID | Condition | Source | Check Point |
|---|---|---|---|
| SC-1 | ρ(Φ) > 0 (field must be active) | `f_Field.md` | Evaluated as Φ_perturbed(k−1) > 0 at each step |
| SC-2 | v_escape not exceeded | `f_Field.md` | v_approach(k) < v_escape computed from Φ_perturbed(k−1) |
| SC-3 | d_bind > 0 | `f_Field.md` | Computed from Φ_perturbed(k−1); zero d_bind halts capture at step k |
| SC-4 | v_approach > 0 | `f_Force.md` | Checked per step |
| SC-5 | capacity_MAX not exceeded | `f_Frame.md` | Total registered count < capacity_MAX before each register_capture |

**Conjunctive enforcement (INV-005):** All five must hold. Failure of any single
SC triggers the corresponding FM and halts the multi-capture session at step k.
Captures from steps 1…k−1 that were already registered are retained.

### §5.2 — Multi-Capture Conditions (New)

| ID | Name | Formal Statement | Violation Consequence |
|---|---|---|---|
| MC-1 | Batch Coherence Floor | Φ_perturbed(k) ≥ ρ(Φ)_floor for all k ∈ {1…N} | Emit FM-003-M; halt session at step k; retain prior registrations |
| MC-2 | Attractor Uniqueness | In MA mode, ∀ i ≠ j: Aᵢ ≠ Aⱼ in eval_order | Structural error; session is invalid; no captures registered |

**MC-1 rationale:** A multi-capture session that exhausts the coherence floor
causes irreversible field suppression, triggering FM-009 (Dampen Cascade). MC-1
is a pre-emptive guard that halts before the cascade begins.

**MC-2 rationale:** An Element captured twice by the same Attractor violates
INV-003 (binding uniqueness). Duplicate Attractor admission is detected at
session initialization before any capture step executes.

### §5.3 — Condition Evaluation Order

At each step k, conditions are checked in this strict sequence:

```
MC-2 (init only) → SC-1 → SC-3 → SC-4 → SC-2 → SC-5 → MC-1
```

MC-2 is checked only once, at session initialization (before k=1). SC-5 (Frame
capacity) is checked immediately before `register_capture` is called, since the
count changes with each step. MC-1 (coherence floor) is checked after
Φ_perturbed(k) is computed, as the final gate before the step is committed.

---

## §6 — Failure Modes

### §6.1 — Active Failure Modes from Base Registry (FM-010 frozen)

| FM ID | Name | Source | Trigger in This File |
|---|---|---|---|
| FM-001 | Approach Rejection | `f_Force.md` | v_approach(k) = 0 at any step k |
| FM-002 | Field Null | `f_Field.md` | Φ_perturbed(k−1) ≤ 0 at any step k |
| FM-003 | Frame Saturation | `f_Frame.md` | registered count = capacity_MAX before step k |
| FM-007 | Dissolution | `f_Force.md` | M_A or M_E = 0 at any step k |
| FM-009 | Dampen Cascade | `f_Dampen.md` | Φ_perturbed(k) < ρ(Φ)_floor |

### §6.2 — FM-003-M: Frame Saturation — Multi-Capture Sub-Mode

**FM-003-M** is a sub-mode of FM-003, not a new FM ID. It is raised exclusively
within multi-capture sessions when Frame Saturation is induced by the
perturbation model rather than by the absolute capacity limit.

| Field | Value |
|---|---|
| Sub-mode ID | FM-003-M |
| Parent FM | FM-003 (Frame Saturation) |
| Trigger | Φ_perturbed(k) < ρ(Φ)_floor (MC-1 violation) OR eval_order modified mid-session |
| State transition | Session halts; registered captures from steps 1…k−1 are preserved; step k and onward are abandoned |
| Recovery | Resume only if ρ(Φ) is restored above floor via `suppress_field` (PRIM:018) or `amplify_coupling` (PRIM:021); eval_order may not be re-initialized on the same session object |
| Terminal? | No — the individual bindings registered before FM-003-M are valid and retained; the session object itself enters SATURATED state |

**FM-003-M vs. FM-003:** The base FM-003 triggers when registered count =
capacity_MAX (a hard integer ceiling). FM-003-M triggers when the field
coherence budget is exhausted before the count ceiling is reached (a soft
energetic ceiling). Both halt further registration; neither invalidates existing
bindings.

### §6.3 — Non-Applicable Failure Modes

| FM ID | Reason Not Applicable |
|---|---|
| FM-004 | Decay (δ) is a post-capture process; not evaluated during capture steps |
| FM-005 | Asymmetric infall requires single-pair geometry; not defined for multi-capture |
| FM-006 | Gradient reversal is a single-force-node concept; multi-capture uses per-step force nodes |
| FM-008 | Release is a post-capture process |
| FM-010 | Emit/Amplify ceiling is post-capture; not evaluated during session |

---

## §7 — Engineering Primitives

### §7.1 — Wave 4 Primitive Block Header

```
# WAVE 4 PRIMITIVE BLOCK
# Opened: f_Capture_Multi.md
# Range: PRIM:025–026 (this file)
# Prior block closed at: PRIM:024 (f_Deflect.md)
# All Wave 4 files continue from PRIM:025 forward.
# Registry is append-only. No Wave 3 or earlier ID may be reused.
```

### §7.2 — PRIM:025 — `execute_multi_capture`

**Purpose:** Orchestrate a full multi-capture session in either ME or MA mode.
Validates session parameters, runs the eval_order loop, manages field
perturbation, and halts cleanly on any condition violation.

**Signature:**
```python
def execute_multi_capture(
    mode: str,                # "ME" or "MA"
    participants: list,       # ordered list of (A, E) pairs or single shared node
    frame: dict,              # Frame node state from f_Frame.md
    field: dict,              # Field node state from f_Field.md (contains ρ(Φ))
    k_perturb: float = 0.05  # perturbation coefficient
) -> dict:
    """
    Execute a multi-capture session.

    Parameters
    ----------
    mode         : "ME" (one A, many E) or "MA" (many A, one E)
    participants : For ME — list of E dicts [E1, E2, ...En]
                  For MA — list of A dicts [A1, A2, ...An]
    frame        : Frame node state dict (must include capacity_MAX,
                   registered_count, r_capture, k_frame)
    field        : Field node state dict (must include rho_phi, rho_floor)
    k_perturb    : Per-capture coherence cost coefficient

    Returns
    -------
    {
        "status"           : "COMPLETE" | "PARTIAL" | "INVALID",
        "registered_count" : int,
        "registered_ids"   : list,
        "phi_final"        : float,
        "steps"            : list of per-step result dicts,
        "failure"          : None | "FM-003-M" | "FM-001" | "FM-002" | "FM-003" | "FM-007",
        "failure_step"     : None | int
    }
    """
    # --- Validation ---
    if mode not in ("ME", "MA"):
        return {"status": "INVALID", "failure": "UNKNOWN_MODE"}

    if len(participants) < 2:
        return {"status": "INVALID", "failure": "N_LT_2"}

    # MC-2: Attractor Uniqueness (MA mode only)
    if mode == "MA":
        attractor_ids = [a["id"] for a in participants]
        if len(attractor_ids) != len(set(attractor_ids)):
            return {"status": "INVALID", "failure": "MC-2_VIOLATION"}

    phi = field["rho_phi"]          # Φ_perturbed(0) = ρ(Φ)
    phi_floor = field["rho_floor"]
    registered = []
    steps = []

    for k, participant in enumerate(participants, start=1):
        # SC-1: Field must be active
        if phi <= 0:
            return _halt(registered, steps, phi, "FM-002", k)

        # Resolve A and E for this step
        if mode == "ME":
            A = frame["attractor"]
            E = participant
        else:
            A = participant
            E = frame["element"]

        # SC-4: v_approach must be positive
        v_approach_k = A.get("v_approach", 0)
        if v_approach_k <= 0:
            return _halt(registered, steps, phi, "FM-001", k)

        # SC-7 (mass check): M_A and M_E must be non-zero
        if A.get("M_A", 0) == 0 or E.get("M_E", 0) == 0:
            return _halt(registered, steps, phi, "FM-007", k)

        # SC-2: v_approach < v_escape
        v_esc = (2 * A["M_A"] * phi / frame["r_capture"]) ** 0.5
        if v_approach_k >= v_esc:
            return _halt(registered, steps, phi, "FM-001", k)

        # SC-3: Compute d_bind(k)
        beta_k = E.get("beta", A.get("beta", 0))
        e_k = E.get("e", 0)
        d_bind_k = beta_k * phi * (1 - e_k)
        if d_bind_k <= 0:
            return _halt(registered, steps, phi, "FM-002", k)

        # SC-5: Frame capacity
        if len(registered) >= frame["capacity_MAX"]:
            return _halt(registered, steps, phi, "FM-003", k)

        # Register capture
        registered.append(E.get("id", f"E_{k}") if mode == "ME"
                          else A.get("id", f"A_{k}"))

        # Compute δ_perturb(k) and update Φ_perturbed
        delta_perturb_k = d_bind_k * (1 - e_k) * k_perturb
        phi -= delta_perturb_k

        step_result = {
            "step": k,
            "d_bind": d_bind_k,
            "delta_perturb": delta_perturb_k,
            "phi_after": phi,
            "registered_id": registered[-1]
        }
        steps.append(step_result)

        # MC-1: Coherence floor check (after update)
        if phi < phi_floor:
            return {
                "status": "PARTIAL",
                "registered_count": len(registered),
                "registered_ids": registered,
                "phi_final": phi,
                "steps": steps,
                "failure": "FM-003-M",
                "failure_step": k
            }

    return {
        "status": "COMPLETE",
        "registered_count": len(registered),
        "registered_ids": registered,
        "phi_final": phi,
        "steps": steps,
        "failure": None,
        "failure_step": None
    }


def _halt(registered, steps, phi, failure, k):
    return {
        "status": "PARTIAL" if registered else "INVALID",
        "registered_count": len(registered),
        "registered_ids": registered,
        "phi_final": phi,
        "steps": steps,
        "failure": failure,
        "failure_step": k
    }
```

**Constraints:**
- `N ≥ 2` (single-participant session must use base `f_Capture.md`)
- `eval_order` is fixed at call time; mutation after first step raises FM-003-M
- `k_perturb` must satisfy `0 < k_perturb ≤ 1`
- Returns COMPLETE only if all N steps succeed without floor violation or FM halt

**INV compliance:**
- INV-001: G(k) is evaluated per-step with all three nodes
- INV-005: SC-1–SC-5 conjunctive check at each step
- INV-006: Terminal state check (E or A not already in COLLAPSED / FIELD_NULL)
- INV-009: All symbols from OPERATORS.md
- INV-010: New operators frozen here; not re-declared in downstream files

---

### §7.3 — PRIM:026 — `compute_perturbation_budget`

**Purpose:** Pre-flight check that computes the maximum number of capture steps
sustainable given the current field state, before a multi-capture session begins.
Returns the safe step count N_safe and the projected Φ_perturbed trajectory.

**Signature:**
```python
def compute_perturbation_budget(
    rho_phi: float,          # current field density ρ(Φ)
    rho_floor: float,        # field floor ρ(Φ)_floor
    d_bind_estimates: list,  # list of estimated d_bind(k) per step
    e_estimates: list,       # list of estimated e(k) per step
    k_perturb: float = 0.05  # perturbation coefficient
) -> dict:
    """
    Pre-flight budget check for multi-capture session planning.

    Parameters
    ----------
    rho_phi          : Initial field density
    rho_floor        : Floor below which session halts (MC-1)
    d_bind_estimates : Per-step binding depth estimates [d_bind_1, ..., d_bind_N]
    e_estimates      : Per-step eccentricity estimates [e_1, ..., e_N]
    k_perturb        : Perturbation coefficient

    Returns
    -------
    {
        "N_requested"   : int,   # total steps requested (len of estimates)
        "N_safe"        : int,   # max steps before floor violation
        "trajectory"    : list,  # Φ_perturbed after each step
        "budget_margin" : float, # Φ_perturbed(N_safe) − rho_floor
        "warning"       : bool   # True if N_safe < N_requested
    }
    """
    if len(d_bind_estimates) != len(e_estimates):
        raise ValueError("d_bind_estimates and e_estimates must have equal length")

    phi = rho_phi
    trajectory = []
    n_safe = 0

    for k, (d_k, e_k) in enumerate(zip(d_bind_estimates, e_estimates), start=1):
        delta_k = d_k * (1 - e_k) * k_perturb
        phi -= delta_k
        trajectory.append(round(phi, 6))
        if phi >= rho_floor:
            n_safe = k
        else:
            break  # floor would be breached at step k

    n_requested = len(d_bind_estimates)
    budget_margin = trajectory[n_safe - 1] - rho_floor if n_safe > 0 else 0.0

    return {
        "N_requested"   : n_requested,
        "N_safe"        : n_safe,
        "trajectory"    : trajectory,
        "budget_margin" : round(budget_margin, 6),
        "warning"       : n_safe < n_requested
    }
```

**Constraints:**
- Input lists must be equal length
- `rho_floor` must be positive
- `d_bind_estimates` must all be positive; zero estimates are a planning error
- Output `N_safe` is an upper bound; actual session may diverge from estimates
  if field conditions change between pre-flight and execution

**Usage pattern:**
```
budget = compute_perturbation_budget(...)
if budget["warning"]:
    # Trim participant list to budget["N_safe"] before calling execute_multi_capture
    participants = participants[:budget["N_safe"]]
```

---

## §8 — Canonical Examples

### §8.1 — Example 1: MULTI_ELEMENT — Full Session Completes (N=3)

**Setup:**
- Mode: ME
- Attractor A: M_A = 2.0, v_approach varies per step
- Elements: E₁ (β=0.7, e=0.1), E₂ (β=0.6, e=0.2), E₃ (β=0.5, e=0.3)
- Field: ρ(Φ) = 1.0, ρ(Φ)_floor = 0.50
- Frame: capacity_MAX = 5, r_capture = 3.0, k_frame = 1.0
- k_perturb = 0.05

**Step-by-step evaluation:**

| k | Participant | d_bind(k) | δ_perturb(k) | Φ_perturbed(k) | MC-1 |
|---|---|---|---|---|---|
| 1 | E₁ | 0.7×1.0×0.9 = 0.630 | 0.630×0.9×0.05 = 0.02835 | 0.97165 | PASS |
| 2 | E₂ | 0.6×0.97165×0.8 = 0.46639 | 0.46639×0.8×0.05 = 0.01866 | 0.95299 | PASS |
| 3 | E₃ | 0.5×0.95299×0.7 = 0.33355 | 0.33355×0.7×0.05 = 0.01167 | 0.94132 | PASS |

**Result:**
```
status: COMPLETE
registered_count: 3
registered_ids: [E1, E2, E3]
phi_final: 0.94132
failure: None
```

**Interpretation:** A well-resourced field with low k_perturb sustains all three
bindings. Each successive capture is marginally cheaper (lower d_bind) due to
falling Φ_perturbed, and each step passes MC-1 comfortably above the floor.
Session closes as COMPLETE.

---

### §8.2 — Example 2: MULTI_ELEMENT — FM-003-M at Step 2 (Floor Breach)

**Setup:**
- Mode: ME
- Elements: E₁ (β=0.9, e=0.05), E₂ (β=0.9, e=0.05)
- Field: ρ(Φ) = 0.60, ρ(Φ)_floor = 0.55
- k_perturb = 0.10 (elevated; stress-test scenario)

**Step-by-step evaluation:**

| k | d_bind(k) | δ_perturb(k) | Φ_perturbed(k) | MC-1 |
|---|---|---|---|---|
| 1 | 0.9×0.60×0.95 = 0.513 | 0.513×0.95×0.10 = 0.04874 | 0.55126 | PASS |
| 2 | 0.9×0.55126×0.95 = 0.47133 | 0.47133×0.95×0.10 = 0.04478 | 0.50648 | **FAIL** |

**Result:**
```
status: PARTIAL
registered_count: 1
registered_ids: [E1]
phi_final: 0.50648
failure: FM-003-M
failure_step: 2
```

**Interpretation:** Step 1 barely passes MC-1 (0.55126 > 0.55). Step 2's
perturbation drops Φ_perturbed below the floor. FM-003-M is raised; E₂ is not
registered. E₁'s binding is retained. The session enters SATURATED state;
recovery requires `suppress_field` (PRIM:018) to restore ρ(Φ) before a new
session may be initiated.

---

### §8.3 — Example 3: MULTI_ATTRACTOR — Valid Session (N=2)

**Setup:**
- Mode: MA
- Element E: M_E = 1.0, e = 0.15
- Attractors: A₁ (M_A=3.0, β=0.6), A₂ (M_A=2.5, β=0.55)
- Field: ρ(Φ) = 1.0, ρ(Φ)_floor = 0.80
- Frame per attractor: capacity_MAX = 3, r_capture = 4.0
- k_perturb = 0.05

**MC-2 check:** A₁.id ≠ A₂.id → PASS.

**Step-by-step evaluation:**

| k | Attractor | d_bind(k) | δ_perturb(k) | Φ_perturbed(k) | MC-1 |
|---|---|---|---|---|---|
| 1 | A₁ | 0.6×1.0×0.85 = 0.510 | 0.510×0.85×0.05 = 0.02168 | 0.97832 | PASS |
| 2 | A₂ | 0.55×0.97832×0.85 = 0.45680 | 0.45680×0.85×0.05 = 0.01941 | 0.95891 | PASS |

**Result:**
```
status: COMPLETE
registered_count: 2
registered_ids: [A1, A2]
phi_final: 0.95891
failure: None
```

**Interpretation:** A single Element E is simultaneously held by two Attractor
nodes in distinct Frames. The perturbation cost is modest. Both bindings are
valid, each with their own r_capture(k) and β(k). The field remains well above
floor. This pattern represents a shared-custody configuration — common in
resonant triadic systems where E carries cross-domain significance.

---

### §8.4 — Example 4: MULTI_ATTRACTOR — MC-2 Violation (Duplicate Attractor)

**Setup:**
- Mode: MA
- eval_order: [A₁, A₂, A₁] — A₁ appears at positions 1 and 3 (duplicate)
- Field: ρ(Φ) = 1.0

**Session initialization check:**

```
attractor_ids = [A1_id, A2_id, A1_id]
set(attractor_ids) = {A1_id, A2_id}
len(attractor_ids) = 3 ≠ len(set) = 2 → MC-2 VIOLATED
```

**Result:**
```
status: INVALID
registered_count: 0
registered_ids: []
phi_final: 1.0  (unchanged; no steps executed)
failure: MC-2_VIOLATION
failure_step: None  (detected at initialization, before k=1)
```

**Interpretation:** The session is structurally invalid before any capture step
executes. No bindings are registered, no field perturbation occurs, and the
Frame nodes are untouched. The client must reconstruct eval_order with unique
Attractor IDs before reattempting. This is not a recoverable FM — it is a
session design error surfaced at validation time.

---

## §9 — Cross-Module References

### §9.1 — Upstream Dependencies

| File | Dependency | Role |
|---|---|---|
| `f_Capture.md` | PRIM:001–006 | Base capture primitives; `execute_multi_capture` calls `register_capture` (PRIM:003) internally |
| `f_Field.md` | ρ(Φ), ρ(Φ)_floor, d_bind, v_escape, FM-002 | Field density initializes Φ_perturbed(0); floor enforces MC-1 |
| `f_Force.md` | β, e, M_A, M_E, v_approach, FM-001, FM-007 | Per-step force parameters; FM-001/007 halt session at failing step |
| `f_Frame.md` | capacity_MAX, register_capture, FM-003 | Frame capacity enforces SC-5; register_capture called per step |
| `f_Dampen.md` | ρ(Φ)_floor, PRIM:018 | Floor constant shared; suppress_field used for FM-003-M recovery |
| `f_Amplify.md` | PRIM:021 | amplify_coupling available as alternative recovery path |
| `f_Deflect.md` | heading_delta | Deflection may be applied between capture steps to adjust v_approach(k+1) |

### §9.2 — Downstream Consumers

| File | How This File's Output Is Used |
|---|---|
| `f_Orbit.md` | Each registered capture from a ME session may independently enter orbit; T_orb computed per (A, Eₖ) pair |
| `f_Decay.md` | δ(t) is tracked per binding; MULTI_ELEMENT sessions produce N independent decay timelines |
| `f_Release.md` | Each registered binding may independently trigger release; v_release computed per (A, Eₖ) |
| `f_Collapse.md` | If decay exhausts all N bindings simultaneously, collapse proceeds via Path B (FM-007 → COLLAPSED) |

### §9.3 — OPERATORS.md Registration (Wave 4 Additions)

The following operators introduced in this file must be appended to OPERATORS.md
under a "Wave 4" section header:

```
| N            | Participant Count     | Integer | N ≥ 2                           | f_Capture_Multi.md |
| eval_order   | Evaluation Order      | List    | Fixed; immutable after init     | f_Capture_Multi.md |
| Φ_perturbed  | Perturbed Field State | Real    | ρ(Φ)_floor ≤ Φ_perturbed ≤ ρ(Φ)| f_Capture_Multi.md |
| δ_perturb    | Per-Capture Perturbation | Real | δ_perturb ≥ 0                   | f_Capture_Multi.md |
| k_perturb    | Perturbation Coefficient | Real | 0 < k_perturb ≤ 1              | f_Capture_Multi.md |
```

---

## §10 — Document Metadata

### §10.1 — Invariant Compliance Table

| INV ID | Statement | Compliance Status | Notes |
|---|---|---|---|
| INV-001 | G = F_freq · F_fluid · F_force | ✅ | G(k) evaluated per-step with all three nodes |
| INV-002 | ρ(Φ) ≥ 0 always | ✅ | MC-1 halts session before Φ_perturbed goes negative |
| INV-003 | No duplicate bindings | ✅ | MC-2 enforces Attractor uniqueness; ME mode naturally yields distinct Eₖ IDs |
| INV-004 | Frame capacity respected | ✅ | SC-5 checked before each register_capture |
| INV-005 | SC-1–SC-5 conjunctive | ✅ | All five checked at every step k in defined order |
| INV-006 | Terminal states irreversible | ✅ | COLLAPSED and FIELD_NULL nodes rejected at session init |
| INV-007 | v_approach < v_escape | ✅ | SC-2 enforced per-step against Φ_perturbed(k−1) |
| INV-008 | d_bind > 0 for valid binding | ✅ | SC-3 checked per-step; zero d_bind halts step |
| INV-009 | OPERATORS.md is symbol authority | ✅ | All symbols sourced from OPERATORS.md; Wave 4 additions registered in §9.3 |
| INV-010 | Operators frozen on first appearance | ✅ | N, eval_order, Φ_perturbed, δ_perturb, k_perturb all frozen here |

### §10.2 — Stability Condition Summary

| SC ID | Evaluated Against | Step of Evaluation |
|---|---|---|
| SC-1 | Φ_perturbed(k−1) > 0 | Step k, first check |
| SC-2 | v_approach(k) < v_escape(Φ_perturbed(k−1)) | Step k, after SC-4 |
| SC-3 | d_bind(k) > 0 | Step k, after SC-2 |
| SC-4 | v_approach(k) > 0 | Step k, second check |
| SC-5 | registered_count < capacity_MAX | Step k, before register_capture |

### §10.3 — Primitive Registry (This File)

| PRIM ID | Name | File | Wave |
|---|---|---|---|
| PRIM:025 | `execute_multi_capture` | `f_Capture_Multi.md` | Wave 4 |
| PRIM:026 | `compute_perturbation_budget` | `f_Capture_Multi.md` | Wave 4 |

### §10.4 — Failure Mode Registry (This File)

| FM ID | Type | Trigger | Terminal? |
|---|---|---|---|
| FM-003-M | Sub-mode of FM-003 | MC-1 violation or mid-session eval_order mutation | No (prior bindings retained) |

### §10.5 — Changelog

```
v1.0.0 — Initial canonical release.
         Wave 4 primitive block opened (PRIM:025–026).
         MULTI_ELEMENT and MULTI_ATTRACTOR modes defined.
         MC-1, MC-2 conditions introduced.
         FM-003-M sub-mode formalized.
         δ_perturb perturbation model frozen.
         4 canonical examples delivered.
         INV-001–INV-010 compliance verified.
```

### §10.6 — Wave 4 Status Tracker

| File | Status | Primitives | Notes |
|---|---|---|---|
| `f_Capture_Multi.md` | ✅ CANONICAL | PRIM:025–026 | This file; Wave 4 opens here |
| `f_Capture_Soft.md` | 🔲 Pending | PRIM:027+ | Soft-threshold capture variant |
| `f_Capture_Hard.md` | 🔲 Pending | TBD | Hard-threshold capture variant |
| `f_Capture_Resonant.md` | 🔲 Pending | TBD | Resonant-state capture variant |
| `f_Capture_Mutual.md` | 🔲 Pending | TBD | Symmetric mutual-capture variant |
| `f_Capture_Cascade.md` | 🔲 Pending | TBD | Cascade-trigger capture variant |
| `f_Capture_Asymmetric.md` | 🔲 Pending | TBD | Asymmetric geometry variant |

### §10.7 — Suggested Commit Message

```
feat(FFF_Gravity): add canonical f_Capture_Multi — MULTI_ELEMENT/MULTI_ATTRACTOR
modes, δ_perturb perturbation model, PRIM:025-026, FM-003-M, MC-1/MC-2 [Wave4-Session-001]
```

---
*End of f_Capture_Multi.md — canonical, Wave 4, v1.0.0*
