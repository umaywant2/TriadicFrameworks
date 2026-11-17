# Crosswalk #4 — PKI and Integrity Truth

**Module:** Resonance Truth  
**Artifact:** Operational Truth Crosswalk #4  
**Truth Class:** Integrity Truth  
**Reference System:** Public Key Infrastructure (PKI) / X.509 Certificate Validation  
**Primary RTT Dimensions:** Lineage · Coherence · Authority · Regime  
**Supporting RTT Dimensions:** Identity · Temp · Drift · Paradox · Elec  
**Status:** Research Crosswalk / Architecture Challenge  
**Context:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

---

## Purpose

This crosswalk examines Public Key Infrastructure and X.509 certificate validation as the fourth operational reference system for the RTT Resonance Truth Service.

The governing question is:

> **Is this still what it claims to be?**

That description begins with Integrity Truth but quickly exposes a more complex structure.

Certificate validation may involve relationships among:

- subject
- public key
- certificate
- issuer
- signature
- trust anchor
- certification path
- policy
- validity period
- revocation state
- relying party
- application context

Crosswalk #4 therefore provides an important test of whether the Truth Service can keep several Truth Classes distinct while evaluating one operational result.

A single certificate-validation question may simultaneously involve:

    Identity Truth
    Integrity Truth
    Authority Truth
    Temporal Truth
    Lineage Truth
    State Truth

The central architectural question becomes:

> **Can the Truth Service preserve these dimensions separately while still producing a usable Regime-qualified result?**

---

# 1. Evidence Boundary

The primary technical reference for this crosswalk is:

    RFC 5280
    Internet X.509 Public Key Infrastructure
    Certificate and Certificate Revocation List (CRL) Profile

RFC 5280 profiles:

- X.509 version 3 certificates
- X.509 version 2 certificate revocation lists
- certificate extensions
- CRL extensions
- certification paths
- trust relationships
- revocation
- certification path validation

The RFC also defines a certification path validation algorithm.

Supporting NIST material may be used where useful to clarify path-validation and certification concepts.

This crosswalk focuses on:

    certificates
    trust anchors
    certification paths
    signatures
    validity
    constraints
    policy
    revocation
    relying-party validation

It does not attempt to model every PKI deployment architecture.

---

# 2. Evidence Discipline

This crosswalk distinguishes:

## PKI Fact

A mechanism explicitly represented in RFC 5280 or supporting bounded reference material.

## RTT Interpretation

A structural interpretation introduced through Resonance Truth.

## Candidate Generalization

A mechanism potentially reusable across multiple Truth Classes.

## Hypothesis

A proposed abstraction requiring further crosswalk evidence.

Example:

    PKI Fact:
      A certification path links certificates toward
      a trust anchor used during path validation.

    RTT Interpretation:
      Operational trust depends on validated Authority Lineage.

    Candidate Generalization:
      Lineage can participate directly in qualification.

    Hypothesis:
      Authority relationships should become first-class
      generalized Truth-Service objects.

The hypothesis remains provisional.

---

# 3. Why PKI Comes Fourth

The previous crosswalks progressively exposed:

    NTP
      ↓
    reference + Observation + Drift + Revalidation

    DNS
      ↓
    scope + delegation + Lineage + freshness

    IAM
      ↓
    Subject + evidence + authority + consumer context

PKI brings these structures together.

A certificate may:

- identify a Subject
- bind information to a public key
- be issued by an authority
- carry a signature
- exist inside a certification path
- operate under policy constraints
- have a validity interval
- later become revoked
- be evaluated by a relying party

This makes PKI an unusually useful architectural stress test.

It forces the Truth Service to distinguish:

    cryptographic integrity

from:

    identity binding

from:

    issuer authority

from:

    path validity

from:

    temporal validity

from:

    application suitability

These are related.

They are not interchangeable.

---

# 4. Integrity Truth

The primary Truth Class is:

    Integrity Truth

Its operational question is:

> **Is this still what it claims to be?**

For PKI, however, Integrity Truth cannot safely be reduced to:

    signature valid
      =
    certificate operationally trusted

Certificate validation may involve multiple additional conditions.

Therefore a more precise generalized question is:

> **Within this Regime, does the presented object preserve the integrity, Lineage, authority, validity, and policy relationships required for the declared operational use?**

This formulation keeps Integrity Truth central without pretending it acts alone.

---

# 5. PKI on Its Own Terms

At a high level, PKI uses public-key certificates and certification relationships to associate public keys with subjects and authorities.

A simplified conceptual relationship is:

    Trust Anchor
        ↓
    CA Certificate
        ↓
    Intermediate CA
        ↓
    End-Entity Certificate
        ↓
    Relying Party Validation

The relying party evaluates a certification path.

Relevant validation concerns may include:

- signatures
- validity periods
- name relationships
- certificate constraints
- certificate policy
- key usage
- revocation information

The final result is not merely:

    signature mathematically correct

It is an operational decision about whether the certificate/path is acceptable under the validation context.

---

# 6. Initial Structural Crosswalk

| PKI Concept | RTT Truth-Service Interpretation | Status |
|---|---|---|
| Trust anchor | Bounded Truth Anchor | Strong Candidate General |
| Certificate authority | Authority Source / Role | Strong Candidate General |
| Subject | Truth Subject | Strong Candidate General |
| Certificate | Signed Assertion / Evidence object | Strong Candidate General |
| Public key binding | Identity / integrity relationship | Domain-Specific with general relevance |
| Digital signature | Integrity evidence | Strong Candidate General |
| Certificate chain / path | Authority Lineage | Strong Candidate General |
| Intermediate CA | Delegated Authority | Strong Candidate General |
| Path validation | Lineage + Authority qualification | Strong Candidate General |
| Validity period | Temporal qualification boundary | Strong Candidate General |
| Certificate policy | Regime / qualification rule | Strong Candidate General |
| Name constraints | Scope constraint | Candidate General |
| Basic constraints | Authority-role constraint | Candidate General |
| Key usage | Permitted-use constraint | Strong Candidate General |
| Revocation | State / qualification transition | Strong Candidate General |
| CRL | Revocation-state evidence | Candidate General |
| Relying party | Observer / Consumer | Strong Candidate General |
| Trust store | Consumer-local Anchor set | Strong Candidate General |

PKI strongly reinforces several candidates from DNS and IAM while introducing an especially clear:

    signed Assertion
      +
    Authority Lineage
      +
    relying-party Anchor set
      +
    Temporal validity
      +
    policy constraints

relationship.

---

# 7. Trust Anchor → Bounded Truth Anchor

## PKI Reference-System View

Certification path validation begins relative to a trust anchor selected or recognized by the validating environment.

## RTT Interpretation

This strongly validates:

    Truth Anchor

but with an important constraint:

> **The Anchor is meaningful relative to the relying party and Regime.**

A trust anchor is not:

    universally trusted by definition

Instead:

    Relying Party
        ↓
    Trust Configuration
        ↓
    Trust Anchor
        ↓
    Certification Path

## Architectural Contribution

After NTP, DNS, IAM, and PKI:

    Anchor

continues to survive,

but:

    one universal Anchor

does not.

The emerging generalized concept is:

> **A bounded reference recognized within an operational Regime.**

Status:

    CANDIDATE_GENERAL — strongly strengthened

---

# 8. Trust Store → Consumer-Local Anchor Set

PKI contributes a significant refinement.

A relying party may operate with a configured set of trusted Anchors.

RTT interpretation:

    Consumer-Local Anchor Set

Conceptually:

    Consumer
       ↓
    Regime
       ↓
    Anchor Set
       ↓
    Validation

This strengthens the IAM finding:

    Consumer Context matters.

It also reinforces DNS:

    Authority is scoped.

## Candidate Generalization

The Truth Service may eventually require:

    Regime.allowed_anchor_ids

or a more general:

    AuthoritySet

rather than assuming every Evaluation can consult every known Anchor.

Status:

    CANDIDATE_GENERAL

---

# 9. Certificate Authority → Authority Role

A certification authority issues certificates.

RTT interpretation:

    Authority Role

This reinforces the IAM finding that:

    Source
      ≠
    Authority

and:

    Actor
      ≠
    one permanent role

A CA participates as an authority because of:

- certificate relationships
- constraints
- trust configuration
- scope
- Lineage
- Regime

Therefore:

> **Authority is a relationship involving actor, role, scope, Lineage, consumer, and Regime.**

After DNS + IAM + PKI, this candidate has survived three strong challenges.

Status:

    CANDIDATE_GENERAL — strongly strengthened

---

# 10. Subject → Truth Subject

PKI certificates contain subject-related information and bind public keys within the certificate structure.

RTT interpretation:

    Truth Subject

PKI therefore strengthens the candidate introduced by DNS and IAM.

Conceptual pattern:

    Subject
       ↓
    Claim / Assertion
       ↓
    Evidence
       ↓
    Evaluation

The Subject may be:

- person
- organization
- service
- device
- another named entity

## Architectural Finding

After IAM and PKI, a first-class Subject abstraction is becoming increasingly difficult to avoid.

Status:

    CANDIDATE_GENERAL — strongly strengthened

Still defer core-model promotion until additional crosswalks are considered.

---

# 11. Certificate → Signed Assertion

This is one of the most important results from Crosswalk #4.

IAM introduced the possibility that:

    Assertion
      ≠
    Observation

PKI provides a strong second example.

A certificate is not merely an Observation.

It is a signed data structure containing claims/bindings issued within a certification system.

RTT interpretation:

    Signed Assertion

This strongly reinforces a broader evidence hierarchy.

Candidate architecture:

    EvidenceItem
       │
       ├── Observation
       └── Assertion
              │
              └── Signed Assertion

Potential future extension:

    EvidenceItem
       ├── Observation
       ├── Assertion
       ├── Attestation
       └── Record

Status:

    CANDIDATE_GENERAL — significantly strengthened

This is now one of the strongest pending data-model changes.

---

# 12. Assertion ≠ Truth State

A certificate can be structurally valid as a data object yet fail operational validation for a relying party.

Therefore:

    signed Assertion
          ≠
    accepted Truth State

This parallels:

    Observation
      ≠
    Truth State

The generalized architecture now appears to require:

    Evidence
       ↓
    Qualification
       ↓
    Truth State

where Evidence may contain multiple subtypes.

---

# 13. Digital Signature → Integrity Evidence

A digital signature provides evidence regarding the integrity/authenticity relationship of signed data under the applicable cryptographic mechanism.

RTT interpretation:

    Integrity Evidence

However:

    signature valid
      ≠
    certificate acceptable for every purpose

This distinction is central.

A valid signature may coexist with:

- expiration
- revocation
- inappropriate use
- unacceptable policy
- unacceptable path
- unrecognized Anchor

Therefore:

> **Integrity evidence participates in qualification without becoming the whole Truth State.**

This strongly supports the multi-dimensional evaluation architecture.

---

# 14. Cryptographic Integrity ≠ Operational Trust

This is the canonical PKI distinction.

Consider:

    Signature:
      valid

but:

    Certificate:
      expired

or:

    Certificate:
      revoked

or:

    Path:
      does not terminate at an accepted trust anchor

The cryptographic integrity result remains meaningful.

The operational acceptance result differs.

Therefore:

    Integrity Truth
      ≠
    Authority Truth
      ≠
    Temporal Truth
      ≠
    Regime Acceptance

The Truth Service must preserve these dimensions separately.

---

# 15. Certification Path → Authority Lineage

RFC 5280 makes certification paths central to validation.

RTT interpretation:

    Authority Lineage

Conceptually:

    Trust Anchor
        ↓
    CA
        ↓
    Intermediate CA
        ↓
    End-Entity Certificate

The Lineage is not merely a historical path.

It participates directly in establishing whether the certificate may be accepted.

This strongly validates the DNS finding:

> **Lineage can establish authority.**

and strengthens it significantly.

Status:

    CANDIDATE_GENERAL — strongly strengthened

---

# 16. Lineage Is Operational

After NTP, Lineage could still have been interpreted as useful provenance metadata.

DNS made Lineage relevant to delegation.

IAM made Lineage relevant to federation.

PKI makes the case stronger:

> **Lineage may directly participate in qualification.**

This suggests:

    Lineage

belongs in the evaluation path rather than merely the audit path.

Current architecture already does this.

Crosswalk #4 strongly validates that design.

---

# 17. Intermediate CA → Delegated Authority

An intermediate CA provides another strong example of:

    delegated authority

Conceptually:

    Upstream Authority
          ↓
      delegation
          ↓
    Downstream Authority
          ↓
      assertion

RTT interpretation:

    Authority Relationship

This again suggests that simple:

    Source.anchor_id

may eventually be too weak as the sole authority relationship.

A richer graph may need to preserve:

- delegator
- delegate
- scope
- constraints
- validity
- Lineage
- policy

Status:

    ARCHITECTURE_CHALLENGE — strengthened

---

# 18. Path Validation → Lineage Qualification

PKI path validation provides perhaps the strongest real-system example yet of:

    Lineage Qualification

The question is not simply:

> Does a path exist?

It is:

> **Does the path satisfy the validation rules required by this application and trust context?**

RTT interpretation:

    Lineage
      +
    Authority
      +
    Time
      +
    Constraints
      +
    Regime
      ↓
    Qualification

This strongly supports the idea that Qualification may operate on:

- individual Evidence items
- Sources
- Lineage paths
- whole evidence structures

not merely one Observation at a time.

---

# 19. Qualification Scope Must Expand

The current architecture initially emphasizes:

    Observation Qualification

PKI demonstrates that qualification may also apply to:

    Evidence Item
    Source
    Authority Relationship
    Certification Path
    Anchor
    Policy Relationship

Therefore the generalized component may need to evolve conceptually from:

    Observation Qualification Engine

toward:

    Evidence / Relationship Qualification Engine

The external component name need not change yet.

Status:

    ARCHITECTURE_CHALLENGE

Crosswalk #5 should test this further.

---

# 20. Validity Period → Temporal Qualification

Certificates have temporal validity conditions.

RTT interpretation:

    Temporal Qualification Boundary

This reinforces the principle:

> **A structurally intact object may cease to be operationally acceptable because the current time crosses a validity boundary.**

Conceptually:

    Integrity:
      valid

    Temporal qualification:
      expired

    Operational result:
      unacceptable under Regime

This strongly demonstrates interaction among Truth Classes.

---

# 21. Temporal Truth Embedded Inside Integrity Evaluation

PKI provides a clear example of:

    Primary Truth Class:
      Integrity

while still requiring:

    Temporal Truth

for operational acceptance.

Therefore the Truth-Class model must support:

    one primary class
      +
    multiple secondary classes

without forcing the entire Evaluation into one category.

Candidate structure:

    truth_classes:
      - integrity
      - authority
      - identity
      - temporal
      - lineage

This validates the existing array-based model.

---

# 22. Certificate Policy → Regime Rule

Certificate policies and validation policy provide another strong mapping.

RTT interpretation:

    Regime Rule

A path or certificate may be structurally meaningful while failing the consumer's policy requirements.

Conceptually:

    Evidence
      ↓
    Valid Path
      ↓
    Policy Evaluation
      ↓
    Operational Acceptance

This reinforces:

> **Regime is not metadata around Truth. It participates in qualification.**

Status:

    CANDIDATE_GENERAL — strongly strengthened

---

# 23. Key Usage → Permitted Use

PKI exposes allowed-use constraints explicitly.

RTT interpretation:

    Permitted Use

This is significant because the Truth Service already models:

    permitted_uses
    prohibited_uses

PKI provides concrete support for that architectural distinction.

A Truth State may be sufficiently qualified for:

    use A

but not:

    use B

Therefore:

> **Truth-State usability is action-specific.**

This does not make the underlying evidence arbitrary.

It makes the operational Regime explicit.

---

# 24. Name Constraints → Scope Constraint

PKI can constrain the name space for which subordinate certification relationships are permitted.

RTT interpretation:

    Scope Constraint

This strengthens DNS:

    Authority is scoped.

It strengthens IAM:

    Authority is audience / relationship scoped.

And now PKI adds:

    Authority can be constrained through Lineage.

Generalized candidate:

    Authority Scope
      =
    Actor
      +
    Role
      +
    Subject / namespace
      +
    Regime
      +
    Lineage constraints

Status:

    CANDIDATE_GENERAL — strongly strengthened

---

# 25. Basic Constraints → Authority-Role Constraint

PKI distinguishes certificates permitted to act as certification authorities from ordinary end-entity certificates.

RTT interpretation:

    Role Constraint

This reinforces:

> **Capabilities should derive from qualified roles, not merely entity identity.**

A certificate's existence does not automatically confer:

    authority to issue subordinate assertions

This will matter strongly in Crosswalk #5:

    Authority Truth

---

# 26. Revocation → Qualification-State Transition

Revocation provides another lifecycle transition.

Conceptually:

    Certificate
      previously acceptable
          ↓
      revocation
          ↓
      no longer acceptable
      under applicable validation

RTT interpretation:

    Qualification-State Transition

This strongly reinforces IAM:

    previously accepted evidence
      ≠
    permanently acceptable evidence

Revocation provides event-driven:

    Revalidation pressure

Status:

    CANDIDATE_GENERAL — strengthened

---

# 27. Revocation State ≠ Integrity Destruction

A crucial distinction:

A revoked certificate does not necessarily become cryptographically malformed.

Its signature may still verify.

Its encoded information may remain intact.

Yet its operational qualification changes.

Therefore:

    Object Integrity
      may remain

while:

    Operational Acceptance
      changes

This is an exceptionally clean example of why:

    Integrity Truth
      ≠
    current authorization / trust state

The Truth Service must preserve both.

---

# 28. CRL → Revocation-State Evidence

Certificate Revocation Lists provide information about certificate status changes.

RTT interpretation:

    Revocation-State Evidence

This gives another example of an Evidence Item that is not directly:

    an Observation about the Subject

Instead, it supplies evidence about:

    qualification state of another evidence object

The architecture therefore needs to tolerate:

    Evidence about Evidence

Conceptually:

    Certificate
        ↑
    Revocation Evidence

This may later generalize into:

    Meta-Evidence

Status:

    CANDIDATE_GENERAL

Do not promote yet.

---

# 29. Evidence Can Refer to Evidence

This is an important architecture challenge.

Initial model:

    Claim
      ↓
    Observation

PKI suggests:

    Claim
      ↓
    Certificate Assertion
      ↑
    Revocation Evidence
      ↑
    Authority / Lineage

Therefore evidence relationships may form graphs.

They need not remain:

    Claim → flat list of Observations

This strongly reinforces the move toward an:

    Evidence Graph

as a future candidate architecture.

Status:

    ARCHITECTURE_CHALLENGE

---

# 30. Relying Party → Observer / Consumer

PKI again supplies:

    relying party

as the entity making the operational trust decision.

This strengthens IAM's consumer-context finding.

The same certificate/path may not produce identical acceptance under every relying-party configuration because:

- trust Anchors may differ
- policy may differ
- intended use may differ
- constraints may differ

Therefore:

> **Observer / Consumer context is becoming a repeated generalized mechanism.**

Status:

    CANDIDATE_GENERAL — strongly strengthened

---

# 31. Consumer-Relative Trust ≠ Arbitrary Truth

This distinction must remain explicit.

If:

    Consumer A
      accepts Anchor A

while:

    Consumer B
      does not

the evidence itself has not become subjective in the loose sense.

The operational Regimes differ.

Therefore:

    same Evidence
      +
    different valid Regimes
      ↓
    different operational acceptance

is possible without claiming:

    anything can be true

The architecture records the conditions.

That is the point of Regime qualification.

---

# 32. PKI Coherence

What does Coherence mean in PKI?

Again, simple equality is insufficient.

Coherence may involve compatibility among:

- certificate subject relationships
- issuer relationships
- signatures
- certification path
- constraints
- policies
- validity
- revocation state
- relying-party Anchor set

Therefore:

    Coherence
      =
    structural compatibility under validation semantics

This strongly validates the DNS/IAM conclusion:

> **Coherence is domain-semantic.**

At this point, generic equality-based Coherence should be considered rejected as a generalized model.

---

# 33. PKI Drift

Potential PKI-related Drift dimensions include:

## Trust-Anchor Drift

The relying party's accepted Anchor set changes.

## Authority Drift

Issuing authority relationships change.

## Path Drift

A different certification path is used.

## Policy Drift

Acceptance policy changes.

## Temporal Drift

Validity state moves toward or beyond expiration.

## Revocation Drift

Certificate status changes.

## Subject-Binding Drift

Identity / name relationships change across replacement certificates.

## Cryptographic-Parameter Drift

Accepted cryptographic requirements change over time.

Not all of these are certificate changes.

Some are Regime changes.

This reinforces multi-dimensional Drift strongly.

---

# 34. Stable Certificate, Changed Regime

Consider a certificate whose bytes remain unchanged.

Meanwhile:

    trust store changed
    policy changed
    certificate revoked
    current time crossed validity boundary

The object is identical.

The operational result changes.

Therefore:

> **Truth-State Drift may occur without object mutation.**

This is one of the clearest generalizations emerging from Crosswalk #4.

Integrity of the object is only one dimension.

---

# 35. Integrity Drift vs Regime Drift

Suppose:

    certificate data changes

That may be:

    Integrity Drift

Suppose instead:

    trust Anchor removed

That may be:

    Regime / Authority Drift

Suppose:

    certificate expires

That may be:

    Temporal Drift

Suppose:

    certificate revoked

That may be:

    State / Qualification Drift

The accepted result may be similar:

    no longer operationally acceptable

but the cause differs.

The model must preserve the causal dimension.

---

# 36. PKI Paradox

Potential PKI paradox-like conditions may include:

- distinct valid paths producing different policy outcomes
- different relying-party trust stores producing different acceptance
- identity and authority relationships conflicting across Regimes
- a certificate remaining cryptographically intact while becoming operationally unusable

However:

> **Different relying-party outcomes are not automatically Paradox.**

They may simply reflect:

    different Regimes

Likewise:

    signature valid
    certificate revoked

is not necessarily paradoxical.

Those are different Truth dimensions.

The architecture should preserve both without forcing contradiction.

---

# 37. Multi-Dimensional Truth Prevents False Paradox

This is a major contribution from PKI.

Consider:

    Integrity:
      valid

    Temporal:
      valid

    Authority:
      invalid

    Operational Acceptance:
      rejected

A simplistic model might interpret this as:

    contradictory evidence

A multi-dimensional model instead recognizes:

    different dimensions
      →
    one synthesis result

No Paradox is required.

Therefore:

> **Truth-Class separation prevents false contradiction.**

This strongly validates the two-axis Truth-Class × RTT-State model.

---

# 38. PKI and Explicit Absence

DNS introduced explicit absence.

Identity systems reinforced it.

PKI adds related structures.

Examples may include:

    required path cannot be established

    accepted trust Anchor unavailable

    required revocation information unavailable

These conditions should remain distinct from:

    certificate explicitly revoked

and:

    certificate expired

The architecture must keep:

    absence
    negative state
    unknown state
    unusable state

structurally distinguishable.

---

# 39. Path Failure ≠ Certificate Corruption

Suppose the relying party cannot establish an acceptable certification path.

That does not necessarily imply:

    certificate bytes corrupted

or:

    signature malformed

The correct conclusion may instead be:

> **The presented evidence cannot be qualified through an acceptable authority Lineage under the current Regime.**

This again demonstrates why failure causes need structured Decision Reasons.

---

# 40. PKI as Assertion Validation

PKI strongly supports the architecture shift from:

    Observation-Centric Truth Service

toward:

    Evidence-Centric Truth Service

Candidate generalized flow:

    Claim
      ↓
    Evidence Items
      │
      ├── Observations
      ├── Assertions
      ├── Signed Assertions
      └── Status Evidence
      ↓
    Evidence Relationships
      ↓
    Lineage
      ↓
    Qualification
      ↓
    Domain-Semantic Coherence
      ↓
    Truth State

This architecture is now supported conceptually by:

    IAM
    PKI

and partially by:

    DNS

It deserves serious consideration after Crosswalk #5.

---

# 41. Evidence Graph Candidate

PKI also strengthens a candidate:

    Evidence Graph

Conceptually:

    Trust Anchor
         ↓
    CA Certificate
         ↓
    Intermediate Certificate
         ↓
    End-Entity Certificate
         ↑
    Revocation Evidence
         │
         └── Status Source

The evidence does not form a simple flat list.

Relationships matter.

A generalized Truth Service may eventually need:

    EvidenceNode
    EvidenceEdge

analogous to the existing:

    LineageNode
    LineageEdge

Before adding these objects, test against:

    Authority Truth
    State Truth
    Transactional Truth
    Lineage Truth

Status:

    ARCHITECTURE_CHALLENGE — strengthening

---

# 42. Worked Example — Valid Path

## Claim

    "Certificate C is acceptable for Use U."

## Primary Truth Class

    integrity

## Secondary Truth Classes

    identity
    authority
    temporal
    lineage

## Consumer

    Relying Party R

## Trust Anchor

    Anchor A

## Path

    Anchor A
      ↓
    Intermediate B
      ↓
    Certificate C

## Integrity

    required signatures validate

## Temporal Qualification

    applicable validity conditions satisfied

## Policy

    applicable requirements satisfied

## Revocation State

    no disqualifying revocation state identified under the evaluated conditions

## Result

    Truth State:
      operationally_accepted

## Accepted Value

    certificate:
      C

    use:
      U

## Architectural Finding

Acceptance emerges from multiple qualified dimensions.

No single dimension alone establishes the result.

---

# 43. Worked Example — Valid Signature, Expired Certificate

## Integrity

    signature:
      valid

## Temporal Qualification

    validity:
      expired

## Result

    Truth State:
      expired
      or rejected

depending on the evaluation model and requested use.

## Architectural Finding

    valid signature
      ≠
    currently acceptable certificate

Integrity Truth remains positive while Temporal Truth disqualifies present operational use.

No Paradox is required.

---

# 44. Worked Example — Valid Signature, Revoked Certificate

## Integrity

    signature:
      valid

## Revocation State

    revoked

## Result

    Truth State:
      rejected

for the relevant operational use.

## Architectural Finding

The evidence object remains cryptographically intact.

Its qualification state has changed.

This strongly demonstrates:

    Object Integrity
      ≠
    Operational Acceptance

---

# 45. Worked Example — Unrecognized Trust Anchor

## Certificate

    structurally intact

## Certification Path

    terminates at Anchor A

## Relying Party

    does not recognize Anchor A

## Result

    Truth State:
      rejected
      or indeterminate

depending on the exact Evaluation semantics.

## Architectural Finding

The certificate's structure did not change.

The Regime / consumer trust configuration determines qualification.

---

# 46. Worked Example — Different Relying Parties

## Certificate

    C

## Path

    P

## Relying Party A

    recognizes Anchor A
    policy permits Use U

Result:

    operationally_accepted

## Relying Party B

    does not recognize Anchor A

Result:

    rejected

## Architectural Finding

The difference is:

    Regime / consumer context

not:

    certificate mutation

This reinforces Crosswalk #3 strongly.

---

# 47. Worked Example — Policy Mismatch

## Certificate

    cryptographically valid

## Path

    otherwise acceptable

## Requested Use

    U

## Policy

    certificate/path does not satisfy the required policy for U

## Result

    rejected for Use U

## Architectural Finding

Truth-State usability can be purpose-specific.

This strongly validates:

    permitted_uses
    prohibited_uses

in the emerging data model.

---

# 48. Worked Example — Changed Trust Store

## Time T1

    Trust Store:
      contains Anchor A

    Certificate C:
      accepted

## Time T2

    Trust Store:
      Anchor A removed

    Certificate C:
      unchanged

## Result

    prior Truth State may no longer remain operationally accepted

## Drift

    dimension:
      regime
      authority

## Architectural Finding

> **Operational Truth can Drift because the observer's Regime changes even when the evaluated object remains bit-for-bit identical.**

---

# 49. RTT Dimension Mapping

| RTT Dimension | PKI Crosswalk Interpretation | General Truth-Service Candidate |
|---|---|---|
| **Resonance** | Certificates and status assertions propagate through PKI relationships | Evidence propagates through governed Source relationships |
| **Coherence** | Certificates, signatures, paths, constraints, policy, and status remain compatible | Domain-semantic evidence compatibility |
| **Drift** | Trust, policy, validity, status, path, or binding changes | Multi-dimensional structural Drift |
| **Paradox** | Qualified states remain incompatible after Truth-Class and Regime separation | Preserved structural contradiction |
| **Regime** | Relying-party trust, policy, use, time, and scope govern acceptance | Context governs operational qualification |
| **Spin** | Subject/key/authority relationships persist | Identity and Lineage persistence |
| **Elec** | Subject, issuer, Anchor, role, scope, policy, and evidence remain distinct | Structural differentiation |
| **Temp** | Validity, revocation, trust changes, and Revalidation alter qualification | Lifecycle and temporal transition |

---

# 50. SET Mapping

## Spin

PKI expresses Spin through persistence of:

- Subject relationships
- public-key bindings
- issuer relationships
- trust relationships
- certification paths

## Elec

PKI strongly expresses Elec through distinction among:

- Subject
- issuer
- end entity
- certification authority
- trust Anchor
- certificate role
- policy
- usage constraints
- relying party

## Temp

PKI expresses Temp through:

- validity periods
- renewal
- replacement
- revocation
- trust-store changes
- policy changes
- Revalidation

Compactly:

> **Spin preserves certified relationships.**

> **Elec distinguishes roles, scopes, constraints, and authorities.**

> **Temp governs validity, revocation, replacement, and renewed qualification.**

---

# 51. NTP-Derived Candidate Review

| Candidate from NTP | PKI Result | Finding |
|---|---|---|
| Truth Anchor | Strongly survives | Relying-party bounded |
| Source | Survives | Roles increasingly necessary |
| Observation | Survives but insufficient alone | Evidence abstraction pressure |
| Lineage | Strongly survives | Operationally central |
| Lineage distance | Partially survives | Relationship semantics matter more |
| Qualification | Strongly survives | Must expand beyond Observation |
| Coherence | Strongly survives | Domain-semantic |
| Drift | Strongly survives | Multidimensional / mostly qualitative |
| Paradox | Survives cautiously | Class separation avoids false paradox |
| Regime | Strongly survives | Central to validation |
| Truth-State synthesis | Strongly survives | Multi-class synthesis |
| Correction | Survives differently | Trust/configuration actions vary |
| Holdover | Highly constrained | Not a generic PKI assumption |
| Revalidation | Strongly survives | Validity/revocation/trust changes |
| Failure transparency | Strongly survives | Failure reasons matter |

---

# 52. DNS-Derived Candidate Review

| Candidate from DNS | PKI Result | Finding |
|---|---|---|
| Authority Scope | Strongly survives | Major PKI mechanism |
| Authority Lineage | Strongly survives | Certification path central |
| Observer Context | Strongly survives | Relying party central |
| Delegated Authority | Strongly survives | Intermediate CAs |
| Materialized Truth State | Partially survives | Trust stores / cached state need careful modeling |
| Multi-Valued Truth | Possible | Multiple paths may exist |
| Explicit Absence | Survives conceptually | Missing path/status distinct from negative state |
| Domain-Semantic Coherence | Strongly survives | Path validation demonstrates it |
| Transformation Lineage | Less central here | Still relevant |
| Freshness Revalidation | Strongly survives | Validity/status changes |
| Stable-Value Structural Drift | Strongly survives | Trust/policy may change around stable object |

---

# 53. IAM-Derived Candidate Review

| Candidate from IAM | PKI Result | Finding |
|---|---|---|
| Truth Subject | Strongly survives | Strengthened |
| Identity Relationship | Survives | Certificate binds identity-like information to keys |
| Assertion | Strongly survives | Certificate is strong second example |
| Evidence type distinction | Strongly survives | Strengthened |
| Source Role | Strongly survives | CA/end entity/relying party distinctions |
| Audience / Consumer | Strongly survives | Relying party context |
| Assurance Requirement | Analog exists in validation requirements | Broader Qualification Profile strengthened |
| Cross-Regime Propagation | Survives | Trust path and consumer evaluation |
| Revalidation Depth | Survives conceptually | Path/status/policy checks may differ |
| Relationship Lifecycle | Strongly survives | Validity/revocation |
| Revocation Revalidation | Strongly survives | Direct support |
| Semantic preservation through Lineage | Survives | Constraints/policy influence meaning |

PKI strongly validates several IAM-derived challenges rather than rejecting them.

---

# 54. New Candidate Mechanisms from PKI

Crosswalk #4 introduces or strongly strengthens:

1. Signed Assertion
2. Evidence about Evidence
3. Evidence Graph
4. Qualification of Lineage
5. Consumer-Local Anchor Set
6. permitted-use constraints
7. policy-qualified Truth State
8. role-constrained authority
9. multi-class Truth-State synthesis
10. causal Drift dimension
11. object-integrity / operational-acceptance separation
12. trust-configuration Drift

Several of these now have evidence from multiple crosswalks.

---

# 55. Architecture Refinement #1 — Evidence Should Become the General Abstraction

After IAM and PKI, this candidate has become substantially stronger:

    EvidenceItem
       │
       ├── Observation
       └── Assertion
              │
              └── Signed Assertion

Potential later extensions:

    Attestation
    Record
    Status Evidence

The current architecture's:

    Observation

can remain the implemented first subtype.

But conceptually:

> **Evidence should become broader than Observation.**

Status:

    CANDIDATE_GENERAL — strong

Recommendation:

    validate once more in Crosswalk #5 before promoting.

---

# 56. Architecture Refinement #2 — Qualification Applies to Relationships

PKI demonstrates that qualification may apply to:

- certificate
- certification path
- Authority relationship
- policy relationship
- validity relationship
- status evidence

Therefore:

    Qualification
      ≠
    only Observation filtering

A generalized Qualification Engine should evaluate:

    evidence
    relationships
    Lineage
    Regime

This is now strongly supported.

Status:

    CANDIDATE_GENERAL — strong

---

# 57. Architecture Refinement #3 — Authority Deserves Richer Representation

DNS:

    scoped authority

IAM:

    role + audience + federation authority

PKI:

    delegated path-constrained authority

Together suggest:

    AuthorityRelationship

as a possible future first-class object.

Candidate fields:

    authority_id
    actor_id
    role
    subject_scope
    delegator_id
    regime_id
    valid_from
    valid_until
    lineage_reference
    constraints

Do not modify the core schema yet.

Crosswalk #5 is specifically about Authority Truth and should decide whether this promotion is justified.

---

# 58. Architecture Refinement #4 — Truth Evaluation May Require an Evidence Graph

The original architecture assumes roughly:

    Claim
      ↓
    Observation[]

PKI suggests:

    Claim
      ↓
    Evidence Graph
       │
       ├── Signed Assertion
       │      ↓
       │   Authority Lineage
       │
       ├── Status Evidence
       │
       └── Policy / Constraint Relationships
              ↓
         Evaluation

This is a major candidate architectural evolution.

Status:

    ARCHITECTURE_CHALLENGE

Do not implement before testing against:

    Authority Truth
    State Truth
    Transactional Truth

---

# 59. Architecture Refinement #5 — Truth-State Usability Is Purpose-Specific

PKI explicitly pressures the assumption that a Truth State is either:

    accepted

or:

    not accepted

for every operation.

A more useful result is:

    accepted for:
      Use A

    prohibited for:
      Use B

The existing fields:

    permitted_uses
    prohibited_uses

are strongly validated.

Status:

    CANDIDATE_GENERAL — strengthened

---

# 60. Architecture Refinement #6 — Truth Classes Must Remain Orthogonal

PKI demonstrates why the two-axis model is necessary.

One Evaluation may produce:

    Integrity:
      coherent

    Identity:
      coherent

    Temporal:
      expired

    Authority:
      coherent

    Lineage:
      coherent

Overall operational state:

    rejected / expired for requested use

No contradiction exists.

Different dimensions produced different findings.

Therefore:

> **Truth Classes must remain independently inspectable during synthesis.**

This may eventually imply:

    per-class evaluation state

inside a Truth State.

Current schema does not yet model that explicitly.

Status:

    ARCHITECTURE_CHALLENGE

---

# 61. Per-Class Truth-State Candidate

Potential future representation:

    class_states:

      integrity:
        status: coherent

      identity:
        status: coherent

      authority:
        status: coherent

      temporal:
        status: expired

      lineage:
        status: coherent

    overall:
      status: rejected

This would preserve causal structure better than one flattened result.

However, it introduces substantial complexity.

Test against:

    Authority Truth
    State Truth
    Transactional Truth

before promotion.

Status:

    CANDIDATE_GENERAL

---

# 62. Architecture Refinement #7 — Cause Must Survive Final Status

Two Truth States may both be:

    rejected

for entirely different reasons.

Example A:

    expired

Example B:

    untrusted Anchor

Example C:

    invalid signature

Example D:

    revoked certificate

A generic status alone is therefore insufficient.

The architecture already preserves:

    DecisionReason

PKI strongly validates that design.

The final state should preserve causal structure.

---

# 63. Architecture Refinement #8 — Anchor Sets May Be Regime-Bound

One Evaluation may recognize:

    Anchor Set A

while another recognizes:

    Anchor Set B

Therefore:

    Anchor eligibility

should potentially belong to:

    Regime

or:

    Consumer Context

rather than globally to the service.

This strengthens:

    Consumer-Local Anchor Set

as a generalized mechanism.

Status:

    CANDIDATE_GENERAL

---

# 64. Scoring Boundary

The scoring boundary for this crosswalk is:

    System:
      Internet X.509 Public Key Infrastructure

    Primary Truth Class:
      Integrity Truth

    Evaluated Scope:
      X.509 certificate and CRL structure
      certification paths
      path validation
      trust anchors
      validity
      constraints
      certificate policy
      revocation relationships

    Primary Evidence:
      RFC 5280

    Supporting Evidence:
      bounded NIST PKI path-validation material

    Deferred Scope:
      vendor-specific trust stores
      TLS protocol behavior beyond certificate validation
      private deployment policy
      platform-specific UI / warning behavior
      certificate issuance automation
      proprietary certificate lifecycle systems

The crosswalk evaluates PKI validation structure rather than every system that happens to use certificates.

---

# 65. Preliminary Scoring Status

Current status:

    provisional

Likely scoring strengths include:

- Anchor Quality
- Lineage Visibility
- Observation / Evidence Quality
- Regime Awareness
- Freshness / Revalidation
- Failure Transparency

Areas requiring careful interpretation include:

- Coherence Detection
- Drift Detection
- Paradox Handling
- Correction Discipline

The rubric should not reward PKI merely because path validation is structurally rich.

Each criterion still requires evidence.

---

# 66. Provisional Scorecard Template

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

No numeric value should be entered without:

    rationale
    evidence
    evaluation boundary

---

# 67. Scoring-Rubric Challenge

PKI pressures several scoring criteria.

## Anchor Quality

A trust anchor is exceptionally explicit, but trust is still consumer/Regime bounded.

The rubric must score structural quality without implying universal authority.

## Lineage Visibility

PKI has strong certification paths.

However:

    path construction

and:

    path validation

should not automatically be conflated.

The score must respect the defined evaluation boundary.

## Observation Quality

The current criterion name may become too narrow if PKI Evidence is better understood as Assertion rather than Observation.

This supports potentially renaming later to:

    Evidence Quality

after rubric review.

## Coherence Detection

PKI validation is not necessarily Coherence detection in the same sense as NTP comparison.

The rubric must not reward any validation mechanism as though it were multi-Source Coherence.

## Correction Discipline

Certificate validation can reject or accept use, but broader correction/remediation may exist outside core PKI.

Delegation must remain visible.

This is exactly why:

    delegated
      ≠
    absent

was added to the scoring model.

---

# 68. Scoring-Criterion Rename Candidate

After IAM and PKI, the criterion:

    Observation Quality

may be too narrow.

Potential replacement:

    Evidence Quality

This would naturally include:

    Observations
    Assertions
    Signed Assertions
    Status Evidence
    Attestations

Before changing the canonical rubric:

1. record this as a candidate
2. test Crosswalk #5
3. re-evaluate NTP and DNS terminology
4. rescore only if the criterion is formally revised

Status:

    RUBRIC_CHALLENGE

---

# 69. Crosswalk #4 Findings

## Finding 1 — Integrity Is Not Operational Acceptance

Cryptographic integrity may remain positive while other Truth dimensions disqualify use.

    Status:
      CANDIDATE_GENERAL

## Finding 2 — Certificates Are Assertions, Not Observations

Truth-bearing input requires a broader abstraction than Observation alone.

    Status:
      CANDIDATE_GENERAL — strengthened

## Finding 3 — Authority Lineage Is Operational

Certification paths demonstrate that Lineage can directly influence qualification.

    Status:
      CANDIDATE_GENERAL — strongly strengthened

## Finding 4 — Anchors Are Consumer / Regime Bounded

Trust Anchor recognition belongs to an operational context.

    Status:
      CANDIDATE_GENERAL — strengthened

## Finding 5 — Authority Is Role- and Scope-Constrained

Authority cannot safely be represented as a simple Source property.

    Status:
      CANDIDATE_GENERAL — strongly strengthened

## Finding 6 — Evidence May Qualify Other Evidence

Revocation/status information introduces evidence relationships.

    Status:
      CANDIDATE_GENERAL

## Finding 7 — Truth-State Usability Is Purpose-Specific

A qualified object may be permitted for one use and prohibited for another.

    Status:
      CANDIDATE_GENERAL — strengthened

## Finding 8 — Stable Objects Can Experience Operational Drift

Trust, policy, time, or status may change around an unchanged object.

    Status:
      CANDIDATE_GENERAL — strongly strengthened

## Finding 9 — Multi-Class Evaluation Prevents False Paradox

Integrity, Identity, Authority, Temporal, and Lineage findings can legitimately differ.

    Status:
      CANDIDATE_GENERAL

## Finding 10 — Final Status Must Preserve Cause

Rejected or expired states need structured rationale.

    Status:
      CANDIDATE_GENERAL — strongly strengthened

## Finding 11 — Qualification Applies Beyond Observations

Evidence, Lineage, roles, authority relationships, and policy may all participate in qualification.

    Status:
      CANDIDATE_GENERAL — strengthened

## Finding 12 — Evidence Graphs May Be Required

Flat Observation lists may be insufficient for complex Truth relationships.

    Status:
      ARCHITECTURE_CHALLENGE

---

# 70. Four-Crosswalk Comparison

After:

    NTP
    DNS
    IAM
    PKI

the architecture is beginning to separate into increasingly stable and increasingly challenged abstractions.

## Strongly Surviving

    Claim

    Regime

    Evidence

    Source

    Lineage

    Qualification

    Coherence

    Drift

    Truth State

    Revalidation

    Failure Transparency

## Increasingly Strong

    Subject

    Authority Scope

    Consumer / Observer Context

    Source Role

    domain-semantic Coherence

    multi-dimensional Drift

    lifecycle

    purpose-specific usability

## Newly Strong

    Assertion

    Evidence typing

    Authority Relationship

    Lineage qualification

    Evidence relationships

## Under Significant Pressure

    Observation as universal Evidence type

    flat Evidence lists

    global Anchor assumptions

    one overall unstructured Truth status

    generic equality-based Coherence

    numeric confidence as universal qualification

## Narrowed

    Holdover

    simple Lineage distance

    Correction as direct local value adjustment

This is evidence that the crosswalk sequence is progressively refining rather than merely confirming the original model.

---

# 71. Emerging General Pattern After PKI

The model is evolving toward:

    SUBJECT
       ↓
    CLAIM
       ↓
    INTENDED USE
       ↓
    CONSUMER / OBSERVER
       ↓
    REGIME
       ↓
    BOUNDED ANCHOR SET
       ↓
    AUTHORITY RELATIONSHIPS
       ↓
    EVIDENCE GRAPH
       │
       ├── Observations
       ├── Assertions
       ├── Signed Assertions
       └── Status Evidence
       ↓
    LINEAGE
       ↓
    QUALIFICATION
       ↓
    PER-CLASS / DOMAIN-SEMANTIC EVALUATION
       ↓
    COHERENCE
       ↓
    MULTIDIMENSIONAL DRIFT
       ↓
    PARADOX
       ↓
    TRUTH-STATE SYNTHESIS
       ↓
    PERMITTED / PROHIBITED USE
       ↓
    CORRECTION / RESPONSE
       ↓
    REVALIDATION
       ↓
    IMMUTABLE HISTORY

This model is still provisional.

Crosswalk #5 will specifically pressure the Authority layer.

---

# 72. Next Crosswalk Challenge

Crosswalk #5 examines:

    Policy / IAM
      ↓
    Authority Truth

The governing question becomes:

> **Who may declare, validate, or act?**

This is the right next test because three prior systems now point toward:

    Authority Relationship

as a candidate core abstraction.

DNS contributed:

    delegated namespace authority

IAM contributed:

    identity / federation authority

PKI contributed:

    path-constrained certification authority

Crosswalk #5 should determine whether these can be represented by one generalized structure or whether:

    authority

is too domain-specific to promote cleanly.

The central architectural question becomes:

> **Can authority be modeled as a Regime-qualified relationship among actor, role, scope, delegation, Lineage, policy, and time without conflating permission with truth?**

---

# 73. Canonical Integrity Truth Statement

> **Integrity Truth is not merely evidence that an object's bits or signature remain intact. It is a Regime-qualified relationship among the evaluated object, its signed assertions, Subject bindings, Authority Lineage, temporal validity, status evidence, policy constraints, consumer trust configuration, and intended use.**

Operational integrity therefore requires the architecture to preserve:

    what remained intact

    who asserted it

    through which authority path

    for which Subject

    during which validity conditions

    under which policy

    for which consumer

    for which use

without collapsing those dimensions into one generic:

    valid = true

---

# 74. Canonical Crosswalk Finding

Crosswalk #4 demonstrates that:

> **A truth-bearing object can remain internally intact while becoming operationally unusable because authority, time, policy, status, Lineage, or consumer Regime changed around it.**

That finding significantly strengthens the Resonance Truth architecture.

The first four systems now show:

    NTP
      → accepted local state can Drift from reference

    DNS
      → authority and location are scope-bound

    IAM
      → identity is relationship-bound

    PKI
      → integrity is not sufficient for operational trust

The Truth Service is therefore moving further from:

    Is this value true?

toward:

    What relationship is being asserted?

    What evidence supports it?

    Who had authority to assert it?

    Through what Lineage?

    Under which policy?

    At what time?

    For which observer?

    For which use?

    What has changed since qualification?

That is a substantially more mature architecture than the original NTP-derived model.

---

# 75. References

Primary technical reference:

    RFC 5280
    Internet X.509 Public Key Infrastructure
    Certificate and Certificate Revocation List (CRL) Profile

RFC Editor / Internet Engineering Task Force.

Supporting bounded reference material:

    NIST PKI path-validation material

The technical references establish the PKI mechanisms used in this crosswalk.

RTT terminology, Truth Classes, Drift categories, Regime interpretation, Evidence abstraction, and proposed architectural generalizations remain the analytical contribution of Resonance Truth.

---

## Canonical Summary

Crosswalk #1 asked:

    When?

Crosswalk #2 asked:

    Where?

Crosswalk #3 asked:

    Who?

Crosswalk #4 asks:

    Is it still intact and operationally valid?

PKI answers that last question with something much richer than:

    signature valid

It exposes:

    Subject

    Assertion

    Signature

    Authority

    Delegation

    Path

    Anchor

    Constraint

    Policy

    Time

    Status

    Consumer

    Use

The emerging structure now looks less like a truth lookup service and increasingly like a:

> **qualified evidence-and-relationship evaluation system.**

That may be the largest architectural shift since the crosswalk series began.

**NTP gave truth a reference.**

**DNS gave it scope.**

**IAM gave it a Subject.**

**PKI gives it an evidence chain and asks whether every link still qualifies.**

**Crosswalk #5 now gets to ask who had the authority to make those links matter.**
