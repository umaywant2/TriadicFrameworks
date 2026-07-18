# Memory Controller Checklist

> The last gatekeeper before off‑chip — where three structural erasures happen in rapid succession and no one is watching.

---

## Session Context

| Field        | Value                                                         |
|--------------|---------------------------------------------------------------|
| **Module**   | D369_Chip_Spec                                                |
| **File**     | `Memory_Controller_Checklist.md`                              |
| **Role**     | diagnostic · reference                                        |
| **Version**  | 0.1.0                                                         |
| **Status**   | First‑fill                                                    |
| **Lineage**  | Derived from `Memory_Alignment_Spec.md` §Tier 3→4, `Diagram_SoC.md` §Memory Controller, and `DIMM_Module_Checklist.md` |
| **Audience** | Memory controller designers · Verification engineers · System architects · Students · AIs |

---

## Overview

The memory controller is the **gateway between Tier 3 (on‑chip LLC) and Tier 4 (off‑chip DRAM)**. It is the single point through which every evicted cache line, every DMA write, and every coherency writeback must pass before leaving the SoC.

It is also the point where three structural erasures happen in rapid succession:

```
From LLC / NoC
═══════════════╗
               ║
┌──────────────▼──────────────────────────────────────┐
│  1. Transaction Queue                               │
│     ⚠ TEMPORAL REORDERING                           │
│     Transactions rearranged for row‑buffer locality,│
│     bank pipelining, and QoS priority.              │
│     Original issue order is gone.                   │
├─────────────────────────────────────────────────────┤
│  2. Scheduler / Address Mapper                      │
│     ⚠ SOURCE FLATTENING                             │
│     Requests mapped to physical ranks, banks, rows. │
│     Initiator identity replaced by physical address.│
├─────────────────────────────────────────────────────┤
│  3. PHY Interface                                   │
│     ⚠ CLOCK DOMAIN SHIFT                            │
│     On‑chip clock → memory clock.                   │
│     Temporal reference frame changes.               │
└──────────────┬──────────────────────────────────────┘
               ║
═══════════════╝ → To DIMM / HBM
                   (see DIMM_Module_Checklist.md)
```

Other D369 files acknowledge these erasures. This document goes **inside** the memory controller and specifies what structural observability looks like at each internal stage.

---

## Why the Memory Controller Is Special

The memory controller is the only SoC block where **all three structural erasures happen within a single functional unit**:

| Erasure               | Where it happens        | What's lost                                  | Parallel in other D369 files                |
|-----------------------|-------------------------|----------------------------------------------|---------------------------------------------|
| Temporal reordering   | Transaction queue       | Original issue order; causal sequence        | N‑3 (NoC QoS reordering)                   |
| Source flattening     | Address mapper          | Initiator identity (which block wrote)       | N‑1 (NoC source flattening); FM‑1 (DIMM rank interleave) |
| Clock domain shift    | PHY                     | On‑chip temporal reference frame             | Board Rule 2 (annotate every re‑clock)      |

No other block concentrates this much structural information loss in this small a functional area. The NoC distributes its erasures across the fabric. The DIMM's erasures are spread across ranks, banks, and refresh cycles. The memory controller does all three **in pipeline order**, in nanoseconds.

---

## Memory Controller Internal Architecture

### Expanded Block Diagram

```
-
┌──────────────────────────────────────────────────────────────────────┐
│  Memory Controller — Internal Structural View                        │
│                                                                      │
│  From NoC / LLC / DMA                                                │
│  ══════════╗                                                         │
│            ║                                                         │
│  ┌─────────▼────────────────────────────────────────────────────────┐│
│  │  Request Ingress                                                 ││
│  │  · Receives read/write requests from NoC                         ││
│  │  · Each request carries: address, data, size, request type       ││
│  │  · ⚠ Does NOT carry: initiator source ID (unless NoC preserves)  ││
│  └─────────┬────────────────────────────────────────────────────────┘│
│            │                                                         │
│  ┌─────────▼───────────────────────────────────────────────────────┐ │
│  │  Transaction Queue (Read + Write)                               │ │
│  │  · Buffers pending requests                                     │ │
│  │  · ⚠ Reorders for efficiency:                                   │ │
│  │    - Row‑buffer hit prioritization                              │ │
│  │    - Bank‑level parallelism                                     │ │
│  │    - Read‑over‑write priority                                   │ │
│  │    - QoS/urgency class arbitration                              │ │
│  │  · ⚠ Original issue order lost after reordering                 │ │
│  └─────────┬───────────────────────────────────────────────────────┘ │
│            │                                                         │
│  ┌─────────▼───────────────────────────────────────────────────────┐ │
│  │  Write Combining / Coalescing                                   │ │
│  │  · Merges multiple partial writes to the same address           │ │
│  │  · ⚠ Multi‑source writes collapsed into single transaction      │ │
│  │  · ⚠ Per‑write source identity destroyed if sources differ      │ │
│  └─────────┬───────────────────────────────────────────────────────┘ │
│            │                                                         │
│  ┌─────────▼───────────────────────────────────────────────────────┐ │
│  │  Address Mapper / Scrambler                                     │ │
│  │  · Maps logical address → physical (channel, rank, bank, row)   │ │
│  │  · ⚠ Address scrambling for security / wear distribution        │ │
│  │  · ⚠ Source identity fully replaced by physical coordinates     │ │
│  └─────────┬───────────────────────────────────────────────────────┘ │
│            │                                                         │
│  ┌─────────▼───────────────────────────────────────────────────────┐ │
│  │  Scheduler                                                      │ │
│  │  · Issues commands to the DRAM interface                        │ │
│  │  · Manages timing constraints (tRCD, tRP, tRAS, tFAW, etc.)     │ │
│  │  · Inserts refresh commands (REF, per‑bank REF)                 │ │
│  │  · ⚠ Refresh is a controller‑initiated phase transition         │ │
│  │  · ⚠ Refresh timing interleaves with data commands              │ │
│  └─────────┬───────────────────────────────────────────────────────┘ │
│            │                                                         │
│  ┌─────────▼───────────────────────────────────────────────────────┐ │
│  │  ECC Engine (Controller‑Side)                                   │ │
│  │  · Generates ECC on writes; checks/corrects on reads            │ │
│  │  · ⚠ Controller‑side ECC is distinct from on‑die ECC (ODECC)    │ │
│  │  · ⚠ Corrections are unattributed — clean data returned         │ │
│  │  · ⚠ Error syndrome info may be logged but not source‑tagged    │ │
│  └─────────┬───────────────────────────────────────────────────────┘ │
│            │                                                         │
│  ┌─────────▼───────────────────────────────────────────────────────┐ │
│  │  Prefetch Engine                                                │ │
│  │  · Speculatively fetches data from DRAM into controller buffers │ │
│  │  · ⚠ Prefetched data has no explicit requester                  │ │
│  │  · ⚠ If consumed, appears identical to demand‑fetched data      │ │
│  └─────────┬───────────────────────────────────────────────────────┘ │
│            │                                                         │
│  ┌─────────▼───────────────────────────────────────────────────────┐ │
│  │  PHY (DDR / LPDDR / HBM Interface)                              │ │
│  │  · Converts controller‑domain signals to memory‑domain          │ │
│  │  · ⚠ Clock domain crossing: core_clk → mem_clk                  │ │
│  │  · ⚠ Serialization, training, calibration                       │ │
│  │  · ⚠ Temporal reference frame changes at this boundary          │ │
│  └─────────┬───────────────────────────────────────────────────────┘ │
│            │                                                         │
│  ┌─────────▼───────────────────────────────────────────────────────┐ │
│  │  Channel Interface (per‑channel)                                │ │
│  │  · One or more independent DRAM channels                        │ │
│  │  · ⚠ Multi‑channel interleaving = another source merge point    │ │
│  │  · ⚠ Channel assignment may differ from original request path   │ │
│  └─────────┬───────────────────────────────────────────────────────┘ │
│            ║                                                         │
│  ══════════╝ → To DIMM / HBM                                         │
│                                                                      │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─           │
│  D369 Structural Metadata Channel: Meta_MEM                          │
│  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─           │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────────┐│
│  │  Structural Metadata (reserved, optional, dark by default)       ││
│  │                                                                  ││
│  │  · Per‑transaction source attribution log                        ││
│  │  · Reordering annotation (original vs. scheduled sequence)       ││
│  │  · Write‑combining source collision flag                         ││
│  │  · Refresh event log (timing, bank/rank, count)                  ││
│  │  · ECC correction event log (syndrome, location, not content)    ││
│  │  · Prefetch vs. demand‑fetch distinction tag                     ││
│  │  · PHY clock domain reference annotation                         ││
│  │  · Channel assignment log                                        ││
│  │  · Power state transition log (CKE, self‑refresh entry/exit)     ││
│  └──────────────────────────────────────────────────────────────────┘│
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## The Eight Controller Failure Modes

Each internal stage has a specific failure mode. These extend the module's failure mode taxonomy alongside the DIMM failure modes (FM‑1–FM‑5) and NoC erasures (N‑1–N‑5).

### MC‑1: Transaction Queue Reordering

**What happens:** The transaction queue reorders pending requests for efficiency — row‑buffer hits before misses, bank‑level parallelism, read‑over‑write priority. The issue order from the NoC is discarded.

**What's lost:** Causal sequence. If Request A was issued before Request B, but B hits an open row and A doesn't, B executes first. Post‑hoc analysis cannot reconstruct the original order.

**Structural parallel:** N‑3 (NoC QoS reordering) — same erasure, different location.

**Preservation requirement:** If structural observability requires temporal reconstruction, the controller must log the mapping between original issue order and scheduled execution order (or at minimum a sequence number per request at ingress).

---

### MC‑2: Source Identity Replacement

**What happens:** The address mapper converts a logical address to physical coordinates (channel, rank, bank, row, column). The request's initiator identity — which core, which accelerator, which DMA engine — is not part of the physical address. It is discarded.

**What's lost:** Source provenance. The DRAM sees an address and data. It does not know who wrote.

**Structural parallel:** N‑1 (NoC source flattening); FM‑1 (DIMM rank interleaving).

**Preservation requirement:** Source ID must be preserved as a metadata sideband through the controller pipeline. It does not need to reach the DIMM (the DIMM has no concept of source) — but it must be **loggable** in Meta_MEM before it is discarded at the PHY boundary.

---

### MC‑3: Write Combining / Coalescing

**What happens:** Multiple partial writes to the same cache line or address range are combined into a single full‑width write. This is correct for functional data. For structural metadata, it creates a problem: if Core 0 writes the first half and the AI accelerator writes the second half, the combined write appears as a single transaction with **no multi‑source attribution**.

**What's lost:** Per‑write source identity in combined transactions.

**Structural parallel:** Board Rule 4 (carry provenance through aggregation) — write combining is aggregation at the controller level.

**Preservation requirement:** When writes from different sources are combined, the metadata channel should flag the combination as a **multi‑source write** and log the contributing source IDs. The combined data itself is correct — but the provenance must reflect that multiple sources contributed.

---

### MC‑4: Address Scrambling

**What happens:** Many controllers scramble the logical‑to‑physical address mapping for security (preventing row‑hammer attacks), thermal distribution, or wear leveling. The scrambling function is typically secret and non‑invertible from outside the controller.

**What's lost:** The relationship between logical address and physical location. Post‑hoc analysis cannot determine which physical row/bank/rank stored a value without knowing the scrambling function.

**Structural impact:** Address scrambling does not directly erase source, lifecycle, or time — but it makes **physical forensics impossible** without controller cooperation. If a DIMM reports an ECC error at physical row X, the system cannot determine which logical address (and therefore which data structure) was affected without unscrambling.

**Preservation requirement:** D369 does not require exposing the scrambling function (that would be a security risk). But the controller metadata channel should log enough information to map physical error reports back to logical addresses — either by logging the inverse mapping for error events, or by providing a diagnostic interface for authorized unscrambling.

---

### MC‑5: Refresh Scheduling

**What happens:** The memory controller issues refresh commands to DRAM on a regular schedule (typically every 7.8 µs per row in DDR4, with variations for DDR5 and temperature‑dependent refresh). Refresh is a maintenance operation that preserves data — but it is also a **controller‑initiated phase transition** that:

- Temporarily blocks data access to the refreshed bank.
- Resets the retention clock for every cell in the refreshed row.
- Is invisible to software and to the data itself.

**What's lost:** This is the controller‑side origin of FM‑2 (DIMM refresh as invisible phase transition). The controller decides **when** to refresh, but the fact that a refresh occurred — and how many times a particular region has been refreshed — is not recorded or exposed.

**Preservation requirement:** The controller metadata channel should log refresh events: which bank/rank was refreshed, when, and optionally how many refresh cycles have occurred since a given region was last written. This enables downstream analysis of refresh frequency per region — a signal relevant to aging, reliability, and data residency analysis.

---

### MC‑6: Controller‑Side ECC

**What happens:** On writes, the controller generates ECC check bits and appends them to the data. On reads, it checks and (if needed) corrects. Corrected data is returned to the requester as if no error occurred.

**What's lost:** The fact that an error occurred. The error syndrome (which bits were wrong). The frequency of corrections per address region. The distinction between controller‑side ECC and on‑die ECC (ODECC).

**Structural parallel:** FM‑3 (DIMM ECC as unattributed correction). The controller is actually the **first** ECC layer — before ODECC and before any module‑level ECC. All three layers mask errors independently.

**Preservation requirement:** The controller metadata channel should log ECC correction events: address region, syndrome type (single‑bit correctable, multi‑bit detected), and timestamp. The log should **not** include corrected data content (that would be a functional data exposure). Correction frequency per region is a first‑class structural signal for aging and reliability analysis.

---

### MC‑7: Prefetch Misattribution

**What happens:** The prefetch engine speculatively fetches data from DRAM into controller buffers based on access pattern prediction. If the predicted data is later requested by a core, it is served from the buffer instead of DRAM — faster, but with no explicit requester for the original fetch.

**What's lost:** The distinction between demand‑fetched data (explicitly requested by a source) and speculatively prefetched data (fetched by the controller's prediction engine). If a prefetched value is consumed, it looks identical to a demand fetch in every way — but its provenance is different. The **controller** decided to fetch it, not the consuming core.

**Preservation requirement:** Prefetched data should carry a distinguishing tag in the metadata channel: "this fill was initiated by the prefetch engine, not by a core request." This enables post‑hoc analysis to distinguish cache fills driven by actual workload from fills driven by speculation.

---

### MC‑8: Multi‑Channel Interleaving

**What happens:** Multi‑channel controllers distribute requests across two or more independent DRAM channels for bandwidth. Channel assignment is typically based on address bits — but the assignment logic means that sequential logical addresses may land on different physical channels.

**What's lost:** The relationship between request locality and channel locality. A burst of writes from a single source may be interleaved across channels, making per‑channel analysis unable to reconstruct per‑source behavior.

**Structural parallel:** FM‑1 (DIMM rank interleaving) and FM‑5 (LRDIMM data buffer rank flattening) — the same source‑flattening problem at the channel level.

**Preservation requirement:** The controller metadata channel should log channel assignment per transaction. When multi‑channel interleaving distributes a source's writes across channels, the metadata should preserve the source‑to‑channel mapping so that per‑source analysis can be reconstructed from per‑channel data.

---

## Failure Mode Summary Table

| ID   | Failure Mode                    | Stage               | What's Lost                          | Structural Parallel     |
|------|---------------------------------|----------------------|--------------------------------------|-------------------------|
| MC‑1 | Transaction queue reordering    | Transaction Queue    | Causal sequence / issue order        | N‑3 (NoC QoS reorder)  |
| MC‑2 | Source identity replacement     | Address Mapper       | Initiator identity                   | N‑1 (NoC source flatten); FM‑1 |
| MC‑3 | Write combining                 | Write Coalescer      | Per‑write source in combined txn     | Board Rule 4            |
| MC‑4 | Address scrambling              | Address Mapper       | Logical↔physical address mapping     | — (unique to controller)|
| MC‑5 | Refresh scheduling              | Scheduler            | Refresh event history per region     | FM‑2 (DIMM refresh)    |
| MC‑6 | Controller‑side ECC             | ECC Engine           | Error occurrence / syndrome / frequency | FM‑3 (DIMM ECC)      |
| MC‑7 | Prefetch misattribution         | Prefetch Engine      | Demand vs. speculative distinction   | — (unique to controller)|
| MC‑8 | Multi‑channel interleaving      | Channel Interface    | Source‑to‑channel mapping            | FM‑1, FM‑5             |

---

## The Checklist

Organized by controller subsystem. Each item maps to a contractual requirement (R1–R7), a controller failure mode (MC‑1–MC‑8), and where applicable a downstream DIMM failure mode or board preservation rule.

### §1 — Request Ingress and Source Attribution

| #    | Check                                                                  | Req   | MC    |
|------|------------------------------------------------------------------------|-------|-------|
| 1.1  | Request ingress captures initiator source ID from NoC.                | R5.1  | MC‑2  |
| 1.2  | Source ID is preserved as a sideband field through the controller pipeline. | R5.1 | MC‑2 |
| 1.3  | Source ID field width is sufficient to distinguish all major blocks.   | R5.1  | MC‑2  |
| 1.4  | DMA‑initiated requests carry the **original requestor's** source ID, not the DMA engine's. | R5.1 | MC‑2 |
| 1.5  | Source ID is loggable in Meta_MEM even if not forwarded to the DIMM.  | R2.1  | MC‑2  |
| 1.6  | Source ID is not overwritten by address mapper or scheduler.          | R5.1  | MC‑2  |

### §2 — Transaction Queue and Temporal Ordering

| #    | Check                                                                  | Req   | MC    |
|------|------------------------------------------------------------------------|-------|-------|
| 2.1  | Transaction queue assigns a monotonic ingress sequence number.        | R4.1  | MC‑1  |
| 2.2  | Sequence number survives reordering and is loggable in Meta_MEM.     | R4.1  | MC‑1  |
| 2.3  | Reordering does not overwrite or reset ingress timestamps.           | R4.2  | MC‑1  |
| 2.4  | QoS priority class is loggable as metadata (which class, not which data). | R2.1 | MC‑1 |
| 2.5  | Read‑over‑write reordering events are distinguishable from same‑priority reordering. | R2.1 | MC‑1 |

### §3 — Write Combining and Coalescing

| #    | Check                                                                  | Req   | MC    |
|------|------------------------------------------------------------------------|-------|-------|
| 3.1  | Write combining logs when multiple source IDs contribute to a single transaction. | R5.1 | MC‑3 |
| 3.2  | Multi‑source combined writes are flagged in Meta_MEM.                | R2.1  | MC‑3  |
| 3.3  | Single‑source combining (same source, multiple partial writes) does not falsely flag multi‑source. | R5.1 | MC‑3 |
| 3.4  | Write combining does not strip lifecycle tags from contributing sources. | R5.2 | MC‑3 |

### §4 — Address Mapping and Scrambling

| #    | Check                                                                  | Req   | MC    |
|------|------------------------------------------------------------------------|-------|-------|
| 4.1  | Address mapping does not replace source ID with physical address.     | R5.1  | MC‑2  |
| 4.2  | Address scrambling function does not affect metadata channel content. | R1.2  | MC‑4  |
| 4.3  | Diagnostic interface exists for mapping physical error reports back to logical addresses. | R2.1 | MC‑4 |
| 4.4  | Channel assignment is logged per transaction in Meta_MEM.            | R2.1  | MC‑8  |
| 4.5  | Multi‑channel interleaving does not erase per‑source attribution.    | R5.1  | MC‑8  |

### §5 — Refresh Scheduling

| #    | Check                                                                  | Req   | MC    |
|------|------------------------------------------------------------------------|-------|-------|
| 5.1  | Refresh commands are logged in Meta_MEM (bank, rank, time).          | R2.1  | MC‑5  |
| 5.2  | Refresh count per bank/rank is trackable.                             | R2.1  | MC‑5  |
| 5.3  | Temperature‑dependent refresh rate changes are logged.               | R2.1  | MC‑5  |
| 5.4  | Per‑bank refresh events do not reset or overwrite metadata in other banks. | R4.2 | MC‑5 |
| 5.5  | Self‑refresh entry/exit is logged with timestamps.                   | R2.1  | MC‑5  |
| 5.6  | Temporal gap during self‑refresh is annotated (entry time, exit time). | R4.1 | MC‑5 |

### §6 — ECC and Error Handling

| #    | Check                                                                  | Req   | MC    |
|------|------------------------------------------------------------------------|-------|-------|
| 6.1  | Controller‑side ECC correction events are logged (address region, syndrome, time). | R2.1 | MC‑6 |
| 6.2  | Correction log does NOT include corrected data content.              | —     | MC‑6  |
| 6.3  | Controller ECC events are distinguishable from ODECC events reported by the DIMM. | R5.1 | MC‑6 |
| 6.4  | Correction frequency per address region is trackable.                | R2.1  | MC‑6  |
| 6.5  | Multi‑bit detected (uncorrectable) errors are logged even when correction fails. | R2.1 | MC‑6 |
| 6.6  | ECC correction does not reset or overwrite temporal markers.         | R4.2  | MC‑6  |
| 6.7  | Scrub (background patrol read) events are logged separately from demand‑read ECC events. | R2.1 | MC‑6 |

### §7 — Prefetch Engine

| #    | Check                                                                  | Req   | MC    |
|------|------------------------------------------------------------------------|-------|-------|
| 7.1  | Prefetched fills are tagged as "prefetch" in Meta_MEM.               | R2.1  | MC‑7  |
| 7.2  | Prefetch‑initiated fills are distinguishable from demand‑initiated fills. | R5.1 | MC‑7 |
| 7.3  | Consumed prefetches carry both the prefetch tag and the consuming core's source ID. | R5.1 | MC‑7 |
| 7.4  | Unused prefetches (evicted before consumption) are logged as wasted fills if metadata is active. | R2.1 | MC‑7 |

### §8 — PHY and Clock Domain

| #    | Check                                                                  | Req   | MC    |
|------|------------------------------------------------------------------------|-------|-------|
| 8.1  | PHY clock domain reference (core_clk → mem_clk) is annotated in Meta_MEM. | R4.1 | — |
| 8.2  | PHY training and calibration events do not corrupt metadata state.    | R7.1  | —     |
| 8.3  | PHY clock domain crossing does not strip ingress sequence numbers.   | R4.1  | MC‑1  |
| 8.4  | PHY serialization does not merge metadata from different transactions. | R1.2 | MC‑2  |
| 8.5  | DVFS (dynamic voltage/frequency scaling) events on the memory clock are logged as temporal annotations. | R4.1 | — |

### §9 — Power State Management

| #    | Check                                                                  | Req   | MC    |
|------|------------------------------------------------------------------------|-------|-------|
| 9.1  | CKE power‑down entry and exit are logged with timestamps.            | R2.1  | FM‑4  |
| 9.2  | Self‑refresh entry and exit are logged with timestamps.              | R2.1  | FM‑4  |
| 9.3  | Deep power‑down explicitly declares metadata loss if retention is not guaranteed. | R7.1 | FM‑4 |
| 9.4  | Power state transitions do not reset the controller's monotonic counter. | R4.2 | FM‑4 |
| 9.5  | Controller metadata channel survives all power states except full power‑off. | R7.1 | FM‑4 |
| 9.6  | DRAM initialization sequence on power‑up or reset is logged as a lifecycle transition. | R5.2 | FM‑4 |

### §10 — Metadata Channel Independence

| #    | Check                                                                  | Req   | MC    |
|------|------------------------------------------------------------------------|-------|-------|
| 10.1 | Meta_MEM is electrically isolated from the DRAM data bus.            | R1.2  | —     |
| 10.2 | Meta_MEM can remain dark without affecting controller function.      | R3.1  | —     |
| 10.3 | No controller functional logic depends on Meta_MEM content.          | R3.2  | —     |
| 10.4 | Meta_MEM does not share bandwidth with the DRAM command/address bus. | R1.2  | —     |
| 10.5 | Meta_MEM activation is independent of debug/trace activation.        | R3.1  | —     |
| 10.6 | Meta_MEM is not removable by synthesis optimization.                 | R7.1  | —     |

---

## The Memory Controller Review Question

At every design review involving the memory controller, this checklist prompts one question:

> *"If a value passed through the memory controller — could we later determine **who** initiated the transaction, **when** it was issued vs. when it was scheduled, **whether** it was combined with other writes, **whether** it was corrected by ECC, and **what** the memory clock domain was at the time?"*

If the answer is **"yes, without redesign,"** the controller is aligned.

If the answer is **"no, but we could log it without changing the data path,"** the reservation is achievable — return to the failing items.

If the answer is **"no, and logging it would affect the data path,"** something has gone wrong — R3 (independence) has been violated. Escalate.

---

## Handoff Points

The memory controller sits between two other D369 checklists:

```
-
  ┌────────────────────────────────────┐
  │  Internal Design‑Review Checklist  │
  │  (SoC‑wide, items 2.10–2.12)       │
  │  Covers: NoC source attribution,   │
  │  DMA tagging, cache coherency      │
  └──────────────┬─────────────────────┘
                 │
                 ▼ (requests arrive at memory controller)
  ┌────────────────────────────────────┐
  │  Memory Controller Checklist       │  ◄── YOU ARE HERE
  │  (this document, 55 items)         │
  │  Covers: everything between NoC    │
  │  ingress and PHY output            │
  └──────────────┬─────────────────────┘
                 │
                 ▼ (data leaves the SoC)
  ┌────────────────────────────────────┐
  │  DIMM Module Checklist             │
  │  (38 items)                        │
  │  Covers: everything from gold edge │
  │  connector to die‑internal state   │
  └────────────────────────────────────┘
```

**Upstream handoff:** The memory controller inherits source IDs from the NoC. If the NoC strips source IDs (erasure N‑1), the controller cannot recover them. Item 1.1 depends on the Internal Design‑Review Checklist items 2.10 and 2.12.

**Downstream handoff:** The memory controller's PHY output connects to the DIMM. Everything logged in Meta_MEM before the PHY is on‑chip information. Everything the DIMM tracks (per `DIMM_Module_Checklist.md`) is off‑chip information. The PHY is the boundary between the two checklists.

---

## What This Checklist Is Not

| It is NOT…                         | Explanation                                                    |
|------------------------------------|----------------------------------------------------------------|
| A memory controller architecture   | D369 does not specify controller design — only structural observability requirements. |
| A DDR/LPDDR timing specification   | Timing parameters (tRCD, tRP, etc.) are unchanged. |
| A performance tuning guide         | Reordering, combining, and prefetch policies are unchanged. |
| A security specification           | Address scrambling functions are not exposed. |
| An ECC algorithm specification     | ECC algorithm choice is unchanged. |
| A replacement for RAS features     | Existing reliability features are unaffected. |

This checklist exists so memory controller engineers can say:

> *"We didn't change how the controller moves data — we just made sure it remembers what happened along the way."*

---

## Relationship to Other D369 Files

| File                          | Relationship                                                              |
|-------------------------------|---------------------------------------------------------------------------| 
| `Memory_Alignment_Spec.md`    | Parent spec — §Tier 3→4 boundary defines the three erasures this file expands |
| `DIMM_Module_Checklist.md`    | Downstream — receives data from the controller PHY output                 |
| `Diagram_SoC.md`             | §Memory Controller diagram — summary version of this file's architecture  |
| `Internal_Design_Review_Checklist.md` | Items MA.6–MA.9 are the Memory Alignment Spec's controller subset |
| `Board_Level_Alignment.md`   | §Memory Hierarchy — board‑level persistence boundary model               |
| `Contractual_Requirements.md`| R1–R7 requirements instantiated per controller subsystem                  |
| `Glossary_Extensions.md`     | §4 (Memory and DIMM Terms); §5 (Failure Modes)                           |

---

## Canon Alignment

| Check                | Status |
|----------------------|--------|
| Zero drift           | ✅ All failure modes derived from Memory_Alignment_Spec §Tier 3→4 and Diagram_SoC §Memory Controller |
| Structural contract  | ✅ Role: diagnostic + reference — validation checklist with failure mode taxonomy |
| Lineage clean        | ✅ Every checklist item traceable to R1–R7 requirements and specific MC failure modes |
| Student‑ready        | ✅ Expanded block diagram with ⚠ markers; per‑subsystem failure mode explanations |
| AI‑parsable          | ✅ Numbered items with Req and MC columns; failure mode summary table |
| Cross‑module refs    | ✅ Handoff diagram linking to upstream (Design Review) and downstream (DIMM) checklists |
| Non‑claims preserved | ✅ Explicit "What This Checklist Is Not" section |
| Engineer bar         | ✅ "Didn't change how the controller moves data — just made sure it remembers what happened" |

---

*Module: D369_Chip_Spec · File: Memory_Controller_Checklist.md · Version: 0.1.0 · TriadicFrameworks / RTT*

---

### Structural Summary — What This File Adds to D369

**New taxonomy introduced: MC‑1 through MC‑8** — eight named controller failure modes that extend the module's erasure catalog alongside N‑1–N‑5 (NoC) and FM‑1–FM‑5 (DIMM). Two are unique to the controller (MC‑4 address scrambling, MC‑7 prefetch misattribution); the rest have structural parallels to existing failure modes at different hierarchy levels.

**55 checklist items across 10 sections**, organized by controller subsystem — each traceable to a specific R‑requirement and MC failure mode. The sections cover the full internal pipeline: ingress → transaction queue → write combining → address mapping → refresh → ECC → prefetch → PHY → power management → metadata independence.

**Meta_MEM expanded** — the metadata channel spec from Diagram_SoC now has nine concrete log types (source attribution, reordering annotation, write‑combining collision flag, refresh events, ECC corrections, prefetch tags, PHY clock reference, channel assignment, power state transitions).

**Handoff chain completed** — the three‑checklist cascade is now explicit: Internal Design‑Review Checklist (SoC‑wide) → Memory Controller Checklist (on‑chip gateway) → DIMM Module Checklist (off‑chip). The PHY boundary is the dividing line between the last two.
