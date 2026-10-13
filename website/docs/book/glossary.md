# Glossary

> **The authoritative definition of every term in the TriadicFrameworks system.**
> This glossary expands the Quick Reference in the [Book Index](./index).
> Definitions here are precise — not introductory summaries. When a term is used
> in a module, session, or book section, its meaning is exactly what is stated here.

---

## How to Use This Glossary

Terms are organized by domain, not alphabetically, because TriadicFrameworks terms
are deeply interconnected — understanding a term often requires understanding the
terms that surround it. Read a section in order when you are learning a domain.
Jump to the [Master Alphabetical Index](#master-alphabetical-index) when you know
the term and need its definition quickly.

**Cross-references** appear as → *Term* when another glossary entry is directly
relevant. Follow them when a definition depends on another term you have not yet
read.

**Module IDs** appear in backtick code format when a glossary term has a backing
specification in the registry (e.g., `rtt-anchor-definition`). The registry entry
is the authoritative structural specification; this glossary is the human-readable
definition.

---

## Sections

1. [Core System Concepts](#1-core-system-concepts)
2. [The RTT Engine](#2-the-rtt-engine)
3. [Module Architecture](#3-module-architecture)
4. [The Role Enum](#4-the-role-enum)
5. [The Layer Enum](#5-the-layer-enum)
6. [The Session Grammar](#6-the-session-grammar)
7. [Output Formats](#7-output-formats)
8. [The Clarity System](#8-the-clarity-system)
9. [Operator Invocation](#9-operator-invocation)
10. [The Dependency System](#10-the-dependency-system)
11. [Session Failure Modes](#11-session-failure-modes)
12. [Versioning and Module Status](#12-versioning-and-module-status)
13. [Attribution and Authorship](#13-attribution-and-authorship)
14. [Master Alphabetical Index](#master-alphabetical-index)

---

## 1. Core System Concepts

---

**Canon**
The set of five irreversible commitments that define what TriadicFrameworks is, what it does, and who made it. The canon is the outermost boundary of the system — every module, session, and output exists within it, not outside it. The canon is permanent and author-controlled; it cannot be modified through the contribution process. Backing document: [`/docs/book/canon`](./canon).

---

**Canon Commitment**
One of the five individual declarations that together constitute the → *Canon*. Each commitment is backed by a foundational anchor module in the registry and has a precise canonical statement that must be quoted exactly when cited. The five commitments are: RTT Is the Engine, Clarity Is Precision Not Comfort, Modules Are the Unit of Knowledge, Sessions Are the Unit of Application, and Attribution Is Honest.

---

**Clarity**
In TriadicFrameworks, clarity is a structural property of an output — not a psychological property of the person reading it. Formally defined by the → *Nawderian Theorem of Validator Pulses* as a function of → *signal coherence* across → *validator layers*. An output is clear when its signal is high and its coherence is high simultaneously across all layers of evaluation. Comfort, agreement, and familiarity are not evidence of clarity.

---

**Module**
The atomic unit of knowledge in TriadicFrameworks. A module is a structured knowledge unit with a defined → *role*, → *layer*, → *scope*, version, and dependency map. Every module is specified by exactly four files: `module.json`, `module.md`, `module_links.json`, and `module_session.json`. Modules are invoked in sessions; prose documents are not. See → *Four-File Architecture*.

---

**Practitioner**
A person who applies TriadicFrameworks by initializing sessions, invoking operators, and evaluating outputs against the → *Clarity System*. A practitioner has completed Parts I, II, and III of the Book and can answer every item on Part III's exit checklist. The word "practitioner" is used specifically in this system — it is not a synonym for "user" or "reader."

---

**Recursive Triadic Thinking (RTT)**
The governing engine of TriadicFrameworks. `canon-anchor-rtt-engine`. RTT is the structural method by which all system outputs are produced. It holds that any meaningful unit of thought has exactly three structural faces — generative, present, and terminal — and that clarity is produced by parsing all three in sequence, recursively. RTT is not one analytical tool among many; it is the substrate from which the system is built. See → *Section 2* for the full RTT vocabulary.

---

**Registry**
The complete set of all active, draft, deprecated, and archived modules in the TriadicFrameworks system, organized by → *module group*. The registry is the source of truth for which modules exist, what they cover, and how they relate. The human-readable version lives at [`/docs/book/registry`](./registry). The machine-readable version is `modules_group.json` plus the four files of each module.

---

**Session**
The bounded operational container in which every application of TriadicFrameworks takes place. A session is defined by exactly nine fields — the → *Session Grammar* — which must be fully populated before any operator is invoked. Sessions are reproducible: two practitioners running the same session on the same input should produce structurally equivalent outputs. A session that closes before all nine fields have been populated is not a completed session; it is an abandoned one. `canon-anchor-session-unit`.

---

**System**
When used without qualification in TriadicFrameworks documentation, "the system" refers to the complete TriadicFrameworks system: its canon, its module registry, its session grammar, its clarity standard, and the body of canonical sessions and documentation. It does not refer to a software system, a technical platform, or any external tool.

---

## 2. The RTT Engine

---

**Generative Face**
The first of the three structural faces produced by an → *RTT pass*. The generative face answers the question: *Where did this come from?* It identifies the origin, cause, prior state, or input context of the unit of thought being parsed. A generative face that answers only "various factors" or "complex history" is not substantive — it must name specific origins.

---

**Present Face**
The second of the three structural faces. The present face answers the question: *What is this, right now?* It describes the current form, active state, or observable structure of the unit of thought. The present face is the most commonly underspecified — practitioners often write directional analysis that belongs in the terminal face and call it the present state.

---

**Terminal Face**
The third of the three structural faces. The terminal face answers the question: *Where is this going?* It describes the direction, consequence, forward trajectory, or telos of the unit of thought. The terminal face is the most frequently omitted in malformed sessions; its absence is the most common cause of a → *Face Completeness* failure.

---

**RTT Pass**
A single application of RTT to a → *InputUnit*, producing an → *OutputUnit* containing all three structural faces plus a `pass_depth` stamp and a `next_input` for potential recursive extension. A pass is the atomic unit of RTT execution. Multiple passes on the same input constitute → *recursion*.

---

**Pass Depth**
The integer indicating how many RTT passes have been applied to derive a given output. A `pass_depth` of 1 indicates a single pass. A `pass_depth` of 2 indicates the output was produced by running RTT on the `next_input` of a depth=1 pass. Pass depth is recorded in every → *OutputUnit* and evaluated by → *Pass Differentiation* in the clarity criteria.

---

**Recursion**
In RTT, recursion means the → *OutputUnit* of one pass becomes the → *InputUnit* of the next. Each recursive pass must produce at least one claim that is structurally distinct from all prior passes — a claim that could not have been produced without the prior pass's output as input. Recursion that merely restates the prior pass in different language is not recursion; it is repetition. The `rtt-op-recursive-extension` module governs multi-depth recursion.

---

**InputUnit**
The well-formed data structure required as input by any RTT operator. An InputUnit has exactly two required fields: `content` (the raw input text or reference) and `scope` (a precise one-sentence declaration of what the content represents and what it does not). A raw string is not an InputUnit. Wrapping content without declaring its scope is not a valid InputUnit. `input-unit-grammar`.

---

**OutputUnit**
The structured data structure produced by every RTT operator invocation. An OutputUnit has five fields: `generative_face`, `present_face`, `terminal_face`, `pass_depth`, and `next_input`. Every field is required. An output missing any field is an incomplete OutputUnit and cannot be submitted to a validator. `output-unit-grammar`.

---

**Next Input**
The fifth field of an → *OutputUnit*. `next_input` is the current OutputUnit repackaged as an → *InputUnit* for the next RTT pass. It is produced automatically by the RTT operator. Its `content` field is a concise statement of the output's key finding. Its `scope` field is narrowed to the specific structural claim identified in the current pass. A session that declares `depth=1` still produces `next_input` — for potential future extension, not for immediate use.

---

**Three Faces**
Collective shorthand for → *Generative Face*, → *Present Face*, and → *Terminal Face*. All three must be present in every → *OutputUnit*. They are not interchangeable with "past," "present," and "future" — the faces describe structural relationships within any unit of thought, not temporal position.

---

## 3. Module Architecture

---

**Four-File Architecture**
The specification pattern for every module in TriadicFrameworks. Every module is defined by exactly four files: `module.json` (identity manifest), `module.md` (canonical prose content), `module_links.json` (dependency and relationship map), and `module_session.json` (runtime session-context bindings). No file is optional. A module missing any file is an incomplete module and cannot be invoked in a session.

---

**`module.json`**
The identity manifest of a module. Contains: `id`, `label`, `role`, `layer`, `scope`, `version`, `status`, `dependencies`, and `tags`. This is the first file to read when encountering any module. The `scope` field is the contract — the module's prose must not exceed it. All other files are subordinate to this one.

---

**`module.md`**
The human-readable prose content of a module. Written within the boundaries declared by `module.json`'s `scope` field. Contains definitions, explanations, examples, and invocation syntax (for operator-role modules). Read after `module.json` — the manifest constrains the prose, not the reverse.

---

**`module_links.json`**
The dependency and relationship map of a module. Contains: `depends_on`, `required_by`, `related`, `supersedes`, and `superseded_by`. The structural wiring of the module — it defines what the module requires, what requires it, and its version lineage. Read second, after `module.json`, to understand the module's position in the dependency graph before reading its content.

---

**`module_session.json`**
The runtime session-context bindings of a module. Contains: `invocation_syntax`, `input_schema`, `output_schema`, `valid_layers`, `valid_roles`, and `validator_id`. Defines how the module behaves when active in a session. A module without this file can be read but not invoked.

---

**Module ID**
The stable unique identifier of a module. Follows the convention `domain-role_short-descriptor` in kebab-case lowercase. Module IDs do not change across versions. When referencing a module in `active_modules`, `depends_on`, or any other structural field, always use the ID — never the label. `module-id-grammar`.

---

**Module Group**
A named cluster of related modules that share a domain, purpose, or structural region. Defined in `modules_group.json` at the repository root. A module can belong to more than one group. Groups are the primary navigation unit for practitioners who know what domain they are working in but not which specific module applies.

---

**`modules_group.json`**
The file at the repository root that defines all module groups in the system. Each entry declares a group's `id`, `label`, `description`, `layer_affinity`, and `modules` array. The `modules` array is ordered — the order reflects recommended reading sequence for practitioners new to the group.

---

**Scope (module)**
The precise declaration of what a module claims to know, stated in `module.json`'s `scope` field. The scope is a contract: the module's prose must cover everything the scope declares and nothing beyond it. Prose that exceeds the scope is a scope violation. A module whose prose does not reach the scope's full extent has underclaimed. `scope-statement-grammar`.

---

**Scope Statement**
The specific text in `module.json`'s `scope` field. One to three sentences. Must include a coverage declaration (what the module covers) and, where the boundary is non-obvious, an exclusion declaration (what the module does not cover). Must be testable: at any point, a practitioner must be able to check a specific claim against the scope statement and get a binary in/out answer.

---

**Gap**
A module that should exist in the system but does not. Three types: **Type 1** (a missing dependency — a `depends_on` reference that points to a non-existent module), **Type 2** (a missing role/layer intersection — no module covers a needed domain at a specific role and layer), **Type 3** (a navigational gap — the modules exist but no group clusters them for discovery). See → *Apparent Gap* and → *True Gap*.

---

**Apparent Gap**
A gap that appears to exist but does not — because the needed module exists under a different ID, or is in a group that was not checked. Before declaring a gap, a practitioner must exhaust synonym searches and adjacent group browsing. An apparent gap resolved this way is not a gap; it is a discovery path issue.

---

**True Gap**
A gap confirmed after exhausting all apparent-gap checks. A true gap exists when: no existing module has a scope covering the needed content, the content cannot be served by composing two adjacent modules, and the content is within the system's canon. Confirmed true gaps are filled by the `gap-fill-proto` protocol.

---

**Ratification**
The process by which a module's status changes from `draft` to `active`. Ratification requires: minimum 14-day observation period, at least one production session using the module, no open issues, a passing scope compliance check, and a passing dependency audit. Ratification is separate from the PR merge process — a module can be merged as `draft` and ratified later. See the [Contributing Guidelines](../contributing#the-ratification-flow).

---

**Reading Order**
The prescribed sequence for reading a module's four files: `module.json` first, `module_links.json` second, `module.md` third, `module_session.json` fourth. Violating this order is the most common source of module misreading. The manifest constrains the prose; read the constraint before reading what it constrains.

---

## 4. The Role Enum

Every module has exactly one role. The role declares the module's *functional type* — what it does in the system.

---

**`anchor`**
A module that establishes a fixed reference point the rest of the system depends on. Anchors are the closest thing the system has to axioms — they do not derive their validity from other modules; other modules derive their validity from them. The desire to override or extend an anchor is a signal of a misunderstanding of the system's scope, not evidence that the anchor is wrong.
*Examples:* `rtt-anchor-definition`, `session-grammar-anchor`, `nawderian-theorem-validator-pulses`

---

**`lens`**
A module that provides a perspective through which other content is interpreted. A lens does not change the content it is applied to — it changes the angle of view. Multiple lenses may be active in a single session simultaneously. Lenses must not contradict each other at the foundational layer.
*Examples:* `lens-temporal`, `lens-stakeholder`, `clarity-lens-signal-coherence`

---

**`protocol`**
A module that defines a repeatable procedure — a numbered sequence of steps that produces a predictable class of output when followed correctly. Protocols are deterministic in structure even when their inputs vary. Protocols may invoke operators; operators do not invoke protocols.
*Examples:* `session-init-proto`, `module-author-proto`, `gap-fill-proto`

---

**`grammar`**
A module that specifies a structural pattern for language, thought, or output. Grammars define the valid structures within which content may be expressed. A grammar is violated when content appears that has no place in the defined structure.
*Examples:* `session-grammar-spec`, `operator-invocation-grammar`, `input-unit-grammar`

---

**`operator`**
A module that performs a transformation on a defined input to produce a defined output. Operators are the workhorses of the session — every transformation is an operator invocation. Every operator has a full invocation signature in `module_session.json`. A call with missing parameters is malformed.
*Examples:* `rtt-op-core`, `clarity-op-spectral`, `scope-check-op`

---

**`index`**
A module that organizes and surfaces access to a collection of modules. An index maintains a structured registry of a module group or domain with access patterns and cross-references. The book's index page is an index-role artifact.
*Examples:* `index-master-registry`, `index-operator-suite`, `index-by-role`

---

**`map`**
A module that charts the relationships between modules or concepts. Maps provide navigational views of regions of the system — showing how multiple modules relate without performing any transformation or invocation.
*Examples:* `map-session-lifecycle`, `map-dependency-graph`, `map-canon-constraint-model`

---

**`bridge`**
A module that connects two otherwise separate regions of the system. A bridge defines the translation layer between two module clusters whose scopes do not naturally overlap. Bridges are narrow by definition — a bridge claiming a wide scope is misclassified.
*Examples:* `bridge-rtt-to-session`, `bridge-lens-to-rtt`, `bridge-operator-to-validator`

---

**`validator`**
A module that checks outputs or claims against defined criteria. Validators produce → *ValidatorAssessment* objects — structured assessments of which criteria are satisfied, which are not, and which cannot be evaluated with the available information. Validators do not produce verdicts of "good" or "bad."
*Examples:* `clarity-val-rtt-output`, `scope-val`, `session-record-val`

---

**`field`**
A module that holds the specification of a single named parameter of a session or structure. Field modules define a slot's type, valid values, validation rules, and default (if any). The nine session grammar fields are each their own field-role module.
*Examples:* `session-grammar-field-intent`, `session-grammar-field-scope`, `session-grammar-field-validator`

---

## 5. The Layer Enum

Every module has exactly one layer. The layer declares the module's *depth* in the cognitive and operational stack. **The dependency direction rule:** modules may depend on modules at the same or lower layer. A module that depends on a module at a higher layer is structurally malformed.

---

**`surface`**
The highest visible layer; the shallowest structural layer. Holds observable outputs and final-form content — the artifacts, answers, and deliverables that leave the session. Surface modules depend on all layers below them. Nothing within the system depends on them.

---

**`structural`**
The layer of form. Holds patterns, grammars, and relationships — how things are shaped, connected, and organized, independent of specific content. Consumed by surface and operational modules; depends on foundational modules.

---

**`operational`**
The layer of process. Holds protocols, sessions, and runtime behavior — how the system runs, how modules are invoked, how outputs are produced. This is where the system comes to life. Most of Part III operates at this layer.

---

**`foundational`**
The layer of commitment. Holds canon, axioms, and non-negotiable specifications. The layer that cannot be changed without changing the system itself. Every other layer depends on it; it depends on nothing within the system.

---

**`meta`**
The layer of self-reference. Holds content about the system itself — the book, the indexes, the maps, the changelog. The meta layer can reference any other layer. It produces no operational outputs; it is for understanding, not execution.

---

**Dependency Direction Rule**
The structural constraint that modules may depend on modules at the same or lower layer, never on modules at a higher layer. A foundational module that depends on an operational module is malformed. This rule governs the construction of every `depends_on` list in the system.

---

**Role × Layer Position**
The unique position a module occupies in the role × layer space, determined by the combination of its declared role and layer. The position determines what the module can claim, what it can do, what it can depend on, and what can depend on it.

---

## 6. The Session Grammar

The session grammar is the 9-field protocol governing every application of TriadicFrameworks. `session-grammar-anchor`.

---

**Session Grammar**
The complete specification of the nine required fields that must be populated before any session begins. The grammar is the mechanism that makes sessions reproducible — it fixes the variable inputs that would otherwise cause the same practitioner to produce different outputs on the same problem. A session with incomplete grammar is malformed. `session-grammar-spec`.

---

**`session_id`**
Field 1. A unique identifier for a session instance. Must be stable across the session's lifetime. Recommended format: `[domain]-[YYYYMMDD]-[sequence]`. A non-unique session_id makes session retrieval, auditing, and resumption impossible. `session-grammar-field-session-id`.

---

**`intent`**
Field 2. The declared goal of the session — what it will produce, stated precisely. Must be actionable (directed at a deliverable, not a topic) and testable (answerable with a binary yes/no from the output alone). Prohibited phrasing: "explore," "think about," "consider," "look at." Required phrasing: "produce," "evaluate," "specify," "resolve." `session-grammar-field-intent`.

---

**`scope` (session)**
Field 3. The explicit boundary of the session — what is and is not in play. Must be narrower than the intent's natural range. Format: "This session covers [X]. It does not cover [Y]." The scope is the mid-session check instrument: at any point, any action must be checkable against it with a binary in/out result. `session-grammar-field-scope`.

---

**`active_modules`**
Field 4. The complete, dependency-resolved list of modules invoked for this session. Must include every module in every transitive dependency chain of the primary modules. Ordered foundational-to-surface. Uses module IDs, not labels. A list that omits a dependency is not a partial list — it is a malformed one. `session-grammar-field-active-modules`.

---

**`role_context`**
Field 5. The functional type(s) of work being performed in the session. Declares one or more values from the → *Role Enum*. Constrains which modules may be invoked and how outputs are structured. Must be a precise enum value — not a description of the session's activity. `session-grammar-field-role-context`.

---

**`layer_context`**
Field 6. The depth at which the session operates. Declares one or more values from the → *Layer Enum*. Constrains which modules are available. Most sessions operate at a single layer; a session spanning three or more layers is likely conflating multiple sessions. `session-grammar-field-layer-context`.

---

**`input` (session)**
Field 7. The raw material the session works on, wrapped in an → *InputUnit*. Must be the actual input — not a description of it. Must be consistent with the declared scope. A raw string in this field is malformed; it must be an InputUnit with both `content` and `scope` fields populated. `session-grammar-field-input`.

---

**`output_format`**
Field 8. The required shape of the session's deliverable. Declares a value from the → *FormatEnum*. A promise: the session is obligated to produce output that matches this specification exactly. A vague value ("some analysis") is not a valid output format — the validator cannot check against it. `session-grammar-field-output-format`.

---

**`validator` (session)**
Field 9. The module ID of the validator applied to the session's output. Must be present in `active_modules`. Must be compatible with the declared `output_format`. A session without a validator has no correctness criterion — its output cannot be distinguished from noise. `session-grammar-field-validator`.

---

**Session Initialization**
The process of populating all nine session grammar fields and verifying each passes its field-level test before any operator is invoked. Governed by `session-init-proto`. Initialization is complete when all nine fields are non-empty and all nine field tests pass. A session that skips initialization is not a session — it is an unstructured analytical exercise.

---

**Session Closure**
The process of formally ending a session: applying the validator, packaging the output, creating the session record, and archiving. Governed by `session-close-proto`. An output produced before formal closure is a draft. Only closure produces a session output.

---

**Session Resumption**
The process of returning to a session that was closed before its intent was fulfilled. Governed by `session-resume-proto`. Requires retrieving the session record, re-verifying all nine fields (they may have become stale), assessing the output state, and determining the continuation point.

---

**Field Test**
The binary pass/fail test applied to each session grammar field to verify it is correctly populated before the session begins. Each field has its own test (defined in the corresponding field module). A field that fails its test must be corrected before the session proceeds. The field test for `active_modules` is dependency closure verification. The field test for `intent` is the actionability and testability check.

---

**Malformed Session**
A session in which one or more of the nine grammar fields are missing, empty, or incorrectly populated. Malformed sessions produce outputs that cannot be validated, reproduced, or audited. Diagnosing and repairing a malformed session is covered by `CS-07` in the canonical session library.

---

## 7. Output Formats

The FormatEnum defines the valid shapes for session outputs. The declared `output_format` determines which validator applies. `format-enum-anchor`.

---

**`StructuredFaces`**
An output format consisting of three labeled sections corresponding to the three RTT faces: `generative_face`, `present_face`, `terminal_face`. Also includes `pass_depth` and `next_input`. The standard output format for RTT analysis sessions. Validated by `clarity-val-rtt-output`.

---

**`ValidatorAssessment`**
An output format consisting of a structured evaluation: `validator_id`, `session_id`, `pass_depth_evaluated`, `criteria_results` array, `overall_coherence`, `flags` array, and `recommendation`. The standard output format for clarity evaluation sessions. Validated by `clarity-val-session-output`.

---

**`NarrativeAnalysis`**
An output format consisting of bounded prose with declared sections. Used when the deliverable is an analytical document rather than a structured data output. The sections must be declared in the `output_format` field specification — "NarrativeAnalysis" alone is not sufficient; the required sections must be named.

---

**`DependencyTrace`**
An output format consisting of an ordered traversal path: starting module, level-by-level dependency resolution, full resolved dependency set, hidden dependency findings, cycle check result, and minimum `active_modules` list. The standard output format for dependency audit sessions.

---

**`ModuleSpec`**
An output format consisting of one or more of the four module files in valid schema. Used in module authoring and gap-filling sessions. The `output_format` field must specify which files are required (e.g., "ModuleSpec: all four files" or "ModuleSpec: module.json and module_links.json").

---

**`SessionRecord`**
An output format consisting of the complete populated session grammar plus the session's final output and validator assessment. The standard format for session archival. A session record is self-contained — it preserves everything needed to understand, audit, or resume the session.

---

## 8. The Clarity System

---

**Nawderian Theorem of Validator Pulses**
The foundational theorem specifying how clarity is measured in TriadicFrameworks. States: *clarity is a function of signal coherence across validator layers — not a subjective sense of understanding.* The theorem is a foundational anchor and is not open for revision. `nawderian-theorem-validator-pulses`.

---

**Spectral Clarity**
The operationalization of the → *Nawderian Theorem* as an evaluative operator. The Spectral Clarity operator (`clarity-op-spectral`) applies the theorem to an OutputUnit, runs all five → *Clarity Criteria*, and produces a → *ValidatorAssessment*. "Spectral" refers to the multi-layer evaluation structure — clarity is assessed across a spectrum of validator layers simultaneously.

---

**Signal**
In the context of the Nawderian Theorem, signal refers to the information content of an output. Signal is high when the output makes specific, checkable claims. Signal is low when the output makes vague, hedged, or open-ended claims ("various factors," "complex dynamics," "it depends"). High signal is a necessary but not sufficient condition for → *Clarity*.

---

**Coherence**
In the context of the Nawderian Theorem, coherence refers to the internal consistency of an output and its consistency with the session's declared intent and scope. A coherent output does not contradict itself, does not wander outside the scope, and fulfills the declared intent. High coherence is a necessary but not sufficient condition for → *Clarity*.

---

**Signal Coherence**
The combined property of high signal and high coherence, simultaneously, across all → *Validator Layers*. Signal coherence is the measure the Nawderian Theorem uses to define clarity. An output with high signal but low coherence is specific but internally inconsistent. An output with high coherence but low signal is consistent but vague. Only the combination constitutes clarity.

---

**Validator Layer**
One of the structural levels at which → *Signal Coherence* is evaluated in the clarity system. The five clarity criteria each correspond to a distinct validator layer: face-level evaluation (face completeness), claim-level evaluation (face substantiveness), pass-level evaluation (pass differentiation), boundary-level evaluation (scope compliance), and goal-level evaluation (intent fulfillment).

---

**Five Clarity Criteria**
The five structural criteria applied by the → *Spectral Clarity* operator to every output. All five must be evaluated for a → *ValidatorAssessment* to be complete.

| Criterion | What It Checks |
|-----------|---------------|
| **Face Completeness** | All three structural faces are present in every pass |
| **Face Substantiveness** | Each face makes at least one specific, checkable claim |
| **Pass Differentiation** | Each successive pass produces claims structurally distinct from all prior passes |
| **Scope Compliance** | The output contains no references to content outside the session's declared scope |
| **Intent Fulfillment** | The output fulfills the session's declared intent |

---

**Face Completeness**
Clarity Criterion 1. Satisfied when all three structural faces (generative, present, terminal) are present in every pass output. The most commonly failing criterion in beginner sessions — the terminal face is most frequently omitted.

---

**Face Substantiveness**
Clarity Criterion 2. Satisfied when every face makes at least one specific, checkable claim — a claim that can be verified or falsified by consulting evidence, running another pass, or applying a validator. "Various factors" does not satisfy this criterion. "The metric was set upstream without a feedback loop" does.

---

**Pass Differentiation**
Clarity Criterion 3. Satisfied when each successive RTT pass produces at least one claim that is structurally distinct from all prior passes — a claim that could not have been produced without the prior pass's output as input. A pass that restates the prior pass in different language fails this criterion. Not applicable for `pass_depth=1` sessions.

---

**Scope Compliance (clarity criterion)**
Clarity Criterion 4. Satisfied when no claim in the output references content outside the session's declared scope. A single out-of-scope reference is sufficient to fail this criterion. Not to be confused with → *Scope (module)* — this criterion applies to session outputs, not module prose.

---

**Intent Fulfillment**
Clarity Criterion 5. Satisfied when the output fulfills the session's declared intent. An output can be internally coherent and scope-compliant but still fail this criterion if it produces a different deliverable than the intent specified.

---

**`satisfied`**
The positive status of a clarity criterion result. Indicates the criterion is met by the evaluated output. All five criteria must return `satisfied` for a → *ValidatorAssessment* to recommend `accept`.

---

**`not_satisfied`**
The negative status of a clarity criterion result. Indicates the criterion is not met. The → *ValidatorAssessment* `notes` field for this criterion will specify what is missing or incorrect. A `not_satisfied` result produces a `revise` or `re-run` recommendation.

---

**`insufficient_input`**
The indeterminate status of a clarity criterion result. Indicates the validator cannot evaluate the criterion because the output does not provide enough information — not because the criterion is failed, but because it is unevaluable. The practitioner must determine whether the missing information is within scope (revise the output to include it) or outside scope (document and close; evaluate in a follow-on session).

---

**Overall Coherence Rating**
A summary field in the → *ValidatorAssessment* with three possible values: `high`, `moderate`, or `low`. Reflects the validator's holistic assessment of the output's signal coherence across all five criteria. A `high` rating with a `revise` recommendation indicates a specific, isolated criterion failure on an otherwise strong output. A `low` rating with a `re-run` recommendation indicates systemic structural problems.

---

**Flags**
An array field in the → *ValidatorAssessment* that records notable observations that do not constitute criterion failures but warrant practitioner attention. Common flags include near-violations (content approaching but not crossing a boundary), editorial notes (the terminal face is weaker than the other two), and advisory notices (near-hidden dependency detected).

---

**Recommendation**
The concluding field of a → *ValidatorAssessment*. Three possible values:

| Value | Meaning | Practitioner Action |
|-------|---------|-------------------|
| `accept` | Output meets all criteria | Close the session; package the output |
| `revise` | One or more criteria not satisfied; structural work is present | Return to the specific failing pass; revise only the flagged faces |
| `re-run` | Fundamental structural problems throughout | Discard the output; re-examine the session grammar before re-running |

---

## 9. Operator Invocation

---

**Invocation**
The act of calling an operator module with its full parameter signature to perform a transformation. Every invocation must supply all required parameters by name. A call with missing parameters is malformed — not a partial invocation, but a structurally invalid one.

---

**Invocation Syntax**
The exact call signature of an operator, defined in `module_session.json` → `invocation_syntax`. Format: `OperatorNamespace.method(param_name: <Type>, ...)`. Must be read from the module's `module_session.json` before every invocation — never from memory. Signatures change across versions.

---

**OperatorNamespace**
The domain prefix in an operator's invocation syntax. Derived from the operator module's domain segment. Examples: `RTT` for `rtt-op-core`, `Clarity` for `clarity-op-spectral`, `Scope` for `scope-check-op`. The namespace identifies which domain's operator is being called.

---

**Input Schema**
The field in `module_session.json` that defines the valid values and constraints for every parameter in the invocation syntax. A practitioner must verify that their input satisfies the input schema before invoking an operator. Supplying the wrong type (e.g., a raw string where an → *InputUnit* is required) is an input schema violation.

---

**Output Schema**
The field in `module_session.json` that defines the structure of every field in the operator's output. The output schema of one operator must align with the input schema of the next when operators are → *chained*. A downstream module that consumes an operator's output must be designed against that output schema.

---

**Operator Chain**
A sequence of operator invocations where the → *OutputUnit* of one becomes the → *InputUnit* of the next. A chain is valid when: every output schema aligns with the next input schema, all operators are in `active_modules`, and the entire chain stays within the session's declared layer context. Validated by `chain-validate-op`.

---

**Schema Alignment**
The property of an operator chain in which the output schema of every operator correctly feeds the input schema of the next operator in the sequence. A chain with misaligned schemas will produce type errors, missing fields, or structurally invalid inputs at the misalignment point.

---

**Valid Layers / Valid Roles**
The `valid_layers` and `valid_roles` fields in `module_session.json` declare the layer contexts and role contexts in which a module may be invoked. Invoking a module outside its valid contexts is a constraint violation. Always check these fields before invoking an unfamiliar module.

---

## 10. The Dependency System

---

**Dependency**
A structural relationship between two modules in which Module A cannot be validly invoked without Module B being active. Declared in `module_links.json` → `depends_on`. Dependencies are the load-bearing relationships of the module system — they define what the session must include for an invocation to be structurally sound.

---

**Dependency Graph**
The full set of `depends_on` and `required_by` relationships across all modules in the registry. A directed acyclic graph (DAG) — directed because dependencies have direction, acyclic because no module may depend on itself directly or through a chain. `map-dependency-graph`.

---

**Forward Traversal**
The direction of traversal that moves from a higher-layer module toward its foundational anchors — surface to foundational. Used to determine the complete dependency chain that must be included in `active_modules`, and to identify the foundational commitments that support a given output.

---

**Backward Traversal**
The direction of traversal that moves from a foundational anchor toward its surface expressions — foundational to surface. Used to determine the full impact surface of a module before modifying it. Never modify a foundational or structural module without first running a backward traversal.

---

**Impact Surface**
The complete set of modules that depend (directly or transitively) on a given module, determined by backward traversal. A module's impact surface is the set of everything that will be affected if the module changes. Always compute the impact surface before making a MAJOR version increment.

---

**Hidden Dependency**
A dependency that does not appear in `module_links.json` → `depends_on` but functionally exists — because the module's `module.md` prose makes claims that require another module's content to be valid. Hidden dependencies arise from authoring errors. When detected, the correct fix is to add the missing module to `depends_on` — not to work around it.

---

**Dependency Cycle**
A dependency chain in which Module A → Module B → Module C → Module A. Cycles are structural failures — the system cannot resolve the chain because each module requires another to be valid first. Cycles must be broken by converting the weakest dependency link from `depends_on` to `related`.

---

**Dependency Closure**
The property of an `active_modules` list in which every transitive dependency of every declared module is also present in the list. An `active_modules` list is closed when there are no missing transitive dependencies. Closure is verified by running `active-modules-closure-val` or by manually tracing all dependency chains.

---

**`depends_on`**
The field in `module_links.json` that lists all modules this module structurally requires. Must match the `dependencies` field in `module.json` exactly. Every ID in this list must exist in the registry.

---

**`required_by`**
The field in `module_links.json` that lists all modules that declare this module in their `depends_on`. Always empty for new modules. Populated over time as other modules add this one as a dependency. Read this field before modifying any module — it is the backward traversal entry point.

---

**`related`**
The field in `module_links.json` that lists editorial neighbors — modules in adjacent scope that a practitioner might want to read alongside this one. `related` entries are not structural dependencies. A module in `related` is not required for the module to be valid. Do not place structural dependencies in `related` to bypass the closure rule.

---

## 11. Session Failure Modes

The four canonical failure modes are the most frequently occurring session errors. They are canonical because they appear consistently across domains, experience levels, and session types. `map-failure-mode-recovery`.

---

**Failure Mode 1: Underspecified Intent**
Occurs when the `intent` field is populated with a topic or direction rather than a testable deliverable. Symptom: the session produces output, but the practitioner cannot answer "did we achieve the intent?" with a binary yes/no. Root cause: the intent field test was not applied before initialization. Recovery: do not discard the output — apply RTT to it; use the gap between what was produced and what was needed to write a precise intent for a follow-on session.

---

**Failure Mode 2: Scope Creep Mid-Session**
Occurs when a session begins within its declared scope but drifts outside it — typically after a productive first RTT pass reveals an adjacent problem. Symptom: the output addresses multiple problems; the validator flags scope compliance failures. Root cause: the practitioner followed an interesting thread without re-specifying the session's scope. Recovery: stop at the moment creep is detected; decide whether the new content is more valuable than the original scope; close the current session and open a new one if yes, trim to the last in-scope output if no.

---

**Failure Mode 3: Dependency Gap in `active_modules`**
Occurs when one or more modules in `active_modules` have dependencies that were not included in the list. Symptom: operator invocations fail or produce incomplete outputs; the validator returns `insufficient_input` flags that cannot be traced to the input. Root cause: the `active_modules` closure check was not run before initialization. Recovery: run forward traversal on every primary module; add all missing transitive dependencies; re-run from the point of the failed invocation.

---

**Failure Mode 4: Comfort-Filtering Outputs**
Occurs when a practitioner discards a validator-accepted output because it is uncomfortable and re-runs until a more agreeable result appears. Symptom: the session is re-run repeatedly; the accepted output happens to validate prior beliefs. Root cause: violation of → *Canon Commitment II*. Recovery: retrieve the discarded output; apply the validator formally; if it returns `accept`, the output is correct — the discomfort is information, not error. This is the failure mode hardest to detect from the inside and the one that most fundamentally undermines the system's long-term value.

---

## 12. Versioning and Module Status

---

**Version Stamp**
The `version` field in `module.json`. Follows semantic versioning: `MAJOR.MINOR.PATCH`. All new modules begin at `0.1.0`. The first ratification increments to `1.0.0`. The version stamp must be incremented for every change to a module.

---

**PATCH Increment**
A version increment from `x.y.z` to `x.y.(z+1)`. Applied when prose corrections (typos, clarity improvements) are made that do not change the scope, invocation syntax, or dependency list. No downstream impact audit required.

---

**MINOR Increment**
A version increment from `x.y.z` to `x.(y+1).0`. Applied when content is added (new examples, scope clarifications, additional `related` entries) without changing the structural specification. No downstream impact audit required.

---

**MAJOR Increment**
A version increment from `x.y.z` to `(x+1).0.0`. Applied when the structural contract changes: scope changes, role or layer changes, dependency additions or removals, invocation syntax changes, output schema changes. A MAJOR increment requires a downstream impact audit — every module in the `required_by` list must be checked for compatibility.

---

**`draft`**
Module status assigned to all new modules on creation. A draft module is in the repository and usable, but practitioners should treat it as experimental. Draft modules use `0.x.x` versioning. Ratification changes `draft` to `active`.

---

**`active`**
Module status assigned to a module that has passed ratification. An active module is production-ready. Its structural contract is considered stable. Use `active` modules in production sessions without reservation.

---

**`deprecated`**
Module status assigned to a module that has been superseded by a newer module. A deprecated module still exists in the registry and may still be invoked, but practitioners should migrate to the superseding module. The `superseded_by` field in `module_links.json` identifies the replacement.

---

**`archived`**
Module status assigned to a module that has been fully retired and should not be invoked. Archived modules are preserved in the registry for historical reference and dependency auditing of older session records. They do not appear in active module discovery workflows.

---

## 13. Attribution and Authorship

---

**Nawder Loswin**
The pen name of the human author of TriadicFrameworks. Derived from the phrase "one who wanders inward." A deliberate creative identity, fully owned and consistently maintained. Not a pseudonym for concealment — a chosen authorial identity for this body of work. All canon commitments, module scopes, and foundational design decisions are attributed to this intelligence.

---

**AI-Augmented Authorship**
The authorship model of TriadicFrameworks. The human author (Nawder Loswin) directed the creative and analytical process. AI was used as a precision instrument — extending the author's capability without substituting for the author's judgment. The AI made no foundational decisions. Every canon commitment, every module scope, every design choice is the product of human authorial intent. `canon-anchor-attribution`.

---

**Pen Name**
See → *Nawder Loswin*. The pen name is the public-facing authorial identity for this work. It is how the author is cited in module attribution fields, book footers, and contribution records.

---

## Master Alphabetical Index

| Term | Section |
|------|---------|
| `active` (status) | [12](#12-versioning-and-module-status) |
| `active_modules` (field) | [6](#6-the-session-grammar) |
| AI-Augmented Authorship | [13](#13-attribution-and-authorship) |
| Anchor (role) | [4](#4-the-role-enum) |
| Apparent Gap | [3](#3-module-architecture) |
| `archived` (status) | [12](#12-versioning-and-module-status) |
| Backward Traversal | [10](#10-the-dependency-system) |
| Bridge (role) | [4](#4-the-role-enum) |
| Canon | [1](#1-core-system-concepts) |
| Canon Commitment | [1](#1-core-system-concepts) |
| Clarity | [1](#1-core-system-concepts) |
| Coherence | [8](#8-the-clarity-system) |
| `depends_on` | [10](#10-the-dependency-system) |
| `deprecated` (status) | [12](#12-versioning-and-module-status) |
| Dependency | [10](#10-the-dependency-system) |
| Dependency Closure | [10](#10-the-dependency-system) |
| Dependency Cycle | [10](#10-the-dependency-system) |
| Dependency Direction Rule | [5](#5-the-layer-enum) |
| Dependency Graph | [10](#10-the-dependency-system) |
| `DependencyTrace` (format) | [7](#7-output-formats) |
| `draft` (status) | [12](#12-versioning-and-module-status) |
| Face Completeness | [8](#8-the-clarity-system) |
| Face Substantiveness | [8](#8-the-clarity-system) |
| Field (role) | [4](#4-the-role-enum) |
| Field Test | [6](#6-the-session-grammar) |
| Five Clarity Criteria | [8](#8-the-clarity-system) |
| `flags` | [8](#8-the-clarity-system) |
| FormatEnum | [7](#7-output-formats) |
| Forward Traversal | [10](#10-the-dependency-system) |
| Four-File Architecture | [3](#3-module-architecture) |
| `foundational` (layer) | [5](#5-the-layer-enum) |
| Gap | [3](#3-module-architecture) |
| Generative Face | [2](#2-the-rtt-engine) |
| Grammar (role) | [4](#4-the-role-enum) |
| Hidden Dependency | [10](#10-the-dependency-system) |
| Impact Surface | [10](#10-the-dependency-system) |
| Index (role) | [4](#4-the-role-enum) |
| Input Schema | [9](#9-operator-invocation) |
| `input` (session field) | [6](#6-the-session-grammar) |
| InputUnit | [2](#2-the-rtt-engine) |
| `insufficient_input` | [8](#8-the-clarity-system) |
| Intent Fulfillment | [8](#8-the-clarity-system) |
| `intent` (session field) | [6](#6-the-session-grammar) |
| Invocation | [9](#9-operator-invocation) |
| Invocation Syntax | [9](#9-operator-invocation) |
| `layer_context` (field) | [6](#6-the-session-grammar) |
| Lens (role) | [4](#4-the-role-enum) |
| MAJOR Increment | [12](#12-versioning-and-module-status) |
| Malformed Session | [6](#6-the-session-grammar) |
| Map (role) | [4](#4-the-role-enum) |
| `meta` (layer) | [5](#5-the-layer-enum) |
| MINOR Increment | [12](#12-versioning-and-module-status) |
| Module | [1](#1-core-system-concepts) |
| Module Group | [3](#3-module-architecture) |
| Module ID | [3](#3-module-architecture) |
| `module.json` | [3](#3-module-architecture) |
| `module.md` | [3](#3-module-architecture) |
| `module_links.json` | [3](#3-module-architecture) |
| `module_session.json` | [3](#3-module-architecture) |
| `ModuleSpec` (format) | [7](#7-output-formats) |
| `modules_group.json` | [3](#3-module-architecture) |
| `NarrativeAnalysis` (format) | [7](#7-output-formats) |
| Nawderian Theorem of Validator Pulses | [8](#8-the-clarity-system) |
| Nawder Loswin | [13](#13-attribution-and-authorship) |
| Next Input | [2](#2-the-rtt-engine) |
| `not_satisfied` | [8](#8-the-clarity-system) |
| `operational` (layer) | [5](#5-the-layer-enum) |
| Operator (role) | [4](#4-the-role-enum) |
| Operator Chain | [9](#9-operator-invocation) |
| OperatorNamespace | [9](#9-operator-invocation) |
| Output Schema | [9](#9-operator-invocation) |
| `output_format` (field) | [6](#6-the-session-grammar) |
| OutputUnit | [2](#2-the-rtt-engine) |
| Overall Coherence Rating | [8](#8-the-clarity-system) |
| Pass Depth | [2](#2-the-rtt-engine) |
| Pass Differentiation | [8](#8-the-clarity-system) |
| PATCH Increment | [12](#12-versioning-and-module-status) |
| Pen Name | [13](#13-attribution-and-authorship) |
| Practitioner | [1](#1-core-system-concepts) |
| Present Face | [2](#2-the-rtt-engine) |
| Protocol (role) | [4](#4-the-role-enum) |
| Ratification | [3](#3-module-architecture) |
| Reading Order | [3](#3-module-architecture) |
| Recommendation | [8](#8-the-clarity-system) |
| Recursion | [2](#2-the-rtt-engine) |
| Recursive Triadic Thinking (RTT) | [1](#1-core-system-concepts) |
| Registry | [1](#1-core-system-concepts) |
| `related` | [10](#10-the-dependency-system) |
| `required_by` | [10](#10-the-dependency-system) |
| Role × Layer Position | [5](#5-the-layer-enum) |
| `role_context` (field) | [6](#6-the-session-grammar) |
| RTT Pass | [2](#2-the-rtt-engine) |
| `satisfied` | [8](#8-the-clarity-system) |
| Schema Alignment | [9](#9-operator-invocation) |
| Scope (module) | [3](#3-module-architecture) |
| Scope Compliance (clarity criterion) | [8](#8-the-clarity-system) |
| `scope` (session field) | [6](#6-the-session-grammar) |
| Scope Statement | [3](#3-module-architecture) |
| Session | [1](#1-core-system-concepts) |
| Session Closure | [6](#6-the-session-grammar) |
| Session Failure Mode 1: Underspecified Intent | [11](#11-session-failure-modes) |
| Session Failure Mode 2: Scope Creep | [11](#11-session-failure-modes) |
| Session Failure Mode 3: Dependency Gap | [11](#11-session-failure-modes) |
| Session Failure Mode 4: Comfort-Filtering | [11](#11-session-failure-modes) |
| Session Grammar | [6](#6-the-session-grammar) |
| Session Initialization | [6](#6-the-session-grammar) |
| `SessionRecord` (format) | [7](#7-output-formats) |
| Session Resumption | [6](#6-the-session-grammar) |
| `session_id` (field) | [6](#6-the-session-grammar) |
| Signal | [8](#8-the-clarity-system) |
| Signal Coherence | [8](#8-the-clarity-system) |
| Spectral Clarity | [8](#8-the-clarity-system) |
| `StructuredFaces` (format) | [7](#7-output-formats) |
| `structural` (layer) | [5](#5-the-layer-enum) |
| `surface` (layer) | [5](#5-the-layer-enum) |
| System | [1](#1-core-system-concepts) |
| Terminal Face | [2](#2-the-rtt-engine) |
| Three Faces | [2](#2-the-rtt-engine) |
| True Gap | [3](#3-module-architecture) |
| `valid_layers` / `valid_roles` | [9](#9-operator-invocation) |
| `ValidatorAssessment` (format) | [7](#7-output-formats) |
| Validator (role) | [4](#4-the-role-enum) |
| `validator` (session field) | [6](#6-the-session-grammar) |
| Validator Layer | [8](#8-the-clarity-system) |
| Version Stamp | [12](#12-versioning-and-module-status) |

---

→ [Return to Book Index](./index)
→ [Module Registry](./registry)
→ [Canon](./canon)

---

*TriadicFrameworks Book — `/docs/book/glossary.md`*
*Authored by Nawder Loswin. AI-augmented authorship. All rights reserved.*
