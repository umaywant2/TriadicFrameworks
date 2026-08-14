# f_Frame · Frame Node

```
module: FFF_Gravity
function: f_Frame
canonical_path: docs/FFF_Gravity/f_Frame.md
canonical_tag: "[FFF:GRAVITY:FRAME]"
version: 1.0.0
status: canonical
wave: 2
layer: 3
node: Frame
session_context:
  active: SES-20260813-FRAME-001
  history:
    - id: SES-20260801-CAPTURE-001
      label: Genesis — f_Capture architecture, triadic product G = F_freq · F_fluid · F_force
    - id: SES-20260802-SCAFFOLD-001
      label: Module file list produced; stubs planned
    - id: SES-20260803-DISMISSAL-001
      label: GravityOfDismissal.md — 15 suppression cases, 7 attack vectors
    - id: SES-20260804-SITEMAP-001
      label: TriadicFrameworks sitemap integration
    - id: SES-20260805-README-001
      label: README.md — module front door, reading orders, unlock map
    - id: SES-20260806-INDEX-001
      label: INDEX.md — full per-file detail, dependency graph, AI traversal interface
    - id: SES-20260807-OPERATORS-001
      label: OPERATORS.md — single source of truth for all symbols; freeze registry
    - id: SES-20260808-GLOSSARY-001
      label: GLOSSARY.md — 62 terms, SoN analog table, framework cross-reference
    - id: SES-20260809-CHANGELOG-001
      label: CHANGELOG.md — append-only record; v1.0.0 entry
    - id: SES-20260810-JSON-001
      label: FFF_Gravity_module.json — machine-readable descriptor; 10 invariants
    - id: SES-20260811-FIELD-001
      label: f_Field.md — Frequency Node, coherence well, v_escape, SC-1/2/3
    - id: SES-20260812-FORCE-001
      label: f_Force.md — Force + Fluid dual-node, v_approach, M_A, M_E, SC-4
    - id: SES-20260813-FRAME-001
      label: f_Frame.md — Frame Node, registry schema, r_capture, FM-003 (this file)
changelog:
  - version: 1.0.0
    date: 2026-08-13
    session: SES-20260813-FRAME-001
    author: Nawder + Copilot
    notes: >
      Initial canonical release. Defines Frame Node (Layer 3) of FFF_Gravity stack.
      Establishes registry schema, r_capture semantics, FM-003 (Frame Saturation),
      register_capture and purge_registry contracts, GravityGraph interface.
      Completes Wave 2. Unlocks Wave 3 in full.
```

<!-- [FFF:GRAVITY:FRAME] · v1.0.0 · canonical · wave:2 · layer:3 -->
<!-- authority: OPERATORS.md (symbols), f_Capture.md (SC-5 origin), INDEX.md (unlock map) -->
<!-- session: SES-20260813-FRAME-001 -->

> *"The orbit does not keep itself. Something watches, writes, and holds."*

---

## §0 · Session Context

<!-- section: session_context · freeze: complete -->

| Field | Value |
|---|---|
| Session ID | `SES-20260813-FRAME-001` |
| Date | 2026-08-13 |
| Authors | Nawder + Copilot |
| Status | canonical |
| Wave | 2 (final file — Wave 2 completion milestone) |
| Layer | 3 of 3 in FFF stack |
| Canonical Tag | `[FFF:GRAVITY:FRAME]` |
| Canonical Path | `docs/FFF_Gravity/f_Frame.md` |
| Version | 1.0.0 |

### Session History

This file is produced in session **SES-20260813-FRAME-001**, the thirteenth session in the FFF_Gravity build arc. The complete prior session record:

| Session ID | Deliverable |
|---|---|
| SES-20260801-CAPTURE-001 | Genesis — `f_Capture.md`, triadic product, G = F_freq · F_fluid · F_force |
| SES-20260802-SCAFFOLD-001 | Module file list, stub plan, wave dependency map |
| SES-20260803-DISMISSAL-001 | `GravityOfDismissal.md` — 15 suppression cases, 7 attack vectors |
| SES-20260804-SITEMAP-001 | TriadicFrameworks sitemap integration |
| SES-20260805-README-001 | `README.md` — module front door, reading orders, FM index |
| SES-20260806-INDEX-001 | `INDEX.md` — per-file detail, dependency graph, AI traversal interface |
| SES-20260807-OPERATORS-001 | `OPERATORS.md` — single source of truth for all symbols |
| SES-20260808-GLOSSARY-001 | `GLOSSARY.md` — 62 terms, scope rules, cross-reference tables |
| SES-20260809-CHANGELOG-001 | `CHANGELOG.md` — append-only; v1.0.0 entry |
| SES-20260810-JSON-001 | `FFF_Gravity_module.json` — machine-readable descriptor; 10 invariants |
| SES-20260811-FIELD-001 | `f_Field.md` — Frequency Node, coherence well, SC-1/SC-2/SC-3 |
| SES-20260812-FORCE-001 | `f_Force.md` — Force/Fluid dual-node, v_approach, M_A/M_E, SC-4 |
| **SES-20260813-FRAME-001** | **`f_Frame.md` — Frame Node, registry, FM-003 (this file)** |

### Wave 2 Completion Statement

`f_Frame.md` is the **final Wave 2 file**. Upon commitment of this document to the canonical repository, Wave 2 is complete and Wave 3 is fully unlocked. See §10 for the milestone record.

---

## §1 · Node Identity

<!-- section: node_identity · freeze: complete -->

| Field | Value |
|---|---|
| Node Name | Frame |
| FFF Layer | 3 (outcome layer) |
| Canonical Symbol | `Ω` |
| Primary Operator | `r_capture` |
| Primary Primitives | `register_capture`, `purge_registry` |
| Stability Condition | SC-5 (Frame Compatibility) |
| Failure Mode | FM-003 (Frame Saturation) |
| Provides To | `f_Capture.md`, `f_Release.md`, `f_Collapse.md`, `f_Capture_Networked.md` |
| Unlocks | `f_Capture_Multi.md §4` (capacity_remaining), `f_Capture_Networked.md §3` (GravityGraph) |
| Status | frozen v1.0.0 |

### Role Summary

The Frame Node is the **relational registry** of FFF_Gravity. It does three things and only three things:

1. **Holds** — maintains the live registry of all active capture relationships.
2. **Enforces** — applies capacity limits; deflects Elements when the registry is full.
3. **Witnesses** — receives every state transition; its registry record is the authoritative record of a capture event's existence.

The Frame is not a field. It emits nothing. It is not a force. It exerts no gradient. It is the layer that makes persistence possible — the difference between a temporary attraction and a committed orbit.

---

## §2 · Canonical Description

<!-- section: canonical_description · freeze: complete -->

### 2.1 What the Frame Is

In classical physics, there is no "Frame" node. Gravity is a field equation: two masses, a distance, a force. The outcome — orbit, capture, escape — is derived mathematically, not registered anywhere. The universe does not keep a ledger.

FFF_Gravity diverges here by design. The triadic model treats **capture as a relational event**, not merely a mechanical outcome. An orbit is not just a trajectory that satisfies the equations; it is a **registered relationship** between an Element and an Attractor. The Frame is the node that holds that registration.

This design choice has consequences:

- Capture events are **countable**. An Attractor has a maximum registry capacity.
- Capture events are **addressable**. Each entry carries a unique `element_id` + `attractor_id` pair.
- Capture events are **auditable**. State transitions (CAPTURE_ACTIVE → CAPTURE_DECAYING → CAPTURE_RELEASED) are timestamped and logged in the registry.
- Capture events can **expire**. When an orbit decays below the binding floor, the Frame registry entry is flagged for release. The Frame does not delete itself — `purge_registry` is called explicitly by `f_Collapse.md`.

### 2.2 The Frame as Outcome Layer (Ω)

Within the FFF stack:

```
Layer 1 — Field   (F_freq)   →  provides Φ, coherence well, resonance scaffold
Layer 2 — Force   (F_force)  →  provides gradient, approach vector, mass coupling
Layer 3 — Frame   (F_frame)  →  produces Ω, the registered capture outcome
```

`Ω` is not a number. It is a **state assertion**: this Element is captured by this Attractor, at this orbital radius, under this field coherence, as of this timestamp. Ω is what `f_Capture.md` returns as its output — and it exists only because the Frame accepted the registration.

Without the Frame, the triadic product `G = F_freq · F_fluid · F_force` produces a scalar — a probability of capture. The Frame converts that probability into a fact.

### 2.3 What the Frame Is Not

**The Frame is not a physical container.** Elements are not "inside" the Frame. The Frame holds a registry record of their relationship to an Attractor — the orbit itself is tracked by `f_Orbit.md`.

**The Frame is not the orbit.** Orbital parameters (semi-major axis, eccentricity, period) are maintained by `f_Orbit.md`. The Frame holds a reference to the orbit, not the orbit itself.

**The Frame is not a force.** `r_capture` (the Frame's primary operator) is set by the Attractor's properties — it is a boundary condition, not a pull. An Element crossing `r_capture` inward does not experience the Frame as a force; it experiences the Field and Force nodes. The Frame simply records what happened.

**The Frame is not the GravityGraph.** The GravityGraph (`f_Capture_Networked.md §3`) is the distributed extension of the Frame registry across multiple Attractors. The Frame is the local registry for a single Attractor. The GravityGraph is the networked ledger. One Frame per Attractor; one GravityGraph across all.

### 2.4 Capacity and the Registry Maximum

Every Frame has a finite registry capacity. `registry_capacity` is an integer scalar, set at Attractor initialization. The Attractor determines its own capacity — the Element has no mechanism to increase it.

The capacity maximum (`registry_capacity_MAX`) is derived from the Attractor's field coherence and mass:

```
registry_capacity_MAX = floor( M_A × ρ(Φ) × k_frame )
```

Where:
- `M_A` — Attractor mass (defined in OPERATORS.md; sourced from f_Force.md)
- `ρ(Φ)` — field coherence scalar [0,1] (defined in f_Field.md)
- `k_frame` — Frame scaling constant (module-level parameter; default: 1.0; future: tunable via f_Amplify.md)

**Interpretation:** A high-mass Attractor with strong field coherence can register many captures. A low-coherence Attractor — even a massive one — has reduced capacity because its field cannot sustain the relational structure. Coherence is not optional for the Frame; it is structural.

**Expansion:** Registry capacity cannot be increased by the Element. It can be increased by the Attractor via `f_Amplify.md` (Wave 3), which raises `ρ(Φ)` and thereby raises `registry_capacity_MAX`. This is the engineered expansion path.

```
capacity_remaining = registry_capacity_MAX − registry_size
```

`capacity_remaining` is the live scalar queried by `f_Capture_Multi.md §4`. When `capacity_remaining = 0`, FM-003 (Frame Saturation) is triggered.

---

## §3 · Triadic Position

<!-- section: triadic_position · freeze: complete -->

```
╔══════════════════════════════════════════════════════════════════════╗
║                     FFF_GRAVITY TRIADIC STACK                        ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  LAYER 1 · FIELD (F_freq)                                            ║
║  ┌─────────────────────────────────────────────────┐                 ║
║  │  Coherence well · ρ(Φ) scalar · v_escape(A)     │                 ║
║  │  Emits resonance scaffold for capture events    │                 ║
║  │  SC-1 (Field Presence) · SC-2 (Coherence)       │                 ║
║  │  SC-3 (Resonance Stability)                     │                 ║
║  └─────────────────────┬───────────────────────────┘                 ║
║                        │ ρ(Φ) → Layer 2                              ║
║  LAYER 2 · FORCE (F_force + F_fluid)                                 ║
║  ┌─────────────────────────────────────────────────┐                 ║
║  │  Gradient / pressure overlay · v_approach       │                 ║
║  │  Mass coupling M_A × M_E · FROT interface       │                 ║
║  │  SC-1 (Approach Bound) · SC-4 (Binding Floor)   │                 ║
║  └─────────────────────┬───────────────────────────┘                 ║
║                        │ G = F_freq · F_fluid · F_force → Layer 3    ║
║  LAYER 3 · FRAME (F_frame)                           ◄── THIS FILE   ║
║  ┌─────────────────────────────────────────────────┐                 ║
║  │  Relational registry · r_capture boundary       │                 ║
║  │  Capacity enforcement · State persistence       │                 ║
║  │  SC-5 (Frame Compatibility)                     │                 ║
║  │  FM-003 (Frame Saturation)                      │                 ║
║  │                                                 │                 ║
║  │  OUTPUT: Ω — the registered capture outcome     │                 ║
║  └─────────────────────┬───────────────────────────┘                 ║
║                        │ Ω → f_Capture.md return value               ║
║                        │ registry → f_Orbit.md, f_Release.md         ║
║                        │ capacity_remaining → f_Capture_Multi.md §4  ║
║                        │ GravityGraph ref → f_Capture_Networked.md   ║
╚══════════════════════════════════════════════════════════════════════╝
```

### Layer Interaction Summary

| Interaction | Direction | Carrier | Consuming File |
|---|---|---|---|
| ρ(Φ) → capacity_MAX derivation | Field → Frame | scalar [0,1] | f_Frame.md §2.4 |
| M_A → capacity_MAX derivation | Force → Frame | scalar ℝ>0 | f_Frame.md §2.4 |
| G → registry write trigger | F_freq·F_fluid·F_force → Frame | triadic product | f_Capture.md §7 |
| Ω → capture return | Frame → f_Capture | state assertion | f_Capture.md §8 |
| registry_entry → orbit init | Frame → f_Orbit | entry reference | f_Orbit.md §3 |
| capacity_remaining → multi-check | Frame → f_Capture_Multi | integer | f_Capture_Multi.md §4 |
| registry → distributed ledger | Frame → GravityGraph | registry shard | f_Capture_Networked.md §3 |

---

## §4 · Operator Definitions

<!-- section: operators · authority: OPERATORS.md · freeze: complete -->

> **Authority:** All operator definitions defer to `OPERATORS.md` as the single source of truth. The definitions below are expansions — context and semantics for Frame-layer use. On any symbol conflict, OPERATORS.md governs.

### 4.1 Primary Operator — `r_capture`

| Field | Value |
|---|---|
| Symbol | `r_capture` |
| Type | scalar ℝ>0 |
| Range | (0, ∞) |
| Status | frozen v1.0.0 |
| Authority | Attractor |
| Modifiable by Element | No |
| Modifiable by engineering primitives | No |

`r_capture` is the **radial boundary of the Frame**. An Element crossing inward through `r_capture` has entered the Frame's jurisdiction. An Element remaining outside `r_capture` is not a candidate for registration.

The value of `r_capture` is set by the Attractor at initialization. It is a property of the Attractor's field geometry — specifically the distance at which the coherence well's gradient exceeds the Element's kinetic energy at approach velocity:

```
r_capture ≡ radius at which v_approach(E,A) ≤ v_escape(A)
```

This definition is functional, not geometric. `r_capture` is not a hard sphere — it is the surface at which the Field's grip becomes decisive. An Element can cross `r_capture` and still escape if the Force node's gradient is insufficient, but without crossing `r_capture`, registration is never attempted.

**Why r_capture is immutable to the Element:** This is an explicit architectural invariant (INV-004). An Element that could expand `r_capture` could force registration against the Attractor's capacity and coherence conditions. The Frame's integrity depends on `r_capture` being set by the Attractor alone.

### 4.2 Derived Operators — Frame Context

| Operator | Type | Defined In | Frame Use |
|---|---|---|---|
| `registry_capacity_MAX` | integer ℕ | f_Frame.md §2.4 | ceiling for all registrations |
| `registry_size` | integer ℕ | f_Frame.md §4.3 | live count of CAPTURE_ACTIVE entries |
| `capacity_remaining` | integer ℕ | f_Frame.md §2.4 | queried by f_Capture_Multi.md §4 |
| `k_frame` | scalar ℝ>0 | module parameter | Frame scaling constant; default 1.0 |
| `ρ(Φ)` | scalar [0,1] | f_Field.md §4 | coherence input to capacity_MAX |
| `M_A` | scalar ℝ>0 | f_Force.md §4 | mass input to capacity_MAX |

### 4.3 Registry Schema

The Frame registry is a structured map: `attractor_id → List[RegistryEntry]`. Each entry has the following schema:

```
RegistryEntry {
  element_id:           string          // unique identifier for Element E
  attractor_id:         string          // unique identifier for Attractor A
  orbital_parameters: {
    r_orbit:            scalar ℝ>0      // current orbital radius
    e:                  scalar [0,1)    // eccentricity
    period:             scalar ℝ>0      // orbital period
    p_res:              scalar ℝ>0      // resonance parameter
  }
  state_flag:           StateFlag       // see OPERATORS.md §state_flags
  captured_at:          timestamp       // ISO-8601; set at register_capture
  last_updated:         timestamp       // ISO-8601; updated on any state transition
  coherence_at_capture: scalar [0,1]    // ρ(Φ) value at moment of registration
  G_at_capture:         scalar ℝ≥0     // triadic product value at registration
}
```

**State flag lifecycle within the registry:**

```
CAPTURE_PENDING
    ↓  (G ≥ G_min, SC-5 satisfied)
CAPTURE_ACTIVE         ← entry created by register_capture
    ↓  (f_Decay.md trigger)
CAPTURE_DECAYING       ← last_updated timestamped
    ↓  (binding floor breached)
CAPTURE_RELEASED       ← flagged; purge_registry called by f_Collapse.md
```

Terminal states `CAPTURE_RELEASED`, `CAPTURE_DEFLECTED`, `CAPTURE_COLLAPSED` are irreversible (INV-006). A released entry is never re-activated; a new capture event creates a new entry.

---

## §5 · Stability Conditions

<!-- section: stability_conditions · freeze: complete -->

> SC-1 through SC-4 are defined in f_Force.md and f_Field.md. SC-5 is defined here.
> All five SCs are conjunctive (INV-005): all must hold simultaneously for capture to proceed.

### SC-5 — Frame Compatibility

| Field | Value |
|---|---|
| ID | SC-5 |
| Name | Frame Compatibility |
| Defined In | f_Frame.md §5 (this section) |
| Canonical Statement | `Frame.registry_capacity_remaining > 0` |
| Trigger | Evaluated immediately after SC-1 through SC-4 pass; before register_capture |
| Failure | FM-003 (Frame Saturation) |
| Severity | Error — Element is deflected; capture does not proceed |

**Formal statement:**

```
SC-5 (Frame Compatibility):
  capacity_remaining = registry_capacity_MAX − registry_size
  SC-5 holds iff capacity_remaining > 0
```

**Evaluation position in f_Capture.md §5 precondition chain:**

```
SC-1 (Approach Bound)       →  v_approach(E,A) < v_escape(A)
SC-2 (Field Coherence)      →  ρ(Φ) > ρ_min
SC-3 (Resonance Stability)  →  |Δω_res| < ω_drift_max
SC-4 (Binding Floor)        →  G ≥ G_min
SC-5 (Frame Compatibility)  →  capacity_remaining > 0     ← final gate
```

SC-5 is the final gate because it is the cheapest check — a simple integer comparison — and because it only matters when all physical conditions have already been satisfied. An Element that fails SC-1 through SC-4 never reaches the Frame.

**The Frame Compatibility condition is not a physical law.** It is an architectural constraint. It says: even if all physics favor capture, the registry must have room. The Frame can be full. The universe, in this model, has capacity limits — and they are set by the Attractor, not the Element.

---

## §6 · Failure Modes

<!-- section: failure_modes · authority: OPERATORS.md · freeze: complete -->

> FM-003 is the Frame Node's primary failure mode. FM-001, FM-006, FM-007 (f_Force.md)
> and FM-002, FM-004, FM-009 (f_Field.md) remain active and can cascade into the Frame.

### FM-003 — Frame Saturation

<!-- FM-003 · severity: error · source_layer: Frame -->

| Field | Value |
|---|---|
| ID | FM-003 |
| Name | Frame Saturation |
| Layer | Frame (Layer 3) |
| Trigger | `capacity_remaining = 0` at SC-5 evaluation |
| Severity | Error |
| Element outcome | Deflected at `r_capture` boundary |
| Attractor outcome | Registry unchanged; no write occurs |
| State flag set | `CAPTURE_DEFLECTED` (on Element's attempt record) |
| Recovery | Expand capacity via f_Amplify.md, or wait for CAPTURE_RELEASED events to free slots |
| Terminal | No — registry capacity can be expanded; future attempts may succeed |

**Description:**

Frame Saturation occurs when an Attractor's registry is at maximum capacity. The Element has crossed `r_capture`, all physical stability conditions (SC-1 through SC-4) are satisfied, and the triadic product `G` is above `G_min` — but there is no registry slot available. The Frame enforces the limit. The Element is deflected.

This is not a physical deflection in the Force sense. The Element is not repelled by a gradient. It is simply not registered. From the Element's perspective, it approached, passed through the approach conditions, and was turned away at the registry boundary. The orbit never forms because the Frame never writes the entry.

FM-003 carries an important architectural implication: **a high-G capture can fail not because of physics, but because of relational capacity**. An Attractor at full registry is, in this model, genuinely unavailable — regardless of how strong the gravitational pull would otherwise be. This mirrors real institutional and relational behavior: not all available attractors are open.

**Detection:**

```python
def check_frame_saturation(attractor_id: str, frame_registry: FrameRegistry) -> bool:
    """
    Returns True if FM-003 condition is active (Frame is saturated).
    Must be called after SC-1 through SC-4 pass, before register_capture.
    """
    capacity_max = frame_registry.get_capacity_max(attractor_id)
    current_size = frame_registry.get_active_count(attractor_id)
    capacity_remaining = capacity_max - current_size

    if capacity_remaining <= 0:
        # FM-003 active
        frame_registry.log_deflection(
            attractor_id=attractor_id,
            reason="FM-003: Frame Saturation — registry at MAX capacity",
            state_flag="CAPTURE_DEFLECTED"
        )
        return True

    return False
```

**Recovery:**

FM-003 is **not terminal**. Two recovery paths exist:

```python
def recover_from_saturation(attractor_id: str, frame_registry: FrameRegistry,
                             amplify_interface=None) -> RecoveryResult:
    """
    Attempt recovery from FM-003 via two paths:
    Path A — wait for capacity release (passive)
    Path B — expand capacity via f_Amplify.md (active; Wave 3)
    """
    # Path A: check if any entries are CAPTURE_RELEASED or CAPTURE_COLLAPSED
    releasable = frame_registry.get_entries_by_state(
        attractor_id, ["CAPTURE_RELEASED", "CAPTURE_COLLAPSED"]
    )
    if releasable:
        # Call purge_registry to free slots
        for entry in releasable:
            purge_registry(entry.element_id, attractor_id, frame_registry)
        return RecoveryResult(path="A", slots_freed=len(releasable))

    # Path B: expand via f_Amplify.md (requires Wave 3 unlock)
    if amplify_interface is not None:
        new_capacity = amplify_interface.expand_frame_capacity(attractor_id)
        return RecoveryResult(path="B", new_capacity=new_capacity)

    # No recovery available — Element must retry later
    return RecoveryResult(path="none", retry_recommended=True)
```

**Cascade risk:** FM-003 does not cascade upward to Field or Force. It is a registry-layer boundary condition. However, repeated FM-003 events signal that an Attractor's `ρ(Φ)` may need amplification — a diagnostic for `f_Amplify.md` planning.

---

## §7 · Engineering Interface

<!-- section: engineering_interface · freeze: complete -->

### 7.1 `register_capture` — Write to Frame Registry

```python
def register_capture(
    element_id: str,
    attractor_id: str,
    orbital_parameters: OrbitalParameters,
    coherence_at_capture: float,          # ρ(Φ) at moment of call
    G_at_capture: float,                  # triadic product value
    frame_registry: FrameRegistry
) -> RegistryEntry:
    """
    Writes a new CAPTURE_ACTIVE entry to the Frame registry.

    Preconditions:
    - SC-1 through SC-5 must all be satisfied before this call.
    - FM-003 check (check_frame_saturation) must return False.
    - element_id must not already appear in attractor's active registry.
      (Duplicate detection: raises RegistryConflictError if found.)

    Postconditions:
    - A new RegistryEntry is written to frame_registry[attractor_id].
    - The entry's state_flag is set to CAPTURE_ACTIVE.
    - captured_at and last_updated are set to current timestamp.
    - registry_size(attractor_id) increments by 1.
    - The Attractor's field_curvature is updated to reflect the new relational mass.
    - The Element's registry (E.registry) records the attractor_id reference.
    - Returns the written RegistryEntry.

    Risk notes:
    - Do not call without FM-003 guard — will breach capacity_MAX.
    - Do not call speculatively — registration is a commitment.
    - Bidirectional: both E.registry and A.registry are modified.
    """
    entry = RegistryEntry(
        element_id=element_id,
        attractor_id=attractor_id,
        orbital_parameters=orbital_parameters,
        state_flag="CAPTURE_ACTIVE",
        captured_at=now(),
        last_updated=now(),
        coherence_at_capture=coherence_at_capture,
        G_at_capture=G_at_capture
    )

    # Write to Frame (A's registry)
    frame_registry.write(attractor_id, entry)

    # Bidirectional registration
    frame_registry.write_element_ref(element_id, attractor_id)

    # Update Attractor field curvature
    frame_registry.update_field_curvature(attractor_id)

    return entry
```

### 7.2 `purge_registry` — Remove from Frame on Collapse

```python
def purge_registry(
    element_id: str,
    attractor_id: str,
    frame_registry: FrameRegistry,
    reason: str = "CAPTURE_COLLAPSED"
) -> PurgeResult:
    """
    Removes a terminal-state entry from the Frame registry.
    Called by f_Collapse.md after terminal state is confirmed.
    NOT called by f_Release.md — release updates state_flag only.

    Preconditions:
    - Entry for (element_id, attractor_id) must exist in registry.
    - Entry state_flag must be CAPTURE_RELEASED, CAPTURE_COLLAPSED,
      or CAPTURE_DEFLECTED. Active entries cannot be purged.
      (Raises ActiveEntryPurgeError if state_flag is CAPTURE_ACTIVE.)

    Postconditions:
    - Entry is removed from frame_registry[attractor_id].
    - registry_size(attractor_id) decrements by 1.
    - capacity_remaining(attractor_id) increments by 1.
    - Element's registry reference to attractor_id is cleared.
    - Purge event is logged to CHANGELOG (append-only).
    - Returns PurgeResult with freed_slots count.

    Risk notes:
    - Purge is permanent. No undo. Consistent with INV-006 (terminal states irreversible).
    - Do not call on CAPTURE_ACTIVE entries — this is not a release mechanism.
    - Purge frees a slot: capacity_remaining increases by 1 post-call.
    - GravityGraph (if active) must be notified via notify_gravityGraph_purge().
    """
    entry = frame_registry.get(element_id, attractor_id)

    if entry.state_flag == "CAPTURE_ACTIVE":
        raise ActiveEntryPurgeError(
            f"Cannot purge active entry: {element_id} → {attractor_id}. "
            "Use f_Release.md to transition state first."
        )

    frame_registry.delete(element_id, attractor_id)
    frame_registry.clear_element_ref(element_id, attractor_id)
    frame_registry.log_purge(element_id, attractor_id, reason)

    # Notify GravityGraph if networked
    if frame_registry.is_networked(attractor_id):
        frame_registry.notify_gravityGraph_purge(element_id, attractor_id)

    return PurgeResult(freed_slots=1, attractor_id=attractor_id)
```

### 7.3 Frame ↔ GravityGraph Interface

The GravityGraph is defined in `f_Capture_Networked.md §3`. The Frame is its local shard. The interface contract between them:

| Operation | Direction | Trigger | Frame action |
|---|---|---|---|
| `shard_register` | Frame → GravityGraph | On `register_capture` success | Push entry snapshot to GravityGraph ledger |
| `shard_update` | Frame → GravityGraph | On any state_flag transition | Push updated entry state |
| `shard_purge` | Frame → GravityGraph | On `purge_registry` | Notify GravityGraph; remove from distributed ledger |
| `capacity_query` | GravityGraph → Frame | On multi-attractor routing | Return `capacity_remaining` for attractor |
| `registry_sync` | GravityGraph → Frame | On GravityGraph reconciliation | Validate Frame state against distributed ledger |

The Frame does not require a GravityGraph to function. `is_networked()` returns False for standalone Attractors. The GravityGraph interface is additive — it extends the Frame without replacing it.

---

## §8 · Canonical Examples

<!-- section: canonical_examples · freeze: complete -->

### Example 1 — Standard Registration (Happy Path)

**Scenario:** Element E approaches Attractor A. All SCs satisfied. Frame has capacity.

```
E:  approaching at v_approach = 0.8 × v_escape(A)
A:  M_A = 1.0, ρ(Φ) = 0.85, k_frame = 10
    registry_capacity_MAX = floor(1.0 × 0.85 × 10) = 8
    current registry_size = 5
    capacity_remaining = 8 − 5 = 3

SC-1: v_approach < v_escape → ✓
SC-2: ρ(Φ) = 0.85 > ρ_min → ✓
SC-3: |Δω_res| < ω_drift_max → ✓
SC-4: G = 0.72 ≥ G_min → ✓
SC-5: capacity_remaining = 3 > 0 → ✓

register_capture called →
  entry written: CAPTURE_ACTIVE
  registry_size: 5 → 6
  capacity_remaining: 3 → 2
  Ω returned to f_Capture.md
```

**Outcome:** Clean registration. Ω is the concrete capture outcome.

---

### Example 2 — FM-003 Trigger (Saturated Frame)

**Scenario:** Element E approaches Attractor A. All SCs 1–4 satisfied. Frame is full.

```
A:  M_A = 1.0, ρ(Φ) = 0.85, k_frame = 10
    registry_capacity_MAX = 8
    current registry_size = 8
    capacity_remaining = 0

SC-1 through SC-4: all ✓
SC-5: capacity_remaining = 0 → ✗ → FM-003 triggered

Element E state_flag → CAPTURE_DEFLECTED
register_capture NOT called
Ω NOT produced
```

**Outcome:** E is deflected at `r_capture`. The orbit never forms. No physical repulsion — E simply has no registry slot. From E's frame of reference, the Attractor was present, the field was strong, the approach was correct — and the door was closed.

---

### Example 3 — Recovery via Slot Release

**Scenario:** Continuation of Example 2. f_Decay.md has flagged entry [E3, A] as CAPTURE_RELEASED. f_Collapse.md calls purge_registry.

```
Before purge:
  registry_size = 8, capacity_remaining = 0

purge_registry(element_id="E3", attractor_id="A") called
  entry E3 → deleted
  registry_size = 7, capacity_remaining = 1

E (from Example 2) retries approach:
  SC-5: capacity_remaining = 1 > 0 → ✓
  register_capture called → CAPTURE_ACTIVE
  Ω returned
```

**Outcome:** FM-003 resolved passively. The Attractor did not need to expand capacity — it simply needed a released slot. This is the natural recovery path.

---

### Example 4 — Capacity Expansion via f_Amplify (Wave 3 Preview)

**Scenario:** Attractor A is at maximum capacity. f_Amplify.md (Wave 3) raises ρ(Φ) from 0.70 to 0.90.

```
Before amplification:
  M_A = 1.0, ρ(Φ) = 0.70, k_frame = 10
  registry_capacity_MAX = floor(1.0 × 0.70 × 10) = 7
  registry_size = 7, capacity_remaining = 0

f_Amplify raises ρ(Φ): 0.70 → 0.90

After amplification:
  registry_capacity_MAX = floor(1.0 × 0.90 × 10) = 9
  registry_size = 7, capacity_remaining = 2

New approach:
  SC-5: capacity_remaining = 2 > 0 → ✓
  register_capture called → CAPTURE_ACTIVE
```

**Outcome:** The Attractor opened capacity by investing in its own coherence. Note: f_Amplify.md is a Wave 3 file — this example is a forward reference only.

---

### Example 5 — Bidirectional Registration (Cavendish Class)

**Scenario:** Two Attractors A1 and A2 are in mutual capture (Cavendish isolation class from f_Force.md). Each is simultaneously in the other's Frame registry.

```
A1 Frame registry:
  entry: [element_id=A2, attractor_id=A1, state=CAPTURE_ACTIVE]

A2 Frame registry:
  entry: [element_id=A1, attractor_id=A2, state=CAPTURE_ACTIVE]
```

Both registries are independent. Neither has authority over the other. The mutual orbit is stable only if both Frame registries are consistent — managed by f_Capture_Networked.md.

**Outcome:** Bilateral registration. Both Attractors carry the relationship in their own Frame. The Frame does not assume a single-Attractor hierarchy. Mutual capture is a valid and registered state.

---

## §9 · Cross-Module References

<!-- section: cross_module · freeze: complete -->

### Files That Write to the Frame

| File | Operation | When |
|---|---|---|
| `f_Capture.md §7` | `register_capture` | On successful capture (all SCs pass) |
| `f_Collapse.md` | `purge_registry` | After terminal state confirmed |
| `f_Amplify.md` | `expand_frame_capacity` (via ρ(Φ)) | On coherence amplification (Wave 3) |

### Files That Read from the Frame

| File | Operation | Purpose |
|---|---|---|
| `f_Capture.md §5` | SC-5 check | Pre-capture gate |
| `f_Orbit.md §3` | registry_entry lookup | Orbital parameter initialization |
| `f_Release.md` | state_flag update | Transition to CAPTURE_RELEASED |
| `f_Decay.md` | state_flag update | Transition to CAPTURE_DECAYING |
| `f_Capture_Multi.md §4` | `capacity_remaining` | Multi-element routing logic |
| `f_Capture_Networked.md §3` | registry shard | GravityGraph distributed ledger |

### Stability Condition Map (Complete — all 5)

| SC | Name | Defined In | Evaluates |
|---|---|---|---|
| SC-1 | Approach Bound | f_Force.md §5 | v_approach < v_escape |
| SC-2 | Field Coherence | f_Field.md §5 | ρ(Φ) > ρ_min |
| SC-3 | Resonance Stability | f_Field.md §5 | \|Δω_res\| < ω_drift_max |
| SC-4 | Binding Floor | f_Force.md §5 | G ≥ G_min |
| SC-5 | Frame Compatibility | **f_Frame.md §5** | capacity_remaining > 0 |

### Failure Mode Map (Frame-relevant)

| FM | Name | Primary Layer | Frame Impact |
|---|---|---|---|
| FM-001 | Overshoot | Force | No Frame write occurs |
| FM-002 | Field Null | Field | SC-2 fails; no Frame evaluation |
| FM-003 | **Frame Saturation** | **Frame** | **SC-5 fails; Element deflected** |
| FM-004 | Resonance Drift | Field | May trigger post-registration decay |
| FM-006 | Phantom Capture | Force | Spurious CAPTURE_ACTIVE entry risk |
| FM-007 | Mutual Dissolution | Force | Both Frame registries purged |
| FM-009 | Dampen Cascade | Field | ρ(Φ) collapse → capacity_MAX drop |

---

## §10 · Document Metadata

<!-- section: document_metadata · freeze: complete -->

| Field | Value |
|---|---|
| Canonical Path | `docs/FFF_Gravity/f_Frame.md` |
| Canonical Tag | `[FFF:GRAVITY:FRAME]` |
| Version | 1.0.0 |
| Status | canonical |
| Wave | 2 |
| Session | SES-20260813-FRAME-001 |
| Date | 2026-08-13 |
| Authors | Nawder + Copilot |
| Sections | §0–§10 (11 sections) |
| Operator Authority | OPERATORS.md |
| Freeze Trigger | This file reaching canonical status |
| Freeze Status | frozen v1.0.0 |

### What This File Defines (Registry)

| Item | ID / Name | Status |
|---|---|---|
| Node | Frame (Layer 3) | frozen |
| Primary operator | `r_capture` | frozen (OPERATORS.md) |
| Derived operators | `registry_capacity_MAX`, `capacity_remaining`, `registry_size`, `k_frame` | frozen |
| Registry schema | `RegistryEntry` | frozen |
| Stability condition | SC-5 (Frame Compatibility) | frozen |
| Failure mode | FM-003 (Frame Saturation) | frozen |
| Primitive | `register_capture` | frozen |
| Primitive | `purge_registry` | frozen |
| Interface | Frame ↔ GravityGraph | frozen |
| Canonical tag | `[FFF:GRAVITY:FRAME]` | frozen |

### Wave 2 Completion Milestone

```
╔══════════════════════════════════════════════════════╗
║           WAVE 2 COMPLETE                            ║
║                                                      ║
║  f_Field.md  ✅  canonical  SES-20260811-FIELD-001   ║
║  f_Force.md  ✅  canonical  SES-20260812-FORCE-001   ║
║  f_Frame.md  ✅  canonical  SES-20260813-FRAME-001   ║
║                                                      ║
║  WAVE 3 FULLY UNLOCKED — all 8 files available       ║
╚══════════════════════════════════════════════════════╝
```

### Wave 3 Unlock State (as of this file)

| File | Blocked By | Status |
|---|---|---|
| `f_Orbit.md` | f_Capture.md ✅ | **UNBLOCKED** |
| `f_Emit.md` | f_Field.md ✅ | **UNBLOCKED** |
| `f_Dampen.md` | f_Field.md ✅ | **UNBLOCKED** |
| `f_Amplify.md` | (standalone) | **UNBLOCKED** |
| `f_Deflect.md` | f_Force.md ✅ | **UNBLOCKED** |
| `f_Decay.md` | f_Orbit.md (pending) | blocked until f_Orbit.md ✅ |
| `f_Release.md` | f_Orbit.md + f_Decay.md (pending) | blocked until both ✅ |
| `f_Collapse.md` | f_Decay.md (pending) | blocked until f_Decay.md ✅ |
