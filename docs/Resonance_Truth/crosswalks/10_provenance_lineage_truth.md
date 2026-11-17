
# Crosswalk #10 — Supply-Chain Provenance and Lineage Truth

**Module:** Resonance Truth  
**Artifact:** Operational Truth Crosswalk #10  
**Truth Class:** Lineage Truth  
**Reference System:** Software Supply-Chain Provenance / Artifact Attestation  
**Primary RTT Dimensions:** Lineage · Spin · Elec · Regime  
**Supporting RTT Dimensions:** Integrity · Authority · Coherence · Drift · Temp · Paradox  
**Status:** Research Crosswalk / Architecture Challenge  
**Context:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

---

## Purpose

This crosswalk examines software supply-chain provenance and artifact attestation as the tenth operational reference system for the RTT Resonance Truth Service.

The governing question is:

> **Where did this Claim, artifact, or Evidence come from?**

The first nine crosswalks examined:

    NTP
      ↓
    When?

    DNS
      ↓
    Where?

    IAM
      ↓
    Who?

    PKI
      ↓
    Is it intact and qualified?

    Policy / Authorization
      ↓
    May it act?

    Distributed Systems
      ↓
    What state did the system accept?

    Transactional Systems
      ↓
    What transition became committed?

    Desired-State Systems
      ↓
    What should the state be?

    Telemetry
      ↓
    What was actually observed?

Crosswalk #10 asks the question underneath all nine:

    Provenance
      ↓
    Lineage Truth
      ↓
    Where did this come from?

This final crosswalk directly tests concepts that now sit near the center of the emerging Truth-Service architecture:

    EvidenceItem
    Evidence Graph
    Lineage Graph
    ReferenceBasis
    AuthorityRelationship
    transformation
    dependency
    Integrity
    ContextEvidence
    EvidenceGap
    derived Evidence
    recursive Truth
    cycle detection

The central architectural question becomes:

> **Can the Truth Service preserve origin and transformation strongly enough to distinguish known Lineage from incomplete, transformed, copied, derived, conflicting, or circular Lineage?**

---

# 1. Evidence Boundary

The primary reference family for this crosswalk is:

    software supply-chain provenance
    artifact attestation
    build provenance
    dependency relationships
    integrity verification

The bounded reference model focuses on a common provenance structure:

    Source
      ↓
    Build / Transformation
      ↓
    Artifact
      ↓
    Attestation
      ↓
    Distribution / Consumption

Relevant operational concepts include:

- source material
- build inputs
- build process
- transformation
- artifact identity
- artifact digest
- dependency
- attestation
- signer / attester
- build system
- provenance statement
- verification
- distribution
- downstream consumption

The purpose is not to model one software-package ecosystem completely.

The objective is to examine provenance as an operational Truth system.

---

# 2. Evidence Discipline

This crosswalk distinguishes four statement types.

## Provenance Fact

A mechanism explicitly represented by the bounded supply-chain provenance model.

## RTT Interpretation

A structural interpretation introduced through Resonance Truth.

## Candidate Generalization

A mechanism potentially reusable outside Lineage Truth.

## Hypothesis

A proposed abstraction requiring architectural consolidation or implementation testing.

Example:

    Provenance Fact:
      An artifact may be associated with provenance information
      describing source material and transformation.

    RTT Interpretation:
      Artifact identity is connected to origin through structured
      Lineage and Evidence relationships.

    Candidate Generalization:
      Lineage must preserve transformation rather than only ancestry.

    Hypothesis:
      Lineage Graph should become one of the foundational
      structural objects in the generalized Truth Service.

The final architectural decision belongs to the consolidation pass.

---

# 3. Why Provenance Comes Last

Lineage appeared in every previous crosswalk.

## NTP

    reference hierarchy
    Source relationship
    Lineage distance

## DNS

    delegation
    authority path
    alias / resolution path

## IAM

    proofing
    federation
    assertion path

## PKI

    certification path
    trust-chain relationships

## Authority

    delegation
    Authority Lineage

## Distributed State

    replicated log
    accepted-history Lineage

## Transactional Truth

    committed transition history

## Intent Truth

    declaration history
    reconciliation Lineage

## Observational Truth

    trace relationships
    Evidence derivation
    correlation
    transformation

Lineage has therefore already survived nine distinct operational systems.

Crosswalk #10 does not introduce Lineage.

It tests whether Lineage has become sufficiently fundamental to promote into the generalized kernel.

---

# 4. Lineage Truth

The primary Truth Class is:

    Lineage Truth

Its operational question is:

> **Where did this come from?**

A more complete formulation is:

> **Through which identifiable Sources, dependencies, transformations, authorities, and Evidence relationships did this Claim, artifact, or Truth State arrive at its present form?**

Lineage Truth therefore concerns:

- origin
- ancestry
- dependency
- transformation
- derivation
- authorship / production
- attestation
- authority
- integrity
- identity
- ordering
- gaps
- branch points
- merge points
- version
- current artifact relationship

Lineage is not merely:

    who created this?

It may require a graph.

---

# 5. Provenance on Its Own Terms

A simplified software provenance structure is:

    Source Material
          ↓
      Build Inputs
          ↓
    Build / Transformation
          ↓
        Artifact
          ↓
      Attestation
          ↓
      Distribution
          ↓
       Consumer

A more realistic structure may involve:

    Source A ────┐
                 │
    Source B ────┼──► Build Process ───► Artifact X
                 │                          │
    Dependency C ┘                          │
                                            ▼
                                      Attestation
                                            │
                                            ▼
                                       Consumer

This is immediately graph-shaped.

It contains:

    fan-in

and potentially:

    fan-out

The final artifact may derive from multiple upstream entities.

One Source may also contribute to multiple artifacts.

---

# 6. Initial Structural Crosswalk

| Provenance Concept | RTT Truth-Service Interpretation | Status |
|---|---|---|
| Source material | Origin Evidence / Source | Candidate Core |
| Build input | Dependency Evidence | Candidate Core |
| Dependency | Lineage relationship | Candidate Core |
| Build process | Transformation | Candidate Core |
| Build system | Transformer / Evidence producer | Strong Candidate General |
| Artifact | Truth Subject / Materialized object | Strong Candidate General |
| Artifact digest | Integrity Evidence / identity reference | Strong Candidate General |
| Provenance statement | Lineage Assertion | Candidate Core |
| Attestation | Governed Assertion / EvidenceItem | Candidate Core |
| Attester | Assertion Source / Authority Role | Candidate Core |
| Signature | Integrity Evidence | Strong Candidate General |
| Distribution step | Transition / Lineage edge | Candidate General |
| Consumer | Observer / relying party | Strong Candidate General |
| Verification | Qualification | Candidate Core |
| Missing provenance | Evidence / Lineage Gap | Candidate Core |
| Derived artifact | Materialized Transformation Result | Candidate Core |
| Build graph | Evidence / Lineage Graph | Candidate Core |
| Version / generation | Lineage Epoch | Candidate General |

Crosswalk #10 immediately reinforces the architecture's shift from:

    flat Evidence list

toward:

    graph-structured Evidence + Lineage

---

# 7. Source Material → Origin Evidence

Supply-chain provenance begins with upstream material.

RTT interpretation:

    Origin Evidence

The Source may include:

- source artifact
- dependency
- configuration
- build input
- another generated artifact

The important question is:

> **What existed before the current artifact, upon which the current artifact depends?**

This is Lineage in its most direct form.

---

# 8. Origin ≠ Authority

A Source artifact may genuinely be the origin of some content while carrying no authority to make unrelated Claims.

Therefore:

    origin
      ≠
    Authority

This continues the architecture's repeated separation of roles.

A Source may be:

    origin

without being:

    verifier

or:

    authority

or:

    attester

or:

    consumer

The Role abstraction remains strongly justified.

---

# 9. Build Input → Dependency Evidence

An artifact may depend on multiple upstream materials.

RTT interpretation:

    Dependency Evidence

Conceptually:

    Artifact X
      depends_on
        Source A
        Source B
        Dependency C

Dependency is not merely metadata.

It participates in explaining:

    how X came to exist

and potentially:

    why X has particular properties

This strongly validates:

    EvidenceDependency

as a relationship semantic.

---

# 10. Dependency ≠ Provenance Completion

Knowing:

    X depends on Y

does not necessarily establish:

- which version of Y
- how Y was transformed
- whether additional inputs existed
- whether Y itself has known provenance
- when the relationship existed

Therefore:

    dependency list
      ≠
    complete Lineage

Lineage completeness must remain separately represented.

---

# 11. Build Process → Transformation

A build process transforms inputs into outputs.

RTT interpretation:

    Transformation

This is a major Lineage relationship.

Conceptually:

    Inputs
      ↓
    Transformation T
      ↓
    Output Artifact

The Truth Service should preserve:

- what entered
- what transformation occurred
- what emerged
- what system performed the transformation
- when
- under which Regime / configuration where relevant

This strongly validates:

    LineageEdge.transformation

as a generalized capability.

---

# 12. Transformation Is First-Class Lineage

Earlier systems already suggested transformation:

    DNS:
      alias / resolution transformation

    IAM:
      federated assertion / attribute transformation

    Telemetry:
      aggregation / processing

Provenance makes the need explicit.

A path that records only:

    A
      ↓
    B

without:

    transformation:
      T

may lose critical Truth structure.

Therefore:

> **Lineage should preserve meaningful transformation semantics.**

Status:

    CANDIDATE CORE PRINCIPLE

---

# 13. Transformation ≠ Corruption

Crosswalk #9 introduced this distinction.

Supply-chain provenance makes it central.

An artifact may differ from its Sources because:

    transformation was intended

Therefore:

    output differs from input
      ≠
    integrity failure

The question becomes:

> **Does the output correspond to the declared / qualified transformation of the declared / qualified inputs?**

This is substantially richer than:

    bits are different

---

# 14. Transformation Truth

Lineage Truth may therefore contain a sub-question:

> **What transformation produced this object?**

Potential domain result:

    transformation:
      identified
      qualified
      unknown
      contested

No new top-level Truth Class is required.

This remains a Lineage Truth subdimension.

---

# 15. Build System → Transformer Role

The system performing a build acts as:

    Transformer

RTT interpretation:

    Entity Role

This further validates:

    Entity
      +
    Role
      +
    Regime

rather than creating a special core entity for every operational actor.

Possible provenance roles include:

    origin
    dependency
    transformer
    attester
    signer
    distributor
    consumer

Role belongs to a relationship.

---

# 16. Artifact → Truth Subject / Materialized Object

The resulting artifact becomes the object about which a provenance Claim is made.

RTT interpretation:

    Truth Subject

and:

    Materialized Object

This creates an interesting dual role.

The artifact is:

    output materialization

of:

    upstream Source + transformation

and later:

    input / Evidence / dependency

for another downstream artifact.

Therefore:

> **Materializations can become Sources in later Lineage.**

This strongly supports recursive graph structure.

---

# 17. Materialization Can Become Evidence

Earlier architecture:

    Truth State
      ↓
    Materialization

Provenance adds:

    Materialization
      ↓
    later Evidence / Source

Conceptually:

    Source A
       ↓
    Build 1
       ↓
    Artifact B
       ↓
    Build 2
       ↓
    Artifact C

Artifact B is:

    output

and later:

    input

This is another reason the generalized architecture should be composable rather than rigidly layered.

---

# 18. Artifact Digest → Integrity Evidence

A digest can participate in identifying and verifying artifact content.

RTT interpretation:

    Integrity Evidence

However:

    matching digest
      ≠
    complete provenance

It may support:

    artifact identity / integrity relationship

while leaving unanswered:

    who produced it?
    from what?
    under what process?
    using which dependencies?

Again:

    Integrity Truth
      ≠
    Lineage Truth

Truth Classes compose.

---

# 19. Digest Equality ≠ Lineage Equality

Two artifacts may possess identical content while arriving through different operational paths.

Conceptually:

    Artifact A
      digest: D
      Lineage: L1

    Artifact B
      digest: D
      Lineage: L2

Content:

    identical

Lineage:

    different

Therefore:

> **Object equality does not imply provenance equality.**

This extends the recurring:

    stable value
      ≠
    stable structure

finding into explicit provenance.

---

# 20. Provenance Statement → Lineage Assertion

A provenance statement describes origin or transformation relationships.

RTT interpretation:

    Lineage Assertion

This strongly validates:

    Assertion

as an Evidence subtype.

The statement itself is not:

    Lineage automatically accepted

It must still be evaluated.

Conceptually:

    Provenance Assertion
          ↓
    Source / Attester
          ↓
    Integrity
          ↓
    Authority
          ↓
    Evidence
          ↓
    Qualification
          ↓
    Lineage Truth State

---

# 21. Attestation → Governed Assertion

An attestation is a particularly clear Evidence type.

RTT interpretation:

    Governed Assertion

It says, in effect:

> **An identified party asserts something about an artifact or process.**

This is structurally similar to:

    IAM assertion

and:

    PKI signed assertion

Therefore:

    Assertion

has now survived multiple independent crosswalks.

Status:

    CANDIDATE CORE — strongly validated

---

# 22. Assertion ≠ Fact

This distinction must remain explicit.

An attestation may be:

    intact

    correctly signed

and still:

    inaccurate
    incomplete
    out of scope
    stale
    based on incomplete inputs

Therefore:

    valid assertion structure
      ≠
    factual certainty

The Truth Service evaluates:

    assertion
    Source
    authority
    scope
    Lineage
    corroboration
    Regime

before synthesis.

---

# 23. Attester → Source + Authority Role

The attester provides the assertion.

RTT interpretation:

    Source
      +
    Role

Authority depends on:

- what is being asserted
- what the attester is authorized / qualified to attest
- scope
- Regime
- relationship to the transformation
- identity
- integrity

This further validates:

    AuthorityRelationship

as a generalized core structure.

---

# 24. Provenance Authority Is Scoped

An attester may be authoritative regarding:

    build performed by system X

without being authoritative regarding:

    upstream source authorship

or:

    security of dependency Y

or:

    correctness of artifact behavior

Therefore:

> **Authority must remain Claim-scoped.**

This is now one of the strongest generalized findings in the entire series.

---

# 25. Signature → Integrity Evidence

A signed attestation may include Integrity Evidence.

But:

    signature valid
      ≠
    provenance Claim true

The signature may establish:

    this Source signed this assertion

It does not independently establish:

    the assertion accurately describes reality

This repeats PKI's core lesson.

---

# 26. Identity + Integrity + Authority + Lineage

A provenance assertion may require simultaneous evaluation of:

    Identity Truth
      Who signed?

    Integrity Truth
      Is the assertion intact?

    Authority Truth
      May this Source attest this Claim?

    Lineage Truth
      What origin / transformation does it assert?

    Temporal Truth
      When was it valid / produced?

These dimensions compose.

They must not collapse.

---

# 27. Verification → Qualification

Provenance information must be verified / evaluated before operational use.

RTT interpretation:

    Qualification

Potential factors include:

- assertion integrity
- attester identity
- attester authority
- artifact identity
- dependency identity
- transformation relationship
- time
- scope
- missing links
- conflicts

Qualification now clearly applies to:

    Evidence Graph

not merely individual Evidence items.

Status:

    CANDIDATE CORE — strongly validated

---

# 28. Graph Qualification

This introduces:

    Graph Qualification

Question:

> **Does this set of Evidence and relationships form a sufficiently qualified Lineage structure for the intended Claim?**

Potential outcomes:

    complete enough
    partial
    gap present
    contested
    cyclic
    structurally inconsistent
    indeterminate

This may be an application of the existing generalized Qualification Engine.

No separate engine is required yet.

---

# 29. Provenance Graph → Evidence + Lineage Graph

Software provenance is naturally graph-shaped.

Potential structure:

    Source A ──────┐
                   │
    Source B ──────┼──► Transformation T1
                   │          │
    Dependency C ──┘          ▼
                           Artifact D
                              │
                              ▼
                       Transformation T2
                              │
                              ▼
                           Artifact E

This directly validates:

    Evidence Graph

and:

    Lineage Graph

as core architecture.

Status:

    PROMOTION RECOMMENDED

---

# 30. Evidence Graph vs Lineage Graph

After Crosswalk #9 and #10, it is worth asking:

> Are these actually two separate graphs?

Potential answer:

    Evidence Graph
      =
    nodes and relationships among evidentiary objects

    Lineage Graph
      =
    provenance / derivation relationships relevant to those objects

In implementation they may share:

    one graph representation

with typed:

    nodes
    edges
    relationships

Potential generalized name:

    Truth Evidence Graph

However, one supergraph could become too broad.

Recommendation:

    retain conceptual distinction
    allow shared graph infrastructure

Status:

    CONSOLIDATION DECISION REQUIRED

---

# 31. Fan-In

Provenance strongly demonstrates Evidence fan-in.

    Source A
       \
    Source B ──► Build ──► Artifact X
       /
    Source C

The output depends upon multiple inputs.

Therefore:

    one artifact
      ≠
    one parent

Lineage must support:

    many-to-one

relationships.

This is already compatible with graph semantics.

---

# 32. Fan-Out

A Source may also contribute to multiple artifacts.

    Source A
      ├──► Artifact X
      ├──► Artifact Y
      └──► Artifact Z

Therefore Lineage must also support:

    one-to-many

relationships.

Combined:

    fan-in
    fan-out

make a simple chain insufficient.

---

# 33. Shared Dependency

Two artifacts may share the same upstream dependency.

Conceptually:

    Dependency D
      ├──► Artifact A
      └──► Artifact B

If A and B later make similar downstream Claims:

    they are not fully independent

with respect to:

    D-derived properties

This mirrors Telemetry's shared Evidence dependency.

Therefore:

> **Lineage determines independence.**

Status:

    CANDIDATE CORE — strongly confirmed

---

# 34. Provenance and Corroboration

Suppose:

    Artifact A attests Claim X

    Artifact B attests Claim X

If both derive from:

    Source S

their apparent corroboration may be weaker than two independent Lineages.

Therefore Coherence must evaluate:

    common ancestry

not merely:

    number of agreeing downstream artifacts

This reinforces the generalized independence rule.

---

# 35. Copied Evidence

Evidence may be copied across systems.

Conceptually:

    Evidence E
      ↓ copy
    E1
    E2
    E3

Count:

    three records

Independent Evidence:

    one origin

Therefore:

    duplication
      ≠
    corroboration

The Truth Service must preserve origin identity where possible.

---

# 36. Mirrored Evidence

Mirrored content creates the same risk.

A Claim may appear in:

    Site A
    Site B
    Site C

while all three derive from:

    Source S

Without Lineage:

    apparent Source diversity:
      3

With Lineage:

    independent origins:
      1

This provides a powerful generalized motivation for provenance-aware Coherence.

---

# 37. AI-Derived Evidence

The same structural rule applies to AI-generated or AI-transformed Evidence.

Conceptually:

    Source S
      ↓
    Model Transformation M
      ↓
    Derived Statement D

If D later appears as support for S:

    circular Lineage

may emerge.

Therefore:

> **AI transformation does not create an independent Source merely by rephrasing upstream Evidence.**

This follows directly from the generalized Lineage principle.

No special AI exemption is required.

---

# 38. Derived Evidence → Provenance Requirement

Crosswalk #9 established:

    Derived Evidence
      ≠
    Independent Evidence

Crosswalk #10 provides the corresponding requirement:

> **Derived Evidence should preserve provenance to its upstream Evidence and transformation where structurally possible.**

Potential metadata:

    derived_from
    transformed_by
    transformation_version
    produced_at
    authority
    context

Status:

    CANDIDATE CORE

---

# 39. Circular Lineage

Crosswalk #8 introduced circular Truth risk.

Crosswalk #9 introduced circular Evidence corroboration.

Provenance now allows us to state the general problem precisely.

Example:

    Claim A
      supports
    Claim B

    Claim B
      transformed into
    Claim C

    Claim C
      cited as support for
    Claim A

This creates:

    A → B → C → A

The cycle may inflate apparent support without introducing independent grounding.

Therefore:

> **Lineage cycles must be detected and must not automatically increase Evidence independence or Coherence.**

Status:

    CANDIDATE CORE REQUIREMENT

---

# 40. Cycle ≠ Automatically Invalid

Important nuance:

A graph cycle does not automatically mean:

    Evidence false

Some legitimate systems may contain:

    recursive dependencies
    feedback
    reconciliation loops
    repeated evaluations

The problem is not:

    cycle exists

The problem is:

    cycle misrepresented as independent corroboration

Therefore cycle analysis must preserve semantics.

---

# 41. Grounding Depth

A derived Claim may be traced backward through Evidence.

Conceptually:

    Derived Truth State
          ↓
    Parent Truth State
          ↓
    Derived Evidence
          ↓
    Primary Evidence
          ↓
    Reference Basis

Candidate generalized property:

    Grounding Depth

This resembles NTP's:

    Lineage Distance

but is now more general.

Potential measures include:

    hop count
    transformation count
    derived-state depth

However:

    deeper
      ≠
    false

It provides qualification metadata.

Status:

    CANDIDATE GENERAL

---

# 42. Lineage Distance Revisited

Crosswalk #1 introduced:

    Lineage Distance

Crosswalks #2 through #10 progressively showed that one scalar is insufficient.

The final interpretation is:

> **Lineage distance is a derived property of a graph, not necessarily a primitive universal field.**

Potential dimensions:

    hop count
    transformation count
    authority transitions
    derivation depth
    dependency depth

Recommendation:

    retain lineage_distance only as optional derived metadata

not:

    foundational Lineage representation

This is a major consolidation finding.

---

# 43. Missing Provenance → Lineage Gap

Crosswalk #9 established:

    Evidence Gap

Provenance introduces:

    Lineage Gap

Definition:

> **A missing or unavailable relationship required to reconstruct the expected provenance path.**

Examples:

    unknown Source
    undocumented transformation
    missing dependency version
    unknown attester
    missing build step
    unavailable upstream provenance

Status:

    CANDIDATE CORE

---

# 44. Lineage Gap ≠ Evidence of No Transformation

The absence of a recorded transformation does not prove:

    no transformation occurred

Likewise:

    missing provenance
      ≠
    clean provenance

The correct interpretation may be:

    unknown

or:

    incomplete Lineage

This directly parallels Crosswalk #9:

    missing Evidence
      ≠
    Evidence of absence

The principle now generalizes beyond observation.

---

# 45. Known Absence vs Unknown Lineage

There is a difference between:

    qualified claim:
      "No intermediate transformation occurred."

and:

    no recorded intermediate transformation

The first requires sufficient provenance coverage.

The second may simply be:

    Lineage Gap

Therefore:

> **Absence claims require qualified coverage of the relevant structural domain.**

This appears increasingly universal.

---

# 46. Provenance Coverage

Crosswalk #9 introduced:

    ObservationCoverage

Provenance introduces:

    ProvenanceCoverage

Question:

> **Which parts of the expected origin / transformation graph are actually represented?**

Possible domains:

    source coverage
    dependency coverage
    transformation coverage
    attestation coverage
    distribution coverage

Potential generalization:

    Coverage

as a broader Truth-Service concept.

Subtypes:

    ObservationCoverage
    ProvenanceCoverage
    EvaluationCoverage

Status:

    CANDIDATE CORE concept

---

# 47. Coverage as Generalized Truth Metadata

Across systems, the Truth Service increasingly needs to know:

    what was inside the evaluation boundary

and:

    what was not

Coverage may therefore describe:

> **The declared or measured extent over which available Evidence can support conclusions.**

This is broader than telemetry.

Status:

    CANDIDATE CORE

---

# 48. Versioned Provenance

Sources, transformations, dependencies, and build systems may have versions.

Therefore:

    "built from Source S"

may be insufficient without:

    which S?

    which revision?

    which dependency version?

    which process version?

RTT interpretation:

    Regime / Lineage Epoch

This strongly supports versioned ReferenceBasis and Lineage relationships.

---

# 49. Provenance Drift

Potential Lineage Truth Drift dimensions include:

## Source Drift

Origin Source changes.

## Dependency Drift

Dependencies change.

## Transformation Drift

Build/transformation process changes.

## Authority Drift

Attester or build authority changes.

## Integrity Drift

Artifact identity changes.

## Provenance Coverage Drift

More or less Lineage becomes available.

## Semantic Drift

Same labels refer to materially different transformations.

The final artifact may appear similar while provenance Drifts substantially.

---

# 50. Stable Artifact, Changed Provenance

Suppose:

    Artifact digest:
      unchanged

but:

    attestation Source changes

or:

    provenance metadata changes

or:

    transformation claim changes

The artifact content remains identical.

Its asserted Lineage changes.

Therefore:

> **Stable object identity does not imply stable Lineage Truth.**

This is a direct extension of the recurring:

    stable value
      ≠
    stable structure

principle.

---

# 51. Changed Artifact, Preserved Lineage

The inverse may also occur.

A new artifact version may preserve:

    Source family
    build process
    authority
    dependency structure

while:

    artifact identity changes

Therefore Lineage should not assume:

    same provenance
      =
    same artifact

Identity and Lineage remain separate Truth dimensions.

---

# 52. Reproducibility

Provenance raises a powerful question:

> **Can the declared inputs and transformation reproduce the declared output?**

If so, reproducibility may provide additional Evidence supporting the Lineage Claim.

RTT interpretation:

    Independent Transformation Validation

However:

    successful reproduction
      ≠
    proof of every historical detail

It supports:

    relationship compatibility

not necessarily:

    complete original event reconstruction

This distinction matters.

---

# 53. Reproduction vs Provenance

A reproduced artifact may show:

    these inputs + this process can produce this output

It does not necessarily prove:

    this exact historical artifact was produced in precisely this historical execution

Therefore:

    reproducibility
      ≠
    historical provenance identity

Both can strengthen Coherence while remaining separate.

---

# 54. Provenance Coherence

Lineage Truth Coherence may involve compatibility among:

- artifact identity
- claimed Source materials
- dependency relationships
- transformation description
- build system
- attestation
- signatures
- version
- time
- distribution relationships

Coherence means:

> **The provenance graph forms a structurally compatible account under the evaluated Regime.**

Again:

    Coherence
      ≠
    value equality

The generalized definition is now firmly structural.

---

# 55. Provenance Paradox

A Lineage Truth Paradox may arise when:

- two qualified provenance graphs claim mutually incompatible origins
- equally authoritative attestations conflict
- one artifact is claimed to derive from incompatible build histories
- transformations cannot be reconciled under the same Regime

Before Paradox:

    different version?

    different build?

    different artifact?

    different Regime?

    incomplete provenance?

    alternate valid path?

    copied attestation?

    stale claim?

Only unresolved structural incompatibility should become:

    Paradox

---

# 56. Multiple Provenance Paths

An artifact may legitimately have multiple upstream dependency paths.

Therefore:

    multiple paths
      ≠
    contradiction

The architecture must distinguish:

    multi-parent provenance

from:

    incompatible provenance

This repeats a major cross-system lesson:

> **Multiplicity is domain-semantic.**

---

# 57. Alternate Valid Build Paths

If two different qualified transformations can produce the same artifact:

    Path A
      Source X
      Build A
      ↓
      Artifact D

    Path B
      Source Y
      Build B
      ↓
      Artifact D

the existence of both paths is not automatically Paradox.

Question:

> Is the Claim asserting one exclusive historical origin or merely possible derivation?

Claim semantics matter.

This is an important Lineage Truth distinction.

---

# 58. Historical Provenance vs Possible Provenance

## Historical Provenance

Claims:

> **This artifact was actually produced through this path.**

## Possible Provenance

Claims:

> **This artifact can be produced through this path.**

These are different Truth Claims.

Reproducibility typically supports:

    possible provenance

more directly than:

    historical provenance

The Truth Service should preserve Claim semantics.

---

# 59. Attested Provenance vs Observed Provenance

Another important distinction:

## Attested Provenance

A Source asserts a Lineage relationship.

## Observed Provenance

Instrumentation directly observed a transformation/event.

These Evidence types can support each other.

They are not identical.

This strongly validates Evidence typing.

---

# 60. Provenance and Observational Truth

Telemetry may observe:

    build event

while an attestation asserts:

    build event occurred with inputs X

The two may be correlated.

Conceptually:

    Observational Evidence
          +
    Assertion Evidence
          ↓
    Provenance Coherence

This is a concrete example of heterogeneous Evidence synthesis.

---

# 61. Provenance and Integrity Truth

An artifact digest or signature may establish:

    integrity relationship

An attestation may establish:

    claimed provenance relationship

Together:

    Integrity
      +
    Lineage

can strengthen qualification.

Neither replaces the other.

Again:

    Truth Classes compose.

---

# 62. Provenance and Authority Truth

Who may issue provenance Claims?

That is:

    Authority Truth

An attestation Source should be evaluated regarding:

    identity
    role
    scope
    authority
    Regime

Therefore:

    provenance assertion signed
      ≠
    provenance assertion authoritative

This repeats PKI's strongest lesson.

---

# 63. Provenance and Temporal Truth

Lineage relationships may have temporal structure:

    Source revision existed before build

    build produced artifact

    attestation followed build

    release followed artifact creation

The ordering itself may participate in qualification.

Therefore:

    Temporal Truth

and:

    Transactional / Transition Lineage

may reinforce provenance.

---

# 64. Impossible Temporal Lineage

Suppose a provenance graph claims:

    Artifact built at T1

from:

    dependency version created at T2

where:

    T2 > T1

under a Regime where that ordering is impossible.

This introduces:

    temporal Lineage incoherence

The graph may therefore fail qualification even when individual nodes appear valid.

This is a powerful example of graph-level Coherence.

---

# 65. Graph-Level Qualification

Earlier Qualification began with individual Observations.

After ten crosswalks, the generalized model clearly needs:

    node qualification

and:

    relationship qualification

and:

    graph qualification

Potential evaluation:

    EvidenceItem A:
      qualified

    EvidenceItem B:
      qualified

    Edge A→B:
      incompatible

Overall:

    Lineage graph:
      not coherent

Therefore:

> **Qualified nodes do not guarantee a qualified relationship.**

This should become canonical.

---

# 66. Relationship Truth

This leads to a deeper architectural finding.

Many of the Truth Classes are fundamentally about relationships:

    Temporal:
      local state ↔ reference

    Locational:
      name ↔ target

    Identity:
      subject ↔ identity

    Integrity:
      artifact ↔ asserted preserved form

    Authority:
      actor ↔ operation ↔ target

    State:
      participant ↔ accepted state

    Transactional:
      transition ↔ commitment

    Intent:
      desired ↔ current

    Observational:
      observer ↔ evidence ↔ subject

    Lineage:
      source ↔ transformation ↔ artifact

Therefore:

> **Operational Truth appears increasingly relational rather than purely propositional.**

This may be the deepest result of the crosswalk series.

---

# 67. Truth Graph Candidate

The architecture has evolved toward:

    nodes:
      Subjects
      Claims
      Evidence
      Truth States
      Reference Bases
      Actors
      Artifacts
      Transitions

    edges:
      supports
      derives_from
      observed_by
      delegated_by
      transformed_from
      depends_on
      committed_as
      materialized_as
      supersedes
      compensates
      reconstructs_from
      drifted_from
      evaluated_against
      correlates_with

Potential name:

    Truth Graph

However:

    graph storage
      ≠
    Truth architecture automatically

The graph is a representation of relationships.

Qualification semantics remain essential.

Status:

    CANDIDATE ARCHITECTURAL FORM

---

# 68. Graph ≠ Knowledge Graph Requirement

The Truth Service should not automatically become:

    general-purpose knowledge graph

The graph exists to preserve:

    operational Evidence
    Lineage
    qualification relationships
    derived Truth
    evaluation history

Its scope remains bounded.

This protects the initial architectural non-goal:

    not a universal knowledge graph

---

# 69. Provenance Reconstruction

Given sufficient Lineage Evidence, the Truth Service may reconstruct:

    how an artifact arrived here

This resembles:

    Transaction recovery

and:

    Telemetry reconstruction

but the purposes differ.

## Transaction Recovery

Reconstruct operational state.

## Telemetry Reconstruction

Reconstruct bounded activity narrative.

## Provenance Reconstruction

Reconstruct origin and transformation path.

These are distinct uses of:

    Lineage

The core graph can support all three.

---

# 70. Lineage Is Generative and Explanatory

After Crosswalk #7:

    Lineage can reconstruct materialization.

After Crosswalk #9:

    Lineage can reconstruct observational narrative.

After Crosswalk #10:

    Lineage can reconstruct provenance path.

Therefore Lineage serves at least:

    explanatory

    qualifying

    generative

functions.

This strongly establishes it as a core architectural object.

---

# 71. Lineage Completeness

A provenance graph may be:

    complete enough for Use A

but:

    insufficient for Use B

Therefore:

    completeness
      ≠
    universal binary

It is Regime-qualified.

Example:

    basic provenance:
      sufficient for traceability

    high-assurance provenance:
      insufficient for release policy

The architecture should avoid one universal:

    complete = true/false

without scope.

---

# 72. Coverage + Regime → Usability

A generalized relationship now appears:

    Evidence Coverage
          +
    Regime Requirements
          ↓
    Sufficient Evaluation Boundary?

This applies to:

    telemetry
    provenance
    identity proofing
    path validation
    distributed state
    transactions

Potential generalized construct:

    CoverageAssessment

However, this may simply be part of:

    Qualification

rather than a dedicated entity.

Status:

    CANDIDATE RELATION

---

# 73. Provenance Freshness

Lineage information may also become outdated.

Examples include:

    new artifact revision
    new dependency
    new attestation
    revoked signer
    corrected provenance
    superseding build

Therefore:

    provenance accepted once
      ≠
    provenance permanently current

Revalidation remains necessary.

This gives Revalidation its tenth crosswalk.

At this point Revalidation is no longer merely candidate-general.

It is effectively a core invariant.

---

# 74. Provenance Revalidation

Potential triggers include:

    artifact changed
    new attestation
    signer status changed
    authority changed
    dependency information changed
    provenance gap filled
    provenance contradiction discovered
    Regime changed

The old Truth State should remain historically available.

The new Evaluation should produce a new state.

Append-oriented Evaluation history remains strongly supported.

---

# 75. Provenance Correction

Suppose provenance information is discovered to be incomplete or incorrect.

Correction should not necessarily rewrite historical Evidence silently.

A better pattern:

    Prior Provenance Assertion
          ↓
    New Corrective Assertion
          ↓
    New Evaluation
          ↓
    Superseding Lineage Truth State

This parallels:

    compensating transaction

and:

    revised Intent

The historical claim remains visible.

---

# 76. Correction as New Evidence

This suggests another generalized principle:

> **Correction often arrives as new Evidence rather than mutation of old Evidence.**

Examples:

    revised attestation
    compensating transaction
    new telemetry
    updated policy
    new certificate status
    corrected declaration

This strongly supports append-oriented Evidence history.

---

# 77. Provenance Audit

Lineage Truth naturally supports audit.

The system should be able to move backward from:

    current artifact

to:

    transformations

to:

    dependencies

to:

    Sources

to:

    attestations

to:

    authority

to:

    Reference Bases

and identify:

    gaps
    cycles
    conflicts
    transformations

This is essentially the reverse traversal of Truth Lineage.

---

# 78. Forward Lineage

Lineage is also useful forward.

From:

    Source S

the system may ask:

> **What downstream artifacts or Truth States depend on this Source?**

Conceptually:

    Source S
      ├── Artifact A
      ├── Artifact B
      │      └── Artifact C
      └── Derived Truth State D

This supports:

    impact analysis

after:

    Source compromise
    revocation
    correction
    dependency change

---

# 79. Impact Propagation

Suppose:

    Dependency D

becomes:

    revoked / compromised / invalidated

Forward Lineage may identify:

    Artifact A
    Artifact B
    Truth State C

as potentially requiring:

    Revalidation

This yields an important generalized mechanism:

> **Lineage events can trigger downstream Revalidation.**

Status:

    CANDIDATE CORE

---

# 80. Revalidation Propagation

Potential generalized flow:

    Upstream Evidence Change
            ↓
    Lineage Traversal
            ↓
    Dependent Truth States
            ↓
    Mark for Revalidation
            ↓
    New Evaluations

This makes Lineage operational rather than archival.

The crosswalk series has now demonstrated both:

    backward explanation

and:

    forward Revalidation

functions.

---

# 81. Drift Propagation

Upstream Drift may propagate downstream.

Example:

    dependency version changes
      ↓
    artifact provenance changes
      ↓
    downstream artifact relationships change
      ↓
    derived Truth States may require review

This does not mean:

    every downstream Claim becomes false

It means:

    qualification may have changed

Therefore propagation should trigger:

    evaluation

not:

    automatic invalidation

This distinction is critical.

---

# 82. Dependency Change ≠ Automatic Falsehood

The correct generalized behavior is:

    upstream change
      ↓
    affected Lineage identified
      ↓
    Revalidation required
      ↓
    downstream state reevaluated

not:

    upstream change
      ↓
    all descendants = false

This maintains bounded reasoning.

---

# 83. Worked Example — Complete Provenance

## Artifact

    A

## Sources

    S1
    S2

## Dependency

    D1

## Transformation

    Build B1

## Attestation

    Attester T1

## Integrity

    artifact identity matches expected digest

## Authority

    T1 qualified for the asserted provenance scope

## Lineage

    S1 ──┐
         │
    S2 ──┼──► B1 ──► A
         │
    D1 ──┘

## Result

    Truth State:
      operationally_accepted

    domain_result:
      provenance:
        sufficiently_supported

## Architectural Finding

Lineage Truth emerges from qualified relationships, not merely a metadata field containing a Source URL.

---

# 84. Worked Example — Missing Build Step

## Artifact

    A

## Known Lineage

    Source S
      ↓
    [UNKNOWN]
      ↓
    Artifact A

## Result

    Lineage Gap:
      transformation unknown

## Possible Truth State

    degraded
    or
    indeterminate

depending on Regime.

## Incorrect Conclusion

    no transformation occurred

## Architectural Finding

Missing Lineage is not qualified absence.

---

# 85. Worked Example — Conflicting Attestations

## Attestation A

    Artifact X derived from Source S1

## Attestation B

    Artifact X derived from Source S2

Both appear:

    intact
    authoritative
    same artifact
    same Regime

If the Claims are mutually exclusive:

    potential Lineage Paradox

Before Paradox:

    check version
    check build
    check time
    check artifact identity
    check alternate-path semantics

## Architectural Finding

Qualified nodes can still form an incoherent graph.

---

# 86. Worked Example — Shared Dependency

## Artifact A

    depends on D

## Artifact B

    depends on D

Both later display:

    property P

If P plausibly derives from D:

    A
    B

should not automatically count as:

    independent corroboration

## Architectural Finding

Common ancestry reduces Evidence independence.

---

# 87. Worked Example — Copied Attestation

## Original Attestation

    T1

Copies:

    T1a
    T1b
    T1c

Apparent:

    four supporting records

Actual independent origin:

    one attestation

## Architectural Finding

Evidence duplication must be collapsed through Lineage where possible.

---

# 88. Worked Example — Transformation

## Source

    S

## Transformation

    T

## Output

    Artifact A

A differs from S.

## Correct Interpretation

Difference may be expected because:

    T transforms S

## Incorrect Interpretation

    A differs from S
      therefore
    integrity failure

## Architectural Finding

Lineage semantics explain legitimate change.

---

# 89. Worked Example — Same Artifact, Different Provenance

## Artifact A

    digest:
      D

## Provenance Claim 1

    Source:
      S1

## Provenance Claim 2

    Source:
      S2

Content:

    identical

Lineage:

    different

## Architectural Finding

Integrity equality does not resolve Lineage Truth.

---

# 90. Worked Example — Reproducible Artifact

## Historical Claim

    Build B produced Artifact A from Source S.

## Independent Reproduction

    Source S
      +
    transformation equivalent to B
      ↓
    Artifact with matching identity

## Result

This strengthens:

    compatibility of Source + transformation + artifact

It does not independently prove:

    every historical detail of B's original execution

## Architectural Finding

Possible provenance and historical provenance remain distinct.

---

# 91. Worked Example — Circular Derived Claim

## Source Claim

    A

## AI Summary

    B derived from A

## Report

    C cites B

## Later Analysis

    C cited as independent support for A

Lineage:

    A → B → C → A

## Result

    cycle detected

## Independence

    no new independent grounding introduced

## Architectural Finding

Transformation and republication must not create synthetic corroboration.

---

# 92. Worked Example — Upstream Revocation

## Prior State

    Artifact A provenance:
      accepted

## Event

    Attester authority revoked
    or relevant upstream Evidence invalidated

## Correct Response

    identify dependent Lineage
      ↓
    trigger Revalidation

## Incorrect Response

    artifact A automatically false

## Architectural Finding

Upstream change triggers reevaluation, not automatic conclusion.

---

# 93. Worked Example — Corrected Provenance

## Original Assertion

    A derived from S1

## New Evidence

    corrected assertion:
      A derived from S2

## Evaluation

    new Evidence
      ↓
    new Lineage Evaluation
      ↓
    new Truth State

## History

Original assertion remains visible as historical Evidence.

## Architectural Finding

Correction should preserve Lineage rather than rewrite history invisibly.

---

# 94. RTT Dimension Mapping

| RTT Dimension | Provenance Interpretation | General Truth-Service Candidate |
|---|---|---|
| **Resonance** | Sources, artifacts, attestations, and transformations propagate through supply-chain relationships | Evidence and Truth propagate through governed Lineage |
| **Coherence** | Source, artifact, transformation, integrity, and attestation relationships form a compatible provenance graph | Graph-level structural compatibility |
| **Drift** | Source, dependency, transformation, authority, artifact, or coverage changes | Multi-dimensional Lineage Drift |
| **Paradox** | Qualified provenance graphs remain mutually incompatible | Preserved graph-level contradiction |
| **Regime** | Required provenance depth, authority, coverage, integrity, and intended use govern acceptance | Evaluation boundary determines sufficient Lineage |
| **Spin** | Artifact identity and provenance relationships persist through transformations | Lineage continuity |
| **Elec** | Source, dependency, transform, artifact, attester, and consumer remain distinct | Role and relationship separation |
| **Temp** | Builds, attestations, revisions, revocations, releases, and corrections change Lineage over time | Provenance lifecycle and Revalidation |

---

# 95. SET Mapping

## Spin

Lineage Truth expresses Spin through:

- artifact identity
- Source identity
- dependency identity
- transformation relationships
- attestation identity
- persistent provenance

## Elec

Lineage Truth strongly expresses Elec through distinction among:

- Source
- dependency
- transformer
- artifact
- attester
- signature
- distribution step
- consumer
- copied Evidence
- derived Evidence

## Temp

Lineage Truth expresses Temp through:

- Source revision
- build
- transformation
- release
- attestation
- correction
- revocation
- Revalidation

Compactly:

> **Spin preserves the continuity of origin and relationship.**

> **Elec distinguishes who produced, transformed, attested, copied, and consumed.**

> **Temp governs revision, transformation, correction, and renewed qualification.**

---

# 96. Prior Candidate Review — EvidenceItem

Prior status:

    Promotion recommended

Provenance result:

    STRONGLY VALIDATED

Attestations, artifact identities, dependency records, integrity Evidence, and provenance statements all require broader Evidence semantics than Observation alone.

Decision recommendation:

    PROMOTE TO CORE DURING CONSOLIDATION

---

# 97. Prior Candidate Review — Evidence Graph

Prior status:

    Promotion recommended

Provenance result:

    DIRECTLY VALIDATED

Supply-chain provenance is graph-shaped by nature.

Decision recommendation:

    PROMOTE TO CORE

Potential implementation may share infrastructure with Lineage Graph.

---

# 98. Prior Candidate Review — Lineage Graph

Prior status:

    Core mechanism

Provenance result:

    DIRECTLY VALIDATED

Lineage has now survived all ten crosswalks in different forms.

Decision recommendation:

    CONFIRM CORE

Lineage is no longer a candidate peripheral property.

It is foundational.

---

# 99. Prior Candidate Review — ReferenceBasis

Prior status:

    Candidate Core

Provenance result:

    STRONGLY SURVIVES

Lineage qualification may depend upon:

    authority
    attestation policy
    integrity requirements
    Source identity
    provenance requirements

No single external Anchor is universally sufficient.

Decision recommendation:

    PROMOTE ReferenceBasis

while retaining:

    Anchor

as one specialized ReferenceBasis form.

---

# 100. Prior Candidate Review — AuthorityRelationship

Prior status:

    Candidate Core

Provenance result:

    STRONGLY SURVIVES

Attesters and transformers operate within bounded roles and scopes.

Decision recommendation:

    PROMOTE TO CORE

---

# 101. Prior Candidate Review — ContextEvidence

Prior status:

    strongly validated

Provenance result:

    SURVIVES

Build configuration, transformation environment, and artifact context can affect interpretation.

Decision recommendation:

    PROMOTE CONCEPTUALLY

Keep schema lightweight until implementation requires richer context objects.

---

# 102. Prior Candidate Review — EvidenceGap

Prior status:

    Candidate Core

Provenance result:

    STRONGLY SURVIVES

Missing provenance is a Lineage-specific form of Evidence Gap.

Decision recommendation:

    PROMOTE TO CORE

with gap types such as:

    evidence
    lineage
    coverage
    transformation

---

# 103. Prior Candidate Review — ObservationCoverage

Prior status:

    Candidate Core concept

Provenance result:

    GENERALIZES TO COVERAGE

Rather than promoting:

    ObservationCoverage

as the universal object, the broader generalized abstraction may be:

    Coverage

Possible forms:

    ObservationCoverage
    ProvenanceCoverage
    EvaluationCoverage

Decision recommendation:

    PROMOTE COVERAGE concept
    keep domain-specific types extensible

---

# 104. Prior Candidate Review — StateView

Prior status:

    Candidate Core

Provenance result:

    PARTIALLY SURVIVES

A consumer may have a bounded view of available provenance.

However, Lineage Truth does not require StateView universally.

Decision recommendation:

    retain as composable core extension
    not mandatory for every Evaluation

---

# 105. Prior Candidate Review — TruthComparison

Prior status:

    Candidate Core

Provenance result:

    STRONGLY SURVIVES

Provenance Claims may compare:

    claimed vs observed Lineage

    expected vs supplied provenance

    artifact A vs artifact B

    prior vs current provenance

Decision recommendation:

    PROMOTE TO CORE COMPARISON CAPABILITY

---

# 106. Prior Candidate Review — MaterializedTruthState

Prior status:

    Strong Candidate Core

Provenance result:

    SURVIVES

Artifacts themselves are materialized transformation results.

However:

    MaterializedTruthState

should remain a relationship / structured object rather than becoming mandatory in every class.

Decision recommendation:

    PROMOTE AS COMPOSABLE CORE CONCEPT

---

# 107. Prior Candidate Review — AcceptanceRule

Prior status:

    Candidate Core

Provenance result:

    STRONGLY SURVIVES

A provenance graph may need to satisfy:

    authority
    integrity
    depth
    coverage
    transformation
    policy

requirements before being accepted.

Decision recommendation:

    PROMOTE TO CORE

---

# 108. Prior Candidate Review — RegimeEpoch

Prior status:

    strong candidate

Provenance result:

    SURVIVES THROUGH VERSIONING

Provenance versions, artifact generations, policy versions, and build generations support a broader epoch/version concept.

Decision recommendation:

    retain candidate
    avoid mandatory standalone entity until implementation demonstrates need

---

# 109. Prior Candidate Review — Constituted Operational Truth

Prior status:

    strong candidate

Provenance result:

    SURVIVES BUT IS NOT UNIVERSAL

Some provenance Truth is:

    discovered / reconstructed

Some is:

    asserted

Some is:

    constituted through build / release process

Decision recommendation:

    retain as classification
    not core persistent entity

---

# 110. New Candidate — Coverage

Across Telemetry and Provenance, Coverage has become sufficiently general to deserve promotion consideration.

Definition:

> **The bounded extent over which Evidence or Lineage is expected to support a Claim.**

Possible properties:

    coverage_id
    subject_scope
    evidence_types
    lineage_scope
    time_scope
    expected_sources
    known_gaps
    completeness_classification
    regime_id

Status:

    CANDIDATE CORE

---

# 111. New Candidate — Gap

EvidenceGap and LineageGap may be generalized.

Potential object:

    Gap
      ├── gap_type
      ├── expected_relation
      ├── subject_scope
      ├── time_scope
      ├── reason
      ├── impact
      └── status

Gap types:

    evidence
    lineage
    transformation
    coverage
    authority
    context

Status:

    CANDIDATE CORE

This may be cleaner than separate gap objects.

---

# 112. New Candidate — Relationship Qualification

Crosswalk #10 confirms that qualified nodes do not guarantee qualified edges.

Therefore Qualification should apply to:

    EvidenceItem

and:

    Relationship

and:

    Graph / Subgraph

Potential conceptual model:

    QualificationTarget
      ├── node
      ├── edge
      └── graph

Status:

    CANDIDATE CORE PRINCIPLE

Implementation form can remain flexible.

---

# 113. New Candidate — GroundingSet

Recursive Truth requires identifying the independent basis beneath derived Claims.

Potential abstraction:

    GroundingSet

Definition:

> **The set of independent foundational Evidence and Reference Bases upon which a derived Truth State ultimately depends.**

Potential uses:

    independence analysis
    circularity detection
    evidence deduplication
    Coherence assessment

Status:

    CANDIDATE CORE

This may be computed rather than persisted.

---

# 114. GroundingSet and Independence

Example:

    Derived Claim A
      depends on
    E1, E2

    Derived Claim B
      depends on
    E2, E3

Their Grounding Sets overlap:

    E2

Therefore A and B are:

    partially dependent

This generalizes existing:

    source_independence

far more accurately.

Potential independence classification:

    independent
    partially_dependent
    dependent
    unknown

The current model already contains these values.

The calculation mechanism can now become graph-based.

---

# 115. Architecture Refinement #1 — Lineage Becomes Foundational

After ten crosswalks, Lineage has appeared as:

    reference hierarchy
    delegation
    resolution path
    federation
    certification path
    authority chain
    replicated history
    transaction history
    reconciliation history
    trace causality
    supply-chain provenance

This is sufficient evidence to state:

> **Lineage is foundational to the generalized RTT Resonance Truth Service.**

It should remain:

    first-class
    graph-structured
    queryable
    qualification-aware
    historically preserved

This is no longer provisional.

---

# 116. Architecture Refinement #2 — EvidenceItem Becomes Foundational

The original:

    Observation

abstraction has been outgrown.

The crosswalk series now requires:

    EvidenceItem
       ├── Observation
       ├── Assertion
       ├── Declaration
       ├── Attribute
       ├── Status Evidence
       ├── Transition Evidence
       ├── Derived Evidence
       └── Attestation

Therefore:

> **EvidenceItem should become the generalized input object.**

Observation remains one important subtype.

This is a formal consolidation recommendation.

---

# 117. Architecture Refinement #3 — ReferenceBasis Replaces Universal Anchor Assumption

Anchor remains useful for:

    NTP
    DNS
    PKI

But later systems show that reference may instead arise from:

    policy
    protocol
    accepted history
    authorized declaration
    observation contract

Therefore:

    Anchor

should become one specialization of:

    ReferenceBasis

Potential types:

    external_anchor
    governing_policy
    governing_protocol
    accepted_history
    authorized_declaration
    measurement_standard
    trust_configuration

This is a formal consolidation recommendation.

---

# 118. Architecture Refinement #4 — AuthorityRelationship Becomes Core

Authority has appeared repeatedly as:

    scoped
    role-based
    operation-specific
    delegated
    consumer-relative
    time-bounded
    Regime-qualified

Therefore:

    AuthorityRelationship

should become a core object or first-class relationship.

It must not collapse into:

    source.authoritative = true

This is a formal consolidation recommendation.

---

# 119. Architecture Refinement #5 — Qualification Applies to Nodes, Edges, and Graphs

The generalized Qualification Engine should be able to evaluate:

    EvidenceItem

    Source / Entity Role

    AuthorityRelationship

    Lineage Relationship

    Evidence Graph

    Derived Truth State

This is substantially broader than:

    Observation filtering

This is a formal consolidation recommendation.

---

# 120. Architecture Refinement #6 — Coverage and Gaps Become Core Evaluation Metadata

Crosswalk #9 and #10 independently demonstrate:

    missing Evidence

and:

    missing Lineage

must remain visible.

Therefore:

    Coverage
    Gap

should become explicit architecture concepts.

They need not dominate every Evaluation.

They must be available where completeness matters.

---

# 121. Architecture Refinement #7 — TruthComparison Becomes Core Capability

The system increasingly needs comparisons such as:

    Intent vs State

    Expected vs Observed

    Prior vs Current

    Claimed vs Observed Provenance

    Committed vs Materialized

    Source A vs Source B

Therefore:

    TruthComparison

should become a core evaluation capability.

It may produce:

    Drift
    Coherence
    Gap
    domain result

This is a formal consolidation recommendation.

---

# 122. Architecture Refinement #8 — Domain Result Must Separate from Qualification

Ten crosswalks have now repeatedly produced:

    qualified negative results

Examples:

    DNS:
      absent

    IAM:
      authentication failed

    PKI:
      validation rejected

    Authority:
      deny

    State:
      entry uncommitted

    Transaction:
      rolled back

    Intent:
      not converged

    Observation:
      event not established

    Provenance:
      Lineage incomplete

Therefore:

> **Truth-State qualification and domain result must be represented separately.**

This is a formal consolidation recommendation.

---

# 123. Architecture Refinement #9 — Derived Truth Requires Grounding Analysis

Truth States may become inputs to later Truth States.

Derived Evidence may become Evidence for later Claims.

Therefore the architecture must support:

    derivation Lineage
    cycle detection
    GroundingSet analysis
    dependency-aware independence
    inherited limitations

This is now a formal architectural requirement candidate.

---

# 124. Architecture Refinement #10 — The Architecture Is a Graph, Not a Pipeline

The first architecture was largely:

    Claim
      ↓
    Observation
      ↓
    Qualification
      ↓
    Coherence
      ↓
    Truth State

After ten crosswalks, the generalized model is closer to:

    SUBJECTS
       │
       ▼
    CLAIMS
       │
       ├───────────────┐
       │               │
       ▼               ▼
    EVIDENCE ◄────► REFERENCE BASES
       │               │
       ├──────┬────────┤
       │      │        │
       ▼      ▼        ▼
    SOURCE   ROLE   AUTHORITY
       │      │        │
       └──────┼────────┘
              ▼
         LINEAGE GRAPH
              │
       ┌──────┼──────────┐
       │      │          │
       ▼      ▼          ▼
      Q       C          D
       │      │          │
       └──────┼──────────┘
              ▼
           PARADOX
              │
              ▼
         DOMAIN RESULT
              │
              ▼
          TRUTH STATE
              │
       ┌──────┼───────────┐
       │      │           │
       ▼      ▼           ▼
    COMPARE  MATERIALIZE  ACT
       │      │           │
       └──────┼───────────┘
              ▼
          NEW EVIDENCE
              │
              └──────────────► LOOP

where:

    Q = Qualification
    C = Coherence
    D = Drift

The architecture is:

    graph-structured
    recursive
    lifecycle-aware
    feedback-capable

not merely:

    linear

This is perhaps the largest structural conclusion of the crosswalk series.

---

# 125. Architecture Refinement #11 — Not Every Evaluation Uses Every Component

The first architecture suggested one canonical flow.

The completed crosswalk series demonstrates that different Truth Classes emphasize different mechanisms.

Examples:

    NTP:
      Drift + Revalidation

    DNS:
      scope + delegation + freshness

    IAM:
      Subject + evidence + consumer context

    PKI:
      path + Integrity + policy

    Authority:
      relationship + policy decision

    State:
      protocol + agreement + commitment

    Transaction:
      ordered transition + durability

    Intent:
      comparison + reconciliation

    Observation:
      coverage + Evidence gaps + correlation

    Lineage:
      transformation + graph qualification

Therefore the generalized Truth Service should be:

    composable

rather than:

    one mandatory fixed Evaluation pipeline

This is a formal consolidation recommendation.

---

# 126. Architecture Refinement #12 — Relationship Truth Is Central

Across all ten Truth Classes, the apparent "truth value" often belongs to a relationship.

Examples:

    Temporal:
      local ↔ reference

    Locational:
      name ↔ target

    Identity:
      Subject ↔ identity

    Integrity:
      artifact ↔ asserted preserved form

    Authority:
      actor ↔ operation ↔ Target

    State:
      participant ↔ accepted history

    Transactional:
      transition ↔ commitment

    Intent:
      desired ↔ current

    Observational:
      observer ↔ Evidence ↔ Subject

    Lineage:
      Source ↔ transformation ↔ artifact

Therefore the architecture should treat:

> **relationships as evaluable truth-bearing structures**

rather than attaching every Truth condition to one isolated object.

This may be the canonical result of the ten-system study.

---

# 127. Scoring Boundary

The scoring boundary for this crosswalk is:

    System:
      Software Supply-Chain Provenance / Artifact Attestation

    Primary Truth Class:
      Lineage Truth

    Evaluated Scope:
      source material
      dependency relationships
      build / transformation
      artifact identity
      provenance statements
      attestations
      authority
      integrity
      verification
      downstream consumption

    Deferred Scope:
      specific package managers
      specific signing products
      vendor-specific CI/CD systems
      proprietary build platforms
      regulatory policy
      organization-specific release governance

The crosswalk evaluates provenance structure rather than one product ecosystem.

---

# 128. Preliminary Scoring Status

Current status:

    provisional

Likely structural strengths include:

- Reference Basis Quality
- Lineage Visibility
- Evidence Quality
- Regime Awareness
- Drift Detection
- Failure Transparency

Areas requiring careful interpretation include:

- Coherence Detection
- Paradox Handling
- Correction Discipline
- Freshness / Revalidation

Scores should follow explicit evidence.

---

# 129. Provisional Scorecard Template

| Criterion | Score | Delegation | Status |
|---|---:|---|---|
| Reference Basis Quality |  |  | Not yet scored |
| Lineage Visibility |  |  | Not yet scored |
| Evidence Quality |  |  | Not yet scored |
| Coherence Detection |  |  | Not yet scored |
| Drift Detection |  |  | Not yet scored |
| Paradox Handling |  |  | Not yet scored |
| Regime Awareness |  |  | Not yet scored |
| Freshness / Revalidation |  |  | Not yet scored |
| Correction Discipline |  |  | Not yet scored |
| Failure Transparency |  |  | Not yet scored |
| **Total** | **/50** |  | Deferred |

No numeric values should be assigned without:

    evidence
    rationale
    evaluation boundary

---

# 130. Rubric Consolidation Result

After ten crosswalks, two rubric changes have accumulated strong evidence.

## Change 1

    Anchor Quality
      ↓
    Reference Basis Quality

Rationale:

Not all Truth systems derive operational state from an external Anchor.

Some use:

    policy
    protocol
    accepted history
    declaration
    observation contract

## Change 2

    Observation Quality
      ↓
    Evidence Quality

Rationale:

Operational Truth systems use:

    observations
    assertions
    declarations
    attributes
    attestations
    status records
    transition records
    derived Evidence

The revised rubric should be versioned.

Earlier crosswalks should then be reviewed under the updated terminology.

---

# 131. Proposed Scoring Rubric v0.2

Recommended dimensions:

1. Reference Basis Quality
2. Lineage Visibility
3. Evidence Quality
4. Coherence Detection
5. Drift Detection
6. Paradox Handling
7. Regime Awareness
8. Freshness / Revalidation
9. Correction Discipline
10. Failure Transparency

The structural profile remains:

    R-L-E-C-D-P-G-F-X-T

where:

    R = Reference Basis Quality
    L = Lineage Visibility
    E = Evidence Quality
    C = Coherence Detection
    D = Drift Detection
    P = Paradox Handling
    G = Regime Awareness
    F = Freshness / Revalidation
    X = Correction Discipline
    T = Failure Transparency

The rubric should not be formally replaced until the consolidation artifact is created.

---

# 132. Ten-Crosswalk Architecture Check

The initial operational crosswalk series is now complete:

    #1  NTP
        Temporal Truth

    #2  DNS
        Locational Truth

    #3  IAM
        Identity Truth

    #4  PKI
        Integrity Truth

    #5  Policy / Authorization
        Authority Truth

    #6  Distributed Systems
        State Truth

    #7  Transactional Systems
        Transactional Truth

    #8  Desired-State Systems
        Intent Truth

    #9  Telemetry
        Observational Truth

    #10 Supply-Chain Provenance
        Lineage Truth

Across the series, the following generalized structures have survived repeated challenge.

---

# 133. Generalized Kernel — Strong Evidence

## Claim

What is being asserted, requested, or evaluated.

## Truth Class

Which operational relationship is being examined.

## Subject / Target

What the Claim concerns and, where applicable, what is acted upon.

## Regime

The bounded operational context governing interpretation.

## ReferenceBasis

The recognized basis against which qualification is evaluated.

## EvidenceItem

Typed input relevant to the Claim.

## Evidence Graph

Relationships among Evidence items.

## Entity / Participant

Actors, Sources, Observers, Consumers, and systems participating in the relationship.

## Role

Contextual function performed by an Entity.

## AuthorityRelationship

Scoped, role-specific, Regime-qualified authority.

## Lineage Graph

Origin, delegation, derivation, transition, transformation, and dependency relationships.

## Qualification

Determination of suitability for Evaluation.

## AcceptanceRule

The governing condition for operational acceptance.

## Coherence

Domain-semantic structural compatibility.

## Drift

Displacement between relevant Truth-bearing states or structures.

## Paradox

Qualified incompatibility that remains after scope, class, and Regime resolution.

## Domain Result

The domain-native outcome of Evaluation.

## Truth-State Qualification

The operational usability state of that result.

## TruthComparison

Evaluation of relationships among Truth States.

## Coverage

The bounded extent over which Evidence supports conclusions.

## Gap

Missing expected Evidence, Lineage, transformation, context, or coverage.

## MaterializedTruthState

Operational materialization of accepted Truth.

## Correction / Action Policy

Governed downstream response.

## Revalidation

Renewed challenge of prior accepted Truth.

## Immutable History

Preservation of previous Evidence, Evaluations, Truth States, and corrections.

---

# 134. Generalized Kernel — Strong Principles

The ten crosswalks support the following principles strongly.

    Evidence ≠ Truth State

    Observation ≠ Reality

    Identity ≠ Authority

    Authority ≠ Correctness

    Authority ≠ Capability

    Intent ≠ State

    Proposal ≠ Commitment

    Commitment ≠ Materialization

    Commitment ≠ Finality

    Decision ≠ Enforcement

    Recovery ≠ Revalidation

    Revalidation ≠ Reconciliation

    Negative Domain Result ≠ Evaluation Failure

    Evidence Absence ≠ Qualified Absence

    Derived Evidence ≠ Independent Evidence

    Integrity ≠ Operational Acceptance

    State Equality ≠ Lineage Equality

    Stable Value ≠ Stable Structure

    Multiple Values ≠ Paradox

    Difference ≠ Contradiction

    Correction ≠ Historical Erasure

These distinctions now have support across multiple operational systems.

---

# 135. Generalized Kernel — Graph Principles

The completed series also supports several graph-specific principles.

## Principle 1

Evidence relationships matter.

## Principle 2

Lineage can contain:

    fan-in
    fan-out
    branching
    merging
    transformation
    dependency

## Principle 3

Derived Evidence inherits upstream limitations.

## Principle 4

Common ancestry reduces independence.

## Principle 5

Graph cycles must not automatically create corroboration.

## Principle 6

Qualified nodes do not imply qualified relationships.

## Principle 7

Lineage changes may matter even when value does not.

## Principle 8

Forward Lineage can identify downstream Revalidation impact.

## Principle 9

Backward Lineage can explain current Truth.

## Principle 10

Lineage may be explanatory, qualifying, and generative.

These principles should shape the architecture consolidation.

---

# 136. Candidate Core Model After Ten Crosswalks

The consolidated conceptual model now appears closer to:

    ENTITY / SUBJECT / TARGET
              │
              ▼
            CLAIM
              │
              ▼
         TRUTH CLASS
              │
              ▼
        INTENDED USE
              │
              ▼
            REGIME
              │
              ▼
       REFERENCE BASIS
              │
              ▼
    AUTHORITY RELATIONSHIPS
              │
              ▼
        EVIDENCE GRAPH
              │
              ▼
         LINEAGE GRAPH
              │
       ┌──────┼─────────┐
       │      │         │
       ▼      ▼         ▼
    COVERAGE  GAPS   CONTEXT
       │      │         │
       └──────┼─────────┘
              ▼
        QUALIFICATION
              │
              ▼
       ACCEPTANCE RULE
              │
       ┌──────┼────────┐
       │      │        │
       ▼      ▼        ▼
    COHERENCE DRIFT  PARADOX
       │      │        │
       └──────┼────────┘
              ▼
         DOMAIN RESULT
              │
              ▼
         TRUTH STATE
              │
       ┌──────┼────────────┐
       │      │            │
       ▼      ▼            ▼
    COMPARE MATERIALIZE   ACT
       │      │            │
       └──────┼────────────┘
              ▼
        NEW EVIDENCE
              │
              ▼
         REVALIDATION
              │
              └──────────────► LOOP

This is no longer best understood as a simple pipeline.

It is a:

    bounded operational Truth Graph

with composable Evaluation mechanisms.

---

# 137. The Observer Has Survived

One significant result deserves explicit recognition.

The Observer first appeared subtly in:

    NTP

became clearer in:

    DNS

became operationally central in:

    IAM / PKI

became participatory in:

    Distributed State

became comparative in:

    Intent Truth

and became unavoidable in:

    Telemetry

Provenance adds the consumer / verifier perspective.

Therefore:

> **Observer position belongs in the generalized architecture.**

It may be represented through:

    Entity
    Role
    StateView
    Regime
    ContextEvidence

rather than one mandatory standalone Observer entity.

That keeps the model thin while preserving the concept.

---

# 138. The Anchor Has Changed

Crosswalk #1 began with:

    Truth Anchor

After ten systems, the more general concept is:

    ReferenceBasis

An external Anchor remains useful.

But operational Truth may also rely on:

    policy
    protocol
    accepted history
    authority relationship
    authorized declaration
    observation contract
    provenance requirement

Therefore:

> **Anchor survives as a specialized ReferenceBasis, not as the universal shape of reference.**

This is a successful example of the crosswalk series changing its own initial architecture.

---

# 139. Observation Has Changed

Crosswalk #1 began with:

    Observation

After ten systems, the generalized concept is:

    EvidenceItem

Observation survives as one subtype.

Other Evidence forms include:

    Assertion
    Declaration
    Attribute
    Attestation
    Transition Evidence
    Status Evidence
    Derived Evidence

Therefore:

> **Observation survives, but Evidence becomes the generalized architecture boundary.**

---

# 140. Coherence Has Changed

Crosswalk #1 could tempt a simple interpretation:

    Sources agree
      ↓
    Coherence

After ten systems:

    Coherence
      =
    domain-semantic structural compatibility
    among qualified Evidence and relationships
    under a declared Regime

Coherence may involve:

    agreement
    compatibility
    correlation
    historical consistency
    relationship validity
    graph consistency
    reconstruction

Therefore:

> **Coherence is structural, not merely numerical agreement.**

---

# 141. Drift Has Changed

Crosswalk #1 began with:

    numeric temporal offset

After ten systems Drift includes:

    value
    state
    source
    lineage
    semantic
    authority
    policy
    regime
    instrumentation
    coverage
    context
    transformation

Therefore:

> **Drift is generalized displacement between truth-bearing relationships, not merely numeric error.**

Numeric Drift remains useful where meaningful.

It is not mandatory.

---

# 142. Paradox Has Changed

Crosswalk #1 introduced unresolved Source disagreement.

After ten systems, the architecture has learned:

    multiplicity
      ≠
    Paradox

    different Truth Classes
      ≠
    Paradox

    different Regimes
      ≠
    Paradox

    stale state
      ≠
    Paradox

    local vs committed state
      ≠
    Paradox

    missing Evidence
      ≠
    Paradox

Paradox should be reserved for:

> **qualified structural incompatibility that remains after domain, Truth-Class, Lineage, temporal, and Regime distinctions have been applied.**

This is a substantially stronger definition.

---

# 143. Revalidation Has Survived Everything

NTP:

    polling

DNS:

    TTL / expiry

IAM:

    authentication / credential lifecycle

PKI:

    validity / revocation

Authority:

    policy / attribute change

Distributed State:

    epoch / leadership / membership change

Transactions:

    settlement / recovery context

Intent:

    recurring reconciliation

Telemetry:

    new / delayed Evidence

Provenance:

    new attestations / upstream changes

Therefore:

> **Revalidation is a generalized core Truth-Service invariant.**

Operational Truth ages, changes, or gains new Evidence.

Acceptance is not permanent by default.

---

# 144. Correction Has Changed

Crosswalk #1 introduced:

    clock adjustment

After ten systems Correction includes:

    local adjustment

    cache replacement

    access restriction

    replica reconciliation

    compensating transaction

    state reconciliation

    new Evidence

    corrected attestation

Therefore:

> **Correction is a governed response to changed Truth relationships, not one universal mutation operation.**

The action taxonomy should remain extensible.

---

# 145. Lineage Has Become the Spine

The crosswalk began with:

    Lineage

as one dimension among several.

After ten operational systems, Lineage connects:

    ReferenceBasis
    Evidence
    Authority
    transformations
    Claims
    Truth States
    comparisons
    corrections
    materializations
    Revalidations

It can answer:

    Where did this come from?

    What depends on it?

    What changed?

    Who transformed it?

    Which Truth States used it?

    Which later Claims derive from it?

    Which downstream states require Revalidation?

Therefore:

> **Lineage is not merely one Truth Class. Lineage Truth is also the structural spine through which the other Truth Classes remain explainable.**

This does not eliminate Lineage Truth as a Truth Class.

It explains why it appears everywhere.

---

# 146. Final Crosswalk Evaluation

Crosswalk #10 does not break the emerging architecture.

Instead, it reveals which pieces were actually structural.

The strongest result is:

> **Operational Truth is best represented not as a value with confidence, but as a qualified relationship embedded in Evidence, Regime, Lineage, and lifecycle.**

A practical Truth Service therefore needs to preserve enough structure to answer:

    What is the Claim?

    What kind of Truth is involved?

    What Evidence exists?

    What is missing?

    Where did the Evidence come from?

    What was transformed?

    Which Sources are actually independent?

    What Reference Basis governs qualification?

    Who had authority?

    Which Regime applies?

    What coheres?

    What Drifted?

    What remains incompatible?

    What domain result was established?

    How qualified is that result?

    What became materialized?

    What downstream action occurred?

    What must now be Revalidated?

Those questions form the generalized kernel.

---

# 147. Formal Consolidation Trigger

The ten operational crosswalks are now complete.

The next architecture phase should be:

    MODEL CONSOLIDATION

The consolidation pass should review:

    architecture/
      truth_service_architecture.md
      truth_service_components.md
      truth_service_data_model.md
      truth_service_api.yaml
      implementation_roadmap.md

and:

    schemas/

against the completed crosswalk evidence.

Recommended consolidation targets include:

    Observation
      → EvidenceItem generalization

    Anchor
      → ReferenceBasis generalization

    AuthorityRelationship
      → promotion

    Evidence Graph
      → promotion

    Lineage Graph
      → confirmation as foundational

    Coverage
      → promotion

    Gap
      → promotion

    TruthComparison
      → promotion

    Domain Result
      → separation from Truth-State qualification

    MaterializedTruthState
      → composable core concept

    AcceptanceRule
      → promotion

    observer / role semantics
      → explicit review

    derived-Truth cycle detection
      → architecture requirement

    inherited limitation propagation
      → architecture requirement

The consolidation pass should simplify where possible.

It should not merely add every new noun discovered during the crosswalk series.

---

# 148. Promotion Test

Every consolidation candidate should still pass the existing promotion rule.

Promote when the mechanism:

1. appears across multiple Truth Classes
2. has independent structural meaning
3. affects qualification or interpretation
4. has lifecycle implications
5. prevents information loss
6. improves explanation or Revalidation
7. cannot be represented cleanly by an existing generalized object

Otherwise:

    keep as relationship
    keep as attribute
    keep as domain extension
    keep as derived value

This should keep the generalized kernel thin.

---

# 149. Canonical Lineage Truth Statement

> **Lineage Truth is the Regime-qualified account of origin, dependency, transformation, authority, derivation, and transition through which a Claim, Evidence item, artifact, or Truth State arrived at its present form.**

Lineage Truth does not require every path to be complete.

It requires the system to preserve:

    what is known

    what is asserted

    what is observed

    what was transformed

    what depends on what

    what is missing

    what conflicts

    what was copied

    what was derived

    what remains independently grounded

without inventing missing relationships to make the graph appear complete.

---

# 150. Canonical Crosswalk Finding

Crosswalk #10 produces the closing finding of the first operational truth study:

> **Truth without Lineage may still be usable, but the conditions under which it became usable become progressively harder to inspect, challenge, compare, reproduce, correct, or Revalidate.**

The ten-system sequence began with:

    What time is it?

and ended with:

    How do you know where that answer came from?

That progression matters.

NTP taught us that operational state can Drift.

DNS taught us that authority has scope.

IAM taught us that identity is relational.

PKI taught us that integrity is not sufficient for operational trust.

Policy taught us that authority belongs to a relationship.

Distributed systems taught us that accepted state can be constituted through agreement.

Transactional systems taught us that commitment and history matter.

Desired-state systems taught us that Truth can differ from Truth without contradiction.

Telemetry taught us that Observation is bounded and missing Evidence is not absence.

Provenance teaches us that none of those answers should become detached from their origin, transformation, dependencies, or Evidence path.

That gives Resonance Truth its first generalized operational model.

---

# 151. References

Primary reference family:

    software supply-chain provenance
    artifact attestation
    build provenance
    dependency Lineage
    integrity verification

The bounded provenance model used by this crosswalk examines relationships among:

    Source material
    dependencies
    build / transformation
    artifact
    attestation
    authority
    integrity
    distribution
    consumer

The exact implementation mechanisms vary among supply-chain systems.

This crosswalk therefore focuses on structural provenance relationships rather than assuming one universal software-supply-chain protocol.

RTT terminology, Lineage Truth, Evidence Graph, ReferenceBasis, AuthorityRelationship, Coverage, Gap, GroundingSet, Drift categories, cycle analysis, Revalidation propagation, and the proposed generalized Truth-Service kernel remain the analytical contribution of Resonance Truth.

---

## Canonical Summary

Crosswalk #1 asked:

    When?

Crosswalk #2 asked:

    Where?

Crosswalk #3 asked:

    Who?

Crosswalk #4 asked:

    Is it intact?

Crosswalk #5 asked:

    May it act?

Crosswalk #6 asked:

    What state did the system accept?

Crosswalk #7 asked:

    What became committed?

Crosswalk #8 asked:

    What should the state be?

Crosswalk #9 asked:

    What did we actually observe?

Crosswalk #10 asks:

    Where did all of that come from?

And that final question folds backward through the entire series.

    Which reference?

    Which Source?

    Which Observer?

    Which Evidence?

    Which authority?

    Which transformation?

    Which dependency?

    Which transition?

    Which Regime?

    Which history?

    Which gaps?

    Which derived Claims?

    Which apparently independent Sources
    actually share an ancestor?

The resulting architecture no longer looks like:

    Claim
      ↓
    true / false

It looks like:

    Claim
      ↓
    qualified relationships
      ↓
    Evidence Graph
      ↓
    Lineage
      ↓
    Regime
      ↓
    Coherence + Drift + Paradox
      ↓
    Domain Result
      ↓
    Truth-State Qualification
      ↓
    Action / Materialization
      ↓
    New Evidence
      ↓
    Revalidation

And Lineage runs through the entire cycle.

**NTP gave Truth a reference.**

**DNS gave it scope.**

**IAM gave it identity relationships.**

**PKI gave it an evidence chain.**

**Policy gave it bounded authority.**

**Distributed systems gave it agreed state.**

**Transactions gave it committed history.**

**Desired-state systems gave it intention and feedback.**

**Telemetry gave it an observer and an evidence boundary.**

**Provenance gives the whole structure memory.**

The first crosswalk cycle is complete.

**Up next: consolidate what survived.**
