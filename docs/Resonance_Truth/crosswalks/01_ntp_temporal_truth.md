# Crosswalk #1 — NTP and Temporal Truth

**Module:** Resonance Truth  
**Artifact:** Operational Truth Crosswalk #1  
**Truth Class:** Temporal Truth  
**Reference System:** Network Time Protocol (NTP)  
**Primary RTT Dimensions:** Temp · Coherence · Drift · Regime  
**Supporting RTT Dimensions:** Resonance · Paradox · Lineage  
**Status:** Research Crosswalk / Reference Architecture  
**Context:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

---

## Purpose

This crosswalk examines the Network Time Protocol as the first operational reference system for the RTT Resonance Truth Service.

The governing question is:

> **When is it true?**

NTP is useful because time synchronization requires a distributed system to maintain an operationally usable temporal state while accounting for:

- multiple Sources
- distance from reference
- network delay
- local clock offset
- Observation history
- Source selection
- Source disagreement
- instability
- uncertainty
- local state Correction
- repeated Revalidation

The objective is not to claim:

    NTP
     =
    RTT

or:

    time synchronization
     =
    all truth

Instead, the crosswalk asks:

> **Which NTP mechanisms reveal structures that may generalize into an operational Truth Service?**

---

# 1. Evidence Boundary

The primary technical reference for this crosswalk is:

    RFC 5905
    Network Time Protocol Version 4:
    Protocol and Algorithms Specification

The RFC defines the NTPv4 protocol and implementation model.

Relevant mechanisms include:

- Peer Process
- Clock Filter Algorithm
- Selection Algorithm
- Cluster Algorithm
- Combine Algorithm
- Clock Discipline Algorithm
- Clock-Adjust Process
- Poll Process

These mechanisms provide the concrete reference-system behavior used in this crosswalk.

RTT terms introduced in this document are analytical interpretations.

They are not terminology used by NTP itself unless explicitly stated otherwise.

---

# 2. Evidence Discipline

This crosswalk distinguishes four statement types.

## NTP Fact

A mechanism explicitly described by the NTP specification.

## RTT Interpretation

A proposed structural interpretation of that mechanism through the RTT lens.

## Candidate Generalization

A proposed architectural mechanism that may apply beyond Temporal Truth.

## Hypothesis

A proposed generalization that remains insufficiently tested across other Truth Classes.

Example:

    NTP Fact:
      NTP compares timing information from multiple associations.

    RTT Interpretation:
      Multiple timing Sources form a candidate Coherence field.

    Candidate Generalization:
      Operational truth systems may benefit from multi-Source comparison.

    Hypothesis:
      All Truth Classes require explicit Coherence clustering.

The final statement remains provisional until later crosswalks challenge it.

---

# 3. Why NTP Comes First

NTP addresses a deceptively simple question:

> **What time is it?**

A local system cannot safely assume that its own clock remains perfectly aligned with its reference.

A distributed timing system must account for:

- local clock behavior
- network transport
- remote Sources
- multiple observations
- changing measurements
- Source suitability
- local adjustment

This makes NTP a useful first operational truth system because several important structural conditions are measurable.

Temporal Drift, for example, can be represented quantitatively.

This gives the Resonance Truth research a comparatively concrete starting point before moving into less directly measurable domains such as:

- Identity Truth
- Authority Truth
- Intent Truth
- Observational Truth
- Lineage Truth

---

# 4. Temporal Truth

The primary Truth Class is:

    Temporal Truth

Its operational question is:

> **When does this Claim hold?**

Temporal Truth includes more than a timestamp.

It may involve:

- observation time
- reference time
- local time
- Source time
- transport delay
- freshness
- validity intervals
- temporal Drift
- re-observation
- expiration

The generalized Temporal Truth relationship is therefore:

    local temporal state
          ↕
    qualified external Observations
          ↕
    recognized references
          ↕
    time

---

# 5. NTP on Its Own Terms

At a high level, NTP is a protocol used to synchronize computer clocks.

Its specification includes mechanisms for:

- exchanging timing information
- maintaining peer associations
- processing timing samples
- filtering samples
- selecting candidate Sources
- clustering candidates
- combining timing information
- disciplining the local clock
- adjusting the local clock
- determining polling behavior

The system therefore contains more structure than:

    ask server for time
        ↓
    set clock

A more useful conceptual sequence is:

    RECEIVE TIMING INFORMATION
              ↓
    MAINTAIN SOURCE ASSOCIATIONS
              ↓
    FILTER SAMPLES
              ↓
    SELECT CANDIDATES
              ↓
    CLUSTER / MITIGATE OUTLIERS
              ↓
    COMBINE
              ↓
    DISCIPLINE LOCAL CLOCK
              ↓
    ADJUST LOCAL CLOCK
              ↓
    POLL AGAIN

This process provides the operational substrate for the RTT crosswalk.

---

# 6. Initial Structural Crosswalk

| NTP Concept | RTT Truth-Service Interpretation | Status |
|---|---|---|
| Reference clock | Truth Anchor | Candidate General |
| Server / peer | Source | Candidate General |
| Association | Source relationship | Candidate General |
| Stratum | Lineage distance | Candidate General |
| Time sample | Observation | Candidate General |
| Timestamp | Observation time | Candidate General |
| Delay | Observation distance / propagation condition | Candidate General |
| Offset | Drift | Strong Candidate General |
| Jitter | Instability | Candidate General |
| Dispersion | Uncertainty growth | Candidate General |
| Clock filter | Evidence qualification / filtering | Strong Candidate General |
| Selection algorithm | Source qualification | Strong Candidate General |
| Cluster algorithm | Coherence / outlier containment | Candidate General |
| Combine algorithm | Truth-State synthesis | Candidate General |
| Clock discipline | Bounded Correction | Strong Candidate General |
| Clock adjustment | Local state mutation | Candidate General |
| Poll process | Revalidation | Strong Candidate General |

The table intentionally labels these mappings as candidates.

Later crosswalks must determine which survive beyond Temporal Truth.

---

# 7. Truth Anchor

## NTP Reference-System View

NTP ultimately operates relative to timing references.

Reference clocks and upstream timing Sources participate in a hierarchy through which timing information reaches downstream systems.

## RTT Interpretation

The crosswalk introduces:

    Truth Anchor

A Truth Anchor is:

> **A recognized reference within a declared operational domain and Regime.**

For Temporal Truth:

    recognized temporal reference
          ↓
    timing Source
          ↓
    downstream Source
          ↓
    local Observation

## Candidate Generalization

Operational truth systems may benefit from explicitly representing:

- reference identity
- reference domain
- authority
- validity
- Lineage distance
- Source relationship

## Open Question

Does every Truth Class require an Anchor?

Later crosswalks may reveal systems where:

- authority is distributed
- state emerges through agreement
- no single reference exists
- multiple Anchors legitimately coexist

Therefore:

    Anchor

remains a candidate generalized abstraction rather than a universal requirement.

---

# 8. Source

## NTP Reference-System View

NTP maintains associations with timing peers or servers.

These associations provide timing information used by the protocol's algorithms.

## RTT Interpretation

The generalized entity is:

    Source

A Source is:

> **An entity capable of supplying an Observation relevant to a Claim.**

For NTP:

    timing Source
        ↓
    time sample

For the generalized Truth Service:

    Source
        ↓
    Observation

## Candidate Generalization

Separating:

    Source

from:

    Observation

is likely useful beyond Temporal Truth because it preserves:

- identity
- history
- reliability
- dependencies
- Lineage
- independence

These properties cannot be represented adequately if the Observation alone is retained.

---

# 9. Source Association

## NTP Reference-System View

NTP maintains state associated with peers.

A peer relationship is not merely one isolated timing packet.

The protocol retains data used in processing and selection.

## RTT Interpretation

This suggests:

    Source relationship

The Truth Service may need to preserve the ongoing structural relationship between:

- observer
- Source
- Anchor
- Observation history

rather than treating every Observation as independent.

## Candidate Generalization

A Source relationship may eventually contain:

- Source identity
- Anchor relationship
- Observation history
- dependency information
- stability
- rejection history
- freshness

## Architectural Status

The current generalized model carries much of this through:

    Source
    Observation
    Lineage
    Evaluation history

A dedicated SourceAssociation entity has not yet been promoted into the core data model.

Further crosswalk evidence is required.

---

# 10. Stratum → Lineage Distance

## NTP Reference-System View

NTP exposes a hierarchy related to distance from reference timing Sources through stratum.

## RTT Interpretation

The crosswalk generalizes this as:

    Lineage Distance

The useful structural question becomes:

> **How far has this Observation traveled from the reference relationship from which it derives?**

This may involve:

- Source hops
- transformations
- aggregators
- delegations
- caches
- intermediaries

## Candidate Generalization

Lineage Distance should not necessarily be one integer in every Truth Class.

Possible representations include:

- hop count
- transformation count
- authority chain
- dependency depth
- graph path

The important principle is:

> **Distance from reference may itself be truth metadata.**

## Architectural Caution

    greater Lineage distance
        ≠
    false

Distance changes qualification context.

It does not automatically determine correctness.

---

# 11. Time Sample → Observation

## NTP Reference-System View

Timing samples provide information used by the protocol's filtering and selection mechanisms.

## RTT Interpretation

The generalized object is:

    Observation

An Observation records:

> **What a Source reported or measured under identifiable conditions.**

A Temporal Observation may contain:

    Source
    observed timestamp
    receipt timestamp
    timing data
    freshness information
    Source Lineage

## Candidate Generalization

The Truth Service separates:

    Observation

from:

    Truth State

This is one of the strongest initial architectural distinctions.

An Observation participates in Evaluation.

It is not itself the final state.

---

# 12. Observation Time

NTP makes temporal relationships unusually visible because timestamps participate directly in protocol behavior.

The generalized Truth Service should preserve several different temporal fields.

## Observation Time

When the Source observed the state.

## Receipt Time

When the evaluator received the Observation.

## Evaluation Time

When the Observation was used.

## Expiration Time

When the Observation no longer satisfies a freshness requirement.

## Revalidation Time

When the resulting Truth State must be challenged again.

These are structurally different moments.

The crosswalk therefore supports:

> **Time should be attached to evidence and evaluation, not merely to the final Claim.**

---

# 13. Delay → Observation Distance

## NTP Reference-System View

Network delay affects temporal measurement.

The Observation does not arrive under ideal zero-distance conditions.

## RTT Interpretation

The candidate generalized concept is:

    Observation Distance

Observation Distance represents structural separation between:

    original state

and:

    received evidence

Potential contributors beyond NTP may include:

- network propagation
- caching
- transformation
- aggregation
- translation
- replication
- summarization
- inference

## Candidate Generalization

An Observation without any information about its path may be structurally weaker than apparently identical evidence whose path is known.

This overlaps with Lineage.

Later crosswalks should determine whether:

    Observation Distance

deserves a distinct architectural field or should remain a property derived from Lineage.

---

# 14. Offset → Drift

## NTP Reference-System View

Offset concerns the difference between temporal states involved in synchronization.

## RTT Interpretation

This maps strongly to:

    Drift

General form:

    Drift
      =
    displacement between relevant states

Potential comparisons include:

    local vs reference

    current vs prior

    declared vs observed

    Source A vs Source B

    expected vs actual

## Temporal Example

    local:
      09:00:00.000

    qualified observed:
      09:00:00.014

    temporal Drift:
      +14 ms

## Candidate Generalization

Drift is currently one of the strongest generalized mechanisms obtained from the NTP crosswalk.

Not every Truth Class will provide a meaningful numeric magnitude.

Therefore:

    magnitude:
      null

must remain valid for semantic or structural Drift.

---

# 15. Jitter → Instability

## NTP Reference-System View

Variation among timing measurements is operationally relevant to NTP processing.

## RTT Interpretation

The candidate generalized concept is:

    Instability

Instability asks:

> **How much does the Observation stream vary over repeated measurement?**

Potential manifestations include:

- fluctuating measurements
- inconsistent Source behavior
- alternating classifications
- unstable state
- rapidly changing evidence
- changing interpretation

## Candidate Generalization

A system should not necessarily evaluate only:

    latest Observation

It may also need to evaluate:

    behavior of Observation history

This remains a candidate abstraction.

Later crosswalks should determine whether Instability belongs:

- inside Drift
- inside Observation Quality
- as its own object
- as domain-specific metadata

---

# 16. Dispersion → Uncertainty Growth

## NTP Reference-System View

NTP represents error and uncertainty-related timing conditions as part of its synchronization machinery.

## RTT Interpretation

The candidate generalized mechanism is:

    Uncertainty Growth

The generalized principle is:

> **Evidence may become less useful without becoming explicitly false.**

Potential causes include:

- age
- Source loss
- increasing Lineage distance
- transformation
- reduced corroboration
- changing conditions
- unresolved contradiction

## Candidate State Progression

    OPERATIONALLY_ACCEPTED
            ↓
        DEGRADED
            ↓
        HELD_OVER
            ↓
         EXPIRED

This progression is an RTT architectural generalization.

It is not presented as NTP terminology.

---

# 17. Clock Filter → Evidence Qualification

## NTP Reference-System View

RFC 5905 defines a Clock Filter Algorithm used in processing timing samples.

## RTT Interpretation

The generalized mechanism is:

    Evidence Qualification

Potential Observation checks include:

- structural validity
- freshness
- integrity
- Source status
- precision
- Lineage
- duplication
- Regime compatibility

## Qualification Outcomes

The Truth Service currently proposes:

    qualified
    degraded
    rejected
    expired
    indeterminate

## Critical Rule

    rejected from synthesis
          ≠
    false

The crosswalk preserves this distinction because an Observation may be unsuitable for the current operational Evaluation without supporting a universal claim of falsehood.

---

# 18. Selection → Source Qualification

## NTP Reference-System View

NTP includes a Selection Algorithm as part of its system process.

## RTT Interpretation

The generalized mechanism is:

    Source Qualification

The Truth Service distinguishes:

    Source exists

from:

    Source may influence this Evaluation

Potential qualification factors include:

- Source status
- Anchor relationship
- Lineage
- Observation quality
- independence
- freshness
- Regime compatibility

## Candidate Generalization

This separation appears strong enough to remain in the current architecture.

Later crosswalks should test whether Source qualification differs meaningfully from Observation qualification.

---

# 19. Clustering → Coherence

## NTP Reference-System View

RFC 5905 defines a Cluster Algorithm as part of the system process.

## RTT Interpretation

This suggests:

    Coherence Clustering

Qualified Observations may form:

    Cluster A
      Observation 1
      Observation 2
      Observation 3

while another Observation or cluster remains separate.

## RTT Question

> **Do qualified Observations form a mutually usable operational field?**

Possible Coherence states:

    coherent
    weakly_coherent
    fragmented
    contested
    inverted
    indeterminate

These states are RTT architectural constructs.

They are not NTP protocol terminology.

---

# 20. Outliers → Paradox Containment

NTP motivates a useful distinction between:

    identifying disagreement

and:

    destroying evidence of disagreement

For the generalized Truth Service, dissenting evidence should remain available for audit even when it does not influence the accepted state.

## Candidate Pattern

    Qualified Observations
          ↓
    Coherence Analysis
          ↓
       ┌──┴──┐
       │     │
    Cluster  Dissent
       │     │
       ▼     ▼
    Synthesis  Preserve

## RTT Interpretation

Where incompatible qualified states remain significant:

    Paradox

may be registered.

## Important Constraint

Not every NTP outlier is an RTT Paradox.

The crosswalk distinguishes:

    outlier

from:

    structurally meaningful unresolved contradiction

Paradox should be reserved for the latter.

---

# 21. Combine → Truth-State Synthesis

## NTP Reference-System View

RFC 5905 defines a Combine Algorithm after Source selection and clustering.

## RTT Interpretation

The generalized mechanism is:

    Truth-State Synthesis

The operation asks:

> **Given the surviving qualified evidence, what operational state can presently be supported?**

## Candidate Output

A Truth State may preserve:

- accepted value
- Sources
- Observations
- Anchor
- Lineage
- Coherence
- Drift
- uncertainty
- Paradox
- Regime
- expiration
- Revalidation

## Critical Distinction

Synthesis produces:

    operationally qualified state

not:

    universal absolute truth

This is a central Resonance Truth principle.

---

# 22. Clock Discipline → Bounded Correction

## NTP Reference-System View

NTP includes a Clock Discipline Algorithm that governs the local clock relationship with synchronization results.

## RTT Interpretation

This maps strongly to:

    Bounded Correction

The generalized distinction is:

    determine better-supported state
                ≠
    immediately replace local state

## Candidate Correction Modes

The Truth Service currently proposes:

    none
    step
    gradual
    quarantine
    dual_state
    human_escalation
    holdover
    fail_closed
    fail_bounded

These modes are generalized Truth-Service concepts.

They should not be interpreted as NTP's own correction vocabulary.

## Architectural Contribution

NTP strongly motivates separation between:

    Evaluation

and:

    state adjustment

This is one of the most important mechanisms contributed by Crosswalk #1.

---

# 23. Clock Adjustment → State Mutation

NTP also makes another distinction useful:

    deciding how correction should occur

and:

    executing the local adjustment

These need not be the same operation.

In the Truth Service architecture:

    Truth State
        ↓
    Correction Policy
        ↓
    Downstream System
        ↓
    State Mutation

The Truth Service may determine that:

    correction:
      gradual

without itself owning the system being corrected.

This preserves:

    truth evaluation
        ≠
    mutation authority

---

# 24. Poll Process → Revalidation

## NTP Reference-System View

RFC 5905 defines a Poll Process governing repeated timing exchange behavior.

## RTT Interpretation

This strongly suggests:

    Revalidation

The service should not assume that a Truth State remains operationally acceptable indefinitely.

## General Lifecycle

    OBSERVE
       ↓
    QUALIFY
       ↓
    EVALUATE
       ↓
    ACCEPT
       ↓
    USE
       ↓
    AGE
       ↓
    REVALIDATE

Then:

    RENEW
    DEGRADE
    CONTEST
    HOLD OVER
    REJECT
    EXPIRE

## Architectural Contribution

Revalidation is one of the strongest mechanisms contributed by NTP.

Operational truth has a lifecycle.

---

# 25. Loss of Fresh Sources → Holdover

A useful architectural question arises when a previously supported local state loses access to fresh qualified observations.

The Truth Service distinguishes:

    no fresh evidence

from:

    evidence that prior state is false

This makes room for:

    HELD_OVER

## RTT Holdover

A Truth State may remain provisionally usable when:

- it was previously qualified
- fresh evidence temporarily disappears
- no strong contradicting evidence has appeared
- expected Drift remains bounded
- the Regime permits temporary continuation

## Candidate Lifecycle

    OPERATIONALLY_ACCEPTED
            ↓
       Source Loss
            ↓
        HELD_OVER
            ↓
       ┌────┴────┐
       │         │
    Renew      Expire

Holdover is an RTT architecture generalization.

Later crosswalks must determine whether it generalizes usefully beyond Temporal Truth.

---

# 26. Failure Transparency

NTP provides an important operational lesson:

> A synchronization system must represent when it cannot establish a usable synchronized state.

The generalized RTT principle becomes:

> **A Truth Service must be able to admit that it does not presently possess enough qualified evidence to produce an accepted state.**

The corresponding Truth State is:

    INDETERMINATE

This should be considered:

    successful evaluation

rather than:

    service failure

The inability to establish a qualified state is itself useful operational information.

---

# 27. Temporal Regime

Temporal Claims are meaningful only relative to operational requirements.

Consider:

    "The clock is synchronized."

This Claim is incomplete without asking:

> **Synchronized sufficiently for what?**

Potential Regimes include:

- human-readable display
- log correlation
- distributed processing
- measurement
- transaction ordering

The same measured offset may be acceptable in one Regime and unacceptable in another.

Therefore:

    measurement
        +
    Regime
        ↓
    operational qualification

This supports the core architectural principle:

> **Truth qualification may depend on Regime without truth becoming arbitrary.**

---

# 28. Worked Example — Coherent Temporal Truth

Consider a deterministic fixture.

## Claim

    Current reference time is T.

## Truth Class

    temporal

## Regime

    low-consequence display clock

## Anchor

    recognized temporal reference

## Sources

    Source A
    Source B
    Source C

## Observations

    A:
      offset: +12 ms

    B:
      offset: +15 ms

    C:
      offset: +14 ms

## Qualification

    A:
      qualified

    B:
      qualified

    C:
      qualified

## Coherence

    coherent

## Drift

    magnitude:
      bounded

## Paradox

    no material unresolved contradiction

## Truth State

    operationally_accepted

## Correction

    regime-defined bounded correction

## Revalidation

    scheduled

The important result is not merely the accepted time value.

The important result is that the path to acceptance remains inspectable.

---

# 29. Worked Example — Outlier

Now alter Source C.

## Observations

    A:
      offset: +12 ms

    B:
      offset: +15 ms

    C:
      offset: +900 ms

The service should evaluate:

- whether C remains qualified
- whether C belongs to the same Coherence cluster
- whether its Lineage differs
- whether Source independence is meaningful
- whether the disagreement is an outlier
- whether it becomes a material Paradox

Possible result:

    supporting cluster:
      A
      B

    dissenting:
      C

The dissent should remain visible even if it does not influence the accepted temporal state.

---

# 30. Worked Example — Fragmented Sources

Consider:

    A:
      state → X

    B:
      state → X

    C:
      state → Y

    D:
      state → Y

The correct response is not automatically:

    average X and Y

The Coherence Engine may produce:

    Cluster X:
      A
      B

    Cluster Y:
      C
      D

with:

    coherence:
      fragmented

and:

    Truth State:
      contested

or:

    Truth State:
      indeterminate

depending on Regime.

This fixture tests whether:

> **The implementation can resist manufacturing certainty.**

---

# 31. Worked Example — Stale Sources

Suppose previously qualified Observations age beyond the Regime's freshness requirement.

Possible lifecycle:

    OPERATIONALLY_ACCEPTED
            ↓
        DEGRADED
            ↓
        HELD_OVER
            ↓
         EXPIRED

The exact transitions are Regime-specific.

This fixture tests:

- freshness
- uncertainty growth
- Holdover
- expiration
- Revalidation

---

# 32. Worked Example — No Qualified Sources

Suppose:

    Observation A:
      expired

    Observation B:
      rejected

    Observation C:
      indeterminate

Then:

    selected Observations:
      none

Possible result:

    coherence:
      indeterminate

    Drift:
      unknown

    Truth State:
      indeterminate

    accepted_value:
      null

This is a successful result.

The service has answered:

> **The available evidence does not presently support a qualified temporal state.**

---

# 33. RTT Dimension Mapping

| RTT Dimension | NTP Crosswalk Interpretation | General Truth-Service Candidate |
|---|---|---|
| **Resonance** | Timing information propagates through Source relationships | Evidence propagates through Source relationships |
| **Coherence** | Qualified timing Sources form a usable timing field | Qualified Observations form a mutually usable state |
| **Drift** | Local temporal state differs from qualified timing state | Accepted state differs from relevant evidence/reference |
| **Paradox** | Significant qualified disagreement remains unresolved | Competing qualified states remain structurally incompatible |
| **Regime** | Timing precision and suitability depend on operational need | Truth acceptance depends on declared operational conditions |
| **Spin** | Temporal relationship persists across observations | Claim / Source / Lineage identity persists |
| **Elec** | Sources and observations remain distinguishable | Evidence and boundaries remain separable |
| **Temp** | Synchronization requires repeated adjustment | Truth States age, transition, and require Revalidation |

---

# 34. SET Mapping

## Spin

Within the Temporal Truth crosswalk, Spin corresponds to persistence of:

- Source identity
- Anchor relationship
- timing relationship
- Lineage
- local temporal state

## Elec

Elec corresponds to distinction among:

- Sources
- peers
- candidate observations
- rejected observations
- clusters
- operational boundaries

## Temp

Temp is particularly visible in NTP because the system directly manages:

- temporal change
- freshness
- polling
- Drift
- correction
- synchronization state

The generalized interpretation is:

> **Spin preserves temporal relationship.**

> **Elec distinguishes Sources and observations.**

> **Temp governs synchronization, transition, and renewal.**

---

# 35. Candidate General Mechanisms from NTP

Crosswalk #1 produces the following candidate generalized mechanisms:

1. Truth Anchor
2. Source
3. Source relationship
4. Observation
5. Lineage
6. Lineage distance
7. Observation distance
8. Qualification
9. Coherence
10. Coherence clustering
11. Drift
12. Instability
13. uncertainty growth
14. Paradox containment
15. Regime qualification
16. Truth-State synthesis
17. bounded Correction
18. Holdover
19. Revalidation
20. failure transparency

These should not all be promoted blindly.

Crosswalks #2 through #10 must challenge them.

---

# 36. Strongest Architectural Contributions

Crosswalk #1 currently provides particularly strong support for the following ideas.

## Observation ≠ Truth State

Timing samples participate in state determination.

They are not themselves identical to the local synchronized state.

## Source ≠ Observation

The Source has identity and history beyond one sample.

## Drift Is First-Class

Displacement between local and reference-related state can be operationally important.

## Qualification Precedes Synthesis

Not every available Observation should influence accepted state.

## Multi-Source Coherence Matters

A system benefits from comparing candidate Sources rather than blindly trusting one Observation.

## Correction Is Separate from Evaluation

Determining state and adjusting local state are distinct functions.

## Revalidation Is Continuous

Operational state ages and must be refreshed.

## Indeterminate Must Exist

Loss of sufficient qualification should remain visible.

---

# 37. Mechanisms Still Under Question

Some NTP-inspired concepts require additional validation before becoming core generalized abstractions.

## Lineage Distance

Strong in hierarchical systems.

May behave differently in:

- consensus systems
- peer systems
- decentralized systems

## Observation Distance

May overlap too strongly with Lineage.

DNS and provenance may clarify this.

## Instability

May belong inside Drift or Observation Quality rather than remaining independent.

## Uncertainty Growth

May differ significantly by Truth Class.

## Holdover

Strong for temporal continuity.

May not generalize cleanly into Identity or Authority Truth.

## Coherence Clustering

Strong candidate, but later systems may use fundamentally different agreement structures.

These remain:

    CANDIDATE_GENERAL

rather than:

    CONFIRMED_GENERAL

---

# 38. Architectural Challenge Produced by NTP

NTP immediately challenges a simplistic Truth Service architecture.

A naïve design might use:

    Claim
      ↓
    Single Source
      ↓
    Boolean Result

The NTP crosswalk instead suggests:

    Claim
      ↓
    Multiple Sources
      ↓
    Multiple Observations
      ↓
    Qualification
      ↓
    Comparison
      ↓
    Coherence
      ↓
    Drift
      ↓
    Synthesis
      ↓
    Correction
      ↓
    Revalidation

This is the first major structural expansion of the Truth-Service model.

---

# 39. NTP Bias Risk

Because NTP is the first reference system, it may exert too much influence over the initial architecture.

Known risks include assuming that every Truth Class requires:

- one external reference hierarchy
- measurable Drift
- numeric uncertainty
- periodic polling
- Source clustering
- local convergence
- Holdover

These assumptions must be challenged.

The next crosswalk therefore has a specific research role.

---

# 40. Crosswalk #2 Challenge

Crosswalk #2 examines:

    DNS
      ↓
    Locational Truth

DNS introduces mechanisms such as:

- namespace hierarchy
- delegation
- authoritative zones
- recursive resolution
- caching
- TTL
- observer-dependent answers
- negative responses

The primary challenge becomes:

> **Can the Truth-Service architecture represent Locational Truth without pretending DNS is another clock?**

Crosswalk #2 should explicitly revisit every NTP-derived candidate generalization.

---

# 41. Scoring Boundary

The scoring boundary for this crosswalk is:

    System:
      Network Time Protocol

    Primary Truth Class:
      Temporal Truth

    Evaluated Scope:
      NTPv4 protocol and algorithms represented by RFC 5905

    Primary Evidence:
      RFC 5905

    Excluded / Deferred:
      deployment-specific monitoring
      vendor-specific implementation behavior
      external operational policy
      mechanisms not established by the reviewed evidence

This boundary matters.

The crosswalk should not score an idealized global "NTP ecosystem" unless that broader scope is explicitly declared.

---

# 42. Preliminary Scoring Status

At this stage:

    Score Status:
      provisional

Scores should be assigned only where the evidence boundary supports them.

The current specification review supports detailed examination of:

- Observation processing
- filtering
- Source selection
- clustering
- combination
- clock discipline
- polling

Other dimensions may require additional evidence before receiving stable scores.

Therefore:

> **Do not force completion of the scorecard merely because the rubric contains ten rows.**

---

# 43. Provisional Scorecard Template

| Criterion | Score | Delegation | Status |
|---|---:|---|---|
| Anchor Quality |  |  | Not yet scored |
| Lineage Visibility |  |  | Not yet scored |
| Observation Quality |  |  | Not yet scored |
| Coherence Detection |  |  | Not yet scored |
| Drift Detection |  |  | Not yet scored |
| Paradox Handling |  |  | Not yet scored |
| Regime Awareness |  |  | Not yet scored |
| Freshness / Revalidation |  |  | Not yet scored |
| Correction Discipline |  |  | Not yet scored |
| Failure Transparency |  |  | Not yet scored |
| **Total** | **/50** |  | Deferred |

The blank scores are deliberate.

The detailed scoring pass should attach rationale and evidence to each value.

---

# 44. Expected Scoring Strengths

Before scoring, the crosswalk suggests likely areas of strong structural representation.

These are hypotheses, not scores.

Likely strong areas include:

- Observation Quality
- Coherence Detection
- Drift Detection
- Freshness / Revalidation
- Correction Discipline

Potentially more nuanced areas include:

- Lineage Visibility
- Paradox Handling
- Regime Awareness
- Failure Transparency

The scoring pass should confirm or reject these expectations from evidence.

---

# 45. Fixture Requirements

Crosswalk #1 should eventually be represented by deterministic fixtures under:

    ../fixtures/ntp/

Initial fixtures are:

    coherent.json
    minor_drift.json
    outlier.json
    fragmented.json
    stale.json
    indeterminate.json

Each fixture should preserve:

- Claim
- Truth Class
- Regime
- Anchor
- Sources
- Observations
- Lineage
- Qualification
- Coherence
- Drift
- Paradox where applicable
- Truth State
- Correction policy
- Revalidation condition

The fixture result should be explainable from those objects.

---

# 46. Test Requirements

The NTP reference implementation should eventually test:

## Qualification

Can stale or unsuitable Observations be excluded with explicit rationale?

## Coherence

Can compatible Observations be identified without relying solely on Source count?

## Drift

Can temporal displacement be represented quantitatively?

## Paradox

Can materially conflicting qualified evidence remain visible?

## Regime

Can the same temporal evidence produce different operational qualification under different requirements?

## Lifecycle

Can a Truth State:

    operationally_accepted
        ↓
    degraded
        ↓
    held_over
        ↓
    expired

without being rewritten historically?

---

# 47. Findings Classification

At the completion of this crosswalk, findings should be classified using:

    CONFIRMED_GENERAL

    CANDIDATE_GENERAL

    DOMAIN_SPECIFIC

    ARCHITECTURE_GAP

    REGIME_SPECIFIC

    PARADOX_PRESERVED

    REJECTED_GENERALIZATION

Current NTP-derived mechanisms should generally remain:

    CANDIDATE_GENERAL

until later Truth Classes provide additional evidence.

---

# 48. Initial Findings

## Finding 1

Operational temporal state is synthesized from relationships among local state, Sources, Observations, and reference structure.

    Status:
      CANDIDATE_GENERAL

## Finding 2

An Observation should remain distinct from the state produced using it.

    Status:
      CANDIDATE_GENERAL

## Finding 3

Source identity and Observation identity should remain separate.

    Status:
      CANDIDATE_GENERAL

## Finding 4

Drift can be a first-class property of operational truth.

    Status:
      CANDIDATE_GENERAL

## Finding 5

Evidence qualification should precede Truth-State synthesis.

    Status:
      CANDIDATE_GENERAL

## Finding 6

Contradictory Observations should remain inspectable after Source selection.

    Status:
      CANDIDATE_GENERAL

## Finding 7

Determining a better-supported state should remain separate from correcting local state.

    Status:
      CANDIDATE_GENERAL

## Finding 8

Operational Truth States require Revalidation.

    Status:
      CANDIDATE_GENERAL

## Finding 9

Loss of fresh evidence does not necessarily imply immediate falsehood.

    Status:
      CANDIDATE_GENERAL

## Finding 10

A Truth Service should be able to expose loss of qualification without fabricating an accepted state.

    Status:
      CANDIDATE_GENERAL

---

# 49. NTP-to-Truth-Service Processing Crosswalk

The complete candidate processing crosswalk is:

    NTP REFERENCE                    RTT TRUTH SERVICE
    ─────────────                    ─────────────────

    Reference timing source
              ↓
                                      Truth Anchor

    Server / peer
              ↓
                                      Source

    Association
              ↓
                                      Source relationship

    Stratum
              ↓
                                      Lineage distance

    Time sample
              ↓
                                      Observation

    Delay
              ↓
                                      Observation distance

    Offset
              ↓
                                      Drift

    Jitter
              ↓
                                      Instability

    Dispersion
              ↓
                                      Uncertainty growth

    Clock filter
              ↓
                                      Qualification

    Selection
              ↓
                                      Source qualification

    Clustering
              ↓
                                      Coherence analysis

    Outlier handling
              ↓
                                      Dissent / Paradox containment

    Combination
              ↓
                                      Truth-State synthesis

    Clock discipline
              ↓
                                      Correction policy

    Clock adjustment
              ↓
                                      Downstream state mutation

    Poll process
              ↓
                                      Revalidation

The right-hand side remains the RTT interpretation.

It should change if later crosswalk evidence demonstrates that these abstractions are incorrect or over-generalized.

---

# 50. Crosswalk Evaluation

Crosswalk #1 establishes an important starting result:

> **Operational truth does not necessarily require a system to possess an absolute, context-free answer.**

NTP demonstrates an operational architecture in which useful local state can be maintained through structured relationships among:

- reference
- Source
- Observation
- filtering
- comparison
- Drift
- Correction
- repeated reevaluation

The RTT Resonance Truth Service proposes to generalize those relationships cautiously.

The crucial word is:

> **cautiously**

NTP is evidence for Temporal Truth mechanisms.

It is not proof that every Truth Class shares the same structure.

---

# 51. Canonical Temporal Truth Statement

> **Temporal Truth is not merely a timestamp. It is a Regime-qualified relationship between an observer's local temporal state and a Lineage of external Observations, maintained through qualification, Coherence evaluation, Drift measurement, bounded Correction, and repeated Revalidation.**

This statement is the RTT interpretation produced by Crosswalk #1.

It is not an NTP protocol definition.

---

# 52. Canonical Crosswalk Finding

Crosswalk #1 contributes the following candidate architecture:

    REFERENCE
        ↓
    SOURCE
        ↓
    OBSERVATION
        ↓
    LINEAGE
        ↓
    QUALIFICATION
        ↓
    COHERENCE
        ↓
    DRIFT
        ↓
    PARADOX CONTAINMENT
        ↓
    REGIME-QUALIFIED SYNTHESIS
        ↓
    TRUTH STATE
        ↓
    BOUNDED CORRECTION
        ↓
    REVALIDATION

Crosswalk #2 must now attempt to break it.

If DNS cannot be represented without distorting Locational Truth, the architecture must change.

The objective is not to preserve the NTP-derived model.

The objective is to discover which structures survive repeated operational challenge.

---

# 53. Reference

Primary technical reference:

    RFC 5905
    Network Time Protocol Version 4:
    Protocol and Algorithms Specification
    Internet Engineering Task Force

Relevant specification areas include:

    Peer Process
    Clock Filter Algorithm
    Selection Algorithm
    Cluster Algorithm
    Combine Algorithm
    Clock Discipline Algorithm
    Clock-Adjust Process
    Poll Process

---

## Canonical Summary

Crosswalk #1 begins with:

    "What time is it?"

and discovers a deeper operational problem:

    Which reference?

    Which Source?

    Which Observation?

    How far from reference?

    How stable?

    How fresh?

    Which Sources agree?

    What has Drifted?

    What disagreement remains?

    Which Regime determines acceptability?

    How should local state respond?

    When must the question be asked again?

NTP provides one mature operational answer to those questions within Temporal Truth.

RTT does not copy that answer.

It extracts candidate structural mechanisms and exposes them to later crosswalks.

**NTP starts the model.**

**DNS gets the first chance to break it.**
