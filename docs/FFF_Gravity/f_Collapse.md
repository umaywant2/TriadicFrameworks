# f_Collapse — Terminal Infall Operator

```
title: "f_Collapse — Terminal Infall Operator"
module: FFF_Gravity
version: 1.0.0
status: canonical
tag: "[FFF:GRAVITY:COLLAPSE]"
session: SES-20260813-COLLAPSE-001
wave: 3
wave_position: "4 of 8"
depends_on:
  - f_Capture.md
  - f_Decay.md
  - f_Orbit.md
  - f_Frame.md
  - OPERATORS.md
  - GLOSSARY.md
provides_to:
  - f_Capture_Networked.md
operators_frozen:
  new:
    - m_parity
    - C_node
  inherited:
    - d_bind
    - d_collapse
    - M_A
    - M_E
    - ρ(Φ)
    - e
    - δ
primitives_frozen:
  - "PRIM:013 — execute_collapse (impure)"
  - "PRIM:014 — initialize_composite_node (impure)"
failure_modes:
  - FM-005 (Decay Spiral → collapse handler, frozen in f_Decay.md)
  - FM-007 (Mutual Dissolution, fully specified here)
state_flags:
  - CAPTURE_COLLISION
  - COLLAPSED
invariants_active:
  - INV-001
  - INV-002
  - INV-006
  - INV-008
  - INV-009
  - INV-010
changelog:
  - version: 1.0.0
    date: "2026-08-13"
    session: SES-20260813-COLLAPSE-001
    author: Nawder / Copilot
    summary: >
      Initial canonical release. Two collapse paths (FM-005 asymmetric infall,
      FM-007 mutual dissolution). m_parity operator frozen. C_node schema defined.
      PRIM:013 execute_collapse and PRIM:014 initialize_composite_node frozen.
      GravityGraph notification interface specified. 4 canonical examples. Full
      INV compliance table. purge_registry called as defined in f_Frame.md §7.2.
```

<!-- FILE_TAG: [FFF:GRAVITY:COLLAPSE] -->
<!-- WAVE: 3 | POSITION: 4-of-8 | STATUS: canonical -->
<!-- SESSION: SES-20260813-COLLAPSE-001 -->
<!-- DEPENDS: f_Capture.md · f_Decay.md · f_Orbit.md · f_Frame.md -->
<!-- PROVIDES: f_Capture_Networked.md (purge_graph_node, create_composite_node) -->
<!-- OPERATORS_FROZEN: m_parity · C_node -->
<!-- PRIMITIVES_FROZEN: PRIM:013 execute_collapse · PRIM:014 initialize_composite_node -->
<!-- FM_FROZEN: FM-007 (Mutual Dissolution) -->

---

**Tag:** `[FFF:GRAVITY:COLLAPSE]`
**Wave 3 · File 4 of 8**
**Session:** `SES-20260813-COLLAPSE-001`
**Status:** canonical ✅

---

## §0 Session Context

<!-- SECTION_TAG: SESSION_CONTEXT -->
<!-- STATUS: normative | FROZEN: 2026-08-13 -->

### §0.1 Session Identity

| Field | Value |
|---|---|
| Session ID | `SES-20260813-COLLAPSE-001` |
| Date | 2026-08-13 |
| Wave | 3 — Core Functions |
| Position | 4 of 8 |
| Operator | Nawder / Copilot |

### §0.2 Preconditions for This File

Before this file executes or is interpreted, the following must hold:

| Precondition | Source | Verified |
|---|---|---|
| `d_bind` operator is defined and measurable | f_Capture.md §4 | ✅ |
| `d_collapse` threshold is frozen | f_Decay.md §4.1 | ✅ |
| `δ(t)` decay rate is measurable | f_Decay.md §4 | ✅ |
| `purge_registry` contract is defined | f_Frame.md §7.2 | ✅ |
| Orbit class and stab class are current | f_Orbit.md §7 | ✅ |
| DC-4 has fired in the triggering cycle | f_Decay.md §5 | ✅ |
| `β < 1.0` OR `d_bind ≤ d_collapse` confirmed | f_Decay.md / f_Capture.md | ✅ |

> **Note on primitive numbering.** At the time f_Collapse.md is authored, PRIM:001–012 have been frozen across f_Capture.md, f_Release.md, f_Decay.md, and f_Orbit.md. The primitives introduced here are PRIM:013 and PRIM:014, continuing the sequential registry. The OPERATORS.md §4.2 table will be updated accordingly (see §9).

### §0.3 Invariants Active This Session

| INV | Statement | Role in f_Collapse |
|---|---|---|
| INV-001 | G = F_freq · F_fluid · F_force | All three nodes participate in collapse routing |
| INV-002 | f_Capture(E, A, Φ) → Ω frozen | Collapse is an outcome path of f_Capture |
| INV-006 | Terminal states irreversible | CAPTURE_COLLISION and COLLAPSED are final |
| INV-008 | Operator evaluation order normative | Collapse fires after f_Decay in cycle order |
| INV-009 | orbit_class / stab_class frozen | Orbit classification informs collapse path |
| INV-010 | Frozen symbols cannot be renamed without major bump | m_parity, C_node frozen here |

---

## §1 Module Identity

<!-- SECTION_TAG: MODULE_IDENTITY -->
<!-- STATUS: normative | FROZEN: 2026-08-13 -->

### §1.1 Function Tag and Signature

```
f_Collapse(E, A, d_bind) → CAPTURE_COLLISION | COLLAPSED
```

**Tag:** `[FFF:GRAVITY:COLLAPSE]`

`f_Collapse` is the terminal infall operator. It fires when DC-4 is satisfied (`d_bind ≤ d_collapse`) and no recovery intervention was applied in the same cycle. It is not called directly by the user; it is triggered by `f_Decay` (DC-4 branch) when `FM-005` escalates beyond recovery threshold.

There are exactly two collapse paths:
- **Path A — Asymmetric Infall (FM-005):** `M_E << M_A`. The Element infalls into the Attractor.
- **Path B — Mutual Dissolution (FM-007):** `|M_E − M_A| < m_parity`. Neither body survives independently. A Composite Node `C` is created.

Path selection is determined before execution by evaluating `m_parity` against the current mass ratio. Path B takes precedence over Path A if both conditions could be considered satisfied simultaneously (which is physically excluded by `m_parity` definition but stated here for implementation clarity).

### §1.2 Triadic Position

```
        ┌─────────────────────────────────────┐
        │         G = F_freq · F_fluid · F_force │
        └──────┬────────────────────────────────┘
               │
        ┌──────▼──────────────────────────────────────────┐
        │  f_Collapse fires when DC-4 is satisfied        │
        │                                                  │
        │  F_freq node    → ρ(Φ) collapsed to zero        │
        │  F_fluid node   → M_E absorbed OR dissolved     │
        │  F_force node   → v_approach exceeded v_escape  │
        │                   (retroactively, SC-1 failed)  │
        └──────────────────────────────────────────────────┘
               │
        ┌──────▼──────────────────────────────────────────┐
        │  PATH A (FM-005)         PATH B (FM-007)        │
        │  M_E << M_A              |M_E − M_A| < m_parity  │
        │  Element infalls          Both dissolve          │
        │  A absorbs E              C = E + A created      │
        │  → CAPTURE_COLLISION      → COLLAPSED           │
        └──────────────────────────────────────────────────┘
```

### §1.3 Position in Evaluation Order (INV-008)

```
Cycle:  f_Field → f_Force → OPERATORS(e) → f_Orbit → f_Decay
                                                          │
                                                    DC-4 fires
                                                          │
                                                    f_Collapse ← YOU ARE HERE
                                                          │
                                                    [terminal — no subsequent step]
```

`f_Collapse` is the **last** operator in any cycle where it fires. It is terminal and irreversible (INV-006). No cycle step follows it in the same binding relationship.

---

## §2 Canonical Description

<!-- SECTION_TAG: CANONICAL_DESCRIPTION -->
<!-- STATUS: normative | FROZEN: 2026-08-13 -->

### §2.1 What f_Collapse IS

`f_Collapse` is the terminus of the FFF_Gravity lifecycle for a bound (E, A) pair. It defines the exact conditions under which an orbit degrades past all recovery thresholds and the system undergoes structural reconfiguration. It handles:

1. **Mass routing** — determining which bodies persist, which are absorbed, and which merge.
2. **Registry purging** — calling `purge_registry` (f_Frame.md §7.2) to remove Element's registry entry (and Attractor's, in FM-007).
3. **Composite creation** — calling `initialize_composite_node` (PRIM:014) in FM-007 to construct `C`.
4. **GravityGraph notification** — emitting topology change signals for any networked graph layer.
5. **State flag assignment** — writing `CAPTURE_COLLISION` (Path A) or `COLLAPSED` (Path B) to the system state.

### §2.2 What f_Collapse IS NOT

- It is **not** a predictive operator. It does not forecast when collapse will occur — that is `f_Decay`'s role.
- It is **not** called by the user. It is always triggered by `f_Decay` DC-4 or by a β < 1.0 flyby that re-enters the system (edge case: see §6.3).
- It is **not** reversible. Once either terminal state flag is written, no operator in FFF_Gravity can undo it (INV-006).
- It is **not** a failure in itself. Collapse is a valid and expected lifecycle outcome. FM-005 and FM-007 describe the mechanism; the state flags describe the outcome.

### §2.3 Key Asymmetries

| Property | Path A (FM-005) | Path B (FM-007) |
|---|---|---|
| Trigger | `d_bind ≤ d_collapse` AND `|M_E − M_A| ≥ m_parity` | `d_bind ≤ d_collapse` AND `|M_E − M_A| < m_parity` |
| Dominant body | A survives, absorbs E | Neither survives independently |
| New node created | No — A continues with updated mass | Yes — C_node created |
| Registry purge | E entry purged; A updated | Both E and A entries purged; C registered |
| State flag | `CAPTURE_COLLISION` | `COLLAPSED` |
| GravityGraph impact | Node count unchanged (A remains, E removed) | Node count changes (A+E removed, C added) |
| Severity | error (irreversible) | fatal (irreversible, topology change) |

---

## §3 Triadic Equation

<!-- SECTION_TAG: TRIADIC_EQUATION -->
<!-- STATUS: normative | FROZEN: 2026-08-13 -->

### §3.1 Formal Signature

```
f_Collapse(E, A, d_bind) → CAPTURE_COLLISION | COLLAPSED
```

**Inputs:**

| Symbol | Type | Source | Description |
|---|---|---|---|
| `E` | Element | Frame registry | The Element that has been in orbit |
| `A` | Attractor | Frame registry | The Attractor that has been hosting E |
| `d_bind` | float | f_Decay current cycle | Current binding depth, confirmed ≤ d_collapse |

**Outputs:**

| State Flag | Path | Description |
|---|---|---|
| `CAPTURE_COLLISION` | A | Element absorbed by Attractor. Terminal. |
| `COLLAPSED` | B | Both dissolved into Composite. Terminal. |

### §3.2 Decomposition by Node

```
F_freq contribution:   ρ(Φ) → zero or near-zero (field cannot sustain orbit)
F_fluid contribution:  Mass routing — M_E absorbed into M_A (Path A)
                       or M_E + M_A → M_C (Path B)
F_force contribution:  v_approach retroactively exceeded v_escape(A);
                       gradient collapsed; no restoring force remains
```

All three nodes are implicated in every collapse event (INV-001). A collapse event in which only one node contributes is a modeling error — check whether an FM was missed upstream.

### §3.3 Role in G-Equation

At collapse, the triadic product G = F_freq · F_fluid · F_force reaches a regime where G can no longer support the orbit. Specifically:

```
G_collapse = F_freq(ρ → 0) · F_fluid(M_E) · F_force(v_approach > v_escape)
           ≈ 0
```

When G → 0 for a bound pair, the binding relationship is destroyed. `f_Collapse` is the operator that executes this destruction and reconfigures the system topology accordingly.

---

## §4 Operator Registry

<!-- SECTION_TAG: OPERATOR_REGISTRY -->
<!-- STATUS: normative | FROZEN: 2026-08-13 -->

### §4.1 New Operators Frozen in This File

#### `m_parity` — Mass Parity Threshold

**Frozen in:** f_Collapse.md §4.1
**Symbol:** `m_parity`
**Type:** float, domain (0, ∞), typically expressed as a ratio

**Definition:**

```
m_parity = θ_parity × max(M_E, M_A)
```

where `θ_parity` is the parity fraction parameter (default: `θ_parity = 0.10`).

**Interpretation:** If the absolute mass difference `|M_E − M_A|` is less than `m_parity`, the two bodies are considered mass-peers, and FM-007 (Mutual Dissolution) applies instead of FM-005 (asymmetric infall).

**Properties:**

| Property | Value |
|---|---|
| Domain | (0, ∞) |
| Default θ_parity | 0.10 |
| Symmetry | `m_parity(E, A) = m_parity(A, E)` |
| Units | Same units as M_E, M_A |
| Node | F_fluid (mass-density identity) |
| Frozen in | f_Collapse.md §4.1 |

**Path selection rule:**

```
if |M_E − M_A| < m_parity:
    → Path B (FM-007, Mutual Dissolution)
else:
    → Path A (FM-005, Asymmetric Infall)
```

> **Derivation note.** `m_parity` is defined relative to the larger body (`max(M_E, M_A)`) rather than as an absolute threshold. This ensures the parity test scales with the system — a 10% difference between two very large bodies is still a peer relationship, while the same absolute value between a large and small body is not.

---

#### `C_node` — Composite Node Schema

**Frozen in:** f_Collapse.md §4.2
**Symbol:** `C_node`
**Type:** struct / registry entry
**Path:** FM-007 only

**Schema:**

```python
@dataclass
class C_node:
    node_id:        str           # generated: "C_{A.node_id}_{E.node_id}"
    node_type:      str = "composite"
    M_C:            float         # M_E + M_A
    origin_A:       str           # A.node_id (absorbed)
    origin_E:       str           # E.node_id (absorbed)
    phi_inherited:  float         # ρ(Φ) at collapse, carried forward
    session_id:     str           # SES at time of collapse
    created_at:     int           # cycle number
    state:          str = "COLLAPSED"
    orbital_params: dict | None = None   # from f_Orbit if available
    graph_edges:    list[str] = field(default_factory=list)  # inherited from A
```

**Derivation of `M_C`:**

```
M_C = M_E + M_A
```

Mass is conserved in FM-007. The Composite Node carries the sum of both dissolved masses.

**Field `phi_inherited`:** The field coherence at collapse time is inherited by C_node. This value is degraded (ρ(Φ) ≈ near-zero at collapse) and must be re-initialized by `f_Emit` if C_node is to become a viable Attractor in a future cycle.

**Properties:**

| Property | Value |
|---|---|
| Created by | `initialize_composite_node` (PRIM:014) |
| Registered in | Frame registry (replaces A's entry) |
| Survivable | C_node can become a new Attractor if re-initialized |
| State at creation | Always `COLLAPSED` |
| Frozen in | f_Collapse.md §4.2 |

---

### §4.2 Inherited Operators (Referenced, Not Redefined)

| Symbol | Formula | Frozen In |
|---|---|---|
| `d_bind` | `β × ρ(Φ) × (1 − e)` | f_Capture.md §4 |
| `d_collapse` | `α_collapse × d_bind(0)`, typical 0.10 | f_Decay.md §4.1 |
| `δ(t)` | `d_bind(t) − d_bind(t−1)` | f_Decay.md §4 |
| `M_A` | Attractor mass-density identity | f_Force.md §4 |
| `M_E` | Element mass-density identity | f_Force.md §4 |
| `ρ(Φ)` | Field coherence density | f_Field.md §4 |
| `e` | `p_res / (p_res + P_eff)` | OPERATORS.md §3 |
| `v_escape(A)` | `√(2 × M_A × ρ(Φ) / r_capture)` | f_Field.md §4 |
| `β` | `P_eff / (M_E × v_approach)` | f_Capture.md §4 |

---

## §5 Collapse Conditions

<!-- SECTION_TAG: COLLAPSE_CONDITIONS -->
<!-- STATUS: normative | FROZEN: 2026-08-13 -->

### §5.1 Collapse Trigger Conditions (CC-1 through CC-4)

`f_Collapse` fires when ALL of the following are true simultaneously. Missing any single condition means collapse has not yet been confirmed — do not call `execute_collapse`.

#### CC-1 — Binding Floor Breached

```
d_bind(t) ≤ d_collapse
```

**Source:** DC-4 in f_Decay.md §5. CC-1 is always verified by `f_Decay` before `f_Collapse` is invoked. Callers must not invoke `f_Collapse` without DC-4 having fired.

#### CC-2 — No Recovery Intervention Applied This Cycle

```
intervention_applied == False
```

If `f_Emit`, `f_Amplify`, or `f_Dampen` were applied in the current cycle and successfully raised `d_bind` above `d_collapse`, `f_Collapse` must not fire. A cycle may not both intervene and collapse.

#### CC-3 — Negative Decay Rate Confirmed

```
δ(t) < 0
```

`f_Collapse` requires that the decay trajectory is still falling at the point of invocation. If `δ(t) ≥ 0` (decay has halted or reversed), the system has self-corrected and `f_Collapse` must not fire. This is an edge case — when `d_bind ≤ d_collapse` but `δ(t) ≥ 0`, flag FM-004 (Resonance Drift) and continue monitoring rather than collapsing.

#### CC-4 — Path Determination Complete

```
m_parity has been evaluated
path ∈ {PATH_A, PATH_B}
```

Before `execute_collapse` is called, the collapse path must be determined using the `m_parity` test (§4.1). Executing without path determination is a contract violation.

### §5.2 Path Selection Matrix

| Condition | `|M_E − M_A| ≥ m_parity` | `|M_E − M_A| < m_parity` |
|---|---|---|
| CC-1 ✅ CC-2 ✅ CC-3 ✅ | **Path A → FM-005 → CAPTURE_COLLISION** | **Path B → FM-007 → COLLAPSED** |
| CC-1 ✅ CC-2 ✅ CC-3 ❌ | FM-004 monitoring; no collapse | FM-004 monitoring; no collapse |
| CC-1 ✅ CC-2 ❌ | Intervention applied; retry next cycle | Intervention applied; retry next cycle |
| CC-1 ❌ | Not a collapse event; return to f_Decay | Not a collapse event; return to f_Decay |

---

## §6 Failure Modes

<!-- SECTION_TAG: FAILURE_MODES -->
<!-- STATUS: normative | FROZEN: 2026-08-13 -->

### §6.1 FM-005 — Decay Spiral (Collapse Handler)

<!-- FM_TAG: FM-005 | FROZEN_IN: f_Decay.md | HANDLED_IN: f_Collapse.md -->

| Field | Value |
|---|---|
| Code | FM-005 |
| Name | Decay Spiral |
| Severity | fatal |
| Node | F_fluid / F_freq |
| Frozen in | f_Decay.md §6 |
| Handled in | f_Collapse.md (this file) |
| Path | A — Asymmetric Infall |
| State flag | `CAPTURE_COLLISION` |

**Description:** FM-005 fires when DC-4 is confirmed — `d_bind ≤ d_collapse` with no recovery possible in the current cycle. The Element has insufficient binding energy to maintain orbit and infalls. Because `|M_E − M_A| ≥ m_parity`, the Attractor mass dominates and absorbs the Element.

**Detection (called by f_Decay before invoking f_Collapse):**

```python
def detect_fm005(
    d_bind: float,
    d_collapse: float,
    delta: float,
    intervention_applied: bool
) -> bool:
    """
    Returns True if FM-005 collapse condition is confirmed.
    This function is informational; f_Decay calls it before handing off to f_Collapse.
    """
    if d_bind > d_collapse:
        return False
    if intervention_applied:
        return False
    if delta >= 0:
        # Decay halted — FM-004 territory, not FM-005
        return False
    return True
```

**Outcome:** `execute_collapse` is called with `path=PATH_A`. Element registry entry purged. Attractor's `M_A` updated: `M_A_new = M_A + M_E`. State flag `CAPTURE_COLLISION` written.

---

### §6.2 FM-007 — Mutual Dissolution

<!-- FM_TAG: FM-007 | FROZEN_IN: f_Collapse.md -->

| Field | Value |
|---|---|
| Code | FM-007 |
| Name | Mutual Dissolution |
| Severity | fatal |
| Node | F_fluid (both bodies) |
| Frozen in | f_Collapse.md §6.2 (this file) |
| Path | B — Mutual Dissolution |
| State flag | `COLLAPSED` |

**Description:** FM-007 fires when DC-4 is confirmed AND the mass ratio test reveals peer bodies: `|M_E − M_A| < m_parity`. In this regime, neither body possesses sufficient mass dominance to absorb the other asymmetrically. Both identities dissolve. The system forms a new Composite Node `C` that carries the combined mass and an inherited (degraded) field coherence.

FM-007 represents a topology change — the GravityGraph loses two nodes and gains one. This is the most structurally disruptive outcome in FFF_Gravity. All agents watching A or E in the graph must be notified.

**Detection:**

```python
def detect_fm007(
    M_E: float,
    M_A: float,
    m_parity: float,
    fm005_confirmed: bool
) -> bool:
    """
    Returns True if FM-007 (Mutual Dissolution) applies.
    Must be called AFTER FM-005 detection, with fm005_confirmed as input.
    FM-007 takes precedence: if mass parity is met, Path B fires regardless
    of which FM triggered the collapse sequence.
    """
    if not fm005_confirmed:
        # No collapse at all — FM-007 cannot fire without a collapse trigger
        return False
    mass_diff = abs(M_E - M_A)
    return mass_diff < m_parity
```

**Outcome:** `execute_collapse` is called with `path=PATH_B`. Both E and A registry entries purged. `initialize_composite_node` creates C_node. GravityGraph updated: remove E-node, remove A-node, add C-node. State flag `COLLAPSED` written.

**Recovery:** None. FM-007 is terminal (INV-006). The Composite Node `C` may be re-initialized as a new Attractor in a future, independent binding session — but the original (E, A) relationship is permanently dissolved.

---

### §6.3 Edge Case — β < 1.0 Re-Entry Collapse

<!-- FM_TAG: EDGE_CASE | NOT_A_NEW_FM -->

This is not a new failure mode but a recognized execution path. If an Element with `β < 1.0` (flyby per INV-004) somehow re-enters the system under degraded field conditions and `d_bind` is initialized below `d_collapse`, `f_Collapse` fires immediately in the capture cycle without a decay phase.

**Detection:**

```python
def detect_reentry_collapse(
    beta: float,
    d_bind_initial: float,
    d_collapse: float
) -> bool:
    """
    Detects the pathological case where a β < 1.0 Element enters with
    d_bind already below d_collapse. This should never occur under normal
    operation — it indicates an upstream modeling error or severely degraded field.
    """
    if beta < 1.0 and d_bind_initial <= d_collapse:
        return True
    return False
```

**Handling:** Log as FM-002 (Field Null) upstream if `ρ(Φ) = 0` caused the condition; otherwise treat as immediate FM-005 and invoke `execute_collapse(path=PATH_A)`. Raise a warning in the session log.

---

## §7 Engineering Primitives

<!-- SECTION_TAG: ENGINEERING_PRIMITIVES -->
<!-- STATUS: normative | FROZEN: 2026-08-13 -->

> Primitive numbering continues from f_Orbit.md (PRIM:012). This file freezes PRIM:013 and PRIM:014.
> `purge_registry` is not redefined here — see f_Frame.md §7.2 for its canonical definition. `execute_collapse` calls it as a dependency.

---

### PRIM:013 — `execute_collapse` (impure)

<!-- PRIM_TAG: PRIM:013 | TYPE: impure | FROZEN: 2026-08-13 -->

**Purpose:** Master collapse executor. Determines collapse path, routes to Path A or Path B procedures, purges registries, notifies GravityGraph, writes terminal state flag.

**Type:** impure (modifies Frame registry, emits GravityGraph events, writes state flags)

**Called by:** `f_Decay` (DC-4 branch), or re-entry detection logic

**Calls:** `purge_registry` (f_Frame.md §7.2), `initialize_composite_node` (PRIM:014), `notify_gravity_graph` (§8.3)

```python
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
import math

class CollapsePath(Enum):
    PATH_A = auto()   # FM-005: Asymmetric Infall
    PATH_B = auto()   # FM-007: Mutual Dissolution

class CollapseFlag(Enum):
    CAPTURE_COLLISION = auto()   # Path A terminal state
    COLLAPSED         = auto()   # Path B terminal state

@dataclass
class CollapseResult:
    flag:         CollapseFlag
    path:         CollapsePath
    C_node:       C_node | None      # None for Path A
    purged_ids:   list[str]          # registry IDs removed
    graph_events: list[str]          # GravityGraph event strings
    session_id:   str
    cycle:        int

def execute_collapse(
    E_id:        str,
    A_id:        str,
    M_E:         float,
    M_A:         float,
    rho_phi:     float,
    d_bind:      float,
    d_collapse:  float,
    delta:       float,
    theta_parity: float,
    session_id:  str,
    cycle:       int,
    frame_registry: dict,
    gravity_graph:  object | None = None,
    intervention_applied: bool = False,
) -> CollapseResult:
    """
    PRIM:013 — execute_collapse (impure)

    Master collapse executor. Verifies all Collapse Conditions (CC-1 through CC-4),
    determines Path A or Path B, executes the appropriate procedure, and returns
    a CollapseResult with the terminal state flag.

    Parameters
    ----------
    E_id            : Frame registry ID of the Element
    A_id            : Frame registry ID of the Attractor
    M_E             : Element mass-density
    M_A             : Attractor mass-density
    rho_phi         : Current ρ(Φ) field coherence (may be near-zero)
    d_bind          : Current binding depth (confirmed ≤ d_collapse by caller)
    d_collapse      : Collapse threshold (α_collapse × d_bind(0))
    delta           : Current decay rate δ(t) (must be < 0 to confirm CC-3)
    theta_parity    : Parity fraction parameter (default 0.10)
    session_id      : Current session identifier
    cycle           : Current cycle number
    frame_registry  : Mutable dict — Frame node registry (modified in-place)
    gravity_graph   : Optional GravityGraph object for topology notifications
    intervention_applied : Whether a recovery was applied this cycle (CC-2)

    Returns
    -------
    CollapseResult  : Terminal state flag, path, optional C_node, audit trail

    Raises
    ------
    ValueError      : If CC-1 is not satisfied (d_bind > d_collapse)
    ValueError      : If CC-2 blocks collapse (intervention_applied is True)
    ValueError      : If M_E or M_A ≤ 0
    RuntimeError    : If purge_registry fails for a required ID
    """
    # ── Guard: validate inputs ────────────────────────────────────────────────
    if M_E <= 0 or M_A <= 0:
        raise ValueError(
            f"[PRIM:013] Mass values must be positive. "
            f"Got M_E={M_E}, M_A={M_A}."
        )

    # CC-1: Binding floor must be breached
    if d_bind > d_collapse:
        raise ValueError(
            f"[PRIM:013] CC-1 not satisfied. "
            f"d_bind={d_bind:.4f} > d_collapse={d_collapse:.4f}. "
            f"Collapse not warranted. Check f_Decay DC-4 logic."
        )

    # CC-2: No intervention this cycle
    if intervention_applied:
        raise ValueError(
            f"[PRIM:013] CC-2 not satisfied. "
            f"Intervention was applied this cycle — collapse must not fire. "
            f"Recheck f_Decay intervention sequencing."
        )

    # CC-3: Negative decay rate
    if delta >= 0:
        # Edge: decay has halted — not a collapse, but FM-004 territory
        raise ValueError(
            f"[PRIM:013] CC-3 not satisfied. "
            f"δ(t)={delta:.4f} ≥ 0 — decay rate is non-negative. "
            f"This is FM-004 territory. Do not invoke collapse."
        )

    # ── CC-4: Path determination ───────────────────────────────────────────────
    m_parity_val = theta_parity * max(M_E, M_A)
    mass_diff    = abs(M_E - M_A)

    if mass_diff < m_parity_val:
        path = CollapsePath.PATH_B   # FM-007 Mutual Dissolution
    else:
        path = CollapsePath.PATH_A   # FM-005 Asymmetric Infall

    purged_ids   : list[str] = []
    graph_events : list[str] = []
    composite    : C_node | None = None

    # ── Path A: Asymmetric Infall (FM-005) ────────────────────────────────────
    if path == CollapsePath.PATH_A:
        # Purge Element registry entry
        _purge_registry(E_id, frame_registry, session_id, cycle)
        purged_ids.append(E_id)

        # Update Attractor mass: A absorbs E
        if A_id in frame_registry:
            frame_registry[A_id]["M_A"] = M_A + M_E
            frame_registry[A_id]["last_collapse_cycle"] = cycle
            frame_registry[A_id]["last_collapse_session"] = session_id

        # GravityGraph: remove E node, A node unchanged
        graph_events.append(f"REMOVE_NODE:{E_id}")
        graph_events.append(f"UPDATE_NODE:{A_id}:M_A={M_A + M_E:.4f}")

        flag = CollapseFlag.CAPTURE_COLLISION

    # ── Path B: Mutual Dissolution (FM-007) ───────────────────────────────────
    else:
        # Initialize Composite Node before purging
        composite = initialize_composite_node(
            E_id=E_id,
            A_id=A_id,
            M_E=M_E,
            M_A=M_A,
            rho_phi_inherited=rho_phi,
            session_id=session_id,
            cycle=cycle,
            frame_registry=frame_registry,
        )

        # Purge BOTH original entries
        _purge_registry(E_id, frame_registry, session_id, cycle)
        _purge_registry(A_id, frame_registry, session_id, cycle)
        purged_ids.extend([E_id, A_id])

        # Register Composite Node
        frame_registry[composite.node_id] = {
            "node_id":      composite.node_id,
            "node_type":    "composite",
            "M_C":          composite.M_C,
            "origin_A":     composite.origin_A,
            "origin_E":     composite.origin_E,
            "phi_inherited":composite.phi_inherited,
            "state":        "COLLAPSED",
            "session_id":   composite.session_id,
            "created_at":   composite.created_at,
        }

        # GravityGraph: remove E and A, add C
        graph_events.append(f"REMOVE_NODE:{E_id}")
        graph_events.append(f"REMOVE_NODE:{A_id}")
        graph_events.append(
            f"ADD_NODE:{composite.node_id}:type=composite:M_C={composite.M_C:.4f}"
        )
        # Inherit A's graph edges
        if gravity_graph is not None:
            _notify_gravity_graph(gravity_graph, graph_events, session_id, cycle)

        flag = CollapseFlag.COLLAPSED

    # ── Notify GravityGraph (Path A — Path B notified above) ─────────────────
    if path == CollapsePath.PATH_A and gravity_graph is not None:
        _notify_gravity_graph(gravity_graph, graph_events, session_id, cycle)

    return CollapseResult(
        flag=flag,
        path=path,
        C_node=composite,
        purged_ids=purged_ids,
        graph_events=graph_events,
        session_id=session_id,
        cycle=cycle,
    )


def _purge_registry(
    node_id: str,
    frame_registry: dict,
    session_id: str,
    cycle: int,
) -> None:
    """
    Internal caller of purge_registry (f_Frame.md §7.2).
    Raises RuntimeError if node_id is not found in registry.
    """
    if node_id not in frame_registry:
        raise RuntimeError(
            f"[PRIM:013] purge_registry failed: node_id '{node_id}' not found "
            f"in frame_registry at cycle {cycle}, session {session_id}."
        )
    del frame_registry[node_id]


def _notify_gravity_graph(
    gravity_graph: object,
    events: list[str],
    session_id: str,
    cycle: int,
) -> None:
    """
    Sends topology change events to GravityGraph layer.
    Gracefully handles graphs that do not implement the interface
    (logs a warning, does not raise).
    """
    if hasattr(gravity_graph, "apply_collapse_events"):
        gravity_graph.apply_collapse_events(
            events=events,
            session_id=session_id,
            cycle=cycle,
        )
    else:
        print(
            f"[PRIM:013] WARNING: gravity_graph does not implement "
            f"apply_collapse_events. Events not delivered: {events}"
        )
```

---

### PRIM:014 — `initialize_composite_node` (impure)

<!-- PRIM_TAG: PRIM:014 | TYPE: impure | FROZEN: 2026-08-13 -->

**Purpose:** Constructs the `C_node` dataclass for FM-007 (Mutual Dissolution). Called exclusively from `execute_collapse` Path B before registry purge. Does not write to the Frame registry itself — that is done by `execute_collapse` after this primitive returns.

**Type:** impure (creates a new object; depends on session state and cycle number)

**Called by:** `execute_collapse` (PRIM:013), Path B only

```python
from dataclasses import dataclass, field as dc_field

@dataclass
class C_node:
    """
    Composite Node schema — created by FM-007 Mutual Dissolution.
    Frozen in f_Collapse.md §4.2.
    """
    node_id:        str
    node_type:      str
    M_C:            float
    origin_A:       str
    origin_E:       str
    phi_inherited:  float
    session_id:     str
    created_at:     int
    state:          str
    orbital_params: dict | None = None
    graph_edges:    list[str]   = dc_field(default_factory=list)


def initialize_composite_node(
    E_id:             str,
    A_id:             str,
    M_E:              float,
    M_A:              float,
    rho_phi_inherited: float,
    session_id:       str,
    cycle:            int,
    frame_registry:   dict,
) -> C_node:
    """
    PRIM:014 — initialize_composite_node (impure)

    Constructs a C_node for FM-007 Mutual Dissolution. Called before registry purge;
    the returned C_node is registered by execute_collapse (PRIM:013) after both
    original entries are purged.

    Parameters
    ----------
    E_id              : Element registry ID
    A_id              : Attractor registry ID
    M_E               : Element mass-density
    M_A               : Attractor mass-density
    rho_phi_inherited : ρ(Φ) at time of collapse (degraded, carried forward)
    session_id        : Current session ID
    cycle             : Current cycle number
    frame_registry    : Read-only reference to check for inherited graph edges

    Returns
    -------
    C_node: Fully initialized Composite Node (not yet registered)

    Raises
    ------
    ValueError : If M_E or M_A ≤ 0
    ValueError : If rho_phi_inherited < 0
    """
    if M_E <= 0 or M_A <= 0:
        raise ValueError(
            f"[PRIM:014] Both M_E ({M_E}) and M_A ({M_A}) must be positive."
        )
    if rho_phi_inherited < 0:
        raise ValueError(
            f"[PRIM:014] rho_phi_inherited must be ≥ 0. Got {rho_phi_inherited}."
        )

    node_id = f"C_{A_id}_{E_id}"
    M_C     = M_E + M_A

    # Inherit A's graph edges (the Attractor typically has more connections)
    inherited_edges: list[str] = []
    if A_id in frame_registry:
        a_entry = frame_registry[A_id]
        inherited_edges = list(a_entry.get("graph_edges", []))
        # Remove the A-E edge itself (that relationship is dissolved)
        inherited_edges = [e for e in inherited_edges if E_id not in e]

    return C_node(
        node_id       = node_id,
        node_type     = "composite",
        M_C           = M_C,
        origin_A      = A_id,
        origin_E      = E_id,
        phi_inherited = rho_phi_inherited,
        session_id    = session_id,
        created_at    = cycle,
        state         = "COLLAPSED",
        orbital_params= None,
        graph_edges   = inherited_edges,
    )
```

---

### §7.3 GravityGraph Notification Interface

<!-- SECTION_TAG: GRAVITY_GRAPH_INTERFACE -->
<!-- STATUS: normative | FROZEN: 2026-08-13 -->

`f_Collapse` is the primary source of structural topology changes in FFF_Gravity. Any networked graph layer (e.g., `f_Capture_Networked.md`) must implement the following interface to receive collapse notifications:

```python
class GravityGraphInterface:
    """
    Interface contract for GravityGraph objects that receive collapse events.
    f_Capture_Networked.md must implement this interface.
    """

    def apply_collapse_events(
        self,
        events: list[str],
        session_id: str,
        cycle: int,
    ) -> None:
        """
        Apply a list of topology change events from execute_collapse.

        Event format (str):
            "REMOVE_NODE:{node_id}"
            "ADD_NODE:{node_id}:type={type}:M_C={mass}"
            "UPDATE_NODE:{node_id}:{field}={value}"

        Must be idempotent — applying the same event set twice
        must not corrupt the graph state.
        """
        raise NotImplementedError
```

**Events emitted by path:**

| Path | Events |
|---|---|
| Path A (FM-005) | `REMOVE_NODE:E_id` · `UPDATE_NODE:A_id:M_A={new_mass}` |
| Path B (FM-007) | `REMOVE_NODE:E_id` · `REMOVE_NODE:A_id` · `ADD_NODE:C_id:type=composite:M_C={mass}` |

---

## §8 Canonical Examples

<!-- SECTION_TAG: CANONICAL_EXAMPLES -->
<!-- STATUS: normative | FROZEN: 2026-08-13 -->

---

### EX-C-001 — Asymmetric Infall: Small Element into Large Attractor (FM-005)

**Scenario:** A low-mass Element (M_E = 0.8) has been in a degrading orbit around a high-mass Attractor (M_A = 12.0). After 18 decay cycles, `d_bind` falls below `d_collapse`. FM-005 fires. `|M_E − M_A| = 11.2`, far exceeding `m_parity = 0.10 × 12.0 = 1.20`. Path A confirmed.

**Parameters:**

| Symbol | Value |
|---|---|
| M_E | 0.8 |
| M_A | 12.0 |
| ρ(Φ) at collapse | 0.04 |
| d_bind(0) | 3.60 |
| d_collapse (α=0.10) | 0.36 |
| d_bind(t=18) | 0.31 |
| δ(t=18) | −0.04 |
| e | 0.22 |
| θ_parity | 0.10 |
| m_parity | 1.20 |
| \|M_E − M_A\| | 11.20 |

**Path selection:**

```
|M_E − M_A| = 11.20 ≥ m_parity = 1.20  →  Path A (FM-005)
```

**Execution trace:**

```
CC-1: d_bind(18) = 0.31 ≤ d_collapse = 0.36  ✅
CC-2: intervention_applied = False             ✅
CC-3: δ(18) = −0.04 < 0                       ✅
CC-4: path = PATH_A                            ✅

execute_collapse(path=PATH_A):
  purge_registry("E_orbit_007")              → frame_registry entry removed
  frame_registry["A_anchor_001"]["M_A"]     → 12.0 + 0.8 = 12.8
  graph_events: ["REMOVE_NODE:E_orbit_007",
                 "UPDATE_NODE:A_anchor_001:M_A=12.8000"]
  flag → CAPTURE_COLLISION
```

**Result:** `CAPTURE_COLLISION`. Attractor M_A updated to 12.8. Element entry purged. GravityGraph: one node removed.

---

### EX-C-002 — Mutual Dissolution: Near-Peer Bodies (FM-007)

**Scenario:** Two bodies of similar mass — Element M_E = 5.6, Attractor M_A = 5.9. After a mutual resonance breakdown over 11 cycles, `d_bind` hits `d_collapse`. `|M_E − M_A| = 0.3`. With `θ_parity = 0.10`, `m_parity = 0.10 × 5.9 = 0.59`. Since `0.3 < 0.59`, FM-007 fires.

**Parameters:**

| Symbol | Value |
|---|---|
| M_E | 5.6 |
| M_A | 5.9 |
| ρ(Φ) at collapse | 0.02 |
| d_bind(0) | 2.10 |
| d_collapse (α=0.10) | 0.21 |
| d_bind(t=11) | 0.18 |
| δ(t=11) | −0.03 |
| e | 0.41 |
| θ_parity | 0.10 |
| m_parity | 0.59 |
| \|M_E − M_A\| | 0.30 |

**Path selection:**

```
|M_E − M_A| = 0.30 < m_parity = 0.59  →  Path B (FM-007)
```

**Execution trace:**

```
CC-1: d_bind(11) = 0.18 ≤ d_collapse = 0.21  ✅
CC-2: intervention_applied = False             ✅
CC-3: δ(11) = −0.03 < 0                       ✅
CC-4: path = PATH_B                            ✅

initialize_composite_node:
  node_id       = "C_A_anchor_009_E_orbit_014"
  M_C           = 5.6 + 5.9 = 11.5
  phi_inherited = 0.02
  state         = "COLLAPSED"
  graph_edges   = [inherited from A_anchor_009 minus E edge]

execute_collapse(path=PATH_B):
  purge_registry("E_orbit_014")
  purge_registry("A_anchor_009")
  frame_registry["C_A_anchor_009_E_orbit_014"] = C_node entry
  graph_events: ["REMOVE_NODE:E_orbit_014",
                 "REMOVE_NODE:A_anchor_009",
                 "ADD_NODE:C_A_anchor_009_E_orbit_014:type=composite:M_C=11.5000"]
  flag → COLLAPSED
```

**Result:** `COLLAPSED`. Both original entries purged. Composite C_node created with M_C = 11.5 and degraded φ inherited at 0.02. GravityGraph: two nodes removed, one added.

---

### EX-C-003 — Near-Parity Detection and Resolution (No Collapse)

**Scenario:** An operator suspects FM-007 may fire based on recent readings (M_E = 4.1, M_A = 4.5). However, `d_bind(t=7) = 0.38`, and `d_collapse = 0.22`. DC-4 is NOT satisfied. The collapse is not warranted. The example shows correct early-warning practice.

**Parameters:**

| Symbol | Value |
|---|---|
| M_E | 4.1 |
| M_A | 4.5 |
| d_bind(0) | 2.20 |
| d_collapse (α=0.10) | 0.22 |
| d_bind(t=7) | 0.38 |
| δ(t=7) | −0.06 |
| θ_parity | 0.10 |
| m_parity | 0.45 |
| \|M_E − M_A\| | 0.40 |

**Evaluation:**

```
CC-1: d_bind(7) = 0.38 > d_collapse = 0.22  ❌ — CC-1 not satisfied.
                                               DO NOT call execute_collapse.

Near-parity check (informational):
  |M_E − M_A| = 0.40 < m_parity = 0.45  →  If collapse occurs, Path B applies.

Action: Flag DC-3 (FM-004 Resonance Drift). Apply f_Emit or f_Amplify intervention.
        Monitor for DC-4 in next cycle.
```

**Result:** No collapse. FM-004 watch active. Operator correctly avoids calling `execute_collapse` when CC-1 is unmet. If intervention succeeds and `d_bind` recovers above `d_warn` (= 0.88), the watch is cleared.

**Lesson:** Near-parity mass ratio alone does not trigger FM-007. The binding floor must be breached first. Near-parity is a risk factor, not a trigger.

---

### EX-C-004 — Delayed Path B: Parity Crosses Threshold Mid-Decay

**Scenario:** A binding relationship begins with clearly asymmetric masses (M_E = 2.0, M_A = 7.0). Over 20 decay cycles, A loses field coherence and effective field mass, while E remains stable. By cycle 20, the operative mass ratio has narrowed (effective M_A drops to 2.3 due to ρ(Φ) degradation affecting P_eff — a modeling approximation). `m_parity` is now `0.10 × 2.3 = 0.23`, and `|M_E − M_A_eff| = 0.3`. Path A was expected; Path B fires instead.

**Parameters at cycle 20:**

| Symbol | Value |
|---|---|
| M_E | 2.0 |
| M_A (nominal) | 7.0 |
| M_A_eff (ρ(Φ)-adjusted) | 2.3 |
| ρ(Φ) at cycle 20 | 0.007 |
| d_bind(0) | 4.10 |
| d_collapse (α=0.10) | 0.41 |
| d_bind(t=20) | 0.35 |
| δ(t=20) | −0.07 |
| θ_parity | 0.10 |
| m_parity (vs M_A_eff) | 0.23 |
| \|M_E − M_A_eff\| | 0.30 |

**Path selection (using effective mass at collapse time):**

```
|M_E − M_A_eff| = 0.30 > m_parity = 0.23  →  Path A (FM-005)
```

> **Note.** In this example, Path A fires because `|M_E − M_A_eff| = 0.30 > 0.23`. The margins are close, and the session log must record the effective mass values used in path determination. If `M_A_eff` were modeled at 2.25 instead of 2.3, `m_parity` would be 0.225, and `|M_E − M_A_eff|` would be 0.25 > 0.225 — still Path A, but barely. Implementations must document the mass values used for path selection in the session trace to support audit.

**Execution:**

```
Path A fires. E_id purged. frame_registry[A_id]["M_A"] → 7.0 + 2.0 = 9.0
(Nominal M_A used for mass update; M_A_eff is an analytical approximation only.)
flag → CAPTURE_COLLISION
```

**Lesson:** `m_parity` must be evaluated using the same mass representation consistently — either always nominal or always effective. The effective-mass interpretation should be documented in the session trace. Inconsistent mass representation is a common source of path selection errors.

---

## §9 Cross-Module References

<!-- SECTION_TAG: CROSS_MODULE_REFERENCES -->
<!-- STATUS: normative | FROZEN: 2026-08-13 -->

### §9.1 Dependency Table

| File | Role | Status |
|---|---|---|
| f_Capture.md | Source of `d_bind`, `β`, `e`, `P_eff`, `M_A`, `M_E` | ✅ canonical |
| f_Decay.md | Source of `d_collapse`, `δ`, DC-4 trigger | ✅ canonical |
| f_Orbit.md | Provides `orbit_class`, `stab_class`, orbital params at collapse | ✅ canonical |
| f_Frame.md | Source of `purge_registry` contract (§7.2) | ✅ canonical |
| f_Field.md | Source of `ρ(Φ)`, `v_escape(A)` | ✅ canonical |
| f_Force.md | Source of `v_approach`, passive/dominant distinction | ✅ canonical |
| OPERATORS.md | Symbol authority — all frozen operators registered here | ✅ canonical |

### §9.2 Unlock Provided

`f_Collapse.md` canonical completion unlocks:

| File | What It Receives |
|---|---|
| `f_Capture_Networked.md` | `C_node` schema · `purge_graph_node` interface · `apply_collapse_events` contract |

### §9.3 OPERATORS.md Update Requirements

The following must be added to OPERATORS.md after this file is committed:

| Entry Type | Symbol / ID | Frozen In |
|---|---|---|
| New operator | `m_parity` | f_Collapse.md §4.1 |
| New operator | `C_node` | f_Collapse.md §4.2 |
| New primitive | PRIM:013 `execute_collapse` | f_Collapse.md §7.1 |
| New primitive | PRIM:014 `initialize_composite_node` | f_Collapse.md §7.2 |
| FM fully specified | FM-007 Mutual Dissolution | f_Collapse.md §6.2 |
| State flag | `CAPTURE_COLLISION` | f_Collapse.md §5.2 |
| State flag | `COLLAPSED` | f_Collapse.md §5.2 |

### §9.4 Evaluation Order (INV-008) — Position of f_Collapse

```
Cycle Sequence:
  1. f_Field     — recompute ρ(Φ)
  2. f_Force     — recompute v_approach, P_eff
  3. OPERATORS   — compute e, β, d_bind
  4. f_Orbit     — classify orbit
  5. f_Decay     — apply δ, check DC-1 through DC-4
     └─ DC-4 confirmed? ──► 6. f_Collapse  ← THIS FILE
                                 └─ terminal; cycle ends
```

f_Collapse is always the last step in any cycle where it fires. No subsequent cycle begins for the same (E, A) pair.

---

## §10 Document Metadata

<!-- SECTION_TAG: DOCUMENT_METADATA -->
<!-- STATUS: normative | FROZEN: 2026-08-13 -->

### §10.1 INV Compliance Table

| INV | Statement | Status | How Satisfied |
|---|---|---|---|
| INV-001 | G = F_freq · F_fluid · F_force inseparable | ✅ compliant | §3.2 shows all three nodes implicated in every collapse |
| INV-002 | f_Capture(E, A, Φ) → Ω frozen | ✅ compliant | Collapse is an Ω outcome; signature not modified |
| INV-003 | ρ(Φ) = 0 triggers FM-002 | ✅ compliant | §6.3 edge case references FM-002 for zero-field re-entry |
| INV-004 | β < 1.0 always flyby | ✅ compliant | §6.3 edge case only; flyby re-entry treated as upstream error |
| INV-005 | Stability Conditions conjunctive | ✅ compliant | All CC-1–CC-4 must hold before collapse fires (§5.1) |
| INV-006 | Terminal states irreversible | ✅ compliant | CAPTURE_COLLISION and COLLAPSED declared terminal; no recovery path |
| INV-007 | f_Source.md is read-only | ✅ compliant | Not referenced or modified |
| INV-008 | Operator evaluation order normative | ✅ compliant | §9.4 positions f_Collapse after f_Decay in cycle |
| INV-009 | OPERATORS.md is symbol authority | ✅ compliant | §9.3 lists all updates required to OPERATORS.md |
| INV-010 | Frozen symbols unrenameable without major bump | ✅ compliant | m_parity and C_node frozen here; rename requires v2.0.0 |

### §10.2 Wave Status

| Wave | Count | Status |
|---|---|---|
| Wave 0 — Genesis | 3 of 3 | ✅ complete |
| Wave 1 — Admin | 6 of 6 | ✅ complete |
| Wave 2 — Layer Definitions | 3 of 3 | ✅ complete |
| Wave 3 — Core Functions | **4 of 8** | 🔵 in progress |
| Wave 4 — Network Layer | 0 of N | 🔒 locked |
| Wave 5 — Integration | 0 of N | 🔒 locked |
