# Part III — Apply

> **Who this is for:** Practitioners who have completed Parts I and II and can answer every item on Part II's exit checklist.
> **What it requires:** Part I fluency. Part II navigation skill. A willingness to work through the examples hands-on, not just read them.
> **What it produces:** The ability to run live sessions — populating the grammar correctly, invoking operators with full syntax, evaluating outputs against the Spectral Clarity model, and recovering from the four canonical failure modes.

---

Part III is where the system becomes useful.

Parts I and II were preparation. This part is execution. Every chapter is built around doing something — not understanding a concept in isolation, but applying it to real input and producing a real output. The examples in this part are designed to be followed step by step, not skimmed. If you skim them, you will think you understand more than you do. The failure modes in Chapter 17 exist specifically because practitioners skimmed.

There are five chapters. They follow a natural operational sequence: initialize the session, invoke the operators, run the passes, evaluate the output, and recover when something goes wrong.

---

## Chapters

- [Chapter 13 — Populating the 9-Field Session Grammar](#chapter-13--populating-the-9-field-session-grammar)
- [Chapter 14 — Operator Invocation: Full Signature Syntax](#chapter-14--operator-invocation-full-signature-syntax)
- [Chapter 15 — Running a Complete RTT Pass on Novel Input](#chapter-15--running-a-complete-rtt-pass-on-novel-input)
- [Chapter 16 — Applying Spectral Clarity and the Nawderian Theorem](#chapter-16--applying-spectral-clarity-and-the-nawderian-theorem)
- [Chapter 17 — The Four Canonical Session Failure Modes](#chapter-17--the-four-canonical-session-failure-modes)
- [Exit Checklist — You Can Apply When...](#exit-checklist--you-can-apply-when)

---

## Chapter 13 — Populating the 9-Field Session Grammar

A session begins with grammar. Not with the problem. Not with the input. Not with the modules. With the grammar — the nine fields that define everything the session is and is not allowed to do.

A session with incomplete grammar is not a session running without some optional scaffolding. It is a malformed session. Outputs from malformed sessions cannot be validated, audited, or reproduced. They may be useful by accident. They are never useful by design.

This chapter walks through each of the nine fields in order, specifying the population rules, the valid values, the common errors, and the test you can apply to verify the field is correctly set before proceeding.

---

### The Session Grammar Template

Every session begins with this structure, populated before any operator is invoked:

```json
{
  "session_id": "",
  "intent": "",
  "scope": "",
  "active_modules": [],
  "role_context": "",
  "layer_context": "",
  "input": "",
  "output_format": "",
  "validator": ""
}
```

Do not begin operator invocations until all nine fields are non-empty and have passed their field-level tests.

---

### Field 1: `session_id`

**What it holds:** A unique identifier for this session instance.

**Population rules:**
- Must be unique across all sessions in the practitioner's history.
- Must be stable — do not change it once the session has begun.
- Recommended format: `[domain]-[date]-[sequence]` — e.g., `clarity-eval-20260925-01`
- The date should be the date the session is initialized, in `YYYYMMDD` format.
- The sequence number disambiguates multiple sessions initialized on the same date.

**Common error:** Using a vague or non-unique ID like `session-1` or `test`. These collide across time. When you need to audit or resume a session, a non-unique ID makes retrieval impossible.

**Field test:** Can you locate this session by its ID alone, with no other context, six months from now? If not, the ID is insufficient.

---

### Field 2: `intent`

**What it holds:** The declared goal — what this session is for, stated precisely.

**Population rules:**
- One to three sentences. No more.
- Must be actionable — it should specify what the session will *produce*, not what it will *think about*.
- Must be testable — at the end of the session, you must be able to answer "did we achieve the intent?" with a yes or no.
- Do not use hedged language ("explore," "consider," "look at"). Use directed language ("produce," "evaluate," "specify," "resolve").

**Examples:**

| Weak (do not use) | Strong (use this) |
|-------------------|-------------------|
| Explore what RTT means for decision-making | Produce a single-pass RTT analysis of a named decision, identifying all three structural faces and packaging the output as a valid next-pass input |
| Think about the clarity of the draft output | Evaluate the draft output against the Spectral Clarity model and produce a structured validator assessment stating which criteria are satisfied and which are not |
| Work on the new module | Author the complete four-file specification for the `scope-check-operator` module, including manifest, links, prose, and session bindings |

**Common error:** Writing the intent as a topic rather than a deliverable. "Understand RTT" is a topic. "Produce a two-pass RTT analysis of the onboarding problem with depth=2 and output_format=StructuredFaces" is a deliverable.

**Field test:** Remove the intent and show someone the session's final output. Can they reconstruct the intent from the output alone? If yes, the intent was precise. If not, it was underspecified.

---

### Field 3: `scope`

**What it holds:** The explicit boundary — what is and is not in play for this session.

**Population rules:**
- State both what is included and what is excluded.
- The scope must be narrower than the intent's natural range. Every intent has implicit scope creep potential — the scope field closes it off before the session begins.
- Use the format: *"This session covers [X]. It does not cover [Y]."*
- Scope statements should be short enough to check against at any moment during the session.

**Examples:**

> This session covers the evaluation of the draft `rtt-operator-core` module's `module.md` for scope compliance against its `module.json` manifest. It does not cover the module's dependency chain, its session bindings, or its compatibility with other operator modules.

> This session covers a single-depth RTT pass on the input statement provided in Field 7. It does not cover recursive extension beyond depth=1, application to adjacent inputs, or evaluation of the output's implications.

**Common error:** Leaving the scope field as a restatement of the intent. The scope narrows the intent. If `scope` and `intent` say the same thing, the scope has not been set — it has been paraphrased.

**Field test:** At any point during the session, you should be able to check any action against the scope and get a binary answer: *is this within scope?* If the scope is so vague that the answer is usually "probably," the scope needs tightening.

---

### Field 4: `active_modules`

**What it holds:** The complete, dependency-resolved list of modules invoked for this session.

**Population rules:**
- Use the four-stage module discovery protocol from Chapter 10 to identify the primary modules.
- Trace the full dependency chain for each primary module (Chapter 8, forward traversal).
- Include every module in every dependency chain. The `active_modules` list is the complete closure of all module dependencies for the session.
- Order the list from foundational to surface — anchors first, operators last.
- Use module IDs, not labels.

**Common error:** Including only the top-level modules and omitting their dependencies. This creates invisible dependency gaps — the session will invoke modules that require other modules to be valid, but those supporting modules are not active. The session's outputs cannot be properly validated.

**Field test:** For every module in the list, open its `module_links.json`. Every module in its `depends_on` list must also appear in `active_modules`. If any do not, the list is incomplete.

---

### Field 5: `role_context`

**What it holds:** The role(s) in operation during this session — the functional types of work being performed.

**Population rules:**
- Declare the primary role this session is performing. Use the Role enum exactly.
- If the session spans multiple functional types (e.g., both evaluating and transforming), list all roles that apply.
- Most sessions have one or two primary roles. A session with five or more declared roles is likely conflating multiple sessions into one — consider splitting.

**Valid values:** `anchor`, `lens`, `protocol`, `grammar`, `operator`, `index`, `map`, `bridge`, `validator`, `field`

**Common error:** Leaving this field at a vague meta-description ("thinking," "working," "analyzing") rather than a value from the Role enum. The role_context field exists to constrain which modules may be invoked and how outputs are structured — a vague value provides no constraint.

**Field test:** Does every module in `active_modules` have a `valid_roles` entry in its `module_session.json` that includes at least one of the declared role_context values? If not, a module is being invoked outside its valid role context.

---

### Field 6: `layer_context`

**What it holds:** The analyzer layer(s) the session operates within.

**Population rules:**
- Declare the primary layer. Use the Layer enum exactly.
- Most sessions operate at a single layer. If a session genuinely spans two layers (e.g., both `structural` and `operational`), both may be declared — but examine whether the session should be split.
- The layer_context constrains which modules may be invoked. A module with `valid_layers: ["operational"]` cannot be invoked in a `foundational` layer context.

**Valid values:** `surface`, `structural`, `operational`, `foundational`, `meta`

**Common error:** Defaulting to `operational` for every session without considering whether the work is actually at the structural or foundational layer. A session authoring a new grammar module is structural, not operational. The distinction matters — it affects which validators apply and which modules are available.

**Field test:** Does every module in `active_modules` have a `valid_layers` entry that includes the declared `layer_context`? If not, the layer context or the module list is wrong.

---

### Field 7: `input`

**What it holds:** The raw material the session works on.

**Population rules:**
- The input must be a well-formed `InputUnit` — a thought, claim, decision, artifact, or document with a declared scope.
- If the input is text, include the full text — do not summarize it. The session works on the actual input, not a description of it.
- If the input is a module, include the module ID and specify which file(s) are in scope.
- The input must be consistent with the declared scope in Field 3. If the input exceeds the scope, reduce the input to the in-scope portion before populating this field.

**Common error:** Populating this field with a description of the input rather than the input itself. "A draft of the module" is not an input. The draft module's actual content is the input.

**Field test:** Could the session be handed to a different practitioner — with only the nine fields and no additional context — and produce the same class of output? If the `input` field requires implicit knowledge to interpret, it is underspecified.

---

### Field 8: `output_format`

**What it holds:** The required shape of the session's deliverable.

**Population rules:**
- Declare the format precisely. Use the FormatEnum values where applicable.
- If the output is a structured document, specify the document's sections.
- If the output is a validator assessment, specify which validator fields must be present.
- If the output is a module, specify which of the four files are required.
- The output format is a promise — the session is obligated to produce output that matches this specification exactly.

**FormatEnum core values:**

| Value | Output Shape |
|-------|-------------|
| `StructuredFaces` | Three labeled sections: generative_face, present_face, terminal_face |
| `ValidatorAssessment` | Criteria list with satisfied/unsatisfied/insufficient-input status per criterion |
| `ModuleSpec` | One or more of the four module files in valid schema |
| `NarrativeAnalysis` | Prose analysis with declared sections, bounded to scope |
| `DependencyTrace` | Ordered list of module IDs from source to foundational anchor |
| `SessionRecord` | Complete populated session grammar plus output |

**Common error:** Leaving this field vague ("a write-up," "some notes," "analysis"). A vague output format means the validator cannot check whether the output meets the session's intent. The output becomes a judgment call rather than a checkable deliverable.

**Field test:** Given only the `output_format` value, could you tell whether a sample output passes or fails? If not, the format is not specific enough.

---

### Field 9: `validator`

**What it holds:** The module ID of the validator applied to the session's output.

**Population rules:**
- Use a module ID from the `validator-suite` or `clarity-system` group.
- The validator must be present in `active_modules`.
- The validator must be appropriate for the declared `output_format` — a validator designed for RTT pass outputs should not be applied to a module spec deliverable.
- If no existing validator covers the session's output type, this is a gap — address it before running the session, or document the absence explicitly.

**Common error:** Leaving this field as `"none"` or `"TBD"`. A session without a validator has no correctness criterion. Its output cannot be distinguished from noise. This is not a minor omission — it defeats the purpose of the session grammar.

**Field test:** Can you read the declared validator's `module.json` scope and confirm it covers the output format declared in Field 8? If not, the validator is mismatched.

---

### A Fully Populated Example Session

```json
{
  "session_id": "rtt-analysis-20260925-01",
  "intent": "Produce a depth=2 RTT analysis of the input statement, identifying all three structural faces at both pass levels and packaging the second-pass output as a valid InputUnit for a potential third pass.",
  "scope": "This session covers a two-pass RTT analysis of the single input statement in Field 7. It does not cover application to related statements, recursive extension beyond depth=2, or evaluation of the output's downstream implications.",
  "active_modules": [
    "rtt-anchor-definition",
    "session-grammar-anchor",
    "session-grammar-field-input",
    "session-grammar-field-output-format",
    "session-grammar-field-validator",
    "rtt-operator-core",
    "rtt-operator-recursive-extension",
    "clarity-validator-rtt-output"
  ],
  "role_context": "operator",
  "layer_context": "operational",
  "input": "Our team's decision-making process produces inconsistent outcomes. Sometimes we converge quickly on the right answer; other times we cycle through the same options without resolution. The pattern is not correlated with decision difficulty or team composition.",
  "output_format": "StructuredFaces",
  "validator": "clarity-validator-rtt-output"
}
```

This session is fully specified. Every field is populated, precise, and internally consistent. The `active_modules` list includes all declared dependencies. The `validator` is present in the module list. The `output_format` and `validator` are compatible. The `scope` narrows the `intent`. The `input` is the actual input, not a description of it.

This session can be handed to any practitioner and produce structurally equivalent output.

---

## Chapter 14 — Operator Invocation: Full Signature Syntax

Operators are the workhorses of the session. Every transformation you perform on an input is the result of an operator invocation. This chapter covers how to read an operator's invocation syntax, how to construct a valid call, and the errors that make a call malformed.

### The Invocation Grammar

Every operator invocation follows this structure:

```
[OperatorNamespace].[method](
  [param_name]: <value>,
  [param_name]: <value>,
  ...
)
```

- **OperatorNamespace** — the domain prefix of the operator module (e.g., `RTT`, `Clarity`, `Scope`, `Session`)
- **method** — the specific operation being performed (e.g., `pass`, `evaluate`, `check`, `initialize`)
- **param_name: value** — every parameter declared in `module_session.json` → `invocation_syntax`, in order

All parameters are required unless explicitly marked `optional` in the `input_schema`. There are no positional defaults — every parameter must be named explicitly.

### Reading the Syntax from `module_session.json`

Before invoking any operator, open its `module_session.json` and read three fields:

1. **`invocation_syntax`** — the exact call signature, with parameter names and type placeholders
2. **`input_schema`** — the valid values and constraints for each parameter
3. **`output_schema`** — what you will receive, which determines how you handle the result

Never invoke an operator from memory. Always read the `module_session.json` freshly. Version changes alter signatures.

### Worked Invocations

#### Invocation 1: RTT Core Operator

**`module_session.json` → `invocation_syntax`:**
```
RTT.pass(input: <InputUnit>, depth: <integer>, output_format: <FormatEnum>)
```

**`input_schema`:**
- `input`: A well-formed InputUnit with a declared scope
- `depth`: Integer ≥ 1. Number of recursive passes. Default: 1
- `output_format`: A value from FormatEnum. Specifies the output structure

**Valid invocation:**
```
RTT.pass(
  input: {
    content: "Our team's decision-making process produces inconsistent outcomes...",
    scope: "Single decision-making pattern statement — no adjacent statements in scope"
  },
  depth: 2,
  output_format: StructuredFaces
)
```

**Malformed invocation (missing parameter):**
```
RTT.pass(
  input: "Our team's decision-making process produces inconsistent outcomes...",
  depth: 2
)
```
> Missing `output_format`. This is a malformed call. The operator does not know how to structure its output. Do not attempt to infer the output format from context — stop and complete the call.

**Malformed invocation (wrong input type):**
```
RTT.pass(
  input: "Our team's decision-making process produces inconsistent outcomes...",
  depth: 2,
  output_format: StructuredFaces
)
```
> The `input` is a raw string, not an `InputUnit`. An `InputUnit` requires a `content` field and a `scope` field. A raw string has no declared scope — the operator cannot validate that the input is well-formed.

---

#### Invocation 2: Spectral Clarity Operator

**`module_session.json` → `invocation_syntax`:**
```
Clarity.evaluate(
  input: <OutputUnit>,
  theorem_ref: <TheoremID>,
  validator_id: <ValidatorModuleID>,
  output_format: <FormatEnum>
)
```

**`input_schema`:**
- `input`: A completed OutputUnit — the result of a prior operator invocation, with all declared output_schema fields present
- `theorem_ref`: The ID of the Nawderian Theorem module to apply. Standard value: `nawderian-theorem-validator-pulses`
- `validator_id`: The validator module to use for assessment. Must match the output type
- `output_format`: Must be `ValidatorAssessment` for clarity evaluations

**Valid invocation:**
```
Clarity.evaluate(
  input: {
    generative_face: "The inconsistency originates in...",
    present_face: "A reproducibility failure exists because...",
    terminal_face: "Without intervention, the pattern will compound because...",
    pass_depth: 1,
    next_input: { content: "...", scope: "..." }
  },
  theorem_ref: "nawderian-theorem-validator-pulses",
  validator_id: "clarity-validator-rtt-output",
  output_format: ValidatorAssessment
)
```

---

#### Invocation 3: Scope Check Operator

**`module_session.json` → `invocation_syntax`:**
```
Scope.check(
  module_id: <ModuleID>,
  target_file: <FileEnum>,
  manifest_ref: <ModuleID>
)
```

**`input_schema`:**
- `module_id`: The ID of the module being checked
- `target_file`: Which file to check against the manifest scope. Values: `module.md`, `module_session.json`
- `manifest_ref`: The module ID whose `module.json` scope field serves as the boundary. Usually the same as `module_id`, unless checking a linked module

**Valid invocation:**
```
Scope.check(
  module_id: "rtt-operator-core",
  target_file: module.md,
  manifest_ref: "rtt-operator-core"
)
```

---

### Chaining Invocations

Operators may be chained — the output of one invocation becomes the input of the next. Chaining is valid when:

1. The output schema of the first operator matches the input schema of the second.
2. Both operators are in `active_modules`.
3. The chain stays within the session's declared scope.

**Valid chain:**
```
Step 1:
RTT.pass(input: <InputUnit>, depth: 1, output_format: StructuredFaces)
→ produces: OutputUnit { generative_face, present_face, terminal_face, pass_depth, next_input }

Step 2:
Clarity.evaluate(
  input: <OutputUnit from Step 1>,
  theorem_ref: "nawderian-theorem-validator-pulses",
  validator_id: "clarity-validator-rtt-output",
  output_format: ValidatorAssessment
)
→ produces: ValidatorAssessment { criteria_results[], overall_coherence, flags[] }
```

This is the canonical two-step pattern for any session that both transforms an input and evaluates the result. Use it as the default unless the session's intent specifies otherwise.

### The Non-Negotiable Rules of Invocation

1. **Never invoke without reading `module_session.json` first.** Memory is not a valid substitute.
2. **Never omit a required parameter.** There is no such thing as a "partial invocation." A call with missing parameters is malformed.
3. **Never pass a raw string where an `InputUnit` is required.** Wrap it properly.
4. **Never chain operators whose schemas are incompatible.** Verify output_schema → input_schema alignment before chaining.
5. **Never invoke an operator outside its `valid_layers` or `valid_roles`.** Check these constraints before every invocation.

---

## Chapter 15 — Running a Complete RTT Pass on Novel Input

This chapter is a full end-to-end execution. It begins with a raw problem statement and ends with a validated two-pass RTT output. Follow it step by step.

### The Input

> *"We are three months into a new product initiative. The team is executing well on individual tasks, but the initiative as a whole feels directionless. Stakeholders are starting to ask questions we don't have answers to. The PM is confident but cannot articulate what success looks like beyond the next sprint."*

### Step 1: Prepare the InputUnit

Wrap the raw input in an `InputUnit` by declaring its scope:

```json
{
  "content": "We are three months into a new product initiative. The team is executing well on individual tasks, but the initiative as a whole feels directionless. Stakeholders are starting to ask questions we don't have answers to. The PM is confident but cannot articulate what success looks like beyond the next sprint.",
  "scope": "A single product initiative's current state as described by a team member — no adjacent initiatives, no historical context, no organizational context beyond what is stated."
}
```

The scope declaration is not optional. It tells the RTT operator exactly what the input claims to represent and what it does not. Without it, the operator cannot know whether a given face is drawing inside or outside the input's legitimate bounds.

### Step 2: Initialize the Session

```json
{
  "session_id": "rtt-product-initiative-20260925-01",
  "intent": "Produce a depth=2 RTT analysis of the product initiative input, identifying structural failure at both the surface and meta levels, and packaging the second-pass output as a valid InputUnit for intervention planning.",
  "scope": "This session covers a two-pass RTT analysis of the single input statement. It does not cover team dynamics, stakeholder management strategy, or PM performance evaluation.",
  "active_modules": [
    "rtt-anchor-definition",
    "session-grammar-anchor",
    "session-grammar-field-input",
    "session-grammar-field-output-format",
    "session-grammar-field-validator",
    "rtt-operator-core",
    "rtt-operator-recursive-extension",
    "clarity-validator-rtt-output"
  ],
  "role_context": "operator",
  "layer_context": "operational",
  "input": "<InputUnit from Step 1>",
  "output_format": "StructuredFaces",
  "validator": "clarity-validator-rtt-output"
}
```

All nine fields populated. Session initialized.

### Step 3: First RTT Pass (depth=1)

**Invocation:**
```
RTT.pass(
  input: <InputUnit>,
  depth: 1,
  output_format: StructuredFaces
)
```

**Execution — filling the three faces:**

**Generative face — where did this come from?**

The initiative began with energy and individual competence — the team executes well on tasks. The origin context is one where local execution was prioritized over systemic coherence. At the time of launch, success was likely defined in terms of task delivery rather than initiative-level outcomes. The PM's confidence is real but is anchored to a task-delivery frame, not an outcomes frame. This mismatch between the launch framing (task-oriented) and the current expectation (stakeholder-facing outcomes) is the generative source of the problem.

**Present face — what is this, right now?**

A coherence gap between micro-execution and macro-orientation. The team is operationally capable but strategically unmoored. The specific structural failure: the initiative has no declared success definition at the initiative level — only at the sprint level. Sprint-level success can be high while initiative-level direction is undefined. This is not a morale problem, a talent problem, or a stakeholder management problem. It is a missing artifact problem: the initiative-level success specification does not exist.

**Terminal face — where is this going?**

Without intervention, two convergent failure paths:
1. Stakeholder confidence erodes as questions go unanswered, leading to reduced sponsorship or increased scrutiny that slows execution.
2. The PM's sprint-level confidence persists while initiative-level drift accelerates, creating a growing gap between reported progress and actual strategic alignment.

Both paths terminate in initiative failure or redefinition — not from poor execution, but from undefined direction.

**First-pass output:**

```json
{
  "generative_face": "The initiative was launched with a task-delivery frame. The PM's confidence and the team's execution capability are both anchored to sprint-level success definitions. No initiative-level success specification was established at launch.",
  "present_face": "A missing artifact: the initiative-level success specification. The gap between sprint-level execution (strong) and initiative-level orientation (absent) is the structural failure. This is not a performance problem — it is a specification problem.",
  "terminal_face": "Two convergent failure paths: stakeholder confidence erosion and accelerating strategic drift, both leading to initiative failure or forced redefinition.",
  "pass_depth": 1,
  "next_input": {
    "content": "The initiative lacks an initiative-level success specification. Sprint-level success is well-defined and being achieved. The absence of the higher-level specification is creating stakeholder misalignment and strategic drift.",
    "scope": "The structural gap identified in the first RTT pass — scoped to the specification deficit, not to team performance or stakeholder management."
  }
}
```

### Step 4: Second RTT Pass (depth=2)

**Invocation:**
```
RTT.pass(
  input: <next_input from first-pass output>,
  depth: 2,
  output_format: StructuredFaces
)
```

**Execution:**

**Generative face — where did this specification deficit come from?**

Initiative-level success specifications are not authored because most teams do not have a grammar for them. Sprint-level success is easy to specify — stories, points, acceptance criteria. Initiative-level success requires a different kind of specification: one that declares what the world looks like when the initiative has succeeded, measured at a level above any individual sprint's deliverables. Without a grammar for this artifact, it is not authored — not because teams forget, but because they do not have the structural tools to do it.

**Present face — what is the specification deficit, at a deeper level?**

The deficit is not just the absence of one document. It is the absence of a specification *practice* at the initiative level. The team knows how to specify sprint outputs because they do it every sprint. They do not know how to specify initiative outcomes because they have never been taught the grammar for it. The PM's inability to articulate what success looks like is not a failure of insight — it is the absence of a structural tool.

**Terminal face — what does filling this deficit enable?**

An initiative-level success specification, once authored, immediately resolves the stakeholder question problem — stakeholders can now be given a clear, testable answer. It also gives the PM a frame for evaluating whether sprint work is initiative-aligned (not just sprint-complete). The drift problem becomes diagnosable: is this sprint's output moving toward the success definition or away from it?

**Second-pass output:**

```json
{
  "generative_face": "Teams lack a grammar for initiative-level success specification. Sprint-level grammar exists and is practiced. Initiative-level grammar does not — so the artifact is never authored.",
  "present_face": "The deficit is structural: the team does not have the tool to specify what they need to specify. The PM's uncertainty is not a knowledge failure — it is a grammar failure.",
  "terminal_face": "Authoring an initiative-level success specification resolves stakeholder misalignment, gives the PM an alignment frame, and makes drift diagnosable at the sprint level.",
  "pass_depth": 2,
  "next_input": {
    "content": "The team needs an initiative-level success specification grammar — a structural tool that enables them to define what success looks like above the sprint level.",
    "scope": "The grammar-level intervention required to resolve the initiative's specification deficit — scoped to the tool itself, not to its implementation or adoption."
  }
}
```

Notice what the second pass produced that the first could not: the identification that the problem is a *grammar failure*, not a specification failure. The first pass said "the artifact is missing." The second pass said "the artifact is missing because the grammar for authoring it does not exist in this team's practice." These are different problems with different interventions. The second pass found the right level.

### Step 5: Apply the Validator

```
Clarity.evaluate(
  input: <second-pass OutputUnit>,
  theorem_ref: "nawderian-theorem-validator-pulses",
  validator_id: "clarity-validator-rtt-output",
  output_format: ValidatorAssessment
)
```

See Chapter 16 for the full validator assessment process.

---

## Chapter 16 — Applying Spectral Clarity and the Nawderian Theorem

Producing output is not the end of a session. Evaluating the output against the system's clarity standard is. This chapter covers the Nawderian Theorem of Validator Pulses, how to apply the Spectral Clarity operator, how to read a validator assessment, and how to act on it.

### The Nawderian Theorem of Validator Pulses

The theorem makes a single foundational claim:

> **Clarity is a function of signal coherence across validator layers — not a subjective sense of understanding.**

Unpacked:

- **Signal** — the information content of the output. A signal is high when the output makes specific, checkable claims. It is low when the output makes vague, hedged, or open-ended claims.
- **Coherence** — the degree to which the output's claims are internally consistent and consistent with the session's declared intent and scope. A coherent output does not contradict itself and does not wander outside the scope.
- **Validator layers** — clarity is not evaluated once. It is evaluated at multiple structural layers: the face level (is each face present and substantive?), the pass level (does the second pass build on the first, not repeat it?), the scope level (does the output stay within the session's declared scope?), and the intent level (does the output fulfill the declared intent?).

An output is **clear** when its signal is high and its coherence is high across all validator layers. An output can feel clear — readable, confident, well-written — while failing on coherence. And an output can feel dense or technical while scoring high on all four validator layers. The feeling is irrelevant. The measurement is what counts.

### The Validator Assessment Structure

Every `clarity-validator-rtt-output` assessment produces a `ValidatorAssessment` with this structure:

```json
{
  "validator_id": "clarity-validator-rtt-output",
  "session_id": "<session being evaluated>",
  "pass_depth_evaluated": <integer>,
  "criteria_results": [
    {
      "criterion": "Face completeness",
      "status": "satisfied | not_satisfied | insufficient_input",
      "notes": "..."
    },
    {
      "criterion": "Face substantiveness",
      "status": "satisfied | not_satisfied | insufficient_input",
      "notes": "..."
    },
    {
      "criterion": "Pass differentiation",
      "status": "satisfied | not_satisfied | insufficient_input",
      "notes": "..."
    },
    {
      "criterion": "Scope compliance",
      "status": "satisfied | not_satisfied | insufficient_input",
      "notes": "..."
    },
    {
      "criterion": "Intent fulfillment",
      "status": "satisfied | not_satisfied | insufficient_input",
      "notes": "..."
    }
  ],
  "overall_coherence": "high | moderate | low",
  "flags": [],
  "recommendation": "accept | revise | re-run"
}
```

### The Five Clarity Criteria

**Criterion 1: Face completeness.**
Are all three structural faces present in every pass output? A pass output with a missing face is incomplete — the terminal face is the most commonly omitted. *Satisfied* means all three faces are present in all passes evaluated.

**Criterion 2: Face substantiveness.**
Does each face contain a specific, checkable claim — or is it vague? A generative face that says "this came from various factors" is not substantive. A generative face that names the specific structural origin is substantive. *Satisfied* means every face makes at least one specific, checkable claim.

**Criterion 3: Pass differentiation.**
Does each successive pass produce claims that could not have been produced by the previous pass? If Pass 2 largely restates Pass 1 in different words, the recursion is not doing its work. *Satisfied* means each pass produces at least one claim that is structurally distinct from all prior passes.

**Criterion 4: Scope compliance.**
Does the output stay within the scope declared in Field 3? Any claim that references content outside the declared scope is a scope violation. *Satisfied* means no scope violations are detected.

**Criterion 5: Intent fulfillment.**
Does the output fulfill the intent declared in Field 2? An output can be internally coherent and scope-compliant but still fail to produce what the intent specified. *Satisfied* means the output can be checked against the intent and passes.

### Reading a Validator Assessment: The Chapter 15 Example

Applying the validator to the two-pass output from Chapter 15:

```json
{
  "validator_id": "clarity-validator-rtt-output",
  "session_id": "rtt-product-initiative-20260925-01",
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
      "notes": "Each face makes specific, checkable claims. Pass 1 present face names the missing artifact precisely. Pass 2 present face identifies the grammar failure specifically."
    },
    {
      "criterion": "Pass differentiation",
      "status": "satisfied",
      "notes": "Pass 2 produces the grammar-failure claim, which is structurally distinct from Pass 1's artifact-absence claim. The level of analysis deepened."
    },
    {
      "criterion": "Scope compliance",
      "status": "satisfied",
      "notes": "No references to team dynamics, PM performance, or stakeholder management strategy detected. Output stayed within declared scope."
    },
    {
      "criterion": "Intent fulfillment",
      "status": "satisfied",
      "notes": "The second-pass next_input is packaged as a valid InputUnit for intervention planning, as the intent specified."
    }
  ],
  "overall_coherence": "high",
  "flags": [],
  "recommendation": "accept"
}
```

All five criteria satisfied. Overall coherence: high. Recommendation: accept.

### Acting on a Validator Assessment

| Recommendation | What It Means | What to Do |
|---------------|---------------|-----------|
| `accept` | The output meets all criteria at the evaluated depth | Close the session. Package the output per `output_format`. |
| `revise` | One or more criteria are `not_satisfied` but the structural work is present | Return to the specific failing pass and revise only the faces flagged in `criteria_results`. Do not re-run the entire session. |
| `re-run` | The output has fundamental structural problems — missing faces, no pass differentiation, or scope violations throughout | Discard the output. Re-examine the session grammar fields (especially `intent`, `scope`, and `input`) before re-running. |

**The critical rule:** Never act on an output before receiving a validator assessment. An unvalidated output is not a session output — it is a draft. Only a `ValidatorAssessment` with `recommendation: accept` produces a session output.

### When a Criterion Returns `insufficient_input`

`insufficient_input` means the validator cannot evaluate the criterion because the output does not provide enough information to check against. This is distinct from `not_satisfied` — it is not a failure, it is a structural gap.

When a criterion returns `insufficient_input`:
1. Read the `notes` field for the specific criterion. It will state what additional information is required.
2. Determine whether the missing information is within the session's scope.
3. If yes — revise the output to include it. The information should have been there.
4. If no — the criterion is genuinely unevaluable within this session's scope. Document this in the session record and close. The criterion will need to be evaluated in a follow-on session with a wider scope.

---

## Chapter 17 — The Four Canonical Session Failure Modes

Every practitioner encounters these four failure modes. They are canonical because they appear consistently, across domains, across experience levels, and across session types. Knowing them in advance does not prevent them — but it makes them recoverable when they occur.

---

### Failure Mode 1: Underspecified Intent

**What it looks like:**

The session produces output, but the output does not feel like it answered the right question. The practitioner cannot determine whether the session succeeded or failed. When asked "did you achieve the intent?" the answer is "I think so?" or "mostly."

**Root cause:**

The `intent` field was populated with a topic or a direction rather than a deliverable. The session had no testable success criterion, so it wandered within the intent's implicit space and produced output that is adjacent to what was needed — but not exactly it.

**How to detect it in advance:**

Apply the intent field test from Chapter 13: can you answer "did we achieve the intent?" with a binary yes or no, using only the session's output? If not, the intent is underspecified. Do not start the session.

**Recovery procedure:**

1. Do not discard the output. Read it carefully — it likely contains valuable material.
2. Apply RTT to the output itself: what did the session actually produce (present face)? What was the original need (terminal face of the session's intent)?
3. Use the gap between present face and terminal face to write a precise intent for a follow-on session.
4. Initialize the follow-on session with the revised intent and use the current output as part of the input.

**The trap:** Re-running the same session with the same underspecified intent. The output will be different but equally unfocused. Fix the intent before re-running.

---

### Failure Mode 2: Scope Creep Mid-Session

**What it looks like:**

The session begins within its declared scope, but at some point — often after a productive first RTT pass — the practitioner begins pulling in adjacent content, related problems, or interesting tangents. By the end, the output addresses two or three problems instead of one. The validator flags scope violations. The output cannot be cleanly accepted.

**Root cause:**

The first RTT pass often reveals adjacent problems that are genuinely interesting and important. The practitioner, energized by the insight, follows the adjacent thread without re-specifying the session's scope. The session scope has drifted, but the grammar fields were not updated to reflect the drift.

**How to detect it in advance:**

At every point during session execution, check any action against Field 3: *is this within scope?* If you find yourself writing content about a topic not named in the scope, stop. You have left the session.

**Recovery procedure:**

1. Stop execution immediately when scope creep is detected.
2. Identify the point at which the output left the declared scope.
3. Decide: is the new content more valuable than the original scope?
   - **If yes:** Close the current session. Open a new session with a scope that covers the new content. Use the current output's in-scope portion as context.
   - **If no:** Discard everything after the scope departure point. Return to the last in-scope output and continue from there.
4. Never attempt to retroactively widen the scope to cover content already produced. Scope is declared before execution, not adjusted to fit the output.

**The trap:** Widening the scope retroactively ("well, it's all related anyway"). This defeats the purpose of the scope field. A scope that expands to fit the output provides no constraint.

---

### Failure Mode 3: Dependency Gap in `active_modules`

**What it looks like:**

An operator invocation fails or produces structurally incomplete output. The validator flags criteria as `insufficient_input` for reasons that cannot be traced to the input itself. The session feels like it is working but the outputs do not cohere.

**Root cause:**

One or more modules in `active_modules` have dependencies that were not included in the list. The operator was invoked, but the modules it depends on were not active. The system is operating with missing structural support — like invoking a function whose required libraries are not imported.

**How to detect it in advance:**

Apply the `active_modules` field test from Chapter 13: for every module in the list, open its `module_links.json` and verify every module in its `depends_on` list also appears in `active_modules`. Do this before initializing the session.

**Recovery procedure:**

1. Run a forward traversal (Chapter 8) on every module in `active_modules`.
2. Identify all dependency IDs that are missing from the list.
3. Add all missing modules to `active_modules`.
4. Re-run the session from the point of the failed invocation — not from the beginning, unless the gap affected earlier steps.
5. If the validator produced `insufficient_input` flags, re-evaluate against the updated module set.

**The trap:** Attempting to infer the missing module's behavior from context and continuing anyway. A dependency gap is a structural error. Workarounds produce structurally unsound outputs.

---

### Failure Mode 4: Comfort-Filtering Outputs

**What it looks like:**

The session produces a valid, well-structured output — but it is uncomfortable. The generative face names an origin the practitioner would prefer not to acknowledge. The present face identifies a failure the practitioner is implicated in. The terminal face describes a future that requires difficult action. The practitioner discards the output and re-runs the session, adjusting the input or the passes until the output is more palatable.

**Root cause:**

The practitioner is using the system as a mirror rather than as a precision instrument. They are filtering outputs by comfort rather than by the validator's assessment. This is the violation of Canon Commitment 2 in operational form.

**How to detect it in advance:**

Ask yourself, before closing a session: *am I accepting this output because the validator assessed it as `accept`, or because I like what it says?* These two reasons should be the same. When they are not, you are comfort-filtering.

**Recovery procedure:**

1. Retrieve the discarded output. Read it again.
2. Apply the validator — formally, with a full invocation — to the discarded output.
3. If the validator returns `accept`, the output is correct. Your discomfort is information — it is telling you something true that you were not ready to hear. Accept the output.
4. If the validator returns `revise` or `re-run`, revise or re-run — but based on the specific criteria that failed, not on the overall comfort level of the result.
5. Never use comfort as a selection criterion between two validator-accepted outputs. If both pass, both are correct — they are different valid analyses of the same input, not a correct answer and a wrong answer.

**The trap:** Running the session repeatedly until a comfortable output appears, then accepting that one. This is not iteration — it is selection bias. The comfortable output is not more correct than the uncomfortable one. It is simply more comfortable.

**The deeper issue:** Comfort-filtering is the failure mode that most directly undermines the system's long-term value. A practitioner who comfort-filters consistently will produce a body of work that validates their existing beliefs — which is exactly what the system was designed to prevent. If you find yourself comfort-filtering often, apply RTT to the pattern itself: where does it come from, what is it now, and where is it going?

---

### Failure Mode Summary

| Failure Mode | Detectable In Advance | Recovery Entry Point |
|-------------|----------------------|---------------------|
| Underspecified intent | Yes — intent field test | Revise intent; use current output as input context |
| Scope creep mid-session | Yes — scope check at each action | Close; new session; or trim to last in-scope output |
| Dependency gap | Yes — `active_modules` field test | Forward traversal; add missing modules; re-run from failure point |
| Comfort-filtering | Partially — requires self-awareness | Retrieve discarded output; validate formally; accept if `accept` |

All four failure modes are preventable through disciplined grammar population and honest validator application. The practitioners who encounter them least are the ones who apply the field tests from Chapter 13 without exception — every session, every time.

---

## Exit Checklist — You Can Apply When...

Before considering yourself a practitioner of TriadicFrameworks, verify you can answer every item below without referring back to this document.

**On the Session Grammar:**
- [ ] You can populate all nine fields correctly for a novel intent without consulting a template.
- [ ] You can apply the field test for each of the nine fields and determine pass/fail independently.
- [ ] You can identify an underspecified intent from the `intent` field alone, before the session runs.
- [ ] You can construct a complete, dependency-resolved `active_modules` list using the discovery protocol and forward traversal.

**On Operator Invocation:**
- [ ] You can read a `module_session.json` and construct a valid invocation from its `invocation_syntax` field.
- [ ] You can identify a malformed invocation (missing parameter, wrong input type, incompatible chain) and state the specific error.
- [ ] You can chain two operators correctly, verifying output_schema → input_schema alignment before chaining.
- [ ] You know all five non-negotiable rules of invocation.

**On Running RTT Passes:**
- [ ] You can prepare a well-formed `InputUnit` from a raw input, including a declared scope.
- [ ] You can execute a first-pass RTT analysis on a novel input, producing all three faces with substantive, checkable claims.
- [ ] You can execute a second-pass RTT analysis on the first pass's `next_input`, producing claims that could not have been produced at depth=1.
- [ ] You can package a pass output as a valid `next_input` for a subsequent pass.

**On Spectral Clarity:**
- [ ] You can state the Nawderian Theorem in one sentence.
- [ ] You can name and define all five clarity criteria.
- [ ] You can read a `ValidatorAssessment` and determine the correct next action (accept, revise, or re-run).
- [ ] You know what `insufficient_input` means and how to respond to it.
- [ ] You can invoke `Clarity.evaluate()` with a full, valid signature.

**On Failure Modes:**
- [ ] You can name all four canonical session failure modes.
- [ ] You can identify which failure mode is occurring from a session's symptoms alone.
- [ ] You can apply the recovery procedure for each failure mode.
- [ ] You can distinguish comfort-filtering from legitimate output revision.
- [ ] You can detect scope creep at the moment it occurs — not retroactively.

---

**If every box is checked, you are a practitioner.**

The system is now available to you in full. Parts I, II, and III together constitute the minimum complete orientation. Everything beyond this point — the full module registry, the canonical example session library, the module authoring guides, the group-level deep dives — builds on what you have read here.

The work begins now.

→ [Return to Book Index](./index)
→ [Browse the Module Registry](./registry)
→ [Explore the Canonical Session Library](./sessions)

---

*TriadicFrameworks Book — `/docs/book/part-iii.md`*
*Authored by Nawder Loswin. AI-augmented authorship. All rights reserved.*
