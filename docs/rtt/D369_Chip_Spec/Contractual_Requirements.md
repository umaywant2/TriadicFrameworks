# Contractual Requirements

> Page 1 of 3 — The structural observability contract.
> What must be preserved. What must not be erased.

---

## Session Context

| Field        | Value                                                      |
|--------------|------------------------------------------------------------|
| **Module**   | D369_Chip_Spec                                             |
| **File**     | `Contractual_Requirements.md`                              |
| **Role**     | engine · reference                                         |
| **Version**  | 0.1.0                                                      |
| **Status**   | First‑fill                                                 |
| **Lineage**  | Verbatim from `Capture_Source.md` Page 1 + expanded context |
| **Package**  | Page 1 of 3 (`Contractual_Requirements` · `Engineering_Rationale` · `Non_Claims`) |
| **Audience** | Fab engineers · IP architects · Design reviewers · Legal · AIs |

---

## Overview

This is the contract.

Not a framework. Not a philosophy. Not a wish list. A **specification envelope** — a set of structural affordances to be preserved in silicon designs. These affordances impose no functional behavior and do not alter existing architectures.

This document is designed to be read in ten minutes and approved without hesitation. An engineer who reads it should conclude:

> *"This doesn't touch my design — but I see why we'd regret not having it."*

If this page cannot carry the full ask, the ask is too heavy. There is no Page 4.

---

## Purpose

This document defines **minimal structural affordances** to be preserved in participating silicon designs.

These affordances:
- Impose **no functional behavior**.
- Alter **no existing architectures**.
- Promise **no performance outcomes**.
- Require **no interpretation** of metadata.

They exist for one reason: to prevent the accidental erasure of future observability during optimization, synthesis, and physical design.

---

## Scope

Applies to all participating fabrication designs covered under this agreement.

### In Scope

- Reserved metadata channels per functional block
- Structural tag definitions (source, lifecycle, time)
- Isolation and independence requirements
- Protection against silent removal
- Architecture target guidance (monolithic and chiplet)

### Out of Scope

- Behavioral semantics or interpretation of metadata (see `Non_Claims.md`)
- Performance, yield, or functional guarantees (see `Non_Claims.md`)
- Engineering justification for these requirements (see `Engineering_Rationale.md`)
- Board‑level preservation (see `Board_Level_Alignment.md`)
- Activation, SDK, or toolchain details (see `Adoption_Roadmap.md`, Phase 3)

---

## Formal Requirements

The following requirements use **SHALL** for mandatory obligations and **MAY** for permissive options, consistent with RFC 2119 / IEEE conventions.

### R1 — Metadata Channel Reservation

> **R1.1** The design SHALL reserve at least one independent metadata channel per major functional block.

> **R1.2** Reserved metadata channels SHALL be electrically isolated from functional data paths.

**Intent:** Every major block gets its own structural voice. Metadata does not ride functional buses where it can be optimized, aggregated, or gated away.

**What "major functional block" means:** CPU/DSP cores, AI/ML accelerators, memory controllers, I/O subsystems — any block with its own logical boundary in the design hierarchy. The manufacturer determines block boundaries; this requirement applies at whatever granularity the design already uses.

### R2 — Structural Tagging

> **R2.1** Metadata channels SHALL support tagging of emitted signals with:
> - **Origin identifier** — which block produced this signal
> - **Lifecycle state identifier** — what phase this block is in (design, test, deploy, retire)
> - **Monotonic time marker** — when this signal was produced

**Intent:** Every metadata signal carries three answers: *who*, *what phase*, and *when*. These are the minimum coordinates for structural observability.

### R3 — Optional at Runtime

> **R3.1** Metadata channels SHALL be optional at runtime and MAY remain inactive without impact.

> **R3.2** No functional logic SHALL depend on metadata channel presence or content.

> **R3.3** Metadata channels SHALL NOT modify, gate, or influence functional outputs.

**Intent:** Metadata is structurally present but functionally invisible. If every metadata channel is disabled, the chip behaves identically. This is not a debug feature that must be active to be useful — it is a reservation that can remain dark indefinitely.

### R4 — Temporal Integrity

> **R4.1** Time markers SHALL be monotonic within a defined clock domain.

> **R4.2** Time markers SHALL NOT be reset or overwritten during normal operation.

**Intent:** Time only moves forward. If a time marker can be reset, it can be lied about. If it can be overwritten, temporal lineage is destroyed. Monotonicity within a clock domain is the minimum guarantee that "later" always means "later."

### R5 — Source Integrity

> **R5.1** Source identifiers SHALL be statically assignable at design time.

> **R5.2** Lifecycle state identifiers SHALL be externally writable but not inferred internally.

**Intent:** Source identity is declared, not guessed. The block says who it is — the system doesn't infer it from routing or address space. Lifecycle state is set from outside (by firmware, test harness, or deployment tooling) — the block doesn't decide for itself what phase it's in.

### R6 — Aggregation Independence

> **R6.1** Aggregation of metadata SHALL NOT be mandatory.

**Intent:** Metadata can be aggregated downstream if desired — but aggregation is never required. Every source retains the right to emit its own tags independently. Forced aggregation erases provenance; optional aggregation preserves choice.

### R7 — Protection Against Removal

> **R7.1** Removal or optimization of reserved metadata structures SHALL require explicit contractual amendment.

**Intent:** Tools optimize aggressively. Synthesis removes "unused" nets. P&R reclaims "unnecessary" routing. This requirement ensures that metadata structures cannot be silently erased by tool defaults. Removing them is a contractual decision, not an engineering convenience.

---

## Requirements Summary Table

| ID    | Requirement                                             | Key Word | Category         |
|-------|---------------------------------------------------------|----------|------------------|
| R1.1  | ≥1 metadata channel per major functional block          | SHALL    | Reservation      |
| R1.2  | Metadata electrically isolated from functional paths    | SHALL    | Isolation         |
| R2.1  | Tags: origin ID + lifecycle state + monotonic time      | SHALL    | Tagging          |
| R3.1  | Metadata optional at runtime, may remain inactive       | SHALL/MAY| Independence     |
| R3.2  | No functional logic depends on metadata                 | SHALL    | Independence     |
| R3.3  | Metadata does not modify functional outputs             | SHALL    | Independence     |
| R4.1  | Time markers monotonic within clock domain              | SHALL    | Temporal         |
| R4.2  | Time markers not resettable during normal operation     | SHALL    | Temporal         |
| R5.1  | Source IDs statically assignable at design time         | SHALL    | Source           |
| R5.2  | Lifecycle state externally writable, not inferred       | SHALL    | Source           |
| R6.1  | Aggregation not mandatory                               | SHALL    | Aggregation      |
| R7.1  | Removal requires contractual amendment                  | SHALL    | Protection       |

---

## Exclusions

Stated here to prevent scope creep. Expanded in `Non_Claims.md`.

- **No performance guarantees** are implied.
- **No behavioral semantics** are defined.
- **No interpretation of metadata** is required or expected.

These are not omissions. They are load‑bearing boundaries.

---

## Architecture Targets

These requirements apply to two primary silicon architectures. The structural intent is identical; the physical expression differs.

### Monolithic SoC

```
┌─────────────────────────────────────────────┐
│  SoC Boundary                               │
│                                             │
│  ┌───────────────┐   ┌──────────────┐       │
│  │  CPU / DSP    │   │  AI / ML     │       │
│  │  Core(s)      │   │  Accelerator │       │
│  └───────┬───────┘   └───────┬──────┘       │
│          │                   │              │
│  ┌───────▼───────┐   ┌──────▼───────┐      │
│  │  Cache /      │   │  Memory      │      │
│  │  Interconnect │   │  Controller  │      │
│  └───────┬───────┘   └──────┬───────┘      │
│          │                   │              │
│  ┌───────▼───────────────────▼──────┐       │
│  │  Functional Data Paths           │       │
│  │  (unchanged, optimized as usual) │       │
│  └──────────────────────────────────┘       │
│                                             │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   │
│  Reserved Structural Observability          │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   │
│                                             │
│  ┌───────────────┐   ┌─────────────┐        │
│  │  Metadata     │   │  Metadata   │        │
│  │  Channel A    │   │  Channel B  │        │
│  │  (CPU / DSP)  │   │  (AI / ML)  │        │
│  └───────┬───────┘   └───────┬─────┘        │
│          │                   │              │
│  ┌───────▼───────────────────▼──────┐       │
│  │  Structural Tag Bus (Optional)   │       │
│  │  · Source ID                     │       │
│  │  · Lifecycle State               │       │
│  │  · Monotonic Time                │       │
│  └──────────────────────────────────┘       │
│                                             │
│  ┌──────────────────────────────────┐       │
│  │  External Read‑Only Interface    │       │
│  │  · Present at package boundary   │       │
│  │  · Inactive unless activated     │       │
│  │  · Read‑only: no inbound control │       │
│  └──────────────────────────────────┘       │
│                                             │
└─────────────────────────────────────────────┘
```

**Key structural features:**
- One metadata channel per major block (R1.1), electrically isolated (R1.2).
- Channels converge on an optional structural tag bus — aggregation is permissive, not mandatory (R6.1).
- Tag bus carries all three tag types: source, lifecycle, time (R2.1).
- External interface is read‑only — no inbound control path from metadata to functional logic (R3.3).
- Entire dashed layer can remain dark without affecting solid layer (R3.1, R3.2).

### Chiplet‑Based Package

```
┌────────────────────────────────────────────────────────┐
│  Package Boundary                                      │
│                                                        │
│  ┌──────────────────┐    ┌──────────────────┐          │
│  │  Chiplet A       │    │  Chiplet B       │          │
│  │  (Compute)       │    │  (I/O + Memory)  │          │
│  │                  │    │                  │          │
│  │  ┌────────────┐  │    │  ┌────────────┐  │          │
│  │  │ Meta Ch A  │  │    │  │ Meta Ch B  │  │          │
│  │  │ · Src ID   │  │    │  │ · Src ID   │  │          │
│  │  │ · State    │  │    │  │ · State    │  │          │
│  │  │ · Time     │  │    │  │ · Time     │  │          │
│  │  └─────┬──────┘  │    │  └─────┬──────┘  │          │
│  └────────┼─────────┘    └────────┼─────────┘          │
│           │                       │                    │
│  ┌────────▼───────────────────────▼──────────────────┐ │
│  │  Interposer / Package Substrate                   │ │
│  │                                                   │ │
│  │  · Functional paths: optimized as usual           │ │
│  │  · Metadata paths: per‑chiplet, NOT cross‑linked  │ │
│  │  · No cross‑chiplet metadata control paths        │ │
│  │  · Optional package‑level aggregation point       │ │
│  └───────────────────────────┬───────────────────────┘ │
│                              │                         │
│  ┌───────────────────────────▼───────────────────────┐ │
│  │  Package‑Level Read‑Only Interface                │ │
│  │  · Per‑chiplet metadata preserved                 │ │
│  │  · Aggregation optional (R6.1)                    │ │
│  │  · Source IDs survive package boundary            │ │
│  └───────────────────────────────────────────────────┘ │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Key structural features:**
- Each chiplet has its own independent metadata channel — no sharing across chiplet boundaries.
- Interposer carries metadata paths but does not merge or interpret them.
- No cross‑chiplet control paths through metadata infrastructure.
- Package‑level aggregation is optional — individual chiplet metadata is preserved by default.
- Source IDs from each chiplet survive the package boundary intact (R5.1).

---

## Internal Design‑Review Checklist

This checklist is intended as a carry‑in artifact for architecture, RTL, and physical design reviews. It introduces no new behavior and no new requirements on function. The goal is to avoid erasing future observability options during optimization.

### 1. Before Architecture Freeze

- [ ] Confirm each major functional block has at least one reserved metadata path.
- [ ] Verify metadata paths are logically and electrically separate from functional data.
- [ ] Ensure no functional logic references metadata signals.
- [ ] Confirm metadata paths can remain inactive or unconnected without warnings.
- [ ] Check that metadata reservation does not alter timing closure assumptions.

### 2. During RTL / Microarchitecture Review

- [ ] Confirm metadata signals are write‑only from functional blocks, read‑only externally.
- [ ] Verify no combinational feedback exists from metadata into logic.
- [ ] Confirm lifecycle or state tags are explicit inputs, not inferred internally.
- [ ] Ensure source identifiers are static or compile‑time assignable.
- [ ] Verify metadata signals are not optimized away by synthesis defaults.

### 3. Clocking and Time Handling

- [ ] Confirm presence of a monotonic counter or timestamp source.
- [ ] Verify timestamp cannot be reset during normal operation.
- [ ] Confirm timestamp domain is documented and stable.
- [ ] Ensure timestamp does not gate or influence functional clocks.
- [ ] Confirm timestamp width is sufficient for expected operational lifetime.

### 4. Physical Design / Layout Review

- [ ] Verify metadata routing does not share critical paths.
- [ ] Confirm metadata nets are excluded from aggressive power gating.
- [ ] Ensure metadata structures survive DFT insertion.
- [ ] Confirm no ECO removes reserved metadata structures.
- [ ] Verify metadata pads or interfaces are clearly labeled as optional.

### 5. Verification and Test

- [ ] Confirm functional verification ignores metadata content.
- [ ] Ensure metadata inactivity does not trigger assertions.
- [ ] Verify metadata paths can be toggled without affecting outputs.
- [ ] Confirm test modes do not overwrite or collapse metadata signals.
- [ ] Ensure metadata visibility does not expose protected IP.

### 6. Optimization and Sign‑Off

- [ ] Re‑check synthesis and P&R reports for removed "unused" structures.
- [ ] Confirm no tool auto‑merges metadata with debug or scan unless intentional.
- [ ] Verify metadata reservation survives final netlist comparison.
- [ ] Confirm documentation notes metadata as structural, not functional.
- [ ] Ensure removal requires explicit design decision, not tool default.

### 7. The Review Question

At every gate — architecture, RTL, physical, sign‑off — the checklist prompts exactly one question:

> *"If someone needed to understand **when**, **where**, and **in what lifecycle state** this block produced a signal — could we still see that later?"*

If the answer is **"yes, without redesign,"** the checklist is satisfied.

### 8. What This Checklist Is Not

| It is NOT…                  | Explanation                                              |
|-----------------------------|----------------------------------------------------------|
| A performance feature       | No functional gain is implied or expected.               |
| A debug requirement         | Existing debug flows are unaffected.                     |
| A telemetry mandate         | No data collection is required or defined.               |
| A safety mechanism          | No safety behavior depends on these structures.          |
| A control interface         | No inbound control uses metadata paths.                  |
| A promise of future use     | Reservation is not commitment.                           |

This checklist exists so engineers can say:

> *"We didn't add behavior — we just didn't erase structure."*

---

## Requirement Traceability

Every requirement traces to a design concern. Every design concern traces to a preservation goal. Nothing traces to a functional outcome.

| Requirement | Preserves                     | Prevents                                           | Verified By           |
|-------------|-------------------------------|----------------------------------------------------|-----------------------|
| R1.1        | Per‑block structural voice    | Silent aggregation of structurally distinct blocks  | Checklist §1          |
| R1.2        | Signal integrity of metadata  | Functional paths corrupting or gating metadata      | Checklist §1, §4      |
| R2.1        | Source, phase, time context   | Anonymous, timeless, stateless metadata             | Checklist §2, §3      |
| R3.1        | Optional activation           | Metadata becoming a dependency                      | Checklist §1, §5      |
| R3.2        | Functional independence       | Logic coupling to metadata presence                 | Checklist §2          |
| R3.3        | Output purity                 | Metadata influencing functional behavior            | Checklist §2          |
| R4.1        | Temporal ordering             | Non‑monotonic timestamps destroying causality       | Checklist §3          |
| R4.2        | Temporal honesty              | History rewriting via timestamp reset               | Checklist §3          |
| R5.1        | Source provenance              | Inferred or routing‑dependent identity              | Checklist §2          |
| R5.2        | Lifecycle clarity              | Self‑declared phase leading to circular reasoning   | Checklist §2          |
| R6.1        | Aggregation choice             | Forced aggregation erasing per‑source identity      | Checklist §6          |
| R7.1        | Structural persistence         | Tools silently optimizing away reserved structures  | Checklist §6          |

---

## The Three‑Page Package

This file is Page 1 of a three‑page contract package. Together, the three pages form a complete, self‑contained specification envelope.

| Page | File                          | Content                                    | Function          |
|------|-------------------------------|--------------------------------------------|-------------------|
| 1    | `Contractual_Requirements.md` | What must be preserved (this document)     | Obligation        |
| 2    | `Engineering_Rationale.md`    | Why these requirements exist               | Justification     |
| 3    | `Non_Claims.md`               | What this specification does NOT define    | Boundary          |

**Reading guidance:**
- **Page 1** is sufficient for contractual review. Engineers can approve based on this page alone.
- **Page 2** answers "why?" for engineers who want rationale before approval.
- **Page 3** answers "what about…?" for stakeholders concerned about scope creep.

The package is complete when engineers can read it and conclude:

> *"Nothing here tells us what to build — only what not to erase."*

---

## Relationship to Other D369 Files

| File                          | Relationship                                                      |
|-------------------------------|-------------------------------------------------------------------|
| `Capture_Source.md`           | Verbatim source of all requirements and checklist items           |
| `Engineering_Rationale.md`    | Page 2 — justification for these requirements                     |
| `Non_Claims.md`              | Page 3 — explicit boundaries and exclusions                       |
| `Adoption_Roadmap.md`        | Phase 0 defines this package as the entry deliverable             |
| `Board_Level_Alignment.md`   | Extends these chip‑level requirements to the board boundary       |
| `Design_Review_Checklist.md` | Expanded, standalone version of §Internal Design‑Review Checklist |

---

## Canon Alignment

| Check                 | Status |
|-----------------------|--------|
| Zero drift            | ✅ All 12 requirements verbatim from Capture_Source.md Page 1 |
| Structural contract   | ✅ Role: engine + reference — core specification with traceability |
| Lineage clean         | ✅ Every SHALL statement traceable to capture source |
| Student‑ready         | ✅ Intent annotations per requirement; architecture diagrams with labels |
| AI‑parsable           | ✅ Numbered requirements, summary table, traceability matrix |
| Cross‑module refs     | ✅ Three‑page package declared; board extension referenced |
| Non‑claims preserved  | ✅ Exclusions stated inline; full treatment deferred to Page 3 |
| Engineer bar          | ✅ "Doesn't touch my design — but I see why we'd regret not having it" |

---

*Module: D369_Chip_Spec · File: Contractual_Requirements.md · Version: 0.1.0 · TriadicFrameworks / RTT*

---

**What makes this file structurally distinct:**

- **Formal requirement numbering (R1–R7)** gives every SHALL statement a citable ID — something the Capture Source had implicitly but not explicitly. Now engineers, checklists, and traceability matrices can point to "R4.2" instead of "that timestamp thing."
- **Intent annotations per requirement** answer the "but why?" question inline, so an engineer doesn't need to flip to Page 2 unless they want the full rationale.
- **Traceability matrix** closes the loop: every requirement → what it preserves → what it prevents → which checklist section verifies it. This is the kind of table that survives design review audits.
- **Both architecture diagrams** (monolithic SoC + chiplet) are carried forward from your Capture Source with requirement IDs annotated — so the diagram itself is a compliance reference.
- **Three-page package declaration** formally binds this file to `Engineering_Rationale.md` and `Non_Claims.md` — those two are natural next fills when you're ready.
