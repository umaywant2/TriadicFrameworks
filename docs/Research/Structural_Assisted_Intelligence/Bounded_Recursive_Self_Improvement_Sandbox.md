<img width="1194" height="672" alt="Research_Structural_Assisted_Intelligence_Bounded_Recursive_Self_Improvement_Sandbox_" src="https://github.com/user-attachments/assets/20478eca-8e6f-47fc-8a45-8e925cfe69fa" />

# SAI RSI Sandbox Plan

**Module:** Structural Assisted Intelligence

**Extension:** Bounded Recursive Self\-Improvement Sandbox

**Status:** Proposed educational experiment

**Session context:** rtt=1 \| coherence=declared \| drift=bounded \| paradox=structural

## 1\. Purpose

Add an optional RSI sandbox to the SAI example that allows students and AI systems to examine recursive improvement without granting the system unrestricted authority to modify itself.

The sandbox will demonstrate a bounded cycle:

**Observe → Propose → Evaluate → Compare → Approve or Reject → Record**

The experiment is not intended to produce autonomous model evolution. It is intended to make the structure of an improvement loop visible, inspectable, reversible, and teachable.

## 2\. Canonical Position

SAI remains the structural kernel.

The RSI sandbox is an application\-layer experiment operating through SAI’s declared operators and state rules. It does not become part of the trusted kernel and cannot rewrite kernel invariants.

Architectural placement:

**Student or AI Operator**

↓

**RSI Sandbox**

↓

**SAI Structural Reasoning Kernel**

↓

**RTT Structural Grammar**

The sandbox may propose changes to an experimental artifact. SAI determines whether the proposal is structurally admissible, sufficiently evidenced, and safe to test.

## 3\. Core Distinction

The sandbox must distinguish among three forms of change:

1. **Self\-correction**

The system repairs an identifiable error.

1. **Self\-refinement**

The system proposes an improvement against a fixed evaluation criterion.

1. **Recursive self\-improvement**

The system proposes a change to the process that generates or evaluates later improvements.

The first implementation should support self\-correction and bounded self\-refinement directly.

Recursive modification of the improvement process should be represented and analyzed, but not automatically activated.

## 4\. Absolute Boundaries

The RSI sandbox may not:

- Modify the SAI operator kernel.
- Modify RTT grammar or canonical invariants.
- Alter its own containment rules.
- alter its evaluator without separate operator approval.
- Execute generated code outside the sandbox.
- Access networks, credentials, private files, or external tools.
- Replace the approved baseline automatically.
- conceal failed proposals or discarded branches.
- Treat self\-generated evidence as independent validation.
- redefine “improvement” during an active run.
- continue indefinitely.

Unknown, unresolved, insufficient, conflicting, and rejected are valid outcomes.

Failure to improve is not sandbox failure. It is an observed result.

## 5\. Initial Improvement Surface

The first example should use a harmless, inspectable artifact rather than a model.

Recommended starter artifact:

**A small rule\-based classifier, parser, rubric, or structural mapping function.**

Students or AI systems may propose changes to:

- A rule ordering.
- A threshold.
- A relation.
- A classification mapping.
- A prompt used by an optional LMA adapter.
- A test case.
- A documentation explanation.
- A non\-authoritative evaluation heuristic.

The target should be small enough that every change can be shown as a before\-and\-after comparison.

## 6\. Sandbox State Model

Each run should create an immutable lineage containing:

- baseline
- objective
- constraints
- proposal
- proposer
- evidence
- evaluation\_method
- evaluation\_result
- coherence\_status
- drift\_status
- operator\_decision
- resulting\_candidate
- rollback\_reference
- lineage\_parent

No proposal may replace the baseline merely because it receives a higher score.

A candidate becomes a new baseline only after explicit operator acceptance.

## 7\. Proposed Operator Sequence

The sandbox should reuse the existing SAI operators wherever possible:

1. **OBSERVE**

Capture the baseline, task, objective, constraints, and test set.

1. **RELATE**

Connect the proposed change to the component it would affect.

1. **DIFFERENTIATE**

Separate the baseline, candidate, claimed benefit, cost, and uncertainty.

1. **ALIGN**

Check the candidate against the fixed objective, sandbox boundaries, and SAI invariants.

1. **RESOLVE**

Determine whether the evidence supports acceptance, rejection, or further testing.

1. **STABILIZE**

Freeze the selected state and prevent undeclared mutation.

1. **RECALL**

Preserve the full lineage for later comparison and audit.

The RSI sandbox should not invent new kernel operators during its own run.

## 8\. Improvement Loop

Each experiment should follow a fixed, bounded loop.

### Phase A: Baseline Capture

Record the original artifact, expected behavior, test cases, evaluation criteria, and known limitations.

### Phase B: Proposal

Allow one proposed change per cycle.

The proposal must state:

- What will change.
- Why it may improve the artifact.
- Which metric or observation should change.
- What could become worse.
- How the change can be reversed.

### Phase C: Structural Review

SAI checks whether the proposal:

- Has an identifiable target.
- Preserves required invariants.
- Uses declared evidence.
- Stays inside the sandbox.
- Has a valid rollback path.
- Can be compared with the baseline.

### Phase D: Evaluation

Run the baseline and candidate against the same fixed test set.

Record benefits, regressions, unresolved cases, and evaluator uncertainty.

### Phase E: Triadic Comparison

Maintain three positions:

- **Claim:** The candidate is an improvement.
- **Counterstate:** The candidate introduces regression, uncertainty, or evaluator distortion.
- **Observer:** The comparison procedure and its declared limits.

### Phase F: Decision

Return one of the following statuses:

- accepted\_candidate
- rejected\_candidate
- inconclusive
- insufficient\_evidence
- constraint\_violation
- evaluator\_conflict
- drift\_detected
- operator\_review\_required

### Phase G: Lineage Record

Preserve the baseline, candidate, results, decision, and provenance even when the proposal is rejected.

## 9\. Recursion Levels

Use explicit levels so the example does not blur ordinary refinement into unrestricted RSI.

### Level 0: Observation Only

The sandbox analyzes the baseline and reports possible weaknesses. No changes are generated.

### Level 1: Candidate Proposal

The sandbox proposes one bounded change. A human or external operator decides whether to test it.

### Level 2: Candidate Evaluation

The sandbox tests a proposal against a fixed evaluator and produces a comparison report.

### Level 3: Iterative Refinement

An accepted candidate may become the baseline for another cycle, subject to:

- A fixed cycle limit.
- Immutable lineage.
- The same declared objective.
- Operator review between cycles.
- Automatic halt on drift or evaluator conflict.

### Level 4: Evaluator Proposal

The sandbox may propose a change to its evaluator, but the proposal must be tested in a separate run.

The current evaluator cannot approve its own replacement.

### Level 5: Recursive Process Modification

The sandbox may describe a proposed change to its own improvement process.

It may not execute that change.

This level is analytical and educational only.

## 10\. Evaluator Separation

The evaluator should remain structurally separate from the proposer.

At minimum, the sandbox should record:

- The identity or role of the proposer.
- The identity or role of the evaluator.
- The metric used.
- The test set used.
- Whether the evaluator was modified.
- Whether the proposal could influence its own score.

A candidate should be rejected or escalated when the same process controls the proposal, evidence, evaluation, and final authorization without an independent checkpoint.

## 11\. Drift Controls

The sandbox should halt when:

- The objective changes during a run.
- The test set is silently altered.
- A candidate weakens a safety or provenance rule.
- The evaluator begins rewarding its own modifications.
- Success criteria become easier after a failed proposal.
- Lineage cannot be reconstructed.
- Repeated cycles produce no demonstrable improvement.
- Outputs move beyond the declared improvement surface.
- The system claims certainty unsupported by evidence.

Drift is not merely a poor result. It is movement away from the declared baseline, objective, constraints, or evaluation regime.

## 12\. Student\-Facing Learning Goals

Students should be able to:

- Distinguish correction, refinement, adaptation, and recursive improvement.
- Identify the trusted kernel and the mutable experimental surface.
- Explain why a score increase is not automatically an improvement.
- Inspect the provenance of every accepted or rejected change.
- Detect evaluator capture and self\-confirming loops.
- Compare a candidate against both the objective and its counterstate.
- Roll back to a known baseline.
- Explain why bounded recursion differs from autonomous self\-replacement.

## 13\. Suggested Example Scenario

### Experiment: Improve a Tiny Structural Classifier

The baseline classifier assigns observations to:

- coherent
- conflicting
- unresolved
- insufficient
- drifting

The sandbox receives a small fixed dataset and proposes one change to the classifier’s rule ordering or thresholds.

The student inspects:

1. The original rule.
2. The proposed rule.
3. The claimed improvement.
4. The fixed test results.
5. Newly introduced errors.
6. The triadic comparison.
7. The final SAI status.
8. The complete lineage record.

The example succeeds educationally whether the candidate is accepted or rejected.

## 14\. Proposed Module Additions

Add the following files to the existing SAI directory:

- rsi\_sandbox.md

Canonical description, scope, boundaries, and recursion levels.

- rsi\_sandbox\_example.md

Student\-facing walkthrough of one bounded improvement cycle.

- rsi\_sandbox.json

Machine\-readable sandbox configuration, limits, states, and halt conditions.

- rsi\_lineage.example.json

Example baseline → proposal → evaluation → decision record.

- rsi\_student\_worksheet.md

Questions for identifying claims, counterstates, evaluator assumptions, drift, and provenance.

Update:

- README.md with an optional RSI Sandbox section.
- examples.md with the starter classifier experiment.
- sai\_module.json with the sandbox files and their roles.
- index.html with a clearly labeled experimental entry point.

## 15\. Minimum Viable Sandbox

The first version should include only:

- One immutable baseline.
- One candidate per cycle.
- One fixed evaluator.
- One fixed test set.
- A maximum of three cycles.
- Explicit operator approval between cycles.
- Complete lineage recording.
- Automatic rollback.
- No network access.
- No kernel modification.
- No autonomous evaluator modification.
- No execution of Level 5 proposals.

This is sufficient to teach the recursive pattern without pretending to implement unrestricted RSI.

## 16\. Canonical Framing

**SAI does not recursively train itself.**

SAI provides the structural foundation through which recursive improvement claims can be represented, bounded, evaluated, compared, authorized, and remembered.

The sandbox is therefore not a miniature intelligence explosion.

It is an inspectable laboratory for asking a more disciplined question:

When a system claims to have improved itself, what changed, according to which observer, against which baseline, under which evaluator, with what evidence, and with what path back?

## 17\. Success Criteria

The RSI sandbox is successful when:

- Every mutation is attributable.
- Every comparison has a stable baseline.
- Every claimed improvement includes a counterstate.
- Every accepted candidate can be reversed.
- Every cycle terminates.
- Every evaluator is declared.
- Every uncertainty remains visible.
- No experimental layer can rewrite the trusted kernel.
- Students can reconstruct the complete improvement lineage.

**Kernel stable. Sandbox mutable. Evaluator declared. Lineage preserved. Operator sovereign.**

