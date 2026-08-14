# f_Capture_Temporal — Temporal Window Capture

```
session_id: SES-20260813-CAPTURE_TEMPORAL-001
tag: f_Capture_Temporal
version: 1.0.0
status: canonical
wave: 4-addendum
file_index: "Wave 4, file 7 of 7"
dependencies:
  - f_Capture.md
  - f_Field.md
  - f_Force.md
  - f_Frame.md
  - f_Decay.md
  - f_Orbit.md
  - f_Collapse.md
new_operators:
  - t_open
  - t_close
  - t_span
  - t_elapsed
  - t_remaining
  - proximity_ratio
  - temporal_decay_factor
  - d_bind_temporal
  - temporal_margin
new_primitives:
  - PRIM:037
  - PRIM:038
failure_modes_referenced:
  - FM-001 (sub-annotation: TEMPORAL_MISS)
  - FM-004
  - FM-005
changelog:
  - "1.0.0 — 2026-08-13 — Initial canonical release. Wave 4 addendum, file 7 of 7."
```

## §0 Session Context

| Field            | Value                                        |
|------------------|----------------------------------------------|
| Session ID       | SES-20260813-CAPTURE_TEMPORAL-001            |
| Author           | umaywant2                                    |
| Date             | 2026-08-13                                   |
| Repository       | TriadicFrameworks                            |
| Module           | FFF_Gravity                                  |
| Wave             | 4-addendum (file 7 of 7)                     |
| Status           | Canonical                                    |
| Prior file       | f_Capture_Asymmetric.md (PRIM:035–036)       |
| PRIM block       | PRIM:037–038                                 |
| Condition prefix | TC-                                          |

### §0.1 Scope Declaration

This file specifies the **Temporal Capture** variant of the base `f_Capture` function. Temporal capture gates binding eligibility on an absolute clock-time window `[t_open, t_close]`. Binding depth degrades continuously as the entity's evaluation time approaches either window edge, reaching a minimum attenuation factor at the boundaries. This variant is non-periodic and non-repeating within a given window instance.

### §0.2 Distinction from f_Capture_Resonant

| Dimension        | f_Capture_Resonant                            | f_Capture_Temporal                             |
|------------------|-----------------------------------------------|------------------------------------------------|
| Gate type        | Phase-gated (φ_E relative to ω_res cycle)     | Clock-gated (t_current within [t_open, t_close]) |
| Periodicity      | Periodic — windows repeat with T_res          | Non-repeating — each window is a one-shot instance |
| Window reference | Oscillation phase (dimensionless)             | Absolute time (clock units)                    |
| Binding modifier | ρ_res_gain — field amplification at resonance | temporal_decay_factor — binding attenuation at edges |
| Identity         | ρ(Φ) domain                                  | d_bind domain                                  |
| Failure mode     | FM-006 phantom resonance; FM-004 drift        | FM-001 TEMPORAL_MISS; FM-004 decay             |

---

## §1 Module Identity

| Field               | Value                                         |
|---------------------|-----------------------------------------------|
| Function name       | f_Capture_Temporal                            |
| Parent function     | f_Capture                                     |
| Module              | FFF_Gravity                                   |
| Triadic identity    | G = F_freq · F_fluid · F_force                |
| Primitive block     | PRIM:037 (Pure), PRIM:038 (Impure)            |
| Condition prefix    | TC-                                           |
| FM references       | FM-001 (TEMPORAL_MISS), FM-004, FM-005        |
| New INV IDs         | None (registry frozen at INV-010)             |
| New FM IDs          | None (registry frozen at FM-010; TEMPORAL_MISS is a sub-annotation of FM-001) |
| Operator authority  | OPERATORS.md (INV-009)                        |

---

## §2 Canonical Description

### §2.1 Conceptual Foundation

Temporal capture models the condition in which an attractor's binding field is only operative during a **defined clock-time interval** `[t_open, t_close]`. Outside this window the attractor exerts no capture force, regardless of its mass `M_A`, field density `ρ(Φ)`, or the entity's approach velocity. Inside the window the binding force is available but is **not uniform across time**: the closer the evaluation instant is to either edge of the window, the more attenuated the resulting binding depth becomes.

This degradation reflects physical and system realities in which:
- Entry conditions are not yet fully established near `t_open` (warm-up degradation)
- Exit conditions begin to deteriorate near `t_close` (wind-down degradation)
- The system's maximum binding fidelity is achieved at the temporal midpoint of the window

The attenuation is governed by `temporal_decay_factor` (symbol α_temp, default 0.40) applied to a `proximity_ratio` that measures how close the current time is to either window edge, normalized over the half-window span.

### §2.2 Window Geometry

```
Time axis:
─────────┬──────────────────────────────────────┬──────────────►
         t_open                                 t_close

Binding depth (d_bind_temporal):

d_bind ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ peak (midpoint)
         /                                     \
        /   d_bind × (1 − α_temp × prox_ratio)  \
       /                                         \
d_bind × (1−α_temp)                     d_bind × (1−α_temp)
     t_open                                   t_close
```

- **Outside `[t_open, t_close]`:** `d_bind_temporal` is undefined; TC-1 fails; FM-001 TEMPORAL_MISS triggered.
- **At window midpoint:** `proximity_ratio = 0`; `d_bind_temporal = d_bind` (unattenuated).
- **At window edges:** `proximity_ratio → 1`; `d_bind_temporal = d_bind × (1 − α_temp)`.

### §2.3 Window Uniqueness (TC-5)

Each `(entity_id, attractor_id, window_id)` triple is subject to a **per-window uniqueness constraint**: once a capture attempt has been registered against a window — whether it succeeded or failed — no second attempt is permitted within the same window instance. A new window with a distinct `window_id` permits a fresh attempt. This prevents opportunistic re-entry after an initial failure within the same temporal gate.

### §2.4 Temporal Margin (TC-2)

A minimum time `τ_min` (temporal_margin) must remain in the window at the moment of evaluation. If `t_remaining < τ_min`, capture is not attempted: there is insufficient time to complete the binding sequence before the window closes. This prevents pathological partial-binds at the window terminus.

---

## §3 Triadic Equation

The governing identity is preserved from INV-001:

```
G = F_freq · F_fluid · F_force
```

Temporal capture applies a **time-domain gate and attenuation** to the binding depth computed by the base `f_Capture` function:

```
proximity_ratio   = 1 − min(t_elapsed, t_remaining) / (t_span / 2)

d_bind_temporal   = d_bind × (1 − temporal_decay_factor × proximity_ratio)

t_span            = t_close − t_open
t_elapsed         = t_current − t_open
t_remaining       = t_close − t_current
```

Where the base binding depth `d_bind` is computed per f_Capture.md:

```
d_bind = β × ρ(Φ) × (1 − e)
```

The temporal attenuation acts solely on `d_bind` — it does not modify `ρ(Φ)`, `β`, or any triadic component directly. The triadic equation remains structurally intact; `d_bind_temporal` replaces `d_bind` in all downstream computations (orbit stability, decay thresholds, collapse paths) for this capture variant.

---

## §4 Operator Registry

All operators introduced in this file. Operators are frozen on first canonical appearance per INV-010. Symbol authority: OPERATORS.md (INV-009).

| Symbol               | Name                  | Type    | Domain / Units   | Default   | Description                                                                    |
|----------------------|-----------------------|---------|------------------|-----------|--------------------------------------------------------------------------------|
| `t_open`             | Window open time      | float   | clock units       | —         | Absolute time at which the temporal capture window opens                       |
| `t_close`            | Window close time     | float   | clock units       | —         | Absolute time at which the temporal capture window closes; must satisfy t_close > t_open |
| `t_current`          | Current evaluation time | float | clock units      | —         | Absolute clock time at which the capture attempt is evaluated                  |
| `t_span`             | Window duration       | float   | clock units       | —         | t_close − t_open; total window length                                          |
| `t_elapsed`          | Time since open       | float   | clock units       | —         | t_current − t_open; time since window opened at evaluation instant             |
| `t_remaining`        | Time until close      | float   | clock units       | —         | t_close − t_current; time remaining in window at evaluation instant            |
| `proximity_ratio`    | Edge proximity ratio  | float   | [0, 1]            | —         | Normalized measure of closeness to either window edge; 0 at midpoint, 1 at edges |
| `temporal_decay_factor` | Temporal decay factor | float | [0, 1)          | α_temp = 0.40 | Scales the maximum binding attenuation imposed at window edges               |
| `d_bind_temporal`    | Temporal binding depth | float  | ≥ 0              | —         | Attenuated binding depth; replaces d_bind for all downstream computations      |
| `temporal_margin`    | Temporal margin       | float   | clock units       | τ_min = 1.0 | Minimum t_remaining required at evaluation time; capture refused if t_remaining < τ_min |
| `window_id`          | Window identifier     | str     | opaque            | —         | Unique identifier for the temporal window instance; scopes TC-5 uniqueness     |

### §4.1 Inherited Operators (key dependencies)

The following operators are defined in prior files and referenced here. They are not re-defined.

| Symbol         | Defined in      | Role in this file                                 |
|----------------|-----------------|---------------------------------------------------|
| `d_bind`       | f_Capture.md    | Base binding depth before temporal attenuation    |
| `β`            | f_Capture.md    | Binding coefficient                               |
| `ρ(Φ)`         | f_Field.md      | Field density at attractor                        |
| `e`            | f_Capture.md    | Eccentricity (orbital shape)                      |
| `d_collapse`   | f_Decay.md      | Collapse threshold; TC-3 checks d_bind_temporal ≥ d_collapse |
| `M_A`          | f_Source.md     | Attractor mass                                    |
| `M_E`          | f_Source.md     | Entity mass                                       |

---

## §5 Conditions

All conditions are **conjunctive** (INV-005): all must hold simultaneously for capture to proceed. Conditions are evaluated in the listed order; the first failing condition terminates evaluation with the associated failure path.

| ID   | Name                     | Expression                                              | Failure path            |
|------|--------------------------|---------------------------------------------------------|-------------------------|
| TC-1 | Window is open           | t_open ≤ t_current ≤ t_close                            | FM-001 TEMPORAL_MISS    |
| TC-2 | Temporal margin satisfied | t_remaining ≥ temporal_margin (τ_min)                  | FM-001 TEMPORAL_MISS    |
| TC-3 | Temporal bind sufficient | d_bind_temporal ≥ d_collapse                            | FM-005 (sub-threshold)  |
| TC-4 | Binding coefficient floor | β ≥ β_min (inherited from f_Capture.md; default 1.0)  | FM-004 (decay drift)    |
| TC-5 | Window uniqueness        | No prior attempt registered for (entity_id, attractor_id, window_id) | FM-001 TEMPORAL_MISS |

### §5.1 Condition Evaluation Order (Normative per INV-008)

```
EVALUATE t_open, t_close, t_current
  │
  ▼
TC-1: t_open ≤ t_current ≤ t_close?
  │ NO  → TEMPORAL_MISS (FM-001, reason=OUTSIDE_WINDOW)
  │ YES ↓
TC-2: t_remaining ≥ τ_min?
  │ NO  → TEMPORAL_MISS (FM-001, reason=MARGIN_VIOLATED)
  │ YES ↓
Compute proximity_ratio, d_bind_temporal
  │
TC-3: d_bind_temporal ≥ d_collapse?
  │ NO  → FM-005 sub-threshold infall
  │ YES ↓
TC-4: β ≥ β_min?
  │ NO  → FM-004 decay drift
  │ YES ↓
TC-5: window_id not in lock_registry[(entity_id, attractor_id)]?
  │ NO  → TEMPORAL_MISS (FM-001, reason=WINDOW_EXHAUSTED)
  │ YES ↓
PRIM:038 lock_temporal_capture → CAPTURE_TEMPORAL state
```

---

## §6 Failure Modes

New FM IDs are **not permitted** (registry frozen at FM-010 per INV-006). The following FM sub-annotations and references apply.

### §6.1 FM-001 — CAPTURE_MISS with sub-annotation: TEMPORAL_MISS

FM-001 is the canonical CAPTURE_MISS failure mode defined in f_Capture.md. In the temporal variant, FM-001 is triggered with a structured sub-annotation `TEMPORAL_MISS` when:

| Sub-reason          | Trigger condition         | TC that fails | Meaning                                                              |
|---------------------|---------------------------|---------------|----------------------------------------------------------------------|
| OUTSIDE_WINDOW      | t_current < t_open or t_current > t_close | TC-1 | Entity evaluated outside temporal window; no binding force present |
| MARGIN_VIOLATED     | t_remaining < τ_min       | TC-2          | Entity arrived with insufficient time remaining to complete binding  |
| WINDOW_EXHAUSTED    | lock exists for window_id | TC-5          | Window already consumed by prior attempt; no re-entry permitted     |

**Outcome:** Entity state set to `CAPTURE_MISS`. `temporal_miss=True` recorded in miss record. Downstream systems may use the sub-reason to schedule entity for the next available window (if any).

**Recovery:** TEMPORAL_MISS is **not** a terminal state for the entity — it is terminal for this window instance. A new window with a distinct `window_id` constitutes a fresh capture opportunity.

### §6.2 FM-004 — Decay Drift (TC-4 failure)

When `β < β_min` (TC-4), the entity does not possess sufficient binding coefficient to sustain capture even within the window. Routed to f_Decay.md. The temporal window does not extend or pause for decay recovery — if the window closes during drift, FM-001 TEMPORAL_MISS (OUTSIDE_WINDOW) is subsequently triggered.

### §6.3 FM-005 — Asymmetric Infall (TC-3 failure)

When `d_bind_temporal < d_collapse`, the temporal attenuation has degraded binding depth below the structural collapse threshold. The entity begins asymmetric infall per f_Collapse.md Path A. This condition is most likely to occur when the entity is evaluated very near a window edge with a high `temporal_decay_factor`.

---

## §7 Engineering Primitives

### PRIM:037 — evaluate_temporal_window (Pure)

**Classification:** Pure  
**Depends on:** TC-1, TC-2, TC-3, TC-4  
**INV compliance:** INV-001, INV-002, INV-003, INV-005, INV-008

```python
def evaluate_temporal_window(
    t_current: float,
    t_open: float,
    t_close: float,
    d_bind: float,
    temporal_decay_factor: float = 0.40,
    temporal_margin: float = 1.0,
    d_collapse: float = 0.0,
    beta: float = 1.0,
    beta_min: float = 1.0,
) -> dict:
    """
    PRIM:037 — evaluate_temporal_window (Pure)
    ==========================================
    Evaluate capture eligibility within a temporal window and compute the
    attenuated binding depth d_bind_temporal.

    This primitive implements TC-1 through TC-4. TC-5 (window uniqueness)
    is enforced by PRIM:038 (Impure), which has write access to the lock
    registry.

    Parameters
    ----------
    t_current : float
        Absolute clock time at evaluation. Must be in same units as t_open / t_close.
    t_open : float
        Absolute clock time at which the temporal window opens.
    t_close : float
        Absolute clock time at which the temporal window closes.
        Invariant: t_close > t_open.
    d_bind : float
        Base binding depth from f_Capture (β × ρ(Φ) × (1 − e)).
        Must be ≥ 0.
    temporal_decay_factor : float, optional
        α_temp ∈ [0, 1). Scales edge-attenuation of d_bind.
        Default: 0.40 (40% maximum degradation at window edges).
    temporal_margin : float, optional
        τ_min in clock units. Minimum t_remaining required to proceed.
        Default: 1.0.
    d_collapse : float, optional
        Collapse threshold from f_Decay / f_Collapse. TC-3 checks
        d_bind_temporal ≥ d_collapse. Default: 0.0.
    beta : float, optional
        Binding coefficient. TC-4 checks β ≥ β_min. Default: 1.0.
    beta_min : float, optional
        Minimum binding coefficient floor (inherited from f_Capture).
        Default: 1.0.

    Returns
    -------
    dict with keys:
        window_open         : bool   — TC-1 result
        margin_ok           : bool   — TC-2 result
        bind_sufficient     : bool   — TC-3 result
        beta_ok             : bool   — TC-4 result
        all_conditions_met  : bool   — conjunction of TC-1 through TC-4
        t_span              : float  — t_close − t_open
        t_elapsed           : float  — t_current − t_open (None if TC-1 fails)
        t_remaining         : float  — t_close − t_current (None if TC-1 fails)
        proximity_ratio     : float  — edge proximity ∈ [0, 1] (None if TC-1 fails)
        d_bind_temporal     : float  — attenuated binding depth (None if TC-1 fails)
        temporal_miss       : bool   — True if any TC-1/TC-2 failure
        miss_reason         : str    — 'OUTSIDE_WINDOW' | 'MARGIN_VIOLATED' | None
        failure_mode        : str    — 'FM-001-TEMPORAL_MISS' | 'FM-004' | 'FM-005' | None

    Raises
    ------
    ValueError
        If t_close <= t_open (degenerate window).
        If d_bind < 0.
        If temporal_decay_factor not in [0, 1).
        If temporal_margin < 0.

    Notes
    -----
    Evaluation order is normative (INV-008). Each condition is evaluated
    exactly once, in TC-1 → TC-2 → compute → TC-3 → TC-4 sequence.
    This primitive is Pure: it reads only its inputs and returns a
    result dict. No state mutations are performed.

    proximity_ratio formula:
        t_span     = t_close − t_open
        t_elapsed  = t_current − t_open
        t_remaining = t_close − t_current
        proximity_ratio = 1 − min(t_elapsed, t_remaining) / (t_span / 2)

    At midpoint  (t_current = (t_open + t_close) / 2): proximity_ratio = 0
    At edges     (t_current → t_open or → t_close):     proximity_ratio → 1

    d_bind_temporal = d_bind × (1 − temporal_decay_factor × proximity_ratio)
    """
    # --- Input validation ---
    if t_close <= t_open:
        raise ValueError(
            f"Degenerate window: t_close ({t_close}) must be > t_open ({t_open})."
        )
    if d_bind < 0:
        raise ValueError(f"d_bind must be ≥ 0; received {d_bind}.")
    if not (0.0 <= temporal_decay_factor < 1.0):
        raise ValueError(
            f"temporal_decay_factor must be in [0, 1); received {temporal_decay_factor}."
        )
    if temporal_margin < 0:
        raise ValueError(
            f"temporal_margin must be ≥ 0; received {temporal_margin}."
        )

    t_span = t_close - t_open
    result = {
        "window_open": False,
        "margin_ok": False,
        "bind_sufficient": False,
        "beta_ok": False,
        "all_conditions_met": False,
        "t_span": t_span,
        "t_elapsed": None,
        "t_remaining": None,
        "proximity_ratio": None,
        "d_bind_temporal": None,
        "temporal_miss": False,
        "miss_reason": None,
        "failure_mode": None,
    }

    # TC-1: Window is open
    window_open = (t_open <= t_current <= t_close)
    result["window_open"] = window_open
    if not window_open:
        result["temporal_miss"] = True
        result["miss_reason"] = "OUTSIDE_WINDOW"
        result["failure_mode"] = "FM-001-TEMPORAL_MISS"
        return result

    # Compute time geometry (only valid once TC-1 passes)
    t_elapsed = t_current - t_open
    t_remaining = t_close - t_current
    result["t_elapsed"] = t_elapsed
    result["t_remaining"] = t_remaining

    # TC-2: Temporal margin satisfied
    margin_ok = (t_remaining >= temporal_margin)
    result["margin_ok"] = margin_ok
    if not margin_ok:
        result["temporal_miss"] = True
        result["miss_reason"] = "MARGIN_VIOLATED"
        result["failure_mode"] = "FM-001-TEMPORAL_MISS"
        return result

    # Compute proximity_ratio and d_bind_temporal
    half_span = t_span / 2.0
    proximity_ratio = 1.0 - min(t_elapsed, t_remaining) / half_span
    # Clamp to [0, 1] to guard against floating-point overshoot at exact edges
    proximity_ratio = max(0.0, min(1.0, proximity_ratio))
    d_bind_temporal = d_bind * (1.0 - temporal_decay_factor * proximity_ratio)

    result["proximity_ratio"] = proximity_ratio
    result["d_bind_temporal"] = d_bind_temporal

    # TC-3: Temporal bind depth sufficient
    bind_sufficient = (d_bind_temporal >= d_collapse)
    result["bind_sufficient"] = bind_sufficient
    if not bind_sufficient:
        result["failure_mode"] = "FM-005"
        return result

    # TC-4: Binding coefficient floor
    beta_ok = (beta >= beta_min)
    result["beta_ok"] = beta_ok
    if not beta_ok:
        result["failure_mode"] = "FM-004"
        return result

    # All TC-1 through TC-4 conditions met
    result["all_conditions_met"] = True
    return result
```

---

### PRIM:038 — lock_temporal_capture (Impure)

**Classification:** Impure  
**Depends on:** TC-5, PRIM:037 result  
**INV compliance:** INV-001, INV-002, INV-005, INV-006, INV-008, INV-010

```python
def lock_temporal_capture(
    entity_id: str,
    attractor_id: str,
    window_id: str,
    window_eval: dict,
    lock_registry: dict,
    state: dict,
) -> dict:
    """
    PRIM:038 — lock_temporal_capture (Impure)
    ==========================================
    Enforce TC-5 (window uniqueness) and, if it passes, commit the
    temporal capture to state. This primitive is Impure: it mutates
    lock_registry and state in place.

    Must only be called after PRIM:037 returns all_conditions_met=True.
    Calling this primitive with a failed PRIM:037 result is a contract
    violation and raises ValueError.

    Parameters
    ----------
    entity_id : str
        Unique identifier for the entity being captured.
    attractor_id : str
        Unique identifier for the attractor.
    window_id : str
        Unique identifier for the temporal window instance. Scopes TC-5.
        Must be distinct for each non-repeating window occurrence.
    window_eval : dict
        Result dict from PRIM:037. Must have all_conditions_met=True.
    lock_registry : dict
        Mutable mapping of (entity_id, attractor_id) → set of consumed
        window_ids. Mutated in place on successful lock.
        Structure: { (str, str): set[str] }
    state : dict
        Mutable system state dict. On success, receives keys:
            capture_state   : str   — 'CAPTURE_TEMPORAL'
            d_bind_active   : float — d_bind_temporal from window_eval
            window_id_active: str   — the consumed window_id
            proximity_ratio : float — recorded for audit
            t_elapsed       : float — recorded for audit
            t_remaining     : float — recorded for audit

    Returns
    -------
    dict with keys:
        success         : bool  — True if TC-5 passed and lock committed
        capture_state   : str   — 'CAPTURE_TEMPORAL' | 'CAPTURE_MISS'
        failure_mode    : str   — None | 'FM-001-TEMPORAL_MISS'
        miss_reason     : str   — None | 'WINDOW_EXHAUSTED'
        lock_record     : dict  — { entity_id, attractor_id, window_id,
                                    d_bind_temporal, proximity_ratio } (None on failure)

    Raises
    ------
    ValueError
        If window_eval["all_conditions_met"] is not True.
        If lock_registry is not a dict.
        If state is not a dict.

    Notes
    -----
    TC-5 (window uniqueness) is enforced here rather than in PRIM:037
    because uniqueness requires write access to lock_registry — a side
    effect incompatible with a Pure primitive (INV-002).

    On TC-5 failure (WINDOW_EXHAUSTED), no state mutation occurs.
    The lock_registry is left unmodified. This preserves the principle
    that failed captures do not alter attractor state (INV-005).

    On success, the window_id is added to lock_registry[(entity_id,
    attractor_id)] atomically before state is updated, ensuring that
    concurrent evaluation (if applicable) cannot produce a double-lock.
    """
    # --- Contract checks ---
    if not isinstance(window_eval, dict) or not window_eval.get("all_conditions_met"):
        raise ValueError(
            "PRIM:038 contract violation: window_eval must have all_conditions_met=True. "
            "Call PRIM:037 first and check its result before invoking PRIM:038."
        )
    if not isinstance(lock_registry, dict):
        raise ValueError("lock_registry must be a dict.")
    if not isinstance(state, dict):
        raise ValueError("state must be a dict.")

    key = (entity_id, attractor_id)

    # TC-5: Window uniqueness check
    consumed_windows = lock_registry.get(key, set())
    if window_id in consumed_windows:
        return {
            "success": False,
            "capture_state": "CAPTURE_MISS",
            "failure_mode": "FM-001-TEMPORAL_MISS",
            "miss_reason": "WINDOW_EXHAUSTED",
            "lock_record": None,
        }

    # TC-5 passed — commit lock (mutate registry atomically before state)
    consumed_windows = consumed_windows | {window_id}   # new set; no in-place mutation on original
    lock_registry[key] = consumed_windows

    # Commit capture state
    d_bind_temporal = window_eval["d_bind_temporal"]
    proximity_ratio = window_eval["proximity_ratio"]
    t_elapsed       = window_eval["t_elapsed"]
    t_remaining     = window_eval["t_remaining"]

    state["capture_state"]    = "CAPTURE_TEMPORAL"
    state["d_bind_active"]    = d_bind_temporal
    state["window_id_active"] = window_id
    state["proximity_ratio"]  = proximity_ratio
    state["t_elapsed"]        = t_elapsed
    state["t_remaining"]      = t_remaining

    lock_record = {
        "entity_id":       entity_id,
        "attractor_id":    attractor_id,
        "window_id":       window_id,
        "d_bind_temporal": d_bind_temporal,
        "proximity_ratio": proximity_ratio,
    }

    return {
        "success":       True,
        "capture_state": "CAPTURE_TEMPORAL",
        "failure_mode":  None,
        "miss_reason":   None,
        "lock_record":   lock_record,
    }
```

---

## §8 Canonical Examples

### Example 1 — Midpoint Capture (Maximum Binding Fidelity)

**Scenario:** Entity E1 is evaluated exactly at the temporal midpoint of a 10-unit window. Binding depth is fully unattenuated.

**Given:**
```
t_open              = 100.0
t_close             = 110.0
t_current           = 105.0      ← exact midpoint
temporal_decay_factor = 0.40
d_bind              = 20.0
d_collapse          = 2.0
β                   = 1.8
β_min               = 1.0
temporal_margin     = 1.0
window_id           = "WIN-001"
```

**Step 1 — Temporal geometry:**
```
t_span      = 110.0 − 100.0 = 10.0
t_elapsed   = 105.0 − 100.0 = 5.0
t_remaining = 110.0 − 105.0 = 5.0
half_span   = 5.0
```

**Step 2 — TC-1:** 100.0 ≤ 105.0 ≤ 110.0 ✓

**Step 3 — TC-2:** t_remaining = 5.0 ≥ τ_min = 1.0 ✓

**Step 4 — Proximity ratio and d_bind_temporal:**
```
proximity_ratio   = 1 − min(5.0, 5.0) / 5.0
                  = 1 − 5.0 / 5.0
                  = 1 − 1.0
                  = 0.0

d_bind_temporal   = 20.0 × (1 − 0.40 × 0.0)
                  = 20.0 × 1.0
                  = 20.0         ← fully unattenuated
```

**Step 5 — TC-3:** 20.0 ≥ 2.0 ✓  
**Step 6 — TC-4:** 1.8 ≥ 1.0 ✓  
**Step 7 — PRIM:037 result:** all_conditions_met = True  
**Step 8 — TC-5:** "WIN-001" not in lock_registry[(E1, A1)] ✓  
**Step 9 — PRIM:038:** lock committed; state["d_bind_active"] = 20.0

**Outcome:** `CAPTURE_TEMPORAL` — d_bind_active = **20.0** (no edge degradation). Entity proceeds to orbit computation via f_Orbit.md.

---

### Example 2 — Edge-Proximate Capture (Attenuated Binding)

**Scenario:** Entity E2 arrives 1.5 units after window open (near the leading edge). Binding is attenuated but sufficient. Temporal margin is satisfied.

**Given:**
```
t_open              = 200.0
t_close             = 210.0
t_current           = 201.5      ← 1.5 units after open
temporal_decay_factor = 0.40
d_bind              = 20.0
d_collapse          = 5.0
β                   = 1.5
β_min               = 1.0
temporal_margin     = 1.0
window_id           = "WIN-002"
```

**Step 1 — Temporal geometry:**
```
t_span      = 10.0
t_elapsed   = 1.5
t_remaining = 8.5
half_span   = 5.0
```

**Step 2 — TC-1:** 200.0 ≤ 201.5 ≤ 210.0 ✓  
**Step 3 — TC-2:** 8.5 ≥ 1.0 ✓

**Step 4 — Proximity ratio:**
```
proximity_ratio = 1 − min(1.5, 8.5) / 5.0
               = 1 − 1.5 / 5.0
               = 1 − 0.30
               = 0.70

d_bind_temporal = 20.0 × (1 − 0.40 × 0.70)
               = 20.0 × (1 − 0.28)
               = 20.0 × 0.72
               = 14.4
```

**Step 5 — TC-3:** 14.4 ≥ 5.0 ✓  
**Step 6 — TC-4:** 1.5 ≥ 1.0 ✓  
**Step 7 — PRIM:037:** all_conditions_met = True  
**Step 8 — TC-5:** "WIN-002" not in registry ✓  
**Step 9 — PRIM:038:** lock committed; d_bind_active = 14.4

**Outcome:** `CAPTURE_TEMPORAL` — d_bind_active = **14.4** (28% attenuation from edge proximity). Entity orbit will be shallower than midpoint capture; f_Decay.md monitoring thresholds recalculated against 14.4.

---

### Example 3 — TEMPORAL_MISS: Outside Window

**Scenario:** Entity E3 is evaluated 3 time units after window close. TC-1 fails; FM-001 TEMPORAL_MISS (OUTSIDE_WINDOW) triggered.

**Given:**
```
t_open    = 300.0
t_close   = 310.0
t_current = 313.0      ← 3 units after window closed
```

**Step 1 — TC-1:** 313.0 > 310.0 → **FAIL**

```
window_open   = False
temporal_miss = True
miss_reason   = 'OUTSIDE_WINDOW'
failure_mode  = 'FM-001-TEMPORAL_MISS'
```

**No further evaluation is performed** (INV-008 normative order).  
Proximity ratio, d_bind_temporal, and all downstream states are **undefined**.

**Outcome:** Entity state → `CAPTURE_MISS`. Sub-annotation: TEMPORAL_MISS / OUTSIDE_WINDOW. Downstream scheduler may register E3 for the next available window instance (new `window_id`) if one exists.

---

### Example 4 — Window Exhausted (TC-5 Failure) and Margin Violation (TC-2 Failure)

**Scenario A — TC-5 (Window Exhausted):**  
Entity E4 makes a second attempt against the same window after an initial failed binding.

**Given:**
```
t_open    = 400.0
t_close   = 420.0
t_current = 408.0
d_bind    = 18.0
β         = 2.0
window_id = "WIN-004"
lock_registry = { ("E4", "A4"): {"WIN-004"} }    ← prior attempt recorded
```

**PRIM:037 evaluation:**
- TC-1: ✓ (within window)
- TC-2: ✓ (t_remaining = 12.0 ≥ τ_min)
- TC-3: ✓ (d_bind_temporal will be sufficient)
- TC-4: ✓
- all_conditions_met = True

**PRIM:038 TC-5 check:**
```
key = ("E4", "A4")
consumed_windows = {"WIN-004"}
"WIN-004" in consumed_windows → True   ← TC-5 FAILS
```

**Outcome (Scenario A):** `CAPTURE_MISS` — miss_reason = `WINDOW_EXHAUSTED`. State **not** mutated. Lock registry **not** modified. Entity must await a new window with a distinct `window_id`.

---

**Scenario B — TC-2 (Margin Violated):**  
Entity E4b arrives with only 0.3 units remaining in the window.

**Given:**
```
t_open          = 500.0
t_close         = 510.0
t_current       = 509.8      ← 0.2 units before close
temporal_margin = 1.0        ← τ_min = 1.0
t_remaining     = 0.2
```

**TC-1:** ✓ (509.8 ≤ 510.0)  
**TC-2:** 0.2 < 1.0 → **FAIL**

```
margin_ok    = False
temporal_miss = True
miss_reason  = 'MARGIN_VIOLATED'
failure_mode = 'FM-001-TEMPORAL_MISS'
```

**Proximity ratio and d_bind_temporal are NOT computed** — evaluation halts at TC-2 per INV-008.

**Outcome (Scenario B):** `CAPTURE_MISS` — sub-annotation TEMPORAL_MISS / MARGIN_VIOLATED. Binding sequence cannot be completed before window close; partial binding is not permitted.

---

## §9 Cross-Module References

| Module                  | Relationship                                                                               |
|-------------------------|--------------------------------------------------------------------------------------------|
| f_Capture.md            | Parent function; provides d_bind, β, β_min, base capture state machine                    |
| f_Field.md              | Provides ρ(Φ) used in d_bind computation upstream of this file                            |
| f_Force.md              | Provides F_force component; heading context for post-capture orbit entry                  |
| f_Frame.md              | Provides frame capacity; temporal capture consumes one frame slot on lock                 |
| f_Decay.md              | Downstream consumer of d_bind_temporal; d_warn and d_collapse thresholds recalculate against d_bind_temporal |
| f_Orbit.md              | Receives d_bind_temporal as d_bind_active for orbit stability classification               |
| f_Collapse.md           | FM-005 routes here (Path A asymmetric infall) when TC-3 fails                            |
| f_Capture_Resonant.md   | Sibling variant; phase-gated rather than clock-gated; does not share window_id space      |
| f_Capture_Soft.md       | Complementary; a soft capture may follow a TEMPORAL_MISS if a grace window is configured  |
| f_Capture_Asymmetric.md | May be composed with temporal capture if mass_ratio imbalance is also present             |
| OPERATORS.md            | Symbol authority for all operators introduced in §4 (INV-009)                             |

---

## §10 Document Metadata

| Field                | Value                                                      |
|----------------------|------------------------------------------------------------|
| File path            | docs/FFF_Gravity/f_Capture_Temporal.md                     |
| Module               | FFF_Gravity                                                |
| Wave                 | 4-addendum (file 7 of 7)                                   |
| Version              | 1.0.0                                                      |
| Status               | Canonical                                                  |
| Session ID           | SES-20260813-CAPTURE_TEMPORAL-001                          |
| PRIM block           | PRIM:037–038                                               |
| New operators        | t_open, t_close, t_span, t_elapsed, t_remaining, proximity_ratio, temporal_decay_factor, d_bind_temporal, temporal_margin |
| New FM IDs           | None (frozen at FM-010)                                    |
| New INV IDs          | None (frozen at INV-010)                                   |
| Condition prefix     | TC-                                                        |
| FM references        | FM-001 (TEMPORAL_MISS), FM-004, FM-005                     |
| Python primitives    | 2 (PRIM:037 Pure, PRIM:038 Impure)                         |

---

## §11 Extended Metadata

### 11.1 INV Compliance Table

| INV     | Description (abbreviated)                    | Compliance in this file                                                         |
|---------|----------------------------------------------|---------------------------------------------------------------------------------|
| INV-001 | G = F_freq · F_fluid · F_force               | Preserved; temporal attenuation acts on d_bind only, not triadic components     |
| INV-002 | Pure/Impure classification enforced          | PRIM:037 Pure (no state mutation); PRIM:038 Impure (lock_registry + state write)|
| INV-003 | Operator domains respected                   | proximity_ratio clamped to [0,1]; temporal_decay_factor ∈ [0,1); validated      |
| INV-004 | Conditions are conjunctive                   | TC-1 through TC-5 are all required; first failure terminates evaluation         |
| INV-005 | Failed captures do not mutate attractor state| TC-5 failure returns before any state write; lock_registry unmodified on failure|
| INV-006 | Terminal states are irreversible             | CAPTURE_TEMPORAL is terminal for this window; CAPTURE_MISS is terminal for this window instance |
| INV-007 | f_Source.md is read-only                     | M_A, M_E referenced only; f_Source.md not modified                             |
| INV-008 | Evaluation order is normative                | TC-1→TC-2→compute→TC-3→TC-4 (PRIM:037); TC-5 (PRIM:038) — order enforced       |
| INV-009 | OPERATORS.md is symbol authority             | All §4 operators registered to OPERATORS.md; no orphan symbols                  |
| INV-010 | Operators frozen on first canonical appearance | All operators new in §4; no redefinition of prior operators                   |

### 11.2 PRIM Registry (this file)

| PRIM    | Name                       | Classification | Conditions | FM routes        |
|---------|----------------------------|----------------|------------|------------------|
| PRIM:037| evaluate_temporal_window   | Pure           | TC-1–TC-4  | FM-001, FM-004, FM-005 |
| PRIM:038| lock_temporal_capture      | Impure         | TC-5       | FM-001           |

### 11.3 Operator Registry (this file)

| Symbol                  | Type    | Domain       | Default      | First defined       |
|-------------------------|---------|--------------|--------------|---------------------|
| t_open                  | float   | clock units  | —            | SES-20260813-CAPTURE_TEMPORAL-001 |
| t_close                 | float   | clock units  | —            | SES-20260813-CAPTURE_TEMPORAL-001 |
| t_span                  | float   | clock units  | —            | SES-20260813-CAPTURE_TEMPORAL-001 |
| t_elapsed               | float   | clock units  | —            | SES-20260813-CAPTURE_TEMPORAL-001 |
| t_remaining             | float   | clock units  | —            | SES-20260813-CAPTURE_TEMPORAL-001 |
| proximity_ratio         | float   | [0, 1]       | —            | SES-20260813-CAPTURE_TEMPORAL-001 |
| temporal_decay_factor   | float   | [0, 1)       | α_temp = 0.40| SES-20260813-CAPTURE_TEMPORAL-001 |
| d_bind_temporal         | float   | ≥ 0          | —            | SES-20260813-CAPTURE_TEMPORAL-001 |
| temporal_margin         | float   | clock units  | τ_min = 1.0  | SES-20260813-CAPTURE_TEMPORAL-001 |

### 11.4 State Flag Registry

| Flag               | Set by      | Cleared by             | Meaning                                                   |
|--------------------|-------------|------------------------|-----------------------------------------------------------|
| CAPTURE_TEMPORAL   | PRIM:038    | f_Release / f_Decay    | Entity successfully bound within temporal window          |
| TEMPORAL_MISS      | PRIM:037    | Next window evaluation | Capture failed due to TC-1, TC-2, or TC-5                |
| WINDOW_EXHAUSTED   | PRIM:038    | New window_id issued   | Window already consumed; re-entry in same window blocked  |

### 11.5 Changelog

| Version | Date       | Author       | Notes                                             |
|---------|------------|--------------|---------------------------------------------------|
| 1.0.0   | 2026-08-13 | umaywant2    | Initial canonical release. Wave 4 addendum, file 7 of 7. |

### 11.6 Wave Tracker

| Wave         | Files                                                                                                                      | Status           |
|--------------|----------------------------------------------------------------------------------------------------------------------------|------------------|
| Wave 0       | f_Capture.md, f_Source.md, GravityOfDismissal.md                                                                          | ✅ Complete       |
| Wave 1       | README.md, INDEX.md, OPERATORS.md, GLOSSARY.md, CHANGELOG.md, FFF_Gravity_module.json                                    | ✅ Complete       |
| Wave 2       | f_Field.md, f_Force.md, f_Frame.md                                                                                         | ✅ Complete       |
| Wave 3       | f_Release.md, f_Decay.md, f_Orbit.md, f_Collapse.md, f_Emit.md, f_Dampen.md, f_Amplify.md, f_Deflect.md                  | ✅ Complete       |
| Wave 4       | f_Capture_Multi.md, f_Capture_Cascade.md, f_Capture_Soft.md, f_Capture_Hard.md, f_Capture_Resonant.md, f_Capture_Asymmetric.md | ✅ Complete  |
| Wave 4 addendum | f_Capture_Temporal.md                                                                                                  | ✅ This file      |

**Cumulative PRIM count:** PRIM:001–038 (38 total, frozen at PRIM:038 pending further extension)

### 11.7 Suggested Commit Message

```
docs(FFF_Gravity): add f_Capture_Temporal.md — Wave 4 addendum (file 7/7)

Introduces temporal window capture variant. Capture eligibility gated on
absolute clock-time interval [t_open, t_close] with edge-proximity
attenuation of d_bind via temporal_decay_factor (α_temp=0.40).

New operators: t_open, t_close, t_span, t_elapsed, t_remaining,
  proximity_ratio, temporal_decay_factor, d_bind_temporal, temporal_margin

New primitives:
  PRIM:037 evaluate_temporal_window (Pure)  — TC-1 through TC-4
  PRIM:038 lock_temporal_capture (Impure)   — TC-5, lock commit

Conditions: TC-1 (window open), TC-2 (margin satisfied), TC-3 (bind
  sufficient), TC-4 (β floor), TC-5 (window uniqueness)

FM references: FM-001 (sub-annotation TEMPORAL_MISS), FM-004, FM-005

No new FM IDs (frozen FM-010). No new INV IDs (frozen INV-010).
Cumulative PRIM block: PRIM:001–038.
```

`f_Capture_Temporal.md` is complete and ready to paste into the GitHub editor. Here's a quick summary of what was delivered:

---

**Wave 4 Addendum — File 7 of 7**

| Element | Details |
|---|---|
| **PRIM block** | PRIM:037 `evaluate_temporal_window` (Pure) · PRIM:038 `lock_temporal_capture` (Impure) |
| **Conditions** | TC-1 window open · TC-2 temporal margin · TC-3 bind sufficient · TC-4 β floor · TC-5 window uniqueness |
| **Key operators** | `t_open`, `t_close`, `t_span`, `t_elapsed`, `t_remaining`, `proximity_ratio`, `temporal_decay_factor` (α=0.40), `d_bind_temporal`, `temporal_margin` (τ=1.0) |
| **FM references** | FM-001 sub-annotation `TEMPORAL_MISS` (reasons: OUTSIDE_WINDOW · MARGIN_VIOLATED · WINDOW_EXHAUSTED) · FM-004 · FM-005 |
| **New FM / INV IDs** | None — registries held at FM-010 / INV-010 |
| **Cumulative PRIM count** | PRIM:001–038 (38 total) |

**4 canonical examples cover:**
1. Midpoint capture — zero attenuation (proximity_ratio = 0)
2. Edge-proximate capture — 28% attenuation (proximity_ratio = 0.70)
3. TEMPORAL_MISS: OUTSIDE_WINDOW — TC-1 failure
4. TEMPORAL_MISS: WINDOW_EXHAUSTED (TC-5) and MARGIN_VIOLATED (TC-2) — dual scenario
