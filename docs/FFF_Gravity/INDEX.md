---
# ┌─────────────────────────────────────────────────────────────┐
# │                  DOCUMENT FRONTMATTER                       │
# └─────────────────────────────────────────────────────────────┘
document:         INDEX
canonical_path:   docs/FFF_Gravity/INDEX.md
canonical_tag:    "[FFF:GRAVITY:INDEX]"
framework:        TriadicFrameworks
module:           FFF_Gravity
version:          1.0.0
status:           canonical
stability:        living
created:          2026-08-13
last_modified:    2026-08-13
authors:
  - TriadicFrameworks
encoding:         UTF-8
line_endings:     LF
description: >
  Authoritative machine-readable and human-readable registry of every
  file in docs/FFF_Gravity/. Covers status, dependencies, section maps,
  operator counts, unlock sequence, and completion tracking.
  Living document — updated whenever a file is created or promoted to canonical.
tags:
  - FFF
  - gravity
  - index
  - registry
  - dependency-graph
  - completion-tracker

session_context:
  current_session:
    session_id:       SES-20260813-INDEX-001
    opened_at:        2026-08-13T07:36:00-04:00
    closed_at:        ~
    editor:           Nawder
    branch:           main
    intent:           Create canonical INDEX.md — full file registry, dependency graph, section maps, completion tracker
    status:           active
    dirty:            true
    sections_touched: [§0, §1, §2, §3, §4, §5, §6, §7, §8, §9]

  session_history:
    - session_id:  SES-20260813-README-001
      opened_at:   2026-08-13T07:19:00-04:00
      closed_at:   2026-08-13T07:35:00-04:00
      intent:      Create canonical README.md
      status:      closed

changelog:
  - version: 1.0.0
    date:    2026-08-13
    author:  TriadicFrameworks
    notes:   Initial canonical release. 27 files registered. 4 canonical, 22 scaffold, 1 archived.
---

# FFF_Gravity · Index

> **Canonical path:** `docs/FFF_Gravity/INDEX.md`
> **Scope:** All files in `docs/FFF_Gravity/` · Branch: `main`
> **Last updated:** 2026-08-13 · **Session:** `SES-20260813-INDEX-001`

This is the authoritative registry for the FFF_Gravity module.
Every file in the module has a full entry here: path, status, version, section count, operator count, dependencies, and what it provides.
Update this file whenever a new file is created or a scaffold is promoted to canonical.

---

## §0 · Session Context

<!--
  metadata:
    section:       session-context
    section_id:    §0
    type:          live-session-register
    normative:     false
    created_in:    SES-20260813-INDEX-001
  session:
    session_id:    SES-20260813-INDEX-001
    touch_count:   1
    change_type:   created
-->

### Active Session

| Field | Value |
|---|---|
| Session ID | `SES-20260813-INDEX-001` |
| Opened | `2026-08-13T07:36:00-04:00` |
| Closed | — (active) |
| Editor | Nawder |
| Branch | `main` |
| Intent | Create canonical INDEX.md |
| Status | 🟡 Active |

### Session Resolution Protocol

```
1. Set current_session.closed_at       → ISO 8601 timestamp
2. Set current_session.status          → "closed"
3. Move current_session                → session_history[]
4. Update §7 Completion Tracker        → reflect any status changes made this session
5. Update document last_modified       → frontmatter
6. Commit:  "index(SES-YYYYMMDD-NNN): <summary of changes>"
```

---

## §1 · Status Legend and Conventions

<!--
  metadata:
    section:       legend
    section_id:    §1
    type:          reference
    normative:     true
    created_in:    SES-20260813-INDEX-001
  session:
    session_id:    SES-20260813-INDEX-001
    touch_count:   1
    change_type:   created
-->

### File Status

| Symbol | Label | Meaning |
|---|---|---|
| ✅ | canonical | Complete, versioned, normative. All sections filled. Passes internal consistency check. |
| 🔵 | scaffold | Structure and frontmatter in place. Section headers present. Content pending. |
| 📁 | archived | Source or historical record. Non-normative. Not expected to be filled further. |
| ⏳ | planned | Designed in INDEX but file not yet created in the repository. |

### Dependency Notation

| Symbol | Meaning |
|---|---|
| `→` | Provides to (output consumed by) |
| `←` | Depends on (input received from) |
| `↔` | Bidirectional dependency |
| `—` | No dependency in this direction |

### Section Count Convention

Section counts include all numbered sections (§0 onward).
Subsections (§4.1, §4.2 …) count as one entry under their parent.
A scaffold file with headers only counts its planned sections.
A canonical file's count is exact.

---

## §2 · Master File Registry

<!--
  metadata:
    section:       master-registry
    section_id:    §2
    type:          flat-registry
    normative:     true
    stability:     living
    created_in:    SES-20260813-INDEX-001
    sort:          wave ascending, then alphabetical within wave
  session:
    session_id:    SES-20260813-INDEX-001
    touch_count:   1
    change_type:   created
-->

### Wave 0 — Existing Files

| File | Status | Version | Wave | Sections | Operators | Primitives | FMs | Depends On | Provides To |
|---|---|---|---|---|---|---|---|---|---|
| `f_Capture.md` | ✅ canonical | 1.0.0 | 0 | 13 (§0–§12) | 10P · 4D · 11F | 6 | FM-001–007 | f_Field, f_Force, f_Frame, FFF_Resonance | f_Release, f_Decay, f_Orbit, f_Collapse, all variants |
| `f_Source.md` | 📁 archived | — | 0 | — | — | — | — | — | f_Capture (genesis) |
| `GravityOfDismissal.md` | ✅ canonical | 1.0.0 | 0 | 13 (§1–§13) | — | — | — | — | strategic context for all files |

### Wave 1 — Admin Files

| File | Status | Version | Wave | Sections | Depends On | Provides To |
|---|---|---|---|---|---|---|
| `README.md` | ✅ canonical | 1.0.0 | 1 | 9 (§1–§9) | f_Capture (reference) | all files (orientation) |
| `INDEX.md` | ✅ canonical | 1.0.0 | 1 | 9 (§0–§9) | all files (registrar) | all files (navigation) |
| `OPERATORS.md` | 🔵 scaffold | 0.1.0 | 1 | 5 (§1–§5) | f_Capture, f_Decay, f_Release, f_Orbit | all files (symbol authority) |
| `GLOSSARY.md` | 🔵 scaffold | 0.1.0 | 1 | alpha | f_Capture, f_Field | all files (term authority) |
| `CHANGELOG.md` | 🔵 scaffold | 0.1.0 | 1 | 1 per release | — | — |
| `FFF_Gravity_module.json` | 🔵 scaffold | 0.1.0 | 1 | — (JSON) | all files | machine consumers |

### Wave 2 — Layer Definitions

| File | Status | Version | Wave | Node | Sections | Depends On | Provides To |
|---|---|---|---|---|---|---|---|
| `f_Field.md` | 🔵 scaffold | 0.1.0 | 2 | `F_freq` | 10 (§0–§10) | OPERATORS.md | f_Capture, f_Emit, f_Dampen, all variants |
| `f_Force.md` | 🔵 scaffold | 0.1.0 | 2 | `F_force` | 7 (§0–§7) | OPERATORS.md | f_Capture, f_Deflect, f_Capture_Asymmetric |
| `f_Frame.md` | 🔵 scaffold | 0.1.0 | 2 | Frame | 6 (§0–§6) | OPERATORS.md | f_Capture, f_Release, f_Collapse, f_Capture_Networked |

### Wave 3 — Core Functions

| File | Status | Version | Wave | Sections | Depends On | Provides To |
|---|---|---|---|---|---|---|
| `f_Release.md` | 🔵 scaffold | 0.1.0 | 3 | 11 (§0–§10) | f_Capture, f_Orbit, f_Decay | f_Capture_Networked |
| `f_Decay.md` | 🔵 scaffold | 0.1.0 | 3 | 11 (§0–§10) | f_Capture, f_Orbit | f_Collapse, f_Capture_Cascade, f_Capture_Networked |
| `f_Orbit.md` | 🔵 scaffold | 0.1.0 | 3 | 10 (§0–§9) | f_Capture | f_Decay, f_Release, f_Collapse |
| `f_Collapse.md` | 🔵 scaffold | 0.1.0 | 3 | 11 (§0–§11) | f_Capture, f_Decay | f_Capture_Networked |
| `f_Emit.md` | 🔵 scaffold | 0.1.0 | 3 | 10 (§0–§9) | f_Field | f_Decay (restore), f_Capture_Resonant |
| `f_Dampen.md` | 🔵 scaffold | 0.1.0 | 3 | 7 (§0–§7) | f_Field | f_Release (assist), f_Capture_Resonant |
| `f_Amplify.md` | 🔵 scaffold | 0.1.0 | 3 | 7 (§0–§7) | f_Field, f_Capture | f_Decay (restore), f_Capture_Resonant |
| `f_Deflect.md` | 🔵 scaffold | 0.1.0 | 3 | 8 (§0–§8) | f_Force, f_Capture | f_Capture_Resonant, f_Capture_Asymmetric |

### Wave 4 — Capture Variants

| File | Status | Version | Wave | Sections | Extends | New Operators | Depends On |
|---|---|---|---|---|---|---|---|
| `f_Capture_Multi.md` | 🔵 scaffold | 0.1.0 | 4 | 7 (§0–§6) | f_Capture | `N`, `eval_order`, `Φ_perturbed`, `capacity_remaining` | f_Capture, f_Orbit, f_Frame |
| `f_Capture_Cascade.md` | 🔵 scaffold | 0.1.0 | 4 | 6 (§0–§6) | f_Capture | `Δcurvature`, `perturbation_sensitivity`, `cascade_depth` | f_Capture, f_Orbit, f_Decay |
| `f_Capture_Resonant.md` | 🔵 scaffold | 0.1.0 | 4 | 11 (§0–§10) | f_Capture | `ω_res_target`, `approach_parameters`, `solution_space`, `nearest_valid` | f_Capture, f_Deflect, f_Emit, f_Amplify |
| `f_Capture_Asymmetric.md` | 🔵 scaffold | 0.1.0 | 4 | 11 (§0–§10) | f_Capture | `ρ(Φ,θ)`, `θ_approach`, `anisotropy_index`, `θ_optimal`, `θ_critical` | f_Capture, f_Field, f_Force, f_Deflect |
| `f_Capture_Temporal.md` | 🔵 scaffold | 0.1.0 | 4 | 11 (§0–§10) | f_Capture | `C_thresh(t)`, `t_entry`, `t_encounter`, `temporal_capture_window`, `ΔM_A`, `Δρ` | f_Capture, f_Field, f_Decay |
| `f_Capture_Networked.md` | 🔵 scaffold | 0.1.0 | 4 | 12 (§0–§11) | f_Capture | `GravityGraph`, `G_edge`, `G_degree`, `G_stability`, `G_cascade_risk` | f_Capture, f_Frame, f_Decay, f_Release, f_Collapse |

---

## §3 · Per-File Detail Entries

<!--
  metadata:
    section:       per-file-detail
    section_id:    §3
    type:          detail-registry
    normative:     true
    stability:     living
    created_in:    SES-20260813-INDEX-001
    note: >
      One entry per file. Each entry includes: purpose, key operators/concepts,
      current gaps (for scaffolds), and what completing it unlocks.
  session:
    session_id:    SES-20260813-INDEX-001
    touch_count:   1
    change_type:   created
-->

---

### `f_Capture.md` · ✅ canonical · v1.0.0

| Field | Value |
|---|---|
| Tag | `[FFF:GRAVITY:CAPTURE]` |
| Role | Reference implementation — defines when an Element enters stable orbit |
| Triadic Equation | `f_Capture(E, A, Φ) → Ω` |
| Sections | §0 Session Context · §1 Module Identity · §2 Canonical Description · §3 Triadic Equation · §4 Operator Registry (§4.1–§4.8) · §5 Stability Conditions · §6 Failure Modes · §7 Engineering Primitives (§7.1–§7.2) · §8 Canonical Examples · §9 Future Applications · §10 Cross-Module References · §11 Document Metadata · §12 Session Log |
| Operators | 6 primary · 4 derived · 11 state flags |
| Primitives | `compute_approach_vector` · `resolve_escape_velocity` · `evaluate_capture_threshold` · `lock_orbit` · `register_capture` · `flag_decay` |
| Failure Modes | FM-001 Overshoot · FM-002 Field Null · FM-003 Frame Saturation · FM-004 Resonance Drift · FM-005 Decay Spiral · FM-006 Phantom Capture · FM-007 Mutual Dissolution |
| Examples | EX-001 Clean Capture · EX-002 Resonance Drift · EX-003 Frame Saturation · EX-004 Mutual Dissolution |
| Current Gaps | None — canonical |
| Unlocks | All Wave 3 and Wave 4 files |

---

### `README.md` · ✅ canonical · v1.0.0

| Field | Value |
|---|---|
| Role | Module front door — orientation, file registry, reading orders, failure mode index |
| Sections | §1 The Model · §2 Triadic Equation · §3 File Registry · §4 Completion Tracker · §5 Unlock Map · §6 Reading Orders · §7 Key Concepts · §8 Failure Mode Index · §9 Module Metadata |
| Current Gaps | None — canonical |
| Unlocks | Nothing blocked by README; it is informational |

---

### `INDEX.md` · ✅ canonical · v1.0.0

| Field | Value |
|---|---|
| Role | Authoritative file registry — this file |
| Sections | §0 Session Context · §1 Legend · §2 Master Registry · §3 Per-File Detail · §4 Dependency Graph · §5 Unlock Sequence · §6 Section Maps · §7 Completion Tracker · §8 AI Traversal Interface · §9 Document Metadata |
| Current Gaps | None — canonical |
| Unlocks | Nothing blocked by INDEX; it is the registrar |

---

### `OPERATORS.md` · 🔵 scaffold · v0.1.0

| Field | Value |
|---|---|
| Role | Master symbol table — single source of truth for every operator symbol in the module |
| Key Contents | §1 Primary operators (all 9) · §2 Derived operators (all 10) · §3 State flags (all 11) · §4 Engineering primitives registry (all 13) · §5 Failure mode index (all 10) |
| Current Gaps | `T_orb`, `δ`, `E_rel`, `F_emit`, `F_damp` marked 🔵 pending full definition; formulas to fill once `f_Orbit`, `f_Decay`, `f_Release`, `f_Emit`, `f_Dampen` are canonical |
| Unlocks | GLOSSARY.md (term definitions pull from operator names); FFF_Gravity_module.json (symbol list) |

---

### `GLOSSARY.md` · 🔵 scaffold · v0.1.0

| Field | Value |
|---|---|
| Role | Module-scoped term definitions — resolves naming ambiguity within FFF_Gravity |
| Key Contents | 30+ terms A–T; each with formal definition, symbol reference, and source file |
| Current Gaps | All terms present in draft; definitions need review against final operator formulas once Wave 3 canonical |
| Unlocks | Final review of f_Field.md §2 (prose) against GLOSSARY terms |

---

### `CHANGELOG.md` · 🔵 scaffold · v0.1.0

| Field | Value |
|---|---|
| Role | Append-only version history for the module |
| Current Gaps | v1.0.0 entry to be written at first full commit; format established |
| Unlocks | Nothing blocked |

---

### `FFF_Gravity_module.json` · 🔵 scaffold · v0.1.0

| Field | Value |
|---|---|
| Role | Machine-readable module descriptor — dependency graph, file list, function registry |
| Key Contents | triadic_equation, nodes, depends_on, files{}, canonical_functions{}, failure_modes{}, tags, related_docs |
| Current Gaps | `canonical_functions` status fields to update as files promote; file list to grow |
| Unlocks | External tooling; AI auto-traversal; Zenodo metadata sync |

---

### `f_Field.md` · 🔵 scaffold · v0.1.0

| Field | Value |
|---|---|
| Tag | `[FFF:GRAVITY:FIELD]` |
| Node | Frequency (`F_freq`) |
| Role | Defines the gravitational field identity node — coherence well, field density `ρ(Φ)`, resonance |
| Key Contents | §2 Canonical Description (coherence well definition) · §4 Operator definitions for `ρ(Φ)`, `v_escape`, `ω_res` · §7 Engineering interface (emit/dampen) · §8 Examples |
| Current Gaps | §2 prose (primary gap) · `ρ(Φ)` formal derivation · coherence well depth formula · turbulence definition |
| Unlocks | `f_Emit.md §2` · `f_Dampen.md §2` · `f_Capture_Asymmetric.md §3` full definition |

---

### `f_Force.md` · 🔵 scaffold · v0.1.0

| Field | Value |
|---|---|
| Tag | `[FFF:GRAVITY:FORCE]` |
| Node | Force (`F_force`) |
| Role | Defines the gradient/pressure identity node — `v_approach`, atmospheric gradients, overlays |
| Key Contents | §3 Operator definitions for `v_approach`, `force.gradient`, `force.overlay` · §6 Failure modes |
| Current Gaps | §2 prose · force node passive/dominant distinction · overlay concept (FROT interface) · formal `v_approach` derivation |
| Unlocks | `f_Deflect.md §2` · `f_Capture_Asymmetric.md §4.2` heading operators |

---

### `f_Frame.md` · 🔵 scaffold · v0.1.0

| Field | Value |
|---|---|
| Tag | `[FFF:GRAVITY:FRAME]` |
| Role | Defines registry structure, capacity rules, and FM-003 boundary enforcement |
| Key Contents | §3 Registry schema (element_id, attractor_id, orbital_parameters, state_flag) · §4 Capacity rules |
| Current Gaps | §2 prose · capacity derivation formula (what sets MAX?) · expansion via `f_Amplify` interface |
| Unlocks | `f_Capture_Multi.md §4` (capacity_remaining operator) · `f_Capture_Networked.md §3` (GravityGraph as distributed extension) |

---

### `f_Release.md` · 🔵 scaffold · v0.1.0

| Field | Value |
|---|---|
| Tag | `[FFF:GRAVITY:RELEASE]` |
| Role | Inverse of `f_Capture` — defines conditions for clean orbital exit |
| Triadic Equation | `f_Release(E, A, Φ, d_bind) → RELEASED \| FM-008` |
| Key Operators | `v_release`, `E_rel`, `r_release` |
| Key Primitives | `compute_release_vector`, `execute_release` |
| Current Gaps | §2 prose · `v_release` formula · `E_rel` formula · release conditions table · 3 examples |
| Unlocks | `f_Capture_Networked.md §7.1` (`update_edge_state → RELEASED`) · `OPERATORS.md §2` (`E_rel` formula) |

---

### `f_Decay.md` · 🔵 scaffold · v0.1.0

| Field | Value |
|---|---|
| Tag | `[FFF:GRAVITY:DECAY]` |
| Role | Cycle-based orbital energy loss — computes `δ`, raises FM-004/005 at thresholds |
| Triadic Equation | `f_Decay(E, A, Φ, t) → d_bind(t) \| FM-004 \| FM-005` |
| Key Operators | `δ` (decay rate) · `d_collapse` (collapse threshold) · `d_warn` (FM-004 threshold) · `t_decay` |
| Key Primitives | `flag_decay` (✅ already defined in f_Capture §7) · `compute_decay_rate` · `assess_decay_cause` |
| Current Gaps | §2 prose · threshold values for `d_warn` and `d_collapse` · reversal interface spec · 3 examples |
| Unlocks | `f_Collapse.md §5` (collapse condition 1) · `f_Capture_Cascade.md §3` (perturbation trigger) · `OPERATORS.md §2` (`δ` formula) |

---

### `f_Orbit.md` · 🔵 scaffold · v0.1.0

| Field | Value |
|---|---|
| Tag | `[FFF:GRAVITY:ORBIT]` |
| Role | Characterizes the established orbit — shape, period, stability class |
| Triadic Equation | `f_Orbit(E, A, p_res, ω_res) → orbital_parameters` |
| Key Operators | `e` (eccentricity) · `T_orb` (period) · `orbit_class` · `stab_class` |
| Key Primitives | `classify_orbit` · `update_orbital_parameters` |
| Classification Thresholds | circular `e < 0.1` · elliptical `0.1–0.5` · eccentric `0.5–0.9` · resonant (low-integer `ω_res`) |
| Current Gaps | §2 prose · `T_orb` formula · threshold formal values · 4 examples |
| Unlocks | `f_Decay.md §4` (stab_class input) · `f_Release.md §7` (eccentricity for release vector) · `OPERATORS.md §2` (`T_orb`, `e` formulas) |

---

### `f_Collapse.md` · 🔵 scaffold · v0.1.0

| Field | Value |
|---|---|
| Tag | `[FFF:GRAVITY:COLLAPSE]` |
| Role | Terminal infall — fires when `d_bind → 0`; handles FM-005 and FM-007 paths |
| Key Operators | `d_collapse` (threshold) · `m_parity` (dissolution threshold) · `C_node` (composite node) |
| Key Primitives | `execute_collapse` · `initialize_composite_node` · `purge_registry` |
| Two Paths | FM-005 asymmetric (E absorbed into A) · FM-007 dissolution (new composite node C) |
| Current Gaps | §2 prose · `d_collapse` value · `m_parity` formula · composite node schema · 3 examples |
| Unlocks | `f_Capture_Networked.md §7.1` (`purge_graph_node`, `create_composite_node`) |

---

### `f_Emit.md` · 🔵 scaffold · v0.1.0

| Field | Value |
|---|---|
| Tag | `[FFF:GRAVITY:EMIT]` |
| Node | `F_freq` — increases `ρ(Φ)` |
| Role | Engineering primitive — deepens the coherence well; can restore decaying orbits |
| Key Operators | `F_emit` · `ρ(Φ)_delta` · `r_emit` · `E_emit` |
| Key Primitives | `emit_field` · `compute_emit_cost` · `check_emit_ceiling` |
| Failure Risk | FM-010 (Amplify Runaway) if `β → ∞` under sustained emission |
| Current Gaps | §2 prose · `F_emit` formula · energy cost model · emission decay rate over time · examples |
| Unlocks | `f_Capture_Resonant.md §7` (emit used in approach engineering) · `f_Decay.md §8` (reversal interface) |

---

### `f_Dampen.md` · 🔵 scaffold · v0.1.0

| Field | Value |
|---|---|
| Tag | `[FFF:GRAVITY:DAMPEN]` |
| Node | `F_freq` — decreases `ρ(Φ)` |
| Role | Engineering primitive — shallows coherence well; assists release; risks FM-009 |
| Key Operators | `F_damp` · `ρ(Φ)_floor` · `r_damp` |
| Key Primitives | `suppress_field` · `check_floor` · `check_cascade_risk` |
| Failure Risk | FM-009 (Dampen Cascade) if propagation exceeds `r_damp` |
| Current Gaps | §2 prose · `F_damp` bounds · propagation model · examples |
| Unlocks | `f_Release.md §5` (dampen as release assist) · `f_Capture_Resonant.md §7` |

---

### `f_Amplify.md` · 🔵 scaffold · v0.1.0

| Field | Value |
|---|---|
| Tag | `[FFF:GRAVITY:AMPLIFY]` |
| Node | `F_fluid` — increases `β` and `P_eff` |
| Role | Engineering primitive — strengthens mass-coupling; deepens `d_bind` in established orbits |
| Key Operators | `F_amp` · `β_max` · `amp_cost` |
| Key Primitives | `amplify_coupling` · `check_runaway_risk` |
| Failure Risk | FM-010 (Amplify Runaway) if `β > β_max` |
| Current Gaps | §2 prose · `F_amp` ceiling derivation · energy cost model · examples |
| Unlocks | `f_Decay.md §8` (amplify as decay reversal) · `f_Capture_Resonant.md §7` |

---

### `f_Deflect.md` · 🔵 scaffold · v0.1.0

| Field | Value |
|---|---|
| Tag | `[FFF:GRAVITY:DEFLECT]` |
| Node | `F_force` — changes approach heading |
| Role | Engineering primitive — redirects `v_approach` without changing magnitude |
| Key Operators | `heading_delta` · `r_deflect` · `deflect_cost` |
| Key Primitives | `redirect_force_node` · `compute_deflection_cost` |
| Current Gaps | §2 prose · heading bounds · deflection cost formula · examples |
| Unlocks | `f_Capture_Resonant.md §7` (primary heading tool) · `f_Capture_Asymmetric.md §7` (`find_optimal_heading`) |

---

### `f_Capture_Multi.md` · 🔵 scaffold · v0.1.0

| Field | Value |
|---|---|
| Tag | `[FFF:GRAVITY:CAPTURE:MULTI]` |
| Extends | `f_Capture` |
| Core Problem | N Elements approaching 1 Attractor simultaneously |
| Key New Operators | `N`, `eval_order`, `Φ_perturbed`, `capacity_remaining` |
| New Failure Modes | FM-003-M (multi-frame saturation) · Priority Starvation · Cross-Perturbation Collapse |
| Current Gaps | §2 prose · evaluation order priority rule · cross-element perturbation model · examples |
| Unlocks | `f_Capture_Cascade.md §2` (cascade extends multi-body model) |

---

### `f_Capture_Cascade.md` · 🔵 scaffold · v0.1.0

| Field | Value |
|---|---|
| Tag | `[FFF:GRAVITY:CAPTURE:CASCADE]` |
| Extends | `f_Capture` |
| Core Problem | New capture event perturbs existing orbits in the Attractor's registry |
| Key New Operators | `Δcurvature`, `perturbation_sensitivity`, `cascade_depth` |
| New Failure Modes | Cascade Destabilization · Cascade Collapse · Registry Cascade |
| Current Gaps | §2 prose · perturbation magnitude formula · cascade termination condition · examples |
| Unlocks | `f_Capture_Networked.md §9` (topology pattern: Registry Cascade) |

---

### `f_Capture_Resonant.md` · 🔵 scaffold · v0.1.0

| Field | Value |
|---|---|
| Tag | `[FFF:GRAVITY:CAPTURE:RESONANT]` |
| Extends | `f_Capture` |
| Core Inversion | Given `ω_res_target` → compute required `{v_approach, heading, ρ(Φ), β}` |
| Key New Operators | `ω_res_target`, `approach_parameters`, `solution_space`, `energy_cost`, `nearest_valid` |
| Key New Primitives | `solve_resonant_approach`, `validate_resonant_solution`, `find_nearest_valid_resonance` |
| Current Gaps | §2 prose · solver algorithm · solution space characterization · resonance target table values · examples |
| Unlocks | `f_Capture_Networked.md §9` (topology pattern: Resonant Cluster) |

---

### `f_Capture_Asymmetric.md` · 🔵 scaffold · v0.1.0

| Field | Value |
|---|---|
| Tag | `[FFF:GRAVITY:CAPTURE:ASYMMETRIC]` |
| Extends | `f_Capture` |
| Core Departure | Replaces scalar `ρ(Φ)` with directional tensor `ρ(Φ,θ)` |
| Key New Operators | `ρ(Φ,θ)`, `θ_approach`, `anisotropy_index`, `θ_optimal`, `θ_critical` |
| Key New Primitives | `map_field_tensor`, `evaluate_at_heading`, `find_optimal_heading`, `assess_postlock_coherence` |
| Current Gaps | §2 prose · field tensor representation format · anisotropy index formula · examples |
| Unlocks | Future: `f_Field.md §9` (asymmetric field states) |

---

### `f_Capture_Temporal.md` · 🔵 scaffold · v0.1.0

| Field | Value |
|---|---|
| Tag | `[FFF:GRAVITY:CAPTURE:TEMPORAL]` |
| Extends | `f_Capture` |
| Core Departure | All operators become time-indexed: `M_A(t)`, `ρ(Φ,t)`, `r_capture(t)` |
| Key New Operators | `C_thresh(t)`, `t_entry`, `t_encounter`, `temporal_capture_window`, `ΔM_A`, `Δρ` |
| Key New Primitives | `build_approach_timeseries`, `find_encounter_conditions`, `detect_phase_miss`, `compute_optimal_entry_time` |
| Current Gaps | §2 prose · time-series representation format · phase miss detection algorithm · examples |
| Unlocks | Future: `f_Orbit.md §9` (time-variant orbital period) |

---

### `f_Capture_Networked.md` · 🔵 scaffold · v0.1.0

| Field | Value |
|---|---|
| Tag | `[FFF:GRAVITY:CAPTURE:NETWORKED]` |
| Extends | `f_Capture` |
| Core Addition | GravityGraph — persistent directed weighted graph of all capture relationships |
| Key New Operators | `GravityGraph`, `G_node`, `G_edge`, `G_degree`, `G_depth`, `G_stability`, `G_cascade_risk` |
| Key New Primitives | `write_to_graph`, `update_edge_state`, `purge_graph_node`, `create_composite_node`, `execute_graph_query`, `compute_cascade_path`, `compute_stability_index`, `snapshot_graph` |
| Topology Patterns | Star · Chain · Cluster · Isolate · Critical Node · Ghost Orbit |
| Current Gaps | §2 prose · graph storage format decision · query interface formal spec · examples |
| Unlocks | Cross-module: `SoN/s_Capture.md` topology correlation queries |

---

### `GravityOfDismissal.md` · ✅ canonical · v1.0.0

| Field | Value |
|---|---|
| Tag | `[FFF:GRAVITY:HISTORY:DISMISSAL]` |
| Role | Historical record of institutional suppression in gravity science; 7-vector attack playbook mapped to FFF_Gravity |
| Sections | §1–§13 (13 sections) |
| Dismissal Registry | 15 cases: Gerber · Ritz · Miller · Mach · Chandrasekhar · Dingle · Arp · Marić · Noether · Payne-Gaposchkin · Bell Burnell · Rubin · Alfvén · Milgrom · Verlinde |
| Attack Vectors | I Authority Ambush · II Empirical Retrofit · III Access Withdrawal · IV Priority Erasure · V Social Quarantine · VI Identity Disqualification · VII Silence Treatment |
| Current Gaps | None — canonical |

---

### `f_Source.md` · 📁 archived

| Field | Value |
|---|---|
| Role | Genesis dialogue archive — the originating flash conversations that produced the FFF triadic gravity model |
| Use | Read-only reference for §2 prose sections in Wave 2 and Wave 3 files; primary source for F_freq / F_fluid / F_force node definitions |
| Do Not Edit | This file is a historical record. No additions. |

---

## §4 · Dependency Graph

<!--
  metadata:
    section:       dependency-graph
    section_id:    §4
    type:          visual-graph
    normative:     true
    notation:      ASCII directed graph
    created_in:    SES-20260813-INDEX-001
  session:
    session_id:    SES-20260813-INDEX-001
    touch_count:   1
    change_type:   created
-->

```
EXTERNAL INPUTS
  FFF_Field ──┐
  FFF_Frame ──┤
  FFF_Momentum┤──────────────────────────────────────────┐
  FFF_Resonance┘                                         │
                                                         ▼
                                              ┌─────────────────┐
LAYER DEFINITIONS                             │   f_Capture.md  │ ✅
  f_Field.md  ──── (F_freq) ──────────────── │   [CANONICAL]   │
  f_Force.md  ──── (F_force) ─────────────── │                 │
  f_Frame.md  ──── (registry) ────────────── └────────┬────────┘
                                                       │
                              ┌────────────────────────┼───────────────────┐
                              │                        │                   │
                              ▼                        ▼                   ▼
                         f_Orbit.md             f_Decay.md           f_Release.md
                              │                    │    │                  │
                              └──────────┐         │    └──────────────────┤
                                         ▼         ▼                       │
                                      f_Collapse.md                        │
                                                                           │
ENGINEERING PRIMITIVES (F_freq / F_fluid / F_force)                       │
  f_Emit.md ────────────────────────────────────────────────────────► restore d_bind
  f_Dampen.md ──────────────────────────────────────────────────────► assist release
  f_Amplify.md ─────────────────────────────────────────────────────► boost β
  f_Deflect.md ─────────────────────────────────────────────────────► change heading

                              ALL WAVE 3 FILES
                                    │
                    ┌───────────────┼───────────────────┐
                    ▼               ▼                   ▼
          f_Capture_Multi    f_Capture_Cascade   f_Capture_Resonant
          f_Capture_Asymmetric  f_Capture_Temporal  f_Capture_Networked
                                    │
                                    ▼
                            FFF_Registry (external)
                            GravityGraph (distributed)
```

---

## §5 · Unlock Sequence

<!--
  metadata:
    section:       unlock-sequence
    section_id:    §5
    type:          dependency-sequence
    normative:     true
    created_in:    SES-20260813-INDEX-001
    note: >
      A file is UNLOCKED when all its blocking dependencies are canonical.
      A file is OPEN when it is unlocked and has not yet been canonicalized.
      Canonicalize in unlock order. Do not skip waves.
  session:
    session_id:    SES-20260813-INDEX-001
    touch_count:   1
    change_type:   created
-->

### Wave 1 — Admin (all open now, no blocking deps)

```
✅ README.md          open → canonicalize anytime
✅ INDEX.md           open → canonicalize anytime
   OPERATORS.md       open → canonicalize anytime (partial pending Wave 3)
   GLOSSARY.md        open → canonicalize anytime (review pending Wave 3)
   CHANGELOG.md       open → canonicalize anytime
   FFF_Gravity_module.json   open → canonicalize anytime
```

### Wave 2 — Layer Definitions (open now, blocked by: nothing)

```
   f_Field.md         open → primary source: f_Source.md §F_freq sections
   f_Force.md         open → primary source: f_Source.md §F_force sections
   f_Frame.md         open → primary source: f_Capture.md §5 Condition 5, §6 FM-003
```

### Wave 3 — Core Functions (blocked by: Wave 2)

```
PRIORITY ORDER (recommended):

   1. f_Release.md    blocked until: f_Orbit.md ✅ + f_Decay.md ✅
   2. f_Decay.md      blocked until: f_Orbit.md ✅
   3. f_Orbit.md      blocked until: f_Capture.md ✅  ← ALREADY MET
   4. f_Collapse.md   blocked until: f_Decay.md ✅

   f_Emit.md          blocked until: f_Field.md ✅
   f_Dampen.md        blocked until: f_Field.md ✅
   f_Amplify.md       blocked until: f_Field.md ✅ + f_Capture.md ✅  ← ALREADY MET
   f_Deflect.md       blocked until: f_Force.md ✅ + f_Capture.md ✅  ← ALREADY MET
```

### Wave 4 — Capture Variants (blocked by: all Wave 3 canonical)

```
   f_Capture_Multi.md        → can open once: f_Orbit.md ✅ + f_Frame.md ✅
   f_Capture_Cascade.md      → can open once: f_Decay.md ✅
   f_Capture_Resonant.md     → can open once: f_Deflect.md ✅ + f_Emit.md ✅ + f_Amplify.md ✅
   f_Capture_Asymmetric.md   → can open once: f_Field.md ✅ + f_Force.md ✅ + f_Deflect.md ✅
   f_Capture_Temporal.md     → can open once: f_Field.md ✅ + f_Decay.md ✅
   f_Capture_Networked.md    → can open once: ALL Wave 3 ✅
```

---

## §6 · Section Maps

<!--
  metadata:
    section:       section-maps
    section_id:    §6
    type:          section-registry
    normative:     true
    scope:         canonical files only; scaffolds tracked by planned sections
    created_in:    SES-20260813-INDEX-001
  session:
    session_id:    SES-20260813-INDEX-001
    touch_count:   1
    change_type:   created
-->

### `f_Capture.md` — Section Map

| § | Title | Normative | Key Content |
|---|---|---|---|
| §0 | Session Context | — | Live register; touch map; resolution protocol |
| §1 | Module Identity | ✅ | Identity table; canonical tag; version |
| §2 | Canonical Description | ✅ | Prose definition of capture event; bidirectional registration |
| §3 | Triadic Equation | ✅ | `f_Capture(E,A,Φ)→Ω`; FFF layer mapping table |
| §4 | Operator Registry | ✅ | §4.1 Primary (6) · §4.2 Derived (4) · §4.3 Flags (5) · §4.4 Master spec · §4.5 Interaction matrix · §4.6 State transitions · §4.7 Eval order · §4.8 Composition rules |
| §5 | Stability Conditions | ✅ | 5 conjunctive conditions; governing operator + eval step per condition |
| §6 | Failure Modes | ✅ | FM-001–007; trigger, operators involved, state transition, severity |
| §7 | Engineering Primitives | ✅ | §7.1 I/O signature table (6 primitives) · §7.2 Definitions with inline session/metadata |
| §8 | Canonical Examples | — | EX-001–004; covers all 4 outcome states |
| §9 | Future Applications | — | 8 roadmap items: planned/research/exploratory |
| §10 | Cross-Module References | ✅ | 5 module deps; direction + operators supplied columns |
| §11 | Document Metadata | — | Administrative record |
| §12 | Session Log | — | Append-only audit; SES-001–004 |

### `GravityOfDismissal.md` — Section Map

| § | Title | Key Content |
|---|---|---|
| §1 | The Standard Story | How canonical gravity history was constructed; 3 structural properties |
| §2 | Before Einstein | Fatio/Le Sage · Paul Gerber · Walter Ritz |
| §3 | The Chandrasekhar Ambush | Full account; mechanics of the kill; aftermath; 48-year vindication |
| §4 | Dayton Miller | 5.2M measurements; Shankland retrofit; posthumous execution |
| §5 | Herbert Dingle | Right to be heard; Social Quarantine pattern |
| §6 | Halton Arp | Telescope access withdrawal; exile to Germany |
| §7 | MOND / Verlinde / Alfvén | The Silence Treatment; three cases |
| §8 | The Erased | Marić · Noether · Payne-Gaposchkin · Bell Burnell · Rubin; Matilda Effect |
| §9 | The Playbook | 7 attack vectors: Authority Ambush · Empirical Retrofit · Access Withdrawal · Priority Erasure · Social Quarantine · Identity Disqualification · Silence Treatment |
| §10 | Mapping to FFF_Gravity | Likelihood table per vector; defense posture per vector |
| §11 | What the Record Shows | 7 summary findings |
| §12 | Dismissal Registry | 15 cases; name, period, mechanism, outcome, vindicated? |
| §13 | References | Primary sources; Matilda Effect; paradigm dynamics |

---

## §7 · Completion Tracker

<!--
  metadata:
    section:       completion-tracker
    section_id:    §7
    type:          tracker
    normative:     false
    stability:     living
    update_policy: >
      Update this section at the close of every session that changes
      any file's status. Do not update mid-session.
    last_updated:  2026-08-13 SES-20260813-INDEX-001
  session:
    session_id:    SES-20260813-INDEX-001
    touch_count:   1
    change_type:   created
-->

### By Wave

| Wave | Group | Files | ✅ | 🔵 | 📁 | % Complete |
|---|---|---|---|---|---|---|
| 0 | Existing | 3 | 2 | 0 | 1 | 67% |
| 1 | Admin | 6 | 2 | 4 | 0 | 33% |
| 2 | Layer Definitions | 3 | 0 | 3 | 0 | 0% |
| 3 | Core Functions | 8 | 0 | 8 | 0 | 0% |
| 4 | Capture Variants | 6 | 0 | 6 | 0 | 0% |
| — | **Total** | **26** | **4** | **21** | **1** | **15%** |

### By File — Full Status List

| File | Status | Version | Last Session |
|---|---|---|---|
| `f_Capture.md` | ✅ canonical | 1.0.0 | SES-20260813-003 |
| `GravityOfDismissal.md` | ✅ canonical | 1.0.0 | SES-20260813-GOD-001 |
| `README.md` | ✅ canonical | 1.0.0 | SES-20260813-README-001 |
| `INDEX.md` | ✅ canonical | 1.0.0 | SES-20260813-INDEX-001 |
| `f_Source.md` | 📁 archived | — | SES-20260813-001 |
| `OPERATORS.md` | 🔵 scaffold | 0.1.0 | SES-20260813-005 |
| `GLOSSARY.md` | 🔵 scaffold | 0.1.0 | SES-20260813-005 |
| `CHANGELOG.md` | 🔵 scaffold | 0.1.0 | SES-20260813-005 |
| `FFF_Gravity_module.json` | 🔵 scaffold | 0.1.0 | SES-20260813-005 |
| `f_Field.md` | 🔵 scaffold | 0.1.0 | SES-20260813-005 |
| `f_Force.md` | 🔵 scaffold | 0.1.0 | SES-20260813-005 |
| `f_Frame.md` | 🔵 scaffold | 0.1.0 | SES-20260813-005 |
| `f_Release.md` | 🔵 scaffold | 0.1.0 | SES-20260813-005 |
| `f_Decay.md` | 🔵 scaffold | 0.1.0 | SES-20260813-005 |
| `f_Orbit.md` | 🔵 scaffold | 0.1.0 | SES-20260813-005 |
| `f_Collapse.md` | 🔵 scaffold | 0.1.0 | SES-20260813-005 |
| `f_Emit.md` | 🔵 scaffold | 0.1.0 | SES-20260813-005 |
| `f_Dampen.md` | 🔵 scaffold | 0.1.0 | SES-20260813-005 |
| `f_Amplify.md` | 🔵 scaffold | 0.1.0 | SES-20260813-005 |
| `f_Deflect.md` | 🔵 scaffold | 0.1.0 | SES-20260813-005 |
| `f_Capture_Multi.md` | 🔵 scaffold | 0.1.0 | SES-20260813-005 |
| `f_Capture_Cascade.md` | 🔵 scaffold | 0.1.0 | SES-20260813-005 |
| `f_Capture_Resonant.md` | 🔵 scaffold | 0.1.0 | SES-20260813-005 |
| `f_Capture_Asymmetric.md` | 🔵 scaffold | 0.1.0 | SES-20260813-005 |
| `f_Capture_Temporal.md` | 🔵 scaffold | 0.1.0 | SES-20260813-005 |
| `f_Capture_Networked.md` | 🔵 scaffold | 0.1.0 | SES-20260813-005 |

---

## §8 · AI Traversal Interface

<!--
  metadata:
    section:       ai-traversal
    section_id:    §8
    type:          interface-spec
    normative:     false
    audience:      AI systems consuming this module
    created_in:    SES-20260813-INDEX-001
  session:
    session_id:    SES-20260813-INDEX-001
    touch_count:   1
    change_type:   created
-->

If you are an AI system reading FFF_Gravity, use this traversal order:

```
STEP 1 — Orientation
  Read: README.md           → what the module is; reading order for your role
  Read: INDEX.md            → this file; full registry

STEP 2 — Symbol Authority
  Read: OPERATORS.md        → all operator symbols; frozen list; failure mode index
  Read: GLOSSARY.md         → term definitions; resolve any ambiguous names

STEP 3 — Reference Implementation
  Read: f_Capture.md        → canonical function; all operator tables; examples; session log

STEP 4 — Layer Context
  Read: f_Field.md          → what F_freq is; how ρ(Φ) is computed
  Read: f_Force.md          → what F_force is; how v_approach is defined
  Read: f_Frame.md          → registry structure; capacity rules

STEP 5 — Function Chain
  Read in order: f_Orbit.md → f_Decay.md → f_Release.md → f_Collapse.md

STEP 6 — Engineering Primitives
  Read: f_Emit.md · f_Dampen.md · f_Amplify.md · f_Deflect.md

STEP 7 — Variants (as needed)
  Read: f_Capture_{Multi|Cascade|Resonant|Asymmetric|Temporal|Networked}.md

STEP 8 — Strategic Context
  Read: GravityOfDismissal.md    → institutional history; defense map
  Read: f_Source.md              → genesis dialogue; original model construction
```

**Key invariants for AI consumers:**
- All symbols in `OPERATORS.md §1–§2` marked ✅ are frozen — do not invent variants
- `f_Capture.md` is the reference implementation — all other files extend or consume it
- `ρ(Φ) = 0` always triggers FM-002 regardless of other conditions
- `β < 1.0` always produces flyby — no capture regardless of field or frame state
- Terminal states `CAPTURE_FAILED` and `CAPTURE_COLLISION` are irreversible
- `f_Source.md` is read-only — it is a historical record, not an editable document

---

## §9 · Document Metadata

<!--
  metadata:
    section:       document-metadata
    section_id:    §9
    type:          administrative
    normative:     false
  session:
    session_id:    SES-20260813-INDEX-001
    touch_count:   1
    change_type:   created
-->

| Field | Value |
|---|---|
| Canonical Path | `docs/FFF_Gravity/INDEX.md` |
| Version | 1.0.0 |
| Status | Canonical |
| Stability | Living — update at close of any session that changes file status |
| Created | 2026-08-13 |
| Last Modified | 2026-08-13 |
| Authors | TriadicFrameworks |
| License | See `/LICENSE` at repository root |
| Encoding | UTF-8 · LF |

---

*Authoritative registry for the FFF_Gravity module.*
*Update this file whenever a new file is created or a scaffold is promoted to canonical.*
*For the full repository index see `docs/SITEMAP.md`.*
```

---

**Commit message:**
```
feat(FFF_Gravity): add canonical INDEX.md — full file registry, per-file detail, dependency graph, completion tracker [SES-20260813-INDEX-001]

---

What INDEX.md does that README.md doesn't:

| README.md | INDEX.md |
|---|---|
| What the module is | What every file is — in full detail |
| Which files exist (summary table) | Per-file entry: operators, primitives, gaps, unlocks |
| Quick reference failure modes | Full dependency resolution per file |
| Reading orders | AI traversal interface with invariants |
| Unlock map (visual) | Unlock sequence with blocking conditions per file |
| Completion tracker (summary) | Completion tracker with per-file status + last session |
| — | Section maps for all canonical files |
