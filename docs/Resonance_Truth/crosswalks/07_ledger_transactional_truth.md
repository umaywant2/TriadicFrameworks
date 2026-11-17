# Crosswalk #7 — Ledgers and Transactional Truth

**Module:** Resonance Truth  
**Artifact:** Operational Truth Crosswalk #7  
**Truth Class:** Transactional Truth  
**Reference System:** Transactional Ledgers / ACID Transaction Systems  
**Primary Reference Case:** PostgreSQL Transaction + Write-Ahead Log Model  
**Supporting Reference Family:** Distributed Ledgers / Settlement Systems  
**Primary RTT Dimensions:** Lineage · Temp · Coherence · Regime  
**Supporting RTT Dimensions:** Drift · State · Integrity · Authority · Paradox  
**Status:** Research Crosswalk / Architecture Challenge  
**Context:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

---

## Purpose

This crosswalk examines transactional systems and ledgers as the seventh operational reference system for the RTT Resonance Truth Service.

The governing question is:

> **What became committed?**

Crosswalk #6 established an important State Truth distinction:

    Proposed
      ≠
    Replicated
      ≠
    Committed
      ≠
    Applied

Crosswalk #7 examines the commitment boundary directly.

Transactional systems must distinguish among states such as:

- proposed
- in progress
- recorded
- committed
- rolled back
- recovered
- reconciled
- applied
- settled
- final

The central architectural question becomes:

> **When does a proposed state transition become part of the operational record, and what structural conditions make that commitment durable, ordered, auditable, reversible, or final?**

---

# 1. Evidence Boundary

The primary reference case for this crosswalk is:

    PostgreSQL
    Transaction Processing
    Write-Ahead Logging

The reference case is useful because it exposes several mechanisms relevant to Transactional Truth:

- transaction boundaries
- commit
- rollback
- write-ahead logging
- ordered log records
- durable commit state
- recovery
- materialization of committed changes
- separation between log durability and physical data-page update

The PostgreSQL WAL model establishes a particularly useful distinction:

    transaction committed
      ≠
    every changed data page already written to its final location

The log can preserve enough information for recovery.

This makes the system highly relevant to:

    commitment
    Lineage
    durability
    materialization
    recovery

The supporting reference family includes distributed ledgers and settlement systems where:

    confirmation
    commitment
    settlement
    finality

may be separately represented.

This document does not treat all ledgers as equivalent.

---

# 2. Evidence Discipline

This crosswalk distinguishes:

## Transaction-System Fact

A mechanism explicitly represented in the bounded reference material.

## RTT Interpretation

A structural interpretation introduced through Resonance Truth.

## Candidate Generalization

A mechanism potentially reusable across Truth Classes.

## Hypothesis

A proposed abstraction requiring further crosswalk evidence.

Example:

    Transaction-System Fact:
      Write-ahead logging records changes before affected
      data pages must be written to durable storage.

    RTT Interpretation:
      Commitment evidence can exist before final
      state materialization completes.

    Candidate Generalization:
      Truth-State acceptance and Truth-State
      materialization should remain separate.

    Hypothesis:
      Commitment should become a distinct generalized
      relationship in the Truth-Service data model.

Crosswalk #7 tests that hypothesis directly.

---

# 3. Why Ledgers Come Seventh

Crosswalk #6 produced several new architectural candidates:

    AcceptanceRule

    CommitmentState

    TransitionLineage

    MaterializedTruthState

    RegimeEpoch

    ReferenceBasis

    ConstitutedOperationalTruth

Transactional systems provide the natural next challenge.

A transaction has a recognizable lifecycle:

    BEGIN
      ↓
    operations
      ↓
    COMMIT

or:

    BEGIN
      ↓
    operations
      ↓
    ROLLBACK

Those paths produce different operational histories.

The state:

    transaction existed

is insufficient.

The important question is:

> **Which transitions crossed the commitment boundary?**

---

# 4. Transactional Truth

The primary Truth Class is:

    Transactional Truth

Its operational question is:

> **What became committed?**

A more complete formulation is:

> **Which proposed state transition crossed the governing commitment boundary and became part of the accepted operational history?**

Transactional Truth therefore concerns:

- transition identity
- transaction scope
- ordering
- validation
- commitment
- durability
- rollback
- recovery
- reconciliation
- settlement
- finality

It is fundamentally historical.

Transactional Truth asks not only:

    what is the state now?

but:

    which transitions legitimately produced it?

---

# 5. Transactional Truth vs State Truth

The distinction between Crosswalk #6 and Crosswalk #7 is important.

## State Truth

Asks:

> **What is presently accepted as current?**

## Transactional Truth

Asks:

> **Which transition became part of the accepted history?**

Conceptually:

    Transactional Truth
          ↓
    Accepted Transitions
          ↓
    State Truth
          ↓
    Current State

The relationship is strong.

The Truth Classes should remain separate.

---

# 6. Transaction System on Its Own Terms

A simplified transactional lifecycle is:

    BEGIN
      ↓
    Read / Write Operations
      ↓
    Validation / Constraints
      ↓
    COMMIT
      │
      ├── success
      │     ↓
      │   durable transaction state
      │
      └── failure / rollback
            ↓
          changes not committed

With write-ahead logging:

    Proposed Change
          ↓
    WAL Record
          ↓
    Durable Log
          ↓
    Commit
          ↓
    Data-Page Materialization
          ↓
    Recovery if Required

The important architectural distinction is:

> **Durable commitment can be represented through the log before every final data-page representation has been updated.**

This directly extends the Crosswalk #6 distinction between:

    committed

and:

    applied

---

# 7. Initial Structural Crosswalk

| Transaction / Ledger Concept | RTT Truth-Service Interpretation | Status |
|---|---|---|
| Transaction | Proposed bounded state transition | Strong Candidate General |
| BEGIN | Transition-scope declaration | Candidate General |
| Operation | Proposed state mutation | Strong Candidate General |
| Transaction identifier | Transition identity | Strong Candidate General |
| Constraint / validation | Qualification rule | Strong Candidate General |
| Write-ahead log | Ordered transition Lineage | Strong Candidate General |
| Log record | Transition Evidence | Strong Candidate General |
| Commit | Commitment boundary | Candidate Core |
| Rollback | Rejected / abandoned transition | Strong Candidate General |
| Durable commit | Accepted durable Transactional Truth | Strong Candidate General |
| Data-page update | Materialization | Strong Candidate General |
| Recovery / REDO | Materialization reconstruction | Strong Candidate General |
| Transaction history | Accepted transition Lineage | Candidate Core |
| Reconciliation | Coherence restoration | Strong Candidate General |
| Settlement | Higher-level acceptance boundary | Candidate General |
| Finality | Reversal boundary / commitment strength | Candidate General |
| Compensating transaction | New corrective transition | Candidate General |

Transactional systems immediately reinforce:

    commitment
      ≠
    materialization

and add:

    rollback
      ≠
    deletion of history

as an important Truth-Service concept.

---

# 8. Transaction → Proposed Bounded Transition

A transaction provides a boundary around one or more operations intended to modify system state.

RTT interpretation:

    Proposed Bounded Transition

Conceptually:

    Prior State
        ↓
    Transaction
        ↓
    Candidate State
        ↓
    Commit or Rollback

The transaction groups operations into one governed relationship.

This is stronger than:

    list of unrelated changes

The boundary itself matters.

---

# 9. Transaction Scope

Crosswalk #5 introduced Authority Scope.

Crosswalk #7 introduces:

    Transition Scope

A transaction defines which operations participate in the same commitment decision.

Conceptually:

    Transaction T
      ├── Operation A
      ├── Operation B
      └── Operation C

The resulting question is not necessarily:

    Did A succeed?
    Did B succeed?
    Did C succeed?

but:

> **Did Transaction T cross the commitment boundary as governed?**

This supports a generalized:

    grouped Evidence / grouped Transition

concept.

Status:

    CANDIDATE_GENERAL

---

# 10. Operation → Proposed State Mutation

An operation inside a transaction may modify candidate state.

RTT interpretation:

    Proposed State Mutation

This is not yet:

    Transactional Truth

The operation becomes part of the accepted history only if the transaction's governing rules allow the transaction to cross commitment.

Thus:

    operation executed
      ≠
    operation committed

This distinction is essential.

---

# 11. Executed ≠ Committed

A system may execute intermediate operations before a transaction commits.

If rollback occurs, those candidate changes do not become committed transactional history in the same sense as a successful commit.

Therefore:

> **Observation that an operation occurred during processing does not establish that its state transition became committed.**

This strongly reinforces:

    Observation
      ≠
    accepted Truth State

and:

    local / intermediate state
      ≠
    operationally committed state

---

# 12. Transaction Identity → Transition Identity

Transactional systems assign identity to bounded transitions.

RTT interpretation:

    Transition Identity

This is useful because State Truth may otherwise preserve only:

    before
    after

Transaction identity preserves:

    which transition
    produced
    which accepted change

Potential generalized fields:

    transition_id
    predecessor_state
    successor_state
    transaction_scope
    commitment_state

Status:

    CANDIDATE_GENERAL

---

# 13. Constraint Validation → Qualification

Transactions may be subject to rules and constraints.

RTT interpretation:

    Qualification

The candidate transition must satisfy applicable rules before acceptance.

Conceptually:

    Proposal
      +
    Current State
      +
    Constraints
      ↓
    Qualified / Rejected Transition

This reinforces the generalized Qualification Engine.

Qualification now applies to:

    Evidence
    Authority Relationship
    State Transition

not merely:

    Observation

Status:

    CONFIRMED_GENERAL — strong

---

# 14. Transaction Qualification vs Commit

Qualification and commitment remain separate.

A transaction may satisfy some validation steps while not yet being committed.

Therefore:

    qualified candidate
      ≠
    committed transition

Potential generalized sequence:

    Proposed
      ↓
    Qualified
      ↓
    Accepted
      ↓
    Committed

Whether every domain requires each stage remains open.

Transactional Truth shows that these distinctions can matter.

---

# 15. Write-Ahead Log → Ordered Transition Lineage

PostgreSQL's WAL records changes before data pages need to be written to their final storage locations.

RTT interpretation:

    Ordered Transition Lineage

The WAL provides structured evidence describing state changes.

Conceptually:

    Transaction T
       ↓
    WAL Records
       ↓
    Commit Record
       ↓
    Recovery / Materialization

This strongly supports the Crosswalk #6 finding:

> **Lineage includes transition history, not merely provenance ancestry.**

Status:

    CANDIDATE_CORE — strengthened

---

# 16. Transition Lineage

The generalized concept now has multiple independent reference systems.

## Provenance Lineage

    Where did this artifact / Claim originate?

## Authority Lineage

    Through which delegation path did authority emerge?

## Transition Lineage

    Through which ordered changes did this state emerge?

Crosswalk #7 makes Transition Lineage especially explicit.

Potential generalized Lineage edge semantics include:

    derives_from
    delegated_by
    transforms
    precedes
    committed_as
    applied_as
    supersedes
    compensates

This strengthens graph-based Lineage.

---

# 17. Log Record → Transition Evidence

A WAL record is evidence about a state transition.

RTT interpretation:

    Transition Evidence

This further strengthens the generalized:

    EvidenceItem

model.

Potential evidence roles now include:

    Observation
    Assertion
    Attribute
    Status Evidence
    Proposal Evidence
    Replication Evidence
    Transition Evidence

The EvidenceItem abstraction appears increasingly justified.

Status:

    CANDIDATE_CORE — strongly strengthened

---

# 18. Evidence Can Describe Change

Early crosswalks often treated Evidence as describing:

    state

Transactional systems show Evidence may instead describe:

    transition

This is important.

The Truth Service should support evidence about:

    what is

and:

    what changed

and:

    what was proposed to change

and:

    what became committed

Therefore the Evidence Graph must support both:

    state nodes

and:

    transition nodes / relationships

---

# 19. Commit → Commitment Boundary

Crosswalk #6 introduced Commitment as a candidate generalized boundary.

Transactional systems make the concept direct.

RTT interpretation:

    Commitment Boundary

Definition:

> **The structural point at which a proposed transition becomes part of the system's accepted operational history under the governing rules.**

This does not necessarily mean:

    irreversible forever

It means:

    committed under this transaction Regime

That distinction becomes important when discussing:

    rollback
    compensation
    settlement
    finality

---

# 20. Commitment Is Not Finality

This distinction is critical.

A committed transaction may become part of accepted history.

A later operation may:

- compensate for it
- reverse its effects through a new transaction
- reconcile it
- supersede related state

Therefore:

    committed
      ≠
    metaphysically irreversible

The correct generalized meaning is:

> **The transition crossed the governing commitment boundary.**

Finality is a separate property.

---

# 21. Commit as Constituted Operational Truth

Crosswalk #6 introduced:

    Constituted Operational Truth

Transactional systems strongly reinforce it.

Before commit:

    transition is proposed

After valid commit:

    transition is part of accepted transactional history

The commit process itself establishes that operational fact.

Therefore:

> **Transactional Truth may be constituted by successful execution of accepted system rules.**

Status:

    CANDIDATE_CORE — strengthened

---

# 22. Durable Commit

PostgreSQL WAL provides a useful distinction between:

    commit

and:

    final data-page materialization

The WAL may preserve sufficient durable information to recover committed changes.

RTT interpretation:

    Durable Commitment

This suggests commitment may possess attributes such as:

    accepted
    durable
    materialized
    settled
    final

These should not automatically become separate generic TruthStatus values.

They may instead belong to:

    domain_result

or:

    commitment descriptor

---

# 23. CommitmentDescriptor Candidate

Potential generalized object:

    CommitmentDescriptor

Possible fields:

    state:
      uncommitted | committed

    durable:
      true | false | unknown

    materialized:
      true | false | partial | unknown

    settled:
      true | false | not_applicable | unknown

    finality:
      reversible | bounded | final | unknown

    committed_at:
      ...

    reference_basis:
      ...

    evidence:
      [...]

This is intentionally provisional.

Crosswalk #7 provides strong evidence for commitment semantics, but not yet for one universal descriptor across every Truth Class.

Status:

    CANDIDATE_CORE

---

# 24. Commit ≠ Materialization

This finding now has independent support from:

    Distributed State
    Transaction Systems

Conceptually:

    accepted transition
        ↓
    committed
        ↓
    durable transition evidence
        ↓
    local state materialization

A crash may interrupt materialization.

Recovery can reconstruct state from durable transition information.

Therefore:

> **Accepted history can remain valid even when its current physical representation requires reconstruction.**

This is a major generalized Truth-Service principle.

---

# 25. MaterializedTruthState Strengthened

DNS introduced local cached state.

Distributed consensus introduced applied replica state.

Transactional systems introduce database-page materialization.

Three different domains now support:

    accepted Truth State
          ↓
    operational materialization

Potential materializations can:

- lag
- expire
- become stale
- require recovery
- be reconstructed
- differ temporarily from accepted history

Therefore:

    MaterializedTruthState

moves from:

    CANDIDATE_CORE

toward:

    STRONG CANDIDATE_CORE

Formal promotion should wait for architecture consolidation.

---

# 26. Rollback → Abandoned Transition

If a transaction does not commit and is rolled back, candidate changes do not become part of committed Transactional Truth.

RTT interpretation:

    Abandoned Transition

Important distinction:

    rollback
      ≠
    transition never existed as an attempted operation

The attempted transaction may remain visible in:

- logs
- audit
- diagnostics
- transaction metadata

But:

    committed history

does not include its intended state mutation as a successful committed transition.

This supports immutable audit history.

---

# 27. Rollback ≠ History Erasure

This is an important Truth-Service principle.

A failed or rolled-back Evaluation / transition should not necessarily disappear.

Conceptually:

    Transaction attempted
        ↓
    Qualification / execution
        ↓
    Rollback
        ↓
    State effect removed / not committed

while:

    historical evidence of attempt
        remains

This is analogous to:

    rejected Observation retained

and:

    dissent preserved

The system should distinguish:

    operational state history

from:

    audit history

---

# 28. Accepted History vs Audit History

Transactional systems expose two related but different histories.

## Accepted State History

Transitions that became committed.

## Audit History

May additionally include:

- attempted transitions
- rejected transitions
- rollback
- failures
- compensating actions

Potential architecture:

    TransitionLineage

with edge/state metadata describing:

    proposed
    rejected
    committed
    rolled_back
    compensated

This may be sufficient without introducing separate history stores conceptually.

---

# 29. Recovery → Materialization Reconstruction

PostgreSQL uses WAL during crash recovery to redo changes that have not yet been applied to data pages.

RTT interpretation:

    Truth-State Materialization Reconstruction

The accepted transactional history provides enough evidence to reconstruct operational materialization.

This yields a powerful general principle:

> **Truth State and its materialization can be separated strongly enough that a damaged or incomplete materialization can be reconstructed from accepted Lineage.**

Potential applications later may include:

- desired-state controllers
- replicated state
- caches
- derived views
- indexes

Status:

    CANDIDATE_GENERAL — strong

---

# 30. Recovery Does Not Re-Decide Commitment

Conceptually, recovery should not arbitrarily reconsider every committed transition from scratch.

It uses preserved transaction history to restore materialization.

RTT interpretation:

    Accepted History
          ↓
    Reconstruction

rather than:

    Re-evaluate original Claim from zero

This is important.

Revalidation and recovery are not the same operation.

---

# 31. Recovery ≠ Revalidation

## Recovery

Restores operational materialization from already accepted history.

## Revalidation

Challenges whether a previously accepted Truth State remains qualified under changed evidence or Regime.

These must remain separate.

Potential example:

    crash
      ↓
    recovery
      ↓
    same accepted transaction history

versus:

    policy change
      ↓
    Revalidation
      ↓
    changed qualification

Crosswalk #7 therefore introduces a new important distinction.

Status:

    CANDIDATE_GENERAL

---

# 32. Reconciliation → Coherence Restoration

Ledgers often require reconciliation between records or states.

RTT interpretation:

    Coherence Restoration

Conceptually:

    Record A
       ↕
    Record B
       ↓
    compare
       ↓
    difference
       ↓
    explanation / correction / adjustment

The system attempts to identify whether differing records represent:

- timing difference
- missing transition
- duplicate transition
- conflicting state
- error
- legitimate separate Regime

Reconciliation therefore combines:

    Coherence
    Drift
    Lineage
    Correction

---

# 33. Reconciliation Is Not Averaging

If two ledgers disagree:

    Ledger A:
      transaction exists

    Ledger B:
      transaction missing

The correct response is not:

    transaction half-exists

The system must determine:

- Source
- authority
- commitment state
- Lineage
- ordering
- Regime
- timing

This provides another strong example that:

> **Coherence analysis must remain semantic and structural.**

---

# 34. Duplicate Transaction → Evidence vs Domain State

Transactional systems may encounter duplicate requests or duplicate records.

This creates another useful distinction.

Two Evidence Items may refer to:

    the same intended transition

Therefore:

    Evidence count
      ≠
    transition count

This parallels:

    three DNS caches
      ≠
    three independent authorities

and:

    three Sources sharing Lineage
      ≠
    three independent confirmations

Identity and deduplication matter.

---

# 35. Transaction Identity and Idempotence

A system may need to determine whether two requests represent:

    same transition

or:

    separate transitions

RTT interpretation:

    Transition Identity / Equivalence

This may become important to:

    Coherence

and:

    Transactional Drift

Potential generalized question:

> **Are these two Evidence Items about the same operational event?**

This is another reason Truth Subjects and transition identifiers matter.

---

# 36. Ordering → Transactional Lineage

Transactions may need ordering.

RTT interpretation:

    Ordered Transition Lineage

State may depend not only on:

    which transitions

but also:

    in which order

Conceptually:

    T1
      ↓
    T2
      ↓
    T3

may produce a different state from:

    T2
      ↓
    T1
      ↓
    T3

Therefore:

> **Lineage ordering can itself be part of Truth.**

This becomes central to Transactional Truth.

---

# 37. Order Truth

Crosswalk #7 reveals a possible subdimension:

    Ordering Truth

Question:

> **In what accepted order did these transitions occur?**

This may belong inside:

    Transactional Truth

rather than becoming an eleventh top-level Truth Class.

Status:

    DOMAIN_SPECIFIC / CANDIDATE SUBDIMENSION

No new canonical Truth Class is recommended.

---

# 38. Settlement

Some transactional systems distinguish:

    transaction committed

from:

    transaction settled

Settlement may represent a later operational boundary at which obligations or transfers are treated as completed under another Regime.

RTT interpretation:

    Secondary Acceptance Boundary

Conceptually:

    Proposed
      ↓
    Accepted
      ↓
    Committed
      ↓
    Settled

Not every transaction system uses this lifecycle.

Therefore settlement remains domain-specific.

The broader generalized lesson is:

> **One process may contain multiple meaningful acceptance boundaries.**

---

# 39. Finality

Distributed ledger systems often distinguish confirmation/commitment from finality.

For this crosswalk, finality is treated generically as:

> **The degree or boundary beyond which an accepted transition is no longer expected or permitted to be reversed under the governing system.**

This should not be assumed identical across all systems.

Possible forms include:

- deterministic finality
- probabilistic finality
- policy finality
- settlement finality
- practical irreversibility

The generalized architecture should preserve:

    commitment
      ≠
    finality

---

# 40. Finality Is Regime-Specific

A transaction may be considered sufficiently final for:

    low-consequence display

before it is sufficiently final for:

    high-consequence settlement

Therefore:

    finality requirement

may belong partly to:

    Regime

while:

    finality state

belongs to:

    domain result / Commitment Descriptor

This parallels earlier:

    freshness
    assurance
    trust

relationships.

---

# 41. Commitment Strength

Rather than forcing all systems into:

    committed = true/false

the architecture may eventually support:

    commitment state
      +
    finality characteristics

Potential representation:

    commitment:
      state: committed
      durability: durable
      finality: bounded
      reversal_model: compensating_transition

This remains provisional.

Status:

    CANDIDATE_GENERAL

---

# 42. Reversal vs Rollback

These should remain distinct.

## Rollback

The candidate transaction does not become committed.

## Reversal

A previously committed effect is later altered by another accepted transition.

Conceptually:

    T1:
      committed

then:

    T2:
      reverses / compensates T1

The historical fact remains:

    T1 committed

The later state is:

    effects changed by T2

This is crucial for immutable history.

---

# 43. Reversal Does Not Make Prior Commitment False

Suppose:

    Transaction A:
      committed

Later:

    Transaction B:
      reverses effect of A

It would be incorrect to rewrite history as:

    Transaction A never committed

The correct Lineage is:

    A
      committed
        ↓
    B
      corrective transition

This strongly supports append-oriented Truth-State history.

---

# 44. Compensating Transaction → Corrective Transition

Some systems correct prior effects through a new transaction rather than rewriting prior committed history.

RTT interpretation:

    Corrective Transition

This is a powerful generalized Correction pattern.

Earlier Correction examples included:

    NTP:
      clock discipline

    DNS:
      cache replacement

    Distributed State:
      replica reconciliation

Transactional systems add:

    append new corrective event

Therefore Correction itself has multiple forms.

---

# 45. Correction Taxonomy Candidate

Potential generalized Correction families:

    MUTATE LOCAL STATE
      e.g. adjust clock

    REPLACE MATERIALIZATION
      e.g. refresh cache

    RECONCILE WITH ACCEPTED HISTORY
      e.g. replica recovery

    APPEND CORRECTIVE TRANSITION
      e.g. compensating transaction

    RESTRICT ACTION
      e.g. authorization deny

    ESCALATE
      e.g. human review

This taxonomy may be more useful than a flat correction-mode enum eventually.

Status:

    CANDIDATE_GENERAL

Do not revise the schema yet.

---

# 46. Transactional Drift

Potential Drift dimensions include:

## State Drift

Materialized state differs from committed state.

## Lineage Drift

Expected transition history differs.

## Ordering Drift

Recorded ordering differs.

## Reconciliation Drift

Independent ledgers disagree.

## Policy Drift

Transaction validity rules change.

## Settlement Drift

Upstream commit and downstream settlement differ.

## Materialization Drift

Data pages / derived views lag accepted history.

Once again:

    Drift

survives strongly,

while its domain expression changes.

---

# 47. Stable Balance, Changed History

Consider two states displaying:

    balance = 100

State A arose through:

    +50
    +50

State B arose through:

    +100

The final value is identical.

The Transactional Lineage differs.

Therefore:

> **Identical present state does not imply identical Transactional Truth.**

This is another powerful example of:

    stable value
      ≠
    stable structure

That finding is now deeply generalized.

---

# 48. Transactional Coherence

Coherence may involve:

- consistent transaction boundaries
- accepted ordering
- valid constraints
- durable commitment
- compatible history
- reconciliation across records
- no conflicting accepted transitions under the same rules

Again:

    Coherence
      ≠
    equality alone

It concerns structural compatibility.

This continues to reinforce domain-semantic Coherence as a core principle.

---

# 49. Transactional Paradox

Potential Transactional Paradox arises when:

- two equally qualified histories claim incompatible commitments
- ordering cannot be reconciled
- two authoritative ledgers claim mutually incompatible settlement
- commitment state differs without a valid Regime distinction

Before registering Paradox, classify:

    pending?

    committed?

    rolled back?

    compensated?

    different Regime?

    stale materialization?

    reconciliation delay?

    different finality threshold?

Only unresolved structural incompatibility should become Paradox.

---

# 50. Pending ≠ Contested

A transaction may simply be:

    pending

This does not necessarily mean:

    contested

Likewise:

    uncommitted

does not mean:

    false

The domain lifecycle must remain visible.

This strongly supports keeping:

    domain result

separate from:

    Truth-State qualification

---

# 51. Rolled Back ≠ Rejected Evidence

A transaction may be rolled back because the transition was not committed.

The Evidence describing:

    attempted transaction

may remain completely valid.

Therefore:

    transaction effect rejected
      ≠
    Evidence rejected

This is an important layer distinction.

The Truth Service may coherently accept:

> Transaction T was attempted and rolled back.

That itself is Transactional Truth.

---

# 52. Truth About Failure

Transactional systems make a subtle but valuable point:

    failed transaction

can still generate:

    true transactional history about the failure

Example:

    Transaction T
      status: rolled_back

The statement:

> Transaction T did not commit.

may be:

    operationally_accepted

Therefore negative lifecycle states are themselves truth-bearing.

This strongly reinforces the Crosswalk #5 result:

> **Truth qualification is independent of domain-result polarity.**

---

# 53. Durability

Durability concerns preservation of committed state across failure.

RTT interpretation:

    Persistence of Committed Truth

This maps strongly to:

    Spin

The accepted transition must survive disturbance sufficiently for the system's guarantees.

This gives Spin one of its clearest operational manifestations:

> **The committed relationship persists across failure and recovery.**

---

# 54. Durability Is Not Freshness

A durable transaction may be old.

A fresh transaction may not yet be committed.

Therefore:

    durability
      ≠
    freshness

These should remain separate dimensions.

Potential Truth-Service descriptors:

    freshness

    durability

    finality

all answer different questions.

This argues against overloading one generic:

    confidence

or:

    validity

field.

---

# 55. Durability Is Not Finality

Likewise:

    durable
      ≠
    irreversible under every future operation

A durable transaction may later be counteracted through another transaction.

Therefore:

    persistence of recorded commitment

and:

    impossibility of future reversal

must remain distinct.

---

# 56. Reference Basis in Transactional Truth

Crosswalk #6 challenged:

    Anchor

and proposed:

    ReferenceBasis

Transactional systems strengthen that challenge.

What forms the reference basis for Transactional Truth?

Potential components include:

    transaction protocol
    constraint rules
    write-ahead log
    accepted history
    recovery semantics

No single external Source necessarily declares:

    this transaction committed

Instead, commitment is established through:

    governed transaction procedure

This strongly supports:

    ReferenceBasis

as broader than:

    Truth Anchor

Status:

    CANDIDATE_CORE

---

# 57. Reference Basis Candidate Structure

Potential conceptual model:

    ReferenceBasis
      ├── type
      ├── authority / governing system
      ├── policy / protocol reference
      ├── accepted-history reference
      ├── Regime
      ├── version
      └── constraints

Potential types:

    external_anchor
    governing_policy
    governing_protocol
    accepted_history
    measurement_standard

This model now has support from:

    NTP
    DNS
    PKI
    Authority
    Distributed State
    Transactions

through different expressions.

---

# 58. AcceptanceRule Strengthened

Distributed systems introduced:

    AcceptanceRule

Transactional systems make it concrete again.

A transaction becomes committed only when the governing transaction mechanism reaches the required commitment condition.

General form:

> **AcceptanceRule defines the structural conditions required for a domain result to cross into operational acceptance.**

Examples:

    Temporal:
      Source-selection / qualification rules

    DNS:
      authority + freshness rules

    IAM:
      proofing/authentication rules

    PKI:
      path-validation rules

    Authority:
      policy evaluation

    Distributed State:
      quorum / commit rule

    Transaction:
      transaction commit rule

Status:

    CANDIDATE_CORE — strongly strengthened

---

# 59. CommitmentState Strengthened

Crosswalk #6 introduced:

    CommitmentState

Crosswalk #7 directly validates the need to distinguish:

    uncommitted
    committed

and potentially:

    rolled_back
    compensated
    settled
    final

However, these values mix lifecycle concepts.

Recommendation:

Do not create one oversized generic enum.

Instead consider:

    TransitionState

plus:

    CommitmentDescriptor

during consolidation.

Status:

    CANDIDATE_CORE

---

# 60. Transactional Regime

A Transactional Truth Regime may include:

- transaction semantics
- isolation requirements
- constraint rules
- durability requirements
- recovery behavior
- settlement requirements
- finality threshold
- application policy

The same transition may have different operational interpretations under different transaction systems.

Therefore:

    committed under Regime A

must not be silently translated into:

    final under Regime B

Regime qualification remains essential.

---

# 61. Isolation as Observer Context

Transactions also raise an observer-related issue.

Concurrent transactions may have different permitted views of state depending on isolation semantics.

RTT interpretation:

    Observer-Scoped State View

This connects strongly to:

    Observer Context

introduced by DNS and strengthened by IAM / PKI.

Potential architecture candidate:

    StateView

with:

    observer
    evaluation point
    regime
    visible state
    lineage

Status:

    CANDIDATE_GENERAL — strengthened

---

# 62. State View ≠ Global State

A transaction's visible state may be a valid operational view without representing:

    every concurrent change everywhere

Therefore:

> **A coherent observer-scoped state can remain valid inside its Regime without being identical to all other simultaneous views.**

This will matter later in:

    Telemetry
    Observational Truth

and potentially:

    Desired-State Systems

---

# 63. Transactional Truth and Authority

Who may commit?

Who may initiate?

Who may reconcile?

Who may reverse?

These are Authority Truth questions.

Transactional Truth therefore composes with:

    Authority Truth

but does not collapse into it.

A transition may be:

    correctly committed

only if relevant authority conditions are satisfied under the transaction system.

Again, Truth Classes compose.

---

# 64. Transactional Truth and Integrity

The transaction record may require integrity mechanisms.

But:

    intact log record
      ≠
    transaction valid

An invalid transaction could be perfectly preserved.

Therefore:

    Integrity Truth
      ≠
    Transactional Truth

This repeats the pattern established by PKI.

Integrity describes preservation.

Transactional Truth describes accepted transition status.

---

# 65. Transactional Truth and Intent

A transaction expresses:

    intended state change

Commit determines whether it became:

    accepted transition

Therefore:

    Intent Truth
      ↓
    proposed transition

    Transactional Truth
      ↓
    committed transition

    State Truth
      ↓
    resulting current state

This gives us perhaps the cleanest three-class chain yet:

    INTENT
      ↓
    TRANSACTION
      ↓
    STATE

Crosswalk #8 will examine the first element directly.

---

# 66. Worked Example — Successful Commit

## Prior State

    State S0

## Transaction

    T1

## Proposed Operations

    O1
    O2

## Qualification

    transaction constraints satisfied

## Commit

    successful

## Durable Evidence

    applicable WAL records persisted according to the transaction mechanism

## Resulting Transactional Truth

    Truth State:
      operationally_accepted

    domain_result:
      transaction: T1
      commitment: committed

## Materialization

    may occur or complete separately

## Architectural Finding

Commit establishes Transactional Truth before every final physical materialization must necessarily be complete.

---

# 67. Worked Example — Rollback

## Prior State

    State S0

## Transaction

    T2

## Candidate Operations

    O1
    O2

## Outcome

    rollback

## Transactional Truth

    Truth State:
      operationally_accepted

    domain_result:
      transaction: T2
      commitment: rolled_back

## Current State

    committed effects of T2 are absent

## Audit History

    T2 was attempted

## Architectural Finding

The Truth Service can coherently accept the fact that:

> T2 did not commit.

A negative transaction outcome remains Truth.

---

# 68. Worked Example — Crash After Commit

## Transaction

    T3

## Commit

    successfully established under the transaction system

## Failure

    system crash occurs before all affected data pages are fully materialized

## Recovery

    accepted WAL history is used to restore the committed state

## Transactional Truth

    T3 remains committed

## Materialization State

    reconstructed during recovery

## Architectural Finding

Commitment and materialization are separate.

Durable accepted Lineage can reconstruct materialization.

---

# 69. Worked Example — Compensating Transaction

## Transaction T4

    committed

## Later Discovery

The operational effect must be corrected.

## Transaction T5

    committed
    compensates T4

## Correct History

    T4:
      committed

    T5:
      committed
      corrective_relation: compensates T4

## Incorrect History

    T4:
