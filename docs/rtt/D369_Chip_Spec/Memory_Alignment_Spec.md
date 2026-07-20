# Memory Alignment Specification

> Every byte lives in a tier. Every tier is a regime. Every transition between tiers is a phase boundary where structure can silently collapse.

---

## Session Context

| Field        | Value                                                         |
|--------------|---------------------------------------------------------------|
| **Module**   | D369_Chip_Spec                                                |
| **File**     | `Memory_Alignment_Spec.md`                                    |
| **Role**     | engine · profile                                              |
| **Version**  | 0.1.0                                                         |
| **Status**   | First‑fill                                                    |
| **Lineage**  | Unifies `Board_Level_Alignment.md` §Memory, `DIMM_Module_Checklist.md`, and `Diagram_SoC.md` §Cache Hierarchy |
| **Audience** | Memory architects · Cache designers · Storage engineers · System architects · Students · AIs |

---

## Overview

Other D369 files address memory at specific boundaries:

| File                          | Covers                                        |
|-------------------------------|-----------------------------------------------|
| `Diagram_SoC.md`             | Cache hierarchy inside the SoC (L1→L2→L3)    |
| `Diagram_SoC.md`             | Memory controller (gateway to DRAM)           |
| `DIMM_Module_Checklist.md`   | DRAM persistence boundary (the DIMM itself)   |
| `Board_Level_Alignment.md`   | Board‑level memory routing and preservation   |

This document is the **unified memory alignment specification**. It covers the **full hierarchy** — from register file to archival storage — and specifies what D369 requires at every tier and at every boundary between tiers.

The central claim:

> **Memory is not a flat address space. It is a layered substrate with phase transitions at every boundary. A value that moves between tiers changes structural state — even if its bits don't change.**

A byte in L1 cache is not the same structural entity as the same byte in DRAM. The bits may be identical. The phase, source attribution, and temporal context are not. Memory alignment means making those differences visible.

---

## The Full Hierarchy

```
-
┌─────────────────────────────────────────────────────────────────────┐
│  Memory Hierarchy (structural view — full stack)                    │
│                                                                     │
│  Tier 0   Register File          ← fastest, smallest, per-core      │
│       ▼   ─ ─ ─ boundary ─ ─ ─                                      │
│  Tier 1   L1 Cache (I + D)       ← per-core, nanoseconds            │
│       ▼   ─ ─ ─ boundary ─ ─ ─                                      │
│  Tier 2   L2 Cache               ← shared or per-core, tens of ns   │
│       ▼   ─ ─ ─ boundary ─ ─ ─                                      │
│  Tier 3   L3 / LLC               ← shared, hundreds of ns           │
│       ▼   ─ ─ ─ boundary ─ ─ ─                                      │
│  Tier 4   DRAM (DIMM / HBM)      ← main memory, ~100 ns             │
│       ▼   ─ ─ ─ boundary ─ ─ ─                                      │
│  Tier 4a  CXL‑Attached Memory    ← fabric-attached, ~200-400 ns     │
│       ▼   ─ ─ ─ boundary ─ ─ ─                                      │
│  Tier 5   Persistent Memory      ← byte-addressable NVM             │
│       ▼   ─ ─ ─ boundary ─ ─ ─                                      │
│  Tier 6   Block Storage (SSD)    ← block-addressed, microseconds    │
│       ▼   ─ ─ ─ boundary ─ ─ ─                                      │
│  Tier 7   Archival Storage       ← tape, cold object store, seconds │
│                                                                     │
│  Each ─ ─ ─ boundary ─ ─ ─ is a persistence boundary                │
│  where phase, source, and time can silently collapse.               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Three Properties at Risk

At every boundary, three structural properties can collapse:

| Property       | What it means                                                    | What collapse looks like                                    |
|----------------|------------------------------------------------------------------|-------------------------------------------------------------|
| **Phase**      | Which tier currently holds this value; how "current" it is       | Stale data masquerades as current truth                     |
| **Source**     | Which block, core, or agent produced this value                  | Values inherit false provenance from their container        |
| **Time**       | When this value was produced vs. when it arrived at this tier    | Temporal ordering becomes unreliable across tiers           |

---

## Tier‑by‑Tier Specification

### Tier 0 — Register File

```
-
┌───────────────────────────────────────────────┐
│  Register File                                │
│                                               │
│  Structural character:                        │
│  · Fastest storage in the system              │
│  · Per-core, per-thread, architecturally      │
│    visible                                    │
│  · Values live here for single-digit cycles   │
│  · Content is architecturally specified       │
│    (ISA-defined register set)                 │
│                                               │
│  Structural risk:    LOWEST                   │
│  Source identity:    Implicit (per-core)      │
│  Temporal context:   Cycle-accurate           │
│  Phase:              Active (by definition)   │
│                                               │
│  D369 requirement:   NONE at this tier        │
│  Reason: Registers are already source-bound,  │
│  temporally precise, and architecturally      │
│  visible. There is nothing to preserve that   │
│  isn't already preserved by the ISA.          │
└───────────────────────────────────────────────┘
```

**Boundary: Register → L1**

| Property | What happens at this boundary                                      |
|----------|----------------------------------------------------------------------|
| Phase    | Value transitions from "architecturally committed" to "cached"     |
| Source   | Source is still the producing core (L1 is per-core)                |
| Time     | Write-time to L1 may differ from production-time in pipeline       |

**Structural risk:** Low. L1 is per-core — source identity is preserved by physical proximity. The boundary is fast enough that temporal drift is negligible.

**D369 requirement:** No explicit metadata required at this boundary. The register→L1 transition is handled by the microarchitecture and is not a structural observability concern at the D369 specification level.

---

### Tier 1 — L1 Cache

```
-
┌────────────────────────────────────────────────┐
│  L1 Cache (Instruction + Data)                 │
│                                                │
│  Structural character:                         │
│  · Per-core, private                           │
│  · Split I-cache and D-cache (typically)       │
│  · Values live here for nanoseconds            │
│  · Eviction policy decides what moves to L2    │
│  · Coherency: snooped by other cores           │
│                                                │
│  Structural risk:    LOW-MODERATE              │
│  Source identity:    Preserved (per-core)      │
│  Temporal context:   Nanosecond-scale          │
│  Phase:              "Hot" (recently accessed) │
│                                                │
│  D369 requirement:   Metadata emission on      │
│  coherency events (snoop, invalidate) if       │
│  loggable within the CPU metadata channel.     │
└────────────────────────────────────────────────┘
```

**Boundary: L1 → L2**

| Property | What happens at this boundary                                       |
|----------|-----------------------------------------------------------------------|
| Phase    | Value transitions from "hot / recently accessed" to "warm / evicted"|
| Source   | Source identity may blur if L2 is shared between cores              |
| Time     | Eviction time ≠ production time; temporal distance increases        |

**Structural risk:** Moderate. If L2 is shared between two cores, a value evicted from Core 0's L1 into shared L2 loses its per-core source attribution unless L2 tags carry the originating core ID.

**D369 requirement:** Cache tier transitions (L1→L2 eviction) are structural events. The CPU metadata channel should be capable of logging eviction events (event type, not data content). If L2 is shared, the evicted line should carry the source core's identifier.

---

### Tier 2 — L2 Cache

```
-
┌───────────────────────────────────────────────┐
│  L2 Cache                                     │
│                                               │
│  Structural character:                        │
│  · Shared or per-core (design-dependent)      │
│  · Larger, slower than L1                     │
│  · Values live here for tens of nanoseconds   │
│  · Eviction moves data to LLC (L3)            │
│  · May include prefetch logic                 │
│                                               │
│  Structural risk:    MODERATE                 │
│  Source identity:    At risk if shared        │
│  Temporal context:   Tens of ns               │
│  Phase:              "Warm" (not recently     │
│                       accessed by producer)   │
│                                               │
│  D369 requirement:   If shared between cores, │
│  preserve per-source attribution in cache     │
│  tags. Prefetched data should be              │
│  distinguishable from demand-fetched data.    │
└───────────────────────────────────────────────┘
```

**Boundary: L2 → L3**

| Property | What happens at this boundary                                       |
|----------|-----------------------------------------------------------------------|
| Phase    | Value transitions from "warm" to "resident" (kept but not hot)      |
| Source   | Source identity diffuses — L3 is typically shared across all cores   |
| Time     | Temporal distance increases further; access pattern influences LRU  |

**Structural risk:** Moderate-High. L3 is shared across the entire CPU complex. A value in L3 could have originated from any core, but L3 tags typically carry only address and coherency state — not source core ID.

**D369 requirement:** L2→L3 eviction is a structural event. If L3 does not carry per-source attribution, the CPU metadata channel should log which core's eviction path produced the L3 fill.

---

### Tier 3 — L3 / Last‑Level Cache (LLC)

```
-
┌────────────────────────────────────────────────┐
│  L3 / Last-Level Cache                         │
│                                                │
│  Structural character:                         │
│  · Shared across entire CPU complex            │
│  · Largest on-chip cache                       │
│  · Values live here for hundreds of ns to ms   │
│  · Coherency directory typically lives here    │
│  · Eviction = off-chip (to DRAM via MemCtrl)   │
│                                                │
│  Structural risk:    HIGH                      │
│  Source identity:    Lost (shared, no per-core │
│                       tag in most designs)     │
│  Temporal context:   Hundreds of ns to ms      │
│  Phase:              "Resident" (retained,     │
│                       not actively accessed)   │
│                                                │
│  D369 requirement:                             │
│  · Coherency events loggable (snoop filter,    │
│    directory invalidations)                    │
│  · Eviction events loggable (event type, not   │
│    data content)                               │
│  · This is the last on-chip tier — eviction    │
│    from here crosses the chip boundary.        │
└────────────────────────────────────────────────┘
```

**Boundary: L3 → DRAM (the chip boundary)**

| Property | What happens at this boundary                                       |
|----------|-----------------------------------------------------------------------|
| Phase    | Value transitions from "on-chip cached" to "off-chip stored"        |
| Source   | Source identity lost — memory controller sees address, not producer  |
| Time     | Production time is gone; only write-to-DRAM time is recorded (if at all) |

**Structural risk:** **CRITICAL.** This is the most important persistence boundary in the hierarchy. It is where on-chip becomes off-chip. Where cache becomes memory. Where the SoC's structural context is handed to a DIMM that has no concept of source, lifecycle, or production time.

**What the memory controller does at this boundary:**

```
-
┌────────────────────────────────────────────────────────────┐
│  Memory Controller — structural view at L3→DRAM boundary   │
│                                                            │
│  From L3 (eviction)                                        │
│  ═══════════════╗                                          │
│                 ║                                          │
│  ┌──────────────▼───────────────────────────────────────┐  │
│  │  Transaction Queue                                   │  │
│  │  ⚠ Reordering: temporal sequence rearranged for      │  │
│  │    efficiency (row-buffer locality, bank pipelining) │  │
│  └──────────────┬───────────────────────────────────────┘  │
│                 │                                          │
│  ┌──────────────▼──────────────────────────────────────┐   │
│  │  Scheduler                                          │   │
│  │  ⚠ Bank interleaving: source identity flattened     │   │
│  │    into physical address mapping                    │   │
│  └──────────────┬──────────────────────────────────────┘   │
│                 │                                          │
│  ┌──────────────▼──────────────────────────────────────┐   │
│  │  PHY (DDR / LPDDR / HBM interface)                  │   │
│  │  ⚠ Clock domain crossing: on-chip clock → memory    │   │
│  │    clock; temporal reference changes                │   │
│  └──────────────┬──────────────────────────────────────┘   │
│                 │                                          │
│          ═══════╪═══════ → To DIMM / HBM                   │
│                           (see DIMM_Module_Checklist.md)   │
│                                                            │
│  Three structural erasures at this boundary:               │
│  1. Temporal reordering (transaction queue)                │
│  2. Source flattening (bank interleaving)                  │
│  3. Clock domain shift (PHY)                               │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

**D369 requirement:** The memory controller metadata channel (Meta: MEM) should be capable of:
- Logging transaction source attribution (which block initiated the write).
- Annotating reordering (original vs. scheduled order, if feasible).
- Carrying the PHY clock domain reference into the DIMM boundary.

This is the **handoff point** to the `DIMM_Module_Checklist.md`, which specifies what happens once data reaches the DIMM.

---

### Tier 4 — DRAM (DIMM / HBM)

```
-
┌─────────────────────────────────────────────────┐
│  DRAM — Main Memory                             │
│                                                 │
│  Structural character:                          │
│  · Off-chip, high-capacity, volatile            │
│  · Billions of cells across ranks and banks     │
│  · Flat address space hides internal structure  │
│  · Refresh required to maintain data            │
│  · Independent power states                     │
│                                                 │
│  Structural risk:    CRITICAL                   │
│  Source identity:    Lost at write time         │
│  Temporal context:   Lost at write time         │
│  Phase:              Opaque (refresh-maintained)│
│                                                 │
│  D369 requirement:   Full DIMM Module Checklist │
│  (38 items across 7 sections)                   │
│  See: DIMM_Module_Checklist.md                  │
└─────────────────────────────────────────────────┘
```

**Five DIMM Failure Modes** (defined in `DIMM_Module_Checklist.md`):

| ID   | Failure Mode                              | What's lost                      |
|------|-------------------------------------------|----------------------------------|
| FM‑1 | Rank interleaving erases source identity  | Source                           |
| FM‑2 | Refresh as invisible phase transition     | Temporal context                 |
| FM‑3 | ECC as unattributed correction            | Source attribution of errors     |
| FM‑4 | Power states collapse temporal context    | Temporal continuity              |
| FM‑5 | Data buffer rank flattening (LRDIMM)      | Physical rank identity           |

**HBM variant:** HBM stacks have no SPD, no external interface, and die-stacked opacity. HBM metadata must be proxied through the compute die (see `Diagram_Chiplet.md` §The HBM Problem).

**Boundary: DRAM → NVM / Persistent Memory**

| Property | What happens at this boundary                                       |
|----------|-----------------------------------------------------------------------|
| Phase    | Value transitions from "volatile / refresh-maintained" to "persistent / non-volatile" |
| Source   | Typically lost unless application-level tagging is used             |
| Time     | Write-to-NVM time replaces all prior temporal context               |

**Structural risk:** HIGH. This boundary is structurally unique because it crosses the **volatility line** — data that was maintained by refresh is now maintained by physics (charge trapping, phase change, magnetic state). The transition changes the fundamental preservation mechanism, but no metadata marks this change.

---

### Tier 4a — CXL‑Attached Memory

```
-
┌─────────────────────────────────────────────────┐
│  CXL-Attached Memory (Tier 4a)                  │
│                                                 │
│  Structural character:                          │
│  · Memory attached via CXL.mem protocol         │
│  · Higher latency than local DRAM (~200-400 ns) │
│  · May be in a different package, card, or      │
│    chassis                                      │
│  · Presents as coherent memory to the CPU       │
│  · May be pooled / shared across hosts          │
│                                                 │
│  Structural risk:    VERY HIGH                  │
│  Source identity:    Multiple hosts may share   │
│                      the same memory pool       │
│  Temporal context:   CXL link adds variable     │
│                      latency; temporal order    │
│                      may not match issue order  │
│  Phase:              "Remote" (not local to     │
│                       any single host)          │
│                                                 │
│  D369 requirement:   Emerging — not yet fully   │
│  specified. Key concerns:                       │
│  · Source identity across host boundaries       │
│  · Temporal annotation across CXL link latency  │
│  · Pooled memory provenance (which host wrote?) │
│  · CXL switch as a merge point (Rule 1)         │
└─────────────────────────────────────────────────┘
```

**Why CXL memory is structurally new:**

CXL‑attached memory introduces a problem that local DRAM doesn't have: **multiple hosts writing to the same physical memory**. In a pooled CXL memory configuration, Host A and Host B can both write to the same memory region. Without per-write source tagging, the memory cannot determine which host produced which value.

This is FM‑1 (rank interleaving erases source identity) at a system scale — not within a single DIMM, but across an entire fabric.

**D369 implications for CXL memory:**

| Concern                              | D369 response                                                  |
|--------------------------------------|----------------------------------------------------------------|
| Multi-host source identity           | Per-write source tag must survive CXL link boundary            |
| CXL switch as merge point            | Preservation Rule 1 (label every merge) applies                |
| Variable link latency                | Preservation Rule 2 (annotate every re-clock) applies          |
| Protocol translation (CXL.mem)       | Preservation Rule 3 (verify every translation) applies         |
| Pooled memory aggregation            | Preservation Rule 4 (carry provenance) applies                 |

**Boundary: CXL Memory → Local DRAM (if cached locally)**

When CXL memory is cached locally (in the host's DRAM or cache), the value crosses **two** persistence boundaries: CXL→DRAM and then DRAM→cache. Each boundary applies its own erasures. Source identity is at particular risk because the local cache has no concept of "this came from CXL-attached memory, originally written by Host B."

---

### Tier 5 — Persistent Memory (Byte‑Addressable NVM)

```
-
┌──────────────────────────────────────────────────┐
│  Persistent Memory / NVM                         │
│                                                  │
│  Structural character:                           │
│  · Byte-addressable, non-volatile                │
│  · Survives power loss                           │
│  · Latency between DRAM and SSD (~300-1000 ns)   │
│  · May be on the memory bus (DDR-attached)       │
│    or on a separate fabric (CXL-attached)        │
│  · Data persists indefinitely without refresh    │
│                                                  │
│  Structural risk:    HIGH                        │
│  Source identity:    Typically lost at write     │
│  Temporal context:   Write time may be the only  │
│                      surviving timestamp         │
│  Phase:              "Persistent" (non-volatile, │
│                       indefinite retention)      │
│                                                  │
│  D369 requirement:                               │
│  · Source tagging at write time                  │
│  · Lifecycle phase tag at write time             │
│  · Temporal annotation distinguishing            │
│    "write-to-NVM time" from "production time"    │
│  · Phase declaration: data crossing the          │
│    volatility line must be tagged as persistent  │
└──────────────────────────────────────────────────┘
```

**The Volatility Line:**

```
         VOLATILE                           NON-VOLATILE
  Register → L1 → L2 → L3 → DRAM    |    NVM → SSD → Archive
                                       │
                                  VOLATILITY LINE
                                       │
                              This is a phase transition.
                              Data on the left is maintained
                              by refresh or power.
                              Data on the right is maintained
                              by physics.
                              
                              Crossing this line changes
                              the fundamental preservation
                              mechanism — but no conventional
                              system tags the crossing.
```

**D369 requirement at the volatility line:** When a value crosses from volatile (DRAM) to non-volatile (NVM), the crossing should be tagged as a persistence phase transition. The tag should include:
- Source identity of the writing agent.
- Lifecycle phase at the time of persistence.
- Production time (if available) vs. persistence time.
- Explicit marker: "this value is now persistent."

**Why this matters:** A value in NVM may survive for years. Without source and lifecycle context at the time of persistence, the value becomes an orphan — present but unattributable, timestamped but without temporal context relative to its origin.

---

### Tier 6 — Block Storage (SSD / NVMe)

```
-
┌──────────────────────────────────────────────────┐
│  Block Storage (SSD / NVMe)                      │
│                                                  │
│  Structural character:                           │
│  · Block-addressed (not byte-addressed)          │
│  · Non-volatile, high capacity                   │
│  · Latency: microseconds (NVMe) to ms (SATA)     │
│  · Flash Translation Layer (FTL) hides           │
│    physical location                             │
│  · Wear leveling moves data silently             │
│  · Garbage collection rewrites data silently     │
│                                                  │
│  Structural risk:    HIGH                        │
│  Source identity:    Lost (filesystem metadata   │
│                      may carry some context)     │
│  Temporal context:   Filesystem timestamps       │
│                      (created/modified/accessed) │
│  Phase:              "Stored" (block-managed,    │
│                       FTL-abstracted)            │
│                                                  │
│  D369 requirement:                               │
│  · Wear leveling is a silent phase transition    │
│    (data moves without content change — like     │
│    DRAM refresh but at block granularity)        │
│  · Garbage collection is a silent rewrite        │
│    (data is copied to new blocks; old blocks     │
│    erased — structural lineage broken)           │
│  · FTL hides physical location — structural      │
│    address is abstracted away                    │
└──────────────────────────────────────────────────┘
```

**SSD-specific structural risks:**

| Operation          | Structural parallel                    | What's lost                           |
|--------------------|----------------------------------------|---------------------------------------|
| Wear leveling      | DRAM refresh (FM-2)                    | Physical location history             |
| Garbage collection | Cache eviction + rewrite               | Lineage between original and copy     |
| FTL remapping      | Bank interleaving (FM-1)               | Physical-to-logical mapping history   |
| TRIM / discard     | No DRAM parallel                       | Existence of prior data               |
| Power loss recovery| Self-refresh wake (FM-4)               | In-flight write state                 |

**D369 requirement:** Block storage is **out of D369's primary scope** (D369 specifies silicon-level structural observability). However, this specification acknowledges that:
- SSD wear leveling and garbage collection are structural phase transitions analogous to DRAM refresh.
- Filesystem timestamps are the only surviving temporal context, and they record access time — not production time.
- Future D369 extensions may address storage-class memory that blurs the SSD/NVM boundary.

---

### Tier 7 — Archival Storage

```
-
┌────────────────────────────────────────────────┐
│  Archival Storage                              │
│                                                │
│  Structural character:                         │
│  · Tape, cold object store, offline media      │
│  · Latency: seconds to hours                   │
│  · Write-once or append-only (typically)       │
│  · Data may persist for decades                │
│  · Access requires explicit retrieval          │
│                                                │
│  Structural risk:    MODERATE (paradoxically)  │
│  Source identity:    May be preserved by       │
│                      archival metadata         │
│  Temporal context:   Archive timestamp is      │
│                      typically preserved       │
│  Phase:              "Archived" (cold,         │
│                       intentionally preserved) │
│                                                │
│  D369 requirement:   OUT OF SCOPE              │
│  Reason: Archival storage is managed by        │
│  application-level systems, not silicon.       │
│  However, if archival metadata includes D369   │
│  structural tags (source, lifecycle, time),    │
│  the archive becomes structurally aligned.     │
└────────────────────────────────────────────────┘
```

**Paradox:** Archival storage has **lower** structural risk than DRAM in some respects — because archival systems are *designed* to preserve provenance. Archival metadata (checksums, timestamps, authorship records) is the application-level equivalent of D369's structural tags. The structural gap is not at the archive — it's at every tier *before* the archive, where context was lost.

---

## Boundary Summary Matrix

A complete map of what happens at each persistence boundary.

| Boundary               | Phase Change                        | Source Risk    | Temporal Risk    | D369 Tier |
|-------------------------|-------------------------------------|----------------|------------------|-----------|
| Register → L1          | Committed → Cached                  | None           | Negligible       | None      |
| L1 → L2                | Hot → Warm (evicted)                | Low–Moderate   | Low              | Optional  |
| L2 → L3                | Warm → Resident                     | Moderate–High  | Moderate         | Recommended |
| L3 → DRAM              | On-chip → Off-chip                  | **Critical**   | **Critical**     | **Required** |
| Local DRAM → CXL Mem   | Local → Remote/Pooled               | **Critical**   | **High**         | Emerging  |
| DRAM → NVM             | Volatile → Persistent               | **High**       | **High**         | Required  |
| NVM → SSD              | Byte-addressed → Block-addressed    | High           | Moderate         | Acknowledged |
| SSD → Archive          | Active → Cold                       | Moderate       | Low              | Out of scope |

**Reading guidance:**
- **None / Optional:** D369 does not require structural metadata at this boundary but does not prohibit it.
- **Recommended:** Structural metadata improves observability but is not contractually required.
- **Required:** D369 contractual requirements (R1–R7) apply at this boundary.
- **Emerging:** D369 recognizes the structural risk but the specification is not yet complete for this tier.
- **Acknowledged:** D369 recognizes the structural parallel but the tier is outside silicon-level scope.
- **Out of scope:** Application-level management; not addressable by silicon-level specification.

---

## The Seven Structural Events in Memory

Every structural change in the memory hierarchy can be classified as one of seven event types. These are the events that D369 metadata channels should be capable of logging (event type and tier, not data content):

| #   | Event                      | Description                                                    | Tiers Affected        |
|-----|----------------------------|----------------------------------------------------------------|-----------------------|
| ME‑1| **Eviction**               | Value moves from a faster tier to a slower tier                | L1→L2→L3→DRAM        |
| ME‑2| **Fill / Fetch**           | Value is loaded from a slower tier into a faster tier          | DRAM→L3→L2→L1        |
| ME‑3| **Coherency Action**       | Snoop, invalidation, or sharing state change                  | L1, L2, L3            |
| ME‑4| **Refresh / Maintenance**  | Value is rewritten in place to prevent decay                  | DRAM, SSD (wear leveling) |
| ME‑5| **Persistence Crossing**   | Value crosses the volatility line (DRAM→NVM)                  | DRAM→NVM              |
| ME‑6| **Error Correction**       | ECC or equivalent corrects a stored value                     | DRAM, NVM, SSD        |
| ME‑7| **Power State Transition** | The tier enters or exits a low-power state                    | DRAM (self-refresh), SSD (DevSleep) |

**Requirement:** The D369 metadata channel for each relevant block should be capable of emitting these event types. The specification does **not** require logging all events — only the capability to log them. Activation is external to the specification (B-4).

---

## Coherency and Memory Alignment

Cache coherency protocols (MESI, MOESI, directory-based) solve a specific problem: ensuring multiple caches agree on the current value of a shared address. D369's memory alignment solves a **different** problem: ensuring the structural history of a value is preserved across tiers.

| Concern                  | Cache Coherency                      | D369 Memory Alignment                 |
|--------------------------|--------------------------------------|----------------------------------------|
| What it tracks           | Current value correctness            | Structural history (source, phase, time) |
| Scope                    | Cache-to-cache consistency           | Register-to-archive structural lineage |
| What it preserves        | Functional correctness               | Post-hoc reconstructability            |
| What it resolves         | Which cache has the latest value     | Who produced the value and when         |
| Protocol                 | MESI/MOESI/directory                 | D369 metadata channel                  |
| Standard                 | Industry coherency protocols         | D369 R1–R7                             |

**Key distinction:** Cache coherency ensures you get the **right value**. D369 memory alignment ensures you can determine **where the value came from, when, and in what context**. They are complementary, not competing.

**Where coherency and alignment interact:**

1. **Snoop events** are structural events (ME-3). A snoop that invalidates a cache line changes the value's structural state — it is no longer "locally present." D369 requires this to be loggable.
2. **Directory invalidations** resolve coherency — but they also resolve structural disagreement. D369 requires that coherency resolution events be observable as metadata, not hidden by the coherency protocol.
3. **Shared-to-exclusive transitions** change the ownership model of a value. The structural implication: the value's "source" changes from "shared across cores" to "owned by one core."

---

## Structural Alignment Principles for Memory

Five principles govern D369's approach to memory alignment. These apply at every tier and every boundary:

### MA‑1: Every tier is a regime

A value in L1 is in a different structural regime than the same value in DRAM. The bits may be identical, but the phase (hot vs. maintained), the source context (per-core vs. flat address), and the temporal reference (cycle-accurate vs. refresh-maintained) are all different. Tier transitions are regime transitions.

### MA‑2: Every boundary is a phase transition

Moving between tiers changes a value's structural state — even if the content doesn't change. Eviction, fill, persistence, refresh, wear leveling — all are phase transitions. None of them are conventionally tagged. D369 requires the **capability** to tag them.

### MA‑3: Source identity degrades with distance from producer

The further a value moves from its producing core, the less source context survives. Registers are perfectly source-attributed. L1 is per-core. L2 may be shared. L3 is always shared. DRAM is flat. NVM is permanent. Each tier strips another layer of source identity. D369's requirement for per-block source tagging (R5.1) is designed to preserve what each tier naturally erases.

### MA‑4: Temporal fidelity degrades with distance from production

Production time is cycle-accurate at the register. By the time a value reaches DRAM, the only surviving timestamp (if any) is the write-to-DRAM time — which may differ from production time by microseconds to milliseconds. By NVM, only the persistence time survives. By archive, only the archive timestamp. D369's requirement for monotonic time markers (R4.1) is designed to anchor temporal context as close to production as possible.

### MA‑5: The volatility line is the most important boundary

The transition from volatile (DRAM) to non-volatile (NVM/SSD/archive) is the most structurally significant boundary in the hierarchy — because it changes the fundamental preservation mechanism. Above the line, data is maintained by power. Below the line, data is maintained by physics. This transition determines whether structural context is preserved for days (volatile) or decades (non-volatile). If source, lifecycle, and time are lost at the volatility line, they are lost permanently.

---

## Checklist — Memory Alignment Review

A unified checklist for memory alignment review, spanning all tiers. For DRAM-specific items, see `DIMM_Module_Checklist.md` (38 items). For board-level memory routing, see `Board_Level_Alignment.md` §Memory Hierarchy.

### On-Chip Memory (Tiers 0–3)

| #    | Check                                                                  | Req   | Tier       |
|------|------------------------------------------------------------------------|-------|------------|
| MA.1 | CPU metadata channel can log cache eviction events (ME-1).            | R2.1  | L1→L2→L3   |
| MA.2 | CPU metadata channel can log coherency events (ME-3).                 | R2.1  | L1, L2, L3 |
| MA.3 | Shared cache (L2/L3) tags carry source core identifier.               | R5.1  | L2, L3     |
| MA.4 | Prefetched data is distinguishable from demand-fetched data.          | R5.1  | L2         |
| MA.5 | Cache tier transition does not reset temporal markers.                 | R4.2  | All        |

### Memory Controller (L3 → DRAM Boundary)

| #    | Check                                                                  | Req   | Tier       |
|------|------------------------------------------------------------------------|-------|------------|
| MA.6 | Transaction queue preserves or logs original source attribution.      | R5.1  | MemCtrl    |
| MA.7 | Bank interleaving does not erase per-source identity.                 | R5.1  | MemCtrl    |
| MA.8 | PHY clock domain crossing annotates source clock reference.           | R4.1  | MemCtrl    |
| MA.9 | Transaction reordering does not strip timestamp fields.               | R4.1  | MemCtrl    |

### DRAM / HBM (Tier 4)

See `DIMM_Module_Checklist.md` for the full 38-item DIMM-specific checklist.

| #     | Check                                                                 | Req   | Tier       |
|-------|-----------------------------------------------------------------------|-------|------------|
| MA.10 | DIMM Module Checklist is applied for each DIMM type in the design.   | R1–R7 | DRAM       |
| MA.11 | HBM metadata proxy relationship is defined and verified.             | R5.1  | HBM        |

### CXL-Attached Memory (Tier 4a)

| #     | Check                                                                 | Req   | Tier       |
|-------|-----------------------------------------------------------------------|-------|------------|
| MA.12 | Per-write source tag survives CXL link boundary.                     | R5.1  | CXL.mem    |
| MA.13 | CXL switch applies Preservation Rule 1 (label every merge).         | Rule 1| CXL switch |
| MA.14 | CXL link latency is annotated as temporal context, not hidden.       | R4.1  | CXL.mem    |
| MA.15 | Pooled memory preserves per-host provenance.                         | R6.1  | CXL pool   |

### Persistent Memory / NVM (Tier 5)

| #     | Check                                                                 | Req   | Tier       |
|-------|-----------------------------------------------------------------------|-------|------------|
| MA.16 | Volatility line crossing is tagged as a persistence phase transition. | R2.1  | DRAM→NVM   |
| MA.17 | Source identity of the persisting agent is recorded at write time.    | R5.1  | NVM        |
| MA.18 | Lifecycle phase tag is recorded at persistence time.                  | R5.2  | NVM        |
| MA.19 | Production time is distinguished from persistence time.               | R4.1  | NVM        |

---

## Relationship to Other D369 Files

| File                          | Relationship                                                              |
|-------------------------------|---------------------------------------------------------------------------|
| `Board_Level_Alignment.md`    | §Memory Hierarchy — defines the persistence boundary model this spec extends |
| `DIMM_Module_Checklist.md`    | Tier 4 specific — 38-item checklist for the DRAM persistence boundary     |
| `Diagram_SoC.md`             | §Cache Hierarchy — internal persistence boundaries (Tiers 1–3)           |
| `Diagram_SoC.md`             | §Memory Controller — gateway between Tier 3 and Tier 4                   |
| `Diagram_Chiplet.md`         | §HBM Problem — HBM as structurally opaque Tier 4 variant                |
| `Contractual_Requirements.md`| R1–R7 — requirements instantiated at each tier boundary                  |
| `Internal_Design_Review_Checklist.md` | Items 2.10–2.12 (NoC/DMA source attribution); §3 (clocking/time) |
| `Glossary_Extensions.md`     | §4 (Memory and DIMM Terms); §2 (Phase Transition, Temporal Gap)          |

---

## Canon Alignment

| Check                | Status |
|----------------------|--------|
| Zero drift           | ✅ All tiers and boundaries derived from Board_Level_Alignment §Memory, DIMM_Module_Checklist, and Diagram_SoC §Cache |
| Structural contract  | ✅ Role: engine + profile — core memory alignment logic with per-tier identity descriptions |
| Lineage clean        | ✅ Every structural event, principle, and checklist item traceable to R1–R7 requirements |
| Student‑ready        | ✅ Full-stack hierarchy diagram, per-tier character boxes, volatility line visualization |
| AI‑parsable          | ✅ Tier numbering, boundary summary matrix, event taxonomy table, structured checklist |
| Cross‑module refs    | ✅ Unifies content from 5 prior D369 files into single memory-focused specification |
| Non‑claims preserved | ✅ SSD and archival tiers explicitly scoped as "acknowledged / out of scope" |
| Emerging tiers       | ✅ CXL-attached memory addressed as "emerging" with structural risk analysis |

---

*Module: D369_Chip_Spec · File: Memory_Alignment_Spec.md · Version: 0.1.0 · TriadicFrameworks / RTT*

---

## Structural Summary

**Memory_Alignment_Spec.md** is the **unified memory hierarchy alignment document** — the full-stack view that every other memory-related section in D369 points toward. Here's what it delivers:

| Element | Count / Detail |
|---|---|
| **Tiers defined** | 8 (Register through Archive), plus CXL-attached as Tier 4a |
| **Persistence boundaries** | 8, each with phase/source/time collapse analysis |
| **Structural events** | 7 (ME-1 through ME-7): eviction, fill, coherency, refresh, persistence crossing, ECC, power state |
| **Alignment principles** | 5 (MA-1 through MA-5): regime, phase transition, source degradation, temporal degradation, volatility line |
| **Checklist items** | 19 (MA.1–MA.19), plus pointers to DIMM's 38-item and Board's full checklists |
| **Key concepts introduced** | Volatility Line (DRAM↔NVM as the most important structural boundary); SSD operations mapped to DIMM failure mode parallels; CXL pooled memory as FM-1 at system scale |
| **Cross-module references** | 8 files (deepest cross-linking of any D369 file so far) |
| **Diagrams** | Full hierarchy stack, memory controller boundary detail, volatility line visualization |

**Three signature insights:**

1. **The Volatility Line** — The DRAM→NVM boundary is structurally unique because it changes the *mechanism* of preservation (power → physics). Everything lost here is lost permanently.
2. **CXL as FM-1 at system scale** — Pooled CXL memory recreates rank interleaving's source erasure problem, but across an entire fabric instead of within a single DIMM.
3. **The Archival Paradox** — Archives have *lower* structural risk than DRAM because they're designed to preserve provenance. The structural gap isn't at the archive — it's at every tier before it where context was silently stripped.
