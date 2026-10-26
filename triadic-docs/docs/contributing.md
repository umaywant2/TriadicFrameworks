# 💞 Contributing to TriadicFrameworks

> **This document governs all contributions to the TriadicFrameworks repository.**
>
> Read it in full before opening a pull request. There are no exceptions to the standards here, not for experience level, not for urgency, not for the size of the change.

---

## Before You Contribute

TriadicFrameworks is a precision system. Its value depends entirely on the structural integrity of its modules, the coherence of its canon, and the correctness of its session grammar. A contribution that is well-intentioned but structurally incorrect is not a partial improvement. It is a source of invisible errors that propagate through the dependency graph and corrupt downstream sessions.

This document is not a formality. It is a set of standards that protect the system's integrity. Every section exists because a class of errors was identified that these standards prevent.

Read Part II of the Book (Navigate) before contributing modules. Read Part III (Apply) before contributing sessions. If you have not read both, your contribution is not ready.

---

## Contents

- [What You Can Contribute](#what-you-can-contribute)
- [What You Cannot Contribute](#what-you-cannot-contribute)
- [The PR Process](#the-pr-process)
- [Module Authoring Standards](#module-authoring-standards)
- [The Ratification Flow](#the-ratification-flow)
- [Session Library Contributions](#session-library-contributions)
- [Book Contributions](#book-contributions)
- [Versioning Standards](#versioning-standards)
- [Review Criteria](#review-criteria)
- [Contribution Principles](#contribution-principles)

---

## What You Can Contribute

Contributions fall into five categories. Each has its own standards and review path.

| Category | Examples | Review Path |
|----------|----------|-------------|
| **New module** | A missing operator, validator, grammar, lens, or map module | Full ratification flow |
| **Module revision** | Corrections, scope clarifications, prose improvements, dependency additions | Version increment + reviewer sign-off |
| **New canonical session** | A fully worked session covering a use case not in the library | Session review checklist |
| **Book contribution** | Corrections, clarifications, worked examples, cross-reference additions | Editorial review |
| **Registry update** | Group creation, group membership change, index update | Structural review |

Each category is detailed in its own section below.

---

## What You Cannot Contribute

The following are not open for contribution. No PR that touches these will be merged.

**The five canon commitments.**

The canon is irreversible. A PR that attempts to add, remove, modify, or reframe any of the five canon commitments will be closed without review. If you believe a canon commitment is wrong, that is a conversation to have with the author, not a pull request.

**The Role or Layer enums.**

Adding, removing, or redefining roles or layers changes the position of every module in the system. These enums are author-controlled. PRs touching `role-enum-anchor` or `layer-enum-anchor` will be closed without review.

**The Nawderian Theorem.**

`nawderian-theorem-validator-pulses` is a foundational anchor authored by Nawder Loswin. Its content is not open for revision. PRs touching this module will be closed without review.

**The session grammar field count or order.**

The nine fields are specified in `session-grammar-anchor`. Adding, removing, or reordering fields changes every session in the system. This is author-controlled. PRs touching the field list or ordering will be closed without review.

**Attribution.**

The honest attribution standard is canonical. Do not modify any attribution field, author credit, or AI-authorship disclosure in any file.

> If you are uncertain whether your contribution touches a non-contributable area, open an issue and ask before writing any code or prose.

---

## The PR Process

Every contribution follows this sequence. No step may be skipped.

### Step 1: Open an Issue First

Before writing anything, open an issue describing:

- **What** you want to contribute: module, session, book edit, or registry change
- **Why** it is needed: gap identification, error correction, or coverage expansion
- **Which existing modules** your contribution depends on or affects

This step exists to catch two things early:

1. **Apparent gaps**: your contribution may already exist under a different ID. A reviewer will search the registry and confirm.
2. **Scope conflicts**: your proposed module may overlap with an existing module's scope in ways you did not see. A reviewer will flag this before you write four files.

Issues are lightweight. A few sentences plus the expected role, layer, and scope statement is enough to start the conversation. Do not spend significant effort on the contribution before the issue is reviewed.

**Exception:** Book contributions such as typo fixes, broken link corrections, and factual corrections may be submitted as a PR without a prior issue. All other contributions require an issue first.

### Step 2: Branch

Create a branch from `main` following this naming convention:

`[type]/[short-descriptor]`

| Type prefix | Use for |
|-------------|---------|
| `module/` | New module or module revision |
| `session/` | New canonical session |
| `book/` | Book documentation change |
| `registry/` | Registry or group change |
| `fix/` | Error correction in any file |

Examples:

- `module/usage-metric-grammar`
- `session/cs-09-multi-module-conflict-detection`
- `book/part-ii-chapter-8-cycle-detection-example`
- `fix/rtt-op-core-scope-near-violation`

### Step 3: Write

Follow the authoring standards for your contribution type detailed in the sections below. Write the content. Do not submit until the content is complete. Partial PRs are not accepted.

### Step 4: Self-Review

Before opening the PR, apply this self-review checklist.

**For modules:**

- [ ] All four files are present and non-empty
- [ ] `module.json` scope statement is one to three sentences, precisely bounded
- [ ] `module.md` prose does not exceed the declared scope
- [ ] `module_links.json` `depends_on` list is complete and closure-verified
- [ ] `module_session.json` invocation syntax is complete and all parameters are named
- [ ] Module ID follows the `domain-role_short-descriptor` convention
- [ ] Version is `0.1.0`
- [ ] Status is `draft`
- [ ] The scope-check operator has been applied and returned compliant or near-compliant

**For sessions:**

- [ ] All nine grammar fields are populated
- [ ] All field-level tests pass
- [ ] All invocations show full signatures
- [ ] Output is complete and in the declared format
- [ ] ValidatorAssessment is present and returns `recommendation: accept`
- [ ] Clone guide is present

**For book contributions:**

- [ ] No content contradicts an existing module's declared scope
- [ ] No content contradicts the canon commitments
- [ ] Cross-references use module IDs, not labels
- [ ] Version stamps are not modified

### Step 5: Open the PR

PR title format:

`[TYPE] Short description`

Examples:

- `[MODULE] Add usage-metric-grammar to grammar-suite`
- `[SESSION] Add CS-09: Multi-Module Conflict Detection`
- `[BOOK] Correct dependency traversal example in Part II Chapter 8`
- `[FIX] Resolve scope near-violation in rtt-op-core module.md`

PR description must include:

1. **Link to the originating issue**
2. **Summary of changes**: what files were added or modified
3. **Self-review checklist**: completed
4. **Dependency impact statement**: which existing modules, if any, are affected by this change and how
5. **Scope compliance statement**: one sentence confirming the new content stays within its declared scope

PRs without all five elements will be returned for revision before review begins.

### Step 6: Review

A reviewer will be assigned within five business days. Reviews evaluate against the criteria in the [Review Criteria](#review-criteria) section below.

Reviewers may:

- **Approve**: contribution meets all standards and is ready to merge
- **Request changes**: specific issues identified and must be addressed before re-review
- **Close**: contribution touches a non-contributable area, or the gap is apparent rather than real

All reviewer feedback is structural, not stylistic. If a reviewer asks for a change, it is because a standard is not met, not because of personal preference.

### Step 7: Ratification (modules only)

New modules require ratification before their status changes from `draft` to `active`. See [The Ratification Flow](#the-ratification-flow) for the complete procedure.

Non-module contributions such as sessions, book edits, and registry updates do not require ratification. They merge on reviewer approval.

### Step 8: Merge and Registry Update

On merge:

- The module is added to `modules_group.json` in its assigned group or groups
- The master registry index is updated
- The registry version stamp is incremented per the `version-increment-proto`
- The book changelog is updated

Registry and changelog updates are handled by the maintainer. Contributors do not need to manage these.

---

## Module Authoring Standards

This section is the complete specification for what a valid module contribution looks like. Every requirement here corresponds to a structural rule in the system. None are stylistic preferences.

### The Four Anchoring Decisions

Before writing a single line of content, make and commit to these four decisions. Write them down. They are your contract with the system.

**Decision 1: Role**

Choose exactly one value from the Role enum. If you cannot choose without ambiguity, the module's purpose is not yet clear. Clarify the purpose. Do not proceed.

**Decision 2: Layer**

Choose exactly one value from the Layer enum. Apply the dependency direction rule: your module will depend on modules at this layer and below. Confirm this constraint works for the content you need to express before proceeding.

**Decision 3: Scope**

Write the scope statement. One to three sentences. State what the module covers. State what it does not cover if the boundary is non-obvious. The scope statement is a promise. The module's prose must not exceed it. Write the scope before writing any prose.

**Decision 4: Dependencies**

List every module whose content must be valid for your module's content to be meaningful. Verify each dependency exists in the registry. If a dependency does not exist, you have found a nested gap. Fill it first.

### `module.json` Requirements

A valid `module.json` must contain:

- `id`: follows the `domain-role_short-descriptor` convention
- `label`: human-readable, title case
- `role`: exactly one value from the Role enum
- `layer`: exactly one value from the Layer enum
- `scope`: one to three sentences, precisely bounded
- `version`: `0.1.0` for all new modules
- `status`: `draft` for all new modules
- `dependencies`: may be an empty array
- `tags`: optional lowercase relevant keywords

**ID naming convention:** `domain-role_short-descriptor`

Role short forms:

| Role | Short Form |
|------|------------|
| `anchor` | `anch` |
| `lens` | `lens` |
| `protocol` | `proto` |
| `grammar` | `gram` |
| `operator` | `op` |
| `index` | `idx` |
| `map` | `map` |
| `bridge` | `bridge` |
| `validator` | `val` |
| `field` | `field` |

Valid ID examples:

- `usage-metric-gram`
- `intervention-lens`
- `module-conflict-val`

Invalid ID examples:

- `UsageMetricGrammar`: not kebab-case
- `grammar-usage-metric`: role before domain
- `usage_metric_grammar`: underscores instead of hyphens
- `ugram`: too abbreviated to be meaningful

### `module_links.json` Requirements

Required fields:

- `id`: must match `module.json` ID exactly
- `depends_on`: same list as `module.json` dependencies
- `required_by`: empty array for all new modules
- `related`: optional editorial neighbors
- `supersedes`: empty array if not replacing an existing module
- `superseded_by`: `null` for all new modules

**The closure rule:** Every module ID in `depends_on` must exist in the registry. If it does not exist, the contribution is blocked until the dependency is authored and merged.

**The `required_by` rule:** New modules always have an empty `required_by`. This field is populated when existing modules are updated to declare a dependency on the new module. Do not pre-populate it.

**The `related` rule:** `related` is editorial, not structural. A module in `related` is not required for the module to be valid. It is a suggested companion for practitioners. Do not put a structural dependency in `related` to avoid the closure rule.

### `module.md` Requirements

`module.md` is the human-readable face of the module. It must be written *within* the scope declared in `module.json`, not up to the edge of the scope and not beyond it.

**Required sections for all modules:**

1. **Definition**: what this module is, in plain language
2. **Scope statement**: the verbatim scope from `module.json`, set off in a blockquote
3. **Content**: the module's substantive content, organized by role type
4. **Constraints**: what this module does not cover and what it must not be used for

**Role-specific content requirements:**

| Role | Required content |
|------|------------------|
| `anchor` | Commitment, non-negotiability, and what breaks if violated |
| `lens` | What it foregrounds, what it does not change, activation, combination rules |
| `protocol` | Numbered sequence, triggers, completion gate, failure handling |
| `grammar` | Structure, field types, validation rules, minimum valid form, worked example |
| `operator` | Invocation syntax, parameters, output structure, worked example |
| `index` | What is indexed, organization, navigation |
| `map` | What is charted, relationships, reading instructions, limitations |
| `bridge` | Connected regions, translation layer, valid input/output types |
| `validator` | Validation target, criteria, assessment interpretation, recommendations |
| `field` | Field name, type, valid values, validation rules, default, field test |

**Prose standards:**

- Write in second person for practitioner-facing content and third person for system-facing content
- Do not use hedging language in scope-claiming sections
- Cross-reference modules using module IDs, not labels
- Examples must be complete worked examples
- Maximum one editorial cross-reference per section

### `module_session.json` Requirements

Required fields:

- `id`: must match `module.json` ID exactly
- `invocation_syntax`: uses `OperatorNamespace.method(param: Type, ...)` form
- `input_schema`: describes valid values and constraints for each parameter
- `output_schema`: names and describes each output field
- `valid_layers`: at least one Layer enum value
- `valid_roles`: at least one Role enum value
- `validator_id`: a valid validator module ID from the registry

**Invocation syntax rules:**

- OperatorNamespace derives from the module's domain
- Method name is a verb describing the transformation
- Every parameter in the syntax appears in `input_schema`
- Parameters are named, not positional
- Optional parameters are marked `optional:` in their description

**Validator ID rule:** `validator_id` must reference an existing validator module. If no suitable validator exists, this is a nested gap. File the nested gap as a separate issue. In the interim, `manifest-complete-val` may serve as a structural placeholder if the PR includes a linked issue for the missing validator.

---

## The Ratification Flow

Ratification is the process by which a module's status changes from `draft` to `active`. It is separate from the PR review process. A PR can be merged with a module in `draft` status, and ratification happens afterward.

### Why Ratification Is Separate

Merging a draft module adds it to the repository. Ratifying a module declares it fit for production use. These are different events.

A draft module may be merged to:

- Unblock a dependency chain
- Begin the ratification clock
- Allow integration testing before production status

A draft module in the registry is visible and usable, but practitioners should treat it as experimental. Sessions using draft modules should note this in their session records.

### Ratification Criteria

A module is ready for ratification when all of the following are true:

**1. Minimum observation period elapsed.**

The module has been in `draft` status for at least 14 days.

**2. At least one production session completed.**

At least one session using the module has run to completion, received `recommendation: accept` from its validator, and been submitted to the session library or documented in the issue thread.

**3. No open issues against the module.**

All issues tagged with the module's ID have been resolved.

**4. Scope compliance confirmed.**

`Scope.check` has been applied to `module.md` against `module.json` and returned `COMPLIANT`, or any near-violation has been resolved and checked again.

**5. Dependency chain audit passed.**

The dependency-audit protocol `CS-04` has been run and returned no hidden dependencies and no cycles.

### Ratification Request

When all five criteria are met, open a ratification request issue containing:

- Module ID and current version
- Link to the original PR
- Link to the production session record or inline session summary
- Scope compliance check result
- Dependency audit result

On approval:

1. `module.json` status changes from `draft` to `active`
2. Version changes from `0.x.x` to `1.0.0`
3. `module_links.json` `required_by` is updated
4. The registry version stamp increments
5. The book changelog is updated

### Fast-Track Ratification

Modules that fill a hard gap, meaning a missing dependency that blocks an existing active module, are eligible for fast-track ratification.

Fast-track reduces the minimum observation period to seven days and waives the production session requirement. A diagnostic session using the gap-fill protocol may substitute. All other criteria apply.

Include `[FAST-TRACK]` in the ratification request issue title and link to the blocked module's dependency audit output confirming the hard gap.

---

## Session Library Contributions

A new canonical session must meet all five criteria before it will be added to the library.

### Criterion 1: Grammar Completeness

All nine session grammar fields are populated. Each field passes its field-level test. The `active_modules` list is dependency-closed. Run `CS-04` against every primary module to confirm.

### Criterion 2: Execution Correctness

Every operator invocation shows the full signature. There are no parameter omissions, raw strings where InputUnits are required, or invocations outside a module's `valid_layers` or `valid_roles`.

Invocations are shown in the order called. Intermediate results that feed subsequent invocations are included.

### Criterion 3: Output Quality

The session output is complete, in the declared format, and structurally substantive.

Each face in a StructuredFaces output or each criterion result in a ValidatorAssessment must make specific, checkable claims.

### Criterion 4: Assessment Completeness

A ValidatorAssessment is present and shows all five criteria evaluated. The recommendation is `accept`.

If an earlier recommendation was `revise` or `re-run`, the session must be revised and only the final accepted output included in the library entry.

### Criterion 5: Clone Utility

A Clone Guide is present. It lists every field that must change when adapting the session and explains what the correct change looks like.

### Session ID Assignment

Session IDs in the form `CS-NN` are assigned by the maintainer on merge. Do not pre-assign an ID in your PR.

Submit with a descriptive working title in the session metadata. The ID will be assigned at merge.

---

## Book Contributions

Book contributions include corrections, clarifications, new worked examples, additional cross-references, and structural improvements to the three parts, registry, and session library.

### What Requires a Book Contribution PR

- Factual corrections
- Prose clarifications
- New worked examples
- Cross-reference additions
- Structural improvements that do not change content

### What Does Not Belong in a Book PR

- Content that contradicts an existing module's declared scope
- New doctrine or system commitments
- Rewrites based solely on stylistic disagreement

### Prose Standards for Book Contributions

Follow the existing voice: second person, practitioner-facing, directive without being prescriptive.

The book's voice is precise and direct. It does not hedge, use filler transitions, or repeat what a prior section already states.

Worked examples should follow the format established in Part III Chapter 15:

**InputUnit → invocation → output → assessment**

Do not abbreviate the structure.

---

## Versioning Standards

Every module has a version stamp in `module.json`. Every change to a module requires a version increment.

### Version Format

`MAJOR.MINOR.PATCH`

| Increment | When to use |
|-----------|-------------|
| `PATCH` | Prose corrections that do not change scope, invocation syntax, or dependencies |
| `MINOR` | Scope clarifications, examples, related entries, and additive documentation improvements |
| `MAJOR` | Scope, role, layer, dependencies, invocation syntax, or output schema changes |

**The major version rule:** A MAJOR increment changes the module's structural contract. Every module in `required_by` must be audited for compatibility. The PR must include a dependency impact statement.

**Draft modules:** Draft modules use `0.x.x` versioning. Ratification advances the module to `1.0.0`.

**The golden rule:** When in doubt, increment higher. A MINOR increment when a MAJOR was warranted is a structural lie. It tells the system that no contract changed when one did.

### Changelog Requirements

Every version increment requires a changelog entry at `/docs/book/changelog`.

Each entry contains:

- Module ID and version
- Date
- Change type: PATCH, MINOR, or MAJOR
- Contributor handle
- Specific changes
- Impact information for MAJOR changes

Changelog entries are written by the contributor and included in the PR. The maintainer verifies and merges them.

---

## Review Criteria

Reviewers evaluate structural correctness against published standards rather than subjective preference.

### Module Review Criteria

| Criterion | What the Reviewer Checks |
|-----------|--------------------------|
| **ID validity** | Correct convention, kebab-case, unique in registry |
| **Role correctness** | Declared role matches actual function |
| **Layer correctness** | Layer and dependency direction are appropriate |
| **Scope precision** | Scope is bounded and testable |
| **Scope compliance** | Prose does not exceed scope |
| **Dependency completeness** | Dependencies exist and closure is verified |
| **No hidden dependencies** | Prose does not implicitly require undeclared modules |
| **No cycles** | Module introduces no dependency cycle |
| **Invocation completeness** | Parameters are named, typed, and represented in the input schema |
| **Output schema completeness** | Output fields are named and typed |
| **Validator appropriateness** | Validator ID is valid and appropriate |
| **Version and status** | Correct initial values or revision increment |

### Session Review Criteria

| Criterion | What the Reviewer Checks |
|-----------|--------------------------|
| **Grammar completeness** | All nine fields populated |
| **Field test compliance** | Each field passes its test |
| **active_modules closure** | Dependency closure verified |
| **Invocation correctness** | Full signatures, correct parameter types, valid context |
| **Output completeness** | Declared format and required fields present |
| **Assessment presence** | ValidatorAssessment present with `accept` recommendation |
| **Clone guide presence** | All fields requiring adaptation are listed |
| **Use case novelty** | Session covers a new use case |

### Book Review Criteria

| Criterion | What the Reviewer Checks |
|-----------|--------------------------|
| **Factual accuracy** | Claims match canonical specifications |
| **Scope consistency** | Content does not contradict module scopes |
| **Canon consistency** | Content does not contradict canon commitments |
| **Voice consistency** | Prose matches established voice |
| **Cross-reference accuracy** | Module IDs are valid |
| **No duplication** | Content does not unnecessarily restate existing material |

---

## Contribution Principles

These principles explain why the rules exist.

**Precision over completeness.**

A module that covers three things precisely is better than a module that covers ten things roughly. When you find yourself widening a scope to include adjacent content, stop and ask whether the adjacent content is a gap that deserves its own module. It usually is.

**Structure over prose.**

The structural specification in `module.json`, `module_links.json`, and `module_session.json` is more important than the prose in `module.md`.

A module with imprecise prose but correct structure can be fixed. A module with correct prose but wrong structure propagates errors silently through every session that invokes it. Get the structure right first.

**Gaps are valuable.**

Identifying a genuine gap in the module registry is a contribution even before you fill it. If you find a gap, open an issue. Gap identification is useful on its own.

**The canon protects everyone.**

The five canon commitments are the shared ground that makes the system coherent across contributors. A contribution that violates the canon does not expand the system. It creates an incompatible fork.

**Ratification is a gift, not a gate.**

The observation period and production session requirement protect practitioners who will depend on the module. Ratification is the system's way of saying: this module has been tested and it holds.

**Your session record is your evidence.**

The best evidence that a module or session contribution is correct is a production session that uses it and returns `recommendation: accept`.

Before submitting anything for ratification, run the session. The output will tell you whether the contribution does what you think it does.

---

*TriadicFrameworks — `/docs/contributing.md`*

*Authored by Nawder Loswin. AI-augmented authorship. All rights reserved.*

🔺 **Triadic Support Path**  
**Clarity • Alignment • Lineage**