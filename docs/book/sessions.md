# Canonical Session Library

> **A reference collection of fully worked sessions practitioners can study, clone, and adapt.**
> Every session in this library is complete: all nine grammar fields populated, every operator invocation shown in full, every output produced, every validator assessment applied.

---

## What This Library Is

The canonical session library is the system's worked-example layer. Where Part III taught you *how* to run sessions, this library shows you sessions that have *already been run* — correctly, in full, with real inputs and real outputs.

Use this library in three ways:

**1. Reference** — When you are unsure how a particular kind of session should look, find the closest canonical session here and read it end-to-end before building your own.

**2. Clone** — When your session is structurally similar to a canonical one, use it as a starting template. Swap the input, adjust the intent and scope, re-resolve the active_modules list, and run. The clone guide at the end of each session tells you exactly which fields to change.

**3. Audit** — When a session you have run produces unexpected results, compare its grammar and invocations against the closest canonical session. The difference between your session and the canonical one is usually where the problem lives.

---

## How to Read a Canonical Session

Each session is structured in five sections:

| Section | What It Contains |
|---------|-----------------|
| **Grammar** | The fully populated 9-field session grammar |
| **Execution** | The operator invocations, in order, with full signatures |
| **Output** | The session's complete output, in the declared format |
| **Assessment** | The validator's assessment of the output |
| **Clone Guide** | Which fields to change when adapting this session |

Read the grammar first — always. The grammar defines everything the execution is allowed to do. If the execution surprises you, return to the grammar. The answer is there.

---

## Session Index

| ID | Title | Primary Operator | Depth | Difficulty |
|----|-------|-----------------|-------|-----------|
| [CS-01](#cs-01--baseline-rtt-analysis) | Baseline RTT Analysis | `RTT.pass` | 1 | Beginner |
| [CS-02](#cs-02--two-pass-recursive-rtt-analysis) | Two-Pass Recursive RTT Analysis | `RTT.pass` | 2 | Beginner |
| [CS-03](#cs-03--scope-compliance-check) | Scope Compliance Check | `Scope.check` | — | Intermediate |
| [CS-04](#cs-04--dependency-audit) | Dependency Audit | `Dependency.trace` | — | Intermediate |
| [CS-05](#cs-05--gap-identification-and-module-draft) | Gap Identification and Module Draft | `Gap.identify` + `Module.draft` | — | Intermediate |
| [CS-06](#cs-06--multi-lens-rtt-analysis) | Multi-Lens RTT Analysis | `RTT.pass` + lens activation | 2 | Advanced |
| [CS-07](#cs-07--session-diagnosis-and-repair) | Session Diagnosis and Repair | `Session.diagnose` + field tests | — | Advanced |
| [CS-08](#cs-08--clarity-evaluation-of-an-existing-output) | Clarity Evaluation of an Existing Output | `Clarity.evaluate` | — | Intermediate |

---

## CS-01 — Baseline RTT Analysis

**Purpose:** The minimum viable session. A single-depth RTT pass on a plain-language problem statement. Use this as your first session template and as the reference for what a correctly formed grammar looks like at its simplest.

---

### Grammar

```json
{
  "session_id": "cs-01-baseline-rtt-20260925",
  "intent": "Produce a single-depth RTT analysis of the input statement, identifying all three structural faces and packaging the output as a valid StructuredFaces unit.",
  "scope": "This session covers one RTT pass on the single input statement below. It does not cover recursive extension, adjacent inputs, or downstream implications of the output.",
  "active_modules": [
    "rtt-anchor-definition",
    "session-grammar-anchor",
    "session-grammar-field-input",
    "session-grammar-field-output-format",
    "session-grammar-field-validator",
    "rtt-op-core",
    "clarity-val-rtt-output"
  ],
  "role_context": "operator",
  "layer_context": "operational",
  "input": {
    "content": "Our engineering team ships features on time but the features rarely get adopted. Leadership keeps asking why, and the team keeps pointing to the product roadmap. Nobody is looking at the gap between what ships and what users actually need.",
    "scope": "A single organizational dynamic described by an observer — scoped to the delivery-adoption gap, no broader organizational context."
  },
  "output_format": "StructuredFaces",
  "validator": "clarity-val-rtt-output"
}
```

---

### Execution

```
RTT.pass(
  input: {
    content: "Our engineering team ships features on time but the features rarely get adopted...",
    scope: "A single organizational dynamic — scoped to the delivery-adoption gap."
  },
  depth: 1,
  output_format: StructuredFaces
)
```

---

### Output

```json
{
  "generative_face": "The team's success metric is delivery velocity — shipping on time. This metric was set upstream and has never been challenged. Because the team is evaluated on delivery, it optimizes for delivery. The roadmap is treated as a specification of user need, not a hypothesis about user need. No mechanism exists to close the loop between what ships and what users do with it.",
  "present_face": "A structural decoupling between delivery and adoption. The team is performing correctly against its stated metric (on-time delivery) and incorrectly against the actual goal (user adoption). The gap is not a motivation failure or a skill failure — it is a metric design failure. The wrong thing is being measured, so the wrong thing is being optimized.",
  "terminal_face": "Without intervention, the gap compounds. Each on-time delivery that goes unadopted reinforces the team's belief that the roadmap is the problem, and leadership's belief that the team is the problem. The actual problem — the absence of a feedback loop between delivery and usage — remains unaddressed and undiagnosed. The system drifts toward blame attribution rather than structural correction.",
  "pass_depth": 1,
  "next_input": {
    "content": "The team optimizes for delivery because delivery is what is measured. No feedback loop connects shipped features to usage data. The metric design is the structural failure.",
    "scope": "The metric design failure identified in the first RTT pass — scoped to the measurement system, not to the team's capabilities or the roadmap's content."
  }
}
```

---

### Assessment

```json
{
  "validator_id": "clarity-val-rtt-output",
  "session_id": "cs-01-baseline-rtt-20260925",
  "pass_depth_evaluated": 1,
  "criteria_results": [
    {
      "criterion": "Face completeness",
      "status": "satisfied",
      "notes": "All three faces present."
    },
    {
      "criterion": "Face substantiveness",
      "status": "satisfied",
      "notes": "Each face makes specific, checkable claims. Present face names the metric design failure precisely. Terminal face identifies a specific drift pattern."
    },
    {
      "criterion": "Pass differentiation",
      "status": "satisfied",
      "notes": "Single pass — differentiation criterion not applicable at depth=1."
    },
    {
      "criterion": "Scope compliance",
      "status": "satisfied",
      "notes": "No reference to broader organizational context detected. Output stayed within declared scope."
    },
    {
      "criterion": "Intent fulfillment",
      "status": "satisfied",
      "notes": "StructuredFaces output produced. next_input packaged correctly for potential extension."
    }
  ],
  "overall_coherence": "high",
  "flags": [],
  "recommendation": "accept"
}
```

---

### Clone Guide

To adapt CS-01 for your own input:

| Field | What to Change |
|-------|---------------|
| `session_id` | New unique ID: `[your-domain]-baseline-rtt-[YYYYMMDD]` |
| `intent` | Keep the structure; replace "input statement" with a one-phrase description of your input |
| `scope` | Replace the example content; keep the exclusion clause ("does not cover recursive extension...") |
| `input.content` | Your raw input |
| `input.scope` | One sentence declaring exactly what the input represents and what it does not |
| `active_modules` | No changes needed — this list is correct for any single-depth RTT session |

Do not change: `role_context`, `layer_context`, `output_format`, `validator`.

---

## CS-02 — Two-Pass Recursive RTT Analysis

**Purpose:** Extends CS-01 to depth=2. The second pass takes CS-01's `next_input` and goes deeper — producing claims that the first pass structurally could not reach. Use this when the first pass identifies a structural problem but does not yet explain why the structure exists or what the correct intervention level is.

---

### Grammar

```json
{
  "session_id": "cs-02-two-pass-rtt-20260925",
  "intent": "Produce a depth=2 RTT analysis of the input statement, identifying all three structural faces at both pass levels. The second pass must produce at least one claim that is structurally distinct from all first-pass claims. Package the second-pass output as a valid InputUnit for a potential third pass.",
  "scope": "This session covers two RTT passes on the single input below. It does not cover a third pass, lateral inputs, or the design of any specific intervention.",
  "active_modules": [
    "rtt-anchor-definition",
    "session-grammar-anchor",
    "session-grammar-field-input",
    "session-grammar-field-output-format",
    "session-grammar-field-validator",
    "rtt-op-core",
    "rtt-op-recursive-extension",
    "clarity-val-rtt-output"
  ],
  "role_context": "operator",
  "layer_context": "operational",
  "input": {
    "content": "Our engineering team ships features on time but the features rarely get adopted. Leadership keeps asking why, and the team keeps pointing to the product roadmap. Nobody is looking at the gap between what ships and what users actually need.",
    "scope": "A single organizational dynamic — scoped to the delivery-adoption gap, no broader organizational context."
  },
  "output_format": "StructuredFaces",
  "validator": "clarity-val-rtt-output"
}
```

---

### Execution

**Pass 1:**
```
RTT.pass(
  input: <InputUnit from grammar field 7>,
  depth: 1,
  output_format: StructuredFaces
)
```

*Output: same as CS-01. Pass 1 next_input:*

```json
{
  "content": "The team optimizes for delivery because delivery is what is measured. No feedback loop connects shipped features to usage data. The metric design is the structural failure.",
  "scope": "The metric design failure — scoped to the measurement system, not to team capability or roadmap content."
}
```

**Pass 2:**
```
RTT.pass(
  input: <next_input from Pass 1>,
  depth: 2,
  output_format: StructuredFaces
)
```

---

### Output

**Pass 1 output:** *(identical to CS-01 — omitted for brevity; see CS-01 output above)*

**Pass 2 output:**

```json
{
  "generative_face": "Metric design failures originate in the moment a team is formed and evaluated. At that moment, a proxy metric — one that is measurable, visible, and attributable to team effort — is selected to stand in for the actual goal. Delivery velocity is an excellent proxy metric: it is unambiguous, timely, and clearly within the team's control. The problem is that it was selected without establishing a second metric that tracks the gap between the proxy and the goal. Once the proxy metric is the only metric, the proxy becomes the goal.",
  "present_face": "The team is operating correctly inside a measurement monoculture. A measurement monoculture is a system with one metric, where that metric is used to define success, allocate resources, and evaluate performance. Monocultures are stable but brittle — they optimize efficiently for the metric and fail silently on everything the metric does not capture. The adoption gap is invisible in this system not because nobody cares about it but because no instrument in the current measurement system can detect it.",
  "terminal_face": "Correcting a measurement monoculture requires adding a second metric, not replacing the first. The intervention is not 'stop measuring delivery' — removing the delivery metric destroys the team's operational clarity. The intervention is 'add a usage metric with the same visibility and cadence as the delivery metric.' When both metrics are visible side by side, the gap between them becomes the diagnostic signal the system has been missing.",
  "pass_depth": 2,
  "next_input": {
    "content": "The team operates inside a measurement monoculture. The correct intervention is not to replace the delivery metric but to add a usage metric with equivalent visibility and cadence. The gap between the two metrics is the diagnostic signal.",
    "scope": "The measurement monoculture diagnosis and the two-metric intervention design — scoped to metric design, not to implementation, tooling, or organizational change management."
  }
}
```

---

### Assessment

```json
{
  "validator_id": "clarity-val-rtt-output",
  "session_id": "cs-02-two-pass-rtt-20260925",
  "pass_depth_evaluated": 2,
  "criteria_results": [
    {
      "criterion": "Face completeness",
      "status": "satisfied",
      "notes": "All three faces present in both passes."
    },
    {
      "criterion": "Face substantiveness",
      "status": "satisfied",
      "notes": "Pass 2 present face names the measurement monoculture precisely. Terminal face specifies the intervention type (add, not replace) and the intervention design (usage metric with equivalent visibility and cadence)."
    },
    {
      "criterion": "Pass differentiation",
      "status": "satisfied",
      "notes": "Pass 1 identified the metric design failure. Pass 2 explained why metric design failures form (the proxy substitution moment) and introduced the measurement monoculture concept — structurally distinct from Pass 1."
    },
    {
      "criterion": "Scope compliance",
      "status": "satisfied",
      "notes": "No reference to implementation, tooling, or organizational change management. Output stayed within declared scope."
    },
    {
      "criterion": "Intent fulfillment",
      "status": "satisfied",
      "notes": "Depth=2 achieved. Pass 2 produced structurally distinct claims. next_input packaged correctly."
    }
  ],
  "overall_coherence": "high",
  "flags": [],
  "recommendation": "accept"
}
```

---

### Clone Guide

| Field | What to Change |
|-------|---------------|
| `session_id` | New unique ID |
| `intent` | Keep the differentiation requirement clause; replace the input description |
| `scope` | Replace content; keep the "does not cover a third pass" exclusion |
| `input` | Your InputUnit |
| `active_modules` | Add `rtt-op-recursive-extension` if not already present |

CS-02 is CS-01 with `rtt-op-recursive-extension` added to `active_modules` and `depth` set to 2 in the Pass 2 invocation. Everything else is structurally identical.

---

## CS-03 — Scope Compliance Check

**Purpose:** Verifies that a module's prose content (`module.md`) does not exceed the scope declared in its manifest (`module.json`). Use this before ratifying any new module, after any `module.md` edit, and whenever a module's content feels like it is claiming more than it should.

---

### Grammar

```json
{
  "session_id": "cs-03-scope-check-20260925",
  "intent": "Evaluate whether the prose content of `rtt-op-core`'s module.md stays within the scope declared in its module.json manifest. Produce a ScopeComplianceReport identifying any violations, near-violations, or confirmed compliance.",
  "scope": "This session covers the scope compliance check of rtt-op-core's module.md against its module.json scope field. It does not cover the module's dependency chain, its session bindings, or its compatibility with other modules.",
  "active_modules": [
    "rtt-anchor-definition",
    "session-grammar-anchor",
    "session-grammar-field-input",
    "session-grammar-field-output-format",
    "session-grammar-field-validator",
    "scope-check-op",
    "scope-statement-grammar",
    "module-manifest-grammar",
    "scope-val",
    "manifest-complete-val"
  ],
  "role_context": "validator",
  "layer_context": "operational",
  "input": {
    "content": "Module: rtt-op-core. Manifest scope: 'Defines the invocation signature, input schema, and output schema for a single RTT pass on any well-formed input unit.' Target file: module.md.",
    "scope": "The scope compliance evaluation of rtt-op-core's module.md — scoped to this single module and this single file."
  },
  "output_format": "NarrativeAnalysis",
  "validator": "scope-val"
}
```

---

### Execution

**Step 1: Verify manifest completeness**
```
Manifest.validate(
  module_id: "rtt-op-core",
  check: manifest-complete-val
)
```

*Result: all four files present, all required fields non-empty. Proceed.*

**Step 2: Run scope compliance check**
```
Scope.check(
  module_id: "rtt-op-core",
  target_file: module.md,
  manifest_ref: "rtt-op-core"
)
```

---

### Output

```
SCOPE COMPLIANCE REPORT — rtt-op-core / module.md
Session: cs-03-scope-check-20260925

MANIFEST SCOPE (verbatim):
"Defines the invocation signature, input schema, and output schema for a single RTT pass
on any well-formed input unit."

COMPLIANCE EVALUATION:

SECTION: Invocation Signature
Status: IN SCOPE
Notes: The module.md correctly specifies RTT.pass() with all parameters named, typed,
and marked required or optional. No overclaiming detected.

SECTION: Input Schema
Status: IN SCOPE
Notes: The InputUnit definition — content field, scope field, well-formedness criteria —
is bounded correctly. The module.md does not attempt to define what "well-formed" means
at the philosophical level; it defines the structural criteria only. Correct.

SECTION: Output Schema
Status: IN SCOPE
Notes: The five output fields (generative_face, present_face, terminal_face, pass_depth,
next_input) are defined with types and constraints. Correct.

SECTION: RTT Conceptual Explanation (paragraphs 3-5)
Status: NEAR-VIOLATION — FLAG FOR REVIEW
Notes: Paragraphs 3 through 5 of module.md explain the conceptual basis of the three
structural faces. This content is informative and accurate, but it exceeds the scope
declaration, which covers only the invocation signature, input schema, and output schema.
The conceptual explanation of RTT belongs in rtt-anchor-definition, not in rtt-op-core.

Recommendation: Move paragraphs 3-5 to rtt-anchor-definition or add an editorial
cross-reference that makes clear this content is provided for reader convenience and
does not constitute a scope claim by rtt-op-core.

SECTION: Worked Example (final section)
Status: IN SCOPE
Notes: The worked example demonstrates the invocation signature and shows a complete
input/output pair. It does not make conceptual claims beyond the operator's scope.

OVERALL COMPLIANCE: NEAR-COMPLIANT — one near-violation requires resolution before ratification.
```

---

### Assessment

```json
{
  "validator_id": "scope-val",
  "session_id": "cs-03-scope-check-20260925",
  "criteria_results": [
    {
      "criterion": "Scope boundary respected",
      "status": "not_satisfied",
      "notes": "Paragraphs 3-5 of module.md exceed the manifest scope. Content belongs in rtt-anchor-definition."
    },
    {
      "criterion": "No underclaiming detected",
      "status": "satisfied",
      "notes": "All three declared scope elements (invocation signature, input schema, output schema) are addressed in module.md."
    },
    {
      "criterion": "Cross-references are editorial not structural",
      "status": "satisfied",
      "notes": "No structural cross-references embedded in prose."
    }
  ],
  "overall_coherence": "moderate",
  "flags": ["near-violation: paragraphs 3-5 exceed scope"],
  "recommendation": "revise"
}
```

---

### Clone Guide

| Field | What to Change |
|-------|---------------|
| `session_id` | New unique ID |
| `intent` | Replace `rtt-op-core` with your target module ID |
| `scope` | Replace module name; keep the exclusion clause |
| `input.content` | Replace with your module's ID, manifest scope (verbatim), and target file |
| `input.scope` | Replace module name |
| `active_modules` | No changes needed |

The `Scope.check()` invocation parameters change: swap `module_id` and `manifest_ref` to your target module.

---

## CS-04 — Dependency Audit

**Purpose:** Performs a complete forward traversal of a module's dependency chain, detects hidden dependencies, and identifies any cycle risks. Use this before invoking any unfamiliar module in a session, before modifying a foundational module, and as a routine check when assembling a new `active_modules` list.

---

### Grammar

```json
{
  "session_id": "cs-04-dependency-audit-20260925",
  "intent": "Perform a complete forward traversal of clarity-op-spectral's dependency chain, identify all transitive dependencies, flag any hidden dependencies detected in module.md prose, and confirm the chain is cycle-free. Produce a DependencyTrace report.",
  "scope": "This session covers the dependency audit of clarity-op-spectral only. It does not cover the audit of modules in the traversal chain — those are separate sessions if needed.",
  "active_modules": [
    "rtt-anchor-definition",
    "session-grammar-anchor",
    "session-grammar-field-input",
    "session-grammar-field-output-format",
    "session-grammar-field-validator",
    "dependency-trace-op",
    "dependency-audit-proto",
    "dependency-val",
    "manifest-complete-val"
  ],
  "role_context": "operator",
  "layer_context": "operational",
  "input": {
    "content": "Module: clarity-op-spectral. Direction: forward (surface to foundational).",
    "scope": "The dependency audit of clarity-op-spectral — forward traversal only."
  },
  "output_format": "DependencyTrace",
  "validator": "dependency-val"
}
```

---

### Execution

```
Dependency.trace(
  module_id: "clarity-op-spectral",
  direction: forward,
  detect_hidden: true,
  output_format: DependencyTrace
)
```

---

### Output

```
DEPENDENCY TRACE — clarity-op-spectral (forward)
Session: cs-04-dependency-audit-20260925

STARTING MODULE: clarity-op-spectral
  Role: operator | Layer: operational | Status: active | Version: 1.2.0

LEVEL 1 — Direct Dependencies (from module_links.json → depends_on):
  ├─ rtt-op-core              [operator / operational / active]
  ├─ nawderian-theorem-validator-pulses  [anchor / foundational / active]
  └─ clarity-grammar-validator-assessment  [grammar / structural / active]

LEVEL 2 — Dependencies of Level 1:

  rtt-op-core depends on:
    ├─ rtt-anchor-definition   [anchor / foundational / active] ← ANCHOR REACHED
    ├─ session-grammar-field-input  [field / structural / active]
    │    └─ depends on: session-grammar-anchor  [anchor / foundational / active] ← ANCHOR REACHED
    └─ session-grammar-field-output-format  [field / structural / active]
         └─ depends on: session-grammar-anchor ← ALREADY RESOLVED

  nawderian-theorem-validator-pulses depends on:
    └─ (none) ← FOUNDATIONAL ANCHOR — no further traversal

  clarity-grammar-validator-assessment depends on:
    └─ validator-assessment-grammar  [grammar / structural / active]
         └─ depends on: (none) ← STRUCTURAL LEAF — no further traversal

FULL RESOLVED DEPENDENCY SET (unique modules):
  1. clarity-op-spectral
  2. rtt-op-core
  3. nawderian-theorem-validator-pulses
  4. clarity-grammar-validator-assessment
  5. rtt-anchor-definition
  6. session-grammar-field-input
  7. session-grammar-anchor
  8. session-grammar-field-output-format
  9. validator-assessment-grammar

HIDDEN DEPENDENCY CHECK:
  Scanning clarity-op-spectral/module.md for prose references to
  modules not in the declared depends_on list...

  FINDING: module.md paragraph 6 references "the five clarity criteria"
  and cites clarity-val-rtt-output as the default validator for RTT outputs.
  clarity-val-rtt-output does NOT appear in depends_on.

  CLASSIFICATION: NEAR-HIDDEN DEPENDENCY
  Notes: The reference is editorial (a cross-reference for reader convenience),
  not structural — the operator does not require clarity-val-rtt-output to function.
  However, practitioners reading module.md in isolation may invoke
  clarity-val-rtt-output assuming it is an active dependency. Recommend adding
  clarity-val-rtt-output to the 'related' field in module_links.json to
  make the editorial relationship explicit.

CYCLE CHECK:
  No cycles detected. Graph is acyclic. ✓

MINIMUM active_modules LIST for any session invoking clarity-op-spectral:
  [
    "rtt-anchor-definition",
    "session-grammar-anchor",
    "session-grammar-field-input",
    "session-grammar-field-output-format",
    "nawderian-theorem-validator-pulses",
    "clarity-grammar-validator-assessment",
    "validator-assessment-grammar",
    "rtt-op-core",
    "clarity-op-spectral"
  ]
```

---

### Assessment

```json
{
  "validator_id": "dependency-val",
  "session_id": "cs-04-dependency-audit-20260925",
  "criteria_results": [
    {
      "criterion": "Dependency list complete",
      "status": "satisfied",
      "notes": "All transitive dependencies resolved. Minimum active_modules list produced."
    },
    {
      "criterion": "No cycles detected",
      "status": "satisfied",
      "notes": "Graph is acyclic."
    },
    {
      "criterion": "No hidden structural dependencies",
      "status": "satisfied",
      "notes": "The near-hidden dependency on clarity-val-rtt-output is editorial, not structural. Not a structural gap."
    }
  ],
  "overall_coherence": "high",
  "flags": ["editorial near-hidden dependency: clarity-val-rtt-output referenced in prose but not in depends_on — recommend adding to related field"],
  "recommendation": "accept"
}
```

---

### Clone Guide

| Field | What to Change |
|-------|---------------|
| `session_id` | New unique ID |
| `intent` | Replace `clarity-op-spectral` with your target module |
| `scope` | Replace module name |
| `input.content` | Replace module ID; keep direction: forward for most audits |
| `active_modules` | No changes needed |

For backward traversal (foundation → impact surface), change `direction: forward` to `direction: backward` in the invocation. The intent and scope should be updated to reflect the backward direction.

---

## CS-05 — Gap Identification and Module Draft

**Purpose:** Confirms a suspected gap in the module registry and produces a minimum valid four-file module draft to fill it. Use this when the module discovery protocol returns no suitable candidates, when a hidden dependency is structural rather than editorial, or when a practitioner identifies a missing operator, validator, or grammar module during session work.

---

### Grammar

```json
{
  "session_id": "cs-05-gap-and-draft-20260925",
  "intent": "Confirm the suspected gap — the absence of a usage-metric-grammar module in the grammar-suite — classify its type, verify it is not an apparent gap, and produce a minimum valid four-file draft for the missing module using the four anchoring decisions.",
  "scope": "This session covers gap confirmation and draft authoring for one suspected module only. It does not cover ratification, dependency chain updates for existing modules, or implementation of the module's content beyond the minimum valid draft.",
  "active_modules": [
    "rtt-anchor-definition",
    "session-grammar-anchor",
    "session-grammar-field-input",
    "session-grammar-field-output-format",
    "session-grammar-field-validator",
    "gap-identify-op",
    "module-author-op",
    "module-manifest-grammar",
    "module-id-grammar",
    "scope-statement-grammar",
    "input-unit-grammar",
    "module-id-val",
    "manifest-complete-val"
  ],
  "role_context": "operator",
  "layer_context": "operational",
  "input": {
    "content": "Suspected gap: no module in the grammar-suite defines the structure of a usage metric specification — what fields are required, what types are valid, and what validation rules apply. The usage metric concept appears in CS-02's second-pass output and in the measurement-monoculture intervention design, but no grammar module specifies its structure.",
    "scope": "The suspected gap in the grammar-suite — scoped to the single missing grammar module, not to the broader measurement framework."
  },
  "output_format": "ModuleSpec",
  "validator": "manifest-complete-val"
}
```

---

### Execution

**Step 1: Confirm the gap**
```
Gap.identify(
  description: "A grammar module specifying the structure of a usage metric specification — required fields, valid types, and validation rules.",
  expected_role: grammar,
  expected_layer: structural,
  search_groups: ["grammar-suite", "clarity-system", "session-grammar"]
)
```

*Gap identification result:*
```
GAP CONFIRMATION REPORT
Type: Soft gap (Type 2 — missing role/layer intersection)
Evidence: No module in grammar-suite, clarity-system, or session-grammar has a scope
covering the structural specification of a usage metric. The closest module is
'output-unit-grammar' (grammar / structural), whose scope covers OutputUnit structure —
not usage metric structure. These are distinct domains.
Apparent gap check: NEGATIVE — no synonym search produced a matching scope.
Gap is real. Proceed to authoring.
```

**Step 2: Make the four anchoring decisions**

| Decision | Value | Rationale |
|----------|-------|-----------|
| Role | `grammar` | This module specifies a structural pattern — the valid form of a usage metric specification |
| Layer | `structural` | Usage metric specifications are structural patterns; they do not perform transformations or define canon |
| Scope | "Specifies the required structure of a usage metric specification: required fields, valid field types, validation rules, and the minimum valid form." | Precise, bounded, testable |
| Dependencies | `session-grammar-anchor`, `output-unit-grammar` | The usage metric grammar must be consistent with the session grammar's output expectations and the OutputUnit structure |

**Step 3: Draft the module**
```
Module.draft(
  role: grammar,
  layer: structural,
  scope: "Specifies the required structure of a usage metric specification: required fields, valid field types, validation rules, and the minimum valid form.",
  dependencies: ["session-grammar-anchor", "output-unit-grammar"],
  output_format: ModuleSpec
)
```

---

### Output

**`module.json` draft:**
```json
{
  "id": "usage-metric-grammar",
  "label": "Usage Metric Grammar",
  "role": "grammar",
  "layer": "structural",
  "scope": "Specifies the required structure of a usage metric specification: required fields, valid field types, validation rules, and the minimum valid form.",
  "version": "0.1.0",
  "status": "draft",
  "dependencies": [
    "session-grammar-anchor",
    "output-unit-grammar"
  ],
  "tags": ["grammar", "metrics", "measurement", "structural"]
}
```

**`module_links.json` draft:**
```json
{
  "id": "usage-metric-grammar",
  "depends_on": [
    "session-grammar-anchor",
    "output-unit-grammar"
  ],
  "required_by": [],
  "related": [
    "clarity-grammar-validator-assessment",
    "scope-statement-grammar"
  ],
  "supersedes": [],
  "superseded_by": null
}
```

**`module.md` draft (minimum content):**
```markdown
# Usage Metric Grammar

## Scope
Specifies the required structure of a usage metric specification: required fields,
valid field types, validation rules, and the minimum valid form.

## Required Fields

A usage metric specification must contain exactly the following fields:

| Field | Type | Description | Required |
|-------|------|-------------|----------|
| `metric_id` | string | Unique identifier for this metric | yes |
| `label` | string | Human-readable metric name | yes |
| `measures` | string | What this metric measures, in one sentence | yes |
| `unit` | string | The unit of measurement (e.g., %, count, score) | yes |
| `cadence` | string | How often this metric is measured (e.g., weekly, per-deploy) | yes |
| `visibility` | enum | Who can see this metric: team, leadership, public | yes |
| `baseline` | number or null | The starting value before any intervention | no |
| `target` | number or null | The desired value after intervention | no |

## Minimum Valid Form

A minimum valid usage metric specification contains the six required fields.
The two optional fields (baseline, target) may be omitted when the metric is
first defined and added later as measurement begins.

## Validation Rules

1. `metric_id` must be unique across all usage metrics in the same session context.
2. `measures` must be a single declarative sentence ending with a period.
3. `cadence` must be consistent with the deployment or release cycle of the
   system being measured.
4. `visibility` must be one of: team, leadership, public.

## Notes
This grammar is a draft. The required fields and validation rules are subject to
revision through the ratification process. Do not treat this as the ratified
specification until version ≥ 1.0.0.
```

**`module_session.json` draft:**
```json
{
  "id": "usage-metric-grammar",
  "invocation_syntax": "UsageMetric.validate(spec: <UsageMetricSpec>)",
  "input_schema": {
    "spec": "A candidate usage metric specification — an object with at minimum the six required fields."
  },
  "output_schema": {
    "status": "valid | invalid",
    "missing_fields": "Array of required field names that are absent.",
    "validation_errors": "Array of validation rule violations with field name and rule reference.",
    "minimum_valid": "Boolean. True if the six required fields are all present and valid."
  },
  "valid_layers": ["structural", "operational"],
  "valid_roles": ["grammar", "validator", "operator"],
  "validator_id": "module-id-val"
}
```

---

### Assessment

```json
{
  "validator_id": "manifest-complete-val",
  "session_id": "cs-05-gap-and-draft-20260925",
  "criteria_results": [
    {
      "criterion": "All four files present",
      "status": "satisfied",
      "notes": "module.json, module_links.json, module.md, and module_session.json all drafted."
    },
    {
      "criterion": "All required fields non-empty",
      "status": "satisfied",
      "notes": "All manifest fields populated. Status correctly set to draft."
    },
    {
      "criterion": "ID conforms to naming convention",
      "status": "satisfied",
      "notes": "usage-metric-grammar: domain=usage-metric, role_short=grammar. Valid."
    }
  ],
  "overall_coherence": "high",
  "flags": ["draft status — requires ratification before active use"],
  "recommendation": "accept"
}
```

---

### Clone Guide

| Field | What to Change |
|-------|---------------|
| `session_id` | New unique ID |
| `intent` | Replace the specific gap description with your suspected gap |
| `scope` | Replace gap description; keep the ratification exclusion |
| `input.content` | Your gap description, expected role, expected layer, groups searched |
| `active_modules` | No changes needed |

The four anchoring decisions (Step 2) are the most important part of this session to get right. Apply RTT to the gap description before making them — the terminal face will surface the intervention type, which maps to the role.

---

## CS-06 — Multi-Lens RTT Analysis

**Purpose:** Applies two lenses simultaneously during a depth=2 RTT analysis, producing lens-annotated face outputs that surface dimensions the neutral analysis would miss. Use this when a problem has strong temporal dynamics, complex stakeholder interests, or when prior neutral RTT passes feel incomplete or one-dimensional.

**Lenses active in this session:** `lens-temporal` + `lens-stakeholder`

---

### Grammar

```json
{
  "session_id": "cs-06-multi-lens-rtt-20260925",
  "intent": "Produce a depth=2 RTT analysis of the input statement with temporal and stakeholder lenses simultaneously active. Each face in each pass must include lens-specific annotations — temporal annotations marking time-dependence, stakeholder annotations marking whose interests are at stake. Package the second-pass output as a valid InputUnit.",
  "scope": "This session covers a depth=2 RTT analysis with two active lenses. It does not cover lens-free analysis of the same input, comparison of lens-active vs lens-free outputs, or lens application beyond temporal and stakeholder.",
  "active_modules": [
    "rtt-anchor-definition",
    "session-grammar-anchor",
    "session-grammar-field-input",
    "session-grammar-field-output-format",
    "session-grammar-field-validator",
    "rtt-op-core",
    "rtt-op-recursive-extension",
    "rtt-lens-temporal",
    "rtt-lens-stakeholder",
    "bridge-lens-to-rtt",
    "lens-temporal",
    "lens-stakeholder",
    "clarity-val-rtt-output"
  ],
  "role_context": "operator",
  "layer_context": "operational",
  "input": {
    "content": "A mid-sized company has been running a hybrid work policy for two years. Productivity metrics are stable. Employee satisfaction scores have split: senior employees report high satisfaction; junior employees report declining satisfaction and increasing feelings of isolation. Leadership sees no problem.",
    "scope": "A single organizational dynamic — the diverging satisfaction split under hybrid work, scoped to the internal dynamic only, no external benchmarks."
  },
  "output_format": "StructuredFaces",
  "validator": "clarity-val-rtt-output"
}
```

---

### Execution

```
Lens.activate(lenses: ["lens-temporal", "lens-stakeholder"])

RTT.pass(
  input: <InputUnit from grammar field 7>,
  depth: 1,
  output_format: StructuredFaces,
  active_lenses: ["lens-temporal", "lens-stakeholder"]
)
```

---

### Output

**Pass 1 — Lens-Annotated:**

```json
{
  "generative_face": "The hybrid work policy was implemented two years ago during a period when hybrid work was framed as temporary accommodation. [TEMPORAL: The policy has since calcified from temporary accommodation into permanent structure, but without any structural redesign for permanence.] Senior employees built professional networks and social capital in-person before remote work existed; they arrived at hybrid with a full relationship graph to draw on. [STAKEHOLDER: Senior employees are not experiencing hybrid the same way junior employees are — they have pre-existing social infrastructure that hybrid preserves. Junior employees are arriving into a hybrid environment without having built that infrastructure first.] The policy is neutral in design. It is not neutral in effect.",
  "present_face": "A structural equity gap disguised as a policy outcome. The hybrid policy is operating identically for all employees, but its effects are asymmetric because the inputs — social capital at point of hire — are asymmetric. [TEMPORAL: This gap widens over time. Each month a junior employee works hybrid without building sufficient in-person social capital, the deficit compounds.] [STAKEHOLDER: Leadership sees stable productivity and senior satisfaction — their visibility into the junior experience is low. Junior employees see declining satisfaction but do not have organizational voice proportional to their concern. The stakeholders with the problem have the least power to surface it.]",
  "terminal_face": "Without intervention, two trajectories diverge. Senior employees stabilize. Junior employees either adapt (by creating informal in-person workarounds outside the policy) or exit. [TEMPORAL: The exit risk accelerates at the 18-month and 36-month marks — the points at which junior employees make deliberate career decisions.] [STAKEHOLDER: Exits disproportionately remove the employees with the most unmet social capital needs — creating a selection effect where the remaining junior population skews toward those who have found informal workarounds, making the problem invisible in aggregate data.] Leadership continues to see no problem, because the metric (productivity) does not capture what is failing.",
  "pass_depth": 1,
  "next_input": {
    "content": "The hybrid policy has asymmetric effects because social capital at point of hire is asymmetric. Junior employees arrive without the pre-existing relationship graph that makes hybrid work feel connected. The gap widens over time and the exits it produces are invisible in productivity metrics.",
    "scope": "The social capital asymmetry and its compounding dynamic — scoped to the structural mechanism, not to policy design or implementation."
  }
}
```

**Pass 2 — Lens-Annotated:**

```json
{
  "generative_face": "Social capital asymmetry in hybrid environments originates in onboarding design. In-person onboarding is a relationship-building mechanism: new employees meet colleagues, establish informal networks, and develop the social infrastructure that makes work feel connected. [TEMPORAL: This relationship-building is front-loaded — it happens in the first 3-6 months and then compounds.] Hybrid onboarding, unless specifically redesigned, provides the same information transfer as in-person onboarding but a fraction of the relationship-building opportunity. The deficit is invisible at hire. [STAKEHOLDER: Hiring managers see successful knowledge transfer and assume successful integration. The new hire sees successful knowledge transfer and underestimates the relationship deficit until 6-12 months later when the absence becomes felt.]",
  "present_face": "A design gap in onboarding — not in the hybrid policy itself. The hybrid policy can remain unchanged. What needs redesigning is the onboarding protocol: it must actively front-load relationship-building opportunities that in-person environments provide passively. [TEMPORAL: The intervention window is narrow — the first 90 days of employment are when relationship infrastructure is most efficiently built.] [STAKEHOLDER: This intervention primarily benefits junior employees and new hires. It does not require senior employees to change behavior. It does not require leadership to change the policy. It requires the HR and onboarding function to redesign one process.]",
  "terminal_face": "A redesigned onboarding protocol that front-loads structured relationship-building closes the social capital gap at the point of hire — before the deficit can compound. [TEMPORAL: Effects are detectable within one cohort cycle (6-12 months).] [STAKEHOLDER: Junior satisfaction scores recover. Exit rates at the 18-month decision point decline. Leadership's productivity metric remains stable — with the additional signal that junior satisfaction is now tracking senior satisfaction rather than diverging from it.] The hybrid policy is validated rather than blamed.",
  "pass_depth": 2,
  "next_input": {
    "content": "The intervention is onboarding redesign — specifically, structured front-loading of relationship-building opportunities in the first 90 days. The hybrid policy does not need to change. The onboarding protocol does.",
    "scope": "The onboarding redesign intervention — scoped to protocol design, not to content, facilitators, budget, or rollout sequence."
  }
}
```

---

### Assessment

```json
{
  "validator_id": "clarity-val-rtt-output",
  "session_id": "cs-06-multi-lens-rtt-20260925",
  "criteria_results": [
    {
      "criterion": "Face completeness",
      "status": "satisfied",
      "notes": "All three faces present in both passes. Lens annotations present in all six faces."
    },
    {
      "criterion": "Face substantiveness",
      "status": "satisfied",
      "notes": "Lens annotations are specific and additive — they surface claims (exit risk timing, 90-day intervention window, stakeholder power asymmetry) that the neutral analysis would not have produced."
    },
    {
      "criterion": "Pass differentiation",
      "status": "satisfied",
      "notes": "Pass 1 identified the social capital asymmetry. Pass 2 traced it to onboarding design and specified the intervention window and intervention type. Structurally distinct."
    },
    {
      "criterion": "Scope compliance",
      "status": "satisfied",
      "notes": "No reference to external benchmarks, policy design, or implementation details. Lens annotations stayed within scope."
    },
    {
      "criterion": "Intent fulfillment",
      "status": "satisfied",
      "notes": "Both lenses active in both passes. Annotations present. next_input packaged."
    }
  ],
  "overall_coherence": "high",
  "flags": [],
  "recommendation": "accept"
}
```

---

### Clone Guide

| Field | What to Change |
|-------|---------------|
| `session_id` | New unique ID |
| `intent` | Replace input description; keep the lens annotation requirement |
| `scope` | Replace content; keep the lens-comparison exclusion |
| `input` | Your InputUnit |
| `active_modules` | Swap lenses as needed — remove `rtt-lens-temporal` / `lens-temporal` and/or `rtt-lens-stakeholder` / `lens-stakeholder`; add your chosen lenses and their bridge modules |

For different lens combinations: add/remove lens pairs (each lens appears twice — its primary ID in core-engine or lens-suite, and its bridge module in bridge-suite). Update the `Lens.activate()` call and the `active_lenses` parameter accordingly.

---

## CS-07 — Session Diagnosis and Repair

**Purpose:** Diagnoses a malformed session — one that has been initialized with structural errors — and produces a repaired grammar. Use this when a session produces unexpected outputs, when a validator returns `insufficient_input` for reasons that cannot be traced to the input itself, or when you inherit a session from another practitioner and need to verify its integrity.

---

### Grammar

```json
{
  "session_id": "cs-07-session-diagnosis-20260925",
  "intent": "Diagnose the structural errors in the malformed session below, identify which of the four canonical failure modes apply, produce a repaired version of the malformed grammar, and confirm the repair passes all nine field tests.",
  "scope": "This session covers the diagnosis and repair of the single malformed session presented as input. It does not cover re-running the repaired session or evaluating its outputs.",
  "active_modules": [
    "rtt-anchor-definition",
    "session-grammar-anchor",
    "session-grammar-field-input",
    "session-grammar-field-output-format",
    "session-grammar-field-validator",
    "session-grammar-complete-val",
    "active-modules-closure-val",
    "intent-val",
    "scope-compliance-val",
    "invocation-val",
    "session-field-test-op",
    "dependency-trace-op",
    "dependency-val"
  ],
  "role_context": "validator",
  "layer_context": "operational",
  "input": {
    "content": "MALFORMED SESSION: { session_id: 'test-1', intent: 'think about whether our hiring process is working', scope: 'hiring', active_modules: ['rtt-op-core', 'clarity-val-rtt-output'], role_context: 'operator', layer_context: 'operational', input: 'Our hiring process.', output_format: 'some kind of analysis', validator: 'clarity-val-rtt-output' }",
    "scope": "The structural diagnosis of the single malformed session above — scoped to grammar errors and active_modules gaps."
  },
  "output_format": "NarrativeAnalysis",
  "validator": "session-grammar-complete-val"
}
```

---

### Execution

```
Session.diagnose(
  target_session: <malformed session from input>,
  apply_field_tests: all,
  check_closure: true
)
```

---

### Output

```
SESSION DIAGNOSIS REPORT
Session: cs-07-session-diagnosis-20260925
Target: 'test-1' (malformed)

FIELD-BY-FIELD DIAGNOSIS:

Field 1 — session_id: 'test-1'
  Status: FAIL
  Reason: 'test-1' is not unique. It does not follow the recommended format
  [domain]-[date]-[sequence]. It will collide with any other session named
  'test-1' in the practitioner's history.
  Fix: Rename to '[domain]-[YYYYMMDD]-01'

Field 2 — intent: 'think about whether our hiring process is working'
  Status: FAIL
  Reason: Violates the actionability test. 'Think about' is a prohibited
  phrasing pattern — it is not directed at a deliverable. No testable
  success criterion is implied. Cannot answer "did we achieve the intent?"
  with a binary yes/no.
  Fix: Rewrite as a deliverable. Example: 'Produce a single-depth RTT
  analysis of the hiring process input, identifying the structural failure
  at each face and packaging the output as a valid StructuredFaces unit.'

Field 3 — scope: 'hiring'
  Status: FAIL
  Reason: Single word. No inclusion declaration. No exclusion declaration.
  Does not follow the inclusion/exclusion format. Cannot be used as a
  scope check at any point during the session.
  Fix: Rewrite as: 'This session covers a single-depth RTT analysis of
  the hiring process description in Field 7. It does not cover compensation
  structure, onboarding, or retention.'

Field 4 — active_modules: ['rtt-op-core', 'clarity-val-rtt-output']
  Status: FAIL (dependency closure)
  Running closure check...
  rtt-op-core depends on: rtt-anchor-definition, session-grammar-field-input,
    session-grammar-field-output-format, session-grammar-anchor
  clarity-val-rtt-output depends on: nawderian-theorem-validator-pulses,
    session-grammar-anchor
  None of these dependencies appear in the declared active_modules list.
  MISSING: rtt-anchor-definition, session-grammar-field-input,
    session-grammar-field-output-format, session-grammar-anchor,
    nawderian-theorem-validator-pulses
  Fix: Add all 5 missing modules. Reorder list foundational-first.

Fields 5 & 6 — role_context / layer_context
  Status: PASS (operator / operational are valid values and correct for
  RTT analysis sessions)

Field 7 — input: 'Our hiring process.'
  Status: FAIL
  Reason: Raw string, not an InputUnit. Missing content/scope structure.
  'Our hiring process.' has no declared scope — the operator cannot
  validate that the input is well-formed.
  Fix: Wrap in InputUnit format with explicit scope declaration.

Field 8 — output_format: 'some kind of analysis'
  Status: FAIL
  Reason: Not a FormatEnum value. 'Some kind of analysis' is not
  checkable — the validator cannot determine whether the output matches
  this specification. Likely intended: StructuredFaces.
  Fix: Replace with 'StructuredFaces'

Field 9 — validator: 'clarity-val-rtt-output'
  Status: PASS (valid module ID, present in active_modules after fix,
  compatible with StructuredFaces output format)

FAILURE MODE CLASSIFICATION:
  - Failure Mode 1: Underspecified Intent ✓ (intent field FAIL)
  - Failure Mode 3: Dependency Gap ✓ (active_modules FAIL)
  No evidence of Failure Mode 2 (scope creep) or Failure Mode 4
  (comfort-filtering) — session never ran.

REPAIRED GRAMMAR:

{
  "session_id": "hiring-rtt-analysis-20260925-01",
  "intent": "Produce a single-depth RTT analysis of the hiring process input, identifying the structural failure at each face and packaging the output as a valid StructuredFaces unit.",
  "scope": "This session covers a single-depth RTT analysis of the hiring process description in Field 7. It does not cover compensation structure, onboarding, or retention.",
  "active_modules": [
    "rtt-anchor-definition",
    "session-grammar-anchor",
    "session-grammar-field-input",
    "session-grammar-field-output-format",
    "session-grammar-field-validator",
    "nawderian-theorem-validator-pulses",
    "rtt-op-core",
    "clarity-val-rtt-output"
  ],
  "role_context": "operator",
  "layer_context": "operational",
  "input": {
    "content": "[Practitioner to provide actual hiring process description here]",
    "scope": "A description of the current hiring process — scoped to the process steps, not to compensation, onboarding, or retention."
  },
  "output_format": "StructuredFaces",
  "validator": "clarity-val-rtt-output"
}
```

---

### Assessment

```json
{
  "validator_id": "session-grammar-complete-val",
  "session_id": "cs-07-session-diagnosis-20260925",
  "criteria_results": [
    {
      "criterion": "All nine fields present and non-empty",
      "status": "satisfied",
      "notes": "Repaired grammar has all nine fields populated."
    },
    {
      "criterion": "All field-level tests pass",
      "status": "satisfied",
      "notes": "All fields in the repaired grammar pass their individual field tests. Note: input.content is a placeholder — the practitioner must replace it before running."
    },
    {
      "criterion": "active_modules closure complete",
      "status": "satisfied",
      "notes": "All five missing dependencies added. Closure verified."
    }
  ],
  "overall_coherence": "high",
  "flags": ["input.content is a placeholder — must be replaced before session execution"],
  "recommendation": "accept"
}
```

---

### Clone Guide

| Field | What to Change |
|-------|---------------|
| `session_id` | New unique ID |
| `intent` | Replace with reference to your malformed session |
| `input.content` | The full text of the malformed session grammar to diagnose |
| `active_modules` | No changes needed |

This session template works for any malformed session. The diagnostic output is deterministic — it runs all nine field tests and the closure check regardless of the specific errors present.

---

## CS-08 — Clarity Evaluation of an Existing Output

**Purpose:** Applies the Spectral Clarity model to an output that was produced in a prior session, producing a full ValidatorAssessment. Use this when a prior session closed without a formal validator application, when you want to audit an existing body of work against the system's clarity standard, or when a previously accepted output is being contested.

---

### Grammar

```json
{
  "session_id": "cs-08-clarity-eval-20260925",
  "intent": "Apply the Spectral Clarity model to the CS-01 output and produce a ValidatorAssessment that states the status of all five clarity criteria, the overall coherence rating, any flags, and a recommendation.",
  "scope": "This session covers clarity evaluation of the CS-01 output only. It does not cover re-running CS-01, modifying its output, or comparison with other outputs.",
  "active_modules": [
    "rtt-anchor-definition",
    "session-grammar-anchor",
    "session-grammar-field-input",
    "session-grammar-field-output-format",
    "session-grammar-field-validator",
    "nawderian-theorem-validator-pulses",
    "clarity-anchor-standard",
    "clarity-op-spectral",
    "clarity-val-rtt-output",
    "clarity-grammar-validator-assessment",
    "bridge-session-to-clarity"
  ],
  "role_context": "validator",
  "layer_context": "operational",
  "input": {
    "content": "Prior output to evaluate — CS-01 StructuredFaces output: { generative_face: 'The team's success metric is delivery velocity...', present_face: 'A structural decoupling between delivery and adoption...', terminal_face: 'Without intervention, the gap compounds...', pass_depth: 1, next_input: { content: '...', scope: '...' } }",
    "scope": "The CS-01 StructuredFaces output — scoped to this single output unit, depth=1."
  },
  "output_format": "ValidatorAssessment",
  "validator": "clarity-val-rtt-output"
}
```

---

### Execution

```
Clarity.evaluate(
  input: <CS-01 OutputUnit from grammar field 7>,
  theorem_ref: "nawderian-theorem-validator-pulses",
  validator_id: "clarity-val-rtt-output",
  output_format: ValidatorAssessment
)
```

---

### Output

```json
{
  "validator_id": "clarity-val-rtt-output",
  "theorem_applied": "nawderian-theorem-validator-pulses",
  "session_id": "cs-08-clarity-eval-20260925",
  "target_session_id": "cs-01-baseline-rtt-20260925",
  "pass_depth_evaluated": 1,
  "criteria_results": [
    {
      "criterion": "Face completeness",
      "status": "satisfied",
      "notes": "All three faces present. next_input packaged correctly."
    },
    {
      "criterion": "Face substantiveness",
      "status": "satisfied",
      "notes": "Generative face names the specific mechanism (metric selected upstream, never challenged). Present face names the structural decoupling precisely and eliminates alternative explanations (not motivation, not skill). Terminal face names a specific drift pattern (blame attribution replacing structural diagnosis)."
    },
    {
      "criterion": "Pass differentiation",
      "status": "satisfied",
      "notes": "Single pass — criterion not applicable at depth=1."
    },
    {
      "criterion": "Scope compliance",
      "status": "satisfied",
      "notes": "Output does not reference broader organizational context, individual performance, or adjacent systems. Stayed within declared scope."
    },
    {
      "criterion": "Intent fulfillment",
      "status": "satisfied",
      "notes": "StructuredFaces output produced. Output matches declared format."
    }
  ],
  "signal_coherence_rating": {
    "generative_face": "high",
    "present_face": "high",
    "terminal_face": "moderate",
    "notes": "Terminal face is the weakest of the three — 'the gap compounds' is directionally correct but less specific than the other two faces. It states the direction of drift without quantifying the compounding mechanism. This is below the threshold for a flag but noted for practitioners who intend to extend this output at depth=2."
  },
  "overall_coherence": "high",
  "flags": [],
  "recommendation": "accept"
}
```

---

### Assessment

*This session's output is itself a ValidatorAssessment — the session-level validator evaluates the quality of the assessment produced, not the quality of the CS-01 output.*

```json
{
  "validator_id": "clarity-val-session-output",
  "session_id": "cs-08-clarity-eval-20260925",
  "criteria_results": [
    {
      "criterion": "Output matches declared format",
      "status": "satisfied",
      "notes": "Output is a ValidatorAssessment with all required fields."
    },
    {
      "criterion": "Intent fulfilled",
      "status": "satisfied",
      "notes": "All five criteria evaluated. Coherence rating produced. Recommendation stated."
    },
    {
      "criterion": "Scope compliance",
      "status": "satisfied",
      "notes": "Evaluation covers CS-01 output only. No reference to re-running or modifying."
    }
  ],
  "overall_coherence": "high",
  "flags": [],
  "recommendation": "accept"
}
```

---

### Clone Guide

| Field | What to Change |
|-------|---------------|
| `session_id` | New unique ID |
| `intent` | Replace reference to CS-01 with your target session/output |
| `scope` | Replace CS-01 reference; keep the "does not cover re-running" exclusion |
| `input.content` | The full OutputUnit from your target session |
| `input.scope` | Describe the target output's session and depth |
| `active_modules` | No changes needed — this list is correct for any clarity evaluation |

If the target output is a session output (not a single RTT pass), swap `clarity-val-rtt-output` for `clarity-val-session-output` in both `active_modules` and `validator`.

---

## Library Notes

### Combining Sessions

Canonical sessions are designed to compose. Common combinations:

| Combination | Use Case |
|-------------|---------|
| CS-01 → CS-08 | Run a baseline analysis, then formally evaluate it |
| CS-01 → CS-02 | Run depth=1, then extend to depth=2 if the terminal face warrants it |
| CS-04 → CS-03 | Audit dependencies, then check scope compliance of the starting module |
| CS-05 → CS-03 | Draft a new module, then immediately check its scope compliance |
| CS-07 → CS-01 | Repair a malformed session, then run it correctly |
| CS-06 → CS-08 | Run a multi-lens analysis, then formally evaluate the lens-annotated output |
| CS-04 → CS-05 | Audit a module's dependencies, then fill any gaps found |

Sessions always close before the next one opens. Never run two sessions simultaneously or allow the output of one session to flow directly into another without first closing the producing session and opening a new one with a fresh grammar. The output of Session A becomes the `input` field of Session B — not a live feed.

---

### When to Use Each Session

| Situation | Start Here |
|-----------|-----------|
| You are new and want to see the system working | CS-01 |
| Your first pass did not go deep enough | CS-02 |
| You are about to ratify a new module | CS-03 |
| You are assembling an active_modules list for a complex session | CS-04 |
| The module discovery protocol returned no results | CS-05 |
| The problem has strong time dynamics or stakeholder conflict | CS-06 |
| A session produced unexpected output and you don't know why | CS-07 |
| A prior output was never formally validated | CS-08 |
| A validator returned `revise` and you're not sure what to fix | CS-08, read assessment flags first |
| You inherited a session from another practitioner | CS-07 |

---

### Common Adaptation Errors

These are the most frequent mistakes when cloning a canonical session. Each one maps to a failure mode from Part III Chapter 17.

**Adapting the intent by copy-pasting and finding-and-replacing the module name — without re-reading the actionability and testability tests.**
The original intent passed both tests. Your adapted version may not. After any intent edit, apply the intent field test before proceeding: can you answer "did we achieve the intent?" with a binary yes/no from the output alone?

**Keeping the canonical scope while changing the input.**
The canonical scope is written for the canonical input. If your input is materially different, your scope is wrong — it still names the canonical content boundaries, not yours. Rewrite the scope from scratch for every adapted session.

**Using the canonical active_modules list without re-running the closure check.**
The canonical list is correct for the canonical session. If you have changed the primary modules, the dependency chain has changed. Run the closure check — or use CS-04 as a diagnostic — before initializing.

**Omitting the InputUnit wrapper because the raw input feels self-explanatory.**
It always feels self-explanatory. The scope declaration in the InputUnit is not for the practitioner — it is for the operator. Without it, the operator cannot validate well-formedness. Wrap every input.

**Changing the `output_format` without updating the `validator`.**
The canonical validator is matched to the canonical output format. If you change the format, check the format-validator compatibility matrix in `session-grammar-field-output-format` and update the validator accordingly. A mismatched validator produces `insufficient_input` flags that are difficult to diagnose.

---

### Adding a Session to the Library

When you produce a session that:
- Is structurally complete (all nine fields, all invocations shown, output produced, validator assessment applied)
- Covers a use case not already represented in the library
- Has received a validator `recommendation: accept`

...it is a candidate for inclusion in the library. Submit it as a pull request following the contribution guidelines at [`/docs/contributing`](../contributing). The session will be reviewed against the five canonical session criteria:

| Criterion | What the Reviewer Checks |
|-----------|-------------------------|
| Grammar completeness | All nine fields populated, all field tests pass |
| Execution correctness | All invocations syntactically complete, full signatures shown |
| Output quality | Output meets all five clarity criteria |
| Assessment completeness | ValidatorAssessment present, all criteria evaluated |
| Clone utility | Clone guide present, adaptation errors noted where applicable |

Sessions that pass all five criteria are assigned a canonical ID (`CS-[NN]`) and added to the library index.

---

### Registry Cross-Reference

Every module referenced in this library appears in the [Module Registry](./registry). If a module ID in a session grammar or invocation is unfamiliar, open the registry and locate it by ID in the [Master Alphabetical Index](./registry#master-alphabetical-index). The registry's scope summary will tell you immediately whether the module is what you think it is.

---

→ [Return to Book Index](./index)
→ [Browse the Module Registry](./registry)
→ [Contributing Guidelines](../contributing)

---

*TriadicFrameworks Book — `/docs/book/sessions.md`*
*Authored by Nawder Loswin. AI-augmented authorship. All rights reserved.*
