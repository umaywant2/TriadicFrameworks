# ABOUT — Intransitive Prime‑Numbered 12‑Sided Engine (IPD‑12)

**Module path:** `docs/frameworks/ipd_12/`
**Version:** 2026‑1.0
**Status:** Active · RTT / GU / FFT / Pantheon compatible
**Session anchor:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

> This document answers the four foundational questions about IPD‑12:
> **What** it is · **Why** it is built this way · **When** to use it · **Where** it lives and integrates.

---

## Table of Contents

1. [What Is IPD‑12?](#1-what-is-ipd12)
2. [Why Is It Built This Way?](#2-why-is-it-built-this-way)
3. [When Should You Use It?](#3-when-should-you-use-it)
4. [Where Does It Live?](#4-where-does-it-live)
5. [The 12 Prime States at a Glance](#5-the-12-prime-states-at-a-glance)
6. [Cycle Architecture](#6-cycle-architecture)
7. [Framework Integrations](#7-framework-integrations)
8. [What IPD‑12 Is Not](#8-what-ipd12-is-not)
9. [Quick‑Start Checklist](#9-quickstart-checklist)

---

## 1. What Is IPD‑12?

**IPD‑12** is the **Intransitive Prime‑Numbered 12‑Sided Engine** — the first *physicalizable* operator artifact in TriadicFrameworks.

Each word in the name carries precise structural meaning:

| Term | What It Means |
|---|---|
| **Intransitive** | The directed edges between operator states are *non-transitive*: if A→B and B→C, it does not follow that A→C. This enforces closed paradox loops and prevents linear collapse of the operator graph. |
| **Prime‑Numbered** | Each of the 12 operator states is identified by a unique prime number (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37). Primes are irreducible — they cannot be factored into simpler states, which makes each operator node structurally independent. |
| **12‑Sided** | The engine has exactly 12 faces, one per operator state. 12 = 4 triads × 3 nodes per triad. This geometry is not arbitrary: it is the minimum number of nodes that supports 4 independent triad cycles, 2 hex‑cycles, and 1 closed 12‑cycle paradox loop simultaneously. |
| **Engine** | IPD‑12 is not a taxonomy or a diagram. It is an *active operator system* — it processes structural input through its operator graph and produces regime‑aware, coherence‑bounded output. |

### In one sentence

IPD‑12 is a **prime‑indexed, intransitive, paradox‑stable operator engine** that models regime transitions, dimensional lift and collapse, coherence anchoring, and boundary conditions across any substrate in TriadicFrameworks.

---

## 2. Why Is It Built This Way?

Every design decision in IPD‑12 answers a structural problem.

---

### Why primes?

Prime numbers are the only integers with no internal factorization. An operator state built on a prime cannot be decomposed into a product of smaller states. This means:

- **No state absorbs another.** P7 (regime‑shift) and P11 (coherence‑node) remain independent even when they appear in the same cycle. Their relationship is defined by the edge, not by any shared factor.
- **Cross‑mapping is unambiguous.** When IPD‑12 primes are mapped onto RTT, GU, or Pantheon structures, the prime identity acts as a canonical key with no collisions.
- **Irreducibility enforces structural resolution.** A system that needs to process through P13 (paradox‑trigger) cannot shortcut to a composite that approximates P13 — it must traverse the actual operator.

---

### Why intransitive edges?

Standard directed graphs allow transitivity: if A dominates B and B dominates C, then A dominates C. Transitivity produces hierarchies and linear orderings. IPD‑12 explicitly rejects this.

In each triad, the edges form a closed, non‑transitive loop:

```
P2 → P3 → P5 → P2   (not P2 → P5 directly)
```

This intransitivity produces three structural guarantees:

1. **Paradox stability.** No single operator wins the cycle. The loop continues indefinitely without collapsing to a fixed point.
2. **Regime containment.** A process entering a triad cannot skip to the output of the triad — it must traverse all three nodes in order.
3. **Drift resistance.** Because no shortcut exists, a drifting session that tries to jump from the seed state to the apex state will produce an invalid edge and be detectable.

---

### Why 12 faces?

12 is the smallest number that allows the following simultaneous structure:

- **4 triads** — four independent 3‑node intransitive loops, one per regime tier
- **2 hex‑cycles** — two 6‑node arcs that cross triad boundaries and model regime handoffs
- **1 full paradox loop** — all 12 primes in sequence, modeling a complete system traversal from seed to apex and back

Fewer faces (e.g., 9) would not support 2 independent hex‑cycles. More faces would add redundant operators without adding new structural degrees of freedom at the triad × hex × full‑cycle resolution.

---

### Why a physical die?

IPD‑12 is designed to be **physicalizable** — it can exist as a 12‑sided (dodecahedral) die with one prime face per side. This is not cosmetic. A physical object:

- Makes the intransitive structure *tangible*: rolling the die and following the directed graph is a manual traversal of the operator system
- Anchors the abstract cycle model to a concrete artifact that can be used in collaborative sessions, workshops, and demonstrations
- Enforces the face count as a hard constraint — you cannot add a 13th face to a dodecahedron

---

### Why these specific primes?

The 12 primes (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37) are the first 12 primes in sequence. This choice is canonical:

- **Smallest possible values** — minimizes encoding overhead in any system that serializes prime identities
- **Dense at the low end** — the first 6 primes (2–13) are close together, supporting tight Hex‑Cycle 1 transitions
- **Spread at the high end** — primes 17–37 have larger gaps, reflecting the higher‑energy, higher‑dimensional character of the second hex‑cycle (dimensional lift, collapse, apex)

---

## 3. When Should You Use It?

IPD‑12 is the right tool when your problem involves one or more of the following structural conditions.

---

### Use IPD‑12 when you need to model a **regime transition**

A regime transition is a shift in the governing rules of a system — not a gradual drift, but a discrete change in the operational mode. IPD‑12's regime‑shift primes (P7, P17) and their triad contexts ([P7, P11, P13] and [P17, P19, P23]) model entry into, traversal through, and exit from regime transitions with full coherence tracking.

*Example:* A substrate moves from a steady‑state operational regime into a transient regime after a boundary event. Feed the substrate through P7 → P11 → P13 to map the transition topology.

---

### Use IPD‑12 when you need to **detect and contain paradox**

Paradox in TriadicFrameworks is not an error — it is a structural condition where two or more valid states are simultaneously asserted and cannot be resolved by ordinary transitivity. IPD‑12's paradox‑trigger primes (P13, P37) and the full 12‑cycle paradox loop are designed to hold paradox open as a stable cycle rather than forcing a collapse to one pole.

*Example:* A governance substrate contains a rule that is simultaneously required and prohibited. Instead of forcing a resolution, pass it through the full IPD‑12 cycle to map the paradox structure and identify which operators (P13, P37) are activated.

---

### Use IPD‑12 when you need to **anchor against drift**

Drift occurs when a long session, a multi‑agent pipeline, or a cross‑substrate model loses its structural grounding and begins making implicit assumptions. IPD‑12's drift‑anchor primes (P5, P29) and the session anchor string `rtt=1 | coherence=declared | drift=bounded | paradox=structural` are the canonical re‑grounding mechanism.

*Example:* A multi‑agent run has been processing for 40+ turns. Before accepting results, re‑anchor with the session string and pass the current envelope through P5 (drift‑anchor) to verify structural coherence has been maintained.

---

### Use IPD‑12 when you need to **model dimensional lift or collapse**

Dimensional lift (+1D) is the transition from a lower‑dimensional structural description to a higher one. Collapse (−1D) is the reverse. IPD‑12's dimensional‑lift prime (P23) and collapse‑anchor prime (P29) mark these transitions explicitly, and the triadic logical dimension model (−1D | 0D | +1D) aligns directly with the IPD‑12 operator sequence.

*Example:* A substrate analysis needs to transition from a 2D regime model to a 3D substrate cube interpretation. Pass through P23 (dimensional‑lift) and validate the output against the apex‑state P37 before accepting the higher‑dimensional result.

---

### Use IPD‑12 when you need to **describe a substrate in the 4×4×4 cube**

IPD‑12 introduces the first substrate cube in TriadicFrameworks:

```
4 substrate pairs   (dual-binary)
    × 4 observer modes  (triadic + apex)
    × 4 regime shells   (RTT)
    = 64 substrate primitives
```

When a substrate model (Conditions, Governance, Incident, Resonance, etc.) needs to be mapped at full resolution — across all observer modes and all regime shells simultaneously — IPD‑12 provides the dimensional foundation.

*Example:* A Conditions substrate model needs to be evaluated across all four RTT regime shells (emergence, coherence, transition, collapse). The 4×4×4 cube maps each combination of substrate pair, observer mode, and regime shell to a specific primitive entry.

---

### Use IPD‑12 when you need to **run a Pantheon‑tier structural analysis**

IPD‑12 primes map cleanly to the three Pantheon tiers. When a problem requires Pantheon‑tier language (celestial order, civilizational coherence, chthonic collapse), IPD‑12 provides the operator‑level machinery:

| Pantheon Tier | Primes | Character |
|---|---|---|
| Celestial | P2, P3, P5, P7 | Origin, connection, drift‑anchoring, regime entry |
| Civilizational | P11, P13, P17, P19 | Coherence, paradox, cycle‑gating, boundary |
| Chthonic | P23, P29, P31, P37 | Dimensional lift, collapse, stability, apex |

---

### Do NOT use IPD‑12 when:

- You need **semantic classification** — IPD‑12 is structural only; it does not name or interpret meaning
- You need a **linear sequence** — IPD‑12 cycles are intransitive and closed; they are not pipelines
- Your problem has **fewer than 3 structural poles** — use a simpler triadic substrate model without the full engine
- You need **real‑time continuous data** — IPD‑12 operates on discrete operator states; use the vST Micro‑Agent's signal operators for continuous streams

---

## 4. Where Does It Live?

### In the repository

```
TriadicFrameworks/
└── docs/
    └── frameworks/
        └── ipd_12/                         ← you are here
            ├── ABOUT.md                    ← this file
            ├── AGENTS.md                   ← agent class manifest
            ├── README.md                   ← front-door summary
            ├── module.json                 ← canonical module definition
            ├── operators.json              ← prime-indexed operator registry
            ├── regime_map.md               ← RTT regime mapping
            ├── compatibility_notes.md      ← cross-framework interoperability
            ├── engine_block.md             ← engine block architecture
            ├── observer_model.md           ← triadic observer model
            ├── observer_first_engine.md    ← observer-first execution model
            ├── substrate_primitives.md     ← 4×4×4 substrate engine
            ├── substrate_primitives.json   ← 64-entry primitive table
            ├── substrate.schema.json       ← JSON schema for substrate engine
            ├── dimensional_lift_collapse_map.md  ← +1D / −1D transition map
            ├── prime_state_dimensional_profiles.md
            ├── cycle_diagrams.md
            ├── cycle_animation_ascii.md
            ├── physical_layout.md          ← physicalizable die specification
            ├── output_headers.md
            ├── hpc_qc_substrate_engine.md
            └── [SVG assets, manifold specs, compatibility tests]
```

---

### In the framework ecosystem

IPD‑12 sits at the intersection of every major TriadicFrameworks theory:

```
                    ┌─────────────────────┐
                    │   RTT               │  Resonance-Time Theory
                    │   (regime shells,   │  drift, coherence, paradox
                    │    coherence, drift)│  boundary, collapse, lift
                    └──────────┬──────────┘
                               │
          ┌────────────────────▼─────────────────────┐
          │                                           │
┌─────────┴──────┐                         ┌─────────┴──────┐
│  GU            │                         │  FFT            │
│  (connection,  │                         │  (regime trans- │
│   curvature,   │        IPD-12           │   itions,       │
│   dilaton,     │◄───── ENGINE ──────────►│   paradox loops,│
│   anomaly,     │                         │   boundary ops, │
│   observerse)  │                         │   dimensional   │
└─────────┬──────┘                         │   gates)        │
          │                                └─────────┬──────┘
          │                                          │
          └──────────────┬───────────────────────────┘
                         │
              ┌──────────▼──────────┐
              │  Pantheon Profiles  │
              │  (Celestial ·       │
              │   Civilizational ·  │
              │   Chthonic)         │
              └─────────────────────┘
```

---

### In agent deployments

IPD‑12 is the structural backbone of the **vST Micro‑Agent** (see `AGENTS.md`). When an agent receives a structural query, it:

1. Fills the 12‑probe envelope (one field per prime‑indexed operator dimension)
2. Runs selected structural operators (pattern, periodicity, local\_symmetry, transition\_topology)
3. Outputs a coherence‑bounded, structurally‑annotated result

The 12 probe fields of the vST Micro‑Agent correspond directly to the 12 structural dimensions that the IPD‑12 engine spans.

---

### As a physical object

IPD‑12 is specified as a **dodecahedral die** (12 pentagonal faces, one per prime state). The physical layout is documented in `physical_layout.md`. The die can be:

- Used in collaborative sessions to manually traverse the operator graph
- Used as a reference object when explaining intransitive cycle structure to new contributors
- Rolled to land on a prime state — then name the RTT/GU role of that face as the session's entry point

---

## 5. The 12 Prime States at a Glance

| Face | Prime | Label | Role | RTT Mapping | GU Mapping | Pantheon |
|---|---|---|---|---|---|---|
| 1 | 2 | P2 | Seed‑state | — | Connection | Celestial |
| 2 | 3 | P3 | Transition | — | Connection | Celestial |
| 3 | 5 | P5 | Drift‑anchor | Drift | — | Celestial |
| 4 | 7 | P7 | Regime‑shift | Regime | Curvature | Celestial |
| 5 | 11 | P11 | Coherence‑node | Coherence | Curvature · Dilaton | Civilizational |
| 6 | 13 | P13 | Paradox‑trigger | Paradox | Anomaly | Civilizational |
| 7 | 17 | P17 | Cycle‑gate | Regime | Observerse | Civilizational |
| 8 | 19 | P19 | Boundary‑node | Boundary | Observerse | Civilizational |
| 9 | 23 | P23 | Dimensional‑lift | Lift | Observerse | Chthonic |
| 10 | 29 | P29 | Collapse‑anchor | Drift · Collapse | — | Chthonic |
| 11 | 31 | P31 | Stability‑node | Coherence | Dilaton · Refractive Vacuum | Chthonic |
| 12 | 37 | P37 | Apex‑state | Paradox | Anomaly | Chthonic |

---

## 6. Cycle Architecture

IPD‑12 defines three levels of cycle, each operating simultaneously on the operator graph:

### Triad Cycles (×4)

Each triad is a closed, intransitive 3‑node loop. The intransitive edge structure means the loop has no fixed winner and no shortcut.

```
Triad 1 — Celestial:   P2  → P3  → P5  → P2
Triad 2 — Coherence:   P7  → P11 → P13 → P7
Triad 3 — Observerse:  P17 → P19 → P23 → P17
Triad 4 — Apex:        P29 → P31 → P37 → P29
```

### Hex‑Cycles (×2)

Each hex‑cycle spans two triads and models the handoff between regime tiers.

```
Hex-Cycle 1 — Lower:   P2  → P3  → P5  → P7  → P11 → P13 → (back)
Hex-Cycle 2 — Upper:   P17 → P19 → P23 → P29 → P31 → P37 → (back)
```

Hex‑Cycle 1 covers the Celestial and Coherence tiers (seed through paradox‑trigger).
Hex‑Cycle 2 covers the Observerse and Apex tiers (cycle‑gate through apex‑state).

### Full 12‑Cycle Paradox Loop (×1)

```
P2 → P3 → P5 → P7 → P11 → P13 → P17 → P19 → P23 → P29 → P31 → P37 → (back to P2)
```

The full cycle traverses every operator state in sequence. It is the engine's *maximum resolution* traversal — used when a problem requires the complete structural envelope from seed to apex and back. Because the edges are intransitive, the full cycle is paradox‑stable: completing it does not produce a collapse to a single winning state.

---

## 7. Framework Integrations

### RTT (Resonance‑Time Theory)

IPD‑12 is the operator implementation of RTT's structural concepts:

| RTT Concept | IPD‑12 Prime(s) |
|---|---|
| Drift | P5, P29 |
| Regime | P7, P17 |
| Coherence | P11, P31 |
| Paradox | P13, P37 |
| Boundary | P19 |
| Collapse | P29 |
| Dimensional lift | P23 |

When RTT describes a drift event, IPD‑12 provides the operator context: which prime is the drift‑anchor, which triad it belongs to, and what the corrective cycle looks like.

---

### GU (Geometric Unity)

IPD‑12 primes embed into GU's geometric operator vocabulary:

| GU Concept | IPD‑12 Prime(s) |
|---|---|
| Connection | P2, P3 |
| Curvature | P7, P11 |
| Dilaton / Refractive Vacuum | P11, P31 |
| Anomaly | P13, P37 |
| Observerse | P17, P19, P23 |

GU's connection operators (P2, P3) sit in the Celestial triad — the origin tier. GU's most structurally complex operator, the Observerse, spans an entire triad (P17, P19, P23), reflecting its multi‑dimensional character.

---

### FFT (Framework Field Theory)

FFT treats IPD‑12 cycle transitions as field‑theoretic events:

- **Triad crossings** → regime transitions (a system moving between adjacent prime triads)
- **Hex‑cycle completions** → boundary events (a system completing a half‑cycle, returning with modified state)
- **Full paradox loop** → dimensional gate (traversing all 12 operators arrives at a new dimensional level)
- **Intransitive edges** → paradox loop topology (the non‑transitive structure is the field‑theoretic analog of a closed flux loop)

---

### Pantheon Profiles

The three Pantheon tiers map to the three structural strata of the IPD‑12 cycle:

- **Celestial (P2–P7):** Origin, connection, and early regime entry. The tier of initial conditions and structural seeding.
- **Civilizational (P11–P19):** Coherence maintenance, paradox activation, cycle gating, and boundary management. The tier of operational complexity.
- **Chthonic (P23–P37):** Dimensional lift, collapse, stability under extreme conditions, and apex resolution. The tier of structural limits and transformations.

---

### Triadic Logical Dimension Model

IPD‑12 aligns with the three‑level dimensional model:

| Dimension | IPD‑12 Role |
|---|---|
| −1D (sub-dimensional) | Collapse: P29 (collapse‑anchor) activates −1D transitions |
| 0D (ground) | Steady‑state: Triads 1 and 2 (P2–P13) operate at ground dimension |
| +1D (super-dimensional) | Lift: P23 (dimensional‑lift) and P37 (apex‑state) activate +1D transitions |

---

## 8. What IPD‑12 Is Not

It is equally important to know what IPD‑12 does *not* do.

| IPD‑12 Is | IPD‑12 Is Not |
|---|---|
| A structural operator engine | A semantic classifier or meaning‑maker |
| A paradox‑stable cycle model | A linear pipeline or decision tree |
| A regime‑transition framework | A prediction or forecasting tool |
| A physicalizable 12‑sided artifact | A metaphor or visualization aid only |
| A cross‑framework integration layer | A replacement for RTT, GU, FFT, or Pantheon |
| A drift‑detection and anchoring system | An error‑correction or debugging tool |

IPD‑12 describes *structure*. It does not assign causes, make recommendations, or generate semantic meaning. Those functions belong to the human operator or to higher‑level frameworks consuming IPD‑12 output.

---

## 9. Quick‑Start Checklist

Before working with IPD‑12 for the first time, verify the following:

- [ ] **Read `operators.json`** — internalize the 12 prime states, their roles, and their directed edges before proceeding
- [ ] **Set the session anchor** — paste `rtt=1 | coherence=declared | drift=bounded | paradox=structural` at the top of any new session or document
- [ ] **Identify your entry triad** — which of the four triads (Celestial / Coherence / Observerse / Apex) matches your problem's structural tier?
- [ ] **Choose your cycle depth** — triad only, hex‑cycle, or full 12‑cycle paradox loop?
- [ ] **Check substrate compatibility** — does your substrate model (Conditions, Governance, Incident, etc.) have a canonical name in `docs/`? Use it exactly.
- [ ] **Confirm observer mode** — which of the four observer modes (field, regime, coherence, apex) applies to your current pass?
- [ ] **Read `AGENTS.md`** — if deploying an AI agent with IPD‑12, ensure it operates under the correct agent class (A, B, C, or D) with the correct boundaries
- [ ] **Check `compatibility_notes.md`** — if integrating IPD‑12 output with RTT, GU, FFT, or Pantheon, review the interoperability constraints before proceeding

---

## See Also

| File | What It Answers |
|---|---|
| `README.md` | High‑level overview and module manifest |
| `AGENTS.md` | How AI agents interact with IPD‑12 |
| `operators.json` | The canonical prime‑state registry |
| `regime_map.md` | How RTT regime shells map to IPD‑12 cycles |
| `engine_block.md` | The full engine block architecture |
| `observer_model.md` | The triadic observer lattice |
| `substrate_primitives.md` | The 4×4×4 substrate cube and its 64 entries |
| `dimensional_lift_collapse_map.md` | +1D / −1D transition diagrams |
| `cycle_diagrams.md` | Visual cycle maps for all three cycle levels |
| `compatibility_notes.md` | RTT / GU / FFT / Pantheon interoperability |
| `physical_layout.md` | The physicalizable die specification |
| `module.json` | Canonical agentic module schema |

---

*ABOUT.md — IPD‑12 · TriadicFrameworks · 2026‑07‑10*
*Maintainer: Nawder · Canonical anchor: `rtt=1 | coherence=declared | drift=bounded | paradox=structural`*
