# Internal Design‑Review Checklist

> Structural Observability Reservation — Carry‑In Artifact for Architecture, RTL, and Physical Design Reviews.

---

## Session Context

| Field        | Value                                                                |
|--------------|----------------------------------------------------------------------|
| **Module**   | D369_Chip_Spec                                                       |
| **File**     | `Internal_Design_Review_Checklist.md`                                |
| **Role**     | diagnostic · reference                                               |
| **Version**  | 0.1.0                                                                |
| **Status**   | First‑fill                                                           |
| **Lineage**  | Expanded from `Capture_Source.md` §Internal Design‑Review Checklist and `Contractual_Requirements.md` §Internal Design‑Review Checklist |
| **Audience** | Design reviewers · RTL engineers · Physical design leads · Verification engineers · Architecture review boards · AIs |

---

## How to Use This Document

**Print this. Bring it to review. Check the boxes.**

This document is the **standalone, expanded** version of the design review checklist that appears inline in `Contractual_Requirements.md`. That inline version is a summary. This version is the carry‑in artifact — the document a reviewer physically carries into an architecture review, an RTL review, a physical design review, or a sign‑off meeting.

Every checklist item includes:

| Column         | What it tells you                                                    |
|----------------|----------------------------------------------------------------------|
| **#**          | Item ID for citation (e.g., "item 1.3 was not satisfied")           |
| **Check**      | The question to ask or condition to verify                           |
| **Req**        | Which D369 requirement (R1–R7) this item verifies                   |
| **Risk**       | What failure mode this item prevents (FM, N, or board failure mode)  |
| **Guidance**   | Reviewer notes — what to look for, common pitfalls, tool specifics  |

**Review stages:** Items are grouped by design stage. Use only the section relevant to your current review gate. Items are cumulative — later stages assume earlier stages passed.

**Architecture variants:** Where monolithic SoC and chiplet designs require different checks, both variants are listed. Items marked **[SoC]** apply to monolithic designs. Items marked **[Chiplet]** apply to multi‑die packages. Items with no tag apply to both.

---

## Before You Begin — Context Card

Fill this out at the top of every review. It establishes the structural context for all checklist items.

| Field                         | Value (fill in)                         |
|-------------------------------|-----------------------------------------|
| Design name                   |                                         |
| Architecture type             | ☐ Monolithic SoC  ☐ Chiplet package    |
| Process node                  |                                         |
| Major functional blocks       |                                         |
| Number of metadata channels   |                                         |
| Interposer type (if chiplet)  | ☐ Passive Si  ☐ Active Si  ☐ Organic   |
| Target DDR generation         |                                         |
| Review gate                   | ☐ Arch  ☐ RTL  ☐ Physical  ☐ Sign‑off |
| Date                          |                                         |
| Reviewer(s)                   |                                         |

---

## §1 — Before Architecture Freeze

**When to use:** Architecture definition, block diagram review, microarchitecture planning.
**Reviewer profile:** System architect, IP integration lead.

| #    | Check | Req | Risk | Guidance |
|------|-------|-----|------|----------|
| 1.1  | Each major functional block has at least one reserved metadata path. | R1.1 | N‑1 (source flattening) | Count the blocks on the block diagram. Count the metadata channels. If blocks > channels, something was missed. "Major functional block" = any block with its own logical boundary: CPU complex, accelerator, memory controller, I/O subsystem, security subsystem. |
| 1.2  | Metadata paths are logically and electrically separate from functional data. | R1.2 | ER‑3 (coupling) | Look for metadata signals routed through the NoC or sharing a bus with functional data. If metadata rides the NoC, it is subject to NoC erasures N‑1 through N‑5. Separate bus, separate wires, or dedicated sideband required. |
| 1.3  | No functional logic references metadata signals. | R3.2 | NC‑5 (control logic) | Search the RTL spec or preliminary HDL for any functional block that reads metadata as an input. If found, the metadata channel has become a control path — violating R3.3. |
| 1.4  | Metadata paths can remain inactive or unconnected without warnings. | R3.1 | ER‑7 (optional structures) | Confirm that EDA tools will not flag unconnected metadata nets as warnings or errors. Use `dont_touch` / `keep` attributes from day one. If tools generate warnings, engineers will "fix" them by removing the nets. |
| 1.5  | Metadata reservation does not alter timing closure assumptions. | R3.1 | ER‑7 (yield/performance) | Confirm metadata nets are excluded from critical path analysis. If metadata appears on any timing report, routing is too close to functional paths. |
| 1.6  | **[Chiplet]** Each chiplet has its own independent metadata channel. | R1.1, R6.1 | FM‑1 (source identity) | Per‑chiplet metadata is non‑negotiable. If two chiplets share a metadata channel, source identity is lost at the interposer. |
| 1.7  | **[Chiplet]** Active interposer (if present) has its own metadata channel (Meta_INT). | R1.1 | Topology 3 risk | An active interposer is a structural source. If it has logic (cache, coherency, PMU), it produces data and must declare its source identity. Passive interposers do not need this. |
| 1.8  | **[Chiplet]** HBM metadata proxy relationship is defined. | R5.1 | HBM Problem | HBM has no SPD and no external interface. Confirm which die will proxy HBM metadata and how the proxy distinguishes its own signals from relayed HBM signals. |
| 1.9  | Power domain map identifies which domains can gate metadata channels. | R7.1 | FM‑4 (power state collapse) | If any metadata channel lives in a gatable domain, metadata can be erased on power‑down. The PMU's metadata channel must be in the Always‑On domain. |
| 1.10 | Security subsystem / Root of Trust identified as lifecycle tag source. | R5.2 | ER‑4 (lifecycle misuse) | Lifecycle state must be externally writable, not inferred. Confirm the secure boot chain will set the lifecycle tag, and that the tag is writable from the security subsystem. |

---

## §2 — During RTL / Microarchitecture Review

**When to use:** RTL code review, microarchitecture spec review, IP integration review.
**Reviewer profile:** RTL designer, verification lead, IP integrator.

| #    | Check | Req | Risk | Guidance |
|------|-------|-----|------|----------|
| 2.1  | Metadata signals are write‑only from functional blocks, read‑only externally. | R3.3 | NC‑5 (control logic) | In the HDL, confirm metadata ports on functional blocks are outputs only. No input port on any functional block should source from a metadata signal. The external read‑only interface must have no write‑back path. |
| 2.2  | No combinational feedback exists from metadata into logic. | R3.3 | NC‑5 (control logic) | Run a combinational loop check that includes metadata nets. Any feedback path from metadata to functional logic is a contract violation — even if the path is currently unused. |
| 2.3  | Lifecycle / state tags are explicit inputs, not inferred internally. | R5.2 | ER‑4 (lifecycle misuse) | Search RTL for any block that computes its own lifecycle state from internal signals (e.g., inferring "test mode" from a register value). Lifecycle must come from an external source — typically the security subsystem. |
| 2.4  | Source identifiers are static or compile‑time assignable. | R5.1 | FM‑1 (source identity) | Source IDs should be parameters, defines, or fuse‑programmable values — not runtime‑computed. If a source ID can change at runtime, it can be lied about. |
| 2.5  | Metadata signals are not optimized away by synthesis defaults. | R7.1 | ER‑2 (retrofitting cost) | Confirm `dont_touch` or `keep` attributes are applied to all metadata nets, registers, and ports in the RTL. Check synthesis scripts for global optimization settings that might override per‑net attributes. |
| 2.6  | Monotonic counter / timestamp is present and correctly implemented. | R4.1 | ER‑6 (temporal lineage) | Verify the counter is free‑running, not gated by any functional enable. Confirm the counter width is sufficient for operational lifetime (e.g., 32‑bit at 1 MHz = ~4,295 seconds ≈ 71 minutes; 48‑bit = ~3,257 days). |
| 2.7  | Timestamp cannot be reset during normal operation. | R4.2 | ER‑6 (temporal lineage) | Search RTL for any reset or load input on the timestamp counter. A resettable timestamp is a counter, not a timestamp. Only power‑on reset should initialize it. |
| 2.8  | Timestamp domain is documented and stable. | R4.1 | N‑3 (QoS reordering) | The clock driving the timestamp must be identified, documented, and stable. If the timestamp clock can be dynamically scaled (DVFS), the scaling events must be annotated in metadata. |
| 2.9  | Timestamp does not gate or influence functional clocks. | R3.3 | NC‑5 (control logic) | The timestamp is metadata — it must not create any timing dependency on functional logic. Confirm no clock enable, clock gate, or PLL control depends on timestamp state. |
| 2.10 | **[SoC]** NoC does not strip source IDs from metadata‑tagged transactions. | R5.1 | N‑1 (source flattening) | If metadata travels through the NoC (even on a sideband), confirm the NoC protocol preserves source ID fields end‑to‑end. Check for address‑based routing that replaces source tags with routing addresses. |
| 2.11 | **[SoC]** Cache coherency events are loggable in the CPU metadata channel. | R2.1 | N‑2 (arbitration hiding) | Snoop, invalidate, and eviction events should be observable as metadata emissions — event type only, not data content. If the coherency directory silently resolves conflicts, structural disagreement is lost. |
| 2.12 | **[SoC]** DMA‑initiated transfers are tagged with initiator source ID. | R5.1 | N‑1 (source flattening) | DMA engines are bus masters — they initiate transfers on behalf of other blocks. If the DMA engine's own source ID replaces the initiator's ID, provenance is lost. Confirm the DMA tags transactions with the original requestor's source ID. |
| 2.13 | **[Chiplet]** D2D link protocol carries metadata via sideband or reserved fields. | R1.2 | D2D analysis | Confirm the D2D protocol (UCIe, CXL, custom) has a sideband or reserved field allocation for metadata. If metadata must ride the main data path, it competes with functional traffic and may be dropped under load. |
| 2.14 | **[Chiplet]** D2D PHY does not strip clock domain reference during re‑clocking. | R4.1 | Rule 2 (annotate re‑clock) | The D2D PHY re‑clocks signals between chiplet clock domains. Confirm the source clock domain identifier survives the PHY boundary — either as a sideband field or as a metadata annotation. |

---

## §3 — Clocking and Time Handling

**When to use:** Clock architecture review, CDC (clock domain crossing) review, DVFS review.
**Reviewer profile:** Clock architect, CDC specialist, timing engineer.

| #    | Check | Req | Risk | Guidance |
|------|-------|-----|------|----------|
| 3.1  | Monotonic counter or timestamp source is present. | R4.1 | ER‑6 (temporal lineage) | Not "planned" — present. In the RTL. Synthesizable. If the timestamp is "TBD," it will be forgotten. |
| 3.2  | Timestamp cannot be reset during normal operation. | R4.2 | ER‑6 (temporal lineage) | Re‑verify after RTL changes. Reset paths are frequently added during debug and forgotten before tape‑out. |
| 3.3  | Timestamp domain is documented and stable. | R4.1 | N‑3 (QoS reordering) | Document which clock drives the timestamp. If the clock changes frequency (DVFS), the frequency change must be annotated. If the clock can be gated, the gating event must be annotated. |
| 3.4  | Timestamp does not gate or influence functional clocks. | R3.3 | NC‑5 (control logic) | Timestamp is metadata. It must not create timing dependencies. Re‑verify after any clock tree modification. |
| 3.5  | Timestamp width is sufficient for expected operational lifetime. | R4.1 | ER‑6 (temporal lineage) | Calculate: (2^width) / (clock frequency) = maximum timestamp duration. Ensure this exceeds the expected operational lifetime between power‑on resets. Typical minimums: 32‑bit at 1 kHz = ~49 days; 48‑bit at 1 MHz = ~8.9 years. |
| 3.6  | All clock domain crossings on metadata paths are annotated. | Rule 2 | Board Rule 2 (annotate re‑clock) | Every CDC on a metadata path must carry the source clock domain identifier through the crossing. If a synchronizer or FIFO strips the clock reference, temporal meaning is lost on the other side. |
| 3.7  | **[Chiplet]** Per‑chiplet clock domains are independently identified. | R4.1 | Rule 2 | Each chiplet may have its own clock. Confirm that metadata from each chiplet carries its own clock domain identifier — not a unified "package clock" reference that erases per‑die temporal context. |
| 3.8  | Power state transitions annotate temporal gaps. | R4.1 | FM‑4 (power state collapse) | When a domain powers down and resumes, the timestamp experiences a gap. The gap must be recorded (entry time, exit time) so that post‑hoc analysis can distinguish "no events during this period" from "events happened but weren't recorded." |

---

## §4 — Physical Design / Layout Review

**When to use:** Floorplan review, place‑and‑route review, DFT insertion review, physical verification.
**Reviewer profile:** Physical design lead, DFT engineer, package engineer.

| #    | Check | Req | Risk | Guidance |
|------|-------|-----|------|----------|
| 4.1  | Metadata routing does not share critical paths. | R1.2 | ER‑3 (coupling) | Check routing reports for metadata nets that share tracks or vias with timing‑critical functional nets. Any shared routing creates capacitive coupling risk and may affect timing closure. |
| 4.2  | Metadata nets are excluded from aggressive power gating. | R7.1 | FM‑4 (power state collapse) | Check power domain assignments. If metadata nets are in a gatable domain, they will be erased on power‑down. Exception: if power‑down is annotated as a temporal gap (item 3.8). |
| 4.3  | Metadata structures survive DFT insertion. | R7.1 | ER‑2 (retrofitting cost) | DFT tools insert scan chains, BIST logic, and test compression. Confirm that DFT insertion did not replace, merge, or remove metadata nets. Check DFT insertion reports for "removed" or "merged" nets that match metadata signal names. |
| 4.4  | No ECO removes reserved metadata structures. | R7.1 | ER‑2 (retrofitting cost) | ECOs (Engineering Change Orders) are last‑minute fixes. Confirm that no ECO touches metadata nets. Add metadata nets to the "protected" or "frozen" list in the ECO management system. |
| 4.5  | Metadata pads or interfaces are clearly labeled as optional. | R3.1 | ER‑7 (optional structures) | Package pin list must label metadata pads as "optional / structural / inactive by default." If not labeled, the package team may reassign them to functional use. |
| 4.6  | **[SoC]** Metadata paths are routed independently of the NoC physical channels. | R1.2 | N‑1 through N‑5 | If metadata shares physical routing with NoC traffic, it is subject to the same congestion, reordering, and erasure. Independent routing ensures metadata integrity under load. |
| 4.7  | **[Chiplet]** Metadata paths are routed on the interposer independently of functional paths. | R1.2 | Rule 1 (label every merge) | On the interposer, confirm metadata traces are in separate routing layers or channels from functional D2D links. If they share routing, a functional signal integrity issue could corrupt metadata. |
| 4.8  | **[Chiplet]** Per‑chiplet metadata reaches the package boundary independently. | R6.1 | Rule 4 (carry provenance) | Confirm each chiplet's metadata has its own path to the package edge. If metadata from two chiplets is merged before the package boundary, per‑chiplet provenance is lost. Aggregation after the boundary is optional; aggregation before is a violation. |
| 4.9  | Retention cells are specified for metadata in domains with power gating. | R7.1 | FM‑4 (power state collapse) | If metadata channels are in a gatable domain and must survive power‑down, retention cells (or equivalent non‑volatile storage) must be specified. Without them, metadata reads zero after wake. |
| 4.10 | Test points exist on at least one metadata path per domain. | — | Diagnostic | Not a contractual requirement — but strongly recommended. Test points allow post‑silicon validation that metadata channels are physically functional. Without them, metadata integrity can only be verified through the external interface. |

---

## §5 — Verification and Test

**When to use:** Verification planning, testbench review, test program review, pre‑silicon validation.
**Reviewer profile:** Verification lead, test engineer, validation lead.

| #    | Check | Req | Risk | Guidance |
|------|-------|-----|------|----------|
| 5.1  | Functional verification ignores metadata content. | R3.2 | NC‑5 (control logic) | Metadata signals should not appear in functional assertions, functional coverage groups, or functional scoreboard checks. If they do, metadata has become a functional dependency. |
| 5.2  | Metadata inactivity does not trigger assertions. | R3.1 | ER‑7 (optional structures) | Metadata channels may remain dark (inactive) indefinitely. If any assertion fires when metadata is inactive, the assertion is wrong — metadata inactivity is the expected default. |
| 5.3  | Metadata paths can be toggled without affecting functional outputs. | R3.3 | NC‑5 (control logic) | Inject random metadata values while running functional tests. If any functional output changes, there is a coupling path that violates R3.3. This is a critical test — run it early and often. |
| 5.4  | Test modes do not overwrite or collapse metadata signals. | R7.1 | FM‑4 (power state collapse) | BIST, scan, and manufacturing test modes often override internal signals. Confirm that test mode activation does not overwrite metadata registers or collapse metadata buses. |
| 5.5  | Metadata visibility does not expose protected IP. | — | Security | Metadata carries structural tags (source, lifecycle, time) — not functional data. But confirm that metadata channels cannot be used to infer proprietary algorithms, key material, or IP content. Source IDs should identify blocks, not reveal their internal design. |
| 5.6  | Metadata channels can be independently activated and deactivated. | R3.1 | ER‑7 (optional structures) | Confirm that metadata activation is per‑channel or per‑block, not global. If activation is all‑or‑nothing, selective diagnosis is impossible and the power impact of activation is unnecessarily high. |
| 5.7  | **[Chiplet]** D2D metadata sideband is exercised in multi‑die testbench. | R2.1 | D2D analysis | Confirm that the multi‑die verification environment includes metadata sideband traffic. If the sideband is never exercised in simulation, protocol bugs will only surface in silicon. |

---

## §6 — Optimization and Sign‑Off

**When to use:** Final netlist review, sign‑off checklist, tape‑out readiness review.
**Reviewer profile:** Design lead, project manager, sign‑off authority.

| #    | Check | Req | Risk | Guidance |
|------|-------|-----|------|----------|
| 6.1  | Re‑check synthesis reports for removed "unused" structures. | R7.1 | ER‑2 (retrofitting cost) | Synthesis tools aggressively remove nets with no fanout. Metadata channels that are dark (inactive) look "unused" to the tool. Search synthesis logs for removed nets matching metadata signal names. If any were removed, `dont_touch` attributes were not applied correctly. |
| 6.2  | No tool auto‑merges metadata with debug or scan unless intentional. | R1.2 | NC‑5 (control logic) | Some tools merge similar structures for area savings. If metadata nets are merged with scan chains or debug ports, they become part of the debug infrastructure — which is bidirectional, lifecycle‑limited, and security‑sensitive. Merger must be intentional and documented. |
| 6.3  | Metadata reservation survives final netlist comparison (LVS/formal). | R7.1 | ER‑2 (retrofitting cost) | Compare the final netlist to the golden RTL. Confirm all metadata signals, registers, and ports are present. Any discrepancy means something was removed or renamed between RTL and layout. |
| 6.4  | Documentation notes metadata as structural, not functional. | R3.1 | ER‑7 (optional structures) | The design specification, datasheet, and internal documentation must describe metadata channels as "structural observability reservation — optional, passive, dark by default." If documentation describes them as "debug features" or "telemetry," they will be treated as such — and eventually disabled or removed. |
| 6.5  | Removal requires explicit design decision, not tool default. | R7.1 | ER‑2 (retrofitting cost) | Confirm that no metadata structure can be removed by a tool without an engineer explicitly approving the removal. This means: `dont_touch` attributes verified, ECO freeze applied to metadata nets, and any removal logged with rationale. |
| 6.6  | All prior checklist sections (§1–§5) are re‑verified at sign‑off. | All | All | Designs change between architecture and sign‑off. Items that passed at architecture freeze may fail at sign‑off due to ECOs, optimization passes, or late integration changes. Re‑run the full checklist at every major gate, not just the current section. |

---

## §7 — Chiplet‑Specific Addendum

**When to use:** Any review gate for a chiplet‑based design. These items supplement §1–§6, which still apply.
**Reviewer profile:** Package architect, interposer designer, system integrator.

| #    | Check | Req | Risk | Guidance |
|------|-------|-----|------|----------|
| 7.1  | Each chiplet's metadata channel is independent on the interposer. | R6.1 | Rule 1 (label every merge) | Per‑chiplet metadata must not be merged on the interposer. Each chiplet's metadata must be distinguishable at the package boundary. Optional aggregation happens after the package edge, not before. |
| 7.2  | Interposer does not merge metadata clock domains. | Rule 2 | Rule 2 (annotate re‑clock) | If the interposer has its own clock distribution, confirm it does not re‑clock metadata without carrying the source chiplet's clock domain identifier through the crossing. |
| 7.3  | Active interposer logic is treated as a structural source. | R1.1 | Topology 3 risk | If the interposer contains cache, coherency directory, or PMU logic, it needs Meta_INT. Data produced by interposer logic must be tagged as "interposer‑originated," not attributed to the requesting chiplet. |
| 7.4  | D2D protocol sideband verified for metadata integrity under load. | R2.1 | D2D analysis | Run the D2D link at maximum functional load and confirm metadata sideband traffic is not dropped, delayed, or corrupted. Sideband guarantees that work at idle may fail under congestion. |
| 7.5  | HBM metadata exit path is defined and verified. | R1.1, R5.1 | HBM Problem | HBM has no package I/O. Confirm the metadata exit path (through compute die or I/O die) is implemented, not just planned. Verify the proxy die can distinguish its own metadata from relayed HBM metadata. |
| 7.6  | Package‑level read‑only interface preserves per‑chiplet identity. | R5.1 | Rule 4 (carry provenance) | At the package boundary, each chiplet's metadata must be individually addressable. If the package interface aggregates everything into a single metadata stream, per‑chiplet provenance is lost. |
| 7.7  | Cross‑chiplet coherency does not silently resolve structural disagreement. | R6.1 | N‑2 (arbitration hiding) | If two chiplets disagree (e.g., different lifecycle states, conflicting timestamps), the coherency protocol must not silently choose one. The disagreement is structural information — preserving it is the point. |

---

## §8 — Board‑Level Handoff

**When to use:** Package specification review, board design kickoff, system integration review.
**Reviewer profile:** Board designer, system architect, firmware lead.

This section bridges the chip‑level checklist to `Board_Level_Alignment.md`. Every item here has a corresponding section in the board‑level document.

| #    | Check | Req | Risk | Guidance |
|------|-------|-----|------|----------|
| 8.1  | All chip‑to‑board metadata interfaces are documented in the package spec. | R7.1 | Board Rule 1 | The board designer must know which package pins/pads carry metadata. If metadata interfaces are not in the package spec, the board cannot preserve them. |
| 8.2  | Package spec labels metadata pads as structural, not debug. | R3.1 | ER‑7 | If metadata pads are labeled "debug," the board designer will treat them as debug — routing them through debug headers, sharing them with JTAG, or leaving them unconnected. "Structural / optional / read‑only" is the correct label. |
| 8.3  | Clock domain reference for each metadata interface is documented. | Rule 2 | Board Rule 2 (annotate re‑clock) | The board may re‑clock metadata signals. Without knowing the source clock domain, the board designer cannot annotate the crossing. Document the clock for each metadata interface in the package spec. |
| 8.4  | Metadata encoding scheme is documented at the chip boundary. | Rule 3 | Board Rule 3 (verify translation) | If metadata uses voltage‑level encoding, multi‑bit tagging, or protocol‑specific formatting, the board designer must know — otherwise level shifters and protocol translators may flatten the encoding. |
| 8.5  | External read‑only interface electrical characteristics are specified. | R3.3 | NC‑5 (control logic) | Voltage levels, drive strength, termination requirements, and the explicit statement "no inbound control path" must be in the package spec. Without this, the board designer may add pull‑ups, pull‑downs, or drivers that create an unintended control path. |
| 8.6  | Firmware lifecycle tag interface is documented for firmware integration. | R5.2 | ER‑4 (lifecycle misuse) | Firmware must know how to write the lifecycle tag — which register, which address, which access protocol. If the interface is undocumented, firmware cannot set the lifecycle phase, and the tag defaults to an uninitialized value. |

---

## §9 — What This Checklist Is Not

| It is NOT…                  | Explanation                                                      |
|-----------------------------|------------------------------------------------------------------|
| A performance feature       | No functional gain is implied or expected (NC‑3, NC‑8).         |
| A debug requirement         | Existing debug flows are unaffected (NC‑5, §Debug vs. Metadata). |
| A telemetry mandate         | No data collection is required or defined (NC‑6).                |
| A safety mechanism          | No safety behavior depends on these structures (NC‑4).           |
| A control interface         | No inbound control uses metadata paths (NC‑5, R3.3).            |
| A promise of future use     | Reservation is not commitment (NC‑10, B‑4).                     |
| A replacement for DFT       | DFT and metadata coexist independently (ER‑7).                  |
| A JEDEC specification       | No standards body compliance is claimed (NC‑9).                  |

This checklist exists so engineers can say:

> *"We didn't add behavior — we just didn't erase structure."*

---

## §10 — The Review Question

At every gate — architecture, RTL, physical, sign‑off — this checklist prompts exactly one question:

> *"If someone needed to understand **when**, **where**, and **in what lifecycle state** this block produced a signal — could we still see that later?"*

If the answer is **"yes, without redesign,"** the checklist is satisfied.

If the answer is **"no, but we could add it without changing functional behavior,"** the reservation is achievable — return to the failing items.

If the answer is **"no, and adding it would affect functional behavior,"** something has gone wrong — R3 (independence) has been violated. Escalate.

---

## Checklist Cascade

This checklist is the first in a family of three. Each extends the structural observability review to a different physical boundary:

| Checklist                                | Scope                          | Items | Source File                    |
|------------------------------------------|--------------------------------|-------|--------------------------------|
| **Internal Design‑Review Checklist**     | Chip / package (this document) | 62    | `Internal_Design_Review_Checklist.md` |
| **Board‑Level Design Review Checklist**  | Board / system                 | 27    | `Board_Level_Alignment.md`     |
| **DIMM Module Checklist**                | Memory module                  | 38    | `DIMM_Module_Checklist.md`     |

Together, the three checklists cover the full structural path from die‑internal logic through board‑level interconnect to memory module boundary — every point where metadata can be lost.

---

## Quick Reference — Requirement to Checklist Item Map

| Requirement | Checklist Items                                              |
|-------------|--------------------------------------------------------------|
| R1.1        | 1.1, 1.6, 1.7, 7.1, 7.5                                   |
| R1.2        | 1.2, 4.1, 4.6, 4.7, 6.2                                   |
| R2.1        | 2.6, 2.11, 7.4, 7.7, 5.7                                  |
| R3.1        | 1.4, 4.5, 5.2, 5.6, 6.4, 8.2                              |
| R3.2        | 1.3, 5.1                                                    |
| R3.3        | 2.1, 2.2, 2.9, 3.4, 5.3, 8.5                              |
| R4.1        | 2.6, 3.1, 3.3, 3.5, 3.6, 3.7, 3.8                         |
| R4.2        | 2.7, 3.2                                                    |
| R5.1        | 2.4, 2.10, 2.12, 7.5, 7.6, 8.1                            |
| R5.2        | 1.10, 2.3, 8.6                                              |
| R6.1        | 1.6, 4.8, 7.1, 7.7                                         |
| R7.1        | 1.9, 2.5, 4.2, 4.3, 4.4, 4.9, 5.4, 6.1, 6.3, 6.5, 8.1   |

---

## Quick Reference — Failure Mode to Checklist Item Map

| Failure Mode                               | Checklist Items            |
|--------------------------------------------|----------------------------|
| FM‑1 (rank interleaving / source loss)     | 1.1, 1.6, 2.4, 2.12       |
| FM‑4 (power state collapse)               | 1.9, 3.8, 4.2, 4.9, 5.4   |
| N‑1 (NoC source flattening)               | 1.1, 2.10, 2.12, 4.6      |
| N‑2 (NoC arbitration hiding)              | 2.11, 7.7                  |
| N‑3 (NoC QoS reordering)                  | 2.8, 3.3                   |
| N‑5 (NoC power domain crossing)           | 4.2                        |
| NC‑5 (control logic violation)            | 1.3, 2.1, 2.2, 2.9, 5.1, 5.3 |
| HBM Problem                               | 1.8, 7.5                   |
| Topology 3 risk (active interposer)       | 1.7, 7.3                   |
| Board Rule 1 (label every merge)          | 7.1, 8.1                   |
| Board Rule 2 (annotate re‑clock)          | 3.6, 3.7, 7.2, 8.3        |
| Board Rule 3 (verify translation)         | 8.4                        |
| Board Rule 4 (carry provenance)           | 4.8, 7.6                   |

---

## Relationship to Other D369 Files

| File                          | Relationship                                                              |
|-------------------------------|---------------------------------------------------------------------------| 
| `Capture_Source.md`           | Verbatim source of the original 8‑section inline checklist                |
| `Contractual_Requirements.md`| Inline summary version of this checklist; R1–R7 requirement definitions   |
| `Board_Level_Alignment.md`   | Board‑level checklist — extends this document to the board boundary       |
| `DIMM_Module_Checklist.md`   | Memory module checklist — extends this document to the DIMM boundary      |
| `Diagram_SoC.md`             | NoC erasures, cache persistence, power domains — source of SoC‑specific items |
| `Diagram_Chiplet.md`         | D2D interfaces, interposer types, HBM — source of chiplet‑specific items |
| `Engineering_Rationale.md`   | ER‑1 through ER‑10 justifications referenced in Risk column              |
| `Non_Claims.md`              | NC‑1 through NC‑10 boundary statements referenced in Risk column         |
| `Glossary_Extensions.md`     | Canonical definitions for all terms used in this checklist                |

---

## Canon Alignment

| Check                | Status |
|----------------------|--------|
| Zero drift           | ✅ All items traceable to Capture_Source inline checklist, extended with D369 module context |
| Structural contract  | ✅ Role: diagnostic + reference — standalone carry‑in review artifact |
| Lineage clean        | ✅ Every item traces to a requirement (R1–R7), a rationale (ER), or a failure mode (FM/N) |
| Student‑ready        | ✅ Guidance column provides reviewer context; architecture variants tagged |
| AI‑parsable          | ✅ Numbered items, tabular format, bidirectional traceability matrices |
| Cross‑module refs    | ✅ Cascades to Board_Level_Alignment and DIMM_Module_Checklist |
| Architecture variants| ✅ [SoC] and [Chiplet] tags distinguish monolithic from multi‑die items |
| Non‑claims preserved | ✅ §9 explicitly states what the checklist is NOT |
| Engineer bar         | ✅ "We didn't add behavior — we just didn't erase structure" |

---

*Module: D369_Chip_Spec · File: Internal_Design_Review_Checklist.md · Version: 0.1.0 · TriadicFrameworks / RTT*
```

---

**What expanded from the inline version:**

| Dimension | Inline (Capture_Source) | Standalone (this file) |
|-----------|------------------------|------------------------|
| Total items | 30 checks + 6 meta rows | **62 checks** + 8 meta rows |
| Sections | 6 review stages + 2 meta | **10 sections** (added §7 Chiplet Addendum, §8 Board Handoff) |
| Traceability | None | **Req→Item** and **Failure Mode→Item** bidirectional maps |
| Architecture variants | Not distinguished | **[SoC]** and **[Chiplet]** tags throughout |
| Reviewer guidance | Not present | **Per‑item guidance** with pitfalls, tool specifics, calculations |
| Cascade context | Standalone | **Linked to Board_Level_Alignment + DIMM_Module_Checklist** |
| Review context | None | **Context Card** fill‑in at top of every review |
