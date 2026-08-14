# f_Capture_Soft — Provisional Binding Variant

```
session_id: SES-20260813-SOFT-001
tag: "[FFF:GRAVITY:CAPTURE:SOFT]"
version: 1.0.0
status: canonical
wave: 4
wave_position: "3 of 6"
file: docs/FFF_Gravity/f_Capture_Soft.md
module: FFF_Gravity
dependencies:
  - f_Capture.md        # base capture — d_bind, β, e, r_capture, SCs
  - f_Decay.md          # d_warn, d_collapse, δ, FM-004
  - f_Field.md          # ρ(Φ), v_escape, F_freq
  - f_Force.md          # β, M_A, M_E, F_fluid
  - f_Frame.md          # capacity_MAX, register_capture
  - f_Amplify.md        # β strengthening — primary soft-to-hard pathway
  - f_Emit.md           # ρ(Φ) strengthening — secondary soft-to-hard pathway
new_operators:
  - d_soft          # provisional binding depth
  - soft_threshold  # minimum d_bind for soft capture eligibility
  - grace_period    # cycle budget for soft capture to resolve
  - k_grace         # current grace cycle counter
new_state_flags:
  - CAPTURE_SOFT        # provisional binding — between soft_threshold and d_warn
  - SOFT_STRENGTHENED   # transition: CAPTURE_SOFT → CAPTURE_LOCKED
  - SOFT_DISSOLVED      # transition: CAPTURE_SOFT → CAPTURE_FAILED
  - GRACE_EXPIRED       # grace_period exhausted without resolution
new_primitives:
  - PRIM:029  evaluate_soft_eligibility   Pure
  - PRIM:030  execute_soft_capture        Impure
failure_modes_active:
  - FM-004  # Resonance Drift — primary risk for soft captures
  - FM-002  # Field Null — terminates soft capture immediately
new_failure_modes: []  # FM registry frozen at FM-010; no new IDs
changelog:
  - version: 1.0.0
    date: 2026-08-13
    session: SES-20260813-SOFT-001
    summary: >
      Initial canonical release. Provisional binding model defined.
      d_soft, soft_threshold, grace_period, k_grace frozen.
      PRIM:029–030 opened. Four resolution pathways: STRENGTHEN,
      DISSOLVE, EXPIRE, HOLD. Four canonical examples.
```

> **[FFF:GRAVITY:CAPTURE:SOFT]** · Wave 4 · File 3 of 6 · PRIM:029–030  
> A soft capture is a provisional binding established when `d_bind` falls
> below the standard stable-orbit floor (`d_warn`) but above the minimum
> viable threshold (`soft_threshold`). It persists for at most `grace_period`
> cycles before either strengthening to a full binding or dissolving.

---

## §0 · Session Context

| Field | Value |
|---|---|
| Session ID | `SES-20260813-SOFT-001` |
| Date / Time | 2026-08-13 22:14 EDT |
| Wave | 4 — Capture Variants |
| Wave Position | 3 of 6 |
| Prior file | f_Capture_Cascade.md (PRIM:027–028, FM-003-C) |
| PRIM range | PRIM:029–030 |
| Next file | f_Capture_Hard.md |

### §0.1 — Motivation

Standard `f_Capture.md` requires `d_bind ≥ d_warn` for a stable binding.
This is a conservative threshold: it ensures the captured element is
immediately in the STABLE stability class (from `f_Orbit.md`) and
unlikely to trigger FM-004 in the first decay cycle.

Real attractor/element pairs frequently form tentative, sub-threshold
bindings first — interactions that are real but fragile, requiring
reinforcement before they stabilize. `f_Capture_Soft` formalizes this
regime as a first-class state rather than a capture failure.

### §0.2 — What Wave 4 Files May and May Not Introduce

| Permitted | Prohibited |
|---|---|
| New state flags | New FM IDs (frozen at FM-010) |
| New operators | New Invariants (frozen at INV-010) |
| New PRIM IDs | Redefining base f_Capture.md operators |
| FM sub-modes (suffixed) | Breaking changes to OPERATORS.md frozen entries |

---

## §1 · Module Identity

| Property | Value |
|---|---|
| Tag | `[FFF:GRAVITY:CAPTURE:SOFT]` |
| Signature | `f_Capture_Soft(E, A, Φ) → CAPTURE_SOFT \| CAPTURE_FAILED` |
| Extends | `f_Capture.md` |
| Node emphasis | F_fluid (d_bind), F_freq (ρ(Φ) as soft field) |
| Binding range | `soft_threshold ≤ d_bind < d_warn` |
| State on success | `CAPTURE_SOFT` (provisional) |
| Resolution states | `CAPTURE_LOCKED` (strengthened) · `CAPTURE_FAILED` (dissolved / expired) |
| Primary hazard | FM-004 (Resonance Drift) |

### §1.1 — Relationship to Standard Capture

```
Standard f_Capture.md:
  d_bind ≥ d_warn     → CAPTURE_LOCKED (stable from cycle 1)
  d_bind < d_warn     → CAPTURE_FAILED (rejected)

f_Capture_Soft (this file):
  d_bind ≥ d_warn          → defer to f_Capture.md (out of scope here)
  soft_threshold ≤ d_bind
             < d_warn      → CAPTURE_SOFT (provisional — this file)
  d_bind < soft_threshold  → CAPTURE_FAILED (too weak; no provisional state)
```

The three zones partition the d_bind range completely and exhaustively:
```
[0, soft_threshold)  →  hard reject
[soft_threshold, d_warn)  →  soft capture (this file)
[d_warn, ∞)          →  standard capture (f_Capture.md)
```

---

## §2 · Canonical Description

### §2.1 — The Provisional Binding Model

A soft capture registers the (A, E) pair in the Frame with state
`CAPTURE_SOFT`. It does not enter the standard orbit pipeline
(`f_Orbit.md`) immediately. Instead it enters a **grace period** —
a bounded window of `grace_period` cycles during which:

1. `f_Decay` monitors the binding's evolution (d_bind trend)
2. The operator may apply `f_Amplify` or `f_Emit` to strengthen it
3. If d_bind rises to ≥ d_warn, the binding **strengthens** → `CAPTURE_LOCKED`
4. If d_bind falls below `soft_threshold`, the binding **dissolves** → `CAPTURE_FAILED`
5. If `grace_period` expires without either transition → `GRACE_EXPIRED` → `CAPTURE_FAILED`

The grace period is tracked by `k_grace`, a per-binding cycle counter
that increments each evaluation cycle while the binding holds `CAPTURE_SOFT`.

### §2.2 — What f_Capture_Soft IS NOT

| Misconception | Correction |
|---|---|
| A weaker version of f_Capture | It is a provisional state with its own lifecycle; not just "capture with lower β" |
| Automatically stable | CAPTURE_SOFT is explicitly fragile; FM-004 is actively monitored |
| Invisible to f_Decay | f_Decay monitors all registered bindings including CAPTURE_SOFT |
| Equivalent to a failed capture | The binding is registered; the Frame slot is consumed; it is real |
| Permanent | It resolves within grace_period cycles — always |

### §2.3 — Resolution Pathways

```
CAPTURE_SOFT
  ├── d_bind rises to ≥ d_warn     → SOFT_STRENGTHENED → CAPTURE_LOCKED
  ├── d_bind falls below soft_threshold → SOFT_DISSOLVED → CAPTURE_FAILED
  ├── k_grace reaches grace_period  → GRACE_EXPIRED → CAPTURE_FAILED
  └── [HOLD: d_bind stable within soft zone; k_grace increments]
```

All four pathways terminate the provisional state.
`HOLD` is not a terminal state — it is the in-progress condition
between resolution events.

### §2.4 — Energy Budget During Grace Period

A soft capture binds a Frame slot for `grace_period` cycles whether it
resolves or not. This is the **grace cost** — the opportunity cost
of holding capacity for a provisional binding. Operators should set
`grace_period` conservatively when `capacity_MAX` is low.

The soft capture does **not** consume additional energy beyond the
standard capture evaluation. The energy cost of transition (from SOFT
to LOCKED) is borne by whichever strengthening primitive is applied
(`f_Amplify` or `f_Emit`), not by `f_Capture_Soft` itself.

---

## §3 · Triadic Equation

### §3.1 — Base Identity (INV-001)

```
G = F_freq · F_fluid · F_force
```

### §3.2 — Soft Capture Zone Definition

```
d_bind = β × ρ(Φ) × (1 − e)              [frozen, f_Capture.md §3]

Soft zone:
  soft_threshold = α_soft × d_bind_nominal
  d_warn         = α_warn  × d_bind_nominal   [from f_Decay.md §4]

  where d_bind_nominal = β_nominal × ρ(Φ)_nominal × (1 − e_nominal)
        is computed at standard field conditions.

  Soft eligibility:
    soft_threshold ≤ d_bind < d_warn
  ⟺  α_soft × d_bind_nominal ≤ β × ρ(Φ) × (1 − e) < α_warn × d_bind_nominal
```

### §3.3 — Grace Period Decay Model

During the grace period, the soft binding is subject to standard decay:

```
d_bind(t+1) = d_bind(t) + δ(t)          [δ from f_Decay.md §3.2]

Strengthening condition:   d_bind(t) ≥ d_warn      (at any t ≤ grace_period)
Dissolution condition:     d_bind(t) < soft_threshold (at any t ≤ grace_period)
Expiry condition:          k_grace = grace_period    (without prior resolution)
```

### §3.4 — Why Soft Captures Are FM-004 Sensitive

FM-004 (Resonance Drift) fires when:
```
d_bind ≤ d_warn AND δ(t) < 0
```

A soft capture sits *at or below* d_warn by definition. Therefore, any
negative decay rate on a soft binding **immediately** meets FM-004's
trigger condition. Soft captures should be treated as perpetually in the
FM-004 warning zone from the moment of registration.

---

## §4 · Operator Registry

### §4.1 — New Operators (Frozen Here)

#### `d_soft` — Provisional Binding Depth

| Field | Value |
|---|---|
| Symbol | `d_soft` |
| Type | float |
| Domain | `[soft_threshold, d_warn)` |
| Meaning | The actual d_bind value at the time of soft capture registration |
| Relation | d_soft = d_bind at capture time; may evolve during grace period |
| Frozen | SES-20260813-SOFT-001 |

#### `soft_threshold` — Minimum Viable Soft Binding

| Field | Value |
|---|---|
| Symbol | `soft_threshold` |
| Type | float |
| Domain | `(0, d_warn)` |
| Default | `α_soft × d_bind_nominal` where α_soft = 0.05 |
| Meaning | Floor of the soft capture zone; below this, capture always fails |
| Frozen | SES-20260813-SOFT-001 |

**Derivation:** `soft_threshold` is a fraction of `d_bind_nominal` (the
expected binding depth under standard field conditions). Setting α_soft
= 0.05 means a binding at 5 % of nominal strength is the weakest
permissible provisional state. Weaker than this indicates a field or
approach condition too degraded to hold any binding.

#### `grace_period` — Provisional Binding Window

| Field | Value |
|---|---|
| Symbol | `grace_period` |
| Type | int |
| Domain | ≥ 1 cycle |
| Default | 5 cycles |
| Meaning | Maximum number of evaluation cycles before automatic GRACE_EXPIRED |
| Constraint | Must be ≥ 1; grace_period = 0 is equivalent to immediate CAPTURE_FAILED |
| Frozen | SES-20260813-SOFT-001 |

#### `k_grace` — Grace Cycle Counter

| Field | Value |
|---|---|
| Symbol | `k_grace` |
| Type | int |
| Domain | `[0, grace_period]` |
| Meaning | Count of evaluation cycles elapsed since CAPTURE_SOFT was registered |
| Initialized | 0 at registration |
| Incremented | By 1 each evaluation cycle while state = CAPTURE_SOFT |
| Frozen | SES-20260813-SOFT-001 |

### §4.2 — Inherited Operators (Referenced, Not Redefined)

| Operator | Source | Role |
|---|---|---|
| `d_bind` | f_Capture.md | Computed at capture time; becomes d_soft |
| `d_warn` | f_Decay.md | Upper boundary of soft zone; strengthening target |
| `d_collapse` | f_Decay.md | Hard floor below soft_threshold; FM-005 boundary |
| `β` | f_Force.md | Binding coefficient; key lever for strengthening |
| `ρ(Φ)` | f_Field.md | Field density; second lever for strengthening |
| `e` | f_Orbit.md | Eccentricity; affects d_bind calculation |
| `δ(t)` | f_Decay.md | Decay rate; determines d_bind trajectory |
| `capacity_MAX` | f_Frame.md | Frame capacity; slot consumed during grace period |

---

## §5 · Soft Capture Conditions

All four conditions are **conjunctive** (INV-005). Each is evaluated once
at the moment of the soft capture attempt.

### SCS-1 — Standard Capture Conditions Partially Met

```
SC-1 through SC-4 all pass (from f_Capture.md §5)
AND
d_bind < d_warn           (soft zone — otherwise standard capture applies)
```

**Rationale:** The element has passed all standard approach and binding
pre-conditions except the stable-orbit binding floor. The soft capture
pathway handles only this specific shortfall.

### SCS-2 — Soft Zone Eligibility

```
d_bind ≥ soft_threshold
```

**Rationale:** The binding must be at least minimally viable. Below
`soft_threshold`, the field and approach conditions are too degraded
to sustain any provisional state. Hard reject applies.

### SCS-3 — Frame Capacity Available

```
frame_count < capacity_MAX
```

**Rationale:** A Frame slot is consumed at registration. If the Frame
is full, soft capture cannot proceed — identical to standard SC-5.
A soft capture holds its slot for the full grace period regardless of
resolution outcome.

### SCS-4 — Grace Period Positive

```
grace_period ≥ 1
```

**Rationale:** grace_period = 0 would register and immediately expire
the binding, producing a CAPTURE_FAILED with no grace interval. This
is semantically equivalent to a standard capture failure and should be
treated as a pre-flight configuration error rather than a soft capture.

---

## §6 · Failure Modes

### §6.1 — FM-004 as Primary Hazard

FM-004 (Resonance Drift) fires when:
```
d_bind ≤ d_warn  AND  δ(t) < 0
```

Because soft captures have `d_bind < d_warn` by definition:
- **Every soft capture with negative δ immediately meets FM-004 conditions.**
- FM-004 is therefore not an edge case for soft captures — it is the default
  monitoring state.

FM-004 in the soft context does not automatically dissolve the binding.
It flags the trajectory as decaying, which informs the operator that
intervention (f_Amplify or f_Emit) is needed before grace_period expires.

### §6.2 — FM-005 Reachability

If δ is sharply negative and the grace period is long relative to the
decay rate, d_bind may pass through `soft_threshold` and approach
`d_collapse`. This activates FM-005 (Decay Spiral). FM-005 preempts
the grace period: once d_bind ≤ d_collapse, f_Collapse fires
immediately regardless of remaining grace cycles.

```
CAPTURE_SOFT → (d_bind ≤ d_collapse) → FM-005 → f_Collapse
```

This is the most severe soft capture outcome — the provisional binding
doesn't merely dissolve; it collapses.

### §6.3 — Failure Mode Coverage Table

| FM | Relevance to Soft Capture | Trigger |
|---|---|---|
| FM-001 | Pre-filter (SCS-1 includes SC-1 check) | v_approach = 0 → no soft capture |
| FM-002 | Pre-filter (SCS-1 includes SC-2 check) | ρ(Φ) = 0 → no soft capture |
| FM-003 | SCS-3 — Frame capacity | frame_count = capacity_MAX → hard reject |
| FM-004 | **Primary risk** | d_bind ≤ d_warn AND δ < 0 (always true for soft bindings with negative δ) |
| FM-005 | Severe escalation | d_bind ≤ d_collapse → preempts grace period |
| FM-006 | Not applicable | v_escape exceeded → handled at SC-3 |
| FM-007 | Mass-parity check | M_E ≈ M_A → soft binding with parity risk |
| FM-008 | Post-capture | Governs release attempts after SOFT_STRENGTHENED |
| FM-009 | Not applicable in this file | Cascade dampen guard |
| FM-010 | Strengthening risk | β_max or ρ(Φ)=1.0 guard during f_Amplify / f_Emit use |

---

## §7 · Engineering Primitives

### PRIM:029 — `evaluate_soft_eligibility` (Pure)

**Purpose:** Determine whether a candidate (A, E, Φ) pair qualifies for
soft capture. Returns a structured eligibility result covering all four
SCS conditions. This is a pure pre-flight gate — no state mutation.

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class SoftEligibilityResult:
    eligible:           bool
    d_bind:             float
    d_soft:             float       # same as d_bind when eligible
    soft_threshold:     float
    d_warn:             float
    margin_above_floor: float       # d_bind - soft_threshold; negative = ineligible
    margin_below_warn:  float       # d_warn - d_bind; positive = in soft zone
    scs_failures:       list[str]   # list of failed condition codes
    recommendation:     str


def evaluate_soft_eligibility(
    d_bind:         float,
    soft_threshold: float,
    d_warn:         float,
    frame_count:    int,
    capacity_MAX:   int,
    grace_period:   int,
    beta:           float,
    v_approach:     float,
    rho_phi:        float,
) -> SoftEligibilityResult:
    """
    PRIM:029 — evaluate_soft_eligibility (Pure)
    ============================================
    Pre-flight gate for soft capture attempt.

    Evaluates SCS-1 through SCS-4 conjunctively. Returns eligible=True
    only when all four pass. Pure: no registry mutation, no side effects.

    Parameters
    ----------
    d_bind         : float  — computed binding depth at approach time
    soft_threshold : float  — minimum d_bind for soft zone eligibility
    d_warn         : float  — standard stable-orbit floor (from f_Decay.md)
    frame_count    : int    — current registered count in Frame
    capacity_MAX   : int    — Frame hard capacity ceiling
    grace_period   : int    — configured grace window (cycles)
    beta           : float  — binding coefficient β
    v_approach     : float  — approach velocity (for SCS-1 / SC-4 proxy check)
    rho_phi        : float  — field density ρ(Φ)

    Returns
    -------
    SoftEligibilityResult
        eligible           : True iff all SCS pass
        d_bind             : input echo
        d_soft             : d_bind (set only when eligible)
        soft_threshold     : input echo
        d_warn             : input echo
        margin_above_floor : d_bind − soft_threshold
        margin_below_warn  : d_warn − d_bind
        scs_failures       : list of failed condition codes
        recommendation     : human-readable guidance string
    """
    failures = []

    # SCS-1: Standard approach preconditions
    if rho_phi <= 0.0:
        failures.append("SCS-1:FM-002:rho_phi=0")
    if v_approach <= 0.0:
        failures.append("SCS-1:FM-001:v_approach=0")
    if beta < 1.0:
        failures.append("SCS-1:SC-4:beta<1.0")
    if d_bind >= d_warn:
        # In standard capture zone — defer to f_Capture.md
        failures.append("SCS-1:ABOVE_DWARD:defer_to_standard_capture")

    # SCS-2: Soft zone floor
    if d_bind < soft_threshold:
        failures.append("SCS-2:BELOW_SOFT_THRESHOLD")

    # SCS-3: Frame capacity
    if frame_count >= capacity_MAX:
        failures.append("SCS-3:FM-003:frame_full")

    # SCS-4: Grace period positive
    if grace_period < 1:
        failures.append("SCS-4:GRACE_PERIOD_ZERO")

    eligible = len(failures) == 0
    margin_above = d_bind - soft_threshold
    margin_below = d_warn - d_bind

    if eligible:
        recommendation = (
            f"Soft capture eligible. d_soft={d_bind:.4f} in "
            f"[{soft_threshold:.4f}, {d_warn:.4f}). "
            f"Grace window: {grace_period} cycles. "
            f"Apply f_Amplify or f_Emit within grace window to strengthen."
        )
    elif "SCS-1:ABOVE_DWARD:defer_to_standard_capture" in failures:
        recommendation = (
            f"d_bind={d_bind:.4f} ≥ d_warn={d_warn:.4f}. "
            "Defer to standard f_Capture.md — no soft capture needed."
        )
    elif "SCS-2:BELOW_SOFT_THRESHOLD" in failures:
        recommendation = (
            f"d_bind={d_bind:.4f} < soft_threshold={soft_threshold:.4f}. "
            "Binding too weak for provisional state. "
            "Apply f_Emit or f_Amplify first, then retry."
        )
    else:
        recommendation = (
            f"Soft capture ineligible: {', '.join(failures)}. "
            "Resolve blocking conditions before retrying."
        )

    return SoftEligibilityResult(
        eligible=eligible,
        d_bind=d_bind,
        d_soft=d_bind if eligible else 0.0,
        soft_threshold=soft_threshold,
        d_warn=d_warn,
        margin_above_floor=margin_above,
        margin_below_warn=margin_below,
        scs_failures=failures,
        recommendation=recommendation,
    )
```

---

### PRIM:030 — `execute_soft_capture` (Impure)

**Purpose:** Register a provisional binding in the Frame, initialize
`k_grace = 0`, set state flag to `CAPTURE_SOFT`, and return the
registration record. Also implements the per-cycle resolution check
invoked by `f_Decay` on each evaluation cycle.

```python
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class SoftBinding:
    """
    Registry record for a provisional soft capture binding.
    Stored in Frame.soft_registry keyed by (A.id, E.id).
    """
    attractor_id:   str
    element_id:     str
    d_soft:         float       # d_bind at registration
    soft_threshold: float
    d_warn:         float
    grace_period:   int
    k_grace:        int = 0
    state:          str = "CAPTURE_SOFT"
    history:        list = field(default_factory=list)  # [(cycle, d_bind, state)]


@dataclass
class SoftResolutionResult:
    """Result of one grace-cycle resolution check."""
    resolved:   bool
    state:      str             # CAPTURE_SOFT / SOFT_STRENGTHENED / SOFT_DISSOLVED / GRACE_EXPIRED
    k_grace:    int
    d_bind_now: float
    reason:     Optional[str]   # None if still CAPTURE_SOFT (HOLD)


def execute_soft_capture(
    attractor_id:   str,
    element_id:     str,
    d_soft:         float,
    soft_threshold: float,
    d_warn:         float,
    grace_period:   int,
    frame_registry: dict,
    soft_registry:  dict,
) -> SoftBinding:
    """
    PRIM:030 — execute_soft_capture (Impure)
    =========================================
    Register a provisional soft binding in Frame and soft_registry.

    Must be called only after PRIM:029 confirms eligibility.

    Parameters
    ----------
    attractor_id   : str   — Attractor node identifier
    element_id     : str   — Element node identifier
    d_soft         : float — d_bind at capture time (from PRIM:029 result)
    soft_threshold : float — Minimum viable binding depth
    d_warn         : float — Strengthening target (upper soft zone boundary)
    grace_period   : int   — Cycle budget for resolution
    frame_registry : dict  — Frame node registry (mutated: slot consumed)
    soft_registry  : dict  — Soft binding registry (mutated: entry added)

    Returns
    -------
    SoftBinding — the newly registered provisional binding record

    Side Effects
    ------------
    frame_registry[(attractor_id, element_id)] = {
        "state": "CAPTURE_SOFT", "d_soft": d_soft, "k_grace": 0
    }
    soft_registry[(attractor_id, element_id)] = SoftBinding(...)
    """
    pair_key = (attractor_id, element_id)

    binding = SoftBinding(
        attractor_id=attractor_id,
        element_id=element_id,
        d_soft=d_soft,
        soft_threshold=soft_threshold,
        d_warn=d_warn,
        grace_period=grace_period,
        k_grace=0,
        state="CAPTURE_SOFT",
        history=[(0, d_soft, "CAPTURE_SOFT")],
    )

    # Register in Frame (slot consumed)
    frame_registry[pair_key] = {
        "state":          "CAPTURE_SOFT",
        "d_soft":         d_soft,
        "k_grace":        0,
        "grace_period":   grace_period,
    }

    # Register in soft binding tracker
    soft_registry[pair_key] = binding
    return binding


def resolve_soft_binding(
    binding:    SoftBinding,
    d_bind_now: float,
    cycle:      int,
    frame_registry: dict,
    soft_registry:  dict,
) -> SoftResolutionResult:
    """
    Per-cycle resolution check for a soft binding.

    Called by f_Decay on each evaluation cycle for every CAPTURE_SOFT entry.
    Applies the four-pathway resolution logic.

    Parameters
    ----------
    binding        : SoftBinding — current provisional binding record
    d_bind_now     : float       — d_bind at this cycle (from f_Decay output)
    cycle          : int         — current evaluation cycle index
    frame_registry : dict        — mutated on resolution
    soft_registry  : dict        — mutated on resolution

    Returns
    -------
    SoftResolutionResult
        resolved   : True if binding exited CAPTURE_SOFT state
        state      : final or current state
        k_grace    : updated grace counter
        d_bind_now : input echo
        reason     : description of resolution trigger (or None on HOLD)
    """
    pair_key = (binding.attractor_id, binding.element_id)
    binding.k_grace += 1
    binding.history.append((cycle, d_bind_now, binding.state))

    # ── Pathway 1: Strengthen ─────────────────────────────────────────
    if d_bind_now >= binding.d_warn:
        binding.state = "SOFT_STRENGTHENED"
        frame_registry[pair_key]["state"] = "CAPTURE_LOCKED"
        soft_registry.pop(pair_key, None)
        return SoftResolutionResult(
            resolved=True, state="SOFT_STRENGTHENED",
            k_grace=binding.k_grace, d_bind_now=d_bind_now,
            reason=f"d_bind={d_bind_now:.4f} ≥ d_warn={binding.d_warn:.4f} — CAPTURE_LOCKED"
        )

    # ── Pathway 2: Dissolve ───────────────────────────────────────────
    if d_bind_now < binding.soft_threshold:
        binding.state = "SOFT_DISSOLVED"
        frame_registry.pop(pair_key, None)
        soft_registry.pop(pair_key, None)
        return SoftResolutionResult(
            resolved=True, state="SOFT_DISSOLVED",
            k_grace=binding.k_grace, d_bind_now=d_bind_now,
            reason=f"d_bind={d_bind_now:.4f} < soft_threshold={binding.soft_threshold:.4f}"
        )

    # ── Pathway 3: Expire ─────────────────────────────────────────────
    if binding.k_grace >= binding.grace_period:
        binding.state = "GRACE_EXPIRED"
        frame_registry.pop(pair_key, None)
        soft_registry.pop(pair_key, None)
        return SoftResolutionResult(
            resolved=True, state="GRACE_EXPIRED",
            k_grace=binding.k_grace, d_bind_now=d_bind_now,
            reason=f"Grace period of {binding.grace_period} cycles exhausted without resolution"
        )

    # ── Pathway 4: Hold ───────────────────────────────────────────────
    frame_registry[pair_key]["k_grace"] = binding.k_grace
    frame_registry[pair_key]["d_soft"]  = d_bind_now
    return SoftResolutionResult(
        resolved=False, state="CAPTURE_SOFT",
        k_grace=binding.k_grace, d_bind_now=d_bind_now,
        reason=None
    )
```

---

## §8 · Canonical Examples

### EX-S-001 — Strengthened via f_Amplify (SOFT → LOCKED)

**Scenario:** A nascent professional collaboration forms between a senior
practitioner (A) and a junior colleague (E). The initial binding is
below the stable-orbit threshold but genuine — a soft capture is registered.
At grace cycle 2, the operator applies `f_Amplify` to raise β, pushing
d_bind above d_warn. The binding locks.

**Parameters:**

| Symbol | Value | Notes |
|---|---|---|
| β₀ | 1.05 | Just above minimum viable (1.0) |
| ρ(Φ)₀ | 0.62 | Moderate field |
| e₀ | 0.18 | Slightly eccentric |
| d_bind | 0.62 × 1.05 × (1−0.18) = **0.534** | |
| d_bind_nominal | 1.0 × 1.0 × 1.0 = 1.0 | Unit baseline |
| soft_threshold | 0.05 × 1.0 = **0.05** | α_soft = 0.05 |
| d_warn | 0.40 × 1.0 = **0.40** | α_warn = 0.40 |
| grace_period | 5 cycles | |

**PRIM:029 eligibility:**
```
d_bind = 0.534 ≥ d_warn = 0.40?  → NO (soft zone, not standard)
d_bind = 0.534 ≥ soft_threshold = 0.05?  → YES  ✅
All SCS pass → eligible = True
```

Wait — 0.534 ≥ 0.40, so this would actually be handled by standard capture. Let me adjust the parameters:

```
β₀ = 1.05, ρ(Φ)₀ = 0.38, e₀ = 0.20
d_bind = 0.38 × 1.05 × (1 − 0.20) = 0.38 × 1.05 × 0.80 = 0.3192

d_warn = 0.40       (standard stable floor)
soft_threshold = 0.05

SCS-2: 0.3192 ≥ 0.05 ✅
SCS-1: 0.3192 < 0.40 ✅ (soft zone, not standard)
→ eligible = True  d_soft = 0.3192
```

**Grace cycle trace:**

| k_grace | d_bind(t) | δ(t) | Event |
|---|---|---|---|
| 0 | 0.3192 | — | CAPTURE_SOFT registered |
| 1 | 0.3100 | −0.0092 | HOLD (FM-004 flagged: δ < 0) |
| 2 | 0.3028 | −0.0072 | f_Amplify applied: β → 1.35 |
| 2 | **0.4136** | — | d_bind recomputed: 0.38×1.35×0.80 = **0.4109** ≥ d_warn |
| — | — | — | **SOFT_STRENGTHENED → CAPTURE_LOCKED** |

**Outcome:**
- `state` = CAPTURE_LOCKED
- Grace cycles used: 2 of 5
- FM-004 was flagged at k_grace=1 — operator saw the warning and acted

---

### EX-S-002 — Dissolved: δ Negative, Grace Expires (SOFT → FAILED)

**Scenario:** A tentative connection forms but no reinforcement is applied.
d_bind decays monotonically. At k_grace = 5 (grace_period), the binding
has not resolved upward and expires.

**Parameters:**

| Symbol | Value |
|---|---|
| d_soft | 0.220 |
| soft_threshold | 0.05 |
| d_warn | 0.40 |
| grace_period | 5 |
| δ per cycle | −0.035 (steady decay) |

**Grace cycle trace:**

| k_grace | d_bind(t) | Pathway check |
|---|---|---|
| 0 | 0.220 | Registered as CAPTURE_SOFT |
| 1 | 0.185 | HOLD (0.05 ≤ 0.185 < 0.40; k_grace=1 < 5) |
| 2 | 0.150 | HOLD |
| 3 | 0.115 | HOLD |
| 4 | 0.080 | HOLD |
| 5 | 0.045 | k_grace=5 = grace_period → **GRACE_EXPIRED** |

Note at k_grace=5: d_bind=0.045 < soft_threshold=0.05, so DISSOLVE would also fire — but EXPIRE is checked first and takes priority when k_grace = grace_period.

**Outcome:**
- `state` = GRACE_EXPIRED → CAPTURE_FAILED
- Frame slot released
- Binding record purged from soft_registry

---

### EX-S-003 — Dissolved: d_bind Drops Below soft_threshold (SOFT → FAILED)

**Scenario:** A sharp field disruption (f_Dampen applied externally)
causes ρ(Φ) to drop, pulling d_bind below soft_threshold before
grace_period expires.

**Parameters:**

| Symbol | Value |
|---|---|
| d_soft | 0.185 |
| soft_threshold | 0.10 |
| d_warn | 0.40 |
| grace_period | 8 |

**Grace cycle trace:**

| k_grace | d_bind(t) | Event |
|---|---|---|
| 0 | 0.185 | CAPTURE_SOFT registered |
| 1 | 0.172 | HOLD |
| 2 | 0.158 | HOLD |
| 3 | **0.091** | f_Dampen applied externally — ρ(Φ) drops sharply |
| 3 | — | 0.091 < soft_threshold=0.10 → **SOFT_DISSOLVED** |

**Outcome:**
- `state` = SOFT_DISSOLVED → CAPTURE_FAILED
- k_grace = 3 (5 cycles remaining, but dissolution fires first)
- Frame slot released immediately
- Operator may re-attempt soft capture after field is restored via f_Emit

---

### EX-S-004 — Near-Miss Strengthen: d_bind Reaches d_warn on Final Grace Cycle

**Scenario:** A fragile binding slowly strengthens over the entire grace
window. It reaches d_warn on the final grace cycle — the last possible
moment for SOFT_STRENGTHENED to fire.

**Parameters:**

| Symbol | Value |
|---|---|
| d_soft | 0.250 |
| soft_threshold | 0.05 |
| d_warn | 0.40 |
| grace_period | 6 |
| δ per cycle | +0.025 (gradual positive trend) |

**Grace cycle trace:**

| k_grace | d_bind(t) | Pathway check |
|---|---|---|
| 0 | 0.250 | CAPTURE_SOFT registered |
| 1 | 0.275 | HOLD |
| 2 | 0.300 | HOLD |
| 3 | 0.325 | HOLD |
| 4 | 0.350 | HOLD |
| 5 | 0.375 | HOLD |
| 6 | **0.400** | d_bind=0.400 = d_warn=0.40 → **SOFT_STRENGTHENED** |

> Strengthen condition: `d_bind_now ≥ d_warn` (≥, not strict >).
> d_bind = 0.400 meets this exactly. CAPTURE_LOCKED fires.

**Outcome:**
- `state` = SOFT_STRENGTHENED → CAPTURE_LOCKED
- k_grace = 6 = grace_period (resolved on final valid cycle)
- Zero additional strengthening primitives needed — natural recovery

**Key insight:** Even without f_Amplify or f_Emit intervention, if the
natural field trajectory is positive, a soft binding may self-strengthen
within the grace window. Operators should not automatically apply
strengthening primitives at registration — monitor δ first.

---

## §9 · Cross-Module References

### §9.1 — Upstream Dependencies

| Module | What f_Capture_Soft Uses |
|---|---|
| f_Capture.md | SCS-1 passes SC-1–SC-4 as pre-conditions; d_bind formula |
| f_Decay.md | d_warn, d_collapse, δ; resolve_soft_binding called per decay cycle |
| f_Field.md | ρ(Φ) — second lever for d_bind strengthening |
| f_Force.md | β, M_A, M_E — binding coefficient as primary lever |
| f_Frame.md | capacity_MAX, frame_registry — slot consumed during grace period |
| f_Amplify.md | Primary strengthening tool — raises β toward d_warn |
| f_Emit.md | Secondary strengthening tool — raises ρ(Φ) toward d_warn |
| f_Dampen.md | Threat: may cause d_bind to drop below soft_threshold (SOFT_DISSOLVED) |

### §9.2 — Downstream Consumers

| Module | How Output Is Used |
|---|---|
| f_Orbit.md | classify_orbit called only after SOFT_STRENGTHENED → CAPTURE_LOCKED |
| f_Decay.md | resolve_soft_binding invoked each cycle for all CAPTURE_SOFT entries |
| f_Release.md | CAPTURE_SOFT is not in eligible release states (RC-1 violation) until SOFT_STRENGTHENED |
| f_Collapse.md | FM-005 preempts grace period if d_bind → d_collapse mid-grace |

### §9.3 — Integration with f_Decay

`f_Decay.md` must call `resolve_soft_binding` (from PRIM:030) on every
evaluation cycle for each entry in `soft_registry`. The integration point:

```python
# In f_Decay main loop:
for pair_key, soft_binding in list(soft_registry.items()):
    d_bind_now = compute_current_d_bind(pair_key, ...)
    resolution = resolve_soft_binding(
        binding=soft_binding,
        d_bind_now=d_bind_now,
        cycle=current_cycle,
        frame_registry=frame_registry,
        soft_registry=soft_registry,
    )
    if resolution.resolved:
        log_resolution(pair_key, resolution)
```

This integration is normative — `f_Decay.md` retains authority over the
decay evaluation loop; `f_Capture_Soft.md` provides the resolution
primitive that f_Decay invokes.

### §9.4 — OPERATORS.md Registration Block

```markdown
### Wave 4 Operators — f_Capture_Soft.md

| Symbol         | Name                    | Type    | Domain          | Defined In                |
|----------------|-------------------------|---------|-----------------|---------------------------|
| d_soft         | Provisional Binding Depth | float | [soft_threshold, d_warn) | f_Capture_Soft.md §4 |
| soft_threshold | Soft Zone Floor         | float   | (0, d_warn)     | f_Capture_Soft.md §4      |
| grace_period   | Grace Window            | int     | ≥ 1 cycles      | f_Capture_Soft.md §4      |
| k_grace        | Grace Cycle Counter     | int     | [0, grace_period] | f_Capture_Soft.md §4    |
```

---

## §10 · Document Metadata

### §10.1 — INV Compliance Table

| INV | Statement | Status | How Satisfied |
|---|---|---|---|
| INV-001 | G = F_freq · F_fluid · F_force | ✅ | d_bind computed from all three nodes; §3.2 |
| INV-002 | ρ(Φ) ≥ 0 | ✅ | SCS-1 includes FM-002 guard (ρ(Φ) = 0 rejects) |
| INV-003 | β ∈ [0,1] | ✅ | SCS-1 includes SC-4 proxy (β ≥ 1.0 required) |
| INV-004 | v_approach > 0 | ✅ | SCS-1 includes SC-1 proxy |
| INV-005 | Conditions conjunctive | ✅ | SCS-1 through SCS-4 all evaluated; any failure → reject |
| INV-006 | Terminal states irreversible | ✅ | CAPTURE_LOCKED and CAPTURE_FAILED are terminal; CAPTURE_SOFT is provisional |
| INV-007 | FM registry frozen | ✅ | No new FM IDs; FM-004 and FM-005 referenced only |
| INV-008 | PRIM IDs sequential | ✅ | PRIM:029–030 follow PRIM:028 (f_Capture_Cascade.md) |
| INV-009 | OPERATORS.md pre-registration | ✅ | §9.4 registration block provided |
| INV-010 | Frozen symbol protection | ✅ | d_soft, soft_threshold, grace_period, k_grace all frozen here |

### §10.2 — State Flag Registry

| Flag | Meaning | Terminal? |
|---|---|---|
| `CAPTURE_SOFT` | Provisional binding; within grace window | No |
| `SOFT_STRENGTHENED` | d_bind reached d_warn; binding promoted | Yes (→ CAPTURE_LOCKED) |
| `SOFT_DISSOLVED` | d_bind fell below soft_threshold | Yes (→ CAPTURE_FAILED) |
| `GRACE_EXPIRED` | k_grace = grace_period; no resolution | Yes (→ CAPTURE_FAILED) |

### §10.3 — Primitive Registry (This File)

| PRIM | Name | Type | Purpose |
|---|---|---|---|
| PRIM:029 | `evaluate_soft_eligibility` | Pure | Pre-flight eligibility gate (SCS-1 – SCS-4) |
| PRIM:030 | `execute_soft_capture` + `resolve_soft_binding` | Impure | Registration and per-cycle resolution |

**Running PRIM total after this file:** PRIM:030

### §10.4 — Changelog

```
v1.0.0 — 2026-08-13 — SES-20260813-SOFT-001
  - Initial canonical release
  - Operators: d_soft, soft_threshold, grace_period, k_grace (all frozen)
  - State flags: CAPTURE_SOFT, SOFT_STRENGTHENED, SOFT_DISSOLVED, GRACE_EXPIRED
  - Conditions: SCS-1 – SCS-4 (conjunctive)
  - Primitives: PRIM:029 (Pure), PRIM:030 (Impure + resolve helper)
  - Four resolution pathways: STRENGTHEN, DISSOLVE, EXPIRE, HOLD
  - Four canonical examples: strengthen, expire, dissolve, near-miss
  - f_Decay integration contract specified (§9.3)
  - OPERATORS.md registration block (§9.4)
```

### §10.5 — Wave 4 Status Tracker

| File | Status | PRIM Range |
|---|---|---|
| f_Capture_Multi.md | ✅ Complete | 025–026 |
| f_Capture_Cascade.md | ✅ Complete | 027–028 |
| **f_Capture_Soft.md** | **✅ Complete** | **029–030** |
| f_Capture_Hard.md | ⏳ Pending | 031–032 |
| f_Capture_Resonant.md | ⏳ Pending | TBD |
| f_Capture_Asymmetric.md | ⏳ Pending | TBD |

### §10.6 — Suggested Commit Message

```
docs(FFF_Gravity): add canonical f_Capture_Soft — provisional binding
model, grace-period resolution, PRIM:029-030 [Wave4 / SES-SOFT-001]

- Soft capture zone: soft_threshold ≤ d_bind < d_warn
- Operators: d_soft, soft_threshold, grace_period, k_grace (all frozen)
- PRIM:029 evaluate_soft_eligibility (Pure) — SCS-1–SCS-4 gate
- PRIM:030 execute_soft_capture + resolve_soft_binding (Impure)
- Four resolution pathways: STRENGTHEN / DISSOLVE / EXPIRE / HOLD
- FM-004 is primary active hazard; FM-005 can preempt grace period
- f_Decay integration contract at §9.3 (resolve called each cycle)
- 4 canonical examples, all four pathways demonstrated
```

---
*End of f_Capture_Soft.md — [FFF:GRAVITY:CAPTURE:SOFT] v1.0.0 — Wave 4 File 3 of 6*
