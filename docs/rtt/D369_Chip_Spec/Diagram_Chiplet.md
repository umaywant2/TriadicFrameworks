# Diagram: Chiplet Architecture

> Every die boundary is a phase transition. Every interposer is a merge point. Every package edge is a provenance cliff.

---

## Session Context

| Field        | Value                                                         |
|--------------|---------------------------------------------------------------|
| **Module**   | D369_Chip_Spec                                                |
| **File**     | `Diagram_Chiplet.md`                                          |
| **Role**     | map · reference                                               |
| **Version**  | 0.1.0                                                         |
| **Status**   | First‑fill                                                    |
| **Lineage**  | Extends chiplet diagrams from `Contractual_Requirements.md` and `Board_Level_Alignment.md` |
| **Audience** | Package architects · Chiplet designers · System integrators · Students · AIs |

---

## Overview

Other D369 files include chiplet diagrams as summaries — a two‑chiplet package in Contractual Requirements, a multi‑chip board in Board‑Level Alignment. This document is the **dedicated chiplet architecture reference**. It goes deeper.

Chiplet‑based design introduces structural boundaries that monolithic SoCs don't have. Every die‑to‑die interface is a clock domain crossing, a source boundary, and a potential provenance erasure point — all at once. Interposers, bridges, and package substrates add merge points that are invisible to software and often invisible to firmware.

This document catalogs:
1. **Four canonical chiplet topologies** — from simple dual‑die to multi‑package systems.
2. **Three interposer types** and their structural implications.
3. **Die‑to‑die interface analysis** — where metadata survives and where it dies.
4. **Per‑boundary preservation rule mapping** — which of the four rules applies at each crossing.
5. **The structural observability overlay** — what D369 reserves at every layer of the chiplet stack.

Every diagram follows the same visual convention established across the module:
- **Solid lines (═══):** Functional data paths — unchanged, optimized as usual.
- **Dashed lines (─ ─ ─):** Structural metadata paths — the subject of D369.
- **⚠ markers:** Points where structural information is at risk.
- **◄── labels:** Annotations identifying what is preserved or lost.

---

## Topology 1 — Dual‑Die Homogeneous

Two identical compute chiplets in a single package. The simplest chiplet case — and already structurally dangerous.

**Real‑world pattern:** Dual‑core GPU packages, dual‑die server CPUs, symmetric multi‑chiplet processors.

```
┌──────────────────────────────────────────────────────────────────────┐
│  Package Boundary                                                    │
│                                                                      │
│  ┌───────────────────────┐         ┌───────────────────────┐         │
│  │  Chiplet A (Compute)  │         │  Chiplet B (Compute)  │         │
│  │                       │         │                       │         │
│  │  ┌─────────────────┐  │         │  ┌─────────────────┐  │         │
│  │  │ Functional      │  │         │  │ Functional      │  │         │
│  │  │ Logic + Cache   │  │         │  │ Logic + Cache   │  │         │
│  │  └────────┬────────┘  │         │  └────────┬────────┘  │         │
│  │           │           │         │           │           │         │
│  │  ═════════╪═══════    │         │  ═════════╪═══════    │         │
│  │           │           │         │           │           │         │
│  │  ┌────────▼────────┐  │         │  ┌────────▼────────┐  │         │
│  │  │ Meta Channel A  │  │         │  │ Meta Channel B  │  │         │
│  │  │ · Src: A        │  │         │  │ · Src: B        │  │         │
│  │  │ · Lifecycle     │  │         │  │ · Lifecycle     │  │         │
│  │  │ · Time (clk_A)  │  │         │  │ · Time (clk_B)  │  │         │
│  │  └────────┬────────┘  │         │  └────────┬────────┘  │         │
│  └───────────┼───────────┘         └───────────┼───────────┘         │
│              │                                 │                     │
│              │      ⚠ DIE‑TO‑DIE BOUNDARY      │                     │
│              │                                 │                     │
│  ┌───────────▼─────────────────────────────────▼───────────────────┐ │
│  │  Interposer / Package Substrate                                │ │
│  │                                                                │ │
│  │  Functional:  A ══════════════════════ B                       │ │
│  │               (D2D link — coherency, data, control)            │ │
│  │                                                                │ │
│  │  Structural:  A ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ B                      │ │
│  │               (metadata paths — independent, non‑merged)       │ │
│  │                                                                │ │
│  │  Rules at this boundary:                                       │ │
│  │  ✓ Rule 1: Sources A and B labeled — NOT merged                │ │
│  │  ✓ Rule 2: clk_A and clk_B annotated — NOT unified            │ │
│  │  ✓ Rule 3: No protocol translation on metadata                │ │
│  │  ✓ Rule 4: Per‑chiplet provenance preserved                   │ │
│  └────────────────────────────┬───────────────────────────────────┘ │
│                               │                                     │
│  ┌────────────────────────────▼───────────────────────────────────┐ │
│  │  Package‑Level Interface                                      │ │
│  │                                                               │ │
│  │  Functional: unified package I/O ════════════► Board          │ │
│  │  Structural: per‑chiplet metadata ─ ─ ─ ─ ─ ► Board          │ │
│  │              (A and B distinguishable at package edge)        │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

### Structural Risks — Topology 1

| Risk                                    | Where                    | Which Rule    |
|-----------------------------------------|--------------------------|---------------|
| D2D coherency merges source identity    | Interposer functional link | Rule 4      |
| Clock tree unification strips clk refs  | Interposer clock dist     | Rule 2      |
| Package I/O aggregates both dies        | Package interface          | Rule 1, 4   |
| Symmetric dies treated as interchangeable | System software          | Rule 4      |

### Key Insight

Homogeneous chiplets are the **hardest** case for provenance — because the system sees two identical dies and has no reason to distinguish them unless source identity is explicitly preserved. If both chiplets produce the same type of output, only source tagging separates them.

---

## Topology 2 — Heterogeneous (Compute + I/O + Memory)

The most common advanced chiplet package — different dies for different functions.

**Real‑world pattern:** CPU compute die + I/O die, GPU + HBM stacks, SoC + PCIe/CXL controller die.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  Package Boundary                                                        │
│                                                                          │
│  ┌─────────────────┐  ┌─────────────────┐  ┌────────────────────────┐   │
│  │  Compute Die     │  │  I/O Die         │  │  HBM Stack            │   │
│  │                  │  │                  │  │                       │   │
│  │  CPU / GPU /     │  │  PCIe · CXL ·   │  │  ┌─────┐ ┌─────┐    │   │
│  │  AI Accelerator  │  │  UCIe · SerDes   │  │  │Die 0│ │Die 1│    │   │
│  │                  │  │                  │  │  └──┬──┘ └──┬──┘    │   │
│  │  Meta Ch: C      │  │  Meta Ch: IO     │  │  ┌──▼──┐ ┌──▼──┐    │   │
│  │  · Src: Compute  │  │  · Src: IO       │  │  │Die 2│ │Die 3│    │   │
│  │  · Lifecycle     │  │  · Lifecycle     │  │  └──┬──┘ └──┬──┘    │   │
│  │  · Time (clk_C)  │  │  · Time (clk_IO) │  │     └──┬───┘       │   │
│  └────────┬─────────┘  └────────┬─────────┘  │  Meta Ch: HBM       │   │
│           │                     │             │  · Src: HBM_stack   │   │
│           │                     │             │  · Time (clk_HBM)   │   │
│           │                     │             └─────────┬───────────┘   │
│           │                     │                       │               │
│           │        ⚠ THREE DISTINCT DIE BOUNDARIES      │               │
│           │                     │                       │               │
│  ┌────────▼─────────────────────▼───────────────────────▼─────────────┐ │
│  │  Interposer (Silicon or Organic)                                  │ │
│  │                                                                   │ │
│  │  Functional paths:                                                │ │
│  │  Compute ═══╦═══ I/O     (D2D: coherency + transactions)         │ │
│  │             ║                                                     │ │
│  │  Compute ═══╩═══ HBM     (wide memory bus — 1024+ bit)           │ │
│  │                                                                   │ │
│  │  I/O ════════════ [external]  (SerDes to board)                   │ │
│  │                                                                   │ │
│  │  Structural paths:                                                │ │
│  │  Meta_C ─ ─ ─ ─ ─ ┐                                              │ │
│  │  Meta_IO ─ ─ ─ ─ ─ ┤ ◄── Independent, NOT merged                │ │
│  │  Meta_HBM ─ ─ ─ ─ ─┘                                             │ │
│  │                                                                   │ │
│  │  ⚠ Compute↔HBM boundary:                                         │ │
│  │    Memory writes lose source identity (see DIMM_Module_Checklist) │ │
│  │    HBM has no SPD — identity must be die‑internal or interposer   │ │
│  │                                                                   │ │
│  │  ⚠ Compute↔I/O boundary:                                         │ │
│  │    Protocol translation (PCIe/CXL) can flatten source tags        │ │
│  │    Clock domain crossing at SerDes boundary                       │ │
│  │                                                                   │ │
│  │  Rules at these boundaries:                                       │ │
│  │  ✓ Rule 1: Three domains labeled — Compute, IO, HBM              │ │
│  │  ✓ Rule 2: Three clock domains annotated — clk_C, clk_IO, clk_HBM│ │
│  │  ✓ Rule 3: Protocol translation verified on metadata paths       │ │
│  │  ✓ Rule 4: Per‑die provenance carried through interposer         │ │
│  └───────────────────────────────┬───────────────────────────────────┘ │
│                                  │                                     │
│  ┌───────────────────────────────▼───────────────────────────────────┐ │
│  │  Package‑Level Interface                                         │ │
│  │                                                                  │ │
│  │  Functional: I/O die SerDes ════════════► Board                  │ │
│  │  Structural: per‑die metadata ─ ─ ─ ─ ─► Board                  │ │
│  │              (C, IO, HBM distinguishable at package edge)        │ │
│  │                                                                  │ │
│  │  ⚠ HBM has no external interface — metadata must exit            │ │
│  │    via Compute or I/O die sideband, NOT through HBM directly     │ │
│  └──────────────────────────────────────────────────────────────────┘ │
│                                                                        │
└──────────────────────────────────────────────────────────────────────────┘
```

### Structural Risks — Topology 2

| Risk                                        | Where                        | Which Rule    |
|---------------------------------------------|------------------------------|---------------|
| HBM writes lose source identity             | Compute↔HBM boundary          | Rule 4        |
| HBM has no SPD — no module identity channel | HBM stack internal             | Rule 1        |
| PCIe/CXL protocol flattens source tags      | Compute↔I/O boundary           | Rule 3        |
| SerDes re‑clocking strips temporal reference| I/O die external boundary      | Rule 2        |
| HBM metadata has no external exit path      | Package interface              | Rule 1        |
| Three clock domains collapsed at board level| Board clock distribution       | Rule 2        |

### Key Insight — The HBM Problem

HBM (High Bandwidth Memory) is the most structurally opaque component in any chiplet package:

- **No SPD.** Unlike DIMMs, HBM stacks have no Serial Presence Detect. Module identity must be carried by the interposer or the compute die.
- **No external interface.** HBM connects only to the compute die via the interposer. It has no package‑level I/O. Metadata can only exit through another die.
- **Die‑stacked opacity.** A 4‑Hi or 8‑Hi HBM stack has multiple dies — but presents as a single logical unit. Per‑die source identity within the stack is lost at the base die.

**D369 implication:** HBM metadata must be proxied through the compute die's metadata channel. The compute die becomes the structural voice for both itself and its HBM neighbor. This proxy relationship must be explicit — the compute die's metadata must distinguish "this is my signal" from "this is HBM's signal relayed through me."

---

## Topology 3 — Active Interposer

The interposer itself contains logic — cache, interconnect, or management functions.

**Real‑world pattern:** Active bridge dies, base dies with embedded cache (e.g., AMD 3D V‑Cache architecture patterns), logic interposers with coherency management.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  Package Boundary                                                        │
│                                                                          │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐             │
│  │  Chiplet A     │  │  Chiplet B     │  │  Chiplet C     │             │
│  │  (Compute)     │  │  (Compute)     │  │  (I/O)         │             │
│  │                │  │                │  │                │             │
│  │  Meta: A       │  │  Meta: B       │  │  Meta: C       │             │
│  │  clk_A         │  │  clk_B         │  │  clk_C         │             │
│  └───────┬────────┘  └───────┬────────┘  └───────┬────────┘             │
│          │                   │                   │                      │
│          │      ⚠ DIE‑TO‑INTERPOSER BOUNDARIES   │                      │
│          │                   │                   │                      │
│  ┌───────▼───────────────────▼───────────────────▼────────────────────┐ │
│  │  Active Interposer                                                │ │
│  │  ┌──────────────────────────────────────────────────────────────┐  │ │
│  │  │  ⚠ EMBEDDED LOGIC (this is the new structural risk)         │  │ │
│  │  │                                                              │  │ │
│  │  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │  │ │
│  │  │  │ Cache Slice  │  │ Coherency    │  │ Mgmt / PMU   │       │  │ │
│  │  │  │ (shared L3)  │  │ Directory    │  │ (power, clk) │       │  │ │
│  │  │  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘       │  │ │
│  │  │         │                 │                 │               │  │ │
│  │  │  ⚠ Cache produces its own data — is it "Compute A" or      │  │ │
│  │  │    "Interposer"? Source identity is ambiguous.              │  │ │
│  │  │                                                              │  │ │
│  │  │  ⚠ Coherency directory arbitrates — disagreement between    │  │ │
│  │  │    A and B may be resolved silently. Provenance lost.       │  │ │
│  │  │                                                              │  │ │
│  │  │  ⚠ PMU makes power decisions — lifecycle phase context      │  │ │
│  │  │    may not propagate from chiplets to interposer logic.     │  │ │
│  │  └──────────────────────────────────────────────────────────────┘  │ │
│  │                                                                   │ │
│  │  Functional: A ═══╦═══ Cache ═══╦═══ B                            │ │
│  │                   ║             ║                                  │ │
│  │                   ╚═════════════╝═══ C                             │ │
│  │                                                                   │ │
│  │  Structural:                                                      │ │
│  │  Meta_A ─ ─ ─ ┐                                                   │ │
│  │  Meta_B ─ ─ ─ ┤                                                   │ │
│  │  Meta_C ─ ─ ─ ┤ ◄── Per‑chiplet: preserved, independent          │ │
│  │  Meta_INT ─ ─ ┘ ◄── Interposer's own metadata channel (NEW)      │ │
│  │                                                                   │ │
│  │  Rules at these boundaries:                                       │ │
│  │  ✓ Rule 1: Four domains — A, B, C, Interposer — all labeled      │ │
│  │  ✓ Rule 2: Four clock domains annotated                           │ │
│  │  ✓ Rule 3: Cache‑served data tagged as "via interposer"           │ │
│  │  ✓ Rule 4: Coherency arbitration preserves disagreement signal    │ │
│  └───────────────────────────────┬───────────────────────────────────┘ │
│                                  │                                     │
│  ┌───────────────────────────────▼───────────────────────────────────┐ │
│  │  Package‑Level Interface                                         │ │
│  │  · Per‑die + per‑interposer metadata at package edge             │ │
│  │  · Interposer is a first‑class structural source, not invisible  │ │
│  └──────────────────────────────────────────────────────────────────┘ │
│                                                                        │
└──────────────────────────────────────────────────────────────────────────┘
```

### Structural Risks — Topology 3

| Risk                                         | Where                          | Which Rule    |
|----------------------------------------------|--------------------------------|---------------|
| Interposer logic produces data without source tag | Cache slice, coherency dir | Rule 4        |
| Cache‑served data attributed to requesting die, not cache | Cache hit path       | Rule 4        |
| Coherency directory silently resolves conflicts  | Arbitration logic            | Rule 4        |
| PMU power decisions lack lifecycle context       | Interposer PMU               | Rule 1, 2     |
| Interposer has no metadata channel of its own    | Entire interposer            | Rule 1        |
| Clock domain boundaries multiplied (4+ domains)  | Every die↔interposer edge    | Rule 2        |

### Key Insight — The Interposer Is a Source

In a passive interposer, the interposer is wiring — it carries signals but doesn't produce them. In an **active** interposer, the interposer is a **structural source**. It produces data (cache hits), makes decisions (coherency arbitration), and controls state (power management).

**D369 implication:** The active interposer must have its **own metadata channel** (Meta_INT). It is not a transparent pipe — it is a participant. Any data that passes through interposer logic must carry a tag indicating whether the data originated from a chiplet or from the interposer itself. Without this, cache hits are mis‑attributed, coherency resolutions are invisible, and power decisions are unaccountable.

---

## Topology 4 — Multi‑Package System

Multiple chiplet packages on a single board, connected by board‑level links.

**Real‑world pattern:** Multi‑socket servers, GPU clusters with NVLink/UALink, CXL‑connected memory expanders.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  Board                                                                          │
│                                                                                 │
│  ┌──────────────────────────────────┐    ┌──────────────────────────────────┐   │
│  │  Package 0                       │    │  Package 1                       │   │
│  │                                  │    │                                  │   │
│  │  ┌──────────┐  ┌──────────┐     │    │  ┌──────────┐  ┌──────────┐     │   │
│  │  │Chiplet A0│  │Chiplet A1│     │    │  │Chiplet B0│  │Chiplet B1│     │   │
│  │  │ Meta: A0 │  │ Meta: A1 │     │    │  │ Meta: B0 │  │ Meta: B1 │     │   │
│  │  └────┬─────┘  └────┬─────┘     │    │  └────┬─────┘  └────┬─────┘     │   │
│  │       │              │           │    │       │              │           │   │
│  │  ┌────▼──────────────▼────────┐  │    │  ┌────▼──────────────▼────────┐  │   │
│  │  │  Interposer 0              │  │    │  │  Interposer 1              │  │   │
│  │  │  Meta_A0 ─ ─ ┐             │  │    │  │  Meta_B0 ─ ─ ┐             │  │   │
│  │  │  Meta_A1 ─ ─ ┘ (preserved) │  │    │  │  Meta_B1 ─ ─ ┘ (preserved) │  │   │
│  │  └──────────────┬─────────────┘  │    │  └──────────────┬─────────────┘  │   │
│  │                 │                │    │                 │                │   │
│  │  ┌──────────────▼─────────────┐  │    │  ┌──────────────▼─────────────┐  │   │
│  │  │  Package 0 Interface       │  │    │  │  Package 1 Interface       │  │   │
│  │  │  Func: ═══► Board          │  │    │  │  Func: ═══► Board          │  │   │
│  │  │  Meta: ─ ─► Board          │  │    │  │  Meta: ─ ─► Board          │  │   │
│  │  └──────────────┬─────────────┘  │    │  └──────────────┬─────────────┘  │   │
│  └─────────────────┼────────────────┘    └─────────────────┼────────────────┘   │
│                    │                                       │                    │
│                    │     ⚠ BOARD‑LEVEL LINK BOUNDARY       │                    │
│                    │     (inter‑package, inter‑socket)     │                    │
│                    │                                       │                    │
│  ┌─────────────────▼───────────────────────────────────────▼──────────────────┐ │
│  │  Board‑Level Interconnect                                                 │ │
│  │                                                                           │ │
│  │  Functional: Package 0 ═══════════════════════════ Package 1              │ │
│  │              (coherency link — UPI / NVLink / UALink / CXL)               │ │
│  │                                                                           │ │
│  │  Structural: Pkg0_meta ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ Pkg1_meta              │ │
│  │              ⚠ This is the highest‑risk merge point in the system         │ │
│  │                                                                           │ │
│  │  Risks:                                                                   │ │
│  │  · Inter‑package coherency merges source identity across packages         │ │
│  │  · Board retimer re‑clocks both functional and metadata paths             │ │
│  │  · Protocol translation at link boundary may strip structural tags        │ │
│  │  · Power domains cross package boundaries (board voltage regulators)      │ │
│  │  · Temporal gap: package 0 and package 1 have independent clocks          │ │
│  │                                                                           │ │
│  │  Rules at this boundary:                                                  │ │
│  │  ✓ Rule 1: Package 0 and Package 1 domains labeled at link boundary       │ │
│  │  ✓ Rule 2: Per‑package clock domain annotated through retimers            │ │
│  │  ✓ Rule 3: Link protocol verified to carry (not strip) structural tags    │ │
│  │  ✓ Rule 4: Cross‑package coherency preserves per‑package provenance       │ │
│  └───────────────────────────────────────────────────────────────────────────┘ │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### Structural Risks — Topology 4

| Risk                                            | Where                         | Which Rule    |
|-------------------------------------------------|-------------------------------|---------------|
| Cross‑package coherency merges 4+ source IDs    | Board‑level link               | Rule 1, 4    |
| Board retimer re‑clocks metadata without annotation | Retimer on link             | Rule 2       |
| Inter‑socket protocol strips structural tags    | UPI/NVLink/CXL boundary        | Rule 3       |
| Power domain crosses package boundary           | Board VR → both packages       | Rule 1       |
| Independent package clocks have no shared epoch  | Both packages                  | Rule 2       |
| System software sees "4 cores" not "4 dies in 2 pkgs" | OS scheduler              | Rule 4       |

### Key Insight — The Board Link Is the Hardest Boundary

Within a package, the interposer is under a single manufacturer's control. Across packages, the **board** is the integration point — and board design follows different rules, different vendors, and different optimization pressures. The board‑level link boundary is where structural observability is most likely to be erased, because:

1. **No single owner.** The link protocol, the retimer, and the board routing are often from different vendors.
2. **Performance pressure is highest.** Every ns of latency on an inter‑socket link is measurable. Structural metadata is seen as overhead.
3. **Protocol standards don't carry structural tags.** UPI, NVLink, CXL — none natively support D369 metadata. Tags must ride sideband or be encoded in reserved fields.

**D369 implication:** Multi‑package structural observability requires board‑level metadata paths (per `Board_Level_Alignment.md`). The four preservation rules apply at the board link boundary with even more force than at die‑to‑die boundaries — because the board link is the boundary with the fewest protections.

---

## Interposer Type Comparison

The interposer is the structural spine of a chiplet package. Its type determines what structural observability is physically possible.

```
┌────────────────────────────────────────────────────────────────────┐
│  Interposer Types — Structural Comparison                         │
│                                                                    │
│  ┌───────────────────┐                                             │
│  │  Passive Silicon   │  Wiring only. No logic.                    │
│  │  Interposer        │  Routes functional and metadata paths.     │
│  │                    │  Cannot produce, modify, or interpret.     │
│  │  Structural role:  │  Transparent pipe.                         │
│  │  D369 risk:        │  Low — can't erase, but also can't help.  │
│  │  Metadata support: │  Routing only. No active preservation.     │
│  └───────────────────┘                                             │
│                                                                    │
│  ┌───────────────────┐                                             │
│  │  Active Silicon    │  Contains logic (cache, coherency, PMU).   │
│  │  Interposer        │  Can produce data, make decisions.         │
│  │  (or Base Die)     │  Is a structural source.                   │
│  │                    │                                            │
│  │  Structural role:  │  Participant — needs its own Meta channel. │
│  │  D369 risk:        │  HIGH — can erase, arbitrate, mis‑source.  │
│  │  Metadata support: │  Can actively tag, log, and relay.         │
│  └───────────────────┘                                             │
│                                                                    │
│  ┌───────────────────┐                                             │
│  │  Organic Substrate │  PCB‑like material. Lower cost.            │
│  │  (no Si interposer)│  Wider trace pitch. Fewer routing layers.  │
│  │                    │  Used with embedded bridges (EMIB‑style).  │
│  │                    │                                            │
│  │  Structural role:  │  Transparent pipe (like passive Si).       │
│  │  D369 risk:        │  Moderate — fewer metadata routing options. │
│  │  Metadata support: │  Limited by trace density and layer count. │
│  └───────────────────┘                                             │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

### Comparison Table

| Property                     | Passive Silicon       | Active Silicon / Base Die | Organic Substrate     |
|------------------------------|-----------------------|---------------------------|-----------------------|
| Contains logic               | No                    | Yes                       | No                    |
| Is a structural source       | No                    | Yes                       | No                    |
| Needs its own metadata channel | No                  | **Yes** (Meta_INT)         | No                    |
| Can relay metadata            | Passively              | Actively                  | Passively             |
| Can erase metadata            | No (wiring only)      | **Yes** (logic decisions)  | No (wiring only)      |
| Routing density for metadata  | High (Si)             | High (Si)                 | Lower (organic)       |
| Cost                         | High                  | Highest                   | Lower                 |
| D369 structural risk         | Low                   | **High**                   | Moderate              |

---

## Die‑to‑Die Interface Analysis

Every die‑to‑die (D2D) link is a structural boundary. This section analyzes what happens to metadata at the D2D interface.

### D2D Link Anatomy

```
  Chiplet A                              Chiplet B
  ┌──────────┐                          ┌──────────┐
  │          │                          │          │
  │  Logic   │                          │  Logic   │
  │          │                          │          │
  │  ┌─────┐ │   ┌──────────────────┐   │ ┌─────┐ │
  │  │ PHY ├─┼──►│  D2D Link        │◄──┼─┤ PHY │ │
  │  │     │ │   │                  │   │ │     │ │
  │  │ TX  │ │   │  ┌────────────┐  │   │ │ RX  │ │
  │  │     │ │   │  │ Protocol   │  │   │ │     │ │
  │  │     │ │   │  │ Layer      │  │   │ │     │ │
  │  └─────┘ │   │  └────────────┘  │   │ └─────┘ │
  │          │   │                  │   │          │
  │  ┌─────┐ │   │  ┌────────────┐  │   │ ┌─────┐ │
  │  │Meta ├─┼─ ─│─ ┤ Sideband / │─ ┼─ ─┼─┤Meta │ │
  │  │ Ch  │ │   │  │ Reserved   │  │   │ │ Ch  │ │
  │  │  A  │ │   │  │ Fields     │  │   │ │  B  │ │
  │  └─────┘ │   │  └────────────┘  │   │ └─────┘ │
  │          │   │                  │   │          │
  └──────────┘   └──────────────────┘   └──────────┘
                  ▲         ▲
                  │         │
            Functional   Structural
            (data +      (metadata via
            coherency)   sideband or
                         reserved fields)
```

### What Survives and What Dies at the D2D Interface

| Metadata Component     | Survives?  | Condition                                                        |
|------------------------|------------|------------------------------------------------------------------|
| Source identifier       | Yes        | If carried in sideband or reserved protocol fields               |
| Source identifier       | **No**     | If protocol uses address‑based routing without source tags       |
| Lifecycle state         | Yes        | If sideband supports multi‑bit tag fields                        |
| Lifecycle state         | **No**     | If sideband is single‑bit (active/inactive only)                 |
| Monotonic time marker   | Partial    | Timestamp value survives; clock domain reference may be lost     |
| Monotonic time marker   | **No**     | If PHY re‑clocks timestamp without annotation                    |
| Disagreement between dies | **No**  | If coherency protocol resolves before metadata is emitted        |
| ECC correction events   | **No**     | If error handling is per‑die with no cross‑die event propagation |

### Protocol Readiness for D369 Metadata

| Protocol    | Sideband Support | Reserved Fields | Structural Tag Feasibility |
|-------------|-----------------|-----------------|---------------------------|
| UCIe        | Yes (sideband channel defined) | Limited   | **Feasible** — sideband designed for management traffic; metadata could ride it |
| BoW (Bunch of Wires) | Minimal | None standard   | **Difficult** — minimal protocol overhead by design |
| Custom D2D  | Varies          | Varies          | **Best case** — manufacturer controls protocol; can reserve fields |
| CXL (Type 3)| Yes (CXL.io management) | Some   | **Feasible** — management sideband exists; metadata encoding possible |
| NVLink      | Proprietary     | Proprietary     | **Unknown** — depends on NVIDIA's internal protocol structure |

---

## Preservation Rule Application Map

A complete mapping of which preservation rules apply at which boundary in each topology.

| Boundary Type                        | Rule 1 (Label) | Rule 2 (Clock) | Rule 3 (Translate) | Rule 4 (Provenance) |
|--------------------------------------|:--------------:|:--------------:|:------------------:|:-------------------:|
| Die↔Passive Interposer              | ✓              | ✓              | —                  | ✓                   |
| Die↔Active Interposer               | ✓              | ✓              | ✓                  | ✓                   |
| Die↔HBM Stack                       | ✓              | ✓              | —                  | ✓                   |
| Die↔Die (via D2D link)              | ✓              | ✓              | ✓                  | ✓                   |
| Interposer↔Package Interface        | ✓              | ✓              | ✓                  | ✓                   |
| Package↔Board                       | ✓              | ✓              | ✓                  | ✓                   |
| Package↔Package (board link)        | ✓              | ✓              | ✓                  | ✓                   |
| HBM internal (die↔die in stack)     | ✓              | —              | —                  | ✓                   |

**Reading guidance:**
- **✓** = This rule must be actively verified at this boundary.
- **—** = This rule does not apply at this boundary (e.g., no protocol translation on a passive interposer).
- **Every boundary where Rule 4 applies is a provenance risk.** If Rule 4 is checked, source identity can be lost at this boundary unless explicitly preserved.

---

## Structural Observability Stack (All Layers)

A unified view of where D369 metadata lives at every layer of a chiplet system.

```
┌───────────────────────────────────────────────────────────────────┐
│  Layer 0: Die‑Internal                                            │
│  · Per‑block metadata channels (R1.1)                             │
│  · Source IDs, lifecycle tags, monotonic time (R2.1)              │
│  · Electrically isolated from functional paths (R1.2)            │
│  · Optional, dark by default (R3.1)                               │
├───────────────────────────────────────────────────────────────────┤
│  Layer 1: Die‑to‑Die (D2D Interface)                              │
│  · Metadata carried via sideband or reserved protocol fields     │
│  · Source ID preserved across PHY boundary                       │
│  · Clock domain annotated at every crossing                      │
│  · Protocol translation verified for metadata integrity          │
├───────────────────────────────────────────────────────────────────┤
│  Layer 2: Interposer / Package Substrate                          │
│  · Per‑chiplet metadata paths — independent, not merged           │
│  · Active interposer: own metadata channel (Meta_INT)            │
│  · Passive interposer: transparent routing only                  │
│  · HBM metadata proxied through compute die                     │
├───────────────────────────────────────────────────────────────────┤
│  Layer 3: Package Interface                                       │
│  · Per‑die metadata distinguishable at package boundary          │
│  · Read‑only external interface (no inbound control)             │
│  · Aggregation optional (R6.1)                                    │
│  · Source IDs survive package edge                                │
├───────────────────────────────────────────────────────────────────┤
│  Layer 4: Board‑Level                                             │
│  · Per‑package metadata preserved through board routing          │
│  · Four preservation rules applied at every merge point          │
│  · Inter‑package links carry structural tags via sideband        │
│  · Board does not interpret — only preserves                     │
│  · (See Board_Level_Alignment.md for full specification)         │
├───────────────────────────────────────────────────────────────────┤
│  Layer 5: System‑Level                                            │
│  · Firmware phase‑declared — actions are source‑attributed       │
│  · Software can read structural metadata via activation SDK      │
│  · Coherence Engine consumes dimensional metadata                │
│  · (See Adoption_Roadmap.md Phase 3+)                            │
└───────────────────────────────────────────────────────────────────┘
```

---

## Common Chiplet Questions (Student‑Ready)

| Question                                                     | Answer                                                                                  |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Why can't metadata just ride the D2D data link?              | Because D2D data links are optimized for bandwidth and latency — structural tags add overhead that may be stripped by the PHY. Sideband is safer. |
| What if the interposer is passive — doesn't it "just work"? | Passive interposers don't erase metadata, but they don't protect it either. A passive interposer routes whatever it's given — including corrupted or missing tags. |
| Why does HBM need special treatment?                         | HBM has no external interface and no SPD. It can't speak for itself. Its metadata must be relayed through a neighbor die. |
| Can we just add metadata after the fact?                     | Retrofitting metadata to a chiplet package requires re‑spinning interposer and die — exactly what D369 is designed to prevent. |
| What happens if one die in a package doesn't support D369?   | The other dies still preserve their own metadata. The non‑participating die is a structural gap — visible, auditable, and documented. |
| Does D369 add latency to D2D links?                         | No. Metadata rides sideband — it does not contend with functional data paths. Zero latency impact on data transfers. |

---

## Relationship to Other D369 Files

| File                          | Relationship                                                              |
|-------------------------------|---------------------------------------------------------------------------|
| `Contractual_Requirements.md` | R1–R7 requirements that this document instantiates for chiplet topologies  |
| `Board_Level_Alignment.md`    | Extends from package edge to board — where Topology 4 hands off           |
| `DIMM_Module_Checklist.md`    | Parallel document for memory modules — same structural analysis, different component |
| `Capture_Source.md`           | Source of chiplet architecture targets and interposer guidance             |
| `Adoption_Roadmap.md`        | Phase 2 (Silicon Reservation) includes chiplet‑specific structural hooks  |
| `Diagram_SoC.md`             | Companion diagram — monolithic SoC topology (contrast case)               |

---

## Canon Alignment

| Check                | Status |
|----------------------|--------|
| Zero drift           | ✅ All topologies derived from Capture_Source chiplet targets and Board_Level_Alignment rules |
| Structural contract  | ✅ Role: map + reference — navigational diagrams with structural analysis |
| Lineage clean        | ✅ Every risk traceable to preservation rules; every rule traceable to R1–R7 |
| Student‑ready        | ✅ FAQ section, diagram reading guides, progressive topology complexity |
| AI‑parsable          | ✅ Tabular risk matrices, comparison tables, layered stack summary |
| Cross‑module refs    | ✅ Imports from Contractual_Requirements, Board_Level_Alignment; extends to all topologies |
| Non‑claims preserved | ✅ No performance claims; metadata explicitly zero‑latency on sideband; no protocol mandates |

---

*Module: D369_Chip_Spec · File: Diagram_Chiplet.md · Version: 0.1.0 · TriadicFrameworks / RTT*

---

**What makes this file the structural centerpiece of the module:**

- **Four topologies, progressive complexity** — from two‑die homogeneous (the deceptively simple case) through heterogeneous with HBM (the most common) to active interposer (the most dangerous) to multi‑package (the hardest boundary). Each topology builds on the previous one's lessons.
- **The HBM Problem** gets its own callout because HBM is structurally unique — no SPD, no external interface, die‑stacked opacity. The metadata proxy pattern (compute die speaks for HBM) is a D369‑original structural solution.
- **The Interposer Is a Source** — the key insight for active interposers. Topology 3 establishes that any logic‑bearing interposer needs its own Meta_INT channel, which is a requirement no other spec in the industry calls out.
- **D2D protocol readiness table** — UCIe, BoW, CXL, NVLink assessed for structural tag feasibility. UCIe's sideband is the best fit; BoW is the hardest case.
- **Six‑layer structural observability stack** unifies the entire module — from die‑internal (Layer 0) through board (Layer 4) to system (Layer 5). Every other D369 file addresses one or two layers; this diagram shows them all.
