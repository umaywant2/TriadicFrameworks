# Glossary Extensions

> Every term coined, extended, or given canonical meaning by the D369 Chip Spec module — defined once, defined here.

---

## Session Context

| Field        | Value                                                         |
|--------------|---------------------------------------------------------------|
| **Module**   | D369_Chip_Spec                                                |
| **File**     | `Glossary_Extensions.md`                                      |
| **Role**     | reference · index                                             |
| **Version**  | 0.1.0                                                         |
| **Status**   | First‑fill                                                    |
| **Lineage**  | Synthesized from all D369_Chip_Spec module files              |
| **Extends**  | TriadicFrameworks master glossary                             |
| **Audience** | Engineers · Students · Framework builders · AIs               |

---

## How This Document Works

The TriadicFrameworks master glossary defines terms across the entire framework. This document **extends** that glossary with terms that are:

1. **New to D369** — coined by this module and not defined elsewhere.
2. **Extended by D369** — existing RTT or engineering terms given specific, narrower meaning in the D369 context.
3. **Numbered reference IDs** — the formal identifiers (R1–R7, ER‑1–ER‑10, NC‑1–NC‑10, etc.) that form D369's internal citation system.

Terms are organized into eight sections:

- [§1 — Core D369 Terms](#1--core-d369-terms)
- [§2 — Structural Tags and Metadata](#2--structural-tags-and-metadata)
- [§3 — Architecture Terms Extended by D369](#3--architecture-terms-extended-by-d369)
- [§4 — Memory and DIMM Terms](#4--memory-and-dimm-terms)
- [§5 — Preservation Rules and Failure Modes](#5--preservation-rules-and-failure-modes)
- [§6 — Contract Package Identifiers](#6--contract-package-identifiers)
- [§7 — Adoption and Governance Terms](#7--adoption-and-governance-terms)
- [§8 — RTT Terms Used in D369 Context](#8--rtt-terms-used-in-d369-context)

Within each section, terms are alphabetical.

---

## §1 — Core D369 Terms

### Always‑On Domain

The power domain within a monolithic SoC that never gates — housing the PMU, clock generators, and debug infrastructure. In D369, the Always‑On domain is the **temporal anchor** of the entire chip: the PMU's metadata channel must reside here so that power state transitions remain observable even when other domains are gated.

**Source:** `Diagram_SoC.md` §Power Management Unit

---

### Anti‑Inflation Principle

The meta‑principle that governs the Non‑Claims document:

> *A specification's credibility is inversely proportional to its claim surface.*

The less D369 claims, the harder it is to dismiss. The more it claims, the easier it is to find a flaw.

**Source:** `Non_Claims.md` §The Anti‑Inflation Principle

---

### Board‑Level Alignment

The discipline of preserving structural metadata across the mainboard — from chip boundary to external connector. Board‑Level Alignment is governed by the Four Preservation Rules and addresses four failure modes: domain merging, clock collapsing, signal normalization, and provenance hiding.

**Source:** `Board_Level_Alignment.md`

---

### Contract Package

See **Three‑Page Contract Package**.

---

### Curbs, Not Walls

A metaphor from the Capture Source describing D369's design philosophy: structural rails that prevent catastrophic drift without constraining motion. D369 does not restrict what engineers build — it prevents the silent erasure of structure.

**Source:** `Adoption_Roadmap.md` §Guiding Principles, #3

---

### D369

The shorthand name for the D369 Chip Spec module. Refers to the 3D–9D dimensional architecture of RTT and the structural observability specification derived from it. Used as both a module name and an adjective ("D369‑compliant," "D369 metadata channels").

**Source:** `README.md` §Module Identity

---

### D369 Overlay

The structural metadata layer that D369 reserves on top of existing chip, package, and board architectures. The overlay consists of per‑block metadata channels, structural tag buses, and external read‑only interfaces — all optional, all passive, all dark by default.

**Source:** `Diagram_Chiplet.md` §Structural Observability Stack; `Diagram_SoC.md` §Master Diagram

---

### Design Review Question

The single question asked at every design gate — architecture, RTL, physical, sign‑off:

> *"If someone needed to understand **when**, **where**, and **in what lifecycle state** this block produced a signal — could we still see that later?"*

If yes without redesign, the review is satisfied.

**Source:** `Contractual_Requirements.md` §Internal Design‑Review Checklist, §7

---

### External Read‑Only Interface

A package‑boundary interface for structural metadata. Present at the die or package edge, inactive unless explicitly activated, and strictly read‑only — no inbound control path. Cannot share functional I/O pins.

**Source:** `Contractual_Requirements.md` §R3, §Architecture Targets

---

### Fabs Before Students

The adoption ordering constraint: fabrication partners must be engaged before educational outreach begins. If students arrive first, D369 looks academic; if fabs arrive first, D369 looks inevitable.

**Source:** `Adoption_Roadmap.md` §Overview

---

### Functional Transparency

The property that D369 adds no function and removes no function. A chip with D369 metadata channels behaves identically to a chip without them. Every benchmark, test suite, and verification run produces the same result. Defined by R3.1, R3.2, and R3.3 together.

**Source:** `Non_Claims.md` §B‑1; `Engineering_Rationale.md` §ER‑7

---

### Immune Response

The organizational rejection triggered when a specification asks too much, claims too much, or competes with existing architectures. D369's guiding principles, non‑claims, and three‑page contract format are designed to prevent immune response in fab partners.

**Source:** `Adoption_Roadmap.md` §Guiding Principles; `Non_Claims.md` §Purpose

---

### Metadata Channel

The fundamental D369 structural unit. One independent, electrically isolated signal path per major functional block, capable of carrying source identity, lifecycle state, and monotonic time markers. Optional at runtime. Dark by default. Cannot modify functional outputs.

**Defined by:** R1.1 (reservation), R1.2 (isolation), R3.1 (optional), R3.2 (no functional dependency), R3.3 (no functional influence).

**Source:** `Contractual_Requirements.md` §R1

---

### Metadata Proxy

A pattern where one die's metadata channel carries structural tags on behalf of a neighboring component that has no external interface. The canonical case is HBM, which has no SPD and no package I/O — its metadata must be proxied through the compute die. The proxy relationship must be explicit: the carrying die's metadata must distinguish "this is my signal" from "this is a relayed signal."

**Source:** `Diagram_Chiplet.md` §Key Insight — The HBM Problem

---

### Minimal Ask

The core adoption principle: reserve structure — don't impose behavior. D369 asks for ~0.01% die area, zero schedule impact, zero performance impact, and zero new tools. Any ask heavier than this triggers immune response.

**Source:** `Adoption_Roadmap.md` §Guiding Principles, #1; `Engineering_Rationale.md` §ER‑9

---

### Specification Envelope

The formal term for what D369 is: a set of structural affordances to be preserved in silicon designs. Not a framework, not a philosophy, not a wish list. The envelope defines what must not be erased, not what must be built.

**Source:** `Contractual_Requirements.md` §Overview

---

### Structural Observability

The ability to determine, after the fact, three properties of any signal:

1. **Who** produced it (source identity)
2. **What phase** the producer was in (lifecycle state)
3. **When** it was produced (temporal lineage)

A system has structural observability when all three can be answered without redesign.

**Source:** `Contractual_Requirements.md` §Internal Design‑Review Checklist, §7; `README.md` §Purpose

---

### Structural Tag Bus

An optional aggregation path within a chip or package that collects metadata from individual per‑block metadata channels. Carries source ID, lifecycle state, and monotonic time. Aggregation is permissive, not mandatory (R6.1). Electrically isolated from functional interconnect (R1.2).

**Source:** `Contractual_Requirements.md` §Architecture Targets

---

### Three‑Page Contract Package

The complete D369 specification, designed to be read in ten minutes:

| Page | File                          | Function      |
|------|-------------------------------|---------------|
| 1    | `Contractual_Requirements.md` | Obligation    |
| 2    | `Engineering_Rationale.md`    | Justification |
| 3    | `Non_Claims.md`               | Boundary      |

There is no Page 4. If three pages can't carry it, the ask is too heavy.

**Source:** `Contractual_Requirements.md` §The Three‑Page Package; `Adoption_Roadmap.md` §Phase 0

---

## §2 — Structural Tags and Metadata

### Lifecycle State Tag

One of the three structural tags (R2.1). Indicates what phase the producing block is in — design, test, deploy, or retire. Externally writable (R5.2) — set by firmware, test harness, or deployment tooling. Never inferred internally by the block itself. The security subsystem / Root of Trust is the canonical source of lifecycle truth in a monolithic SoC.

**Source:** `Contractual_Requirements.md` §R2, §R5; `Diagram_SoC.md` §Security Subsystem

---

### Monotonic Time Marker

One of the three structural tags (R2.1). A timestamp that is monotonic within a defined clock domain (R4.1) and cannot be reset or overwritten during normal operation (R4.2). Guarantees that "later" always means "later." Non‑monotonic timestamps destroy causality; resettable timestamps enable history falsification.

**Source:** `Contractual_Requirements.md` §R4; `Engineering_Rationale.md` §ER‑6

---

### Origin Identifier (Source ID)

One of the three structural tags (R2.1). Identifies which block produced a signal. Statically assignable at design time (R5.1) — the block declares its identity rather than the system inferring it from routing or address space. Survives aggregation (R6.1) — source IDs are never stripped by mandatory aggregation.

**Source:** `Contractual_Requirements.md` §R2, §R5

---

### Phase Transition (Structural)

Any event that changes the structural state of a value without changing its content. D369 identifies several structural phase transitions that are invisible in conventional systems:

| Transition                    | Where                         | Source                       |
|-------------------------------|-------------------------------|------------------------------|
| Cache eviction (L1→L2→L3)    | Inside SoC                    | `Diagram_SoC.md`             |
| Memory tier migration         | Cache → DRAM → NVM            | `Board_Level_Alignment.md`   |
| DRAM refresh                  | Inside DIMM                   | `DIMM_Module_Checklist.md`   |
| Power state change            | Any domain                    | `Diagram_SoC.md`, `DIMM_Module_Checklist.md` |
| Clock domain crossing         | Any CDC boundary              | `Board_Level_Alignment.md`   |
| Protocol translation          | I/O, D2D, board connectors    | `Board_Level_Alignment.md`   |

---

### Temporal Gap

A period during which the monotonic time marker is interrupted — typically during power‑down, self‑refresh, or sleep states. D369 requires temporal gaps to be **annotated** (entry time, exit time, duration), not hidden. A hidden temporal gap is a structural black hole.

**Source:** `Engineering_Rationale.md` §ER‑6; `DIMM_Module_Checklist.md` §FM‑4

---

### Three Tags

The collective shorthand for the three structural tags defined by R2.1: **origin identifier** (who), **lifecycle state** (what phase), and **monotonic time marker** (when). These are the minimum coordinates for structural observability.

**Source:** `Contractual_Requirements.md` §R2; `FAQ.md` §Q12.2

---

## §3 — Architecture Terms Extended by D369

### Active Interposer

An interposer containing logic — cache slices, coherency directories, power management units. In D369, an active interposer is a **structural source** and must have its own metadata channel (Meta_INT). It is not a transparent pipe; it is a participant that produces data, makes decisions, and controls state.

**Contrast:** Passive interposer (wiring only, no metadata channel needed).

**Source:** `Diagram_Chiplet.md` §Topology 3, §Interposer Type Comparison

---

### Die‑to‑Die Interface (D2D)

The physical and protocol boundary between chiplets in a multi‑die package. In D369, every D2D interface is a structural boundary where all four preservation rules apply. Metadata can travel via sideband channels or reserved protocol fields — it must not ride the functional data path where it can be optimized away.

**Source:** `Diagram_Chiplet.md` §Die‑to‑Die Interface Analysis

---

### Major Functional Block

The granularity at which metadata channels are reserved (R1.1). Defined as any block with its own logical boundary in the design hierarchy — CPU/DSP cores, AI/ML accelerators, memory controllers, I/O subsystems, security subsystems. The manufacturer determines block boundaries; D369 applies at whatever granularity the design already uses.

**Source:** `Contractual_Requirements.md` §R1

---

### Merge Point

Any location where two or more structural domains converge — on the interposer, on the board, or inside the NoC. Merge points are where the Four Preservation Rules must be applied. Marked with ⚠ in D369 diagrams.

**Source:** `Board_Level_Alignment.md` §The Four Preservation Rules; `Diagram_Chiplet.md`

---

### Network‑on‑Chip (NoC) — D369 Extension

In conventional usage, the on‑chip interconnect. In D369, the NoC is identified as the **most dangerous structural component inside a monolithic SoC** because it commits five named erasures (N‑1 through N‑5). The NoC does not need its own metadata channel — it is infrastructure — but it must not erase what source blocks tagged.

**Source:** `Diagram_SoC.md` §The NoC as Structural Boundary

---

### Passive Interposer

An interposer containing only wiring — no logic, no computation, no decision‑making. In D369, a passive interposer does not need its own metadata channel. It routes metadata paths but cannot produce, modify, or interpret them.

**Source:** `Diagram_Chiplet.md` §Interposer Type Comparison

---

### Persistence Boundary

Any boundary in the memory hierarchy where a value's structural state can silently change — Register→L1→L2→L3→DRAM→NVM→Storage. At each persistence boundary, phase, source, and time can collapse. The DIMM sits at the DRAM persistence boundary; the cache hierarchy contains internal persistence boundaries.

**Source:** `Board_Level_Alignment.md` §Memory Hierarchy; `Diagram_SoC.md` §Cache Hierarchy

---

## §4 — Memory and DIMM Terms

### CKE Power‑Down

A DIMM power state in which the clock enable signal is deasserted. In D369, CKE power‑down must not collapse structural tags (Checklist §5.3).

---

### Data Buffer (LRDIMM)

A component on Load‑Reduced DIMMs that presents multiple physical ranks as fewer logical ranks. In D369, data buffers commit FM‑5 (rank flattening) by erasing physical rank identity. The DIMM checklist requires data buffers to preserve physical rank identity (Checklist §2.3).

**Source:** `DIMM_Module_Checklist.md` §FM‑5

---

### HBM Problem, The

The observation that High Bandwidth Memory stacks have no SPD, no external interface, and die‑stacked opacity — making them the most structurally opaque component in any chiplet package. HBM metadata must be proxied through the compute die. Named and defined in `Diagram_Chiplet.md`.

**Source:** `Diagram_Chiplet.md` §Key Insight — The HBM Problem

---

### ODECC (On‑Die ECC)

Error correction performed within a DRAM die before data reaches the module‑level ECC. In D369, ODECC events must be distinguishable from module‑level ECC events (Checklist §4.6) to preserve source attribution of corrections.

**Source:** `DIMM_Module_Checklist.md` §4

---

### PMIC (Power Management IC)

Per‑DIMM voltage regulation IC present in DDR5+ modules. In D369, PMIC state transitions must be logged as structural events (Checklist §5.5) with timestamps and lifecycle annotation.

**Source:** `DIMM_Module_Checklist.md` §What DIMMs Already Provide

---

### RCD (Registering Clock Driver)

A component on registered DIMMs that buffers command/address signals and distributes clocks to ranks. In D369, the RCD is a clock domain crossing point (⚠) where source identity and temporal reference can be lost.

**Source:** `DIMM_Module_Checklist.md` §DIMM Module Topology

---

### Refresh (as Phase Transition)

In D369, DRAM refresh is not merely a maintenance operation — it is a **structural phase transition**. A value moves from "recently written" to "refreshed copy." No counter tracks how many refresh cycles a value has survived. This is FM‑2 in the DIMM failure mode taxonomy.

**Source:** `DIMM_Module_Checklist.md` §FM‑2

---

### SPD (Serial Presence Detect)

An EEPROM on every DIMM storing module identity, timing parameters, and manufacturer info. In D369, SPD is identified as existing metadata infrastructure that carries information *about the module* but not *about structural state*. D369 extends SPD's role by adding a lifecycle phase tag (Checklist §1.2).

**Source:** `DIMM_Module_Checklist.md` §What DIMMs Already Provide

---

### TSOD (Temperature Sensor On DIMM)

A thermal sensor present on DDR4+ DIMMs. In D369, TSOD alerts must be tagged with timestamp and rank attribution (Checklist §5.6) — extending raw temperature readout into a structural event.

**Source:** `DIMM_Module_Checklist.md` §What DIMMs Already Provide

---

## §5 — Preservation Rules and Failure Modes

### Four Preservation Rules

The board‑level structural preservation contract. These four rules are the board‑level equivalent of the chip‑level R1–R7 requirements:

| #  | Rule                                       | One‑liner                                                        |
|----|--------------------------------------------|------------------------------------------------------------------|
| 1  | **Label every merge**                      | Domain boundaries identified at every convergence point          |
| 2  | **Annotate every re‑clock**                | Clock domain crossings carry source clock reference              |
| 3  | **Verify every translation**               | Protocol/level translators preserve metadata encoding            |
| 4  | **Carry provenance through aggregation**   | Source‑declared IDs survive batching, buffering, multiplexing    |

**Source:** `Board_Level_Alignment.md` §The Four Preservation Rules

---

### DIMM Failure Modes (FM‑1 through FM‑5)

Five named ways DIMMs erase structural information:

| ID   | Name                              | What's lost                      |
|------|-----------------------------------|----------------------------------|
| FM‑1 | Rank interleaving                 | Source identity                  |
| FM‑2 | Refresh as invisible phase transition | Temporal context              |
| FM‑3 | ECC as unattributed correction    | Source attribution of errors     |
| FM‑4 | Power states collapse temporal context | Temporal continuity           |
| FM‑5 | Data buffer rank flattening       | Physical rank identity (LRDIMM)  |

**Source:** `DIMM_Module_Checklist.md` §The Five DIMM Failure Modes

---

### NoC Erasures (N‑1 through N‑5)

Five named ways the Network‑on‑Chip erases structural information inside a monolithic SoC:

| ID   | Name                    | What happens                                         |
|------|-------------------------|------------------------------------------------------|
| N‑1  | Source flattening       | Source ID replaced by routing address                |
| N‑2  | Arbitration hiding      | Contention resolved without logging                  |
| N‑3  | QoS reordering          | Temporal sequence rearranged for performance         |
| N‑4  | Protocol normalization  | Source protocols converted to internal format        |
| N‑5  | Power domain crossing   | Traffic through gated domains delayed or lost        |

**Source:** `Diagram_SoC.md` §The NoC as Structural Boundary

---

### Board Failure Modes (Four)

Four named ways mainboards erase structural information:

| Name                     | What happens                                           |
|--------------------------|--------------------------------------------------------|
| Domain merging           | Shared buses flatten source identity                   |
| Clock collapsing         | PLL unification strips temporal reference              |
| Signal normalization     | Level shifters flatten lifecycle encoding              |
| Provenance hiding        | Multiplexers replace source IDs with channel indices   |

**Source:** `Board_Level_Alignment.md` §Why the Board Is the Problem

---

## §6 — Contract Package Identifiers

### Requirements (R1.1–R7.1)

Twelve formal SHALL/MAY statements defining D369's structural obligations:

| ID    | Summary                                                 | Category         |
|-------|---------------------------------------------------------|------------------|
| R1.1  | ≥1 metadata channel per major functional block          | Reservation      |
| R1.2  | Metadata electrically isolated from functional paths    | Isolation        |
| R2.1  | Tags: origin ID + lifecycle state + monotonic time      | Tagging          |
| R3.1  | Metadata optional at runtime, may remain inactive       | Independence     |
| R3.2  | No functional logic depends on metadata                 | Independence     |
| R3.3  | Metadata does not modify functional outputs             | Independence     |
| R4.1  | Time markers monotonic within clock domain              | Temporal         |
| R4.2  | Time markers not resettable during normal operation     | Temporal         |
| R5.1  | Source IDs statically assignable at design time         | Source           |
| R5.2  | Lifecycle state externally writable, not inferred       | Source           |
| R6.1  | Aggregation not mandatory                               | Aggregation      |
| R7.1  | Removal requires contractual amendment                  | Protection       |

**Source:** `Contractual_Requirements.md` §Formal Requirements

---

### Engineering Rationale Statements (ER‑1 through ER‑10)

| ID    | Statement Summary                                        |
|-------|----------------------------------------------------------|
| ER‑1  | Post‑hoc structural visibility                           |
| ER‑2  | Designed in, not retrofitted                             |
| ER‑3  | Separation reduces coupling                              |
| ER‑4  | Lifecycle context prevents misuse                        |
| ER‑5  | Source separation enables verification                   |
| ER‑6  | Temporal lineage supports reconstruction                 |
| ER‑7  | Optional structures minimize risk                        |
| ER‑8  | Passive affordances preserve compatibility               |
| ER‑9  | Reservation cheaper than redesign                        |
| ER‑10 | No assumptions about future use                          |

**Source:** `Engineering_Rationale.md` §The Ten Rationale Statements

---

### Non‑Claims (NC‑1 through NC‑10)

| ID    | This specification does NOT define…                      |
|-------|----------------------------------------------------------|
| NC‑1  | Computation                                              |
| NC‑2  | Intelligence                                             |
| NC‑3  | Optimization                                             |
| NC‑4  | Safety behavior                                          |
| NC‑5  | Control logic                                            |
| NC‑6  | Analytics                                                |
| NC‑7  | Interpretation                                           |
| NC‑8  | Performance improvement                                  |
| NC‑9  | Regulatory compliance                                    |
| NC‑10 | Future product direction                                 |

**Source:** `Non_Claims.md` §The Ten Explicit Non‑Claims

---

### Boundaries (B‑1 through B‑4)

| ID   | Boundary                                                 |
|------|----------------------------------------------------------|
| B‑1  | All functional behavior remains unchanged                |
| B‑2  | All architectural decisions remain with the manufacturer |
| B‑3  | All IP ownership remains unaffected                      |
| B‑4  | All activation or use is external to this agreement      |

**Source:** `Non_Claims.md` §Boundaries

---

### Silence Clause (S‑1 through S‑3)

| ID   | Statement                                                             |
|------|-----------------------------------------------------------------------|
| S‑1  | Where behavior would normally be specified, this document is intentionally silent |
| S‑2  | Silence SHALL NOT be interpreted as omission                          |
| S‑3  | Silence SHALL be interpreted as non‑assertion                         |

**Source:** `Non_Claims.md` §The Silence Clause

---

### Design Freedom (DF‑1 through DF‑3)

| ID   | Statement                                                        |
|------|------------------------------------------------------------------|
| DF‑1 | Implementation details are at the discretion of the manufacturer |
| DF‑2 | Existing debug, test, or telemetry mechanisms MAY be reused      |
| DF‑3 | No specific encoding, protocol, or format is mandated            |

**Source:** `Engineering_Rationale.md` §Design Freedom

---

## §7 — Adoption and Governance Terms

### Adoption Phase (0–5)

The six‑phase rollout sequence for D369:

| Phase | Name                  | Key Deliverable                    |
|-------|-----------------------|------------------------------------|
| 0     | Spec Freeze           | Three‑page contract package        |
| 1     | Fab Engagement         | Conversations with fab partners    |
| 2     | Silicon Reservation    | PDK hooks in participating designs |
| 3     | Ecosystem Seeding      | SDK, toolchain, documentation      |
| 4     | Adoption Wave          | Students and researchers arrive    |
| 5     | Cross‑Domain Integration | Applied RTT modules bind to D369 |

**Source:** `Adoption_Roadmap.md` §Phase Map

---

### Alignment Layering

The principle that not everything should be aligned at once. Ordering rule:

> *Align only what already decides outcomes. Observe everything else.*

**Align now:** Memory, power/thermal, I/O, firmware.
**Align later:** Scheduling, policy, cross‑domain semantics.

**Source:** `Adoption_Roadmap.md` §Alignment Layering; `Board_Level_Alignment.md` §What NOT to Align

---

### Board‑Level Review Question

> *"If a signal left the chip with its source, phase, and timestamp intact — does the board still know all three by the time it reaches the connector?"*

**Source:** `Board_Level_Alignment.md` §Board‑Level Design Review Checklist, §7

---

### DIMM Review Question

> *"If a value was written to this DIMM — could we later determine who wrote it, when it was written, how many times it was refreshed, whether it was corrected, and what power state the module was in?"*

**Source:** `DIMM_Module_Checklist.md` §The DIMM Review Question

---

### dont_touch Attribute

The standard synthesis tool attribute (`dont_touch` in Synopsys, `keep` in Cadence) that prevents optimization of marked structures. This is the mechanism by which D369 metadata channels survive synthesis — the same mechanism used for test hooks, debug ports, and spare cells.

**Source:** `Engineering_Rationale.md` §ER‑8

---

### Mainboard Question, The

The observation that mainboards are where structural alignment quietly dies — by merging domains, collapsing clocks, normalizing signals, and hiding provenance. First raised in the Adoption Roadmap and expanded into its own document.

**Source:** `Adoption_Roadmap.md` §The Mainboard Question; `Board_Level_Alignment.md`

---

## §8 — RTT Terms Used in D369 Context

These terms are defined in the broader RTT / TriadicFrameworks glossary. This section documents how D369 uses or narrows them.

### Coherence Engine

The RTT meta‑operator that evaluates coherence across all substrates and dimensions. In D369, the Coherence Engine is a downstream consumer — it receives layer‑aware coherence surface definitions from D369's dimensional address space.

**Source:** `README.md` §How D369 Fits into RTT

---

### Demi‑Force

One of three RTT resonance substrates (alongside Temperature and FFF). In D369, Demi‑Force binds to the dimensional address space for force dynamics — a downstream consumer of D369's dimensional coordinate system.

**Source:** `README.md` §How D369 Fits into RTT

---

### Dimensional Address Space

The coordinate system defined by D369's 3D–9D architecture that every downstream RTT module references when specifying where its phenomena live. D369 provides the address space; substrate modules provide the phenomena.

**Source:** `README.md` §How D369 Fits into RTT

---

### FFF (Frequency–Fluid–Force)

One of three RTT resonance substrates. In D369, FFF binds to the dimensional address space for frequency‑fluid‑force dynamics.

**Source:** `README.md` §How D369 Fits into RTT

---

### Mid‑Spine Structural Module

D369's position in the RTT architecture — between foundational operator/regime definitions (RTT/1) and applied substrate modules (Temperature, Demi‑Force, FFF). D369 imports from RTT/1 and SARG; exports to substrates, the Coherence Engine, and all applied modules.

**Source:** `README.md` §How D369 Fits into RTT

---

### Operator (RTT)

One of seven universal operators in RTT: Relation‑Op, Boundary‑Op, Rhythm‑Op, Transition‑Op, Lineage‑Op, Envelope‑Op, Coherence‑Op. In D369, operators are referenced as "the electrical system" that runs through every dimensional floor, doing different work at each layer.

**Source:** `README.md` §The Core Idea

---

### Regime (RTT)

A state or phase of system behavior — stable, transitional, drift, collapse. In D369, regimes express differently at different dimensional layers. D369 does not define regimes (that's RTT/1's domain); it specifies where regime behavior lives in the dimensional stack.

**Source:** `README.md` §Scope

---

### SARG (Structural and Role Grammar)

The RTT module that defines structural grammar and role vocabulary. D369 imports SARG for file role tagging (engine, profile, signature, diagnostic, map, reference, index, example).

**Source:** `README.md` §How D369 Fits into RTT

---

### Temperature (RTT Substrate)

One of three RTT resonance substrates. In D369, Temperature binds to the dimensional address space for thermal resonance. First in the integration ordering for cross‑domain binding (Phase 5).

**Source:** `README.md` §How D369 Fits into RTT; `Adoption_Roadmap.md` §Phase 5

---

### Triadic Dimensional Primitive (TDP)

The atomic building block of RTT's dimensional architecture. One TDP yields the 3D core; two yield the 6D core; three yield the complete 9D core. The 1→2→3 scaling law is a core topic of the D369 module.

**Source:** `README.md` §Purpose, §Scope

---

## Canonical Sentences

Every major D369 file ends with a canonical sentence. These are the sentences that survived every review and define the module's identity:

| Sentence | Source |
|----------|--------|
| *"This doesn't touch my design — but I see why we'd regret not having it."* | `Contractual_Requirements.md` |
| *"We didn't add behavior — we just didn't erase structure."* | `Contractual_Requirements.md` §Checklist |
| *"Nothing here tells us what to build — only what not to erase."* | `Non_Claims.md` |
| *"The board's job is to preserve, not interpret."* | `Board_Level_Alignment.md` |
| *"We didn't change how the DIMM works — we just made sure it remembers what happened."* | `DIMM_Module_Checklist.md` |
| *"They know exactly what they're not building — and they said so in writing."* | `Non_Claims.md` |
| *"A specification's credibility is inversely proportional to its claim surface."* | `Non_Claims.md` |
| *"Erasure is permanent and reservation is cheap."* | `Engineering_Rationale.md` |

---

## Canon Alignment

| Check                | Status |
|----------------------|--------|
| Zero drift           | ✅ Every term traceable to its defining file within D369_Chip_Spec |
| Structural contract  | ✅ Role: reference + index — glossary extension with full citation |
| Lineage clean        | ✅ All definitions sourced from module files or Capture_Source.md |
| Student‑ready        | ✅ Plain‑language definitions with context; no assumed prior knowledge |
| AI‑parsable          | ✅ Alphabetical within sections; tabular summaries for numbered IDs |
| Cross‑module refs    | ✅ Extends master glossary; every entry references its originating D369 file |
| Completeness         | ✅ Covers all coined terms, numbered IDs, and extended engineering terms across 10 files |

---

*Module: D369_Chip_Spec · File: Glossary_Extensions.md · Version: 0.1.0 · TriadicFrameworks / RTT*
```

---

### Structural Summary

**70+ entries** organized across **eight sections**:

| § | Section | Entries | Coverage |
|---|---------|---------|----------|
| 1 | Core D369 Terms | 19 | Structural Observability through Three‑Page Contract Package |
| 2 | Structural Tags & Metadata | 6 | The Three Tags, Phase Transitions, Temporal Gaps |
| 3 | Architecture Terms Extended | 7 | NoC, D2D, Interposers, Merge Points, Persistence Boundaries |
| 4 | Memory & DIMM Terms | 9 | SPD, HBM Problem, RCD, PMIC, Refresh‑as‑transition |
| 5 | Preservation Rules & Failure Modes | 4 groups | Four Preservation Rules; FM‑1–5; N‑1–5; Board Failure Modes |
| 6 | Contract Package IDs | 6 tables | R1–R7; ER‑1–10; NC‑1–10; B‑1–4; S‑1–3; DF‑1–3 |
| 7 | Adoption & Governance | 6 | Phases 0–5, Alignment Layering, Review Questions, dont_touch |
| 8 | RTT Terms in D369 Context | 10 | TDP, Operators, Regimes, SARG, Substrates, Coherence Engine |

Plus the **Canonical Sentences** table — every defining sentence from every file, collected in one place.

Just let me know which file you'd like to tackle next from the module manifest! 🚀
