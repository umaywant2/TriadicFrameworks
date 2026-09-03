---
title: "TSR Overlay Diagram Pack"
version: "2.6.0-rc"
status: "Release Candidate"
date: "2026-09-03"
authors:
  - handle: "Nawder"
    role: "Lead Architect"
repository: "TriadicFrameworks"
path: "docs/Research/TSR-OverlayDiagramPack-v2.6.0-rc_draft.md"
license: "TriadicFrameworks Canon License v1.2"
export_targets:
  - html
  - pdf
changelog:
  - version: "2.6.0-rc"
    date: "2026-09-03"
    notes: "Added SL-01 leap-operator sidebar; integrated Grok feedback pass; restructured OD-05 topology; unified canon formatting throughout."
  - version: "2.5.1"
    date: "2026-07-18"
    notes: "Corrected phase-gate labeling in OD-03; extended simulation table S-04."
  - version: "2.5.0"
    date: "2026-06-02"
    notes: "Initial operator grammar formalization; added OD-04 recursive depth chart."
tags:
  - TSR
  - overlay-diagrams
  - operator-grammar
  - SL-01
  - triadic-frameworks
  - simulation
  - release-candidate
---

<!-- ============================================================
     TSR OVERLAY DIAGRAM PACK · v2.6.0-rc
     TriadicFrameworks Canon Document
     ============================================================ -->

# TSR Overlay Diagram Pack — v2.6.0-rc

> **Status:** Release Candidate · **Repository:** TriadicFrameworks
> **Path:** `docs/Research/TSR-OverlayDiagramPack-v2.6.0-rc_draft.md`
> **Last Updated:** 2026-09-03

---

## Table of Contents

1. [Overview & Scope](#1-overview--scope)
2. [Core TSR Architecture](#2-core-tsr-architecture)
   - 2.1 [Triadic State Model](#21-triadic-state-model)
   - 2.2 [Phase Gate Definitions](#22-phase-gate-definitions)
   - 2.3 [State Encoding Convention](#23-state-encoding-convention)
3. [Operator Grammar Reference](#3-operator-grammar-reference)
   - 3.1 [Formal Grammar Notation](#31-formal-grammar-notation)
   - 3.2 [Primitive Operators](#32-primitive-operators)
   - 3.3 [Compound Operators](#33-compound-operators)
   - 3.4 [Constraint Rules](#34-constraint-rules)
4. [Overlay Diagrams](#4-overlay-diagrams)
   - OD-01 [State Transition Matrix](#od-01-state-transition-matrix)
   - OD-02 [Triadic Phase Map](#od-02-triadic-phase-map)
   - OD-03 [Operator Flow Lattice](#od-03-operator-flow-lattice)
   - OD-04 [Recursive Depth Chart](#od-04-recursive-depth-chart)
   - OD-05 [SL-01 Leap Topology](#od-05-sl-01-leap-topology)
5. [SL-01 Leap Operator — Sidebar](#5-sl-01-leap-operator--sidebar)
6. [Simulation Tables](#6-simulation-tables)
   - S-01 [Linear Traversal Baseline](#s-01-linear-traversal-baseline)
   - S-02 [Phase-Gate Collision Matrix](#s-02-phase-gate-collision-matrix)
   - S-03 [Operator Composition Outcomes](#s-03-operator-composition-outcomes)
   - S-04 [SL-01 Leap Event Log](#s-04-sl-01-leap-event-log)
7. [Grok Feedback Integration](#7-grok-feedback-integration)
8. [Retrospective](#8-retrospective)
9. [Closing & Publication Checklist](#9-closing--publication-checklist)
10. [Appendices](#10-appendices)
    - A [Notation Glossary](#a-notation-glossary)
    - B [Version Diff Summary](#b-version-diff-summary)
    - C [Canon Formatting Reference](#c-canon-formatting-reference)

---

## 1. Overview & Scope

The **Triadic State Representation (TSR) Overlay Diagram Pack** is the authoritative visual-reference companion to the TriadicFrameworks specification. It provides a complete set of overlay diagrams, operator grammar tables, and simulation records that define how states, transitions, and operators behave across all three phases of the TSR model.

### Purpose

This pack serves three audiences:

| Audience | Primary Use |
|---|---|
| **Framework Authors** | Canonical reference during spec authoring and operator design |
| **Implementers** | Ground-truth diagrams for encoding state machines and phase schedulers |
| **Reviewers / Auditors** | Structured baseline for conformance checks and regression validation |

### Scope of v2.6.0-rc

This release candidate introduces:

- **SL-01 Leap Operator** — full specification, sidebar treatment, and topology diagram (OD-05)
- **Grok Feedback Pass** — integrated editorial notes from the Grok review session, resolved inline
- **Operator Grammar v2.2** — formalized BNF notation replacing the v2.1 semi-formal tables
- **Simulation Table S-04** — new event log covering SL-01 leap events across all phase pairs
- **Canon formatting unification** — all sections now conform to TriadicFrameworks Canon Style Guide §4–§7

> **Out of Scope for this release:** Cross-framework adapter specifications, probabilistic state weighting, and multi-agent TSR federation. These are tracked in the v2.7.x roadmap.

---

## 2. Core TSR Architecture

### 2.1 Triadic State Model

The TSR model structures all representational states into a **three-phase lattice**: Generative (Φ₁), Mediative (Φ₂), and Resolvent (Φ₃). Each phase is a distinct ontological register with its own operator set, transition rules, and memory constraints.

```
╔══════════════════════════════════════════════════════════════╗
║                    TSR STATE LATTICE                         ║
╠══════════════════════╦═══════════════════╦═══════════════════╣
║  Φ₁  GENERATIVE      ║  Φ₂  MEDIATIVE   ║  Φ₃  RESOLVENT   ║
║  ─────────────────   ║  ──────────────   ║  ─────────────   ║
║  · Origin encoding   ║  · Tension hold   ║  · Synthesis     ║
║  · Raw state birth   ║  · Cross-phase    ║  · Collapse      ║
║  · Ψ-seed emission   ║    arbitration    ║  · Commitment    ║
║  · No backflow       ║  · Bidirectional  ║  · Terminal or   ║
║                      ║    transit        ║    re-entry gate ║
╠══════════════════════╩═══════════════════╩═══════════════════╣
║  Transit:  Φ₁ → Φ₂ → Φ₃   (standard)                       ║
║            Φ₃ → Φ₁          (re-entry via Γ-gate)           ║
║            Φ₁ ⇒ Φ₃          (SL-01 leap — see § 5)         ║
╚══════════════════════════════════════════════════════════════╝
```

**Key invariants:**

- A state exists in **exactly one phase** at any moment; phase co-residence is undefined behavior.
- Φ₁ has no inbound standard transit; the only legal inbound path is via Γ-gate re-entry from Φ₃.
- Φ₂ is the sole standard bridge between Φ₁ and Φ₃; bypassing Φ₂ requires an explicit leap operator (see SL-01, § 5).

### 2.2 Phase Gate Definitions

Phase gates are typed transition checkpoints. Every inter-phase edge must pass through a declared gate.

| Gate ID | Edge | Type | Guard Condition | Notes |
|---|---|---|---|---|
| **Γ₁₂** | Φ₁ → Φ₂ | Standard | `state.ψ ≥ ψ_min` | Minimum seed energy required |
| **Γ₂₃** | Φ₂ → Φ₃ | Standard | `tension.resolved = true` | Mediative tension must clear |
| **Γ₃₁** | Φ₃ → Φ₁ | Re-entry | `commit.type = REOPEN` | Controlled re-genesis only |
| **Λ₁₃** | Φ₁ ⇒ Φ₃ | Leap (SL-01) | `leap.authorized ∧ Φ₂.bypassed` | Requires SL-01 operator |
| **Γ₂₁** | Φ₂ → Φ₁ | Rollback | `rollback.depth ≤ R_MAX` | Emergency rollback only; audited |

> **Canon note:** Gate IDs use `Γ` (Gamma) for standard/re-entry gates and `Λ` (Lambda) for leap gates. This distinction is load-bearing for parser implementations — do not conflate.

### 2.3 State Encoding Convention

All states in the TSR system are encoded as a **four-tuple**:

```
S = ⟨ id, phase, ψ, τ ⟩

Where:
  id    → Unique state identifier (string, UUID-compatible)
  phase → Phase register: { Φ₁ | Φ₂ | Φ₃ }
  ψ     → Seed potential (float, 0.0–1.0); meaningful only in Φ₁
  τ     → Tension index (float, 0.0–1.0); meaningful only in Φ₂
```

States in Φ₃ carry resolved payloads rather than ψ/τ values; those fields are frozen at entry-time values for audit traceability.

---

## 3. Operator Grammar Reference

### 3.1 Formal Grammar Notation

The TSR operator grammar is specified in **Augmented BNF (ABNF)** following RFC 5234 conventions, extended with TriadicFrameworks phase-annotation syntax.

```abnf
; ── TSR Operator Grammar v2.2 ──────────────────────────────────

program        = *( statement )
statement      = op-expr NEWLINE
op-expr        = primitive-op / compound-op / leap-op

primitive-op   = op-name "(" arg-list ")" [ phase-tag ]
compound-op    = "{" *( op-expr ) "}" [ combinator ]
leap-op        = "SL" "-" leap-id "(" arg-list ")" phase-tag

op-name        = 1*( ALPHA / DIGIT / "_" )
arg-list       = arg *( "," arg )
arg            = literal / state-ref / op-expr

phase-tag      = "@" phase-id
phase-id       = "Φ1" / "Φ2" / "Φ3"

leap-id        = 1*( DIGIT )
combinator     = "|>" / "&>" / "?>"
                ; |> = sequential, &> = parallel, ?> = conditional

literal        = quoted-str / number / bool
state-ref      = "$" 1*( ALPHA / DIGIT / "_" )
quoted-str     = DQUOTE *( VCHAR / SP ) DQUOTE
number         = 1*DIGIT [ "." 1*DIGIT ]
bool           = "true" / "false"
```

### 3.2 Primitive Operators

Primitive operators are atomic, phase-scoped, and non-decomposable at the grammar level.

| Operator | Phase | Signature | Effect | Idempotent |
|---|---|---|---|---|
| `SEED` | Φ₁ | `SEED(id, ψ)` | Instantiates a new state with seed potential ψ | No |
| `EMIT` | Φ₁ | `EMIT($s)` | Propagates state forward through Γ₁₂ | No |
| `HOLD` | Φ₂ | `HOLD($s, τ)` | Sets tension index; suspends forward transit | Yes |
| `ARBIT` | Φ₂ | `ARBIT($s₁, $s₂)` | Resolves tension between two Φ₂ states | No |
| `SYNTH` | Φ₃ | `SYNTH($s)` | Collapses state into resolved payload | No |
| `COMMIT` | Φ₃ | `COMMIT($s, type)` | Finalizes with type `TERMINAL` or `REOPEN` | No |
| `ROLLBACK` | Φ₂ | `ROLLBACK($s, depth)` | Walks state back toward Φ₁ up to `depth` | No |
| `PROBE` | Any | `PROBE($s)` | Read-only state inspection; no side effects | Yes |

### 3.3 Compound Operators

Compound operators compose primitives using the declared combinator semantics.

```
Sequential  ( |> )  — ops execute left-to-right; each receives prior output
Parallel    ( &> )  — ops execute concurrently; outputs merge into state bag
Conditional ( ?> )  — first op evaluates guard; branches to second or third

Examples:

  { SEED("x", 0.7) |> EMIT($x) |> HOLD($x, 0.4) }@Φ₂
      → Seed, emit through gate, hold in Φ₂ with tension 0.4

  { ARBIT($a, $b) &> PROBE($c) }@Φ₂
      → Arbitrate a/b in parallel with probing c

  { PROBE($s) ?> SYNTH($s) | HOLD($s, τ_max) }
      → If s passes probe, synthesize; else max-hold
```

### 3.4 Constraint Rules

The following rules are **enforced by conforming implementations**. Violations must raise a `TSR_CONSTRAINT_VIOLATION` error.

```
CR-01  SEED may only appear in Φ₁ context.
CR-02  SYNTH and COMMIT may only appear in Φ₃ context.
CR-03  ROLLBACK depth must not exceed R_MAX (default: 3).
CR-04  SL-01 (leap) may not be composed inside a sequential
       combinator with HOLD; leap and hold are mutually exclusive
       for the same state in the same expression.
CR-05  ARBIT requires exactly two distinct state-ref arguments;
       self-arbitration ($s, $s) is undefined behavior.
CR-06  A state that has received COMMIT(TERMINAL) is immutable;
       any subsequent operator targeting it must raise
       TSR_IMMUTABLE_STATE.
CR-07  Phase tags on compound ops override inner phase tags for
       gate-check purposes; inner tags remain for documentation.
```

---

## 4. Overlay Diagrams

> **Rendering note:** All diagrams are rendered in UTF-8 box-drawing characters for inline Markdown display. HTML export resolves these to `<figure>` / `<pre class="tsr-diagram">` blocks with syntax highlighting via the TriadicFrameworks CSS bundle. Mermaid equivalents are provided as collapsible alternates where noted.

---

### OD-01: State Transition Matrix

**Purpose:** Full enumeration of legal state transitions across all phase pairs.

```
┌─────────────────────────────────────────────────────────────────────┐
│  OD-01 · STATE TRANSITION MATRIX                          v2.6.0-rc │
├────────────┬────────────┬───────────┬──────────┬────────────────────┤
│  FROM \TO  │    Φ₁      │    Φ₂     │    Φ₃    │  Gate Required     │
├────────────┼────────────┼───────────┼──────────┼────────────────────┤
│  Φ₁        │  ───       │  LEGAL    │  LEAP ¹  │  Γ₁₂ / Λ₁₃        │
│  Φ₂        │  ROLLBACK² │  ───      │  LEGAL   │  Γ₂₁ / Γ₂₃        │
│  Φ₃        │  RE-ENTRY³ │  ILLEGAL  │  ───     │  Γ₃₁               │
├────────────┴────────────┴───────────┴──────────┴────────────────────┤
│  ¹ Leap: requires SL-01 authorization; Φ₂ bypassed (logged)         │
│  ² Rollback: CR-03 depth limit applies; audited event                │
│  ³ Re-entry: requires COMMIT(REOPEN); initiates new Ψ-seed cycle     │
│  ILLEGAL transitions raise TSR_ILLEGAL_TRANSITION                    │
└─────────────────────────────────────────────────────────────────────┘
```

---

### OD-02: Triadic Phase Map

**Purpose:** Spatial representation of phase topology, gate positions, and directional flow.

```
┌─────────────────────────────────────────────────────────────────────────┐
│  OD-02 · TRIADIC PHASE MAP                                   v2.6.0-rc  │
│                                                                          │
│                                                                          │
│    ┌──────────────────┐     Γ₁₂     ┌──────────────────┐               │
│    │                  │ ──────────► │                  │               │
│    │    Φ₁            │             │    Φ₂            │               │
│    │  GENERATIVE      │ ◄────────── │  MEDIATIVE       │               │
│    │                  │  Γ₂₁(R/B)  │                  │               │
│    │  · SEED          │             │  · HOLD          │               │
│    │  · EMIT          │             │  · ARBIT         │               │
│    │                  │             │  · ROLLBACK      │               │
│    └─────────┬────────┘             └────────┬─────────┘               │
│              │                               │ Γ₂₃                     │
│              │  Λ₁₃                          ▼                          │
│              │  (SL-01 Leap)      ┌──────────────────┐                 │
│              └──────────────────► │                  │                 │
│                                   │    Φ₃            │                 │
│                                   │  RESOLVENT       │                 │
│                                   │                  │                 │
│                                   │  · SYNTH         │                 │
│                                   │  · COMMIT        │                 │
│                                   │                  │                 │
│                                   └────────┬─────────┘                 │
│                                            │ Γ₃₁ (Re-entry)           │
│                                            └──────────────────┐        │
│                                                               ▼        │
│                                                        [Φ₁ Re-genesis] │
│                                                                          │
│  Legend:  ──►  Standard transit    ⇒  Leap transit                      │
│           R/B  Rollback only       (R) Re-entry gate                    │
└─────────────────────────────────────────────────────────────────────────┘
```

---

### OD-03: Operator Flow Lattice

**Purpose:** Dependency and ordering lattice showing which operators can precede or follow each other in valid programs.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  OD-03 · OPERATOR FLOW LATTICE                                v2.6.0-rc  │
│                                                                           │
│    SEED ──► EMIT ──► HOLD ──► ARBIT ──► SYNTH ──► COMMIT                │
│      │                │         │                    │                   │
│      │                │         └──► ROLLBACK        │                   │
│      │                │               │              │                   │
│      │                └───────────────┘              │                   │
│      │                                               │                   │
│      └──────── SL-01 ──────────────────────────────►┘                   │
│                 (leap; skips HOLD + ARBIT path)                          │
│                                                                           │
│   ┌─────────────────────────────────────────────────────────────────┐    │
│   │  PROBE  →  any operator (read-only; does not advance lattice)   │    │
│   └─────────────────────────────────────────────────────────────────┘    │
│                                                                           │
│   Valid head operators:   { SEED, PROBE }                                 │
│   Valid tail operators:   { COMMIT, PROBE }                               │
│   Invalid sequences:      HOLD → SEED  (phase regression without R/B)    │
│                           COMMIT → EMIT (post-terminal emission)         │
│                           SL-01 → HOLD  (CR-04 violation)               │
└──────────────────────────────────────────────────────────────────────────┘
```

---

### OD-04: Recursive Depth Chart

**Purpose:** Visualizes the allowed recursion depth for ROLLBACK operations across phase registers, with R_MAX enforcement bands.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  OD-04 · RECURSIVE DEPTH CHART (ROLLBACK)                     v2.6.0-rc  │
│                                                                           │
│  Depth                                                                    │
│    0  ┤  ═══════════════════════════════════════════════ COMMIT point     │
│       │                                                                   │
│    1  ┤  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  Φ₃ boundary    │
│       │                                                                   │
│    2  ┤  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  Φ₂ zone      │
│       │                                                                   │
│    3  ┤  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  Φ₂ floor     │
│       │                                                                   │
│  R_MAX┤  ████████████████████████████████████████████  HARD LIMIT        │
│    =3 │  (CR-03 enforced; depth > 3 → TSR_CONSTRAINT_VIOLATION)          │
│       │                                                                   │
│       │  NOTE: Rollback cannot cross Γ₁₂ (Φ₁ boundary).                 │
│       │  Φ₁ states are read-only once emitted.                           │
│       │  To return to Φ₁: use COMMIT(REOPEN) → Γ₃₁ re-entry.           │
│       │                                                                   │
│  Depth│  0────────1────────2────────3──[R_MAX]                           │
│  axis │          Φ₃       Φ₂      Φ₂-floor                              │
└──────────────────────────────────────────────────────────────────────────┘
```

---

### OD-05: SL-01 Leap Topology

**Purpose:** Detailed topology of the SL-01 leap operator path, including authorization checkpoint, Λ₁₃ gate traversal, audit hook, and Φ₂ bypass record.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  OD-05 · SL-01 LEAP TOPOLOGY                                  v2.6.0-rc  │
│                                                                           │
│   Φ₁ State                                                                │
│   ┌─────────┐                                                             │
│   │  $s     │                                                             │
│   │ (SEEDED)│                                                             │
│   └────┬────┘                                                             │
│        │  SL-01($s, target_id)                                            │
│        ▼                                                                  │
│   ┌─────────────────────────────────────────────────┐                    │
│   │  AUTH CHECKPOINT                                │                    │
│   │  · Verify: leap.authorized = true               │                    │
│   │  · Verify: $s.phase = Φ₁                        │                    │
│   │  · Verify: target_id resolves to valid Φ₃ slot  │                    │
│   │  · Fail → TSR_LEAP_UNAUTHORIZED                 │                    │
│   └────────────────────┬────────────────────────────┘                    │
│                        │ PASS                                             │
│                        ▼                                                  │
│   ┌─────────────────────────────────────────────────┐                    │
│   │  Φ₂ BYPASS RECORD (audit hook)                  │                    │
│   │  · Write: bypass_log{ state: $s.id,             │                    │
│   │                       gate: Λ₁₃,                │                    │
│   │                       Φ₂_bypassed: true,        │                    │
│   │                       timestamp: <now> }         │                    │
│   │  · Tension index τ frozen at 0.0 (no mediation) │                    │
│   └────────────────────┬────────────────────────────┘                    │
│                        │                                                  │
│                        ▼                                                  │
│                   Λ₁₃  GATE                                              │
│                   ══════════                                              │
│                        │                                                  │
│                        ▼                                                  │
│   ┌─────────────────────────────────────────────────┐                    │
│   │  Φ₃ SLOT: target_id                             │                    │
│   │  · $s arrives with ψ intact, τ=0.0              │                    │
│   │  · SYNTH and COMMIT are now available           │                    │
│   │  · SL-01 call is logged in Φ₃ arrival record   │                    │
│   └─────────────────────────────────────────────────┘                    │
│                                                                           │
│  Dashed path (standard, bypassed):                                        │
│  Φ₁ ·─ ─ ─ Γ₁₂ ─ ─ ─► Φ₂ ─ ─ ─ Γ₂₃ ─ ─ ─► Φ₃  (not taken by SL-01)  │
│                                                                           │
│  CR-04 reminder: SL-01 + HOLD on same state = constraint violation.      │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 5. SL-01 Leap Operator — Sidebar

> **Canon Sidebar Format · SB-SL01**
> *Sidebars provide deep-reference context for a single operator or concept. They are rendered as offset panels in HTML export.*

---

```
╔══════════════════════════════════════════════════════════════════════════╗
║  ◈  SL-01 LEAP OPERATOR  ·  SIDEBAR REFERENCE                           ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  DESIGNATION    SL-01  (State Leap, generation 01)                       ║
║  PHASE SCOPE    Φ₁ → Φ₃  (Generative-to-Resolvent leap)                 ║
║  GATE           Λ₁₃  (Lambda gate; leap-class only)                      ║
║  INTRODUCED     TSR Grammar v2.2  (this release)                         ║
║                                                                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║  SIGNATURE                                                               ║
║                                                                          ║
║    SL-01( state_ref, target_id [, options] ) @Φ₃                        ║
║                                                                          ║
║    state_ref   →  $-prefixed reference to the Φ₁ state to leap          ║
║    target_id   →  Identifier of the Φ₃ destination slot                 ║
║    options     →  Optional map:                                          ║
║                   { audit: bool,       // default: true (recommended)   ║
║                     τ_freeze: float,   // freeze τ value; default 0.0   ║
║                     memo: string }     // freeform leap annotation       ║
║                                                                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║  PRECONDITIONS                                                           ║
║                                                                          ║
║  ✓  leap.authorized = true   (set by framework host or policy engine)   ║
║  ✓  $state_ref.phase = Φ₁   (leap only valid from Generative phase)     ║
║  ✓  target_id is a registered, unoccupied Φ₃ slot                       ║
║  ✓  $state_ref has NOT received EMIT (pre-emission leap only)            ║
║                                                                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║  POSTCONDITIONS                                                          ║
║                                                                          ║
║  →  $state_ref.phase transitions to Φ₃                                  ║
║  →  Φ₂ bypass_log entry written (immutable)                             ║
║  →  Λ₁₃ gate traversal recorded in audit trail                          ║
║  →  $state_ref.τ frozen at options.τ_freeze (default 0.0)               ║
║  →  SYNTH and COMMIT become available on $state_ref                     ║
║                                                                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║  ERRORS & EXCEPTIONS                                                     ║
║                                                                          ║
║  TSR_LEAP_UNAUTHORIZED    leap.authorized flag not set                   ║
║  TSR_INVALID_LEAP_SOURCE  $state_ref not in Φ₁                          ║
║  TSR_SLOT_OCCUPIED        target_id already holds an active Φ₃ state    ║
║  TSR_CONSTRAINT_VIOLATION CR-04: SL-01 composed with HOLD on same $s   ║
║  TSR_POST_EMIT_LEAP       $state_ref already passed through EMIT        ║
║                                                                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║  USAGE EXAMPLE                                                           ║
║                                                                          ║
║    SEED("alpha", 0.9) @Φ₁                                               ║
║    SL-01($alpha, "slot:Φ₃-007",                                         ║
║           { audit: true, memo: "emergency resolution path" }) @Φ₃       ║
║    SYNTH($alpha) @Φ₃                                                    ║
║    COMMIT($alpha, TERMINAL) @Φ₃                                         ║
║                                                                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║  DESIGN RATIONALE                                                        ║
║                                                                          ║
║  SL-01 was introduced to address scenarios where mediative arbitration   ║
║  (Φ₂) would introduce unacceptable latency or where the state's         ║
║  Ψ-potential is sufficient to commit directly without tension            ║
║  resolution. Examples include:                                           ║
║                                                                          ║
║    · High-confidence synthetic states (ψ ≥ 0.9) with no competing       ║
║      Φ₂ states requiring arbitration                                     ║
║    · Time-critical commitment paths in real-time TSR schedulers          ║
║    · Framework bootstrap sequences where Φ₂ has not yet initialized     ║
║                                                                          ║
║  The mandatory audit hook ensures that leap usage is never invisible     ║
║  to conformance checkers or retrospective analysis.                      ║
║                                                                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║  WARNINGS & ANTI-PATTERNS                                                ║
║                                                                          ║
║  ⚠  Do not use SL-01 as a general optimization. The absence of Φ₂       ║
║     arbitration means no tension resolution occurs; states that carry    ║
║     hidden conflicts may commit with unresolved contradictions.          ║
║                                                                          ║
║  ⚠  audit: false is permitted but strongly discouraged. Disabling the   ║
║     audit hook makes leap events invisible to conformance tools.         ║
║                                                                          ║
║  ⚠  SL-01 does not inherit any HOLD state set on $s in a prior          ║
║     expression; if HOLD was applied before leap authorization, the       ║
║     implementation must raise TSR_CONSTRAINT_VIOLATION (CR-04).         ║
║                                                                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║  SEE ALSO                                                                ║
║                                                                          ║
║  · OD-05: SL-01 Leap Topology                                            ║
║  · § 3.4 CR-04 Constraint Rule                                           ║
║  · Simulation Table S-04: SL-01 Leap Event Log                          ║
║  · TriadicFrameworks Spec §9.4 "Leap Authorization Policy"               ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## 6. Simulation Tables

Simulation tables record the outputs of test runs executed against the TSR reference implementation. All runs use the canonical test harness at `tools/tsr-sim/run.sh`.

> **Environment:** TSR Simulator v0.14.2 · Seed RNG: fixed (42) · R_MAX: 3

---

### S-01: Linear Traversal Baseline

Tests the standard Φ₁ → Φ₂ → Φ₃ path with no operators beyond the minimum required set.

| Run | State ID | ψ-seed | Γ₁₂ Pass | τ-hold | ARBIT | Γ₂₃ Pass | SYNTH | COMMIT | Result |
|---|---|---|---|---|---|---|---|---|---|
| S01-R01 | `alpha-001` | 0.75 | ✓ | 0.30 | — | ✓ | ✓ | TERMINAL | PASS |
| S01-R02 | `alpha-002` | 0.40 | ✓ | 0.80 | — | ✓ | ✓ | TERMINAL | PASS |
| S01-R03 | `alpha-003` | 0.10 | ✗ | — | — | — | — | — | FAIL: ψ < ψ_min |
| S01-R04 | `alpha-004` | 0.90 | ✓ | 0.50 | ✓ | ✓ | ✓ | REOPEN | PASS → re-genesis |
| S01-R05 | `alpha-005` | 0.65 | ✓ | 1.00 | ✗ | ✗ | — | — | BLOCKED: tension unresolved |

**Notes:**
- S01-R03 establishes `ψ_min = 0.15` as the baseline threshold for Γ₁₂ passage.
- S01-R05 demonstrates unresolved tension blocking Γ₂₃; ARBIT required before further transit.
- S01-R04 confirms REOPEN triggers Γ₃₁ re-entry and initiates a clean Φ₁ re-genesis.

---

### S-02: Phase-Gate Collision Matrix

Tests what happens when illegal transitions are attempted; verifies error codes.

| Attempt | From | To | Gate Used | Expected Error | Observed | Match |
|---|---|---|---|---|---|---|
| S02-T01 | Φ₂ | Φ₁ | *(none)* | `TSR_ILLEGAL_TRANSITION` | `TSR_ILLEGAL_TRANSITION` | ✓ |
| S02-T02 | Φ₃ | Φ₂ | *(none)* | `TSR_ILLEGAL_TRANSITION` | `TSR_ILLEGAL_TRANSITION` | ✓ |
| S02-T03 | Φ₁ | Φ₃ | Λ₁₃ (no auth) | `TSR_LEAP_UNAUTHORIZED` | `TSR_LEAP_UNAUTHORIZED` | ✓ |
| S02-T04 | Φ₃ | Φ₃ | *(self)* | `TSR_ILLEGAL_TRANSITION` | `TSR_ILLEGAL_TRANSITION` | ✓ |
| S02-T05 | Φ₁ | Φ₁ | *(self)* | `TSR_ILLEGAL_TRANSITION` | `TSR_ILLEGAL_TRANSITION` | ✓ |
| S02-T06 | Φ₂ | Φ₁ | Γ₂₁ (depth=4) | `TSR_CONSTRAINT_VIOLATION` (CR-03) | `TSR_CONSTRAINT_VIOLATION` | ✓ |

**Notes:** All 6 collision tests pass. Error codes are canonical and stable.

---

### S-03: Operator Composition Outcomes

Tests compound operator compositions for correctness, including combinator behaviors.

| Run | Expression | Expected Outcome | Observed | Match |
|---|---|---|---|---|
| S03-C01 | `{ SEED("x",0.7) \|> EMIT($x) \|> HOLD($x,0.4) }` | $x in Φ₂, τ=0.4 | $x in Φ₂, τ=0.4 | ✓ |
| S03-C02 | `{ ARBIT($a,$b) &> PROBE($c) }` | Both run in parallel; $c unchanged | Confirmed | ✓ |
| S03-C03 | `{ PROBE($s) ?> SYNTH($s) \| HOLD($s,1.0) }` | Guard passes → SYNTH | SYNTH executed | ✓ |
| S03-C04 | `{ SL-01($x,"slot-03") \|> HOLD($x,0.5) }` | `TSR_CONSTRAINT_VIOLATION` (CR-04) | CR-04 raised | ✓ |
| S03-C05 | `COMMIT($x, TERMINAL); EMIT($x)` | `TSR_IMMUTABLE_STATE` (CR-06) | CR-06 raised | ✓ |
| S03-C06 | `{ SEED("y",0.8) \|> EMIT($y) \|> SYNTH($y) }` | `TSR_ILLEGAL_TRANSITION` (Φ₁→Φ₃ direct) | Error raised | ✓ |

**Notes:**
- S03-C04 confirms CR-04 enforcement for SL-01 + HOLD composition.
- S03-C06 confirms that SYNTH without SL-01 or Φ₂ traversal is rejected.

---

### S-04: SL-01 Leap Event Log

New in v2.6.0-rc. Records all SL-01 leap executions from the simulation suite with audit trail verification.

| Run | State ID | ψ | auth | target_id | τ_freeze | audit | Leap Result | Φ₂ Bypass Logged | Audit Trail Valid |
|---|---|---|---|---|---|---|---|---|---|
| S04-L01 | `leap-001` | 0.92 | ✓ | `slot:Φ₃-001` | 0.0 | true | PASS | ✓ | ✓ |
| S04-L02 | `leap-002` | 0.85 | ✓ | `slot:Φ₃-002` | 0.0 | true | PASS | ✓ | ✓ |
| S04-L03 | `leap-003` | 0.70 | ✗ | `slot:Φ₃-003` | — | — | FAIL: LEAP_UNAUTHORIZED | N/A | N/A |
| S04-L04 | `leap-004` | 0.95 | ✓ | `slot:Φ₃-004` | 0.2 | false | PASS | ✓ | ✗ (disabled) |
| S04-L05 | `leap-005` | 0.88 | ✓ | `slot:Φ₃-001` | 0.0 | true | FAIL: TSR_SLOT_OCCUPIED | N/A | N/A |
| S04-L06 | `leap-006` | 0.91 | ✓ | `slot:Φ₃-006` | 0.0 | true | PASS → SYNTH → COMMIT(TERMINAL) | ✓ | ✓ |

**Post-run verification:**
- All PASS runs correctly deposited $state in Φ₃ with ψ intact and τ at declared freeze value.
- S04-L04 (`audit: false`) is flagged by the conformance checker with `WARN_AUDIT_DISABLED`.
- S04-L06 demonstrates the full SL-01 → SYNTH → COMMIT pipeline completing cleanly.

---

## 7. Grok Feedback Integration

This section documents the editorial and structural feedback received from the Grok review session conducted during the v2.6.0 development cycle. All items are resolved or explicitly deferred.

---

### 7.1 Feedback Summary

| Item ID | Category | Feedback | Resolution | Status |
|---|---|---|---|---|
| GF-01 | Clarity | "Phase gate naming inconsistent between §2.2 and OD-01" | Unified to `Γ`/`Λ` convention throughout; CR-07 added to grammar | ✅ Resolved |
| GF-02 | Completeness | "SL-01 needs a dedicated sidebar — current inline treatment is insufficient" | Full sidebar added as § 5 with SB-SL01 format | ✅ Resolved |
| GF-03 | Correctness | "CR-04 constraint was described but not enforced in simulation S03" | S03-C04 test case added; CR-04 enforcement confirmed | ✅ Resolved |
| GF-04 | Formatting | "Diagram boxes inconsistent width across OD-01 through OD-04" | All diagram widths normalized to 74-char inner width | ✅ Resolved |
| GF-05 | Completeness | "No simulation data for SL-01 leap events" | Simulation Table S-04 added | ✅ Resolved |
| GF-06 | Correctness | "ROLLBACK depth=3 in S-01 should show Φ₂-floor, not Φ₁ entry" | OD-04 corrected; depth-3 labeled Φ₂-floor | ✅ Resolved |
| GF-07 | Architecture | "Consider whether Φ₃ → Φ₂ ILLEGAL is load-bearing or just convention" | Confirmed load-bearing: CR-02 (SYNTH/COMMIT Φ₃-only) requires it | ✅ Resolved (documented) |
| GF-08 | Roadmap | "SL-02 and SL-03 leap variants mentioned in passing — formalize or remove" | Removed all SL-02/SL-03 references; deferred to v2.7.x roadmap | ✅ Resolved |
| GF-09 | Style | "τ_max undefined in S01-R05 narrative" | Replaced with "tension unresolved" (τ=1.0 = max hold) | ✅ Resolved |
| GF-10 | Deferred | "Add formal semantics for PROBE composing with leap operators" | Deferred — tracked in GitHub Issue #441 | 🕐 Deferred |

### 7.2 Structural Changes Driven by Grok Review

The Grok review session prompted three structural additions not present in v2.5.x:

1. **SL-01 Sidebar (§ 5)** — Elevated from a footnote reference to a full canon sidebar block, per GF-02.
2. **Constraint Rule CR-07** — Added to the grammar to formally document phase-tag override semantics, resolving the ambiguity surfaced in GF-01.
3. **Simulation Table S-04** — Entirely new table, added per GF-05 to provide empirical coverage of SL-01 behavior.

---

## 8. Retrospective

### 8.1 Development Cycle Summary — v2.5.x → v2.6.0-rc

| Milestone | Date | Notes |
|---|---|---|
| v2.5.0 branch opened | 2026-06-02 | Operator grammar formalization initiated |
| v2.5.1 patch | 2026-07-18 | OD-03 labeling fix; S-04 stub added |
| Grok review session | 2026-08-12 | 10 items logged; all addressed except GF-10 |
| SL-01 sidebar drafted | 2026-08-20 | First full sidebar format per SB canon |
| v2.6.0-rc cut | 2026-09-03 | This document |

### 8.2 What Worked

- **ABNF formalization** — Moving from the v2.1 semi-formal tables to ABNF in v2.2 dramatically reduced reviewer ambiguity. GF-01 through GF-03 were all symptoms of under-specified grammar; they dissolved once ABNF was complete.
- **Simulation-first verification** — Running simulation tables before finalizing diagram text caught the OD-04 Φ₂-floor mislabeling (GF-06) before publication.
- **Sidebar format (SB-SL01)** — The canon sidebar box format proved immediately useful for SL-01. It will be adopted for future complex operator references.

### 8.3 What to Improve

- **Earlier Grok engagement** — The Grok review caught issues that should have been caught in the author pass. Consider scheduling review sessions at draft stage, not RC stage.
- **SL-02/SL-03 scope creep** — Informal references to future leap variants crept into multiple sections and required cleanup (GF-08). Future operators should not appear by name in a document until they have a formal spec.
- **Simulation coverage timing** — S-04 was added reactively (GF-05). Simulation tables for new operators should be authored alongside the operator spec, not after.

### 8.4 Open Issues

| Issue | Tracker | Priority | Target |
|---|---|---|---|
| Formal semantics for PROBE + leap composition | GitHub #441 | Medium | v2.7.0 |
| SL-02 and SL-03 leap variant specifications | GitHub #442 | Low | v2.7.x |
| HTML export CSS for sidebar SB format | GitHub #443 | High | v2.6.0 release |
| Leap authorization policy engine integration guide | GitHub #444 | Medium | v2.7.0 |

---

## 9. Closing & Publication Checklist

### 9.1 Checklist

Before promoting this RC to stable release, all items below must be confirmed:

- [x] All overlay diagrams (OD-01 through OD-05) present and normalized to 74-char width
- [x] Operator Grammar v2.2 in ABNF notation with all constraint rules (CR-01 through CR-07)
- [x] SL-01 sidebar (§ 5) in canon SB format with preconditions, postconditions, errors, and design rationale
- [x] Simulation Tables S-01 through S-04 complete with run logs and notes
- [x] Grok feedback table (§ 7.1) with all 10 items addressed or deferred with issue references
- [x] Retrospective (§ 8) complete
- [x] Appendix A (Notation Glossary) complete
- [x] Appendix B (Version Diff Summary) complete
- [x] Appendix C (Canon Formatting Reference) complete
- [x] YAML frontmatter metadata block present and valid
- [x] All internal cross-references resolved
- [ ] HTML export tested against TriadicFrameworks CSS bundle (GitHub #443)
- [ ] Final proofreading pass by secondary author
- [ ] PR submitted to `docs/Research/` with changelog entry

### 9.2 RC to Stable Gate

This document transitions from RC to stable when:

1. GitHub #443 (HTML export CSS for SB sidebar format) is closed
2. HTML export is confirmed rendering correctly in the TriadicFrameworks preview environment
3. One secondary author signs off in the PR review

---

## 10. Appendices

---

### A. Notation Glossary

| Symbol / Term | Definition |
|---|---|
| `Φ₁` | Generative phase — origin of all states |
| `Φ₂` | Mediative phase — tension arbitration and transit bridge |
| `Φ₃` | Resolvent phase — synthesis, commitment, and termination |
| `Γ` | Standard / re-entry gate prefix (Greek Capital Gamma) |
| `Λ` | Leap gate prefix (Greek Capital Lambda) |
| `ψ` (psi) | Seed potential: energy carried by a Φ₁ state (0.0–1.0) |
| `τ` (tau) | Tension index: mediation load on a Φ₂ state (0.0–1.0) |
| `ψ_min` | Minimum seed potential required to pass Γ₁₂ (default: 0.15) |
| `R_MAX` | Maximum ROLLBACK recursion depth (default: 3) |
| `SL-01` | State Leap operator, generation 01; Φ₁ → Φ₃ direct path |
| `ABNF` | Augmented Backus-Naur Form (RFC 5234) |
| `bypass_log` | Immutable audit record written by every SL-01 execution |
| `CR-nn` | Constraint Rule, numbered; enforced by conforming implementations |
| `GF-nn` | Grok Feedback item, numbered; tracked in this document |
| `OD-nn` | Overlay Diagram, numbered |
| `S-nn` | Simulation Table, numbered |
| `SB-nn` | Sidebar block, identified by subject code |
| `TERMINAL` | COMMIT type: state is finalized, immutable, no re-entry |
| `REOPEN` | COMMIT type: state initiates Γ₃₁ re-genesis path |

---

### B. Version Diff Summary

| Section | v2.5.1 | v2.6.0-rc | Change Type |
|---|---|---|---|
| § 1 Scope | Static list | Added SL-01, Grok pass, grammar v2.2 | Expanded |
| § 2.2 Gates | Γ₁₂, Γ₂₃, Γ₃₁ only | Added Λ₁₃, Γ₂₁ | New entries |
| § 3 Grammar | Semi-formal tables (v2.1) | Full ABNF (v2.2) + CR-07 | Replaced |
| OD-01 | Present | Width normalized | Minor fix |
| OD-02 | Present | Λ₁₃ and SL-01 path added | Updated |
| OD-03 | Present | SL-01 lattice path added | Updated |
| OD-04 | Present | Φ₂-floor label corrected (GF-06) | Bug fix |
| OD-05 | Not present | New — SL-01 Leap Topology | **New** |
| § 5 Sidebar | Not present | New — SL-01 canon sidebar | **New** |
| S-01 | Present | Minor note additions | Minor |
| S-02 | Present | No change | — |
| S-03 | Present | C04, C05, C06 added | Expanded |
| S-04 | Not present | New — SL-01 Leap Event Log | **New** |
| § 7 Grok Feedback | Not present | New section | **New** |
| § 8 Retrospective | Stub only | Fully written | Expanded |

---

### C. Canon Formatting Reference

This document adheres to **TriadicFrameworks Canon Style Guide §4–§7**. Key conventions:

| Element | Format Rule |
|---|---|
| Phase identifiers | `Φ₁`, `Φ₂`, `Φ₃` — Unicode subscript numerals; never `Phi1` or `P1` |
| Gate identifiers | `Γ` + subscript pair (e.g., `Γ₁₂`); `Λ` for leap gates |
| Operator names | ALL_CAPS in prose; lowercase in ABNF grammar rules |
| State references | `$`-prefixed lowercase identifiers (e.g., `$alpha`) |
| Diagram width | 74-char inner content width; 76-char total with box frame |
| Diagram header | `OD-nn · TITLE` right-aligned version tag at 74th char boundary |
| Sidebar format | Double-line box (`╔╗╚╝`); section headers centered in `║` rows |
| Constraint rules | `CR-nn` in monospace; full text block-quoted under § 3.4 |
| Error codes | `TSR_SCREAMING_SNAKE_CASE` in monospace |
| Footnotes | Numbered superscripts `¹ ² ³` inside diagram boxes; prose below |
| Changelog | YAML block in frontmatter; reverse-chronological |
| Cross-references | `§ n.m` for section; `OD-nn`, `S-nn`, `SB-nn` for diagram/table/sidebar |

---

<!-- ============================================================
     END OF DOCUMENT
     TSR Overlay Diagram Pack · v2.6.0-rc
     TriadicFrameworks Canon Document
     Generated: 2026-09-03
     ============================================================ -->
