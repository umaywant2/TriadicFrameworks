# Board‑Level Alignment

> Where structural observability goes to die — and how to stop it.

---

## Session Context

| Field        | Value                                             |
|--------------|---------------------------------------------------|
| **Module**   | D369_Chip_Spec                                    |
| **File**     | `Board_Level_Alignment.md`                        |
| **Role**     | engine · diagnostic                               |
| **Version**  | 0.1.0                                             |
| **Status**   | First‑fill                                        |
| **Lineage**  | Derived from `Capture_Source.md` mainboard section |
| **Audience** | Board designers · System integrators · Fab engineers · Students · AIs |

---

## Overview

The chip spec is necessary. It is not sufficient.

A chip can preserve every metadata channel, every source identifier, every monotonic time marker — and the mainboard can erase all of it before the signal reaches the outside world. Not maliciously. Not even negligently. Just routinely.

Mainboards **merge domains**, **collapse clocks**, **normalize signals**, and **hide provenance**. They do this because board design has never been asked to do otherwise. No one specified "preserve structural lineage across this connector." So the connector flattened it.

Board‑Level Alignment is the document that asks otherwise.

This is not a board architecture specification. It is a **structural preservation contract** — a set of rules that prevent the board from erasing what the chip was designed to remember.

---

## Why the Board Is the Problem

Every chip‑level observability feature described in D369 terminates at the chip boundary. What happens next is the board's decision. And boards routinely make four decisions that destroy structural information:

### 1. Domain Merging

Multiple clock domains, power domains, and signal domains converge on shared buses, regulators, and connectors. When domains merge without tagging, the system can no longer distinguish which domain produced a signal.

**Example:** Two chiplets emit metadata on separate channels. The board routes both through a shared I²C bus. Downstream, every tag looks identical — source identity is gone.

**Preservation rule:** Domain boundaries must be labeled at every merge point. If two domains share a bus, the bus protocol must carry a domain identifier. If it can't, the domains must not share the bus.

### 2. Clock Collapsing

Boards normalize timing. Multiple clock sources converge on PLLs, clock buffers, and distribution trees that produce a single, clean output. The problem: monotonic timestamps from different clock domains become meaningless once they're re‑clocked into a unified domain without mapping.

**Example:** A chip emits metadata timestamped against its local 100 MHz oscillator. The board re‑clocks the metadata bus to a 25 MHz system clock. The timestamp values survive — but their temporal meaning is now ambiguous.

**Preservation rule:** Clock domain crossings must preserve or annotate the source clock reference. Re‑clocking metadata is permitted only if the original clock domain identifier travels with the data.

### 3. Signal Normalization

Level shifters, buffers, and protocol translators normalize signals for board‑level compatibility. This is correct for functional data. For structural metadata, normalization can strip encoding that carries meaning.

**Example:** A chip uses voltage‑level encoding on a metadata pad to indicate lifecycle state (design / test / deploy). A level shifter normalizes the output to standard logic levels. The lifecycle encoding disappears.

**Preservation rule:** Metadata encoding schemes must be documented at the chip boundary. Level shifters and protocol translators on metadata paths must be verified to preserve — not just pass — the encoding.

### 4. Provenance Hiding

Boards aggregate, buffer, and batch signals for efficiency. Aggregation erases provenance — the downstream consumer sees a packet but cannot determine which source produced which component.

**Example:** Four sensor channels are multiplexed onto a single SPI bus. Each sensor has a source ID. The multiplexer strips the ID and adds a channel index. The channel index maps to a board layout position, not to the sensor's self‑declared identity. Provenance is now board‑dependent, not source‑declared.

**Preservation rule:** Aggregation must carry source‑declared identifiers through the aggregation boundary. Board‑assigned indices may coexist with source IDs but must never replace them.

---

## The Four Preservation Rules (Summary)

| #  | Rule                              | One‑liner                                                         |
|----|-----------------------------------|-------------------------------------------------------------------|
| 1  | **Label every merge**             | Domain boundaries must be identified at every convergence point.  |
| 2  | **Annotate every re‑clock**       | Clock domain crossings must carry the source clock reference.     |
| 3  | **Verify every translation**      | Protocol/level translators on metadata paths must preserve encoding. |
| 4  | **Carry provenance through aggregation** | Source‑declared IDs survive batching, buffering, and multiplexing. |

These four rules are the board‑level equivalent of the chip‑level design‑review checklist. They don't add behavior. They prevent erasure.

---

## Domain‑Specific Alignment

The Capture Source identifies four domains where board‑level alignment is not optional — because misalignment in these domains already causes failures that engineers debug as ghosts.

### Memory Hierarchy and Persistence Boundaries

Memory is not a flat bucket of bytes. It is a **layered substrate with phase transitions** at every boundary:

```
Register → L1 → L2 → L3 → DRAM → NVM → Storage
     ▲         ▲        ▲        ▲        ▲
     │         │        │        │        │
  phase     phase    phase    phase    phase
  boundary  boundary boundary boundary boundary
```

At each transition, three properties can silently collapse:

| Property       | What collapses                                                  | Consequence                                              |
|----------------|-----------------------------------------------------------------|----------------------------------------------------------|
| **Phase**      | Ephemeral vs. transactional vs. archival                        | Stale data masquerades as current truth                  |
| **Source**     | Which block, chiplet, or domain produced the value              | Values inherit false provenance from their container     |
| **Time**       | When the value was produced vs. when it was written to this tier| Temporal ordering becomes unreliable across tiers        |

**Board‑level alignment means:**
- Tag values with their phase at every persistence boundary.
- Preserve source lineage across cache → DRAM → NVM transitions.
- Distinguish write‑time from production‑time in every tier.

**What this is not:** This is not a coherence protocol. MESI, MOESI, and directory protocols handle cache coherence. This is **semantic coherence across time** — ensuring that a value's meaning doesn't silently change as it moves through the memory hierarchy.

### Power, Thermal, and Reliability Domains

These systems already make decisions that affect correctness:

| System         | Decision it makes                | What gets lost without alignment                          |
|----------------|----------------------------------|-----------------------------------------------------------|
| **Power**      | Throttling, gating, sleep states | Which lifecycle phase was active when power changed        |
| **Thermal**    | Migration, frequency scaling     | Whether a thermal event was cause or effect                |
| **Reliability**| Error correction, aging compensation | Whether a correction was structural or compensatory     |

When these layers are opaque, engineers debug ghosts. A throttling event looks like a performance bug. A thermal migration looks like a scheduling anomaly. An ECC correction looks like a memory error when it was actually an aging compensation.

**Board‑level alignment means:**
- Power state transitions tagged with lifecycle context.
- Thermal events preserved as first‑class structural signals, not side effects buried in management controller logs.
- Reliability interventions visible and source‑attributed rather than silently "fixed."

### I/O and Boundary Crossings

Every boundary crossing is a phase transition:

```
Sensor → Digital
Device → Host
Host → Network
Network → Storage
```

Each of these crossings can — and routinely does — flatten three things:

1. **Source identity.** The downstream side knows what connector the signal arrived on, not what produced it.
2. **Timing context.** Transit latency, buffering delay, and protocol overhead collapse the original temporal reference.
3. **Disagreement.** When multiple sources are aggregated, disagreement between them is averaged or arbitrated away. The downstream consumer sees consensus where none existed.

**Board‑level alignment means:**
- Source identity survives every crossing. Connectors carry provenance, not just payload.
- Timing context is annotated, not flattened. If a boundary adds 50 µs of latency, that's metadata, not noise.
- Aggregation preserves disagreement. If two sensors disagree, the disagreement is the signal. Averaging it away destroys information.

> *This is where systems most often lie without intending to.*

### Firmware and Microcode

Firmware is the most structurally dangerous layer on the board — because it can **rewrite history**.

Firmware already:
- **Patches behavior** — changing what hardware does after tape‑out.
- **Reinterprets hardware** — translating hardware signals into software abstractions.
- **Bridges eras of intent** — a firmware update can make yesterday's chip behave like tomorrow's design.

None of this is wrong. All of it is structurally invisible unless explicitly declared.

**Board‑level alignment means:**
- Firmware actions are **phase‑declared** — the system knows when firmware is acting and can distinguish firmware behavior from hardware behavior.
- Updates don't rewrite history — behavior changes are **lineage‑tracked**, not just versioned. Version 2.3.1 doesn't erase the fact that version 2.3.0 existed and produced data.
- Firmware‑mediated corrections are source‑attributed — if firmware "fixes" a hardware signal, both the original and the fix are observable.

---

## Board‑Level Design Review Checklist

Mirrors the chip‑level Internal Design‑Review Checklist from the Capture Source, extended to the board boundary.

### 1. Before Board Layout

- [ ] Identify all chip‑to‑board metadata interfaces (pads, pins, sideband channels).
- [ ] Confirm metadata paths are routed separately from functional data where possible.
- [ ] Verify that no metadata path shares a critical timing net.
- [ ] Document every point where domains merge on the board.
- [ ] Confirm clock domain crossings on metadata paths are annotated.

### 2. During Schematic Review

- [ ] Verify level shifters on metadata paths preserve encoding, not just voltage.
- [ ] Confirm multiplexers and aggregators carry source‑declared identifiers.
- [ ] Ensure power gating circuits do not erase metadata state.
- [ ] Verify reset domains do not clear metadata without explicit intent.
- [ ] Confirm debug headers/connectors do not re‑purpose metadata paths for control.

### 3. Connector and I/O Review

- [ ] Every external connector that carries metadata is documented.
- [ ] Connector protocols support or at least do not strip source identifiers.
- [ ] Timing annotations survive connector boundary (transit latency documented).
- [ ] Aggregated connectors preserve per‑source disagreement.

### 4. Firmware Integration Review

- [ ] Firmware actions on metadata paths are phase‑declared.
- [ ] Firmware updates are lineage‑tracked (version + timestamp + predecessor).
- [ ] Firmware‑mediated corrections preserve the original signal alongside the correction.
- [ ] Firmware cannot silently redirect metadata into functional control paths.

### 5. Power and Thermal Review

- [ ] Power state transitions on metadata‑carrying domains are tagged.
- [ ] Thermal events are logged as structural signals, not just management events.
- [ ] Reliability corrections (ECC, aging compensation) are source‑attributed.
- [ ] Sleep/hibernate states do not collapse metadata on resume.

### 6. Final Board Sign‑Off

- [ ] Re‑check BOM for components that flatten metadata (buffers, retimers, hubs).
- [ ] Confirm test points exist on at least one metadata path per domain.
- [ ] Verify metadata paths survive environmental testing (thermal cycling, vibration).
- [ ] Document any metadata path that was intentionally removed, with rationale.

### 7. The Board‑Level Review Question

> *"If a signal left the chip with its source, phase, and timestamp intact — does the board still know all three by the time it reaches the connector?"*

If the answer is **"yes, without special tooling,"** the board is aligned.

---

## Board Topology Diagrams

### Single‑SoC Board

```
┌──────────────────────────────────────────────────────────────┐
│  Board                                                       │
│                                                              │
│  ┌──────────────────────────┐                                │
│  │  SoC                     │                                │
│  │  ┌────────┐ ┌──────────┐ │                                │
│  │  │ Core A │ │ Accel B  │ │                                │
│  │  └───┬────┘ └────┬─────┘ │                                │
│  │      │           │       │                                │
│  │  ════╪═══════════╪════   │  ◄── Functional data paths     │
│  │      │           │       │                                │
│  │  ┄┄┄┄┼┄┄┄┄┄┄┄┄┄┄┄┼┄┄┄┄  │  ◄── Structural metadata      │
│  │  │ Meta A │ │ Meta B  │  │      (preserved from chip)     │
│  │  └───┬────┘ └────┬─────┘ │                                │
│  │      └─────┬─────┘       │                                │
│  │            │ Tag Bus     │                                │
│  └────────────┼─────────────┘                                │
│               │                                              │
│  ┌────────────▼─────────────────────────────────────────┐    │
│  │  Board‑Level Metadata Path                           │    │
│  │                                                      │    │
│  │  ┌────────────┐  ┌─────────────┐  ┌───────────────┐ │    │
│  │  │ Domain     │  │ Clock       │  │ Source ID     │ │    │
│  │  │ Labels     │  │ Annotations │  │ Passthrough   │ │    │
│  │  └────────────┘  └─────────────┘  └───────────────┘ │    │
│  └──────────────────────────┬───────────────────────────┘    │
│                             │                                │
│  ┌──────────────────────────▼───────────────────────────┐    │
│  │  External Connector (metadata‑preserving)            │    │
│  │  • Source ID intact                                  │    │
│  │  • Phase / lifecycle tag intact                      │    │
│  │  • Temporal reference annotated                      │    │
│  └──────────────────────────────────────────────────────┘    │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Multi‑Chip / Chiplet Board

```
┌──────────────────────────────────────────────────────────────┐
│  Board                                                       │
│                                                              │
│  ┌────────────────┐          ┌────────────────┐              │
│  │  Package A     │          │  Package B     │              │
│  │  (Compute)     │          │  (I/O + NVM)   │              │
│  │                │          │                │              │
│  │  Meta A₁ A₂   │          │  Meta B₁       │              │
│  └───┬────┬───────┘          └────┬───────────┘              │
│      │    │                       │                          │
│      │    │    ⚠ MERGE POINT      │                          │
│      │    └───────┬───────────────┘                          │
│      │            │                                          │
│      │  ┌─────────▼──────────────────────────────────┐       │
│      │  │  Board Aggregation Layer                   │       │
│      │  │                                            │       │
│      │  │  Rule 1: Domain labels at every merge      │       │
│      │  │  Rule 2: Clock annotations at every CDC    │       │
│      │  │  Rule 3: Encoding preserved, not flattened │       │
│      │  │  Rule 4: Source IDs carried, not replaced  │       │
│      │  └─────────┬──────────────────────────────────┘       │
│      │            │                                          │
│      └────────────┤                                          │
│                   │                                          │
│  ┌────────────────▼──────────────────────────────────┐       │
│  │  Connectors / System Interface                    │       │
│  │  • Per‑source provenance preserved                │       │
│  │  • Disagreement between A and B NOT averaged      │       │
│  │  • Transit latency annotated per path             │       │
│  └───────────────────────────────────────────────────┘       │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**How to read these diagrams:**
- **Solid lines (═══):** Functional data paths — unchanged, optimized as usual.
- **Dotted lines (┄┄┄):** Structural metadata paths — the subject of this document.
- **⚠ MERGE POINT:** Where the four preservation rules must be applied.
- Everything above the board aggregation layer is the chip's responsibility. Everything below is the board's. The aggregation layer is the contract boundary.

---

## What NOT to Align at the Board Level

The Capture Source draws a strict line between "align now" and "align later." At the board level, the same discipline applies:

### Do Not Align

| Layer                          | Why not                                                              |
|--------------------------------|----------------------------------------------------------------------|
| **Scheduling logic**           | Aligning board‑level scheduling before observability works encodes premature assumptions. |
| **Policy enforcement**         | Boards that enforce policy before they can observe structure become brittle. |
| **Cross‑domain semantics**     | Semantic interpretation at the board level is premature — let the system see before it decides. |
| **Behavioral optimization**    | If the board "helps" by interpreting metadata, it's no longer preserving — it's prescribing. |

### The Rule

> **The board's job is to preserve, not interpret.**

Interpretation belongs to the layers above — firmware (with phase declaration), software, and ultimately the Coherence Engine. The board is infrastructure. Good infrastructure carries everything and decides nothing.

---

## Relationship to Other D369 Files

| File                        | Relationship                                                        |
|-----------------------------|---------------------------------------------------------------------|
| `Capture_Source.md`         | Source of mainboard failure modes, alignment layering, memory rails  |
| `Adoption_Roadmap.md`      | Phase 2 (Silicon Reservation) gates Phase 2+ board‑level alignment  |
| `Structural_Observability.md` | Chip‑level counterpart — defines what the chip preserves           |
| `Memory_Alignment.md`      | Deep‑dive on memory hierarchy alignment referenced in §Memory       |
| `Design_Review_Checklist.md`| Chip‑level checklist that this document extends to the board        |
| `Firmware_Lineage.md`      | Detailed firmware phase‑declaration and lineage‑tracking rules      |

---

## Common Failure Modes (Reference)

A quick‑scan table for board reviewers:

| Failure Mode                               | Symptom                                          | Root Cause                              | Prevention                               |
|--------------------------------------------|--------------------------------------------------|-----------------------------------------|------------------------------------------|
| Source ID stripped at multiplexer           | All metadata looks like it came from one source  | MUX replaces source ID with channel index | Rule 4: carry provenance through aggregation |
| Timestamp re‑clocked without annotation    | Temporal ordering breaks across domains          | CDC strips clock domain reference       | Rule 2: annotate every re‑clock          |
| Level shifter flattens lifecycle encoding  | Lifecycle state reads as static logic level      | Encoding was voltage‑based, shifter normalizes | Rule 3: verify every translation    |
| Power gating erases metadata on resume     | Metadata channels read zero after wake           | Retention cells not specified for metadata | Checklist §5: sleep states preserve metadata |
| Debug header repurposed as control path    | Metadata flows backward into functional logic    | Board designer used available pins      | Checklist §2: debug paths stay read‑only |
| Firmware update overwrites telemetry history| Pre‑update behavior becomes unrecoverable       | Firmware versioned but not lineage‑tracked | Checklist §4: lineage‑tracked updates   |
| Sensor disagreement averaged at aggregator | System reports false consensus                   | Aggregation protocol computes mean      | Rule 4 + §I/O: preserve disagreement    |
| Reset domain clears temporal context       | Monotonic counter restarts from zero             | Reset scope too broad                   | Checklist §2: reset domains scoped       |

---

## The Board‑Level Alignment Principle

Everything in this document follows one principle, inherited from the Capture Source:

> **Align only what already decides outcomes. Observe everything else.**

At the board level, this translates to:

- **Memory, power, thermal, I/O, firmware** already decide outcomes → align them.
- **Scheduling, policy, semantics, optimization** only inform understanding → leave them observable, not aligned.
- **The board itself** is infrastructure → it preserves, it does not interpret.

A well‑aligned board is one where an engineer can trace a signal from the chip's metadata channel to the external connector and confirm:

> *"The source, the phase, and the timestamp are all still here — and nothing on the board changed them."*

That's the bar. Nothing more. Nothing less.

---

## Canon Alignment

| Check                | Status |
|----------------------|--------|
| Zero drift           | ✅ All content derived from Capture_Source.md mainboard and alignment sections |
| Structural contract  | ✅ Role: engine + diagnostic — core preservation logic with validation checklists |
| Lineage clean        | ✅ Every failure mode, rule, and domain traceable to capture source |
| Student‑ready        | ✅ Failure modes as concrete examples; diagrams with reading guides; one‑liner rules |
| AI‑parsable          | ✅ Tabular rules, checklists, failure‑mode reference; structured cross‑references |
| Cross‑module refs    | ✅ Imports from Capture_Source; extends chip‑level checklist; feeds Adoption_Roadmap Phase 2+ |
| Non‑claims preserved | ✅ "Preserve, not interpret" — board explicitly scoped away from semantic decisions |

---

*Module: D369_Chip_Spec · File: Board_Level_Alignment.md · Version: 0.1.0 · TriadicFrameworks / RTT*

---

**What makes this file structurally distinct from the others:**

- **Four named preservation rules** distill the entire Capture Source mainboard section into engineer‑scannable one‑liners — these are the board‑level equivalent of the three‑page chip contract.
- **Domain‑specific sections** (Memory, Power/Thermal, I/O, Firmware) each follow the same pattern: what the domain already does → what collapses without alignment → what alignment means here. Directly traceable to Capture Source.
- **Board‑level design review checklist** extends the chip‑level checklist across the board boundary, with its own sign‑off question: *"Does the board still know source, phase, and timestamp at the connector?"*
- **Failure modes reference table** gives board reviewers a quick‑scan diagnostic — symptom → root cause → which rule prevents it.
- **"Do Not Align" section** enforces the same discipline as the Adoption Roadmap's alignment layering: the board preserves, it does not interpret.
