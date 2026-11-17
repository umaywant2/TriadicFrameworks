<img width="1194" height="672" alt="Resonance_Truth_crosswalks_03_iam_identity_truth_" src="https://github.com/user-attachments/assets/cc164b1b-e13c-4b6c-a8a2-7747d3a5c8f9" />

# Crosswalk #3 — IAM and Identity Truth

**Module:** Resonance Truth  
**Artifact:** Operational Truth Crosswalk #3  
**Truth Class:** Identity Truth  
**Reference System:** Identity and Access Management (IAM) / Digital Identity Systems  
**Primary RTT Dimensions:** Spin · Coherence · Regime · Lineage  
**Supporting RTT Dimensions:** Elec · Temp · Drift · Authority · Paradox  
**Status:** Research Crosswalk / Architecture Challenge  
**Context:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

---

## Purpose

This crosswalk examines Identity and Access Management and digital identity systems as the third operational reference system for the RTT Resonance Truth Service.

The governing question is:

> **Who or what is this?**

Crosswalk #1 examined:

    NTP
      ↓
    Temporal Truth
      ↓
    When?

Crosswalk #2 examined:

    DNS
      ↓
    Locational Truth
      ↓
    Where?

Crosswalk #3 moves into:

    IAM
      ↓
    Identity Truth
      ↓
    Who?

This transition significantly changes the problem.

Time and naming systems can often expose reference relationships directly.

Identity introduces relationships among:

- subject
- identity
- evidence
- credentials
- authentication
- identity proofing
- identity provider
- credential service provider
- relying party
- federation
- assertions
- assurance
- lifecycle
- revocation
- context

The central architectural question becomes:

> **Is identity an intrinsic property of an entity, or is operational Identity Truth established through a qualified relationship among subject, evidence, authority, observer, and Regime?**

---

# 1. Evidence Boundary

Primary grounding for this crosswalk is the NIST Digital Identity Guidelines, Revision 4 family.

Relevant reference areas include:

    NIST SP 800-63-4
    Digital Identity Guidelines

    NIST SP 800-63A-4
    Identity Proofing and Enrollment

    NIST SP 800-63B-4
    Authentication and Authenticator Management

    NIST SP 800-63C-4
    Federation and Assertions

The NIST model explicitly distinguishes major digital identity functions including:

    identity proofing
    authentication
    federation

This distinction is useful because the RTT crosswalk should not collapse them into one generic:

    identity check

The crosswalk should preserve their separate operational roles.

---

# 2. Evidence Discipline

This document distinguishes four statement types.

## IAM / Digital Identity Fact

A mechanism explicitly represented in the bounded reference material.

## RTT Interpretation

A structural interpretation introduced by Resonance Truth.

## Candidate Generalization

A mechanism potentially reusable beyond Identity Truth.

## Hypothesis

A proposed abstraction requiring evidence from later crosswalks.

Example:

    Digital Identity Fact:
      Federation allows identity-related assertions to cross
      separately administered system boundaries.

    RTT Interpretation:
      Identity Truth may propagate through Authority and Lineage.

    Candidate Generalization:
      Assertions should preserve Source, audience, scope,
      and transformation relationships.

    Hypothesis:
      Assertion should become a first-class generalized
      Truth-Service entity.

The final claim remains provisional.

---

# 3. Why IAM Comes Third

DNS introduced several architectural candidates that identity systems can directly challenge.

Crosswalk #2 suggested:

    Authority Scope
    Authority Lineage
    Observer Context
    delegated authority
    explicit absence
    Source roles
    materialized local state
    domain-semantic Coherence

IAM provides a strong next test because Identity Truth depends heavily on relationships among multiple operational actors.

A typical identity relationship may involve:

    Subject
       ↓
    Evidence
       ↓
    Proofing
       ↓
    Identity Record
       ↓
    Credential / Authenticator
       ↓
    Authentication
       ↓
    Assertion
       ↓
    Relying Party

The entity answering:

> **Who is this?**

may therefore not be the subject itself.

Nor is the answer necessarily permanent, universal, or valid for every relying party.

---

# 4. Identity Truth

The primary Truth Class is:

    Identity Truth

Its operational question is:

> **Who or what is this?**

This question must be scoped carefully.

Operational digital identity does not necessarily answer:

> **What is the complete real-world identity of this entity?**

A digital identity may instead establish a usable identity relationship within a particular service context.

Therefore the generalized Identity Truth question becomes:

> **Within this Regime and for this intended use, what identity relationship is sufficiently supported for this subject?**

That formulation preserves:

- context
- evidence
- authority
- assurance
- audience
- lifecycle

without requiring identity to become a universal intrinsic label.

---

# 5. Identity Is Contextual

A major contribution from the digital identity reference model is the distinction between:

    person / entity

and:

    digital identity in an operational context

A person may possess more than one digital identity.

Therefore:

    Entity
      ≠
    one universal digital identity

The same subject may legitimately participate in different identity relationships across:

- systems
- organizations
- trust domains
- pseudonymous contexts
- roles
- federation boundaries

This immediately reinforces:

    Regime

as a major Identity Truth dimension.

---

# 6. Initial Structural Crosswalk

| IAM / Digital Identity Concept | RTT Truth-Service Interpretation | Status |
|---|---|---|
| Subject | Truth subject | Strong Candidate General |
| Digital identity | Regime-qualified identity state | Strong Candidate General |
| Identity evidence | Observation / supporting evidence | Strong Candidate General |
| Identity proofing | Evidence qualification | Strong Candidate General |
| Enrollment | Identity-state establishment | Candidate General |
| Credential | Evidence-bearing relationship | Candidate General |
| Authenticator | Authentication mechanism / evidence Source | Domain-Specific / Candidate |
| Authentication | Current identity-relationship qualification | Strong Candidate General |
| Credential Service Provider | Authority / identity Source | Candidate General |
| Identity Provider | Assertion Source / Authority | Candidate General |
| Assertion | Signed or governed identity Claim | Strong Candidate General |
| Relying Party | Observer / consumer | Strong Candidate General |
| Federation | Cross-Regime identity propagation | Strong Candidate General |
| Assurance level | Qualification requirement / Regime parameter | Strong Candidate General |
| Credential lifecycle | Freshness / state lifecycle | Candidate General |
| Revocation | Qualification-state transition | Strong Candidate General |

IAM introduces a particularly important new distinction:

    SUBJECT
       ≠
    IDENTITY CLAIM
       ≠
    CREDENTIAL
       ≠
    AUTHENTICATION EVENT
       ≠
    ASSERTION
       ≠
    RELYING-PARTY ACCEPTANCE

That separation will be central to this crosswalk.

---

# 7. Subject → Truth Subject

## Digital Identity View

Identity systems operate on a subject whose identity relationship is being established or evaluated.

## RTT Interpretation

Crosswalk #2 suggested that Claim subjects may deserve stronger structural representation.

IAM strengthens that conclusion.

The generalized entity becomes:

    Truth Subject

A Truth Subject is:

> **The entity about which the Claim is being made.**

Examples may later include:

    person
    service
    device
    artifact
    account
    organization
    process

## Architectural Contribution

The current model primarily embeds the subject within:

    Claim.statement

IAM suggests this may eventually become insufficient.

Potential future field:

    Claim.subject_id

or:

    Claim.subject

Status:

    CANDIDATE_GENERAL — strengthened

No core schema change should occur until additional crosswalk evidence supports promotion.

---

# 8. Subject ≠ Identity

This distinction is foundational.

The subject is:

    what the Claim is about

An identity is:

    an operational representation associated with that subject

Therefore:

    Subject
      ↓
    Identity Relationship

not:

    Subject
      =
    Identity Record

This protects the architecture from treating database representations as the entities themselves.

It also allows:

    one Subject
      ↓
    multiple legitimate digital identities

under different Regimes.

---

# 9. Digital Identity → Regime-Qualified Identity State

The NIST digital identity model explicitly places identity in service context.

RTT interpretation:

    Digital Identity
         ↓
    Regime-Qualified Identity State

Conceptually:

    Subject
      +
    Identity Evidence
      +
    Authority
      +
    Context
      +
    Assurance Requirement
        ↓
    Operational Identity State

This suggests:

> **Identity Truth is relational rather than purely intrinsic.**

The identity relationship is established strongly enough for a particular operational purpose.

---

# 10. Identity Evidence → Observation

Identity proofing introduces evidence used to support an identity relationship.

RTT interpretation:

    Identity Evidence
         ↓
    Observation / Supporting Evidence

This reinforces the NTP- and DNS-derived distinction:

    evidence
      ≠
    Truth State

Multiple pieces of identity evidence may participate in a proofing process.

The Truth Service should preserve:

- evidence Source
- collection context
- freshness
- integrity
- relationship to subject
- transformation
- qualification result

## Candidate Generalization

The Observation abstraction survives Identity Truth strongly.

However, IAM suggests that an Observation may need a relationship to:

    subject

in addition to:

    Claim

Status:

    CANDIDATE_GENERAL — strengthened

---

# 11. Identity Proofing → Evidence Qualification

Identity proofing establishes another strong example of qualification.

Conceptually:

    Applicant / Subject
          ↓
    Evidence
          ↓
    Verification / Validation
          ↓
    Qualified Identity Relationship

RTT interpretation:

    Qualification Engine

The key architectural rule remains:

    evidence presented
          ≠
    evidence qualified

This is structurally parallel to:

    NTP sample received
          ≠
    sample selected

and:

    DNS answer available
          ≠
    answer qualified for current use

Identity Truth therefore strongly supports:

> **Qualification as a generalized operational truth mechanism.**

---

# 12. Proofing and Authentication Are Different

Identity systems introduce a major architectural separation:

    identity proofing
        ≠
    authentication

Proofing asks roughly:

> **What identity relationship can be established for this subject?**

Authentication asks roughly:

> **Is this current claimant sufficiently associated with the previously established digital identity?**

These should remain separate in the RTT architecture.

Conceptually:

    Establish Identity State
             ↓
    Later Authentication Event
             ↓
    Revalidate Current Identity Relationship

This resembles:

    initial qualification
             ↓
    subsequent Revalidation

but the semantics are domain-specific.

---

# 13. Enrollment → Identity-State Establishment

Enrollment follows successful establishment of an operational identity relationship.

RTT interpretation:

    Identity Truth-State Establishment

The architecture can interpret enrollment as movement from:

    candidate identity Claim

toward:

    established identity state

within a specific Regime.

This resembles a Truth-State transition.

However:

    enrollment status
      ≠
    generic TruthStatus

Enrollment remains an identity-domain lifecycle mechanism.

Status:

    DOMAIN_SPECIFIC with generalized lifecycle relevance

---

# 14. Credentials → Evidence-Bearing Relationships

Credentials create a difficult modeling question.

A credential is not necessarily:

    the Subject

nor:

    the identity itself

nor:

    the current authentication result

Instead, it participates in the relationship among:

    Subject
    Digital Identity
    Authentication
    Authority
    Relying Party

RTT interpretation:

    Evidence-Bearing Relationship

Potential generalized lesson:

> **Truth systems may contain durable evidence objects that can be presented repeatedly without themselves being Truth States.**

This may later matter to:

- PKI certificates
- signed attestations
- supply-chain provenance

Status:

    CANDIDATE_GENERAL

---

# 15. Authentication → Current Identity Qualification

Authentication is an especially important operational process.

RTT interpretation:

    current identity qualification

Conceptually:

    Established Identity
         +
    Current Authentication Evidence
         +
    Regime Requirements
           ↓
    Presently Qualified Identity Relationship

This reinforces:

> **Previously established truth does not automatically remain sufficient for every future use.**

The relationship requires current qualification under applicable conditions.

That is a strong analogue to Revalidation.

---

# 16. Authentication Is Not Identity Proofing

The distinction matters because the architecture must not infer:

    successful authentication
        =
    complete proof of real-world identity

The authenticated entity may be associated with:

- a verified identity
- a pseudonymous identity
- an account
- another service-context identity

depending on the governing Regime.

Therefore:

    authentication strength

and:

    identity proofing strength

must remain separable.

This reinforces multidimensional qualification.

---

# 17. Identity Provider → Assertion Source

Federated systems introduce an identity provider as a Source of assertions used by relying parties.

RTT interpretation:

    Assertion Source

This strengthens the Source-role problem introduced by DNS.

Potential roles now include:

    evidence Source
    proofing authority
    credential Source
    authentication Source
    assertion Source
    relying consumer

The same actor may hold more than one role.

Different actors may hold each role independently.

## Architectural Challenge

The generic:

    Source

entity survives,

but IAM makes Source role increasingly difficult to leave implicit.

Status:

    ARCHITECTURE_CHALLENGE

Potential future structure:

    SourceRole

should remain deferred until PKI and Authority Truth provide additional evidence.

---

# 18. Credential Service Provider → Authority / Source

Digital identity systems may include credential service providers responsible for lifecycle processes related to digital identity and authentication.

RTT interpretation:

    Authority / Source

But DNS has already taught us:

    Source
      ≠
    Authority

Therefore the correct model may be:

    Entity
      +
    Role
      +
    Scope
      +
    Regime
      =
    Authority Relationship

IAM strongly reinforces the DNS-derived principle:

> **Authority should be modeled relationally rather than as an intrinsic permanent Source property.**

Status:

    CANDIDATE_GENERAL — strengthened

---

# 19. Assertion → Identity Claim

Federation introduces assertions.

An assertion is especially interesting because it resembles a portable Truth Claim.

Conceptually:

    Identity Provider
          ↓
    Assertion
          ↓
    Relying Party

RTT interpretation:

    Identity Claim
      +
    Source
      +
    Audience
      +
    Regime
      +
    Lifecycle

This introduces an important candidate concept:

    Assertion

as a truth-bearing message distinct from:

    Observation

An Observation says:

> **This was observed.**

An assertion says:

> **This Source declares this state under these conditions.**

Those are not necessarily identical.

---

# 20. Assertion vs Observation

This may be one of Crosswalk #3's most important challenges.

The initial Truth Service heavily centers:

    Observation

IAM demonstrates a second evidence form:

    Assertion

Potential distinction:

## Observation

Evidence about a state obtained through observation or measurement.

## Assertion

A governed Claim made by a recognized Source or Authority.

Examples beyond IAM may include:

- certificates
- attestations
- policy decisions
- signed provenance
- transaction commitments

## Architectural Question

Should `Assertion` become a first-class generalized object?

Status:

    CANDIDATE_GENERAL

Do not promote yet.

PKI and supply-chain provenance should test this directly.

---

# 21. Federation → Cross-Regime Truth Propagation

Federation allows identity information to cross separately administered system boundaries.

This is a major architectural challenge.

Conceptually:

    Regime A
      Identity Provider
          ↓
       Assertion
          ↓
      Trust Relationship
          ↓
    Regime B
      Relying Party

RTT interpretation:

    Cross-Regime Truth Propagation

The identity relationship is not simply copied.

It is consumed under another operational context.

The receiving system may have its own:

- assurance requirements
- audience requirements
- policy
- trust relationship
- intended use

Therefore:

> **Truth propagation across Regime boundaries requires re-qualification.**

This is a strong candidate generalization.

---

# 22. Federation Is Not Universal Trust

A federation relationship should not be interpreted as:

    Source trusted everywhere

Instead:

    Assertion Source
      +
    Trust Relationship
      +
    Audience
      +
    Regime
        ↓
    Potential Acceptance

This strongly reinforces:

    Authority Scope

from DNS.

Identity federation demonstrates that authority is not only:

    namespace-scoped

but may also be:

    audience-scoped
    relationship-scoped
    purpose-scoped

The generalized Regime concept grows stronger again.

---

# 23. Relying Party → Observer / Consumer

The relying party consumes identity assertions.

RTT interpretation:

    Observer / Consumer

This strongly reinforces the Observer candidate introduced by DNS.

The result of identity processing is meaningful relative to:

    who is relying on it
    for what purpose
    under what requirements

Therefore:

    observer_context

may no longer be merely optional environmental metadata.

Identity Truth suggests that observer/consumer context can directly affect qualification.

Status:

    CANDIDATE_GENERAL — strengthened

---

# 24. Observer Context and Identity

Consider one identity assertion.

Relying Party A may consider it sufficient for:

    low-consequence personalization

Relying Party B may consider it insufficient for:

    high-consequence administrative access

The assertion did not necessarily change.

The Regime did.

Conceptually:

    Same Assertion
       │
       ├── Regime A
       │     ↓
       │   ACCEPTABLE
       │
       └── Regime B
             ↓
          INSUFFICIENT

This is one of the clearest examples yet that:

> **Truth qualification can depend on Regime without the underlying evidence becoming arbitrary.**

---

# 25. Assurance → Regime Requirement

Digital identity systems use assurance concepts to establish requirements around proofing, authentication, and federation.

RTT interpretation:

    Assurance Requirement
          ↓
    Regime Qualification Threshold

The architecture should be careful here.

It should not flatten all assurance into one universal:

    confidence = 0.92

Different assurance dimensions may represent different operational properties.

Therefore:

> **Qualification should remain multidimensional where the domain requires it.**

This supports the existing architecture's resistance to one generic confidence scalar.

---

# 26. Assurance ≠ Confidence

This distinction is important.

An assurance level is not necessarily:

    mathematical probability that identity is true

RTT should therefore avoid translating:

    assurance
      →
    confidence score

without explicit justification.

Instead:

    assurance
      →
    set of operational requirements

is the safer architectural mapping.

The generalized Truth Service may later benefit from:

    RequirementSet

or:

    QualificationProfile

rather than a single numeric confidence.

Status:

    CANDIDATE_GENERAL

---

# 27. Identity Coherence

What does Coherence mean for Identity Truth?

It cannot simply mean:

    all evidence values are identical

Identity Coherence may concern compatibility among:

- claimed identity
- identity evidence
- proofing result
- credential relationship
- authenticator
- assertion
- subject attributes
- relying-party requirements

Therefore Crosswalk #3 strongly reinforces the DNS finding:

> **Coherence is domain-semantic.**

Conceptually:

    Coherence
      =
    structural compatibility among qualified identity relationships
    under the governing Regime

This is not generic equality.

---

# 28. Multiple Identities Are Not Automatically Paradox

A person may legitimately possess multiple digital identities.

Therefore:

    Identity A
    Identity B

does not automatically imply:

    contradiction

The correct interpretation depends on:

- service context
- pseudonymity
- account relationship
- role
- federation
- intended use

This parallels DNS:

    multiple valid addresses
      ≠
    Paradox

IAM reinforces:

> **Multiplicity must be interpreted through domain semantics before contradiction is declared.**

---

# 29. Identity Paradox

A genuine Identity Truth Paradox may instead arise when:

- qualified evidence supports incompatible identity relationships within the same Regime
- incompatible assertions claim the same subject relationship
- two authoritative Sources conflict materially within overlapping scope
- federation boundaries produce irreconcilable identity states

Even then, the system should first ask:

    separate Regimes?

    separate roles?

    separate pseudonyms?

    stale credential?

    changed lifecycle state?

before concluding:

    Paradox

Again:

> **Classification precedes contradiction.**

---

# 30. Identity Drift

Identity Truth introduces several forms of Drift.

Potential dimensions include:

## Attribute Drift

Identity-related attributes change.

## Credential Drift

The set or status of credentials changes.

## Authority Drift

The recognized identity authority changes.

## Federation Drift

Trust relationships change.

## Role Drift

Operational role changes.

## Regime Drift

The context in which identity is interpreted changes.

## Subject-Relationship Drift

The relationship between a digital identity and its underlying subject changes or becomes uncertain.

Most forms are not naturally numeric.

This further validates qualitative Drift.

---

# 31. Stable Identifier, Changed Identity Structure

Consider:

    account_id:
      12345

remaining unchanged.

Meanwhile:

    credential changed
    identity provider changed
    federation relationship changed
    attributes changed

The visible identifier is stable.

The identity structure has Drifted.

This parallels the DNS finding:

> **Stable accepted value does not imply stable truth structure.**

That pattern has now survived two non-identical Truth Classes.

Status:

    CANDIDATE_GENERAL — strengthened

---

# 32. Identity Lifecycle

Identity systems strongly introduce lifecycle.

A conceptual identity lifecycle may include:

    Applicant
       ↓
    Proofing
       ↓
    Enrollment
       ↓
    Credential Establishment
       ↓
    Authentication
       ↓
    Ongoing Use
       ↓
    Credential Change / Renewal
       ↓
    Revocation / Termination

RTT interpretation:

    Truth relationship lifecycle

This supports the broader principle:

> **Operational truth relationships may change state without the underlying subject ceasing to exist.**

The Truth Service should therefore distinguish:

    subject lifecycle

from:

    identity relationship lifecycle

---

# 33. Revocation → Qualification-State Transition

Revocation provides another important operational mechanism.

Previously usable evidence may become unusable.

Conceptually:

    previously qualified credential
          ↓
      revocation
          ↓
    no longer qualified

This strongly supports event-triggered:

    Revalidation

and potentially:

    Truth-State transition

The service must not assume:

    previously accepted
      =
    presently accepted

Crosswalk #3 therefore strengthens:

    Revalidation Required

---

# 34. Identity Freshness

Identity Truth introduces several freshness concepts.

Potential freshness dimensions include:

- age of identity proofing
- credential validity
- authenticator state
- assertion lifetime
- session state
- relying-party policy

This differs from:

    DNS TTL

and:

    NTP repeated synchronization

Yet all three support:

    time-conditioned qualification

Therefore:

> **Freshness appears increasingly generalized, while its operational mechanism remains domain-specific.**

---

# 35. Authentication as Revalidation

Authentication provides a useful identity-specific Revalidation pattern.

Conceptually:

    Established Identity Relationship
             ↓
    Current Authentication Event
             ↓
    Present Operational Qualification

This is not identical to:

    rebuilding identity proofing from scratch

Therefore Revalidation may operate at different layers.

Potential generalized lesson:

    Revalidation Depth

A Truth State may be revalidated by:

- refreshing one Observation
- rechecking a credential
- repeating authentication
- repeating full proofing
- changing authority relationship

The architecture does not yet represent Revalidation depth explicitly.

Status:

    CANDIDATE_GENERAL

---

# 36. Federation Lineage

Federation makes Lineage especially important.

Conceptually:

    Subject
      ↓
    Identity Proofing
      ↓
    Credential Service Provider
      ↓
    Authentication
      ↓
    Identity Provider
      ↓
    Assertion
      ↓
    Relying Party

The relying party may not directly observe the original proofing event.

It receives a downstream assertion.

Therefore:

> **Lineage may determine what the receiving system can legitimately infer from a Truth Claim.**

This strongly validates:

    Lineage

as a first-class generalized mechanism.

---

# 37. Lineage and Meaning Preservation

Crosswalk #3 introduces another subtle problem.

A claim propagated through federation may preserve:

    payload

while changing:

    operational meaning

if:

- audience changes
- Regime changes
- relying-party requirements differ
- attributes are transformed
- assertion context changes

Therefore:

    payload preservation
      ≠
    semantic preservation

This introduces a stronger candidate for:

    semantic Drift

across Lineage.

Status:

    CANDIDATE_GENERAL — strengthened

---

# 38. Identity Absence

DNS introduced:

    qualified absence
      ≠
    unknown

Identity Truth tests this further.

Potential states include:

    no identity record exists

    identity record exists but cannot be qualified

    identity exists but current authentication fails

    identity relationship is revoked

    identity state cannot presently be determined

These are structurally different.

Therefore the architecture should not compress them into:

    false

or:

    indeterminate

without preserving domain-native meaning.

This strengthens:

> **Truth-State lifecycle status and domain-native accepted value must remain separate.**

---

# 39. Authentication Failure ≠ Identity Nonexistence

A particularly important example:

    authentication failed

does not necessarily imply:

    subject does not exist

or:

    identity record does not exist

or:

    identity Claim is false

It means:

> **The current authentication attempt did not establish the required operational relationship.**

This mirrors earlier distinctions:

    expired DNS cache
      ≠
    record proven false

and:

    rejected Observation
      ≠
    false Observation

The pattern is generalizing.

---

# 40. Identity Materialization

DNS introduced:

    materialized local Truth State

Identity systems introduce related local state such as:

- identity records
- credentials
- sessions
- assertions
- cached attributes

However, these objects are not equivalent.

The architectural lesson is broader:

> **Operational Truth may be materialized into reusable artifacts whose qualification lifetime differs from the underlying subject relationship.**

This strengthens the Materialized Truth candidate while also demonstrating that it may need subtype/domain semantics.

Status:

    CANDIDATE_GENERAL — strengthened

---

# 41. IAM and Holdover

Identity Truth narrows Holdover further.

Continuing to use a prior identity relationship after fresh qualification disappears may have very different consequences from:

    NTP Holdover

or:

    DNS cache reuse

Whether prior state remains usable depends heavily on:

- policy
- authentication lifecycle
- credential status
- consequence
- session constraints

Therefore:

    Holdover

should remain a policy-governed Truth-State lifecycle condition rather than a generic automatic fallback.

Status:

    CANDIDATE_GENERAL — constrained

---

# 42. IAM and Authority Scope

DNS established:

    Authority
      =
    Source
      +
    Scope
      +
    Regime
      +
    Lineage

IAM strengthens this further.

Identity authority may be scoped by:

- subject population
- attribute
- authentication process
- relying party
- federation arrangement
- assurance requirement
- intended use

Therefore Authority Scope increasingly appears to deserve explicit architectural representation.

Still:

    one DNS crosswalk
      +
    one IAM crosswalk

is not sufficient to promote a new core entity automatically.

PKI is the next major test.

---

# 43. Source Roles Revisited

DNS suggested possible Source roles.

IAM makes the need clearer.

One identity flow may involve distinct entities acting as:

    evidence Source
    proofing authority
    credential provider
    authenticator
    identity provider
    assertion Source
    relying consumer

Representing all of these simply as:

    Source

may lose important relationship semantics.

Candidate model:

    Entity
      ↓
    Role
      ↓
    Relationship
      ↓
    Scope
      ↓
    Regime

This may be more general than adding many specialized Source types.

Status:

    CANDIDATE_GENERAL

PKI and Policy / IAM should test this model.

---

# 44. Assertion as Candidate Core Object

After NTP and DNS, the architecture centered strongly on:

    Observation

IAM exposes:

    Assertion

as something structurally different enough to watch carefully.

Potential generalized model:

    EvidenceItem
       │
       ├── Observation
       └── Assertion

Where:

    Observation
      = evidence resulting from observation or measurement

and:

    Assertion
      = governed statement made by a Source

This would be a major data-model change.

It should not be made yet.

Crosswalks likely to provide evidence:

    PKI
    Policy
    Ledgers
    Provenance

Status:

    ARCHITECTURE_CHALLENGE

---

# 45. Worked Example — Established Identity

## Claim

    "Subject S is associated with Identity I."

## Truth Class

    identity

## Regime

    service-specific account relationship

## Evidence

    qualified identity evidence

## Proofing

    completed under applicable requirements

## Authority

    recognized identity authority

## Result

    Truth State:
      operationally_accepted

    accepted_value:
      identity: I

## Architectural Finding

The accepted Identity Truth State represents a qualified relationship.

It does not claim to encode every possible identity associated with Subject S.

---

# 46. Worked Example — Successful Authentication

## Existing State

    Subject S
      associated with
    Identity I

## Current Evidence

    valid authentication event

## Regime

    relying-party authentication requirements satisfied

## Result

    Truth State:
      operationally_accepted

## Architectural Finding

Authentication re-establishes present operational usefulness of an existing identity relationship.

It does not necessarily recreate the original proofing process.

---

# 47. Worked Example — Different Relying Parties

## Assertion

    Identity Provider asserts Identity I.

## Relying Party A

Requirements:

    moderate assurance

Result:

    operationally_accepted

## Relying Party B

Requirements:

    stronger qualification

Result:

    rejected
    or
    indeterminate

depending on evidence and policy.

## Architectural Finding

The Assertion remained unchanged.

The Regime changed.

This strongly validates:

    Regime-qualified truth

---

# 48. Worked Example — Multiple Digital Identities

## Subject

    Subject S

## Legitimate Relationships

    Identity A
      service context A

    Identity B
      service context B

## Result

Both may be:

    operationally_accepted

within their respective Regimes.

## Architectural Finding

    multiple identities
      ≠
    contradiction

Multiplicity remains domain-semantic.

---

# 49. Worked Example — Revoked Credential

## Prior State

    Credential C
      qualified

## Event

    Credential C revoked

## New Evaluation

The prior credential can no longer satisfy the applicable qualification requirement.

## Possible Result

    Truth State:
      degraded
      rejected
      or indeterminate

depending on remaining evidence and Regime.

## Architectural Finding

Previously accepted evidence can lose qualification through lifecycle transition.

Revalidation must be event-capable.

---

# 50. Worked Example — Authentication Failure

## Claim

    "Current claimant is sufficiently associated with Identity I."

## Authentication Event

    failed

## Correct Interpretation

The system may conclude:

    current identity relationship not sufficiently authenticated

It should not automatically conclude:

    Subject S does not exist

or:

    Identity I never existed

## Architectural Finding

Failure must remain specific to the evaluated relationship.

---

# 51. Worked Example — Federated Assertion

## Upstream

    Subject
      ↓
    Identity Provider

## Assertion

    Identity I
      +
    relevant attributes
      +
    federation context

## Downstream

    Relying Party

## Evaluation

The Relying Party evaluates the assertion under its own Regime.

## Result

    accepted
    rejected
    degraded
    or indeterminate

## Architectural Finding

> **Truth crossing a Regime boundary requires downstream qualification rather than blind inheritance.**

This is one of the strongest contributions from IAM.

---

# 52. RTT Dimension Mapping

| RTT Dimension | IAM Crosswalk Interpretation | General Truth-Service Candidate |
|---|---|---|
| **Resonance** | Identity Claims and assertions propagate through trust relationships | Claims propagate among Sources and consumers |
| **Coherence** | Evidence, credentials, assertions, and Subject relationships remain compatible | Domain-semantic structural compatibility |
| **Drift** | Identity attributes, credentials, authorities, roles, or federation relationships change | Multi-dimensional truth Drift |
| **Paradox** | Qualified incompatible identity relationships remain in one Regime | Contradiction after domain and Regime qualification |
| **Regime** | Service, relying party, assurance, audience, and policy bound the identity result | Operational context governs acceptance |
| **Spin** | Subject and identity relationships persist across interactions | Identity / relationship persistence |
| **Elec** | Subjects, credentials, roles, authorities, assertions, and consumers remain distinct | Structural distinction |
| **Temp** | Credentials, authentication, assertions, and identity relationships have lifecycle | Freshness, transition, revocation, Revalidation |

---

# 53. SET Mapping

## Spin

Identity Truth strongly expresses Spin through:

- subject persistence
- identity continuity
- identifier continuity
- established identity relationships
- federation relationships

## Elec

Identity systems strongly express Elec through distinction among:

- Subject
- identity
- credential
- authenticator
- identity provider
- relying party
- role
- scope
- assertion

## Temp

Identity systems express Temp through:

- enrollment
- authentication
- credential lifecycle
- assertion lifetime
- revocation
- federation change
- Revalidation

Compactly:

> **Spin preserves identity relationships.**

> **Elec distinguishes subject, evidence, authority, and consumer.**

> **Temp governs proofing, authentication, lifecycle, and revocation.**

---

# 54. NTP-Derived Candidate Review

| Candidate from NTP | IAM Result | Finding |
|---|---|---|
| Truth Anchor | Survives but becomes relational | Strengthened / refined |
| Source | Strongly survives | Requires richer roles |
| Observation | Strongly survives | Assertions expose another evidence type |
| Lineage | Strongly survives | Federation makes it operationally important |
| Lineage distance | Less obviously numeric | Graph semantics stronger |
| Qualification | Strongly survives | Identity proofing/authentication reinforce it |
| Coherence | Survives | Strongly domain-semantic |
| Drift | Survives | Mostly qualitative / structural |
| Paradox | Survives cautiously | Multiplicity must be separated first |
| Regime | Strongly survives | Major identity dimension |
| Truth-State synthesis | Survives | Relationship-oriented |
| Correction | Survives differently | Lifecycle / access consequences differ |
| Holdover | Narrower | Strongly policy-dependent |
| Revalidation | Strongly survives | Authentication and lifecycle reinforce it |
| Failure transparency | Strongly survives | Authentication failure must remain specific |

---

# 55. DNS-Derived Candidate Review

| Candidate from DNS | IAM Result | Finding |
|---|---|---|
| Authority Scope | Strongly survives | Strengthened |
| Authority Lineage | Strongly survives | Federation reinforces it |
| Observer Context | Strongly survives | Relying party makes it explicit |
| delegated authority | Strongly survives | Federation / CSP relationships reinforce it |
| Materialized Truth State | Survives | Credentials / assertions complicate it |
| Multi-valued Truth | Survives conceptually | Multiple identities can be legitimate |
| Explicit Absence | Survives | Must distinguish nonexistent vs unauthenticated |
| Domain-semantic Coherence | Strongly survives | Strengthened |
| Transformation Lineage | Survives | Federation / attribute handling may transform meaning |
| Freshness-triggered Revalidation | Strongly survives | Lifecycle and authentication reinforce it |
| Stable-value structural Drift | Strongly survives | Identity structure may change under stable identifier |

IAM therefore strengthens many of the DNS refinements rather than reversing them.

---

# 56. New Candidate Mechanisms from IAM

Crosswalk #3 introduces or strengthens:

1. Truth Subject
2. Identity Relationship
3. Assertion
4. Evidence type distinction
5. Source Role
6. Audience
7. Relying Party / Consumer Context
8. Assurance Requirement
9. Qualification Profile
10. Cross-Regime Truth Propagation
11. Revalidation Depth
12. Relationship Lifecycle
13. Revocation-triggered Revalidation
14. Semantic preservation across federation

These should not all become core entities yet.

PKI and Authority Truth will provide the next major tests.

---

# 57. Architecture Refinement #1 — Subject May Need First-Class Representation

NTP could operate without an explicit generalized Subject object.

DNS made the queried name more visible.

IAM makes Subject difficult to ignore.

Candidate architecture:

    Subject
      ↓
    Claim
      ↓
    Evidence
      ↓
    Evaluation
      ↓
    Truth State

Before promotion, test against:

    PKI
    Ledgers
    Telemetry
    Provenance

If the concept survives broadly, Subject should become first-class.

---

# 58. Architecture Refinement #2 — Evidence May Need Types

Current architecture centers Observation.

IAM suggests:

    Evidence
       │
       ├── Observation
       └── Assertion

Potential future types may include:

    Measurement
    Assertion
    Attestation
    Credential
    Record

The generalized abstraction may ultimately be:

    EvidenceItem

with domain-specific subclasses.

This remains speculative.

Status:

    ARCHITECTURE_CHALLENGE

---

# 59. Architecture Refinement #3 — Authority Is a Relationship

After DNS and IAM:

    Authority

increasingly appears to require:

    Actor / Source
      +
    Role
      +
    Subject / Scope
      +
    Regime
      +
    Lineage
      +
    Time

This is substantially richer than:

    Source.authoritative = true

The architecture should avoid introducing a simplistic authority Boolean.

Status:

    CANDIDATE_GENERAL — strongly strengthened

---

# 60. Architecture Refinement #4 — Consumer Context Matters

DNS elevated Observer Context.

IAM makes it explicit through the relying party.

Potential generalized pattern:

    Evidence
      ↓
    Consumer
      ↓
    Consumer Regime
      ↓
    Qualification
      ↓
    Truth State

This suggests:

> **Truth-State usability may be consumer-relative without truth becoming arbitrary.**

The consumer provides operational constraints.

It does not invent the evidence.

---

# 61. Architecture Refinement #5 — Cross-Regime Claims Require Requalification

Federation demonstrates:

    Qualified Upstream Claim
           ↓
    Regime Boundary
           ↓
    Downstream Consumer
           ↓
    Requalification

Therefore:

> **Qualification should not automatically propagate across Regime boundaries.**

This likely generalizes strongly.

Potential later applications:

- PKI
- supply chains
- organizational policy
- distributed systems
- inter-service assertions

Status:

    CANDIDATE_GENERAL — strong

---

# 62. Architecture Refinement #6 — Lifecycle Is Relationship-Specific

Identity changes show that lifecycle may attach to:

    credential
    assertion
    session
    authority relationship
    identity relationship

rather than only:

    Truth State

The generalized model currently keeps lifecycle mostly around:

    TruthState
    RevalidationEvent

Later models may need richer entity lifecycle representation.

Do not expand yet.

Status:

    DEFERRED

---

# 63. Architecture Refinement #7 — Failure Must Be Typed

Identity systems demonstrate several semantically distinct failures:

    identity not established

    identity evidence insufficient

    authentication failed

    credential expired

    credential revoked

    assertion unacceptable

    federation trust unavailable

    identity state unknown

Collapsing these into:

    REJECTED

may lose important domain meaning.

The generic Truth Status may remain:

    rejected
    indeterminate
    expired

while:

    accepted_value
    DecisionReason
    domain metadata

preserve the specific failure semantics.

This validates the current separation between generic lifecycle state and domain-native meaning.

---

# 64. Architecture Refinement #8 — Assurance Should Not Become Fake Probability

IAM strongly reinforces the existing architecture's resistance to:

    confidence = arbitrary decimal

Operational requirements may be multidimensional.

Therefore:

    Assurance
      →
    Qualification Profile

is a better candidate than:

    Assurance
      →
    Probability

This may become important when AI-assisted evidence eventually enters the system.

---

# 65. Scoring Boundary

The scoring boundary for this crosswalk is:

    System:
      Digital Identity / IAM reference architecture

    Primary Truth Class:
      Identity Truth

    Evaluated Scope:
      Identity proofing
      authentication
      authenticator / credential lifecycle
      federation
      assertions
      relying-party relationships

    Primary Evidence:
      NIST SP 800-63-4 family

    Deferred Scope:
      vendor-specific IAM platforms
      organization-specific access policy
      proprietary risk engines
      implementation-specific directories
      authorization scoring beyond identity scope

The distinction between:

    Identity Truth

and:

    Authority Truth

should be preserved.

Authorization receives its own primary crosswalk later.

---

# 66. Preliminary Scoring Status

Current score status:

    provisional

Likely areas of substantial structural representation include:

- Anchor / Authority Quality
- Observation / Evidence Quality
- Regime Awareness
- Lineage Visibility
- Freshness / Revalidation
- Failure Transparency

Areas requiring careful scoring include:

- Coherence Detection
- Drift Detection
- Paradox Handling
- Correction Discipline

The crosswalk should not assign numbers until evidence is explicitly tied to each criterion.

---

# 67. Provisional Scorecard Template

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

No numeric value should be populated without:

    rationale
    evidence
    evaluation boundary

---

# 68. Scoring-Rubric Challenge

IAM pressures several scoring dimensions.

## Anchor Quality

Identity often involves multiple authorities and roles rather than one simple Anchor.

The rubric must not reward only single-root structures.

## Lineage Visibility

Federation Lineage may be operationally important without exposing every upstream proofing detail to the relying party.

Delegation and privacy may limit visibility.

The rubric must distinguish:

    unavailable because structurally absent

from:

    intentionally bounded disclosure

## Coherence Detection

Identity Coherence is semantic and relational.

Simple matching is insufficient.

## Drift Detection

Identity Drift may be event-based and qualitative rather than continuously measured.

## Correction Discipline

Correction may involve:

- credential replacement
- session termination
- attribute change
- re-proofing
- access restriction

The rubric must remain broad enough to capture these without assuming clock discipline.

---

# 69. Crosswalk #3 Findings

## Finding 1 — Identity Is Relational

Operational identity emerges from relationships among Subject, evidence, authority, context, and Regime.

    Status:
      CANDIDATE_GENERAL

## Finding 2 — Subject and Identity Must Remain Distinct

The entity being represented is not identical to its digital identity representation.

    Status:
      CANDIDATE_GENERAL

## Finding 3 — Proofing and Authentication Are Different Qualification Operations

Initial identity establishment and later authentication should not be collapsed.

    Status:
      DOMAIN_SPECIFIC with generalized qualification relevance

## Finding 4 — Authority Remains Scoped

Identity authority depends on role, scope, audience, Regime, and Lineage.

    Status:
      CANDIDATE_GENERAL — strengthened

## Finding 5 — Assertions Differ from Observations

Operational truth systems may carry authoritative Claims in addition to observational evidence.

    Status:
      CANDIDATE_GENERAL

## Finding 6 — Federation Is Cross-Regime Truth Propagation

Upstream qualification does not automatically transfer unchanged into downstream acceptance.

    Status:
      CANDIDATE_GENERAL

## Finding 7 — Consumer Context Matters

Relying-party requirements may change operational acceptance without changing the evidence itself.

    Status:
      CANDIDATE_GENERAL — strengthened

## Finding 8 — Multiplicity Is Not Contradiction

One Subject may legitimately have multiple digital identities.

    Status:
      CANDIDATE_GENERAL — strengthened

## Finding 9 — Authentication Failure Is Not Identity Nonexistence

Failure must remain specific to the relationship being evaluated.

    Status:
      CANDIDATE_GENERAL

## Finding 10 — Revalidation May Occur at Different Depths

Authentication, credential checks, and full proofing represent different levels of renewed qualification.

    Status:
      CANDIDATE_GENERAL

## Finding 11 — Stable Identifiers Can Hide Structural Drift

Identity structure may change without changing the visible identifier.

    Status:
      CANDIDATE_GENERAL — strengthened

## Finding 12 — Assurance Should Remain Structural

Assurance requirements should not be reduced automatically to generic numeric confidence.

    Status:
      CANDIDATE_GENERAL

---

# 70. Three-Crosswalk Comparison

After:

    NTP
    DNS
    IAM

several mechanisms have survived three substantially different domains.

## Strongly Surviving

    Claim

    Source

    Evidence / Observation

    Lineage

    Qualification

    Coherence

    Drift

    Regime

    Truth State

    Freshness

    Revalidation

    Failure Transparency

## Increasingly Important

    Subject

    Authority Scope

    Observer / Consumer Context

    Source Role

    domain semantics

    multi-valued state

    structural Drift

## Under Pressure

    single Anchor assumption

    generic equality-based Coherence

    purely numeric Drift

    one universal confidence score

    automatic cross-Regime inheritance

    Observation as the only evidence type

## Narrowed

    Holdover

    polling as generic Revalidation

    Lineage distance as a simple scalar

This is exactly the kind of architecture pressure the crosswalk sequence was intended to create.

---

# 71. Emerging General Pattern

After three crosswalks, the original NTP pattern is evolving.

Initial:

    Anchor
      ↓
    Source
      ↓
    Observation
      ↓
    Qualification
      ↓
    Coherence
      ↓
    Drift
      ↓
    Truth State
      ↓
    Correction
      ↓
    Revalidation

Emerging:

    SUBJECT
       ↓
    CLAIM
       ↓
    REGIME / CONSUMER CONTEXT
       ↓
    BOUNDED AUTHORITY
       ↓
    SOURCE ROLE
       ↓
    EVIDENCE
       ├── Observation
       └── Assertion?
       ↓
    LINEAGE
       ↓
    QUALIFICATION
       ↓
    DOMAIN-SEMANTIC COHERENCE
       ↓
    MULTIDIMENSIONAL DRIFT
       ↓
    PARADOX
       ↓
    REGIME-QUALIFIED TRUTH STATE
       ↓
    POLICY-GOVERNED CORRECTION
       ↓
    REVALIDATION
       ↓
    LIFECYCLE HISTORY

Several items remain provisional.

That uncertainty should remain visible.

---

# 72. Next Crosswalk Challenge

Crosswalk #4 examines:

    PKI
      ↓
    Integrity Truth

The governing question becomes:

> **Is this still what it claims to be?**

PKI should directly challenge:

    Anchor
    Authority Scope
    Authority Lineage
    Source Role
    Assertion
    Evidence type
    validity interval
    revocation
    relying-party trust
    multi-Anchor behavior

The major architectural question becomes:

> **Can the Truth Service keep identity, integrity, authority, Lineage, and temporal validity separate while still synthesizing a usable result?**

PKI should be especially useful for deciding whether:

    Assertion

and:

    Authority Relationship

deserve stronger first-class representation.

---

# 73. Canonical Identity Truth Statement

> **Identity Truth is not merely an identifier. It is a Regime-qualified relationship among a Subject, identity evidence, proofing history, credentials, current authentication state, authority, Lineage, consumer context, and lifecycle conditions sufficient for a declared operational use.**

Identity remains operationally useful because the relationship can be:

    established
    qualified
    authenticated
    propagated
    challenged
    revoked
    Revalidated

without claiming that one digital representation exhaustively defines the Subject.

---

# 74. Canonical Crosswalk Finding

Crosswalk #3 demonstrates that:

> **Operational Identity Truth belongs to relationships, not labels alone.**

IAM adds several major constraints to the emerging Truth-Service architecture:

    Subject is not Identity.

    Identity is context-qualified.

    Evidence must be qualified.

    Proofing is not Authentication.

    Authentication is not universal Identity Proof.

    Authority is scoped.

    Consumer context matters.

    Assertions can cross Regime boundaries.

    Cross-Regime Claims require requalification.

    Multiple identities need not conflict.

    Authentication failure does not imply nonexistence.

    Stable identifiers can conceal structural Drift.

    Assurance must not become fake probability.

After NTP and DNS, the architecture knew how to ask:

    When?

    Where?

IAM forces it to ask:

    Who?

But the answer is no longer:

    "This label."

It becomes:

    "This identity relationship,
     supported by this evidence,
     issued or qualified through this authority,
     preserved through this Lineage,
     for this consumer,
     under this Regime,
     at this point in its lifecycle."

That is a substantially richer form of operational truth.

---

# 75. References

Primary reference family:

    NIST SP 800-63-4
    Digital Identity Guidelines

    NIST SP 800-63A-4
    Identity Proofing and Enrollment

    NIST SP 800-63B-4
    Authentication and Authenticator Management

    NIST SP 800-63C-4
    Federation and Assertions

National Institute of Standards and Technology.

The NIST reference family is used to ground the digital-identity mechanisms in this crosswalk.

RTT terminology and generalized Truth-Service interpretations remain the analytical contribution of Resonance Truth.

---

## Canonical Summary

Crosswalk #1 asked:

    When?

Crosswalk #2 asked:

    Where?

Crosswalk #3 asks:

    Who?

The progression now reveals:

    TIME
      requires
    reference + Observation + Drift + Revalidation

    LOCATION
      requires
    namespace + authority + Lineage + freshness

    IDENTITY
      requires
    Subject + evidence + qualification + authority
    + consumer context + lifecycle

The generalized Truth Service is therefore moving away from:

    value lookup

toward:

    relationship evaluation

That may be the most important result yet.

**NTP taught the system to synchronize.**

**DNS taught it to resolve.**

**IAM teaches it that the thing being resolved is not the same as the identity
