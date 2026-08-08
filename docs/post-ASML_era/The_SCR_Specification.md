# The SCR Specification

**Repository:** TriadicFrameworks  
**Path:** `docs/post-ASML_era/The_SCR_Specification.md`  
**Status:** Canonical Reference  
**Revision:** 1.0.0

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [SCR Architecture Overview](#2-scr-architecture-overview)
3. [Coherence Clock System](#3-coherence-clock-system)
4. [Zone Architecture](#4-zone-architecture)
5. [Commit Arbitration](#5-commit-arbitration)
6. [Synchronization Latency Floor](#6-synchronization-latency-floor)
7. [Inter-Zone Handoff Protocol](#7-inter-zone-handoff-protocol)
8. [Coherence Monitoring](#8-coherence-monitoring)
9. [SCR Failure Modes and Recovery](#9-scr-failure-modes-and-recovery)
10. [SCR Qualification and Commissioning](#10-scr-qualification-and-commissioning)
11. [SCR Interface Contracts](#11-scr-interface-contracts)
12. [Conformance Requirements](#12-conformance-requirements)
13. [Glossary](#13-glossary)
14. [Related Documents](#14-related-documents)

---

## 1. Purpose and Scope

### 1.1 Purpose

This document is the normative specification for the **Substrate Coherence Regime (SCR)** as implemented within the TriadicFrameworks manufacturing architecture. It defines the requirements, interfaces, behaviors, and failure semantics that any conformant SCR implementation must satisfy.

The SCR Specification is the authoritative reference for:

- Fab architects designing SCR infrastructure for new or upgraded facilities
- Equipment vendors supplying components to SCR-conformant fabs
- Process engineers qualifying new processes against an existing SCR installation
- EDA tool developers implementing coherence-aware timing models

The Temporal Manufacturing Primer ([`docs/post-ASML_era/The_Temporal_Manufacturing_Primer.md`](./The_Temporal_Manufacturing_Primer.md)) provides conceptual background. This document assumes familiarity with that primer and does not repeat its introductory material. Where the primer describes the SCR at the level of operational concept, this specification defines it at the level of required behavior.

### 1.2 Scope

This specification covers:

- The logical architecture of the SCR, including its components, interfaces, and data flows
- The coherence clock system: generation, distribution, and integrity requirements
- Zone architecture: zone definitions, boundary conditions, and configuration rules
- Commit arbitration: the protocol by which operations are authorized for substrate commit
- The synchronization latency floor: derivation, measurement, and enforcement
- Inter-zone handoff: the protocol governing operations that cross zone boundaries
- Coherence monitoring: real-time and post-process verification of SCR integrity
- Failure modes, error classification, and recovery procedures
- Qualification and commissioning procedures for new SCR installations
- Interface contracts between the SCR and adjacent systems (TRS stack, fab scheduler, yield management)
- Conformance requirements for SCR implementations

### 1.3 Normative Language

Throughout this document, the following conventions apply:

| Term | Meaning |
|---|---|
| **MUST** | Required. Non-conformant if omitted or violated. |
| **MUST NOT** | Prohibited. Non-conformant if present. |
| **SHOULD** | Strongly recommended. Deviation requires documented justification. |
| **SHOULD NOT** | Strongly discouraged. Deviation requires documented justification. |
| **MAY** | Permitted but not required. |

---

## 2. SCR Architecture Overview

### 2.1 Functional Role

The SCR is the synchronization architecture that enables temporal manufacturing operations to be committed to substrate with defined phase relationships. Without the SCR, the TRS Commit Layer (L4) has no shared time reference against which to place temporal addresses, and no mechanism to prevent conflicting operations from being committed concurrently.

The SCR provides three capabilities that are prerequisites for temporal manufacturing:

1. **A common time reference** shared by all commit endpoints within a zone, with bounded phase deviation across the zone
2. **An arbitration mechanism** that authorizes operations for commit in a defined sequence, enforcing the causal ordering produced by the TRS Sequencing Layer (L2)
3. **An integrity monitoring system** that detects deviations from the expected coherence state in real time and triggers defined responses before those deviations produce committed defects

### 2.2 Component Summary

The SCR comprises five component classes:

| Component Class | Abbreviation | Role |
|---|---|---|
| Coherence Clock Generator | CCG | Produces the master zone timing reference |
| Clock Distribution Network | CDN | Propagates the zone clock to all endpoints |
| Commit Arbiter | CA | Authorizes commit operations per coherence slot |
| Coherence Monitor Array | CMA | Verifies clock integrity across the zone |
| Zone Boundary Interface | ZBI | Manages inter-zone handoff |

Each component class is specified in detail in the sections that follow. All five classes MUST be present in any conformant SCR installation. No component class is optional.

### 2.3 System Boundary

The SCR system boundary is defined as follows:

- **Upstream interface:** The TRS Sequencing Layer (L2) delivers an ordered operation graph to the Commit Arbiter. The SCR does not interact with TRS layers L1 or L3 directly.
- **Downstream interface:** The Commit Arbiter issues authorization signals to TRS Commit Layer (L4) endpoints (Temporal Commit Units). The SCR does not control the physical commit mechanism; it controls only the timing and authorization of commit operations.
- **Lateral interface:** The Zone Boundary Interface connects to peer ZBIs in adjacent SCR zones. This interface is symmetric; both sides of a zone boundary are governed by the same handoff protocol.
- **Monitoring interface:** The Coherence Monitor Array reports to the fab's yield management system. CMA data is consumed externally; the SCR does not interpret CMA output internally.

The fab scheduler interacts with the SCR through a defined scheduling interface that is specified in [Section 11](#11-scr-interface-contracts).

---

## 3. Coherence Clock System

### 3.1 Coherence Clock Requirements

The coherence clock is the timing backbone of the SCR. All temporal operations within a zone are referenced to it. Its properties directly determine the minimum achievable coherence cycle duration, the maximum temporal density, and the phase deviation budget available to commit endpoints.

A conformant coherence clock system MUST satisfy the following requirements:

**R-CLK-01:** The CCG MUST produce a periodic reference signal with a period equal to the target coherence cycle duration, within a frequency accuracy of ±0.1 ppm over the qualified operating temperature range.

**R-CLK-02:** The phase noise of the CCG output MUST be below −130 dBc/Hz at 100 Hz offset from the carrier, and below −160 dBc/Hz at 1 MHz offset.

**R-CLK-03:** The CDN MUST deliver the clock signal to all TCU endpoints within the zone such that the worst-case phase deviation between any two endpoints does not exceed **δ_max**, where δ_max is defined per zone during SCR qualification and MUST NOT exceed 5% of the coherence cycle period.

**R-CLK-04:** The CCG MUST include a holdover capability that maintains frequency accuracy within ±1 ppm for a minimum of 100 ms following loss of the primary reference input.

**R-CLK-05:** The CDN MUST support active deskew at each distribution node to compensate for path-length variation introduced by routing geometry.

**R-CLK-06:** The coherence clock system MUST provide a deterministic phase relationship between the zone clock and the fab master clock, with a defined and stable offset measured during commissioning.

### 3.2 Clock Generation Architecture

The CCG is the sole authoritative source of the zone clock within its zone. Multiple CCGs MUST NOT operate within the same zone. A zone MUST have exactly one CCG.

The CCG generates the zone clock from a primary reference. The primary reference is provided by the fab master clock system, which operates at a frequency that is a rational multiple of all zone clock frequencies in the fab. This relationship MUST be established during fab commissioning and MUST NOT change without full SCR recommission.

The CCG contains an internal oscillator that serves as the holdover source (per R-CLK-04). The internal oscillator is disciplined to the primary reference during normal operation and freewheels during holdover events. CCG implementations MUST document the disciplining loop time constant and the holdover frequency drift rate.

### 3.3 Clock Distribution Network

The CDN distributes the zone clock from the CCG output to every TCU endpoint within the zone. It is a physical network of transmission lines, active repeaters, and deskew elements.

**Topology:** The CDN MUST use a balanced H-tree or equivalent topology that equalizes path lengths from the CCG to all endpoints within the deskew correction range of the active deskew nodes. Star topologies with unequal path lengths are non-conformant unless active deskew achieves R-CLK-03 compliance.

**Active deskew nodes:** CDN deskew nodes MUST be placed such that no endpoint is more than one deskew node removed from the CCG. Chains of deskew nodes accumulate jitter and are non-conformant.

**Signal integrity:** The CDN MUST maintain clock signal integrity such that the duty cycle at any endpoint is within 50% ± 2% after deskew. Duty cycle distortion beyond this bound introduces asymmetric timing margins in the commit arbitration protocol.

**Physical medium:** The CDN transmission medium MUST be specified as part of the SCR qualification record. Changes to the CDN medium after qualification require re-measurement of δ_max and, if δ_max increases, partial or full recommission depending on the magnitude of change (see [Section 10](#10-scr-qualification-and-commissioning)).

### 3.4 Clock Integrity Verification

Clock integrity MUST be verified by the CMA (see [Section 8](#8-coherence-monitoring)) on a per-coherence-cycle basis. The CMA checks that the clock signal received at each monitored endpoint is within the phase deviation budget δ_max and that no cycle has been missed or doubled.

A clock integrity failure detected by the CMA MUST cause the Commit Arbiter to withhold authorization for the affected coherence slot. Operations assigned to that slot are suspended, not discarded; they are rescheduled to the next available slot by the L2 Sequencing Layer upon notification.

---

## 4. Zone Architecture

### 4.1 Zone Definition

An SCR zone is a bounded physical region of a fab within which all TCU endpoints share a single coherence clock and a single Commit Arbiter. The zone is the fundamental unit of SCR organization.

**Zone properties:**

- **Single CCG:** Exactly one CCG per zone (§3.2)
- **Single CA:** Exactly one Commit Arbiter per zone (§5.1)
- **Bounded extent:** The zone's physical extent MUST be small enough that the CDN can distribute the zone clock to all endpoints within δ_max at the target coherence cycle period
- **Defined boundaries:** Zone boundaries are physically defined by the CDN routing perimeter and the ZBI installation points

### 4.2 Zone Sizing

Zone size is constrained by the synchronization latency floor (SLF), which is derived from the zone's physical extent and the CDN signal propagation velocity (see [Section 6](#6-synchronization-latency-floor)).

The maximum zone radius r_max for a given coherence cycle period T_c and CDN propagation velocity v_p is:

```
r_max = (T_c × δ_max_fraction × v_p) / 2

Where:
  T_c             = coherence cycle period (ns)
  δ_max_fraction  = maximum allowed phase deviation as fraction of T_c (≤ 0.05 per R-CLK-03)
  v_p             = CDN signal propagation velocity (m/ns)
  r_max           = maximum zone radius (m)
```

Fab architects MUST verify that all TCU endpoints within a proposed zone fall within r_max of the CCG location before committing to a zone boundary configuration.

### 4.3 Zone Configuration Rules

**R-ZONE-01:** Every TCU in the fab MUST belong to exactly one zone. TCUs MUST NOT be shared between zones.

**R-ZONE-02:** A zone boundary MUST NOT bisect a die. All TCUs that commit operations to the same die MUST be in the same zone, or the die design MUST route all inter-zone signals through defined ZBI paths with explicit latency budgets.

**R-ZONE-03:** Zone boundaries MUST be physically marked and recorded in the fab's SCR configuration record. The configuration record MUST be updated before any zone boundary change takes effect.

**R-ZONE-04:** Zone configuration changes MUST NOT be made while wafers are in process within the affected zone. The zone MUST be quiesced (all in-flight operations completed and no new operations admitted) before any configuration change.

**R-ZONE-05:** Zones MUST NOT be nested. A zone that contains another zone is non-conformant.

### 4.4 Multi-Zone Fabs

Fabs with multiple zones MUST designate one zone as the **primary zone**. The primary zone's CCG provides the timing reference from which all other zones derive their clocks, maintaining a rational frequency relationship to the fab master clock.

Secondary zone CCGs MUST lock to the primary zone clock via a defined reference distribution path. The reference distribution path is not the same as the CDN; it is a dedicated low-jitter reference link that connects the primary CCG to each secondary CCG.

The frequency relationship between zones MUST be an integer ratio. Non-integer ratios between zone clock frequencies are non-conformant because they preclude a common coherence boundary at which inter-zone handoff can occur with deterministic latency.

### 4.5 Zone Isolation

Zones are electrically and temporally isolated except at ZBI points. A failure within one zone MUST NOT propagate to adjacent zones. This isolation property is enforced by:

- **Electrical isolation:** The CDN of each zone is electrically isolated at zone boundaries. CDN signals do not cross zone boundaries; only the ZBI inter-zone reference link crosses zone boundaries.
- **Arbiter isolation:** Each zone's Commit Arbiter operates independently. The arbiters do not communicate directly; inter-zone coordination is handled exclusively through the ZBI protocol.
- **CMA isolation:** Each zone's CMA monitors only its own zone. CMA alerts from one zone do not directly trigger responses in adjacent zones.

---

## 5. Commit Arbitration

### 5.1 Commit Arbiter Architecture

The Commit Arbiter (CA) is the component that authorizes TCUs to execute commit operations during a specified coherence slot. It is the enforcement point for the causal ordering and sequencing constraints produced by the TRS Sequencing Layer (L2).

The CA receives two inputs:

1. **The operation graph** from L2, which specifies the set of operations to be committed in the current and upcoming coherence cycles, their coherence slot assignments, and their causal dependencies
2. **The clock signal** from the CCG via the CDN, which defines the coherence slot boundaries against which authorization signals must be timed

The CA produces one output:

- **Authorization signals** delivered to each TCU, precisely timed to the coherence slot in which the authorized operation must begin

### 5.2 Authorization Protocol

The authorization protocol operates on a per-slot basis within each coherence cycle. The cycle is divided into a fixed number of slots N_slots, determined during SCR qualification. N_slots MUST be a power of two and MUST NOT change after qualification without full recommission.

For each coherence slot s in cycle c, the CA executes the following sequence:

1. **Pre-slot verification:** The CA verifies that all causal predecessors of operations assigned to slot s have received commit-complete acknowledgment from their respective TCUs. If any predecessor is unresolved, the CA withholds authorization for slot s and escalates to the deferred-slot procedure (§5.4).

2. **Authorization window:** At the slot boundary, the CA asserts authorization signals to all TCUs assigned to slot s simultaneously. The authorization signal MUST be asserted within a setup window of T_auth before the slot boundary, where T_auth is defined per zone during qualification.

3. **Commit window:** Each authorized TCU executes its commit operation within the slot's commit window. The commit window duration MUST be less than the slot period minus the acknowledgment propagation time.

4. **Acknowledgment:** Each TCU asserts a commit-complete acknowledgment signal upon completing its operation. The CA MUST receive acknowledgment from all authorized TCUs before the end of the slot's acknowledgment window, or a timeout is declared (§9.2).

5. **Slot close:** The CA records the slot's completion status and advances to the next slot.

**R-ARB-01:** The CA MUST NOT authorize an operation for commit unless all of its causal predecessors, as specified in the L2 operation graph, have been acknowledged as committed.

**R-ARB-02:** The CA MUST NOT authorize two operations for the same coherence slot if they are assigned to the same spatial region of the substrate and their temporal addresses overlap within the substrate's minimum address spacing for the qualified SC class.

**R-ARB-03:** Authorization signals MUST be asserted within the specified T_auth setup window. Authorization asserted after the slot boundary is a timing violation and MUST cause the CA to void the authorization and treat the operation as deferred (§5.4).

**R-ARB-04:** The CA MUST maintain an audit log of all authorization decisions, including slot assignments, authorization timestamps, and acknowledgment timestamps. The audit log MUST be retained for the duration of the wafer lot and MUST be accessible to the yield management system.

### 5.3 Operation Graph Ingestion

The CA ingests the operation graph from L2 via a defined protocol. The operation graph is delivered as a structured record containing:

- Operation identifier (unique within the wafer lot)
- Substrate coordinates (x, y, layer)
- Temporal address
- Coherence slot assignment (zone, cycle index, slot index)
- Causal predecessor list (operation identifiers)
- SC class requirement

The CA validates each incoming operation record against the following checks before admitting it to the arbitration queue:

- Slot assignment is within the zone's qualified N_slots range
- SC class requirement matches the qualified substrate at the specified layer
- Predecessor operation identifiers are known to the CA (registered in a prior ingestion or the current batch)
- Temporal address is within the substrate's minimum address spacing from any concurrently active operation in the same spatial region

Operations that fail validation are rejected and returned to L2 with a rejection code. L2 is responsible for resolving the rejection and resubmitting.

### 5.4 Deferred-Slot Procedure

When the CA withholds authorization for a slot due to an unresolved predecessor, the affected operations enter the deferred-slot queue. The deferred-slot procedure is:

1. The CA notifies L2 that the operation has been deferred, including the reason (unresolved predecessor identifier and its last known status).
2. L2 updates the operation's slot assignment to the next available slot in which all predecessors are projected to be resolved.
3. The CA re-admits the operation from the deferred queue when L2 delivers the updated slot assignment.
4. If an operation has been deferred more than D_max times within a single wafer step (where D_max is a qualified parameter), the CA escalates to the fab scheduler as a sequencing anomaly.

**R-ARB-05:** The deferred-slot queue MUST be FIFO within each priority class. Operations MUST NOT be reordered within the queue except by explicit L2 re-assignment.

**R-ARB-06:** D_max MUST be defined and documented in the SCR qualification record. The default value is 8. Implementations MAY increase D_max; they MUST NOT reduce it below 4.

### 5.5 Arbiter Redundancy

**R-ARB-07:** The CA MUST implement hot-standby redundancy. A standby CA instance MUST be present and synchronized to the primary CA state continuously. Failover from primary to standby MUST complete within one coherence cycle without loss of any operation that had received authorization.

**R-ARB-08:** The standby CA MUST NOT authorize operations independently. It monitors primary CA state and takes over exclusively on detection of primary CA failure. Dual-active arbiter configurations are non-conformant.

---

## 6. Synchronization Latency Floor

### 6.1 Definition

The **Synchronization Latency Floor (SLF)** is the minimum coherence cycle duration that a given SCR zone installation can support without risk of partial-cycle commits. It is a physical property of the installed SCR infrastructure, determined by measurement during commissioning and fixed for the life of that installation.

A coherence cycle duration shorter than the SLF is non-conformant for that installation. The SLF is not a design target; it is a constraint that the designed coherence cycle duration must exceed.

### 6.2 SLF Derivation

The SLF is the sum of four latency components, measured at the worst-case path within the zone:

```
SLF = T_prop + T_arb + T_ack + T_margin

Where:
  T_prop   = maximum CDN propagation latency from CCG to the farthest TCU endpoint (ns)
  T_arb    = Commit Arbiter processing latency, from slot boundary detection to
             authorization signal assertion (ns)
  T_ack    = maximum acknowledgment propagation latency from the farthest TCU
             endpoint to the CA (ns)
  T_margin = implementation margin, MUST NOT be less than 10% of (T_prop + T_arb + T_ack)
```

Each component is measured independently during commissioning. The SLF value recorded in the SCR qualification record is the sum of the measured worst-case values with the required margin applied.

### 6.3 SLF Measurement Protocol

SLF component measurements MUST be performed under the following conditions:

- At the maximum operating temperature of the fab environment
- With all TCU endpoints and CDN active nodes powered and operational
- After a minimum of 30 minutes of thermal stabilization at operating temperature
- Using calibrated time-domain reflectometry for T_prop and T_ack measurements
- Using CA internal instrumentation for T_arb measurement

Each component MUST be measured at a minimum of 10 representative endpoints distributed across the zone extent. The worst-case measured value across all endpoints is the value used in the SLF calculation.

**R-SLF-01:** The target coherence cycle duration T_c MUST satisfy T_c > SLF × 1.05. The 5% overhead above the SLF is required to provide margin for manufacturing variation in CDN path lengths and for CCG jitter accumulation.

**R-SLF-02:** The SLF MUST be remeasured whenever any of the following occur:
- A CDN active node is replaced
- The CDN routing is modified
- The CA is replaced or its firmware is updated
- The operating temperature range of the fab changes by more than ±5°C from the qualification measurement conditions

**R-SLF-03:** The SLF value in the SCR qualification record MUST be updated following any remeasurement. If the new SLF exceeds the prior SLF such that the existing T_c no longer satisfies R-SLF-01, production MUST be halted until T_c is adjusted or the SLF is reduced.

### 6.4 SLF Reduction Strategies

When a process roadmap requires a shorter coherence cycle duration than the current SLF permits, the SLF must be reduced. The available strategies and their tradeoffs are:

| Strategy | Effect on SLF Component | Implementation Complexity | Requires Recommission |
|---|---|---|---|
| Reduce zone physical extent (add zones) | Reduces T_prop, T_ack | High (infrastructure change) | Yes |
| Upgrade CDN medium to higher propagation velocity | Reduces T_prop, T_ack | High (physical replacement) | Yes |
| Replace CA with lower-latency implementation | Reduces T_arb | Medium (equipment swap) | Partial (T_arb only) |
| Optimize CDN topology (shorter paths) | Reduces T_prop, T_ack | Medium (re-routing) | Partial (T_prop only) |
| Reduce T_margin (requires risk assessment) | Reduces margin component | Low (documentation change) | No, but requires review board approval |

Reducing T_margin below 10% is non-conformant per the SLF derivation formula and requires a formal waiver with documented risk assessment.

---

## 7. Inter-Zone Handoff Protocol

### 7.1 Purpose

When an operation's causal dependencies span two or more zones, or when a die's design requires commit operations in multiple zones, a coordination mechanism is required to ensure that the cross-zone causal constraints are honored. This mechanism is the **inter-zone handoff protocol**, implemented at the Zone Boundary Interface (ZBI).

The handoff protocol does not synchronize the clocks of adjacent zones. Zone clocks are independent (§4.5). Instead, it provides a defined latency contract: a message sent from Zone A to Zone B via the ZBI arrives at Zone B within a bounded number of Zone B coherence cycles, allowing L2 in Zone B to reserve coherence slots accordingly.

### 7.2 ZBI Component Requirements

**R-ZBI-01:** Every zone boundary MUST be served by at least one ZBI on each side of the boundary. Zones with a large inter-zone operation volume SHOULD install multiple ZBIs per boundary to provide bandwidth headroom.

**R-ZBI-02:** ZBI pairs (one on each side of a boundary) MUST be matched in firmware version and configuration. Mismatched ZBI pairs are non-conformant.

**R-ZBI-03:** Each ZBI MUST implement electrical isolation between the zones it connects. A fault on one zone's power or ground MUST NOT propagate to the adjacent zone through the ZBI.

**R-ZBI-04:** The ZBI MUST buffer outgoing messages independently of incoming messages. A congested incoming path MUST NOT delay outgoing messages.

### 7.3 Handoff Latency Contract

The ZBI latency contract specifies the maximum number of Zone B coherence cycles that elapse between the transmission of a handoff message from Zone A and its availability for processing by Zone B's Commit Arbiter.

```
L_handoff = ceil((T_ZBI + T_CDN_B) / T_c_B)

Where:
  T_ZBI    = ZBI message transmission latency (measured during commissioning, ns)
  T_CDN_B  = CDN propagation latency from Zone B ZBI endpoint to Zone B CA (ns)
  T_c_B    = Zone B coherence cycle period (ns)
  L_handoff = handoff latency in Zone B coherence cycles (integer, rounded up)
```

L_handoff MUST be measured and recorded for each zone boundary during commissioning. L2 systems that schedule cross-zone operations MUST use the recorded L_handoff value to compute the earliest coherence slot in Zone B at which a cross-zone operation can be authorized.

**R-ZBI-05:** L_handoff MUST be a positive integer. An L_handoff of zero is non-conformant; it would imply that Zone B can receive and process a handoff message within its current coherence slot, which cannot be guaranteed given the independent zone clocks.

**R-ZBI-06:** L_handoff MUST be remeasured whenever the ZBI firmware is updated or the CDN routing between the ZBI and Zone B's CA is modified.

### 7.4 Handoff Message Format

A handoff message transmitted by Zone A to Zone B carries the following fields:

| Field | Type | Description |
|---|---|---|
| `source_zone_id` | uint16 | Zone A identifier |
| `dest_zone_id` | uint16 | Zone B identifier |
| `operation_id` | uint64 | Operation identifier (unique within wafer lot) |
| `ack_type` | enum | `COMMIT_COMPLETE` or `COMMIT_VOID` |
| `source_cycle_index` | uint64 | Zone A coherence cycle in which the operation was committed or voided |
| `source_slot_index` | uint8 | Zone A coherence slot within that cycle |
| `checksum` | uint32 | CRC-32 of all preceding fields |

Zone B's ZBI validates the checksum upon receipt. A checksum failure causes the message to be discarded and a retransmission request to be sent to Zone A's ZBI. If three consecutive retransmissions fail validation, the ZBI escalates to the fab's yield management system as a ZBI integrity fault.

### 7.5 Cross-Zone Operation Scheduling

The L2 Sequencing Layer is responsible for scheduling cross-zone operations with knowledge of L_handoff for each relevant boundary. The scheduling rules are:

1. An operation in Zone B that depends on an operation in Zone A MUST be assigned to a Zone B coherence slot no earlier than L_handoff cycles after the Zone A operation's assigned slot.
2. The Zone A CA transmits the handoff message immediately upon receiving commit acknowledgment from the Zone A TCU.
3. The Zone B CA does not authorize the dependent operation until the handoff message is received and validated. If the message is not received by the slot deadline, the Zone B operation is deferred (§5.4) and L2 is notified.

---

## 8. Coherence Monitoring

### 8.1 Coherence Monitor Array Architecture

The **Coherence Monitor Array (CMA)** is a distributed set of sensor nodes deployed throughout the zone that continuously verify the integrity of the coherence clock as received at representative points across the zone. The CMA is passive with respect to the CDN; it observes but does not modify the clock signal.

**R-CMA-01:** CMA sensor nodes MUST be deployed at a minimum density of one node per 0.5 × r_max radius from the CCG, in at least four angular quadrants. This distribution ensures that phase deviation at the zone periphery is monitored regardless of the angular position of the farthest TCU.

**R-CMA-02:** Each CMA sensor node MUST independently measure and report: clock period, duty cycle, and phase relative to the CCG reference signal. Reports MUST be produced on a per-coherence-cycle basis.

**R-CMA-03:** CMA sensor nodes MUST be electrically isolated from the CDN. Faults in a CMA node MUST NOT affect clock signal integrity at any CDN endpoint.

### 8.2 Monitored Parameters

The CMA monitors the following parameters at each sensor node on every coherence cycle:

| Parameter | Alarm Threshold | Action on Alarm |
|---|---|---|
| Clock period deviation | > ±0.5% of T_c | Advisory; log to yield management |
| Duty cycle deviation | > ±2% of 50% | Advisory; log to yield management |
| Phase deviation from CCG reference | > 80% of δ_max | Warning; notify CA |
| Phase deviation from CCG reference | > δ_max | Critical; CA withholds slot authorization |
| Missing clock cycle | Any occurrence | Critical; CA withholds slot authorization; CCG holdover initiated |
| Doubled clock cycle | Any occurrence | Critical; CA withholds slot authorization; fab scheduler notified |

### 8.3 CMA Data Handling

CMA reports are delivered to two consumers:

1. **The Commit Arbiter:** Receives real-time critical alerts (phase > δ_max, missing/doubled cycle). The CA acts on these alerts within the current coherence cycle. CMA-to-CA alert latency MUST be less than 10% of T_c.

2. **The yield management system:** Receives all CMA reports for logging, trend analysis, and correlation with defect maps. The yield management system may use CMA trend data to trigger preventive SCR maintenance before alert thresholds are reached.

**R-CMA-04:** The CMA MUST continue to operate and report during CCG holdover events. CMA reports during holdover MUST be flagged to distinguish them from normal-operation reports.

**R-CMA-05:** CMA sensor nodes MUST self-test on power-up and report test results to the yield management system. A sensor node that fails self-test MUST be treated as absent for coverage calculation purposes. If the removal of failed nodes causes coverage to fall below R-CMA-01 requirements, production in the affected zone MUST be halted until coverage is restored.

### 8.4 Post-Process Coherence Audit

In addition to real-time monitoring, a post-process coherence audit MUST be performed at the end of each wafer step that includes temporal operations. The audit correlates the CA's authorization log with the CMA's cycle-by-cycle reports to identify any operations that were authorized during a degraded coherence window.

Operations identified by the post-process audit as having been committed during a degraded coherence window are flagged in the wafer lot record. Flagged operations do not automatically result in wafer rejection; they are forwarded to the yield management system for correlation with post-process inspection results.

---

## 9. SCR Failure Modes and Recovery

### 9.1 Failure Classification

SCR failures are classified into three severity levels:

| Level | Name | Definition | Required Response |
|---|---|---|---|
| **L1** | Advisory | Parameter deviation within operating range; no immediate risk to commit fidelity | Log; no operational impact |
| **L2** | Warning | Parameter deviation approaching threshold; risk to commit fidelity if not addressed | Log; notify operators; increase monitoring frequency |
| **L3** | Critical | Parameter deviation exceeds threshold or component failure; confirmed or imminent risk to commit fidelity | Suspend slot authorization; halt production in affected zone; initiate recovery |

### 9.2 Specific Failure Modes

#### 9.2.1 CCG Primary Reference Loss

**Classification:** L2 if holdover is active and stable; L3 if holdover frequency exceeds ±1 ppm drift

**Cause:** Loss of the primary reference signal from the fab master clock to the CCG.

**Detection:** CCG internal monitoring; CMA will observe slow frequency drift if holdover is not maintaining accuracy.

**Recovery procedure:**
1. CCG switches to holdover automatically (§3.2); CA and CMA continue normal operation
2. Fab scheduler notified of holdover condition; new wafer starts in the affected zone are suspended
3. In-flight wafers continue to process; their records are flagged as processed under holdover
4. If holdover is restored within the CCG holdover stability window (100 ms per R-CLK-04), production resumes without additional qualification
5. If holdover exceeds 100 ms, zone is quiesced and SLF is remeasured before production resumes

#### 9.2.2 CDN Node Failure

**Classification:** L3 if the failed node is in the primary distribution path; L2 if the failed node is a redundant path

**Cause:** Failure of a CDN active repeater or deskew node.

**Detection:** CMA will observe phase deviation increase at endpoints downstream of the failed node; CDN self-monitoring may also report directly.

**Recovery procedure:**
1. Affected zone is quiesced
2. Failed node is identified by correlating CMA phase deviation reports with CDN topology
3. Node is replaced and the CDN is re-deskewed
4. δ_max is remeasured at endpoints downstream of the replaced node
5. If measured δ_max is within qualification limits, production resumes
6. If measured δ_max exceeds qualification limits, partial recommission of the CDN is required

#### 9.2.3 Commit Arbiter Primary Failure

**Classification:** L3

**Cause:** Primary CA hardware failure, firmware fault, or loss of power.

**Detection:** Watchdog timeout; standby CA detects loss of primary CA heartbeat.

**Recovery procedure:**
1. Standby CA takes over within one coherence cycle per R-ARB-07
2. Standby CA replays any operations that were in the authorization window at the time of failover, using the synchronized state copy
3. CA failover event is logged and the wafer lot record is flagged
4. Primary CA is replaced or restored; standby CA role is re-established before the replacement primary returns to service
5. A post-failover coherence audit (§8.4) is performed immediately after failover, not waiting for end of wafer step

#### 9.2.4 ZBI Integrity Fault

**Classification:** L3 for the cross-zone operation traffic affected; L1 for traffic on unaffected boundaries

**Cause:** Repeated checksum failures on ZBI messages (§7.4).

**Detection:** ZBI internal monitoring; escalation after three consecutive retransmission failures.

**Recovery procedure:**
1. Cross-zone operations that depend on the affected boundary are suspended; in-zone operations continue
2. ZBI is tested using a defined diagnostic sequence
3. If the fault is in the ZBI hardware, the unit is replaced and L_handoff is remeasured
4. If the fault is in the inter-zone link medium, the medium is inspected and repaired
5. Cross-zone operations resume after L_handoff remeasurement confirms compliance

#### 9.2.5 Coherence-Loss Event

**Classification:** L3

**Cause:** One or more TCUs execute commit operations outside a valid coherence window, either due to a clock integrity failure that was not caught before the commit window, or due to a CA authorization timing violation.

**Detection:** Post-process coherence audit (§8.4); TMU measurement of committed address error rate above the process threshold.

**Recovery procedure:**
1. Affected wafer lot is quarantined pending inspection
2. CA authorization log and CMA records are correlated to identify the affected operations and coherence cycles
3. TMU data is reviewed to assess whether the address error rate falls within the process defect budget
4. If within budget: wafer lot is released with flagged record
5. If outside budget: wafer lot disposition follows yield management escalation procedure
6. Root cause analysis is performed; corrective action is documented and tracked to closure

### 9.3 Recovery Validation

Following any L3 failure and recovery, the zone MUST pass a **Recovery Validation Test (RVT)** before production resumes. The RVT consists of:

1. A full CMA sweep confirming all monitored parameters are within normal operating range
2. A CA authorization log verification confirming clean state (no pending deferred operations from before the failure)
3. A minimum of one complete coherence cycle at the production T_c with no CMA warnings or critical alerts
4. Sign-off by the fab process engineering team

The RVT is documented and retained in the SCR maintenance record.

---

## 10. SCR Qualification and Commissioning

### 10.1 New Installation Qualification

A new SCR installation MUST complete the following qualification sequence before any production wafers are processed. This sequence applies to new fab construction and to installations replacing a prior SCR at the same facility.

**Phase 1 — Infrastructure Verification**

1. Physical installation of all CCG, CDN, CA, CMA, and ZBI components verified against the design bill of materials
2. Electrical isolation between zones verified by continuity measurement
3. CCG primary reference lock verified and frequency accuracy measured per R-CLK-01
4. Phase noise measured per R-CLK-02
5. CDN duty cycle measured at all endpoints per §3.3

**Phase 2 — SLF Measurement**

1. T_prop measured at all TCU endpoints per §6.3
2. T_arb measured using CA instrumentation per §6.3
3. T_ack measured at all TCU endpoints per §6.3
4. SLF calculated and recorded per §6.2
5. Coherence cycle period T_c confirmed to satisfy R-SLF-01

**Phase 3 — δ_max Measurement**

1. Phase deviation measured between all endpoint pairs per R-CLK-03
2. Worst-case δ_max recorded; confirmed to be ≤ 5% of T_c

**Phase 4 — CMA Qualification**

1. CMA sensor nodes powered and self-test confirmed per R-CMA-05
2. CMA coverage density confirmed per R-CMA-01
3. CMA alert delivery latency to CA measured and confirmed < 10% of T_c per R-CMA-04
4. Simulated phase deviation fault injected; CMA alert and CA response verified

**Phase 5 — Arbiter Qualification**

1. CA ingests a test operation graph and produces authorization signals against a reference substrate
2. Authorization timing verified against T_auth specification
3. Causal ordering enforced correctly for a defined set of test cases including dependencies and deferrals
4. Standby CA failover tested per R-ARB-07; failover latency confirmed ≤ one coherence cycle

**Phase 6 — ZBI Qualification (multi-zone only)**

1. ZBI pairs powered and firmware version matched per R-ZBI-02
2. L_handoff measured per §7.3 for all zone boundaries
3. ZBI checksum validation tested using intentionally corrupted messages
4. Retransmission and escalation behavior verified

**Phase 7 — Full-System Operational Test**

1. End-to-end TRS stack exercised with a qualified test process at minimum temporal density
2. CMA, CA audit log, and TMU data reviewed for anomalies
3. Recovery Validation Test (§9.3) performed as a baseline
4. All Phase 1–7 results compiled into the SCR Qualification Record

### 10.2 Partial Recommission Triggers

Partial recommission is required when a component change affects one measurable SCR parameter without affecting others. The scope of recommission is limited to the affected parameter:

| Change | Recommission Scope |
|---|---|
| CDN node replacement | Re-measure δ_max at affected endpoints; recalculate T_prop; update SLF |
| CA replacement | Re-measure T_arb; update SLF |
| ZBI firmware update | Re-measure L_handoff for affected boundaries |
| Operating temperature range change | Full SLF remeasurement (Phases 2–3) |
| Zone boundary modification | Full recommission for affected zones (Phases 1–7) |

### 10.3 SCR Qualification Record

The SCR Qualification Record MUST be maintained for the life of the installation. It MUST include:

- Facility identifier and zone map
- Bill of materials for all SCR components (manufacturer, model, firmware version, serial number)
- All Phase 1–7 measurement results from initial qualification
- Chronological log of all partial recommissions with before/after measurements
- Failure events and recovery records per §9
- Current effective values: SLF, δ_max, T_c, N_slots, D_max, L_handoff (per boundary)

The Qualification Record MUST be available to the yield management system and MUST be producible on request during process audits.

---

## 11. SCR Interface Contracts

### 11.1 TRS L2 Interface (Operation Graph Delivery)

The L2-to-CA interface delivers operation graphs for arbitration. The interface contract specifies:

| Parameter | Requirement |
|---|---|
| Delivery timing | Operation graph for cycle c MUST be delivered to the CA no later than T_graph before the first slot boundary of cycle c, where T_graph ≥ T_arb |
| Format | Structured record per §5.3 |
| Rejection handling | L2 MUST handle CA rejections within 2 coherence cycles; unhandled rejections escalate to the fab scheduler |
| Deferral notification | CA notifies L2 of deferrals within the deferred slot; L2 MUST respond with an updated slot assignment within D_max cycles |

### 11.2 TRS L4 Interface (TCU Authorization)

The CA-to-TCU interface delivers authorization signals and receives acknowledgments. The interface contract specifies:

| Parameter | Requirement |
|---|---|
| Authorization signal | Asserted within T_auth before slot boundary per R-ARB-02 |
| Authorization duration | Signal held asserted for the full commit window duration |
| Acknowledgment | TCU asserts commit-complete within the acknowledgment window; width ≥ 5 ns |
| Timeout | If acknowledgment not received within the acknowledgment window, CA treats as timeout (§9.2.4 analog — logged as L2 event, CA scheduler consulted) |
| Signal levels | Defined in the TCU hardware interface specification for the qualified substrate class |

### 11.3 Fab Scheduler Interface

The fab scheduler interacts with the SCR to manage wafer flow into and out of SCR zones. The interface contract specifies:

| Message | Direction | Trigger |
|---|---|---|
| Zone ready | SCR → Scheduler | Zone completes RVT or recovers from L3 failure |
| Zone quiesce request | Scheduler → SCR | New wafer start or zone configuration change |
| Zone quiesced | SCR → Scheduler | All in-flight operations completed, no new operations |
| Holdover active | SCR → Scheduler | CCG switches to holdover |
| Sequencing anomaly | CA → Scheduler | D_max exceeded for an operation |
| ZBI integrity fault | ZBI → Scheduler | Three consecutive retransmission failures |

The fab scheduler MUST NOT admit new wafers into a zone while a quiesce request is pending or while the zone is in a quiesced state awaiting recovery.

### 11.4 Yield Management Interface

The yield management system receives data from the SCR for process control and defect analysis. The interface contract specifies:

| Data Stream | Source | Frequency | Retention |
|---|---|---|---|
| CMA per-cycle reports | CMA | Every coherence cycle | Lot duration + 90 days |
| CA authorization audit log | CA | Every coherence cycle | Lot duration + 90 days |
| ZBI message logs | ZBI | Per message | Lot duration + 90 days |
| CMA self-test results | CMA | Power-up | Life of installation |
| Post-process coherence audit results | CA + CMA (correlated) | Per wafer step | Lot duration + 90 days |
| SCR failure events | All components | On occurrence | Life of installation |

---

## 12. Conformance Requirements

### 12.1 Conformance Levels

This specification defines two conformance levels:

**Full Conformance:** The SCR installation satisfies all MUST requirements in this specification. Full conformance is required for production use of the SCR for temporal manufacturing operations.

**Partial Conformance:** The SCR installation satisfies all MUST requirements except those explicitly waived through the formal waiver process (§12.2). Partial conformance does not permit production use without explicit approval from the TriadicFrameworks process authority.

### 12.2 Waiver Process

A waiver is required for any deviation from a MUST requirement. Waivers MUST:

- Identify the specific requirement by its requirement identifier (e.g., R-CLK-03)
- Document the reason the requirement cannot be met
- Provide a risk assessment quantifying the impact on temporal manufacturing quality
- Specify compensating measures that partially mitigate the risk
- Be signed by the fab's process authority and retained in the SCR Qualification Record

Waivers for requirements marked with a specific prohibition against waiver (none in the current revision) are not permitted.

### 12.3 Conformance Verification

Conformance MUST be verified at the following occasions:

- Initial SCR commissioning (full conformance check across all requirements)
- Following any partial recommission (conformance check for affected requirements)
- Annually, as a standing operational audit (spot-check of measurable requirements)
- Following any L3 failure event (conformance check for requirements related to the failure mode)

Conformance verification results MUST be recorded in the SCR Qualification Record.

### 12.4 Non-Conformance Response

A non-conformance finding MUST result in:

1. Immediate cessation of production in the affected zone
2. Quarantine of all wafer lots processed in the zone since the last confirmed conformant state
3. Corrective action to restore conformance
4. Recommission of the affected parameters
5. Disposition of quarantined lots by the yield management system

A zone that has been returned to conformance following a non-conformance finding MUST pass a full Recovery Validation Test (§9.3) before production resumes.

---

## 13. Glossary

| Term | Definition |
|---|---|
| **CA** | Commit Arbiter — authorizes TCUs to execute commit operations within specified coherence slots |
| **CBA** | Coherence Budget Analysis — design verification check; defined in The Temporal Manufacturing Primer |
| **CCG** | Coherence Clock Generator — master timing source for an SCR zone |
| **CDN** | Clock Distribution Network — distributes the zone clock to all TCU endpoints |
| **CMA** | Coherence Monitor Array — distributed sensors verifying clock integrity across a zone |
| **Coherence cycle** | The fundamental repeating time unit of SCR operation, defined by the CCG output period |
| **Coherence slot** | A subdivision of the coherence cycle to which specific commit operations are assigned |
| **Commit window** | The time within a coherence slot during which a TCU may execute a commit operation |
| **D_max** | Maximum number of times an operation may be deferred before escalation |
| **δ_max** | Maximum allowed phase deviation between any two CDN endpoints within a zone |
| **Full conformance** | SCR installation satisfying all MUST requirements in this specification |
| **L_handoff** | Inter-zone handoff latency measured in Zone B coherence cycles |
| **N_slots** | Number of coherence slots per coherence cycle; fixed at qualification |
| **Partial recommission** | Recommission limited to parameters affected by a specific component change |
| **RVT** | Recovery Validation Test — required test before resuming production after an L3 failure |
| **SC** | Substrate Clarity — defined in The Temporal Manufacturing Primer |
| **SCR** | Substrate Coherence Regime — the synchronization architecture for temporal manufacturing |
| **SCR Qualification Record** | The mandatory record of all qualification measurements and changes for an SCR installation |
| **SLF** | Synchronization Latency Floor — the minimum conformant coherence cycle duration for a given installation |
| **T_arb** | Commit Arbiter processing latency component of the SLF |
| **T_ack** | Acknowledgment propagation latency component of the SLF |
| **T_auth** | Setup window before slot boundary within which the CA must assert authorization |
| **T_c** | Coherence cycle period — the target duration of one coherence cycle |
| **T_graph** | Minimum lead time for L2 to deliver an operation graph before the first slot of the target cycle |
| **T_margin** | Implementation margin component of the SLF (minimum 10%) |
| **T_prop** | CDN propagation latency component of the SLF |
| **T_ZBI** | ZBI message transmission latency |
| **TCU** | Temporal Commit Unit — the Tier 2 fab tool that executes commit operations |
| **TMU** | Temporal Metrology Unit — in-line measurement tool for committed address fidelity |
| **TRS** | Temporal Resolution Stack — defined in The Temporal Manufacturing Primer |
| **ZBI** | Zone Boundary Interface — implements the inter-zone handoff protocol at zone boundaries |

---

## 14. Related Documents

| Document | Path | Relationship |
|---|---|---|
| The Temporal Manufacturing Primer | `docs/post-ASML_era/The_Temporal_Manufacturing_Primer.md` | Conceptual foundation; defines SCR at the operational level |
| TRS Stack Qualification Procedure | `docs/fab/TRS_Qualification.md` | Defines TCU qualification that depends on SCR infrastructure |
| SCR Zone Configuration Guide | `docs/fab/SCR_Zone_Config.md` | Implementation guidance for zone sizing and layout decisions |
| Temporal Contrast Test Protocol | `docs/metrology/TCT_Protocol.md` | Substrate clarity measurement; SC class determines TRS parameters the SCR must support |
| Temporal Timing Format Reference | `docs/eda/TTF_Reference.md` | Defines how L_handoff and T_arb are expressed as timing arcs in EDA tools |
| Post-ASML PDK Integration Guide | `docs/eda/PostASML_PDK_Integration.md` | Specifies how SCR zone boundaries and parameters are embedded in the process design kit |
| Substrate Clarity Classification Standard | `docs/materials/SC_Classification.md` | SC class requirements drive minimum temporal density, which constrains SCR T_c selection |

---

*This document is part of the TriadicFrameworks canonical reference set. Proposed revisions should be submitted via pull request to the `docs/post-ASML_era/` directory with a linked issue describing the change rationale. Revisions to normative requirements (MUST / MUST NOT) require review by at least two maintainers.*
