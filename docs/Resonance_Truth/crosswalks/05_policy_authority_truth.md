# Crosswalk #5 — Policy, Authorization, and Authority Truth

**Module:** Resonance Truth  
**Artifact:** Operational Truth Crosswalk #5  
**Truth Class:** Authority Truth  
**Reference System:** Access Control Policy / IAM / Attribute-Based Access Control (ABAC)  
**Primary RTT Dimensions:** Regime · Elec · Lineage · Coherence  
**Supporting RTT Dimensions:** Spin · Temp · Drift · Paradox · Intent  
**Status:** Research Crosswalk / Architecture Challenge  
**Context:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

---

## Purpose

This crosswalk examines access-control policy, authorization, and Attribute-Based Access Control as the fifth operational reference system for the RTT Resonance Truth Service.

The governing question is:

> **Who may declare, validate, access, modify, or act?**

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

Crosswalk #3 examined:

    IAM
      ↓
    Identity Truth
      ↓
    Who?

Crosswalk #4 examined:

    PKI
      ↓
    Integrity Truth
      ↓
    Is it still intact and operationally valid?

Crosswalk #5 now separates another dimension:

    Policy / Authorization
      ↓
    Authority Truth
      ↓
    Who may?

This distinction is fundamental.

A Subject may be:

    correctly identified

while still:

    unauthorized

A Source may be:

    authoritative within Scope A

while having:

    no authority within Scope B

An actor may be:

    authorized to perform Operation X

while being:

    unauthorized to perform Operation Y

Therefore Authority Truth must remain separate from:

    Identity Truth
    Integrity Truth
    correctness
    capability
    successful action

The central architectural question becomes:

> **Can authority be represented as a Regime-qualified relationship among actor, role or attributes, action, object, scope, policy, delegation, Lineage, and time without conflating permission with truth?**

---

# 1. Evidence Boundary

Primary grounding for this crosswalk includes:

    NIST SP 800-162
    Guide to Attribute Based Access Control (ABAC)
    Definition and Considerations

The NIST ABAC model defines authorization as an evaluation involving attributes associated with:

    subject
    object
    requested operation

and, in some cases:

    environment conditions

against:

    policy
    rules
    relationships

that describe allowable operations.

Supporting access-control material may also include applicable NIST access-enforcement concepts.

This crosswalk focuses on:

    authorization
    subject
    object
    operation
    attributes
    environment
    policy
    rules
    relationships
    access enforcement
    delegation
    scope
    authority lifecycle

It does not attempt to model every IAM product or access-control implementation.

---

# 2. Evidence Discipline

This document distinguishes four statement types.

## Policy / Authorization Fact

A mechanism explicitly represented in the bounded reference material.

## RTT Interpretation

A structural interpretation introduced through Resonance Truth.

## Candidate Generalization

A mechanism potentially reusable beyond Authority Truth.

## Hypothesis

A proposed abstraction requiring further crosswalk evidence.

Example:

    Authorization Fact:
      Access may be determined by evaluating Subject,
      Object, Operation, and Environment attributes
      against policy.

    RTT Interpretation:
      Authority is a relationship evaluated within a Regime.

    Candidate Generalization:
      Relationships governing Truth usage should be
      representable independently from Subject identity.

    Hypothesis:
      AuthorityRelationship should become a first-class
      generalized Truth-Service object.

The final statement remains provisional until testing against later crosswalks.

---

# 3. Why Authority Comes Fifth

Authority has appeared repeatedly in the first four crosswalks.

## NTP

Reference Sources introduced bounded reference relationships.

## DNS

Delegation introduced:

    Authority Scope
    Authority Lineage

## IAM

Federation introduced:

    role
    audience
    relying party
    scoped identity authority

## PKI

Certification paths introduced:

    delegated authority
    trust Anchors
    role constraints
    scope constraints
    consumer-local trust

By Crosswalk #4, a candidate structure had emerged:

    Authority
      =
    Actor / Source
      +
    Role
      +
    Scope
      +
    Lineage
      +
    Regime
      +
    Time

Crosswalk #5 tests that abstraction directly.

---

# 4. Authority Truth

The primary Truth Class is:

    Authority Truth

Its operational question is:

> **Who may declare, validate, access, modify, or act?**

A more precise generalized formulation is:

> **Within this Regime, is this Subject authorized to perform this Operation on this Object under the currently applicable policy, attributes, relationships, and environmental conditions?**

This means Authority Truth is intrinsically relational.

It cannot safely be reduced to:

    Actor:
      authorized = true

Instead:

    Authority
      =
    Subject
      ×
    Operation
      ×
    Object
      ×
    Policy
      ×
    Environment
      ×
    Regime

The relationship is the evaluated object.

---

# 5. Authorization on Its Own Terms

Attribute-based access control evaluates whether requested operations are allowable using attributes and governing rules.

A simplified conceptual form is:

    Subject Attributes
            │
            ├───────────┐
            │           │
            ▼           ▼
    Requested       Object
    Operation       Attributes
            │           │
            └─────┬─────┘
                  │
                  ▼
           Environment
           Conditions
                  │
                  ▼
               Policy
                  │
                  ▼
           Authorization
             Decision
                  │
                  ▼
             Enforcement

This exposes several distinctions important to Resonance Truth:

    Subject
      ≠
    Permission

    Identity
      ≠
    Authority

    Policy
      ≠
    Decision

    Decision
      ≠
    Enforcement

    Authorization
      ≠
    Successful Action

Those distinctions are foundational to this crosswalk.

---

# 6. Initial Structural Crosswalk

| Authorization Concept | RTT Truth-Service Interpretation | Status |
|---|---|---|
| Subject | Truth Subject / actor | Strong Candidate General |
| Object | Target / Truth object | Strong Candidate General |
| Operation | Requested action | Strong Candidate General |
| Subject attribute | Evidence / qualification input | Strong Candidate General |
| Object attribute | Target-state qualification input | Candidate General |
| Environment condition | Regime input | Strong Candidate General |
| Policy | Declared Intent / Regime rule | Strong Candidate General |
| Rule | Qualification constraint | Strong Candidate General |
| Relationship | Authority relationship | Strong Candidate General |
| Authorization decision | Regime-qualified Authority Truth State | Strong Candidate General |
| Permit | Positive operational authority state | Domain-Specific state |
| Deny | Negative operational authority state | Domain-Specific state |
| Enforcement | Downstream action governance | Strong Candidate General |
| Delegation | Authority Lineage | Strong Candidate General |
| Revocation | Authority-state transition | Strong Candidate General |
| Role / attribute assignment | Authority Evidence | Candidate General |

This crosswalk immediately gives us a cleaner model of authority than:

    Source.authoritative = true

---

# 7. Subject → Actor

IAM established:

    Subject
      ≠
    Identity

Authority Truth now adds:

    Subject
      ≠
    Permission

The Subject is the active entity requesting or attempting an Operation.

RTT interpretation:

    Actor

Conceptually:

    Subject
      +
    Identity State
      +
    Attributes
      ↓
    Actor Context

This becomes one input into authorization.

It does not itself establish permission.

---

# 8. Object → Target

Authorization requires something upon which an Operation is requested.

RTT interpretation:

    Target

The Target may be:

- file
- record
- service
- API
- device
- process
- command
- configuration
- information resource
- another protected object

This introduces a useful general distinction:

    Subject
      acts upon
    Target

Potential future generalized relationship:

    ActionRequest(
      subject,
      operation,
      target,
      regime
    )

Status:

    CANDIDATE_GENERAL

This will likely matter again in:

    State Truth
    Transactional Truth
    Intent Truth

---

# 9. Operation → Requested Action

Authority is meaningless without knowing:

> **Authority to do what?**

Therefore:

    Actor authorized?
      =
    incomplete question

The actual question is:

> **Is Actor A authorized to perform Operation O on Target T under Regime R?**

This strongly reinforces:

    permitted_uses
    prohibited_uses

from the Truth-State data model.

Authority attaches to actions.

It should not be modeled as a universal actor property.

---

# 10. Authority Is Relational

After DNS, IAM, PKI, and now ABAC, the recurring structure is strong enough to state more firmly:

> **Authority is a relationship, not an intrinsic property.**

Canonical candidate structure:

    AuthorityRelationship
      ├── actor
      ├── role / attributes
      ├── operation
      ├── target / scope
      ├── policy
      ├── delegation / Lineage
      ├── Regime
      ├── valid_from
      └── valid_until

This is substantially richer than:

    source:
      authoritative: true

Crosswalk #5 therefore provides direct evidence for promoting:

    AuthorityRelationship

from tentative abstraction toward a core architecture candidate.

---

# 11. Subject Attributes → Qualification Evidence

ABAC evaluates attributes associated with the Subject.

RTT interpretation:

    Qualification Evidence

Possible attributes may represent characteristics relevant to authorization.

The important architectural principle is:

> **An attribute is evidence used by policy evaluation, not permission itself.**

Conceptually:

    Subject Attribute
          ↓
    Policy Evaluation
          ↓
    Authorization Decision

not:

    Subject Attribute
          =
    Authorization

This parallels:

    certificate
      ≠
    accepted Truth State

and:

    identity credential
      ≠
    identity acceptance

---

# 12. Object Attributes → Target Evidence

ABAC also evaluates attributes associated with the protected Object.

RTT interpretation:

    Target Evidence

This is significant because previous crosswalks focused strongly on evidence about the Claim Subject.

Authority Truth shows that evidence may also describe:

    what is being acted upon

Potential generalized architecture:

    Evidence
       │
       ├── Subject Evidence
       ├── Target Evidence
       ├── Environment Evidence
       └── Relationship Evidence

This is a strong argument for moving away from:

    flat Observation[]

toward:

    typed Evidence Graph

Status:

    CANDIDATE_GENERAL — strengthened

---

# 13. Environment Conditions → Regime Input

ABAC may evaluate environmental conditions.

RTT interpretation:

    Regime Input

This strongly supports the Regime model.

Authorization can depend upon conditions beyond:

    Subject
    Object
    Operation

Potential conditions may be contextual.

The generalized principle is:

> **The operational boundary may participate directly in qualification.**

This means Regime is increasingly not merely:

    metadata describing evaluation

but:

    input to evaluation

Status:

    CANDIDATE_GENERAL — strongly strengthened

---

# 14. Policy → Declared Intent

Authority Truth introduces an unusually clean connection to:

    Intent Truth

A policy describes allowable behavior.

RTT interpretation:

    Declared Intent

Conceptually:

    Policy
      =
    desired authority relationship

The current request represents:

    observed / proposed operation

Authorization compares:

    declared Intent

with:

    current request context

This suggests a useful cross-class relationship:

    Authority Truth
          depends on
    Intent Truth

Crosswalk #8 will examine Intent Truth directly.

---

# 15. Policy ≠ Decision

A policy describes governing rules.

It does not itself constitute a particular authorization decision.

Conceptually:

    Policy
      +
    Current Attributes
      +
    Operation
      +
    Environment
        ↓
    Decision

Therefore:

    Policy
      ≠
    Truth State

This parallels earlier distinctions:

    Claim
      ≠
    Truth State

    Certificate
      ≠
    Truth State

    Assertion
      ≠
    Truth State

The system increasingly operates through:

    Input Structure
        ↓
    Evaluation
        ↓
    Qualified State

---

# 16. Rule → Qualification Constraint

Policy rules become constraints used during authority evaluation.

RTT interpretation:

    Qualification Constraint

A constraint may evaluate:

- Subject properties
- Target properties
- requested Operation
- Environment
- relationships
- policy context

This reinforces the PKI finding:

> **Qualification applies to relationships, not merely Evidence items.**

The object being qualified here is effectively:

    proposed authority relationship

---

# 17. Relationship → Authority Relationship

NIST ABAC explicitly allows policies, rules, or relationships to describe allowable operations under attribute combinations.

This directly supports the emerging RTT abstraction:

    AuthorityRelationship

At this point the concept has survived:

    DNS delegation

    IAM federation

    PKI certification paths

    ABAC authorization relationships

This is considerably stronger evidence than existed when the abstraction first appeared.

## Promotion Status

Recommended:

    CANDIDATE_CORE

rather than:

    CANDIDATE_GENERAL

This means:

> Strong enough to model explicitly in the next architecture revision, subject to reconciliation with the remaining crosswalks.

It does not yet require immediate mutation of the current schema.

---

# 18. Authorization Decision → Authority Truth State

Policy evaluation produces an authorization result.

RTT interpretation:

    Authority Truth State

The domain-native result may be:

    permit

or:

    deny

Potentially other implementation-specific states may exist, but the canonical generalized point is:

    Authority evaluation
          ↓
    domain-native authority result

This should remain separate from generic Truth-State lifecycle.

Example:

    truth_state:
      operationally_accepted

    accepted_value:
      authorization: permit

versus:

    truth_state:
      operationally_accepted

    accepted_value:
      authorization: deny

This may initially seem strange, but it preserves an important distinction.

The system may be highly confident and fully coherent that:

    access is denied

A negative domain result is still a successfully qualified Truth State.

---

# 19. Deny ≠ Rejected Evaluation

This is one of Crosswalk #5's most important contributions.

Consider:

    Policy evaluation:
      DENY

The Truth Service itself may have successfully evaluated all evidence.

Therefore:

    Truth State:
      operationally_accepted

    accepted_value:
      authority:
        denied

is structurally different from:

    Truth State:
      rejected

where the evidence itself failed to support a qualified result.

This strongly reinforces the DNS finding:

    qualified absence
      ≠
    indeterminate

and generalizes it:

> **A negative domain result is not the same as evaluation failure.**

---

# 20. Permit ≠ Truth

The inverse is equally important.

A policy decision may return:

    PERMIT

That means:

> **The requested Operation is authorized under the evaluated policy conditions.**

It does not establish that:

- the action is wise
- the action is safe
- the underlying Claim is correct
- the Subject's statement is true
- the system state is valid
- execution will succeed

Therefore:

    authorization
      ≠
    correctness

This distinction must remain canonical.

---

# 21. Authority ≠ Capability

A Subject may be:

    authorized

but technically unable to perform the Operation.

Likewise, a Subject may be:

    technically capable

but unauthorized.

Therefore:

    may
      ≠
    can

Authority Truth answers:

> **May this action occur?**

Capability asks:

> **Can this action occur?**

Those are separate operational dimensions.

The Truth Service should not collapse them.

---

# 22. Authority ≠ Identity

IAM established an identity relationship.

Authority Truth evaluates what that identified Subject may do.

Conceptually:

    Identity Truth
          ↓
    Who is this?

    Authority Truth
          ↓
    What may this Subject do?

A successful identity result may become evidence inside an Authority evaluation.

Therefore Truth Classes may compose.

They should not collapse.

---

# 23. Authority ≠ Integrity

PKI may establish evidence integrity and Authority Lineage.

Authorization policy may then determine whether the identified actor may perform a requested Operation.

Therefore:

    valid certificate
      ≠
    authorized action

and:

    intact signed assertion
      ≠
    permit

Again, Truth Classes compose.

---

# 24. Enforcement → Downstream Action Governance

Authorization decision and enforcement are different stages.

Conceptually:

    Decision
      ↓
    Enforcement
      ↓
    Operational Result

RTT interpretation:

    Truth State
      ↓
    Correction / Action Policy
      ↓
    Downstream Enforcement

This strongly validates the architecture's separation:

    Evaluation
      ≠
    Correction / Mutation

Crosswalk #5 gives us a second very clear operational example after NTP.

---

# 25. Decision ≠ Enforcement

Suppose policy evaluation says:

    DENY

but an enforcement mechanism fails to apply that result.

Then:

    Authority Truth:
      denied

while:

    Observed System State:
      unauthorized action occurred

Those states are different.

This introduces an important relationship between:

    Authority Truth

and:

    Observational Truth

The policy answer can be correct while enforcement fails.

That difference is:

    operational Drift

between:

    intended authority state

and:

    observed system behavior

---

# 26. Policy Enforcement Drift

Consider:

    Policy:
      deny operation O

but:

    System:
      permits operation O

This represents:

    Intent:
      deny

    Observed State:
      permit occurred

Potential RTT interpretation:

    Policy Drift
    State Drift
    Authority Drift

The key principle is:

> **Truth about what should be allowed and truth about what actually occurred are different objects.**

This becomes a bridge toward:

    Desired-State Systems
    Telemetry

later in the series.

---

# 27. Delegation → Authority Lineage

DNS introduced delegated namespace authority.

IAM introduced federated identity authority.

PKI introduced path-constrained certification authority.

Policy systems may also represent delegated authority relationships.

RTT interpretation:

    Authority Lineage

Conceptually:

    Authority A
       ↓
    Delegates bounded authority
       ↓
    Authority B
       ↓
    Exercises permitted action

The Lineage matters because:

    B's authority

may derive from:

    A's authority

under:

    scope
    constraints
    time
    policy

This is now a strongly recurring cross-system structure.

---

# 28. Delegation Is Not Authority Duplication

When authority is delegated:

    Delegate
      ≠
    Delegator

The delegate may receive only a bounded subset.

Conceptually:

    Original Authority:
      operations = [A, B, C]
      scope = S

    Delegated Authority:
      operations = [B]
      scope = S1

Therefore:

> **Authority Lineage must preserve constraints rather than merely ancestry.**

This is a major refinement to generalized Lineage.

Lineage edges may need their own:

    scope
    constraints
    validity

not merely:

    relation

Status:

    CANDIDATE_CORE

---

# 29. Role → Authority Grouping

Role-based systems group permissions or authority relationships.

RTT interpretation:

    Authority Grouping

A role is not itself:

    authorization result

It participates in evaluation.

Potential structure:

    Subject
      ↓
    Role
      ↓
    Permissions
      ↓
    Policy
      ↓
    Decision

This further supports typed evidence and relationships.

The precise role model remains domain-specific.

---

# 30. Attribute → Evidence

ABAC strengthens the broader:

    EvidenceItem

candidate.

Attributes may describe:

    Subject
    Object
    Environment

They become inputs into evaluation.

They are not all Observations in the NTP sense.

This provides another independent reason to generalize:

    Observation

toward:

    Evidence

After:

    IAM
    PKI
    Policy / ABAC

the evidence abstraction has now survived three consecutive challenges.

## Recommended Status

    CANDIDATE_CORE

The architecture revision after Crosswalk #5 should seriously consider:

    EvidenceItem

as the generalized superclass.

---

# 31. Evidence Roles

Crosswalk #5 suggests that evidence needs contextual roles.

Potential categories include:

    Subject Evidence
    Target Evidence
    Policy Evidence
    Environment Evidence
    Relationship Evidence
    Status Evidence

This may be modeled through:

    EvidenceItem.role

rather than adding a separate object type for every domain.

Status:

    CANDIDATE_GENERAL

---

# 32. Environment → Dynamic Regime

Previous crosswalks showed Regime as:

- precision requirement
- namespace
- consumer context
- trust configuration

Authority Truth adds:

    dynamic environment

Therefore Regime can include conditions that change during operation.

Conceptually:

    Regime
      =
    relatively stable policy context
      +
    current environmental state

This raises a modeling question.

Should:

    Environment Evidence

belong inside:

    Regime

or:

    Evidence

Potential answer:

    stable constraints
      → Regime

    observed current conditions
      → Evidence

This distinction should remain provisional.

Status:

    ARCHITECTURE_CHALLENGE

---

# 33. Static Regime vs Dynamic Context

A useful provisional split is:

## Regime

The declared operational rules within which evaluation occurs.

Examples:

    applicable policy
    jurisdiction
    trust domain
    security boundary
    intended use

## Context Evidence

Current conditions used during evaluation.

Examples:

    current environment
    resource state
    current Subject attributes

This prevents Regime from becoming an unbounded container for every input.

Potential generalized pattern:

    Regime
      +
    Context Evidence
      ↓
    Evaluation

Status:

    CANDIDATE_GENERAL

---

# 34. Policy Version → Regime Version

Authorization changes when policy changes.

Therefore:

    policy version

should participate in:

    Evaluation history

This strongly validates:

    Regime.policy_version

from the current architecture.

Example:

    Evaluation 1:
      policy: v1
      result: permit

    Evaluation 2:
      policy: v2
      result: deny

No Subject change is required.

The Regime changed.

---

# 35. Policy Drift

Authority Truth introduces clear Policy Drift.

Potential causes include:

- rule change
- permission change
- role change
- attribute-definition change
- delegation change
- scope change

The resulting accepted authority state may change even when:

    Subject unchanged
    Object unchanged
    Operation unchanged

Therefore:

> **Policy itself is a truth-bearing structural dependency.**

This strongly reinforces multidimensional Drift.

---

# 36. Attribute Drift

Attributes may change.

Examples structurally include:

    Subject attribute changed

    Object attribute changed

    Environment attribute changed

A previously permitted relationship may then become denied.

Therefore:

    Authority Truth

is sensitive not only to policy Drift but:

    evidence Drift

The Truth Service must preserve which input dimension caused the changed result.

---

# 37. Authority Drift

Authority Drift may occur when:

- delegation changes
- role changes
- permissions change
- policy changes
- scope changes
- validity ends
- relationship is revoked

The Actor may remain the same.

Identity may remain the same.

The authority relationship changes.

This strongly validates Authority as an independently inspectable Truth Class.

---

# 38. Temporal Authority

Authority can be time-bounded.

Conceptually:

    authorized from:
      T1

    authorized until:
      T2

At:

    T3

the identity remains intact.

The authority no longer applies.

This gives another clean example of:

    Identity Truth:
      coherent

    Authority Truth:
      expired / denied

No contradiction exists.

Truth-Class orthogonality prevents false Paradox.

---

# 39. Revocation → Authority-State Transition

Revocation or removal of authority provides another event-driven Revalidation mechanism.

Conceptually:

    AuthorityRelationship
      active
        ↓
    revocation event
        ↓
    Revalidation
        ↓
    authority no longer accepted

This strengthens:

    event-driven Revalidation

across yet another Truth Class.

At this point Revalidation is strongly generalized.

---

# 40. Authority Coherence

What does Coherence mean for Authority Truth?

It may involve compatibility among:

- Subject identity
- Subject attributes
- Object attributes
- requested Operation
- policy
- environment
- delegation
- scope
- applicable relationships

Therefore:

    Coherence
      =
    structural compatibility of the authority relationship
    under the applicable policy Regime

This continues to validate:

> **Coherence is domain-semantic.**

Generic equality has now failed across:

    DNS
    IAM
    PKI
    Authority

It should no longer be considered a viable generalized definition.

---

# 41. Conflicting Policies

Authority systems may expose apparently conflicting rules or policies.

Possible situations include:

    Policy A:
      permit

    Policy B:
      deny

Before declaring Paradox, the architecture must determine:

- which policy applies
- scope
- precedence
- Regime
- Subject
- Object
- Operation
- time

If a defined policy-combination rule resolves the conflict:

    no Paradox

If equally qualified policies remain structurally incompatible inside the same Regime:

    potential Paradox

Again:

> **Classification and policy resolution precede Paradox registration.**

---

# 42. Authority Paradox

A genuine Authority Paradox may arise when:

- overlapping recognized authorities provide incompatible decisions
- delegation chains overlap inconsistently
- policies of equal applicability conflict without resolution rule
- Authority relationships remain mutually incompatible after scope and Regime resolution

Potential result:

    contested

or:

    indeterminate

depending on the Regime.

The system should not guess simply because an action is waiting.

---

# 43. Deny Is Not Paradox

A denied request may be:

    fully coherent
    fully qualified
    fully explainable

Therefore:

    DENY
      ≠
    contested

Likewise:

    PERMIT
      ≠
    operationally safe

Domain-native result and Truth-State qualification remain separate.

This is a major recurring pattern.

---

# 44. Negative Domain Results

Across the crosswalks we now have multiple examples:

## DNS

    qualified absence

## IAM

    authentication failure

## PKI

    certificate rejected for use

## Authority

    authorization denied

This suggests a strong generalized principle:

> **Negative domain results must not be represented as generic Truth-Service failure.**

The Truth Service asks:

    Was the domain result determined coherently?

not:

    Was the domain result positive?

This distinction is now strongly generalized.

---

# 45. Truth-State Polarity vs Qualification

A future model may need to distinguish:

    qualification_status

from:

    domain_result

Current pattern:

    Truth State:
      operationally_accepted

    accepted_value:
      authorization: denied

This works.

However, repeated crosswalk evidence suggests possible future structure:

    qualification:
      operationally_accepted

    domain_result:
      denied

This should remain a model candidate rather than immediate schema change.

Status:

    CANDIDATE_GENERAL

---

# 46. Enforcement Failure Example

## Subject

    Subject S

## Operation

    read

## Object

    Object O

## Policy Evaluation

    deny

## Enforcement

    incorrectly permits action

## Authority Truth

    denied

## Observational Truth

    action occurred

## Drift

    dimensions:
      policy
      state

## Architectural Finding

> **Authority Truth can remain correct while enforcement state Drifts away from it.**

This shows why Evaluation and action must remain separated.

---

# 47. Worked Example — Simple Permit

## Subject

    S

## Operation

    read

## Object

    O

## Subject Evidence

    attributes satisfy required conditions

## Object Evidence

    attributes compatible

## Policy

    permits S-like Subjects to read O-like Objects

## Environment

    applicable conditions satisfied

## Result

    Truth State:
      operationally_accepted

    accepted_value:
      authorization: permit

## Architectural Finding

Authority Truth is the evaluated relationship.

The Subject itself did not become globally "authorized."

---

# 48. Worked Example — Simple Deny

## Subject

    S

## Operation

    write

## Object

    O

## Policy Evaluation

    conditions do not permit requested Operation

## Result

    Truth State:
      operationally_accepted

    accepted_value:
      authorization: deny

## Architectural Finding

The Truth Service successfully established a negative domain result.

No service `rejected` state is required.

---

# 49. Worked Example — Same Subject, Different Operation

## Subject

    S

## Object

    O

## Operation A

    read

Result:

    permit

## Operation B

    delete

Result:

    deny

## Architectural Finding

Authority is operation-scoped.

Therefore:

    Subject.authorized = true

is structurally insufficient.

---

# 50. Worked Example — Same Subject, Different Object

## Subject

    S

## Operation

    read

## Object A

Result:

    permit

## Object B

Result:

    deny

## Architectural Finding

Authority is target-scoped.

This strengthens:

    AuthorityRelationship

as a multi-party relationship.

---

# 51. Worked Example — Environment Change

## Initial Context

    Subject:
      S

    Operation:
      O

    Object:
      X

    Environment:
      E1

Result:

    permit

## Changed Context

    Subject:
      S

    Operation:
      O

    Object:
      X

    Environment:
      E2

Result:

    deny

## Architectural Finding

No Subject, Object, or requested Operation changed.

Dynamic context changed the Authority Truth State.

This strongly validates:

    Context Evidence

as distinct from relatively stable Regime rules.

---

# 52. Worked Example — Policy Change

## Evaluation 1

    Policy:
      v1

    Result:
      permit

## Evaluation 2

    Policy:
      v2

    Result:
      deny

Subject, Object, and Operation remain unchanged.

## Drift

    dimension:
      policy
      regime

## Architectural Finding

Truth-State changes can originate in governing Intent rather than observed entity state.

---

# 53. Worked Example — Delegated Authority

## Authority A

May administer:

    Scope S

## Delegation

Authority A delegates to Authority B:

    Operation:
      approve

    Scope:
      S1

## Request

Authority B attempts:

    approve
    within S1

Result:

    potentially permitted

Authority B attempts:

    approve
    within S2

Result:

    deny

## Architectural Finding

Delegation transfers bounded authority relationships.

It does not clone the delegator's entire authority.

---

# 54. Worked Example — Revoked Delegation

## Prior State

    Authority B
      delegated Operation O
      over Scope S

## Event

    delegation revoked

## New Evaluation

    same Actor
    same Operation
    same Target

Result:

    deny

## Architectural Finding

Identity remained unchanged.

Authority relationship changed.

Revalidation must be event-driven.

---

# 55. RTT Dimension Mapping

| RTT Dimension | Authority Crosswalk Interpretation | General Truth-Service Candidate |
|---|---|---|
| **Resonance** | Policy and authority relationships propagate into decisions | Governing Claims influence downstream qualification |
| **Coherence** | Subject, Target, Operation, policy, attributes, and context remain compatible | Domain-semantic relationship compatibility |
| **Drift** | Policy, attribute, scope, delegation, or authority changes | Multi-dimensional relationship Drift |
| **Paradox** | Equally applicable authority structures remain incompatible | Preserved policy / authority contradiction |
| **Regime** | Policy, scope, environment, intended use, and context govern authority | Operational boundary participates directly |
| **Spin** | Subject, roles, delegated relationships, and policy structures persist | Relationship persistence |
| **Elec** | Subject, Object, Operation, role, policy, scope, and authority stay distinct | Structural separation |
| **Temp** | Authority is granted, changed, revoked, and Revalidated | Lifecycle and state transition |

---

# 56. SET Mapping

## Spin

Authority Truth expresses Spin through persistence of:

- Subject identity
- roles
- policy relationships
- delegated authority
- scope relationships

## Elec

Authority Truth strongly expresses Elec through distinction among:

- Subject
- Object
- Operation
- role
- policy
- rule
- attribute
- delegation
- scope
- permit
- deny

## Temp

Authority Truth expresses Temp through:

- policy revision
- attribute change
- authority grant
- delegation
- revocation
- expiry
- environmental change
- Revalidation

Compactly:

> **Spin preserves authority relationships.**

> **Elec distinguishes who, what, which action, and under which boundary.**

> **Temp governs grant, change, revocation, and renewed qualification.**

---

# 57. NTP-Derived Candidate Review

| Candidate from NTP | Authority Result | Finding |
|---|---|---|
| Truth Anchor | Survives abstractly | Policy/authority source rather than time reference |
| Source | Survives | Role semantics essential |
| Observation | Too narrow alone | Evidence abstraction strengthened |
| Lineage | Strongly survives | Delegation path important |
| Qualification | Strongly survives | Core authorization mechanism |
| Coherence | Strongly survives | Domain-semantic |
| Drift | Strongly survives | Policy / relationship dimensions |
| Paradox | Survives | After policy-resolution semantics |
| Regime | Strongly survives | Direct Evaluation input |
| Truth-State synthesis | Strongly survives | Domain result permit/deny |
| Correction | Survives as enforcement | Separate from decision |
| Holdover | Weak / policy-specific | Not a generic authority assumption |
| Revalidation | Strongly survives | Policy / attribute / revocation triggers |
| Failure transparency | Strongly survives | Deny vs indeterminate must remain distinct |

---

# 58. DNS-Derived Candidate Review

| Candidate from DNS | Authority Result | Finding |
|---|---|---|
| Authority Scope | Directly validated | Strongly strengthened |
| Authority Lineage | Directly validated | Strongly strengthened |
| Observer Context | Survives | Request / evaluator context matters |
| Delegated Authority | Directly validated | Strong |
| Materialized Truth State | Context-dependent | Policy decision caching requires separate study |
| Multi-valued Truth | Relevant to permissions | Domain-specific representation |
| Explicit Absence | Survives | No permission vs unknown authority distinct |
| Domain-semantic Coherence | Strongly survives | Strengthened |
| Transformation Lineage | Relevant to delegation | Strengthened |
| Freshness Revalidation | Strongly survives | Grants/revocations/policy changes |
| Stable-value structural Drift | Strongly survives | Identity may stay stable while authority changes |

---

# 59. IAM-Derived Candidate Review

| Candidate from IAM | Authority Result | Finding |
|---|---|---|
| Truth Subject | Strongly survives | Subject central |
| Identity Relationship | Becomes input | Identity ≠ Authority |
| Assertion | Survives | Policy/attribute assertions relevant |
| Evidence typing | Strongly survives | Attribute inputs strengthen it |
| Source Role | Strongly survives | Authority roles central |
| Consumer Context | Survives | Resource/request context central |
| Assurance Requirement | Becomes rule/Regime input | Qualification profile strengthened |
| Cross-Regime Propagation | Relevant to delegated/federated policy | Strengthened |
| Revalidation Depth | Survives | Depends on changed input |
| Relationship Lifecycle | Strongly survives | Authority grants/revocation |
| Revocation Revalidation | Strongly survives | Directly supported conceptually |
| Stable identifier structural Drift | Strongly survives | Authority may change independently |

---

# 60. PKI-Derived Candidate Review

| Candidate from PKI | Authority Result | Finding |
|---|---|---|
| Signed Assertion | Survives conceptually | One Evidence subtype |
| Evidence about Evidence | Survives | Attributes/status may qualify relationships |
| Evidence Graph | Strongly strengthened | Subject/Object/policy relationships form graph-like structure |
| Qualification of Lineage | Strongly survives | Delegation paths matter |
| Consumer-Local Anchor Set | Analog in applicable policy/authority set | Broadened |
| Permitted-Use Constraints | Directly central | Strongly strengthened |
| Policy-Qualified Truth State | Directly validated | Strongly strengthened |
| Role-Constrained Authority | Directly validated | Strong |
| Multi-Class Synthesis | Strongly survives | Identity + Authority + Intent + State |
| Causal Drift Dimension | Strongly survives | Policy/attribute/delegation causes differ |
| Integrity vs Operational Acceptance | Parallel becomes identity vs authorization | Strengthened |
| Trust-Configuration Drift | Analog becomes policy/authority-configuration Drift | Broadened |

Crosswalk #5 therefore confirms much of the structural direction produced by PKI.

---

# 61. Architecture Decision #1 — Promote AuthorityRelationship to Candidate Core

After four prior systems and direct evaluation in Crosswalk #5:

    DNS
      delegated authority

    IAM
      federated authority

    PKI
      certification authority

    Policy / ABAC
      authorization relationships

the abstraction:

    AuthorityRelationship

has sufficient recurring evidence to move from:

    CANDIDATE_GENERAL

to:

    CANDIDATE_CORE

Proposed conceptual fields:

    authority_relationship_id

    subject_id

    actor_id

    role

    operation

    target_scope

    delegator_id

    policy_reference

    regime_id

    valid_from

    valid_until

    constraints

    lineage_reference

    status

This is a research promotion.

Core schema changes should occur during the next formal architecture consolidation pass rather than silently inside this crosswalk.

---

# 62. Architecture Decision #2 — Promote EvidenceItem to Candidate Core

The evidence abstraction now has support from:

    NTP:
      Observation

    DNS:
      records / returned state

    IAM:
      identity evidence + assertions

    PKI:
      signed assertions + status evidence

    Authority:
      Subject/Object/environment attributes

Therefore:

    EvidenceItem

should move to:

    CANDIDATE_CORE

Potential conceptual structure:

    EvidenceItem
      ├── Observation
      ├── Assertion
      ├── SignedAssertion
      ├── Attribute
      ├── StatusEvidence
      └── Attestation

The type list should remain open.

The general abstraction is more important than prematurely fixing every subtype.

---

# 63. Architecture Decision #3 — Qualification Is Generalized

Evidence now strongly supports:

> **Qualification is not merely Observation filtering.**

Qualification may apply to:

- Evidence
- Source
- Authority relationship
- Lineage
- policy compatibility
- Regime compatibility
- requested use

Therefore the generalized mechanism should become:

    Qualification Engine

rather than conceptually:

    Observation Filter

This already matches the current component name.

The architecture interpretation should now be updated accordingly during consolidation.

---

# 64. Architecture Decision #4 — Domain Result Must Remain Separate from Qualification State

Crosswalks now repeatedly show:

    qualified absence
    authentication failure
    certificate rejection
    authorization deny

These are domain results.

They must remain separate from:

    Evaluation failed
    evidence rejected
    Truth State indeterminate

Proposed generalized structure:

    TruthState
      ├── qualification_status
      └── domain_result

Current implementation may continue using:

    status
    accepted_value

until a formal schema revision.

Status:

    CANDIDATE_CORE

---

# 65. Architecture Decision #5 — Regime and Context Should Remain Separate

Authority Truth clarifies that:

    policy / stable operating rules
      ≠
    current environmental values

Proposed distinction:

    Regime
      =
    declared operating boundary

    Context Evidence
      =
    current conditions participating in Evaluation

This avoids turning Regime into an arbitrary bag of changing values.

Status:

    CANDIDATE_GENERAL — strong

Further test:

    Distributed Systems
    Telemetry

---

# 66. Architecture Decision #6 — Decision and Enforcement Remain Separate

Crosswalk #5 provides direct validation for:

    Evaluation
      ≠
    Action

Authorization:

    decision
      ↓
    enforcement

maps cleanly into:

    Truth State
      ↓
    Correction / Action Policy
      ↓
    Mutation / Enforcement

This architectural invariant should now be considered:

    CONFIRMED_GENERAL

pending later contradiction.

---

# 67. Architecture Decision #7 — Negative Results Are First-Class

The crosswalk sequence now provides repeated evidence that:

    negative domain result
      ≠
    architectural failure

Examples:

    DNS:
      absent

    IAM:
      authentication unsuccessful

    PKI:
      validation rejected

    Authorization:
      deny

Therefore:

> **Truth-State qualification must remain independent from the polarity of the domain result.**

Status:

    CANDIDATE_CORE — strong

---

# 68. Scoring Boundary

The scoring boundary for this crosswalk is:

    System:
      Policy / Authorization / ABAC

    Primary Truth Class:
      Authority Truth

    Evaluated Scope:
      logical access-control authorization
      Subject attributes
      Object attributes
      requested operations
      environment conditions
      policy / rule evaluation
      authority relationships
      access enforcement distinction

    Primary Evidence:
      NIST SP 800-162

    Supporting Evidence:
      applicable NIST access-control guidance

    Deferred Scope:
      proprietary policy engines
      vendor-specific IAM products
      physical access control
      organization-specific governance
      risk-engine implementation details
      enforcement technologies outside the defined boundary

This boundary keeps:

    Identity Truth

and:

    Authority Truth

separate.

---

# 69. Preliminary Scoring Status

Current score status:

    provisional

Likely areas of strong structural representation include:

- Regime Awareness
- Authority / Anchor Quality
- Observation / Evidence Quality
- Correction / Enforcement Discipline
- Failure Transparency

Areas requiring careful interpretation include:

- Lineage Visibility
- Coherence Detection
- Drift Detection
- Paradox Handling
- Freshness / Revalidation

The scoring pass should follow evidence rather than expected architectural strength.

---

# 70. Provisional Scorecard Template

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

The rubric issue identified in Crosswalk #4 remains:

    Observation Quality

may eventually need to become:

    Evidence Quality

Crosswalk #5 strengthens that case.

---

# 71. Scoring-Rubric Challenge

Authority Truth puts substantial pressure on several scoring criteria.

## Anchor Quality

Authority may not derive from one Anchor in the PKI sense.

Policy may define allowable relationships.

The criterion must accommodate:

    governing reference

rather than only:

    root-like authority

## Observation Quality

Attributes, assertions, policy inputs, and environmental conditions are better described collectively as Evidence.

This is now the fourth crosswalk challenging Observation-only language.

## Coherence Detection

Policy evaluation is not necessarily Coherence detection.

The rubric must distinguish:

    constraint satisfaction

from:

    multi-Source Coherence

## Drift Detection

Policy systems may not explicitly call state changes Drift.

The scoring process must evaluate actual mechanism visibility rather than RTT interpretability alone.

## Correction Discipline

Authorization decision and access enforcement provide an excellent separation, but enforcement may be delegated outside the policy engine.

Delegation must remain visible.

---

# 72. Rubric Recommendation — Rename Observation Quality

After:

    IAM
    PKI
    Authority

the evidence for renaming:

    Observation Quality

to:

    Evidence Quality

is now substantial.

This change would preserve compatibility with NTP:

    time samples
      =
    Observational Evidence

and DNS:

    resolution / record evidence

while naturally supporting:

    assertions
    attributes
    status evidence
    attestations

## Recommendation

At the next scoring-rubric revision:

    Observation Quality
      →
    Evidence Quality

Existing crosswalks should then be reviewed for terminology consistency.

Do not silently change historical score meanings.

Version the rubric.

Status:

    RECOMMENDED_RUBRIC_REVISION

---

# 73. Crosswalk #5 Findings

## Finding 1 — Authority Is Relational

Authority belongs to a relationship among Subject, Operation, Target, policy, context, scope, and Regime.

    Status:
      CANDIDATE_CORE

## Finding 2 — Identity Does Not Imply Authority

A correctly identified Subject may still be denied an Operation.

    Status:
      CONFIRMED_GENERAL

## Finding 3 — Authority Does Not Imply Correctness

Permission to act does not establish the truth or wisdom of the action.

    Status:
      CONFIRMED_GENERAL

## Finding 4 — Authority Does Not Imply Capability

A Subject may be permitted but unable, or able but forbidden.

    Status:
      CANDIDATE_GENERAL

## Finding 5 — Policy Represents Declared Intent

Authority Truth depends on Intent Truth.

    Status:
      CANDIDATE_GENERAL

## Finding 6 — Policy Is Not the Decision

Policy requires current Evidence and context to produce an authorization result.

    Status:
      CANDIDATE_GENERAL

## Finding 7 — Authorization Decision Is Not Enforcement

Evaluation and downstream action remain distinct.

    Status:
      CONFIRMED_GENERAL

## Finding 8 — Deny Is a Valid Qualified Result

A negative domain result is not evaluation failure.

    Status:
      CANDIDATE_CORE

## Finding 9 — Delegation Preserves Constraints

Authority Lineage must preserve scope and limitations.

    Status:
      CANDIDATE_CORE

## Finding 10 — Regime Is an Evaluation Input

Policy and operational boundary directly participate in qualification.

    Status:
      CANDIDATE_GENERAL — strongly strengthened

## Finding 11 — Dynamic Context Should Remain Distinct from Stable Regime

Current environmental values are better treated as Evidence than as the Regime itself.

    Status:
      CANDIDATE_GENERAL

## Finding 12 — Evidence Is Broader Than Observation

Attributes and governed relationships reinforce EvidenceItem as the more general abstraction.

    Status:
      CANDIDATE_CORE

## Finding 13 — Truth Classes Compose

Identity, Intent, Authority, State, and Observational Truth may participate in one authorization decision without becoming one Truth Class.

    Status:
      CONFIRMED_GENERAL

## Finding 14 — Stable Identity Can Hide Authority Drift

The Subject can remain unchanged while permission structure changes.

    Status:
      CANDIDATE_GENERAL — strongly strengthened

---

# 74. Five-Crosswalk Architecture Check

After:

    NTP
    DNS
    IAM
    PKI
    Policy / Authorization

the architecture has reached its first meaningful consolidation point.

## Strongly Surviving

    Claim

    Subject

    Regime

    Evidence

    Source / Actor

    Lineage

    Qualification

    domain-semantic Coherence

    multi-dimensional Drift

    Truth State

    Revalidation

    Failure Transparency

## Promoted to Candidate Core

    EvidenceItem

    AuthorityRelationship

    domain result separate from qualification state

    constrained Authority Lineage

## Strongly Supported Invariants

    Observation ≠ Truth State

    Evidence ≠ Truth State

    Identity ≠ Authority

    Authority ≠ Correctness

    Evaluation ≠ Action

    Negative Domain Result ≠ Evaluation Failure

    Regime participates in qualification

    Lineage can participate operationally

## Under Continued Pressure

    flat Evidence lists

    global Anchor assumptions

    Source without role

    one flattened Truth-State status

    Regime containing dynamic context

    Correction terminology outside state-adjustment domains

## Narrowing Further

    Holdover as a universal mechanism

    scalar Lineage distance

    numeric Confidence as universal truth qualification

The model is becoming more relational and less value-centric.

---

# 75. Emerging Architecture After Authority Truth

The generalized pattern is now evolving toward:

    SUBJECT / ACTOR
          ↓
    CLAIM / REQUEST
          ↓
    TARGET + OPERATION
          ↓
    INTENDED USE
          ↓
    CONSUMER / OBSERVER
          ↓
    REGIME
          ↓
    AUTHORITY RELATIONSHIPS
          ↓
    EVIDENCE GRAPH
       │
       ├── Observations
       ├── Assertions
       ├── Attributes
       ├── Signed Assertions
       └── Status Evidence
          ↓
    LINEAGE + CONSTRAINTS
          ↓
    QUALIFICATION
          ↓
    DOMAIN-SEMANTIC COHERENCE
          ↓
    MULTIDIMENSIONAL DRIFT
          ↓
    PARADOX
          ↓
    DOMAIN RESULT
          ↓
    TRUTH-STATE QUALIFICATION
          ↓
    ACTION / CORRECTION POLICY
          ↓
    ENFORCEMENT / MUTATION
          ↓
    REVALIDATION
          ↓
    IMMUTABLE HISTORY

This is substantially richer than the original NTP-derived sequence.

That evolution is evidence that the crosswalk process is working.

---

# 76. First Consolidation Candidate

After five crosswalks, several concepts may be ready for a formal architecture-review pass before implementation progresses too far.

Candidate changes:

    Observation
      ↓
    EvidenceItem

with:

    Observation

remaining one Evidence subtype.

Add candidate:

    AuthorityRelationship

Consider:

    ContextEvidence

Clarify:

    TruthState.status
      =
    qualification / lifecycle

while:

    TruthState.accepted_value
      =
    domain-native result

Potentially later formalize:

    domain_result

These should be handled in a versioned architecture revision rather than patched informally across files.

---

# 77. Next Crosswalk Challenge

Crosswalk #6 examines:

    Distributed Systems
      ↓
    State Truth

The governing question becomes:

> **What is presently the case?**

This is the correct next challenge because distributed systems will pressure concepts that have so far been evaluated primarily through:

    reference
    hierarchy
    authority
    policy

Distributed systems may instead introduce:

- replicas
- quorum
- leadership
- epochs
- partitions
- state histories
- convergence
- consensus
- eventual consistency
- competing states

The central question becomes:

> **Can the Truth Service represent operational State Truth when accepted state emerges through distributed agreement rather than direct reference to one authority?**

That should be a serious test of:

    Anchor

    Authority

    Coherence

    Paradox

    Regime

and:

    Truth-State synthesis

---

# 78. Canonical Authority Truth Statement

> **Authority Truth is not a property attached permanently to an actor. It is a Regime-qualified relationship among Subject, Operation, Target, policy, attributes, scope, delegation, Lineage, context, and time that determines whether a particular action is presently permitted.**

This means:

    identified
      ≠
    authorized

    authorized
      ≠
    correct

    authorized
      ≠
    capable

    decision
      ≠
    enforcement

    deny
      ≠
    evaluation failure

Authority Truth is therefore fundamentally relational.

---

# 79. Canonical Crosswalk Finding

Crosswalk #5 demonstrates that the architecture can no longer treat authority as metadata attached to a Source.

Across four independent authority-bearing systems:

    DNS
    IAM
    PKI
    Authorization Policy

authority repeatedly appears as:

    actor
      +
    role
      +
    scope
      +
    relationship
      +
    Lineage
      +
    Regime
      +
    constraints
      +
    time

This provides the strongest evidence yet for:

    AuthorityRelationship

as a generalized architectural object.

At the same time, Authorization introduces another major distinction:

> **A system can coherently determine that an action is denied.**

Therefore:

    negative result
      ≠
    failed truth evaluation

The Truth Service must evaluate:

    quality of the relationship determination

separately from:

    polarity of the domain result

That pattern now spans:

    absence
    authentication
    certificate validation
    authorization

and appears increasingly general.

---

# 80. References

Primary technical reference:

    NIST SP 800-162
    Guide to Attribute Based Access Control (ABAC)
    Definition and Considerations

National Institute of Standards and Technology.

The reference defines ABAC as a logical access-control methodology in which authorization is determined by evaluating attributes associated with the Subject, Object, requested Operations, and, in some cases, environmental conditions against policy, rules, or relationships describing allowable operations.

Supporting access-control guidance may be introduced where the detailed Authority crosswalk requires additional bounded mechanisms.

RTT terminology, Truth Classes, Authority Relationship, Evidence Graph interpretation, Drift dimensions, Regime model, and proposed architectural generalizations remain the analytical contribution of Resonance Truth.

---

## Canonical Summary

Crosswalk #1 asked:

    When?

Crosswalk #2 asked:

    Where?

Crosswalk #3 asked:

    Who?

Crosswalk #4 asked:

    Is it intact and qualified?

Crosswalk #5 asks:

    May it act?

That progression exposes a crucial separation:

    TIME
      does not grant authority

    LOCATION
      does not grant authority

    IDENTITY
      does not grant authority

    INTEGRITY
      does not grant authority

Authority must still be evaluated.

And when it is evaluated, the answer belongs to a relationship:

    Who?

    Wants to do what?

    To which thing?

    Under which policy?

    Using which attributes?

    Through which delegation?

    Within which scope?

    Under which current conditions?

    At what time?

The answer may be:

    PERMIT

or:

    DENY

and either may represent a fully coherent operational Truth State.

That may be the cleanest result of Crosswalk #5:

> **Truth qualification is about whether the answer is structurally supported, not whether the answer is positive.**

**NTP taught truth to synchronize.**

**DNS taught it to resolve.**

**IAM taught it to identify.**

**PKI taught it to validate a chain.**

**Policy teaches it that even a perfectly identified, intact, well-qualified actor still has to ask permission.**

**Crosswalk #6 now removes the single authority from center stage and asks a distributed system what it believes the current state actually is.**
