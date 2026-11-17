<img width="1194" height="672" alt="Resonance_Truth_crosswalks_scoring_criteria_" src="https://github.com/user-attachments/assets/83d741f8-379b-46f3-ad69-c83ab35bd0ea" />

# Operational Truth Systems — Scoring Criteria

**Module:** Resonance Truth  
**Artifact:** Operational Truth-System Scoring Criteria  
**Framework:** Resonance-Time Theory (RTT)  
**Status:** Research Scoring Specification  
**Context:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

---

## Purpose

This document defines the common scoring model used to evaluate operational truth reference systems in the Resonance Truth crosswalk series.

The scoring model asks:

> **How explicitly does a system expose and govern the structural conditions surrounding its operational relationship to truth?**

It does not attempt to measure:

- absolute truth
- philosophical truth
- popularity
- adoption
- implementation size
- system age
- code quality
- security quality
- organizational maturity

The score applies specifically to the architectural mechanisms by which a system establishes, maintains, qualifies, challenges, corrects, or relinquishes an operational truth state.

---

# 1. Systems Covered

The initial scoring framework applies to the ten reference systems in the Operational Truth crosswalk series.

| # | Reference System | Primary Truth Class |
|---:|---|---|
| 1 | NTP | Temporal Truth |
| 2 | DNS | Locational Truth |
| 3 | IAM | Identity Truth |
| 4 | PKI / cryptographic verification | Integrity Truth |
| 5 | Policy / IAM | Authority Truth |
| 6 | Distributed systems | State Truth |
| 7 | Ledgers | Transactional Truth |
| 8 | Desired-state systems | Intent Truth |
| 9 | Telemetry | Observational Truth |
| 10 | Supply-chain provenance | Lineage Truth |

These systems are not presumed equivalent.

The scoring framework exists to expose their structural differences.

---

# 2. Scoring Principle

The score does not answer:

> **How true is this system?**

It asks:

> **How much of the system's operational truth relationship is explicitly represented, observable, governed, and recoverable?**

The scoring dimensions are:

1. Anchor Quality
2. Lineage Visibility
3. Observation Quality
4. Coherence Detection
5. Drift Detection
6. Paradox Handling
7. Regime Awareness
8. Freshness / Revalidation
9. Correction Discipline
10. Failure Transparency

Each criterion receives:

    0–5

Maximum raw score:

    50

An optional normalized representation may be calculated as:

    raw_score × 2 = score / 100

The raw structural profile remains more important than the normalized total.

---

# 3. Common Scoring Scale

| Score | Classification | Meaning |
|---:|---|---|
| **0** | Absent | The mechanism is not meaningfully represented and no explicit delegation is identified |
| **1** | Implicit | The system depends on the property, but representation or governance is largely implicit |
| **2** | Partial | Some explicit mechanism exists, but coverage, visibility, or integration is limited |
| **3** | Operational | The mechanism is explicit and usable during normal operation |
| **4** | Strong | The mechanism is systematic, inspectable, and integrated into operational behavior |
| **5** | Structural | The mechanism is fundamental to architecture and directly governs accepted operational state |

A score represents the strength of the mechanism within the scope being evaluated.

---

# 4. Structural Delegation

A system may intentionally delegate a truth function to another layer.

For example, a narrowly scoped system may rely on an external mechanism for:

- identity
- authority
- time
- integrity
- provenance
- correction
- failure handling

This creates an important distinction:

    ABSENT
      ≠
    DELEGATED

A delegated mechanism should not automatically receive a higher numeric score.

Instead, delegation should be recorded separately.

## Delegation Status

Each criterion may optionally carry one of the following:

    native
    delegated
    hybrid
    unknown

### Native

The mechanism is implemented substantially within the evaluated system.

### Delegated

The evaluated system explicitly relies on another layer for the mechanism.

### Hybrid

Responsibility is shared between the evaluated system and another layer.

### Unknown

Available evidence does not establish where responsibility resides.

## Scoring Rule

The numeric score evaluates the mechanism visible within the defined evaluation boundary.

The delegation status explains why that score has its shape.

This prevents:

> **The mechanism is intentionally external**

from being misreported as:

> **The system forgot to implement the mechanism.**

---

# 5. Evidence Requirement

Every score must include:

- numeric value
- classification
- rationale
- evidence
- delegation status where relevant

A score without rationale and evidence is structurally incomplete.

Recommended representation:

    criterion:
      drift_detection

    score:
      5

    classification:
      structural

    delegation:
      native

    rationale:
      The system directly represents displacement between
      local state and qualified reference state.

    evidence:
      - specification reference
      - implementation reference
      - test reference

---

# 6. Evidence Types

Evidence supporting a score should be classified.

Initial evidence types are:

    specification
    implementation
    documentation
    test
    observation
    analysis

## Specification

Normative technical specification or standard.

## Implementation

Observable implementation structure or source behavior.

## Documentation

Official project or system documentation.

## Test

Repeatable behavior demonstrated through deterministic or documented testing.

## Observation

Directly observed system behavior.

## Analysis

RTT crosswalk interpretation based on the available evidence.

## Evidence Discipline

Whenever possible:

    specification / implementation / documentation / test / observation

should support:

    analysis

rather than:

    analysis

being used as its own sole factual basis.

---

# 7. Criterion 1 — Anchor Quality

## Governing Question

> **How clearly can the system identify the reference against which an operational truth claim is evaluated?**

Evaluate whether the system exposes:

- identifiable reference
- authority
- scope
- validity
- replacement
- revocation
- applicable domain
- applicable Regime

## Scoring

| Score | Condition |
|---:|---|
| **0** | No meaningful Anchor is identifiable within the evaluated scope |
| **1** | A reference is assumed or informal |
| **2** | An Anchor exists, but authority, scope, or lifecycle is weakly represented |
| **3** | Anchor identity and authority are explicitly represented |
| **4** | Anchor identity, authority, scope, and lifecycle are systematically governed |
| **5** | Anchor structure directly governs qualification or accepted operational state |

## RTT Relationship

    Spin
    Regime
    Authority

## Crosswalk Questions

- What counts as the reference?
- Who establishes the reference?
- Where is it authoritative?
- When does that authority begin or end?
- Can the Anchor be changed?
- Can it be withdrawn?
- Can it be revoked?
- Can more than one Anchor apply?

---

# 8. Criterion 2 — Lineage Visibility

## Governing Question

> **Can the system explain how accepted operational state derives from its Sources and references?**

Evaluate:

- provenance
- Source relationships
- delegation
- dependency paths
- transformations
- intermediaries
- distance from Anchor
- historical traceability

## Scoring

| Score | Condition |
|---:|---|
| **0** | Origin cannot meaningfully be reconstructed |
| **1** | Immediate Source may be known, but deeper provenance is unavailable |
| **2** | Partial provenance or dependency information exists |
| **3** | Meaningful Lineage can be reconstructed |
| **4** | Lineage is explicit, inspectable, and used operationally |
| **5** | Lineage directly participates in qualification, acceptance, or rejection |

## RTT Relationship

    Spin
    Lineage
    Drift

## Crosswalk Questions

- Where did the operational state originate?
- Can intermediate Sources be identified?
- Are transformations visible?
- Are dependencies visible?
- Can shared Source ancestry be detected?
- Is distance from reference represented?
- Does Lineage influence acceptance?

---

# 9. Criterion 3 — Observation Quality

## Governing Question

> **How well does the system qualify the evidence used to establish operational state?**

Evaluate:

- Observation identity
- Source identity
- integrity
- precision
- collection conditions
- freshness
- duplication
- malformed evidence
- instability
- suitability

## Scoring

| Score | Condition |
|---:|---|
| **0** | Observations are consumed without meaningful qualification |
| **1** | Minimal or implicit validation occurs |
| **2** | Limited filtering or validation exists |
| **3** | Observations are explicitly qualified before operational use |
| **4** | Multiple quality dimensions systematically affect qualification |
| **5** | Observation qualification is fundamental to accepted-state synthesis |

## RTT Relationship

    Resonance
    Elec
    Observation

## Crosswalk Questions

- What counts as an Observation?
- Is Source identity known?
- Is integrity checked?
- Is precision represented?
- Is freshness evaluated?
- Can stale Observations be excluded?
- Can malformed Observations be rejected?
- Can duplicated evidence be detected?

---

# 10. Criterion 4 — Coherence Detection

## Governing Question

> **Can the system determine whether qualified observations or participants support a mutually usable operational state?**

Evaluate:

- comparison
- corroboration
- consistency
- clustering
- dependency awareness
- Source diversity
- agreement
- dissent

## Scoring

| Score | Condition |
|---:|---|
| **0** | No meaningful agreement evaluation is present |
| **1** | Consistency is largely assumed |
| **2** | Basic comparison or agreement checking exists |
| **3** | Coherence is explicitly evaluated |
| **4** | Multiple Sources, dependencies, or clusters are systematically considered |
| **5** | Coherence directly governs accepted operational state |

## RTT Relationship

    C1
    C2
    C3
    C4

## Crosswalk Questions

- Are Observations compared?
- Does agreement matter?
- Are Sources treated independently?
- Can common upstream dependency be detected?
- Can clusters form?
- Can dissent remain visible?
- Can the system distinguish majority from meaningful corroboration?

---

# 11. Criterion 5 — Drift Detection

## Governing Question

> **Can the system detect displacement between reference, expected, observed, historical, or accepted state?**

Evaluate:

- local vs reference state
- previous vs current state
- expected vs observed state
- declared vs actual state
- Source changes
- Lineage changes
- policy changes
- accumulated divergence

## Scoring

| Score | Condition |
|---:|---|
| **0** | Drift is not meaningfully observable |
| **1** | Drift generally appears only after failure or external detection |
| **2** | Some differences can be identified |
| **3** | Drift is explicitly observable |
| **4** | Drift can be classified or measured systematically |
| **5** | Drift directly affects qualification, Correction, or Regime transition |

## RTT Relationship

    D1
    D2
    D3
    D4

## Crosswalk Questions

- What states can be compared?
- Is magnitude available?
- Is direction available?
- Can qualitative Drift be represented?
- Can Drift accumulate?
- Does Drift affect accepted state?
- Can the system distinguish expected change from uncontrolled divergence?

---

# 12. Criterion 6 — Paradox Handling

## Governing Question

> **What happens when individually qualified states disagree?**

Evaluate whether the system can:

- preserve competing evidence
- detect contradiction
- identify outliers
- form separate clusters
- separate by Regime
- escalate conflict
- avoid premature collapse
- declare indeterminacy

## Scoring

| Score | Condition |
|---:|---|
| **0** | Contradiction is ignored or overwritten without meaningful representation |
| **1** | One state replaces another with little preserved conflict information |
| **2** | Conflict can be detected |
| **3** | Conflict is explicitly represented |
| **4** | Competing qualified states can be contained and inspected |
| **5** | Contradiction is preserved structurally until evidence or Regime justifies resolution |

## RTT Relationship

    P1
    P2
    P3

## Crosswalk Questions

- Can valid Sources disagree?
- Is disagreement visible?
- Can multiple coherent clusters coexist?
- Does the system force one answer?
- Can it return no answer?
- Can contradiction be separated by Regime?
- Are losing states still auditable after resolution?

---

# 13. Criterion 7 — Regime Awareness

## Governing Question

> **Does the system represent the operational boundary within which its accepted state remains valid?**

Evaluate:

- scope
- context
- namespace
- jurisdiction
- policy
- trust domain
- observer position
- epoch
- security context
- consequence level

## Scoring

| Score | Condition |
|---:|---|
| **0** | Operational truth is effectively treated as context-free |
| **1** | Context matters but remains mostly implicit |
| **2** | Some operational boundaries are represented |
| **3** | The governing Regime is explicitly identifiable |
| **4** | Regime directly qualifies interpretation or acceptance |
| **5** | Regime boundaries and transitions directly govern Truth-State behavior |

## RTT Relationship

    Regime
    Elec
    Temp

## Crosswalk Questions

- Where does the result apply?
- Who is the observer?
- Which policy applies?
- Which namespace applies?
- Does location affect the result?
- Does time alter the Regime?
- Can the same evidence produce different operational outcomes under different Regimes?
- Are Regime transitions explicit?

---

# 14. Criterion 8 — Freshness / Revalidation

## Governing Question

> **How does the system determine whether previously accepted operational state remains sufficiently current?**

Evaluate:

- observation age
- expiration
- validity intervals
- polling
- refreshing
- re-observation
- revocation
- stale-state detection
- Revalidation triggers

## Scoring

| Score | Condition |
|---:|---|
| **0** | Accepted state has no meaningful freshness lifecycle |
| **1** | Freshness depends largely on external or manual intervention |
| **2** | Basic expiration, refresh, or validity behavior exists |
| **3** | Operational state is explicitly Revalidated |
| **4** | Revalidation responds systematically to time or state changes |
| **5** | Freshness is a first-class part of accepted-state lifecycle and governance |

## RTT Relationship

    Temp
    Drift
    Lifecycle

## Crosswalk Questions

- Can an earlier accepted state become stale?
- How is staleness determined?
- Can accepted state expire?
- Is refresh periodic?
- Can events trigger Revalidation?
- Does Source change trigger Revalidation?
- Does Anchor change trigger Revalidation?
- Can uncertainty grow as evidence ages?

---

# 15. Criterion 9 — Correction Discipline

## Governing Question

> **How does the system respond when better-supported operational state differs from current local state?**

Evaluate:

- immediate replacement
- gradual convergence
- reconciliation
- rollback
- quarantine
- dual-state operation
- holdover
- escalation
- bounded adjustment

## Scoring

| Score | Condition |
|---:|---|
| **0** | No defined Correction mechanism is visible |
| **1** | Replacement occurs without substantial governance |
| **2** | Basic Correction behavior exists |
| **3** | Correction follows explicit operational rules |
| **4** | Correction accounts for magnitude, confidence, consequence, or Regime |
| **5** | Truth evaluation and state Correction are explicitly separate, bounded, and governed |

## RTT Relationship

    Temp
    Drift
    Regime

## Crosswalk Questions

- What happens when local state is wrong?
- Is state replaced immediately?
- Can correction occur gradually?
- Can change be delayed?
- Can state be quarantined?
- Can competing states coexist?
- Can humans or another authority be required?
- Does consequence affect Correction?

---

# 16. Criterion 10 — Failure Transparency

## Governing Question

> **Can the system visibly admit that it cannot presently establish a sufficiently qualified operational state?**

Evaluate explicit representation of:

- unavailable
- degraded
- stale
- unsynchronized
- contested
- expired
- unverified
- indeterminate
- unknown

## Scoring

| Score | Condition |
|---:|---|
| **0** | The system effectively always emits an apparently acceptable answer |
| **1** | Failure appears primarily as exception, outage, or implicit behavior |
| **2** | Some degradation states are observable |
| **3** | Loss of qualification is explicitly represented |
| **4** | Multiple forms of uncertainty or degradation are distinguished |
| **5** | Failure, indeterminacy, or loss of qualification is first-class and constrains downstream use |

## RTT Relationship

    Coherence
    Paradox
    Regime

## Crosswalk Questions

- Can the system say "unknown"?
- Can it say "stale"?
- Can it say "contested"?
- Can it say "unavailable"?
- Does degraded state remain distinguishable from valid state?
- Can downstream consumers detect the difference?
- Can operational action be restricted because qualification failed?

---

# 17. Standard Scorecard

Every reference-system crosswalk should include the following scorecard.

| Criterion | Score 0–5 | Delegation | Evidence Summary |
|---|---:|---|---|
| Anchor Quality |  |  |  |
| Lineage Visibility |  |  |  |
| Observation Quality |  |  |  |
| Coherence Detection |  |  |  |
| Drift Detection |  |  |  |
| Paradox Handling |  |  |  |
| Regime Awareness |  |  |  |
| Freshness / Revalidation |  |  |  |
| Correction Discipline |  |  |  |
| Failure Transparency |  |  |  |
| **Total** | **/50** |  |  |
| **Normalized** | **/100** |  | Optional |

The total should be calculated only after every populated score has supporting evidence.

---

# 18. Structural Profile

The ten scoring criteria may be represented compactly in this order:

    A-L-O-C-D-P-R-F-X-T

where:

    A = Anchor Quality
    L = Lineage Visibility
    O = Observation Quality
    C = Coherence Detection
    D = Drift Detection
    P = Paradox Handling
    R = Regime Awareness
    F = Freshness / Revalidation
    X = Correction Discipline
    T = Failure Transparency

An illustrative profile:

    5-4-5-5-5-4-3-5-5-5

This profile is not an NTP score.

It is an example of the representation.

The structural profile should be preserved even when a total is also reported.

---

# 19. Why the Profile Matters

Consider two hypothetical systems.

    System A:
      5-5-5-2-2-1-3-5-2-3
      Total: 33

    System B:
      2-2-3-5-5-5-5-2-3-1
      Total: 33

Both systems score:

    33 / 50

but their architectures are structurally very different.

System A is strong in:

- reference
- Lineage
- Observation
- freshness

System B is strong in:

- Coherence
- Drift
- Paradox
- Regime

The total conceals this difference.

The profile exposes it.

---

# 20. RTT Meta-Dimensions

The ten criteria can be grouped into five higher-level structural dimensions.

| Meta-Dimension | Component Scores |
|---|---|
| **Reference** | Anchor Quality + Lineage Visibility |
| **Observation** | Observation Quality + Freshness/Revalidation |
| **Coherence** | Coherence Detection + Paradox Handling |
| **Drift** | Drift Detection + Correction Discipline |
| **Regime** | Regime Awareness + Failure Transparency |

Each Meta-Dimension receives:

    0–10

Example representation:

    Reference    [........]   8/10
    Observation  [.........]  9/10
    Coherence    [.......]    7/10
    Drift        [..........] 10/10
    Regime       [......]     6/10

The brackets above are illustrative only.

They are not intended as an additional scoring algorithm.

---

# 21. Meta-Score Formula

Given:

    A = Anchor Quality
    L = Lineage Visibility

    O = Observation Quality
    F = Freshness / Revalidation

    C = Coherence Detection
    P = Paradox Handling

    D = Drift Detection
    X = Correction Discipline

    R = Regime Awareness
    T = Failure Transparency

calculate:

    Reference   = A + L

    Observation = O + F

    Coherence   = C + P

    Drift       = D + X

    Regime      = R + T

Each remains:

    0–10

No weighting is applied in the initial scoring model.

---

# 22. No Weighting Yet

Different Truth Classes emphasize different structural dimensions.

For example:

| System | Likely Emphasis |
|---|---|
| NTP | Drift · Freshness · Coherence · Correction |
| DNS | Anchor · Lineage · Regime · Freshness |
| IAM | Anchor · Observation · Regime · Failure Transparency |
| PKI | Anchor · Lineage · Freshness · Failure Transparency |
| Policy / IAM | Anchor · Regime · Coherence · Failure Transparency |
| Distributed Systems | Coherence · Drift · Paradox · Correction |
| Ledgers | Lineage · Coherence · Regime · Correction |
| Desired-State Systems | Drift · Coherence · Correction · Revalidation |
| Telemetry | Observation · Coherence · Lineage · Freshness |
| Supply-Chain Provenance | Lineage · Anchor · Observation · Regime |

These are analytical expectations.

They are not numerical weights.

The initial scoring model intentionally gives every criterion equal numeric range.

A weighted model should be introduced only if crosswalk evidence demonstrates a useful need for one.

---

# 23. Scoring Workflow

Every reference system should be scored using the same sequence.

## Step 1 — Describe the System

Document the system on its own terms.

Do not score yet.

## Step 2 — Identify Candidate Evidence

Collect evidence relevant to each criterion.

## Step 3 — Separate Fact from RTT Interpretation

Distinguish:

    Reference-System Fact

from:

    RTT Interpretation

## Step 4 — Identify Delegation

For each criterion ask:

> Is this mechanism native, delegated, hybrid, or unknown?

## Step 5 — Identify Missing Mechanisms

Make absence visible.

Do not fill gaps with assumptions.

## Step 6 — Assign Criterion Score

Use the common 0–5 rubric.

## Step 7 — Record Rationale

Explain why the evidence supports that score.

## Step 8 — Record Evidence

Attach or cite the evidence used.

## Step 9 — Generate Structural Profile

Produce:

    A-L-O-C-D-P-R-F-X-T

## Step 10 — Generate RTT Meta-Dimensions

Produce:

    Reference
    Observation
    Coherence
    Drift
    Regime

## Step 11 — Review for Scope Error

Ask whether a low score represents:

- weakness
- delegation
- narrow scope
- insufficient evidence

## Step 12 — Compare

Only after individual scoring is complete should cross-system comparison begin.

---

# 24. Scoring Confidence

The score itself and confidence in the score are different concepts.

A criterion may appear to warrant:

    score: 4

while available evidence only weakly supports that assessment.

Therefore an optional research confidence field may be recorded:

    evidence_confidence:
      high

or:

    evidence_confidence:
      moderate

or:

    evidence_confidence:
      low

This reflects:

> **confidence in the research assessment**

not:

> **truth confidence of the operational system.**

The two must remain separate.

---

# 25. Evidence Confidence

Suggested research evidence confidence:

## High

Multiple strong sources or direct implementation evidence support the score.

## Moderate

The score is reasonably supported but important implementation details remain unclear.

## Low

Available evidence is partial, indirect, or primarily analytical.

## Unknown

Evidence is insufficient to assess confidence.

Evidence confidence should not modify the score automatically.

It provides context for future review.

---

# 26. Unknown vs Zero

A critical scoring distinction is:

    UNKNOWN
      ≠
    0

Score `0` means:

> Sufficient evidence indicates that the mechanism is meaningfully absent within the evaluated scope.

Unknown means:

> Available evidence is insufficient to determine the mechanism's state.

Therefore an unscored criterion should remain:

    score: null

or:

    status: not_yet_scored

rather than automatically receiving:

    0

This prevents missing research from becoming evidence of missing architecture.

---

# 27. Not Applicable

Another important distinction is:

    NOT_APPLICABLE
      ≠
    0

A mechanism may be structurally irrelevant to a narrowly defined system boundary.

Where justified:

    score: null
    status: not_applicable

may be more accurate than assigning zero.

However, `not_applicable` should be used cautiously.

The crosswalk should first determine whether the mechanism is:

- absent
- delegated
- outside scope
- genuinely not applicable

This decision requires rationale.

---

# 28. Recommended Criterion Record

A full scoring record may use:

    criterion:
      anchor_quality

    status:
      scored

    score:
      4

    classification:
      strong

    delegation:
      native

    evidence_confidence:
      high

    rationale:
      The system explicitly identifies its reference
      authority and operational scope.

    evidence:
      - type: specification
        reference: "..."
        description: "..."

      - type: implementation
        reference: "..."
        description: "..."

    caveats:
      - "Revocation behavior requires further review."

This provides substantially more research value than:

    anchor_quality: 4

---

# 29. Scoring Status

Each criterion may have one of:

    not_yet_scored
    scored
    insufficient_evidence
    not_applicable
    deferred

## Not Yet Scored

Research has not reached the scoring stage.

## Scored

Evidence is sufficient to assign a provisional score.

## Insufficient Evidence

Research was attempted but available evidence does not justify a score.

## Not Applicable

The criterion is structurally outside the defined system scope.

## Deferred

Scoring is intentionally postponed pending another crosswalk or unresolved issue.

---

# 30. Provisional vs Stable Scores

Crosswalk scores should initially be considered:

    provisional

A score becomes increasingly stable when:

- evidence is strong
- the evaluation boundary is explicit
- the scoring rationale survives review
- later crosswalks do not expose a category error
- the scoring rubric remains unchanged

The scoring framework should allow earlier scores to be revised.

Revision is not failure.

It is part of the crosswalk process.

---

# 31. Score Versioning

A score revision should preserve:

- previous value
- new value
- reason for change
- new evidence
- rubric version
- scoring date or revision identifier

Conceptually:

    Score v1
      ↓
    New Evidence
      ↓
    Score Review
      ↓
    Score v2

The goal is to preserve why interpretation changed.

---

# 32. Cross-System Comparison

Once sufficient systems have been scored, comparison may use:

| System | Truth Class | A | L | O | C | D | P | R | F | X | T | Total |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| NTP | Temporal |  |  |  |  |  |  |  |  |  |  | /50 |
| DNS | Locational |  |  |  |  |  |  |  |  |  |  | /50 |
| IAM | Identity |  |  |  |  |  |  |  |  |  |  | /50 |
| PKI | Integrity |  |  |  |  |  |  |  |  |  |  | /50 |
| Policy / IAM | Authority |  |  |  |  |  |  |  |  |  |  | /50 |
| Distributed Systems | State |  |  |  |  |  |  |  |  |  |  | /50 |
| Ledgers | Transactional |  |  |  |  |  |  |  |  |  |  | /50 |
| Desired-State Systems | Intent |  |  |  |  |  |  |  |  |  |  | /50 |
| Telemetry | Observational |  |  |  |  |  |  |  |  |  |  | /50 |
| Supply-Chain Provenance | Lineage |  |  |  |  |  |  |  |  |  |  | /50 |

Blank cells are preferable to unsupported scores.

---

# 33. Comparison Constraints

Cross-system totals should be interpreted carefully.

A system may score lower because:

- its scope is intentionally narrow
- responsibility is delegated
- the criterion belongs to another layer
- observability is limited
- evidence is incomplete

A system may score higher because:

- it explicitly owns more truth-maintenance responsibilities
- the architecture is broader
- it preserves more state
- it exposes more lifecycle behavior

Therefore:

> **Higher score does not automatically mean better system.**

It means:

> **More of the evaluated truth relationship is explicitly exposed or governed within the selected boundary.**

---

# 34. Primary vs Secondary Truth Classes

A reference system is initially mapped to one primary Truth Class.

However, scoring may reveal strong participation in secondary classes.

Example:

    PKI

Primary:

    Integrity

Secondary:

    Identity
    Authority
    Temporal
    Lineage

The score should evaluate the system as scoped in the crosswalk.

It should not silently expand scope simply because secondary Truth Classes exist.

---

# 35. Evaluation Boundary

Every scorecard should declare its evaluation boundary.

Recommended fields:

    system:
      NTP

    evaluated_scope:
      Core time synchronization mechanisms

    primary_truth_class:
      Temporal

    excluded_scope:
      - deployment-specific monitoring
      - vendor-specific extensions

Without a declared boundary, scores risk becoming incomparable.

---

# 36. Scoring Anti-Patterns

The following approaches should be avoided.

## Popularity Scoring

Do not increase scores because a system is widely deployed.

## Complexity Scoring

Do not increase scores because a system is complicated.

## Age Scoring

Do not increase scores because a system is mature.

## Reputation Scoring

Do not score based on institutional prestige.

## Feature Counting

Do not equate number of features with stronger truth structure.

## Binary Presence Scoring

Do not assign high scores merely because a mechanism exists.

The scoring question is:

> **How structurally integrated is the mechanism into operational truth governance?**

## Speculative Scoring

Do not fill missing evidence with plausible assumptions.

## RTT Familiarity Bias

Do not reward a system simply because its terminology maps neatly onto RTT.

---

# 37. NTP Bias Check

Because NTP is Crosswalk #1, the scoring criteria themselves may initially reflect Temporal Truth concerns.

This is a known research risk.

Every subsequent crosswalk should therefore ask:

> **Does this criterion remain meaningful in this Truth Class?**

If DNS, IAM, PKI, distributed systems, or later crosswalks reveal that a criterion is:

- overly temporal
- redundant
- poorly defined
- missing a major dimension

the rubric should be revised.

If revised, earlier systems should be rescored.

The scoring model is itself subject to Drift detection and Revalidation.

---

# 38. Rubric Revalidation

The rubric should be reconsidered after major crosswalk milestones.

Suggested checkpoints:

    After NTP
      ↓
    Baseline rubric

    After DNS
      ↓
    First non-temporal challenge

    After PKI
      ↓
    Trust / Lineage challenge

    After Distributed Systems
      ↓
    Coherence / consensus challenge

    After Telemetry
      ↓
    Observational incompleteness challenge

    After Supply-Chain Provenance
      ↓
    Final Lineage challenge

At each checkpoint ask:

- Are the ten criteria still distinct?
- Is any criterion overly domain-specific?
- Is an important structural dimension missing?
- Are scoring definitions producing unintended bias?
- Does the Meta-Dimension grouping still hold?

---

# 39. Criterion Change Rule

A scoring criterion should change only when evidence demonstrates a structural problem with the rubric.

Potential triggers include:

- multiple systems consistently expose the same missing dimension
- one criterion repeatedly conflates distinct mechanisms
- systems cannot be scored without arbitrary interpretation
- later crosswalks reveal a hidden NTP-specific assumption
- two criteria consistently measure the same structural property

Changes should preserve:

- old definition
- revised definition
- reason
- affected crosswalks
- rescore requirement

---

# 40. Proposed Machine Representation

The eventual research schema may represent a system score as:

    system_id:
      ntp

    primary_truth_class:
      temporal

    scoring_version:
      "0.1"

    criteria:

      anchor_quality:
        status: scored
        score: 5
        delegation: native
        evidence_confidence: high
        rationale: "..."
        evidence:
          - type: specification
            reference: "..."

      lineage_visibility:
        status: scored
        score: 4
        delegation: native
        evidence_confidence: high
        rationale: "..."
        evidence:
          - type: specification
            reference: "..."

    raw_total:
      null

    normalized_total:
      null

The example deliberately leaves totals null.

Scores should not be completed until the full evidence review is performed.

---

# 41. Research Plane Separation

The scoring model belongs strictly to the Research Plane.

    RESEARCH PLANE
          │
          ├── Reference System
          ├── Crosswalk
          ├── Criterion
          ├── Score
          ├── Evidence
          ├── Rationale
          └── Comparative Profile

The Runtime Plane contains:

    Claim
    Observation
    Source
    Anchor
    Regime
    Evaluation
    Truth State
    Drift
    Paradox
    Correction

There should be no runtime logic such as:

    if NTP_score > 40:
        increase_truth_confidence()

That would violate the separation.

The scoring system evaluates architectures.

The Truth Service evaluates Claims.

---

# 42. Score Interpretation

The intended interpretation is:

## 0 — Absent

The chosen evaluation boundary does not meaningfully expose the mechanism, and evidence does not identify explicit delegation.

## 1 — Implicit

The mechanism appears necessary to operation but remains weakly represented.

## 2 — Partial

The mechanism exists explicitly but is incomplete, constrained, or peripheral.

## 3 — Operational

The mechanism is intentionally represented and usable.

## 4 — Strong

The mechanism is systematic and integrated into normal operation.

## 5 — Structural

The mechanism materially governs whether operational state can be accepted.

The final question for a score of `5` should be:

> **Would removing this mechanism fundamentally alter how the system establishes or maintains its operational truth state?**

If the answer is no, a lower score may be more appropriate.

---

# 43. Crosswalk Finding Integration

Scoring should contribute to architectural analysis.

Example:

    System:
      DNS

    Criterion:
      Regime Awareness

    Finding:
      namespace and observer position materially affect resolution

This may support an architectural conclusion:

    Regime must preserve namespace / observer scope

The score itself is not the architectural finding.

The evidence and rationale are.

---

# 44. Score Disagreement

Researchers or evaluators may reasonably disagree about a score.

Disagreement should be represented rather than hidden.

Possible process:

    Evaluation A:
      score: 3
      rationale: ...

    Evaluation B:
      score: 4
      rationale: ...

    Review:
      evidence compared

    Result:
      consensus score

or:

    Result:
      score remains contested

A contested research score does not create a Runtime Plane Paradox automatically.

It is a Research Plane disagreement.

---

# 45. Scoring Completion Criterion

A system is considered fully scored when:

- all ten criteria have a defined status
- every numeric score has rationale
- every numeric score has evidence
- delegation has been considered
- evaluation boundary is explicit
- insufficient evidence remains visible
- not-applicable determinations include rationale
- structural profile is generated
- RTT Meta-Dimensions are generated
- caveats are recorded
- evidence confidence is recorded where useful

Only then should the raw total be calculated.

---

# 46. Crosswalk Scoring Template

Each detailed crosswalk may use the following template.

    ## Scoring

    ### Evaluation Boundary

    System:
      ...

    Primary Truth Class:
      ...

    Evaluated Scope:
      ...

    Excluded Scope:
      ...

    ### Criterion 1 — Anchor Quality

    Score:
      ...

    Classification:
      ...

    Delegation:
      ...

    Evidence Confidence:
      ...

    Rationale:
      ...

    Evidence:
      ...

    Caveats:
      ...

Repeat through:

    Criterion 10 — Failure Transparency

Then:

    ### Structural Profile

    A-L-O-C-D-P-R-F-X-T

    ...

    ### RTT Meta-Dimensions

    Reference:
      /10

    Observation:
      /10

    Coherence:
      /10

    Drift:
      /10

    Regime:
      /10

    ### Total

    Raw:
      /50

    Normalized:
      /100

    ### Score Status

      provisional | reviewed | stable | contested

---

# 47. Initial Score Status

Until the ten-system crosswalk sequence has substantially matured, scores should generally be marked:

    provisional

This is particularly important for early systems such as NTP.

Later reference systems may reveal that the scoring model itself contains hidden assumptions.

A provisional score preserves that possibility.

---

# 48. Canonical Scoring Questions

The ten criteria can be remembered through ten short questions:

    1. ANCHOR
       What is the reference?

    2. LINEAGE
       Where did it come from?

    3. OBSERVATION
       What evidence exists?

    4. COHERENCE
       Does the qualified evidence meaningfully agree?

    5. DRIFT
       What has changed?

    6. PARADOX
       What still conflicts?

    7. REGIME
       Where does the result hold?

    8. FRESHNESS
       Is it still current?

    9. CORRECTION
       What happens when better state appears?

    10. FAILURE
        Can the system admit that it does not know?

These questions form the practical scoring kernel.

---

# 49. Governing Scoring Principle

> **Score the visibility and governance of the truth relationship, not the apparent correctness of the answer.**

A mature operational truth system should increasingly expose:

- its references
- its Sources
- its Lineage
- its Observations
- its agreement structure
- its Drift
- its unresolved contradictions
- its operational boundaries
- its freshness
- its Correction behavior
- its loss of qualification

The scoring model measures how structurally visible and governed those relationships are.

It does not measure absolute truth.

---

# 50. Canonical Summary

The Operational Truth-System score is built from:

    Anchor Quality
          +
    Lineage Visibility
          +
    Observation Quality
          +
    Coherence Detection
          +
    Drift Detection
          +
    Paradox Handling
          +
    Regime Awareness
          +
    Freshness / Revalidation
          +
    Correction Discipline
          +
    Failure Transparency

Each receives:

    0–5

with:

    rationale
    evidence
    delegation status
    evaluation boundary

The result may be represented as:

    Structural Profile:
      A-L-O-C-D-P-R-F-X-T

and:

    RTT Meta-Dimensions:
      Reference
      Observation
      Coherence
      Drift
      Regime

The total score is useful.

The structural shape is more informative.

The evidence is more important than either.

**No naked scores.**

**No unsupported zeros.**

**No penalty for delegation without identifying the boundary.**

**No comparison before scope is declared.**

**No confidence inflation from popularity or familiarity.**

**Score the structure.**

**Preserve the rationale.**

**Keep the evidence visible.**

**Revalidate the rubric as the crosswalks challenge it.**
