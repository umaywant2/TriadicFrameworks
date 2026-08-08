# The Logic Folding Architecture Guide

**Repository:** TriadicFrameworks
**Path:** `docs/post-ASML_era/The_Logic_Folding_Architecture_Guide.md`
**Status:** Canonical Reference
**Revision:** 1.0.0

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [The Logic Folding Concept](#2-the-logic-folding-concept)
3. [The Temporal Computation Model](#3-the-temporal-computation-model)
4. [Fold Architecture Types](#4-fold-architecture-types)
5. [Causal Depth and Fold Depth Analysis](#5-causal-depth-and-fold-depth-analysis)
6. [Temporal Register Architecture](#6-temporal-register-architecture)
7. [Inter-Fold Communication](#7-inter-fold-communication)
8. [Folding Efficiency](#8-folding-efficiency)
9. [Floorplanning for Logic Folding](#9-floorplanning-for-logic-folding)
10. [Timing Closure for Folded Logic](#10-timing-closure-for-folded-logic)
11. [Verification Methodology](#11-verification-methodology)
12. [Design Patterns](#12-design-patterns)
13. [Migration from Spatial Logic](#13-migration-from-spatial-logic)
14. [Glossary](#14-glossary)
15. [Related Documents](#15-related-documents)

---

## 1. Purpose and Scope

### 1.1 Purpose

This document is the architectural guide for **Logic Folding** — the methodology by
which computational structures are mapped into the temporal address space of a
post-ASML manufacturing process. It is the first design-facing document in the
post-ASML era series: where prior documents defined the manufacturing substrate
(TCT Protocol), the synchronization infrastructure (SCR Specification), the
measurement framework (TGI Metrology Standard), and the design rule interface
(TRS-Aware PDK Specification), this guide addresses how a designer or system
architect should think about and structure computation within those constraints.

Logic Folding is not an optional design style. It is the necessary consequence of
temporal manufacturing: because logical state is encoded as committed temporal
addresses in a substrate rather than as voltage levels in a gate network, the
organization of computation must follow the structure of the temporal address space
and the coherence cycle. A designer who attempts to apply classical spatial design
intuition directly to a temporal manufacturing target will encounter constraints that
appear arbitrary until the underlying model is understood. This guide provides that
model.

### 1.2 Intended Audience

This guide is written for:

- **Logic architects** defining the computational structure of a design intended for
  temporal manufacturing
- **RTL designers** translating high-level functional descriptions into fold-aware
  operation graphs
- **Physical design engineers** floorplanning and placing fold regions, temporal
  register files, and zone boundary crossings
- **Timing engineers** performing temporal timing closure using TTF-aware STA tools
- **Verification engineers** developing testbenches and assertion suites for folded
  logic

Readers are assumed to be familiar with the TRS-Aware PDK Specification
([`docs/post-ASML_era/The_TRS-Aware_PDK_Specification.md`](./The_TRS-Aware_PDK_Specification.md))
and to have working knowledge of the concepts introduced in The Temporal
Manufacturing Primer
([`docs/post-ASML_era/The_Temporal_Manufacturing_Primer.md`](./The_Temporal_Manufacturing_Primer.md)).
Readers who need background on the SCR, temporal density, or address spacing should
consult those documents first.

### 1.3 Scope

This guide covers:

- The conceptual basis of logic folding and its relationship to classical design
- The temporal computation model: how state, causality, and sequencing work in the
  temporal domain
- The four primary fold architecture types and their appropriate use cases
- Quantitative analysis of fold depth, fold width, and the trade-off between them
- Temporal register architecture: definition, state horizon, organization, and refresh
- Inter-fold communication: intra-zone and cross-zone handoff protocols at the
  architectural level
- Folding efficiency: the metric, its overhead sources, and targets by architecture
  type
- Floorplanning principles specific to folded logic
- Timing closure methodology, including temporal retiming and fold schedule
  optimization
- Verification methodology: fold-level functional verification, boundary assertions,
  register integrity, and cross-fold causal consistency
- Five canonical design patterns with their fold structure and use-case guidance
- Migration guidance from classical spatial logic to temporal manufacturing, including
  a mapping of classical constructs, constructs that do not translate, and hybrid
  architectures

This guide does not specify design rules; those are in the TDR component of the PDK.
It does not specify timing arc values; those are in the TTF arc library. It does not
specify metrology or process qualification. It is an architectural methodology
document.

---

## 2. The Logic Folding Concept

### 2.1 The Central Analogy

Classical digital logic encodes state as voltage levels and propagates computation
through networks of gates connected by wires. In that model, the two fundamental
resources are **area** (how many gates fit on the die) and **time** (how many gate
stages can be traversed in one clock cycle). Logic depth is a count of gate stages;
it is a spatial property of the circuit topology.

In temporal manufacturing, state is encoded as committed temporal addresses in a
substrate. The two fundamental resources remain area and time, but their relationship
to computation is different. **Area** now determines how many simultaneous operations
can be committed in parallel — how many spatially distinct sites can receive commits
in the same coherence slot. **Time** within a coherence cycle determines how many
sequentially dependent operations can be committed in a single cycle — how many
causally ordered steps can complete before the cycle boundary forces a pause.

The discipline of mapping a computational structure to these two resources — packing
causally ordered operations into coherence slots and parallel operations across
substrate area — is **Logic Folding**.

### 2.2 The Logic Fold Defined

A **Logic Fold** is the assignment of a subgraph of the full operation dependency
graph to a single coherence cycle. All operations assigned to a given fold execute
within that cycle's coherence slots. Operations that depend on the results of
operations in a prior fold must wait for the fold boundary — the coherence cycle
boundary — before they can be assigned a slot.

This is precisely analogous to a pipeline stage in classical design: a pipeline stage
groups the combinational logic that can be traversed in one clock period. A logic fold
groups the temporal operations that can be committed within one coherence cycle. The
fold boundary is the temporal equivalent of the pipeline register.

The critical differences from classical pipelining are:

1. **The boundary is physical, not logical.** A fold boundary occurs at the coherence
   cycle boundary enforced by the SCR. It is not a design choice that can be placed
   arbitrarily within the operation graph; it must align with coherence cycle structure.

2. **State crossing the boundary must be physically stored.** Results that a later
   fold depends on cannot simply propagate through substrate — they must be
   explicitly held in a **Temporal Register (TR)**, a substrate site that retains its
   committed address state between coherence cycles.

3. **The boundary imposes latency, not just sequencing.** Crossing a fold boundary
   costs one full coherence cycle of wall-clock time, plus the overhead of temporal
   register read and write operations within their respective cycles.

### 2.3 What Logic Folding Is Not

Logic folding is not data serialization. Serializing a wide computation over multiple
time steps to reduce area is a classical technique; logic folding is a fundamentally
different activity because the coherence cycle boundary is a physical constraint of
the manufacturing process, not a design choice made to save area.

Logic folding is not classical retiming. Classical retiming moves flip-flops across
combinational stages to balance path delays while preserving the sequential behavior
of the circuit. Temporal retiming (§10.2) adjusts fold boundaries to balance causal
depth across cycles, which is analogous in intent but operates on the operation
dependency graph rather than on a netlist.

Logic folding is not time-multiplexing of a shared computational resource. In time-
multiplexed systems, a single hardware unit performs different operations at different
time slots, with inputs and outputs managed by control logic. In temporal
manufacturing, every operation is committed to a specific substrate site permanently;
the temporal address is part of the committed state, not a tag applied at a shared
resource. Two operations at different temporal addresses in the same substrate region
are not competing for a resource — they are distinguishable states encoded at adjacent
addresses.

---

## 3. The Temporal Computation Model

### 3.1 State, Address, and Value

In a temporal manufacturing substrate, a logical value is encoded as a committed
temporal address. The precise relationship between the address τ and the logical value
it represents is defined by the **address-value mapping** of the design — a
convention established at design time and maintained consistently through all folds.

The simplest address-value mapping is binary threshold encoding: addresses in the
lower half of a designated address subrange encode logical 0; addresses in the upper
half encode logical 1. More complex encodings — thermometer codes, grey codes, analog
gradients — are possible and may offer advantages in specific design patterns (§12),
but binary threshold encoding is the default and is assumed throughout this guide
unless otherwise stated.

The key property of any address-value mapping is that it must be **discrimination-
safe**: the separation between the addresses encoding 0 and 1 must be ≥ Δτ_eff for
the substrate's SC class, so that the two states are resolvable by readback. Mappings
that place the 0 and 1 addresses closer than Δτ_eff are non-conformant; the two
states cannot be reliably distinguished and the logical value is undefined.

### 3.2 Operations and Causality

A temporal operation is the commitment of an address to a substrate site. It
corresponds to the evaluation of one logical function: the output address is
determined by the input addresses (the addresses committed at the predecessor sites in
the dependency graph) and the specific transformation the operation implements.

Causality in the temporal computation model is straightforward and strict:

- An operation cannot be committed until all operations it depends on have been
  committed and their results are stable and readable
- "Stable and readable" means the committed address has been acknowledged by the TCU
  and the ARS can read it back without readback noise exceeding the discrimination
  threshold
- In the temporal domain, readability is established after the commit window of the
  predecessor's coherence slot; the successor can be authorized in any subsequent slot
  in the same cycle (for intra-fold dependencies) or in any slot of the next cycle
  (for cross-fold dependencies requiring a temporal register)

### 3.3 The Dependency Graph as the Circuit

In classical design, the circuit netlist is the primary design artifact; timing
analysis is performed on the netlist to determine whether the circuit meets its
timing constraints. In temporal manufacturing, the **operation dependency graph** is
the primary design artifact. It is not derived from a netlist; it is the design.

Every node in the dependency graph is a temporal operation: a triple (substrate site,
temporal address, predecessor set). Every directed edge is a causal dependency. The
graph's topology encodes the computational structure; its node assignments encode the
substrate-level implementation.

This has an important implication: there is no separate synthesis step that maps
high-level logic onto a gate library and then onto a physical netlist. The mapping
from high-level intent to temporal operations is the synthesis step, and its output is
the dependency graph. The designer or synthesis tool must produce a dependency graph
that is simultaneously:

- Functionally correct (the causal ordering implements the intended computation)
- Rule-compliant (address spacing, density, TGI proximity, and causal graph rules are
  all satisfied)
- Foldable (the graph can be partitioned into coherence-cycle-aligned folds without
  violating any constraint)

### 3.4 The Coherence Cycle as the Computation Boundary

The coherence cycle is the fundamental time unit of temporal manufacturing. Within a
single coherence cycle, all operations in that cycle are committed to the substrate
in a defined causal order enforced by the Commit Arbiter. Between cycles, committed
states are held by temporal registers or by the substrate itself for operations that
do not need to be read across a cycle boundary.

From the design perspective, the coherence cycle has two structural properties that
dominate architectural decisions:

**Depth capacity:** The number of usable coherence slots, N_usable = N_slots − 2
(excluding the two reserved slots), is the maximum number of causally sequential
operations that can be committed in one cycle. A chain of operations longer than
N_usable cannot fit in one fold and must be split across fold boundaries.

**Width capacity:** The maximum number of operations per slot, N_slot_max, multiplied
by N_usable, gives B_cycle — the total operation budget per cycle per zone. This is
the maximum number of operations a single fold can contain, achievable only if all
operations are mutually independent (no causal dependencies within the fold). Real
folds lie between the two extremes of a fully sequential single chain (width 1, depth
N_usable) and a fully parallel flat graph (depth 1, width B_cycle).

---

## 4. Fold Architecture Types

### 4.1 Single-Cycle Folding

In **Single-Cycle Folding**, the entire computation completes within a single
coherence cycle. The dependency graph has a causal depth not exceeding N_usable, all
operations fit within B_cycle, and no temporal registers are required.

Single-cycle folding is the simplest and most efficient architecture type: there are
no fold boundaries, no TR overhead, and no inter-fold communication latency. It is
appropriate for:

- Computations with low causal depth relative to N_usable
- Computations with moderate total operation count relative to B_cycle
- Latency-critical paths where fold boundary overhead is unacceptable
- Small, self-contained functional units that will be instantiated many times on a die

The constraint is that both the depth and the total count must fit within one cycle.
For large computations with deep causal chains, single-cycle folding is not feasible
and multi-cycle folding is required.

### 4.2 Multi-Cycle Folding

In **Multi-Cycle Folding**, the computation is partitioned into a sequence of N_f
folds, each occupying one coherence cycle. The dependency graph is cut at N_f − 1
fold boundaries; each boundary cut defines a **Fold Cutset** — the set of operations
whose results must be written to temporal registers and read by the subsequent fold.

Multi-cycle folding is the most general architecture type and is used when:

- Causal depth exceeds N_usable for a single cycle
- The computation has a natural sequential structure (each fold produces results that
  the next fold consumes)
- The design must process data that arrives at the rate of one fold per coherence cycle

The total latency of a multi-cycle fold chain is N_f coherence cycles, plus the TR
read overhead at the start of each fold. Minimizing N_f while satisfying the depth
constraint at each fold is the primary optimization objective for multi-cycle folding;
this is accomplished through temporal retiming (§10.2).

### 4.3 Pipeline Folding

**Pipeline Folding** is the temporal analog of classical pipelining. A multi-cycle
computation is structured as a fold chain, but multiple instances of the computation
are in-flight simultaneously — each in a different fold stage at any given coherence
cycle. This is possible because successive coherence cycles are independent: the
second computation's first fold can begin in coherence cycle 2 while the first
computation's second fold occupies the same cycle.

Pipeline folding achieves high throughput at the cost of latency. If the fold chain
has N_f stages and a new computation is introduced every cycle, the throughput is one
result per coherence cycle and the latency is N_f coherence cycles. Classical pipeline
efficiency analysis applies with coherence cycles substituted for clock periods and
fold stages substituted for pipeline stages.

The constraints specific to temporal manufacturing are:

- Each pipeline stage occupies substrate area for its operations and its cutset
  temporal registers. The total die area consumed by an N_f-stage pipeline is
  approximately N_f × A_stage, where A_stage is the area required for one fold's
  operations and registers.
- The temporal density in the pipeline region is approximately N_f × TD_stage, where
  TD_stage is the density of one fold's operations. This aggregate density must not
  exceed RWDL for the pipeline's die region.
- DGR rules apply at the boundaries between pipeline stages: the density transition
  between adjacent stages must not exceed ΔTD_max.

### 4.4 Zone-Distributed Folding

**Zone-Distributed Folding** applies when a computation is too large to fit within a
single SCR zone's area or coherence budget, and must be partitioned across multiple
zones. Operations assigned to different zones operate under different SCR clocks;
dependencies that cross zone boundaries incur the inter-zone handoff latency L_handoff
measured in Zone B coherence cycles.

Zone-distributed folding introduces a new constraint dimension: in addition to fitting
each fold within its zone's N_usable and B_cycle, the inter-zone dependencies must
be structured so that the L_handoff overhead is absorbed into the fold boundary
latency without creating timing violations on the dependent path.

The design rule for zone-distributed folding is:

- Operations that depend on cross-zone predecessors must be assigned to folds at least
  L_handoff coherence cycles after the fold containing the predecessor
- The dependency structure should minimize the number of distinct zone crossings on
  the critical causal path; each crossing adds L_handoff to the total computation
  latency

Zone boundary placement in the floorplan should align with natural fold boundaries in
the dependency graph — not cutting through the interior of a fold where possible
(§9.3).

---

## 5. Causal Depth and Fold Depth Analysis

### 5.1 Definitions

**Causal depth** of an operation o in the dependency graph is the length of the
longest directed path from any source operation (an operation with no predecessors)
to o, measured in operations:

```
causal_depth(o) = 0                              if o has no predecessors
causal_depth(o) = 1 + max( causal_depth(p) )    for all predecessors p of o
```

The **critical causal path (CCP)** is the path through the dependency graph with the
maximum causal depth. Its length, D_crit, determines the minimum number of
coherence cycles required to complete the computation:

```
N_f_min = ceil( D_crit / D_fold_max )
```

Where D_fold_max is the maximum usable depth per fold, defined in §5.2.

**Fold depth** of a specific fold F is the number of distinct causal levels present
within F — the difference between the maximum and minimum causal depth of operations
assigned to F:

```
fold_depth(F) = max( causal_depth(o) for o in F )
              − min( causal_depth(o) for o in F )
              + 1
```

Fold depth must not exceed D_fold_max for any fold.

### 5.2 Fold Depth Limit

The maximum achievable fold depth in a single coherence cycle is:

```
D_fold_max = N_usable − N_tr_write

Where:
  N_usable   = N_slots − 2    (usable slots; excludes reserved slots 0 and N_slots−1)
  N_tr_write = number of temporal register write operations in this fold
               (each TR write occupies one slot at the end of the cycle)
```

TR write operations are assigned to the latest available slots within the cycle,
preserving the maximum contiguous slot range for computation operations. Similarly,
TR read operations in the receiving fold are assigned to the earliest available slots,
ensuring computed inputs are available to the fold's computation operations as early
as possible.

For a fold with no TR writes (the last fold in a chain, or a single-cycle fold),
D_fold_max = N_usable.

For a fold with k TR writes:

```
D_fold_max = N_usable − k
```

This creates a design tension: a fold with a large cutset (many results that must
cross the boundary) consumes slot capacity for TR writes, reducing the depth available
for computation. Minimizing cutset size is therefore an objective of fold boundary
placement (§7.3).

### 5.3 The Depth-Width Trade-off

For a fold with fold depth D, the maximum number of operations is constrained by:

```
W_fold_max = D × N_slot_max

Where:
  D           = fold depth (causal levels within this fold)
  N_slot_max  = maximum operations per slot (from TSPS)
  W_fold_max  = maximum total operation count for this fold
```

This expression assumes that each of the D causal levels fills its slot to capacity.
In practice, W_fold ≤ W_fold_max because:

- Not all causal levels have enough independent operations to fill a full slot
- RWDL limits the spatial density and therefore the number of parallel operations
  that can be committed in the die region assigned to the fold

The depth-width trade-off is fundamental: a fold with high D (deep, sequential) has
fewer remaining slots for parallel operations at each level. A fold with low D
(shallow, parallel) can pack more independent operations across many slots but
completes less sequential computation per cycle.

| Fold Style | D_fold | W_fold | Use When |
|---|---|---|---|
| Deep-sequential | High (≈ N_usable) | Low (1 per slot) | Long causal chains dominate; parallelism is limited |
| Balanced | Moderate | Moderate | Mixed causal depth; general use |
| Wide-parallel | Low (1–4) | High (≈ B_cycle) | Independent operations dominate; throughput prioritized over latency |
| TR-heavy | Reduced by N_tr_write | Limited | Large cutsets force slot dedication to TR operations |

### 5.4 Critical Causal Path Reduction

When D_crit exceeds N_usable × N_f for a target N_f, the critical causal path must
be shortened. Reduction techniques in priority order:

**1. Operation fusion:** Combine two causally adjacent operations into a single
operation that implements their composed function. This reduces D_crit by 1 per
fusion, at the cost of requiring a substrate site that can implement the composed
function within Δτ_eff. Not all operations can be fused; fusion is valid only when
the composed function can be expressed as a single address commit.

**2. Temporal retiming:** Move an operation from a depth-critical fold to an adjacent
fold, adjusting which operations cross the fold boundary. This does not reduce D_crit
globally but balances D_fold across folds, potentially allowing N_f to decrease if
the imbalance was the bottleneck (§10.2).

**3. Algorithm substitution:** Replace the high-causal-depth algorithm with an
alternate algorithm for the same function that has lower causal depth. Classic
examples in classical design include carry-lookahead vs. ripple-carry addition;
temporal manufacturing has analogous depth-reducing algorithmic choices specific to
the temporal domain.

**4. Zone distribution:** Assign parts of the critical path to different SCR zones,
accepting L_handoff overhead per zone crossing in exchange for access to each zone's
independent N_usable. This only helps if the L_handoff overhead is less than the
additional cycles required by the depth without zone distribution.

---

## 6. Temporal Register Architecture

### 6.1 Definition and Physical Basis

A **Temporal Register (TR)** is a designated substrate site whose committed temporal
address state is read by a subsequent fold as an input to that fold's operations.
Unlike a classical register — a storage element actively driven and held by a feedback
circuit — a temporal register is passive: once a temporal address is committed to the
site, the substrate material holds the phase state until it is read by the next fold
or until it is explicitly refreshed.

The physical basis for temporal register function is the same substrate property that
enables temporal addressing in general: the committed phase state of the substrate
material at a given site persists for a finite time before relaxing toward a lower-
energy state. This relaxation is characterized by the material's relaxation time
constant τ_relax, which was introduced in the TCT Protocol as a parameter of the
time-since-injection correction. For temporal register applications, τ_relax sets the
**Temporal State Horizon** — the maximum time over which a TR can reliably hold its
committed state.

### 6.2 Temporal State Horizon

The **Temporal State Horizon (TSH)** is the maximum number of coherence cycles over
which a TR site's committed address can be read back at an error rate below the
design's discrimination threshold:

```
TSH = floor( τ_relax × ln( Δτ_eff / (2 × δ_readback_max) ) / T_c )

Where:
  τ_relax        = material relaxation time constant (ns; from TCT material record)
  Δτ_eff         = effective address spacing for the substrate SC class (addr. units)
  δ_readback_max = maximum acceptable readback error (addr. units; typically Δτ_eff/4)
  T_c            = coherence cycle period (ns; from CBT)
  TSH            = temporal state horizon (coherence cycles; integer, rounded down)
```

The TSH sets an architectural constraint: a TR site that holds a value across more
than TSH coherence cycles will accumulate sufficient relaxation error that its
readback may fall outside the discrimination window, producing a logical error in the
dependent fold.

Designs in which a TR must hold its state across more than TSH cycles MUST refresh
the TR (§6.4). Failure to refresh a TR within its TSH is a design error that will
cause intermittent logical failures that are temperature-dependent and difficult to
diagnose post-fabrication.

For typical SC-I substrates at process-qualified temperatures, TSH is in the range of
8–32 coherence cycles depending on T_c and τ_relax. Design tools MUST compute TSH
from measured material parameters and enforce it as a constraint on inter-fold
temporal register lifetimes.

### 6.3 Register File Organization

A collection of TR sites allocated for a fold boundary is called a **Temporal
Register File (TRF)**. The TRF for a given fold boundary has a size equal to the
cutset cardinality — the number of operations whose results must cross that boundary.

TRF sites are allocated in a dedicated substrate region called the **TRF region**,
placed adjacent to the fold region it serves (§9.2). The TRF region requires:

- SC-I substrate qualification for maximum state horizon
- Isolation from high-density computation regions to prevent temporal crosstalk
  (§8 of the PDK Specification) from perturbing TR address states
- Sufficient address spacing between adjacent TR sites (≥ Δτ_eff) to prevent
  inter-site interactions from degrading readback accuracy

**TR site layout within the TRF region:**

TR sites are assigned addresses from a designated subrange of the address space that
does not overlap with the computation operations in either the writing fold or the
reading fold. This subrange is called the **TR address reserve**. Its width must
accommodate all cutset address pairs with Δτ_eff spacing between adjacent pairs:

```
TR_address_reserve_width = N_cutset × Δτ_eff × (1 + margin_fraction)

Where:
  N_cutset        = number of TR sites at this fold boundary
  Δτ_eff          = effective minimum address spacing
  margin_fraction = address spacing margin (recommended 0.20)
```

### 6.4 Temporal Register Refresh

When a computation requires a TR to hold state for more than TSH coherence cycles,
the TR must be **refreshed** — its committed address state re-committed before
relaxation degrades it below the discrimination threshold.

A refresh operation is itself a temporal operation: the Commit Arbiter re-authorizes
a commit of the same address to the same substrate site. The refresh operation:

- Must be assigned to a coherence slot within TSH cycles of the prior commit or
  prior refresh
- Counts against the coherence budget of the cycle in which it is performed
- Consumes the TR site's slot capacity for that cycle, preventing any other operation
  from being committed to the same site in the same cycle

Refresh operations are overhead — they consume coherence budget without contributing
to computation. Designs that require TR sites to hold state across many cycles
accumulate significant refresh overhead. The **refresh overhead fraction** for a TR
site held across N_hold cycles is:

```
f_refresh = ceil( N_hold / TSH ) / N_hold
```

For N_hold >> TSH, f_refresh approaches 1/TSH — one refresh operation per TSH cycles
per TR site. Designs with large TRFs held across many cycles should evaluate whether
architectural restructuring (reducing N_hold or restructuring the fold chain to reduce
hold time) is more efficient than accepting the refresh overhead.

---

## 7. Inter-Fold Communication

### 7.1 The Role of Inter-Fold Communication

Operations in fold F+1 that depend on results from fold F receive their inputs by
reading the committed address states of the relevant TR sites. This reading is the
inter-fold communication step. From the Commit Arbiter's perspective, it is
implemented as an ordinary temporal operation: the reading operation has the TR site
as a predecessor, and the CA will not authorize the reading operation until the TR
commit in fold F has been acknowledged.

The CA's handling of this dependency is automatic, provided the dependency is declared
in the operation graph. The architectural concern is not whether the dependency is
honored — the CA guarantees that — but whether the dependency induces scheduling
constraints that degrade performance.

### 7.2 Intra-Zone Inter-Fold Handoff

When the writing fold and the reading fold are in the same SCR zone, the inter-fold
communication incurs two slot costs:

- **TR write slot (fold F):** The TR commit operation occupies one slot in fold F,
  typically one of the last usable slots before the cycle boundary
- **TR read slot (fold F+1):** The TR read operation (the first computation operation
  in fold F+1 that uses the TR value) must be in a slot after the TR commit has been
  acknowledged. Since the TR commit was in the prior cycle, the read can be in any
  slot of fold F+1, beginning with slot 1

Intra-zone inter-fold handoff therefore imposes no additional cycle latency beyond
the fold boundary itself: fold F completes in cycle c, fold F+1 reads the TR and
proceeds in cycle c+1. The one-cycle gap is the inherent cost of any fold boundary.

### 7.3 Cross-Zone Inter-Fold Handoff

When the writing fold is in Zone A and the reading fold is in Zone B, the handoff
passes through the ZBI protocol. The reading fold in Zone B cannot be authorized
until L_handoff Zone B coherence cycles after the TR commit in Zone A.

This creates an **inter-fold dead time**: the reading fold cannot begin in the cycle
immediately following the writing fold. It must wait L_handoff additional cycles,
during which the substrate sites in Zone B that would serve the reading fold are idle.

For a design with a cross-zone fold boundary, the minimum fold-to-fold latency is:

```
L_FF_cross = 1 + L_handoff   (in Zone B coherence cycles)

Where:
  1          = the inherent one-cycle fold boundary overhead
  L_handoff  = ZBI handoff latency in Zone B cycles (from CBT cross-zone section)
```

The dead time L_handoff is non-recoverable by temporal retiming: it is a physical
property of the SCR infrastructure, not a design parameter. Designs with cross-zone
fold chains must budget this latency on every cross-zone fold boundary in their
critical causal path.

Strategies for managing cross-zone dead time:

- **Fill the dead time:** Assign operations from independent parallel computations to
  the dead cycles in Zone B. If other computations are available that do not depend
  on the Zone A result, their Zone B folds can proceed during the dead cycles,
  effectively hiding the inter-zone latency behind useful work.

- **Minimize cross-zone boundaries on the critical path:** Restructure the fold
  assignment so that the longest sequential dependency chains are confined within a
  single zone, with cross-zone crossings on off-critical-path dependencies where the
  dead-time cost does not affect total latency.

- **Accept the latency:** For computations where cross-zone partitioning is necessary
  and parallelism cannot fill the dead time, the L_handoff overhead is a fundamental
  latency floor that the architecture must accommodate.

### 7.4 Cutset Minimization

The fold cutset is the set of operations whose results must cross a fold boundary via
TR sites. A larger cutset consumes more:

- TR write slots at the end of fold F (reducing D_fold_max by N_tr_write)
- TR read slots at the beginning of fold F+1 (consuming early slots in the next fold)
- TRF region substrate area
- Coherence budget (each TR write and read is a temporal operation charged against
  B_cycle)

Cutset minimization is therefore a first-order optimization objective for fold
boundary placement. The problem is equivalent to a minimum cut problem on the
dependency graph, weighted by the coherence-budget cost of each cut edge.

Practical cutset minimization approaches:

**Topological clustering:** Group operations with high mutual dependency density into
the same fold. Operations with many intra-cluster edges and few inter-cluster edges
produce smaller cutsets when the cluster forms one side of a fold boundary.

**Causal level alignment:** Align fold boundaries with natural causal level boundaries
in the dependency graph. A fold boundary that cuts across a causal level creates more
cut edges than a boundary that coincides with the boundary between two causal levels.

**TR address reuse:** When the same TR value must be read by multiple operations in
fold F+1, those reads can share a single TR site if they all reference the same
committed address. Deduplicating shared TR reads reduces the cutset cardinality even
when the number of distinct logical values crossing the boundary remains the same.

---

## 8. Folding Efficiency

### 8.1 Metric Definition

**Folding efficiency** (η_fold) measures the fraction of total slot capacity consumed
by computation operations, as opposed to overhead operations (TR writes, TR reads,
refresh operations):

```
η_fold = N_compute / ( N_compute + N_overhead )

Where:
  N_compute  = total computation operations across all folds
  N_overhead = total overhead operations: TR writes + TR reads + refresh operations
  η_fold     ∈ (0, 1]; perfect efficiency is 1.0 (no overhead)
```

Perfect efficiency is unachievable in any multi-fold design because fold boundaries
require at least one TR write per cutset element. For single-cycle folding with no
cutset, η_fold = 1.0.

### 8.2 Overhead Sources

Each overhead source contributes a predictable cost:

**TR write overhead:** Each fold boundary with cutset cardinality k_c contributes
k_c TR write operations to the writing fold. For a chain of N_f folds with cutset
sizes k_1, k_2, ..., k_{N_f−1}:

```
N_TR_writes = sum( k_i for i = 1 to N_f − 1 )
```

**TR read overhead:** Each fold boundary contributes the same number of TR read
operations to the reading fold. In the simplest architecture, TR reads are distinct
operations from the computation operations that use the TR values, adding one
operation per TR site per fold boundary on the reading side:

```
N_TR_reads = N_TR_writes   (symmetric; each write produces one read)
```

Some architectures allow TR read-and-compute fusion, where the first computation
operation of a fold directly reads from the TR site as part of its commit. This
eliminates the explicit TR read operation, but is only valid when the TRS L3
resolution layer can apply the apodization envelope directly at the TR site location.
When available, fusion reduces N_TR_reads to zero and improves η_fold.

**Refresh overhead:** Each TR site that must be held across more than TSH cycles
requires ceil(N_hold / TSH) − 1 refresh operations over its lifetime. Refresh
overhead grows linearly with hold time and inversely with TSH.

### 8.3 Efficiency Targets by Architecture Type

The following ranges represent achievable efficiency targets under well-optimized
fold boundary placement. Designs below the lower bound are candidates for
architectural restructuring; designs above the upper bound typically benefit from
using the excess capacity for additional computation rather than leaving it idle.

| Architecture Type | Typical η_fold Range | Notes |
|---|---|---|
| Single-cycle folding | 1.00 | No boundaries, no overhead |
| Multi-cycle (2–4 folds) | 0.85 – 0.95 | Low boundary count; cutset minimization effective |
| Multi-cycle (5–12 folds) | 0.72 – 0.88 | Boundary overhead accumulates; retiming critical |
| Pipeline folding | 0.70 – 0.90 | Depends on stage count and cutset sizes |
| Zone-distributed folding | 0.60 – 0.82 | Dead-time cycles reduce useful work unless filled |
| TR-refresh-heavy designs | 0.50 – 0.72 | Long hold times dominate; consider architectural restructuring |

Designs with η_fold below 0.60 should be reviewed for architectural alternatives
before proceeding to physical design.

---

## 9. Floorplanning for Logic Folding

### 9.1 Fold Region Partitioning

The die is partitioned into **fold regions** — spatial areas within which the
operations of a given fold (or a group of folds, in a pipeline architecture) are
placed. Fold region boundaries are design choices, subject to constraints from the
SCR zone map, the density gradient rules (DGR), and the RWDL spatial map.

**Fold region sizing:**

A fold region must be large enough to accommodate all operations in the fold at a
density no greater than RWDL for the region's SC class:

```
A_fold_min = N_ops_fold / ( RWDL × η_density )

Where:
  N_ops_fold  = total operations (including overhead) in this fold
  RWDL        = Registration-Weighted Density Limit for the region (from PDK SC maps)
  η_density   = target density utilization fraction (recommended 0.80 to maintain
                DDA margin per PDK Specification §9.3)
  A_fold_min  = minimum fold region area (mm²)
```

**Fold region adjacency:**

Operations in adjacent folds frequently exchange values through TRFs. The TRF region
for a fold boundary should be physically adjacent to both the writing fold region and
the reading fold region to minimize the spatial distance between TR writes and TR
reads. This reduces the TGI proximity rule exposure (TPR rules apply based on the
spatial position of operations relative to z_c) and simplifies the address map in the
TRS intent generator.

**Fold region shape:**

Rectangular fold regions are preferred. Irregular shapes complicate density gradient
management at the boundaries: DGR-001 requires that density changes monotonically
across transition zones, and an irregular boundary makes the transition zone geometry
difficult to characterize and verify.

### 9.2 Temporal Register File Placement

The TRF region for each fold boundary is placed in the spatial interval between the
writing fold region and the reading fold region. Placement constraints:

**Isolation requirement:** The TRF region must be separated from the computation
regions of both adjacent folds by a minimum spatial margin of r_int (the interaction
radius from the PDK TSPS). This prevents temporal crosstalk from computation
operations perturbing the TR site address states.

**SC class requirement:** TRF regions must be placed in SC-I substrate zones. SC-II
substrate has a shorter TSH (due to lower SC rating and correspondingly larger address
relaxation per unit time), which reduces the hold time available before refresh is
required. Locating TRF regions in SC-I zones maximizes TSH and minimizes refresh
overhead.

**Address reserve non-overlap:** The TR address reserve (§6.3) must not overlap with
the address ranges used by computation operations in either adjacent fold region.
Address range assignments must be planned at the architectural level and verified by
the TRS intent map generator before the TRF region layout is finalized.

**Density accounting:** TRF operations (TR writes, TR reads, refreshes) contribute
to the temporal density of the TRF region. The TRF region density must be checked
against RWDL for that region, and DGR rules must be satisfied at the boundaries
between the TRF region and adjacent computation regions.

### 9.3 Zone Boundary Alignment

When a design uses zone-distributed folding, the physical boundaries between SCR
zones should align with fold boundaries in the operation graph wherever possible.
Misalignment — where a fold boundary lies in the interior of an SCR zone, and a zone
boundary lies in the interior of a fold — creates operational complexity:

- Operations within the misaligned fold that are assigned to different zones must use
  the ZBI handoff protocol even though they are intended to be within the same fold
- The L_handoff overhead for these within-fold cross-zone operations counts against
  D_fold_max, reducing the depth available for computation

The alignment rule is: **a fold boundary should cross a zone boundary; a zone boundary
should not cross a fold boundary.**

When the physical zone boundary — fixed by SCR infrastructure that cannot be changed
post-commissioning — does not align naturally with the desired fold boundary, one of
two accommodations is required:

1. **Adjust the fold boundary** to align with the zone boundary, accepting that the
   fold depth on one side of the zone boundary may be unbalanced relative to the other
   side. Temporal retiming (§10.2) can address the imbalance.

2. **Accept intra-fold cross-zone overhead** and budget the L_handoff cost against the
   fold's effective depth. This is a fallback that degrades performance and should be
   avoided in designs where cross-zone latency is on the critical causal path.

### 9.4 Density Gradient Management

The DGR rules (from the PDK TDR) constrain the density change between adjacent
500 μm × 500 μm regions. In a floorplan with multiple fold regions at different
densities — which is typical, since fold regions near the critical causal path tend
to be higher density than surrounding regions — the DGR transition zones must be
explicitly planned.

**Density profile planning:**

Before finalizing fold region boundaries, produce a die-level density profile that
maps the intended temporal density at each 500 μm × 500 μm grid point. Verify that
adjacent grid points satisfy DGR-001. For density steps that exceed ΔTD_max, insert
the required transition zone width per DGR-002.

**Transition zone assignment:**

Transition zones are regions where temporal density changes monotonically from the
high-density fold region to the lower-density surrounding area. They consume die area
without contributing operations to the computation. The area cost of transition zones
should be included in the fold region sizing analysis (§9.1); a fold region surrounded
by large density gradients requires more transition zone area, effectively reducing
the net usable area for computation.

**Cross-zone density matching:**

At SCR zone boundaries, the DGR rule applies across the boundary as well as within
each zone. If fold regions on opposite sides of a zone boundary have substantially
different densities, the transition zone must span the zone boundary — introducing
additional DGR-verified area that belongs to neither fold region's computation.

---

## 10. Timing Closure for Folded Logic

### 10.1 The Folded Timing Model

Timing closure for folded logic operates on two levels simultaneously:

**Intra-fold timing:** Within each fold, operations must be assigned to coherence slots
such that no operation is in a slot earlier than any of its predecessors within the
same fold. The TTF-aware STA tool enforces this using the CSA arc (commit sequencing
overhead per operation) and the APA arc (arbiter processing latency at the slot
boundary). The effective timing budget per causal level within a fold is:

```
T_causal_level = T_slot − T_arb − T_seq_max

Where:
  T_slot     = T_c / N_slots  (duration of one coherence slot)
  T_arb      = arbiter processing latency (from APA arc)
  T_seq_max  = maximum commit sequencing latency (from CSA arc, worst case)
```

If T_causal_level > 0, the intra-fold timing is feasible. If T_causal_level ≤ 0,
the combination of T_c, N_slots, T_arb, and T_seq are physically incompatible; the
process cannot support any multi-level fold at all. This is a process-level constraint
and cannot be addressed by design changes.

**Inter-fold timing:** Across fold boundaries, the timing budget is the coherence
cycle period T_c (for intra-zone boundaries) or (1 + L_handoff) × T_c_B (for cross-
zone boundaries, where T_c_B is Zone B's coherence cycle period). The inter-fold
budget must accommodate the TR write time (within fold F's last slot), the cycle
boundary overhead, and the TR read time (within fold F+1's first slot).

The TTF-aware STA tool models inter-fold timing using ZBA arcs (for cross-zone
boundaries) and implicit cycle boundaries (for intra-zone boundaries, represented as
a one-cycle gap between the TR write slot in fold F and the first available slot in
fold F+1).

### 10.2 Temporal Retiming

**Temporal retiming** is the process of moving one or more operations from one fold
to an adjacent fold, adjusting the fold boundary so that the causal depth is more
evenly distributed across the fold chain. It is analogous to classical retiming in
that its goal is to balance the utilization of each "stage" (fold), but the mechanics
are different because:

- Operations cannot cross fold boundaries freely; they must carry their predecessor
  results with them, requiring either new TR sites or adjustment of existing TR
  assignments
- Moving an operation from fold F to fold F−1 requires that all of the moved
  operation's predecessors are already in fold F−1 or earlier; otherwise, the move
  creates a dependency violation
- Moving an operation from fold F to fold F+1 increases the cutset of the F/F+1
  boundary if the moved operation has successors in fold F+1 that depend on operations
  remaining in fold F

**Retiming procedure:**

1. Compute the fold depth D_fold(F) for each fold F in the chain.
2. Identify the fold with maximum D_fold (the bottleneck fold) and the fold with
   minimum D_fold (the slack fold).
3. Identify candidate operations for migration: operations in the bottleneck fold
   whose predecessors are all in fold F−1 or earlier (can move earlier) or whose
   successors are all in fold F+1 or later (can move later).
4. Evaluate the cutset impact of each candidate move. Prefer moves that do not
   increase any fold boundary's cutset cardinality.
5. Apply the move that most reduces max(D_fold) without increasing the cutset beyond
   D_fold_max for the receiving fold.
6. Repeat until D_fold is balanced or no further beneficial moves are available.

**R-RETIME-01:** Temporal retiming MUST preserve the topological order of the
dependency graph. An operation may be moved to a different fold only if, after the
move, every predecessor of the moved operation remains in an equal or earlier fold and
every successor remains in an equal or later fold.

### 10.3 Fold Schedule Optimization

The **fold schedule** is the complete assignment of operations to coherence cycles
and coherence slots. It is the temporal analog of a placed and routed netlist: it
specifies not only which fold an operation belongs to but exactly which slot within
that fold it occupies.

Fold schedule optimization targets three objectives in priority order:

1. **Feasibility:** Every operation must be in a slot later than all of its
   predecessors within the same fold. No slot may exceed N_slot_max. No fold may
   exceed D_fold_max. All CSR rules must be satisfied.

2. **Efficiency:** Minimize the total number of coherence cycles required to complete
   the computation (minimize N_f). Subject to that, minimize TR overhead.

3. **Timing margin:** Maximize the minimum slack across all timing paths, as computed
   by the TTF-aware STA tool. A schedule with positive minimum slack at all paths
   provides robustness against process variation in T_c, T_arb, and T_seq.

A legal fold schedule satisfying objective 1 can always be constructed by a
topological sort of the dependency graph, assigning operations to slots in topological
order and breaking to a new fold when a slot constraint is violated. This greedy
algorithm is a valid starting point; objectives 2 and 3 require iterative refinement.

### 10.4 TTF Arc Consumption in Folded Designs

The TTF-aware STA tool consumes five arc types when analyzing a folded design. Their
interaction in the context of logic folding is summarized:

| Arc Type | Where Applied | Folding-Specific Interaction |
|---|---|---|
| APA | Every temporal operation | Constant overhead per slot boundary; sets T_causal_level floor |
| CSA | Every temporal operation | T_seq_max applies when an operation is deferred; pessimistic bound on intra-fold timing |
| ZBA | Every cross-zone fold boundary | Adds L_handoff cycles to inter-fold latency on affected paths |
| TCA | Operations in die regions with non-zero TAOE_sys | Spatially offset address assignments; may push operations closer to address spacing limits |
| DDA | Operations in high-density fold regions | Reduces timing margin as TD_design approaches RWDL; most severe in pipeline folding |

DDA arcs warrant particular attention in pipeline folding, where multiple fold stages
operate simultaneously in the same die region at aggregate density N_stages × TD_stage.
If the aggregate density approaches RWDL, the DDA multiplier rises to 3.0 (Near-limit
tier per PDK §8.3), and the resulting margin reduction may require either reducing
pipeline depth or distributing pipeline stages across a larger die region.

---

## 11. Verification Methodology

### 11.1 Fold-Level Functional Verification

Functional verification of folded logic is performed fold by fold, then end-to-end.
The fold-level verification strategy:

**Per-fold verification:** For each fold F, apply a set of input address states at the
TR read sites (the inputs from fold F−1) and verify that the committed output address
states at the TR write sites (the outputs to fold F+1) correctly implement the fold's
intended function under the address-value mapping convention.

Per-fold verification can be performed on simulation models before fabrication and on
physical substrate samples after fabrication using the TMU (Temporal Metrology Unit)
for post-commit address readback.

**End-to-end verification:** Apply a set of primary input address states at the source
operations of the full dependency graph and verify that the final output address states
(at the sink operations of the last fold) correctly implement the intended end-to-end
function.

End-to-end verification is more expensive than per-fold verification because it
requires running all folds in sequence with the correct inter-fold TR state threading.
However, it is the only verification mode that can detect errors arising from
incorrect inter-fold state threading — errors that per-fold verification misses.

Both modes are required before tape-out sign-off.

### 11.2 Fold Boundary Assertion Checks

Formal assertions on fold boundary behavior detect structural errors in the fold
assignment that functional simulation may not exercise:

**Assertion FB-01 — TR write completeness:** For every fold boundary, every operation
in the cutset has a corresponding TR write operation in the writing fold. A cutset
operation without a TR write means its result is not preserved across the boundary,
and the reading fold will receive a stale or undefined value.

**Assertion FB-02 — TR read coverage:** For every fold boundary, every TR read
operation in the reading fold references a TR site that was written in the writing fold
or an earlier fold (within TSH cycles). A TR read referencing an unwritten site or a
site whose write is older than TSH cycles is a design error.

**Assertion FB-03 — Cutset minimality:** The cutset at each fold boundary contains
only operations whose results are actually consumed by a later fold. Operations in the
cutset that are never read by any subsequent fold are dead TR writes: they consume
slots and die area without serving any purpose.

**Assertion FB-04 — No forward references within a fold:** Within fold F, no
operation is assigned to a slot ≤ any of its predecessors' slots. Violations indicate
a topological sort error in the fold schedule.

### 11.3 Temporal Register Integrity Verification

TR integrity verification confirms that TR sites maintain their committed address
states within acceptable bounds over the intervals between their write and their last
read.

**TSH compliance check:** For every TR site, compute the hold time N_hold — the
number of coherence cycles between the TR write and the last TR read that references
it. Verify N_hold ≤ TSH if no refresh is planned, or verify that refresh operations
are scheduled at intervals ≤ TSH if N_hold > TSH.

**Crosstalk margin check:** For every TR site, compute the maximum Δτ_xtalk from
adjacent high-density computation regions per the PDK crosstalk model (PDK §8.2).
Verify that the TR site's committed address remains within the discrimination window
after the worst-case crosstalk perturbation:

```
| τ_TR + Δτ_xtalk | ≤ τ_encoding_boundary − Δτ_eff / 2

Where:
  τ_TR             = the committed TR address
  Δτ_xtalk         = worst-case crosstalk perturbation (from PDK crosstalk lookup)
  τ_encoding_boundary = the address boundary between logical 0 and logical 1 encodings
  Δτ_eff           = effective address spacing
```

A TR site that fails this check will produce a logical error when read if the
crosstalk perturbation is present — a condition that is density-dependent and may
appear intermittently in production.

### 11.4 Cross-Fold Causal Consistency

Cross-fold causal consistency verification confirms that the dependency relationship
between folds is correctly implemented: no fold F+1 operation has been scheduled to
begin before its dependencies in fold F are guaranteed to be committed and readable.

This verification is largely handled by the CA's arbitration protocol, which will not
authorize a fold F+1 operation until all its predecessors are acknowledged. However,
the design-level check ensures that the operation graph does not declare any intra-
fold dependency as a cross-fold dependency (which would cause unnecessary TR overhead)
or any cross-fold dependency as an intra-fold dependency (which would produce an
impossible slot assignment that the CA cannot satisfy).

The CGV tool (from the PDK signoff flow) performs causal graph rule checks (CGR-001
through CGR-005) that include cross-fold consistency. CGV must be run on the final
folded schedule, not on the pre-folding dependency graph, to catch scheduling errors
introduced during fold boundary placement.

---

## 12. Design Patterns

The following patterns represent common, well-characterized fold structures that
recur across a range of applications. Each is described in terms of its fold
structure, applicable use cases, efficiency characteristics, and key design
considerations.

### 12.1 The Linear Fold Chain

**Structure:** A sequence of N_f folds, each with a single causal level (fold depth 1),
connected by TRFs at each boundary. All operations in each fold are independent of
each other and collectively compute one stage of a sequential process.

```
Fold 1       Fold 2       Fold 3      ...      Fold N_f
[Op1a Op1b] → [Op2a Op2b] → [Op3a Op3b] → ... → [OpNa OpNb]
     ↓              ↓              ↓
   [TR12]        [TR23]        [TR34]
```

**Use cases:** Iterative algorithms where each iteration depends on the previous
result; serial data processing pipelines; state machine sequences.

**Efficiency:** High W_fold per fold (up to N_slot_max operations per fold), low
D_fold. η_fold = N_compute / (N_compute + 2 × N_f × k_c), where k_c is the cutset
size per boundary.

**Key consideration:** The total latency is N_f coherence cycles. For long chains,
consider whether pipeline folding (§4.3) would serve the use case better.

### 12.2 The Broadcast-Collect Pattern

**Structure:** A two-fold structure in which the first fold commits a set of
independent operations from a common input, and the second fold collects their results
through a TRF to produce a combined output.

```
          Fold 1 (Broadcast)            Fold 2 (Collect)
 [Input] → [Op1a, Op1b, ..., Op1n] →  [TRF] → [Collect Op]
```

**Use cases:** One-to-many transformations where the many outputs are later
aggregated; parallel search with result consolidation; distributed evaluation of
independent conditions.

**Efficiency:** Fold 1 achieves high W_fold (wide parallel operations). Fold 2 has
low D_fold (one or few levels) but potentially high input fan-in, which must be
checked against F_in_max from the CBT (CGR-002 rule).

**Key consideration:** The collect operation in fold 2 has fan-in equal to the number
of broadcast outputs. For large broadcasts, the fan-in may exceed F_in_max, requiring
the collect to be split into a tree structure (see pattern 12.4).

### 12.3 The Folded Pipeline Stage

**Structure:** A multi-stage pipeline where each stage is a single fold of depth D_s.
New inputs arrive every coherence cycle; each cycle advances every in-flight datum by
one stage. The total in-flight datum count equals the number of pipeline stages N_p.

```
Cycle c:   [Stage 1: Datum A]  [Stage 2: Datum B]  [Stage 3: Datum C]
Cycle c+1: [Stage 1: Datum D]  [Stage 2: Datum A]  [Stage 3: Datum B]
                 ↓                     ↓
              [TR 1→2]             [TR 2→3]
```

**Use cases:** High-throughput stream processing; datapath pipelines; systolic
computation.

**Efficiency:** η_fold is high when D_s is large relative to the cutset size, since
TR overhead is amortized over a large computation per stage. The aggregate density in
the pipeline region scales with N_p; DDA derating and RWDL must be evaluated at
aggregate density.

**Key consideration:** Pipeline stage area allocation — each stage needs its own fold
region plus TRF regions at its boundaries. A pipeline with many short stages consumes
more area (more TRF regions) than one with fewer longer stages.

### 12.4 The Temporal Reduction Tree

**Structure:** A binary-tree fold structure that reduces N inputs to 1 output in
ceil(log2(N)) folds. At each level of the tree, pairs of inputs are combined by
reduction operations; the results become the inputs to the next level.

```
Fold 1: [Reduce(A,B)] [Reduce(C,D)] [Reduce(E,F)] [Reduce(G,H)]
                    ↓                            ↓
Fold 2:       [Reduce(AB,CD)]            [Reduce(EF,GH)]
                              ↓
Fold 3:                [Reduce(ABCD,EFGH)]
```

**Use cases:** Any associative reduction — sum, product, maximum, logical AND/OR —
over a set of inputs too large to fit in a single fold; replacing the Broadcast-
Collect pattern when fan-in exceeds F_in_max.

**Efficiency:** The reduction tree has ceil(log2(N)) folds and total N−1 operations,
making it highly efficient in terms of operations per fold. The TRF at each level
stores the intermediate reduction values; TRF sizes halve at each level.

**Key consideration:** Each fold level must fit within the substrate area assigned to
that level. The widest level (fold 1) has N/2 operations; each subsequent level halves.
Floorplanning must accommodate this decreasing-width structure; a tapered fold region
allocation is natural.

### 12.5 The Zone-Partitioned Parallel Fold

**Structure:** A single logical fold that is physically split across two or more SCR
zones, with independent parallel computations assigned to each zone. Operations in
different zones within the same "logical fold" are mutually independent; no cross-zone
dependency exists within the fold.

```
Zone A (Cycle c):  [Op_A1, Op_A2, ..., Op_Ak]
Zone B (Cycle c):  [Op_B1, Op_B2, ..., Op_Bm]  ← independent of Zone A ops
                         ↓                               ↓
                   [TRF_A → next fold]           [TRF_B → next fold]
```

**Use cases:** Computations that are embarrassingly parallel at the fold level and
require more substrate area than a single SCR zone provides; designs where the
coherence budget of one zone is the binding constraint rather than causal depth.

**Efficiency:** Close to single-cycle efficiency for each zone, since there are no
cross-zone dependencies within the fold. The next fold can begin in both zones
simultaneously (no L_handoff delay, since each zone's operations are independent and
each zone's TRF reads can proceed independently).

**Key consideration:** The subsequent fold that consumes results from both zones must
either be confined to a single zone (incurring L_handoff from one of the source zones)
or also split across zones (in which case the subsequent split must be consistent with
the dependency structure). This pattern is most effective when the entire computation
can be partitioned into independent sub-computations that each remain zone-local.

---

## 13. Migration from Spatial Logic

### 13.1 Conceptual Translation

The most effective entry point for a designer trained in classical spatial logic is to
build a mapping table between classical concepts and their temporal analogs. The
following is not an implementation recipe; it is a conceptual translation guide to
orient intuition.

| Classical Concept | Temporal Analog | Key Differences |
|---|---|---|
| Gate | Temporal operation | An operation is a commit, not an evaluation; its output is a committed address, not a voltage |
| Wire / signal | Causal dependency edge | No physical routing; causality is encoded in the dependency graph, not in metal connections |
| Logic level (gate stage) | Causal level | Measured in coherence slots, not in gate delays |
| Clock period | Coherence cycle period T_c | T_c is a physical property of the SCR installation, not a design parameter |
| Clock edge | Coherence slot boundary | Multiple slot boundaries per coherence cycle |
| Flip-flop / register | Temporal Register (TR) | A TR holds state passively; it decays (τ_relax) and must be refreshed if held too long |
| Pipeline stage | Logic Fold | Bounded by coherence cycle boundaries rather than register-to-register timing paths |
| Critical path | Critical Causal Path | Measured in coherence slots (causal depth), not in propagation delay |
| Setup time | T_auth window | The CA must assert authorization within T_auth before the slot boundary |
| Hold time | δ_readback_max | The minimum address separation between a committed state and an adjacent state |
| Timing closure | Fold schedule optimization + TTF STA | Two-level: intra-fold (slot assignment) and inter-fold (cycle assignment) |
| Design rule check | TDRC (Temporal DRC) + classical DRC | TDRC operates on the address space; classical DRC operates on spatial geometry |
| Synthesis | Fold decomposition + address assignment | Produces an operation dependency graph, not a gate netlist |
| Place and route | Fold region floorplan + operation placement | Assigns operations to substrate sites; TRF region placement is the routing analog |

### 13.2 Mapping Classical Constructs

**Combinational logic:** A combinational function with no feedback maps naturally to a
single fold (if its causal depth ≤ D_fold_max) or a multi-fold chain (if deeper). The
absence of feedback means the dependency graph is guaranteed to be a DAG — no
structural cycles.

**Sequential logic (flip-flop-based state machines):** The state elements (flip-flops)
map to Temporal Registers. The combinational next-state logic between registers maps
to the fold between TR reads and TR writes. Each clock cycle of the sequential machine
corresponds to one coherence cycle of the temporal design. The state width (number of
flip-flops) maps to the TRF size at the fold boundary.

**Memory arrays:** Classical memory — addressed read/write structures — has a more
complex temporal analog. Addressed reads in the temporal domain require an operation
that maps an address index to the corresponding TR site's committed state. This is a
fan-in operation (reading from one of N_words TR sites based on an index) that may
require the Temporal Reduction Tree pattern (§12.4) or dedicated address decode logic
expressed in temporal operations.

**Clocked interfaces between modules:** Handshake interfaces between classical
synchronous modules — ready/valid, request/acknowledge — translate to fold boundary
synchronization: the ready signal of the receiving module corresponds to an available
slot in the receiving fold; the valid signal corresponds to a committed TR write in the
sending fold.

### 13.3 What Does Not Translate

Several classical design idioms do not have temporal analogs and must be replaced by
alternative approaches:

**Asynchronous logic:** Classical asynchronous circuits — where computation speed is
governed by individual gate delays rather than a global clock — do not map to temporal
manufacturing. The coherence cycle is a global synchronization boundary; there is no
mechanism for an operation to complete "as fast as its inputs allow" independent of
the slot structure.

**Feedback combinational paths (latches and level-sensitive elements):** Classical
level-sensitive storage requires a feedback path that holds the current value while
the enable is asserted. In the temporal domain, feedback within a fold would require
an operation to depend on the result of a later operation in the same fold — a causal
cycle, which is prohibited by CGR-001. Level-sensitive storage must be restructured
as edge-triggered (fold-boundary-aligned) TR-based storage before a temporal implementation is possible.

**Tri-state buses:** Classical tri-state buses allow multiple drivers to share a common
wire, with at most one driver active at a time. Temporal manufacturing has no analog
for a shared substrate site with multiple conditional writers: a commit operation is
irreversible, and two operations cannot conditionally share a single substrate site
based on runtime enable signals. Multi-driver bus structures must be restructured as
multiplexed fold patterns — each potential driver commits to its own dedicated TR site,
and a selector fold reads the appropriate TR site based on the control condition.

**Glitch-tolerant hazard filtering:** Classical combinational glitch filtering exploits
the fact that glitches are transient voltage excursions that settle before the next
clock edge. In temporal manufacturing there are no transient excursions: a commit is
permanent within the coherence cycle. An incorrect intermediate address committed to a
substrate site cannot be overwritten within the same cycle — it is a defect, not a
glitch. Temporal design therefore requires that no spurious intermediate commits occur
on any path that produces an output read by a subsequent fold. The dependency graph
must be structured so that all committed operations represent valid, intentional
states.

**Clock gating:** Classical clock gating disables the clock to a register when its
value will not change, saving switching energy. In temporal manufacturing, a TR site
that is not written in a given cycle simply retains its prior committed state. There
is no "gating" concept: if no commit is issued to a TR site in a cycle, no energy is
expended and no state change occurs. Clock gating is therefore not a technique that
requires migration — its energy-saving intent is achieved automatically by the passive
hold behavior of TR sites. The designer's responsibility is to track hold time against
TSH and schedule refreshes as needed (§6.4), which is the temporal equivalent of
managing clock gating enable windows.

**Race conditions and metastability:** Classical metastability occurs when a flip-flop
captures a signal that is transitioning at the clock edge, producing an output that
is neither a clean logic 0 nor a clean logic 1. In temporal manufacturing, the analog
failure mode is a committed address that falls within the discrimination threshold
window Δτ_eff — close enough to an adjacent address that readback is ambiguous. Unlike
metastability, this is not a transient condition that resolves over time; the address
error is permanent once committed. The design-time defense is to ensure that all
address-value mappings maintain sufficient discrimination margin (≥ Δτ_eff) at all
stages of the computation, accounting for TAOE, temporal crosstalk, and TSH-related
relaxation. There is no temporal analog to a synchronizer circuit.

### 13.4 Hybrid Spatial-Temporal Architectures

Many practical designs will not be purely temporal. The process stack includes both
Tier 1 spatial layers and Tier 2 temporal layers; a design that uses both is a
**hybrid spatial-temporal architecture**. This is the expected implementation style
for the foreseeable post-ASML era, as not all functional blocks benefit equally from
temporal encoding.

#### 13.4.1 Partitioning Principles

The decision of which functional blocks belong in the spatial domain and which belong
in the temporal domain follows from the comparative advantage of each domain:

**Temporal domain advantages:**
- Very high logical density for operations that are causally ordered and address-
  encodable
- No physical routing required between causally dependent operations — dependency is
  declared, not wired
- Parallelism scales with substrate area without routing congestion

**Spatial domain advantages:**
- Lower latency for small, flat combinational functions (no coherence slot overhead)
- Well-established design methodology and tooling
- No TSH constraint — spatial state is held indefinitely by feedback circuits
- Appropriate for functions that inherently require shared-resource access patterns
  (memory controllers, arbiters, clock distribution) that do not translate to temporal
  operations

The general partitioning guideline:

| Block Characteristic | Preferred Domain |
|---|---|
| High operation count, moderate causal depth, high parallelism | Temporal |
| Low operation count, low causal depth, latency-critical | Spatial |
| Long sequential chains with simple per-step operations | Temporal (fold chain) |
| Wide combinational functions (MUX, decoder) with few levels | Spatial |
| State machines with many states and wide state encoding | Temporal (TR-based) |
| State machines with few states and narrow encoding | Spatial |
| Memory arrays (read/write) | Spatial (with temporal address decode) |
| Reduction trees over large input sets | Temporal |
| Fixed-function arithmetic with known, shallow depth | Spatial |

#### 13.4.2 The Spatial-Temporal Interface

The interface between a spatial block and a temporal block requires translation between
the two state representations: spatial logic operates on voltage levels; temporal
logic operates on committed addresses. This translation occurs at the
**spatial-temporal boundary (STB)**, which is a specialized interface structure.

At the STB, a **boundary commit unit (BCU)** receives a voltage-level signal from the
spatial block and commits the corresponding temporal address to a designated substrate
site, effectively writing a TR that the temporal block reads as its input. In the
reverse direction, a **boundary readback unit (BRU)** reads a committed address from a
temporal output TR site and presents the corresponding voltage-level signal to the
spatial block.

The STB introduces latency in both directions:
- **Spatial-to-temporal latency:** BCU commit latency (approximately T_arb + T_seq)
  plus the time to the next coherence slot boundary at which the temporal block can
  read the committed address
- **Temporal-to-spatial latency:** BRU readback latency (approximately one ARS
  readback cycle, which is process-specific) plus the propagation delay of the
  voltage-level output in the spatial domain

STB latency must be budgeted in the design's timing model. The TTF arc library does
not contain STB-specific arcs; STB timing is characterized separately during the
mixed-domain design qualification and modeled as user-defined constraints in the STA
tool.

#### 13.4.3 Power Domain Considerations

Spatial and temporal domains have different power consumption profiles:

**Spatial blocks** consume dynamic power proportional to switching activity and static
power proportional to leakage. Power management techniques (clock gating, power
gating, voltage scaling) apply normally within spatial blocks and are unaffected by
the presence of adjacent temporal blocks.

**Temporal blocks** consume power in two modes:
- **Commit power:** Proportional to the number of commit operations per cycle and the
  energy per commit (process-specific). Commit power is bursty — concentrated in the
  commit windows of each coherence slot — and must be managed with burst-current
  power delivery (as noted in the PDK Specification §2.3).
- **Refresh power:** Proportional to the number of TR refreshes per cycle. Refresh
  power is lower than commit power per operation but can be significant for designs
  with large TRFs and long hold times.

Power estimation for hybrid designs must account for both profiles. Classical power
analysis tools that model only switching-activity-based dynamic power will
underestimate temporal block power if they do not include commit and refresh energy
in their models.

#### 13.4.4 Verification of Hybrid Designs

Hybrid spatial-temporal designs introduce verification challenges that are absent from
purely temporal or purely spatial designs:

**Interface protocol verification:** The BCU and BRU must be verified to correctly
implement the spatial-temporal translation under all combinations of spatial signal
arrival time and coherence slot timing. Setup and hold checks at the STB must account
for the coherence slot structure.

**Cross-domain causal consistency:** The CGV tool checks causal consistency within the
temporal domain. It does not model the spatial domain. Dependencies that pass through
the STB — where a spatial block's output drives a temporal block's input — must be
manually declared as external constraints in the temporal operation graph. Missing STB
dependency declarations will cause the CGV tool to treat the temporal input as a free
primary input, potentially authorizing temporal operations before the spatial
predecessor has settled.

**Mixed-domain functional simulation:** End-to-end simulation of a hybrid design
requires a simulation environment that models both voltage-level transitions (spatial
domain) and address commit events (temporal domain) in the same time reference.
Neither a classical RTL simulator nor a pure temporal operation graph simulator can
do this alone; a co-simulation framework is required.

---

## 14. Glossary

| Term | Definition |
|---|---|
| **APA** | Arbiter Processing Arc — TTF arc modeling CA processing latency T_arb; consumed by TTF-aware STA to establish the timing floor at each coherence slot boundary |
| **Address-value mapping** | The design-defined convention that associates a committed temporal address with a logical value; must maintain discrimination-safe spacing between encoded values |
| **B_cycle** | Total operation budget per coherence cycle per zone; equal to N_usable × N_slot_max; the maximum operation count achievable in a single fold |
| **BCU** | Boundary Commit Unit — interface structure that converts a spatial voltage-level signal to a committed temporal address at a spatial-temporal boundary |
| **BRU** | Boundary Readback Unit — interface structure that converts a committed temporal address to a spatial voltage-level signal at a spatial-temporal boundary |
| **Causal depth** | The length of the longest directed path from any source operation to a given operation in the dependency graph; measured in operations (causal levels) |
| **Causal level** | A set of operations in the dependency graph at the same causal depth; operations within a causal level are mutually independent and may be placed in the same coherence slot |
| **CBT** | Coherence Budget Table — PDK component encoding SCR zone timing parameters and capacity limits; source of N_slots, N_slot_max, B_cycle, and F_in/out_max values |
| **CGR** | Causal Graph Rules — TDR rule category constraining the structure of the operation dependency graph; enforced by the CGV tool |
| **CGV** | Causal Graph Verification — EDA tool that checks CGR rules against the design's dependency graph |
| **CSA** | Commit Sequencing Arc — TTF arc modeling TRS L2 sequencing latency T_seq |
| **Critical Causal Path (CCP)** | The path through the operation dependency graph with the maximum causal depth; its length D_crit determines N_f_min |
| **D_crit** | The causal depth of the critical causal path; the minimum number of coherence slots required to complete the computation |
| **D_fold** | The fold depth of a specific fold: the number of distinct causal levels present within that fold |
| **D_fold_max** | The maximum achievable fold depth in one coherence cycle; equals N_usable − N_tr_write |
| **DDA** | Density-Dependent Derating Arc — TTF arc modeling timing margin reduction as temporal density approaches RWDL |
| **Dead time** | Coherence cycles during which a zone's substrate sites are idle, waiting for a cross-zone ZBI handoff to complete; equal to L_handoff Zone B cycles at each cross-zone fold boundary |
| **Discrimination-safe** | An address-value mapping property: the address separation between any two encoded logical values is ≥ Δτ_eff, ensuring the values are distinguishable by readback |
| **Fold** | See *Logic Fold* |
| **Fold boundary** | The coherence cycle boundary separating two consecutive folds in a multi-cycle computation |
| **Fold cutset** | The set of operations whose results must cross a fold boundary; each cutset element requires a Temporal Register write in the writing fold and a read in the receiving fold |
| **Fold depth** | See *D_fold* |
| **Fold region** | A designated spatial area of the die within which the operations of a given fold are placed |
| **Fold schedule** | The complete assignment of operations to coherence cycles and coherence slots; the temporal analog of a placed and routed netlist |
| **Fold width (W_fold)** | The total number of operations in a fold; bounded by D_fold × N_slot_max and by RWDL × A_fold_region |
| **Folding efficiency (η_fold)** | The fraction of total slot capacity consumed by computation operations; computed as N_compute / (N_compute + N_overhead) |
| **Hybrid spatial-temporal architecture** | A design that uses both Tier 1 spatial layers and Tier 2 temporal layers for different functional blocks |
| **Inter-fold dead time** | See *Dead time* |
| **L_FF_cross** | Cross-zone fold-to-fold latency; equals 1 + L_handoff in Zone B coherence cycles |
| **L_handoff** | ZBI inter-zone handoff latency in Zone B coherence cycles; from SCR qualification; source of cross-zone fold dead time |
| **Logic Fold** | The assignment of a subgraph of the full operation dependency graph to a single coherence cycle; the fundamental unit of temporal computation |
| **Multi-cycle folding** | A fold architecture in which the computation is partitioned into a sequence of N_f folds across N_f coherence cycles |
| **N_cutset** | The cardinality of the fold cutset at a given fold boundary; equals the number of TR sites required at that boundary |
| **N_f** | The number of folds in a multi-cycle fold chain |
| **N_f_min** | The minimum number of folds required; equals ceil(D_crit / D_fold_max) |
| **N_hold** | The number of coherence cycles a TR site must hold its committed state between its write and its last read |
| **N_overhead** | Total overhead operations in a folded design: TR writes + TR reads + refresh operations |
| **N_slot_max** | Maximum operations per coherence slot; from the TSPS for the layer's SC class |
| **N_tr_write** | Number of TR write operations in a fold; reduces D_fold_max by this amount |
| **N_usable** | Usable coherence slots per cycle: N_slots − 2 (excluding reserved slots 0 and N_slots−1) |
| **Operation fusion** | Combining two causally adjacent operations into a single operation that computes their composed function; reduces D_crit by 1 per fusion |
| **Pipeline folding** | A fold architecture where multiple instances of a computation are in-flight simultaneously, each in a different fold stage |
| **Refresh** | Re-committing the same address to a TR site before its state has relaxed beyond the discrimination threshold; required when N_hold > TSH |
| **Refresh overhead fraction (f_refresh)** | The fraction of cycles consumed by refresh operations for a TR site held N_hold > TSH cycles; approaches 1/TSH for long hold times |
| **RWDL** | Registration-Weighted Density Limit — maximum safe temporal density at a given die location; from TGI metrology; sets the spatial parallelism ceiling within a fold region |
| **SC** | Substrate Clarity — bulk measure of a substrate's capacity to sustain distinct temporal addresses; measured by TCT; governs Δτ_eff and TSH |
| **SCR** | Substrate Coherence Regime — the synchronization architecture for temporal manufacturing; its coherence cycle is the fundamental computation boundary |
| **Single-cycle folding** | A fold architecture where the entire computation completes within one coherence cycle; no fold boundaries, no TR overhead |
| **Spatial-temporal boundary (STB)** | The interface between a spatial block and a temporal block in a hybrid architecture; implemented by BCU (spatial-to-temporal) and BRU (temporal-to-spatial) |
| **T_auth** | Setup window before a coherence slot boundary within which the CA must assert authorization; from the SCR Specification |
| **T_c** | Coherence cycle period; the fundamental time unit of temporal manufacturing; from SCR qualification |
| **T_causal_level** | The timing budget per causal level within a fold: T_slot − T_arb − T_seq_max |
| **T_slot** | Duration of one coherence slot: T_c / N_slots |
| **TCA** | TAOE Correction Arc — TTF arc encoding the systematic temporal address offset from TGI metrology; applied spatially to operations in affected die regions |
| **Temporal Register (TR)** | A substrate site whose committed address state is read by a subsequent fold; passively holds state between coherence cycles up to TSH |
| **Temporal Register File (TRF)** | A collection of TR sites allocated for a given fold boundary; placed in a dedicated TRF region adjacent to both the writing and reading fold regions |
| **Temporal Register File region (TRF region)** | A dedicated substrate area housing a TRF; must be SC-I, isolated from high-density computation regions, and sized for the TR address reserve |
| **Temporal retiming** | Adjusting fold boundaries by moving operations between adjacent folds to balance D_fold across the fold chain; preserves the topological order of the dependency graph |
| **Temporal State Horizon (TSH)** | The maximum number of coherence cycles over which a TR site can reliably hold its committed address; set by τ_relax, Δτ_eff, and T_c |
| **TR address reserve** | The address subrange reserved for TR sites at a fold boundary; must not overlap with computation operation address ranges in either adjacent fold |
| **TRF** | See *Temporal Register File* |
| **TRS** | Temporal Resolution Stack — the four-layer operator system governing temporal manufacturing; defined in The Temporal Manufacturing Primer |
| **TSH** | See *Temporal State Horizon* |
| **TTF** | Temporal Timing Format — standardized format for temporal timing constraints as EDA timing arcs; defined in TTF Reference |
| **W_fold** | See *Fold width* |
| **ZBA** | Zone Boundary Arc — TTF arc modeling ZBI inter-zone handoff latency; applied to cross-zone fold boundaries on the critical causal path |
| **ZBI** | Zone Boundary Interface — SCR component managing inter-zone handoff; its latency L_handoff is the dominant cost of cross-zone fold boundaries |
| **Zone-distributed folding** | A fold architecture where a computation is partitioned across multiple SCR zones; incurs L_handoff dead time at each cross-zone fold boundary |
| **τ_relax** | Material relaxation time constant; the exponential decay constant governing address state relaxation after commit; sets the TSH via the state horizon formula |
| **Δτ_eff** | Effective minimum address spacing enforced by TDRC; equal to Δτ_min + Δτ_margin; governs the discrimination-safe constraint on address-value mappings |

---

## 15. Related Documents

| Document | Path | Relationship |
|---|---|---|
| The Temporal Manufacturing Primer | `docs/post-ASML_era/The_Temporal_Manufacturing_Primer.md` | Foundational concepts: TRS stack, SC classes, temporal density, MQD, coherence cycle, TCU; prerequisite reading for this guide |
| The SCR Specification | `docs/post-ASML_era/The_SCR_Specification.md` | Defines N_slots, T_c, SLF, L_handoff, D_max, and the arbitration protocol that governs intra-fold and cross-fold sequencing |
| The TGI Metrology Standard | `docs/post-ASML_era/The_TGI_Metrology_Standard.md` | Source of RWDL spatial maps that bound fold width; SC_eff values that constrain TR site placement; CLG non-monotonicity zones that impose TRF placement restrictions |
| TCT Protocol | `docs/post-ASML_era/TCT_Protocol.md` | Source of τ_relax (via material qualification record) and SC class; both feed directly into TSH computation and the address-value mapping discrimination-safe constraint |
| The TRS-Aware PDK Specification | `docs/post-ASML_era/The_TRS-Aware_PDK_Specification.md` | Provides the rule sets (TDR), timing arcs (TTF), and coherence budget tables (CBT) that constrain all quantitative parameters used in this guide; the PDK is the bridge between the manufacturing characterization and this architectural methodology |
| TTF Reference | `docs/eda/TTF_Reference.md` | Normative specification of the Temporal Timing Format arc types (APA, CSA, ZBA, TCA, DDA) consumed by TTF-aware STA tools during fold schedule optimization and timing closure |
| TRS Stack Qualification Procedure | `docs/fab/TRS_Qualification.md` | Source of TSPS parameters: Δτ_min, Δτ_margin, N_slot_max, T_seq; required for D_fold_max and W_fold_max computation |
| SCR Zone Configuration Guide | `docs/fab/SCR_Zone_Config.md` | Zone sizing and boundary placement decisions that determine the floorplanning constraints for zone-distributed folding and cross-zone fold boundary alignment |
| Substrate Clarity Classification Standard | `docs/materials/SC_Classification.md` | Defines SC class thresholds and their relationship to material properties including τ_relax, which governs TSH |

---

*This document is part of the TriadicFrameworks canonical reference set. Proposed
revisions should be submitted via pull request to the `docs/post-ASML_era/` directory
with a linked issue describing the change rationale. Revisions to §5 (Causal Depth
and Fold Depth Analysis), §6 (Temporal Register Architecture), or §12 (Design
Patterns) that introduce new quantitative formulas or change existing ones require
review by at least two maintainers with confirmed temporal manufacturing design
experience. Revisions to §13 (Migration from Spatial Logic) that add new classical
constructs to the translation table or the non-translating constructs list require
a cross-reference check against all design pattern sections to ensure consistency.*

**The Logic Folding Architecture Guide is complete.** Here's what the final continuation delivered:

- **§13.3 finished** — the broken sentence on level-sensitive storage was completed, followed by five additional non-translating constructs: tri-state buses, glitch-tolerant hazard filtering, clock gating, race conditions/metastability (with the key note that there is no temporal synchronizer analog)
- **§13.4 added** — Hybrid Spatial-Temporal Architectures, covering partitioning principles (with a domain-selection table), the spatial-temporal boundary (BCU/BRU structures), power domain differences between spatial and temporal blocks, and hybrid verification challenges (interface protocol, cross-domain causal consistency, co-simulation)
- **§14 Glossary** — 48 terms, alphabetically sorted, covering every term introduced in this document plus forward/backward references to terms defined in prior documents
- **§15 Related Documents** — 9-row table linking all five prior documents plus four stubs, with precise relationship descriptions
- **Standard footer** with maintainer review requirements for changes to quantitative sections

That wraps the sixth document in the series. The natural next candidate would be **`TTF_Reference.md`** — it's the most-referenced stub across all six documents (PDK Specification, SCR Spec, Logic Folding Guide all depend on it), and formalizing the five arc types (APA, CSA, ZBA, TCA, DDA) with their full parameter schemas would close the largest remaining gap in the canon. Say the word and I'll start it.
