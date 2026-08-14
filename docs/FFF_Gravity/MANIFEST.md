# FFF_Gravity Module — MANIFEST.md
**Complete Registry: PRIMs · Operators · Conditions · FMs · INVs · State Flags**
> Sealed: 2026-08-14 · Session: SES-20260814-MANIFEST-001
> Append-only. No entry may be modified without a version bump.

---

## §1 Module Summary

| Field                   | Value                                          |
|-------------------------|------------------------------------------------|
| Module                  | FFF_Gravity                                    |
| Repository              | umaywant2/TriadicFrameworks                    |
| Path                    | docs/FFF_Gravity/                              |
| Total spec files        | 29                                             |
| Total waves             | 5                                              |
| PRIM range              | PRIM:001 – PRIM:042                            |
| Total PRIMs             | 42                                             |
| Total Invariants        | 10 (INV-001 – INV-010)                         |
| Total Failure Modes     | 10 base (FM-001 – FM-010) + 3 sub-modes        |
| Total Condition Prefixes| 11                                             |
| Total State Flags       | 31                                             |
| Last updated            | 2026-08-14                                     |
| Status                  | SEALED — all registries frozen pending Wave 6  |

---

## §2 Wave Manifest

| Wave | Role                | Files | PRIM Range | Sealed |
|------|---------------------|-------|------------|--------|
| 0    | Genesis             | 3     | —          | ✅     |
| 1    | Admin / Registry    | 6     | —          | ✅     |
| 2    | Layer Definitions   | 3     | 001–006    | ✅     |
| 3    | Core Functions      | 8     | 007–024    | ✅     |
| 4    | Capture Variants    | 8     | 025–040    | ✅     |
| 5    | Dismissal           | 1     | 041–042    | ✅     |

### §2.1 File Registry

| Wave | #  | File                      | Type               | PRIM(s)  |
|------|----|---------------------------|--------------------|----------|
| 0    | 01 | GravityOfDismissal.md     | Conceptual genesis | —        |
| 0    | 02 | f_Capture.md              | Operator genesis   | —        |
| 0    | 03 | f_Source.md               | Node registry      | —        |
| 1    | 04 | README.md                 | Navigation         | —        |
| 1    | 05 | INDEX.md                  | File index         | —        |
| 1    | 06 | OPERATORS.md              | Symbol authority   | —        |
| 1    | 07 | GLOSSARY.md               | Term definitions   | —        |
| 1    | 08 | CHANGELOG.md              | Change log         | —        |
| 1    | 09 | FFF_Gravity_module.json   | Machine registry   | —        |
| 2    | 10 | f_Field.md                | Layer 1 — F_freq   | 001–002  |
| 2    | 11 | f_Force.md                | Layer 2 — F_force  | 003–005  |
| 2    | 12 | f_Frame.md                | Layer 3 — F_fluid  | 004, 006 |
| 3    | 13 | f_Orbit.md                | Core function      | 007, 012 |
| 3    | 14 | f_Release.md              | Core function      | 008–009  |
| 3    | 15 | f_Decay.md                | Core function      | 010–011  |
| 3    | 16 | f_Collapse.md             | Core function      | 013–014  |
| 3    | 17 | f_Emit.md                 | Core function      | 015–017  |
| 3    | 18 | f_Dampen.md               | Core function      | 018–020  |
| 3    | 19 | f_Amplify.md              | Core function      | 021–022  |
| 3    | 20 | f_Deflect.md              | Core function      | 023–024  |
| 4    | 21 | f_Capture_Multi.md        | Capture variant    | 025–026  |
| 4    | 22 | f_Capture_Cascade.md      | Capture variant    | 027–028  |
| 4    | 23 | f_Capture_Soft.md         | Capture variant    | 029–030  |
| 4    | 24 | f_Capture_Hard.md         | Capture variant    | 031–032  |
| 4    | 25 | f_Capture_Resonant.md     | Capture variant    | 033–034  |
| 4    | 26 | f_Capture_Asymmetric.md   | Capture variant    | 035–036  |
| 4    | 27 | f_Capture_Temporal.md     | Capture variant    | 037–038  |
| 4    | 28 | f_Capture_Networked.md    | Capture variant    | 039–040  |
| 5    | 29 | f_Dismiss.md              | Dismissal          | 041–042  |

---

## §3 PRIM Registry — Full Table

> **INV column key:** ✅ active · — not in scope · ⚠ conditional

| PRIM | Name | Type | File (Wave) | INV-001 | INV-002 | INV-003 | INV-004 | INV-005 | INV-006 | INV-007 | INV-008 | INV-009 | INV-010 |
|------|------|------|-------------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| 001 | `compute_field_density`        | Pure   | f_Field (W2)              | ✅ | ✅ | ✅ | —  | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 002 | `update_field_state`           | Impure | f_Field (W2)              | ✅ | ✅ | ✅ | —  | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 003 | `compute_force_vector`         | Pure   | f_Force (W2)              | ✅ | —  | —  | ✅ | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 004 | `register_capture`             | Impure | f_Frame (W2)              | ✅ | —  | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 005 | `compute_approach_vector`      | Pure   | f_Force (W2)              | ✅ | —  | —  | ✅ | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 006 | `check_frame_capacity`         | Pure   | f_Frame (W2)              | —  | —  | —  | —  | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 007 | `classify_orbit`               | Pure   | f_Orbit (W3)              | ✅ | ✅ | —  | —  | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 008 | `compute_release_vector`       | Pure   | f_Release (W3)            | ✅ | —  | —  | ✅ | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 009 | `execute_release`              | Impure | f_Release (W3)            | ✅ | —  | —  | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 010 | `compute_decay_step`           | Pure   | f_Decay (W3)              | ✅ | ✅ | ✅ | —  | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 011 | `evaluate_collapse_eligibility`| Pure   | f_Decay (W3)              | ✅ | ✅ | —  | —  | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 012 | `compute_orbital_period`       | Pure   | f_Orbit (W3)              | ✅ | ✅ | —  | —  | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 013 | `evaluate_collapse_path`       | Pure   | f_Collapse (W3)           | ✅ | ✅ | ✅ | —  | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 014 | `execute_collapse`             | Impure | f_Collapse (W3)           | ✅ | ✅ | ✅ | —  | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 015 | `compute_emit_vector`          | Pure   | f_Emit (W3)               | ✅ | ✅ | —  | —  | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 016 | `compute_field_delta`          | Pure   | f_Emit (W3)               | ✅ | ✅ | —  | —  | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 017 | `execute_emit`                 | Impure | f_Emit (W3)               | ✅ | ✅ | ✅ | —  | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 018 | `compute_dampen_force`         | Pure   | f_Dampen (W3)             | ✅ | ✅ | —  | —  | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 019 | `apply_field_floor`            | Pure   | f_Dampen (W3)             | ✅ | ✅ | ✅ | —  | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 020 | `execute_dampen`               | Impure | f_Dampen (W3)             | ✅ | ✅ | ✅ | —  | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 021 | `compute_amplify_force`        | Pure   | f_Amplify (W3)            | ✅ | ✅ | —  | ✅ | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 022 | `check_runaway_risk`           | Pure   | f_Amplify (W3)            | ✅ | ✅ | —  | ✅ | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 023 | `compute_deflection_angle`     | Pure   | f_Deflect (W3)            | ✅ | —  | —  | ✅ | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 024 | `execute_deflect`              | Impure | f_Deflect (W3)            | ✅ | —  | —  | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 025 | `execute_multi_capture`        | Impure | f_Capture_Multi (W4)      | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 026 | `compute_perturbation_budget`  | Pure   | f_Capture_Multi (W4)      | ✅ | ✅ | —  | ✅ | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 027 | `evaluate_cascade_eligibility` | Pure   | f_Capture_Cascade (W4)    | ✅ | —  | ✅ | ✅ | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 028 | `execute_cascade_step`         | Impure | f_Capture_Cascade (W4)    | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 029 | `evaluate_soft_eligibility`    | Pure   | f_Capture_Soft (W4)       | ✅ | ✅ | ✅ | ✅ | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 030 | `execute_soft_capture`         | Impure | f_Capture_Soft (W4)       | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 031 | `evaluate_hard_eligibility`    | Pure   | f_Capture_Hard (W4)       | ✅ | ✅ | ✅ | ✅ | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 032 | `execute_hard_lock`            | Impure | f_Capture_Hard (W4)       | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 033 | `eval_resonance_window`        | Pure   | f_Capture_Resonant (W4)   | ✅ | ✅ | ✅ | ✅ | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 034 | `lock_resonance`               | Impure | f_Capture_Resonant (W4)   | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 035 | `eval_asymmetric_approach`     | Pure   | f_Capture_Asymmetric (W4) | ✅ | ✅ | ✅ | ✅ | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 036 | `lock_asymmetric`              | Impure | f_Capture_Asymmetric (W4) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 037 | `evaluate_temporal_window`     | Pure   | f_Capture_Temporal (W4)   | ✅ | ✅ | ✅ | ✅ | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 038 | `lock_temporal_capture`        | Impure | f_Capture_Temporal (W4)   | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 039 | `evaluate_network_capture`     | Pure   | f_Capture_Networked (W4)  | ✅ | ✅ | ✅ | ✅ | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 040 | `lock_network_capture`         | Impure | f_Capture_Networked (W4)  | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 041 | `evaluate_dismissal`           | Pure   | f_Dismiss (W5)            | ✅ | ✅ | ✅ | —  | ✅ | —  | ✅ | ✅ | ✅ | ✅ |
| 042 | `execute_dismissal`            | Impure | f_Dismiss (W5)            | ✅ | ✅ | ✅ | —  | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## §4 Invariant Registry (INV-001 – INV-010)

| ID      | Statement                                                                       | Wave | Scope         |
|---------|---------------------------------------------------------------------------------|------|---------------|
| INV-001 | G = F_freq · F_fluid · F_force — triadic identity must be preserved             | 2    | Module-global |
| INV-002 | ρ(Φ) ∈ [0,1]; ρ_D(Φ) ∈ (−1,0] — field density domains are bounded            | 2    | Module-global |
| INV-003 | ρ(Φ) = 0 triggers FM-002 unconditionally                                        | 2    | Module-global |
| INV-004 | β < 1.0 triggers FM-001 unconditionally                                         | 2    | Module-global |
| INV-005 | All conditions within a file are conjunctive — any failure aborts               | 2    | Module-global |
| INV-006 | Terminal states are irreversible — no re-entry without explicit reset           | 2    | Module-global |
| INV-007 | f_Source.md is read-only — node properties may not be mutated by operators      | 2    | Module-global |
| INV-008 | Evaluation order within a PRIM is normative — documented order is binding       | 3    | All PRIMs     |
| INV-009 | OPERATORS.md is the single symbol authority — all symbols pre-registered        | 3    | Module-global |
| INV-010 | Operators are frozen on first canonical appearance — no redefinition            | 3    | Module-global |

### §4.1 Universal INV Coverage Rules

| INV     | Pure PRIMs | Impure PRIMs | Rule |
|---------|------------|--------------|------|
| INV-005 | Required ✅ | Required ✅ | All condition sets are AND-gated |
| INV-006 | Must be — | Required ✅ | Only Impure PRIMs mutate state |
| INV-007 | Required ✅ | Required ✅ | Source nodes are always read-only |
| INV-008 | Required ✅ | Required ✅ | Evaluation order always normative |
| INV-009 | Required ✅ | Required ✅ | Symbols always pre-registered |
| INV-010 | Required ✅ | Required ✅ | Operators always frozen |

---

## §5 Failure Mode Registry

| ID     | Name                  | Domain       | Fatal? | First defined          | Sub-modes                              |
|--------|-----------------------|--------------|--------|------------------------|----------------------------------------|
| FM-001 | Flyby/Approach Reject | F_force      | No     | f_Force (W2)           | WELL_BARRIER, WINDOW_MISS, TRAJECTORY_MISS, TEMPORAL_MISS |
| FM-002 | Field Null            | F_freq       | Yes    | f_Field (W2)           | —                                      |
| FM-003 | Frame Saturation      | F_fluid      | No     | f_Frame (W2)           | FM-003-M, FM-003-C, FM-003-N           |
| FM-004 | Resonance Drift       | F_freq       | No     | f_Decay (W3)           | —                                      |
| FM-005 | Decay Spiral          | F_freq/fluid | Yes*   | f_Decay (W3)           | —                                      |
| FM-006 | Phantom Capture       | F_force      | Yes    | f_Deflect (W3)         | PHANTOM_RESONANCE, DISMISS_PHANTOM     |
| FM-007 | Mutual Dissolution    | F_fluid      | Yes    | f_Collapse (W3)        | PARITY_BREACH                          |
| FM-008 | Release Failure       | F_force      | No     | f_Release (W3)         | —                                      |
| FM-009 | Dampen Cascade        | F_freq       | No     | f_Dampen (W3)          | —                                      |
| FM-010 | Amplify Ceiling       | F_fluid      | No     | f_Amplify (W3)         | β domain, ρ domain                     |

*FM-005 fatal for the orbit; entity node survives.

### §5.1 FM Sub-mode Registry

| Sub-mode  | Parent | Introduced in              | Trigger                                           |
|-----------|--------|----------------------------|---------------------------------------------------|
| FM-003-M  | FM-003 | f_Capture_Multi (W4)       | Multi-target bind conflict mid-session            |
| FM-003-C  | FM-003 | f_Capture_Cascade (W4)     | Cascade capacity breach mid-chain                 |
| FM-003-N  | FM-003 | f_Capture_Networked (W4)   | All network node frames simultaneously saturated  |

---

## §6 Condition Prefix Registry

| Prefix | Name                       | File                      | Conditions    |
|--------|----------------------------|---------------------------|---------------|
| SC-    | Stability Conditions       | f_Capture (W0)            | SC-1–SC-5     |
| DC-    | Decay Conditions           | f_Decay (W3)              | DC-1–DC-4     |
| MC-    | Multi-Capture Conditions   | f_Capture_Multi (W4)      | MC-1–MC-2     |
| CAS-   | Cascade Conditions         | f_Capture_Cascade (W4)    | CAS-1–CAS-4   |
| SCS-   | Soft Capture Conditions    | f_Capture_Soft (W4)       | SCS-1–SCS-4   |
| HLC-   | Hard Lock Conditions       | f_Capture_Hard (W4)       | HLC-1–HLC-4   |
| RLC-   | Resonance Lock Conditions  | f_Capture_Resonant (W4)   | RLC-1–RLC-5   |
| AC-    | Asymmetric Conditions      | f_Capture_Asymmetric (W4) | AC-1–AC-5     |
| TC-    | Temporal Conditions        | f_Capture_Temporal (W4)   | TC-1–TC-5     |
| NC-    | Network Conditions         | f_Capture_Networked (W4)  | NC-1–NC-5     |
| DISM-  | Dismissal Conditions       | f_Dismiss (W5)            | DISM-1–DISM-5 |

---

## §7 State Flag Registry

| Flag                | Set by PRIM | Terminal? | Meaning                                                        |
|---------------------|-------------|-----------|----------------------------------------------------------------|
| CAPTURE_LOCKED      | 004         | Yes       | Standard capture committed; orbit evaluation begins            |
| CAPTURE_SOFT        | 030         | No        | Provisional binding within grace period                        |
| SOFT_STRENGTHENED   | 030         | Yes       | Soft capture promoted to CAPTURE_LOCKED                        |
| SOFT_DISSOLVED      | 030         | Yes       | Soft capture fell below soft_threshold                         |
| GRACE_EXPIRED       | 030         | Yes       | Grace period exhausted without resolution                      |
| ORBIT_STABLE        | 032         | Yes       | Hard lock confirmed; direct ORBIT_STABLE entry                 |
| HARD_ELIGIBLE       | 031         | No        | HLC conditions passed; PRIM:032 may proceed                    |
| HARD_REJECTED       | 031         | Yes       | HLC conditions failed; no retry this encounter                 |
| FRAME_SATURATED     | 032         | No        | FM-003 in hard lock path; retriable                            |
| WINDOW_OPEN         | 033         | No        | Resonance phase check passed                                   |
| WINDOW_CLOSED       | 033         | No        | Resonance phase check failed; retry at t_next_open             |
| RESONANCE_LOCKED    | 034         | Yes       | Resonant orbit committed; orbit_class = RESONANT               |
| RESONANCE_LOST      | FM-004      | No        | ρ(Φ) < ρ_res_floor; orbit degraded to ELLIPTICAL              |
| ASYMMETRIC_APPROACH | 035         | No        | mass_ratio > 0; asymmetry corrections active                   |
| PARITY_WARN         | 035         | No        | mass_ratio ≥ 0.75 × m_parity; caution zone                    |
| PARITY_BREACH       | 035         | Yes       | mass_ratio ≥ m_parity; routed to f_Collapse Path B            |
| ASYMMETRIC_LOCKED   | 036         | Yes       | Asymmetric capture committed                                   |
| CAPTURE_TEMPORAL    | 038         | Yes       | Temporal window capture committed                              |
| TEMPORAL_MISS       | 037         | No        | TC-1, TC-2, or TC-5 failed                                    |
| WINDOW_EXHAUSTED    | 038         | No        | window_id already consumed; re-entry blocked                   |
| NETWORK_CAPTURED    | 040         | Yes       | Entity locked across distributed attractor network             |
| NETWORK_MISS        | 039         | No        | NC- conditions failed; network capture aborted                 |
| NETWORK_SATURATED   | 039         | No        | FM-003-N: all node frames at capacity                          |
| DISMISSED           | 042         | Yes*      | (A,E) binding severed; Dismissal Well active                   |
| DISMISS_INVALID     | 041         | No        | DISM condition failed; no state mutation                       |
| DISMISS_PHANTOM     | 041         | No        | FM-006 phantom guard; d_dismiss bounded                        |
| CAPTURE_FAILED      | Various     | No        | Generic capture rejection; retry possible                      |
| PARTIAL_CASCADE     | 028         | No        | FM-003-C partial state; prior steps committed                  |
| FIELD_NULL          | 002         | Yes       | ρ(Φ) = 0; FM-002 active; no captures possible                 |
| COLLAPSED           | 014         | Yes       | Node collapsed; no further operations                          |
| RELEASED            | 009         | Yes*      | Entity released from orbit; no Dismissal Well created          |

*DISMISSED terminal for (A,E) relation; entity itself remains active.
*RELEASED terminal for this orbit instance; entity may form new orbits.

---

## §8 MANIFEST Changelog

| Version | Date       | Session                   | Notes                                                         |
|---------|------------|---------------------------|---------------------------------------------------------------|
| 1.0.0   | 2026-08-14 | SES-20260814-MANIFEST-001 | Initial canonical release. All 5 waves sealed. 42 PRIMs tabulated with full INV matrix. |

---

*End of MANIFEST.md — FFF_Gravity — v1.0.0 — 2026-08-14*
*29 files · 42 PRIMs · 10 INVs · 10 FMs (+3 sub-modes) · 11 condition prefixes · 31 state flags*

