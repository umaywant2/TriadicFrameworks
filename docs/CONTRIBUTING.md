<img width="1194" height="672" alt="CONTRIBUTING_" src="https://github.com/user-attachments/assets/930f67ad-adb3-41a3-84fd-0f4ded376dc6" />

- [`CONTRIBUTING_module.json`](https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/main/docs/CONTRIBUTING_module.json) — Agentic module schema role assignments

# 💞 Contributing to TriadicFrameworks  

> **This document governs all contributions to the TriadicFrameworks repository.**
> Read it in full before opening a pull request. There are no exceptions to the standards here — not for experience level, not for urgency, not for the size of the change.

---

## Before You Contribute

TriadicFrameworks is a precision system. Its value depends entirely on the structural integrity of its modules, the coherence of its canon, and the correctness of its session grammar. A contribution that is well-intentioned but structurally incorrect is not a partial improvement — it is a source of invisible errors that propagate through the dependency graph and corrupt downstream sessions.

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
|----------|---------|-------------|
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
The canon is irreversible. A PR that attempts to add, remove, modify, or reframe any of the five canon commitments will be closed without review. If you believe a canon commitment is wrong, that is a conversation to have with the author — not a pull request.

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

---

### Step 1: Open an Issue First

Before writing anything, open an issue describing:

- **What** you want to contribute (module, session, book edit, registry change)
- **Why** it is needed (gap identification, error correction, coverage expansion)
- **Which existing modules** your contribution depends on or affects

This step exists to catch two things early:
1. **Apparent gaps** — your contribution may already exist under a different ID. A reviewer will search the registry and confirm.
2. **Scope conflicts** — your proposed module may overlap with an existing module's scope in ways you did not see. A reviewer will flag this before you write four files.

Issues are lightweight. A few sentences plus the expected role, layer, and scope statement is enough to start the conversation. Do not spend significant effort on the contribution before the issue is reviewed.

**Exception:** Book contributions (typo fixes, broken link corrections, factual corrections) may be submitted as a PR without a prior issue. All other contributions require an issue first.

---

### Step 2: Branch

Create a branch from `main` following this naming convention:

```
[type]/[short-descriptor]
```

| Type prefix | Use for |
|-------------|---------|
| `module/` | New module or module revision |
| `session/` | New canonical session |
| `book/` | Book documentation change |
| `registry/` | Registry or group change |
| `fix/` | Error correction in any file |

Examples:
```
module/usage-metric-grammar
session/cs-09-multi-module-conflict-detection
book/part-ii-chapter-8-cycle-detection-example
fix/rtt-op-core-scope-near-violation
```

---

### Step 3: Write

Follow the authoring standards for your contribution type (detailed in the sections below). Write the content. Do not submit until the content is complete — partial PRs are not accepted.

---

### Step 4: Self-Review

Before opening the PR, apply this self-review checklist:

**For modules:**
- [ ] All four files are present and non-empty
- [ ] `module.json` scope statement is one to three sentences, precisely bounded
- [ ] `module.md` prose does not exceed the declared scope
- [ ] `module_links.json` `depends_on` list is complete and closure-verified
- [ ] `module_session.json` invocation syntax is complete and all parameters are named
- [ ] Module ID follows the `domain-role_short-descriptor` convention
- [ ] Version is `0.1.0` (all new modules start at draft version)
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
- [ ] Version stamps are not modified (book versioning is managed separately)

---

### Step 5: Open the PR

PR title format:
```
[TYPE] Short description
```

Examples:
```
[MODULE] Add usage-metric-grammar to grammar-suite
[SESSION] Add CS-09: Multi-Module Conflict Detection
[BOOK] Correct dependency traversal example in Part II Chapter 8
[FIX] Resolve scope near-violation in rtt-op-core module.md
```

PR description must include:

1. **Link to the originating issue**
2. **Summary of changes** — what files were added or modified
3. **Self-review checklist** — completed (copy from Step 4 above)
4. **Dependency impact statement** — which existing modules, if any, are affected by this change and how
5. **Scope compliance statement** — one sentence confirming the new content stays within its declared scope

PRs without all five elements will be returned for revision before review begins.

---

### Step 6: Review

A reviewer will be assigned within five business days. Reviews evaluate against the criteria in the [Review Criteria](#review-criteria) section below. Reviewers may:

- **Approve** — contribution meets all standards, ready to merge
- **Request changes** — specific issues identified, must be addressed before re-review
- **Close** — contribution touches a non-contributable area, or the gap is apparent rather than real

All reviewer feedback is structural, not stylistic. If a reviewer asks for a change, it is because a standard is not met — not because of personal preference.

---

### Step 7: Ratification (modules only)

New modules require ratification before their status changes from `draft` to `active`. See [The Ratification Flow](#the-ratification-flow) for the complete procedure.

Non-module contributions (sessions, book edits, registry updates) do not require ratification — they merge on reviewer approval.

---

### Step 8: Merge and Registry Update

On merge:
- The module is added to `modules_group.json` in its assigned group(s)
- The master registry index is updated
- The registry version stamp is incremented per the `version-increment-proto`
- The book changelog is updated

Registry and changelog updates are handled by the maintainer — contributors do not need to manage these.

---

## Module Authoring Standards

This section is the complete specification for what a valid module contribution looks like. Every requirement here corresponds to a structural rule in the system. None are stylistic preferences.

---

### The Four Anchoring Decisions

Before writing a single line of content, make and commit to these four decisions. Write them down. They are your contract with the system.

**Decision 1: Role**
Choose exactly one value from the Role enum. If you cannot choose without ambiguity, the module's purpose is not yet clear. Clarify the purpose — do not proceed.

**Decision 2: Layer**
Choose exactly one value from the Layer enum. Apply the dependency direction rule: your module will depend on modules at this layer and below. Confirm this constraint works for the content you need to express before proceeding.

**Decision 3: Scope**
Write the scope statement. One to three sentences. State what the module covers. State what it does not cover if the boundary is non-obvious. The scope statement is a promise — the module's prose must not exceed it. Write the scope before writing any prose.

**Decision 4: Dependencies**
List every module whose content must be valid for your module's content to be meaningful. Verify each dependency exists in the registry. If a dependency does not exist, you have found a nested gap — fill it first.

---

### `module.json` Requirements

```json
{
  "id": "required — follows domain-role_short-descriptor convention",
  "label": "required — human-readable, title case",
  "role": "required — exactly one value from Role enum",
  "layer": "required — exactly one value from Layer enum",
  "scope": "required — one to three sentences, precisely bounded",
  "version": "required — 0.1.0 for all new modules",
  "status": "required — draft for all new modules",
  "dependencies": ["required — may be empty array if no dependencies"],
  "tags": ["optional — lowercase, relevant keywords"]
}
```

**ID naming convention:** `[domain]-[role_short]-[descriptor]`

Role short forms:

| Role | Short Form |
|------|-----------|
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
- `usage-metric-gram` — domain: usage-metric, role: grammar
- `intervention-lens` — domain: intervention, role: lens
- `module-conflict-val` — domain: module-conflict, role: validator

Invalid ID examples:
- `UsageMetricGrammar` — not kebab-case
- `grammar-usage-metric` — role before domain, wrong order
- `usage_metric_grammar` — underscores, not hyphens
- `ugram` — too abbreviated to be meaningful

---

### `module_links.json` Requirements

```json
{
  "id": "required — must match module.json id exactly",
  "depends_on": ["required — same list as module.json dependencies"],
  "required_by": ["required — empty array for all new modules"],
  "related": ["optional — editorial neighbors, not structural dependencies"],
  "supersedes": ["required — empty array if not replacing an existing module"],
  "superseded_by": "required — null for all new modules"
}
```

**The closure rule:** Every module ID in `depends_on` must exist in the registry. If it does not exist, the contribution is blocked until the dependency is authored and merged.

**The `required_by` rule:** New modules always have an empty `required_by`. This field is populated when existing modules are updated to declare a dependency on the new module. Do not pre-populate it.

**The `related` rule:** `related` is editorial, not structural. A module in `related` is not required for the module to be valid — it is a suggested companion for practitioners. Do not put a structural dependency in `related` to avoid the closure rule. Reviewers check this.

---

### `module.md` Requirements

`module.md` is the human-readable face of the module. It must be written *within* the scope declared in `module.json` — not up to the edge of the scope, and not beyond it.

**Required sections for all modules:**
1. **Definition** — What this module is, in plain language. One paragraph.
2. **Scope statement** — The verbatim scope from `module.json`, set off in a blockquote.
3. **Content** — The module's substantive content, organized by the module's role type (see role-specific requirements below).
4. **Constraints** — What this module does not cover and what it must not be used for. Explicit exclusions prevent scope creep by future editors.

**Role-specific content requirements:**

| Role | Required content sections |
|------|--------------------------|
| `anchor` | The commitment stated, its non-negotiability explained, what breaks if violated |
| `lens` | What the lens foregrounds, what it does not change, how to activate it, combination rules |
| `protocol` | Numbered step sequence, trigger conditions, completion gate, what to do if a step fails |
| `grammar` | Required fields/structure, field types, validation rules, minimum valid form, worked example |
| `operator` | Invocation syntax (verbatim from `module_session.json`), parameter definitions, output structure, worked example |
| `index` | What is indexed, how entries are organized, how to use the index for navigation |
| `map` | What is charted, the relationships shown, how to read the map, limitations |
| `bridge` | What two regions are connected, what the translation layer does, valid input/output types |
| `validator` | What is validated, the criteria applied, how to interpret the assessment, how to act on each recommendation |
| `field` | Field name, type, valid values, validation rules, default (if any), field test |

**Prose standards:**
- Write in the second person ("you") for practitioner-facing content, third person ("the module") for system-facing content
- No hedging language in scope-claiming sections ("roughly," "generally," "sometimes") — the scope is precise or it is wrong
- All cross-references to other modules use module IDs, not labels
- Examples must be worked examples — not hypothetical sketches, but complete inputs-and-outputs pairs
- Maximum one editorial cross-reference per section ("see also: `rtt-anchor-definition`") — prose is not a link farm

---

### `module_session.json` Requirements

```json
{
  "id": "required — must match module.json id exactly",
  "invocation_syntax": "required — OperatorNamespace.method(param: <Type>, ...) format",
  "input_schema": {
    "param_name": "required — description of valid values and constraints for each parameter"
  },
  "output_schema": {
    "field_name": "required — type and description for each output field"
  },
  "valid_layers": ["required — at least one Layer enum value"],
  "valid_roles": ["required — at least one Role enum value"],
  "validator_id": "required — a valid validator module ID from the registry"
}
```

**Invocation syntax rules:**
- OperatorNamespace is derived from the module's domain (e.g., `RTT`, `Clarity`, `Scope`, `Session`, `Module`, `Gap`)
- Method name is a verb that describes the transformation (`pass`, `evaluate`, `check`, `trace`, `identify`, `draft`)
- Every parameter in the syntax must appear in `input_schema` with a description
- Parameters are named, not positional — every call must name its parameters explicitly
- If a parameter is optional, mark it with `optional:` in the description field of `input_schema`

**Validator ID rule:** The `validator_id` must reference an existing validator module in the registry. If no suitable validator exists, this is a nested gap. The nested gap must be filed as a separate issue. In the interim, the `validator_id` may reference `manifest-complete-val` as a structural placeholder — but the PR must include a linked issue for the missing validator.

---

## The Ratification Flow

Ratification is the process by which a module's status changes from `draft` to `active`. It is separate from the PR review process — a PR can be merged with a module in `draft` status, and ratification happens afterward.

---

### Why Ratification Is Separate

Merging a draft module adds it to the repository. Ratifying a module declares it fit for production use. These are different events. A draft module may be merged to:
- Unblock a dependency chain (another module needs this one to exist)
- Begin the ratification clock (a module must be in `draft` for a minimum observation period)
- Allow integration testing before the module is declared production-ready

A draft module in the registry is visible and usable, but practitioners should treat it as experimental. Sessions that use draft modules should note this in their session records.

---

### Ratification Criteria

A module is ready for ratification when all of the following are true:

**1. Minimum observation period elapsed.**
The module has been in `draft` status for at least 14 days. This period allows practitioners to use the module in real sessions and surface issues before ratification.

**2. At least one production session completed.**
At least one session using this module has been run to completion, received a `recommendation: accept` from its validator, and been submitted to the session library or documented in the issue thread.

**3. No open issues against the module.**
All issues tagged with the module's ID have been resolved. No unresolved scope disputes, dependency questions, or content concerns.

**4. Scope compliance confirmed.**
The scope-check operator (`Scope.check`) has been applied to `module.md` against `module.json` and returned `COMPLIANT` (not `NEAR-COMPLIANT`) — or any near-violation identified has been resolved and the check re-run.

**5. Dependency chain audit passed.**
The dependency-audit protocol (`CS-04`) has been run on the module and returned no hidden dependencies and no cycles.

---

### Ratification Request

When all five criteria are met, open a ratification request issue with:

- Module ID and current version
- Link to the original PR
- Link to the production session record (or inline session summary)
- Scope compliance check result (copy the output)
- Dependency audit result (copy the DependencyTrace output)

The maintainer reviews the ratification request within 10 business days. On approval:

1. `module.json` `status` changes from `draft` to `active`
2. `module.json` `version` increments from `0.x.x` to `1.0.0`
3. `module_links.json` `required_by` is updated for all modules that now declare this module as a dependency
4. The registry version stamp increments
5. The book changelog is updated

---

### Fast-Track Ratification

Modules that fill a hard gap — a missing dependency that blocks an existing active module — are eligible for fast-track ratification. Fast-track reduces the minimum observation period to 7 days and waives the production session requirement (a diagnostic session using the gap-fill protocol may substitute). All other criteria apply.

To request fast-track ratification, include `[FAST-TRACK]` in the ratification request issue title and link to the blocked module's dependency audit output confirming the hard gap.

---

## Session Library Contributions

A new canonical session must meet all five criteria before it will be added to the library:

---

### Criterion 1: Grammar Completeness

All nine session grammar fields are populated. Each field passes its field-level test (Chapter 13, Part III). The `active_modules` list is dependency-closed — run `CS-04` against every primary module to confirm.

---

### Criterion 2: Execution Correctness

Every operator invocation shows the full signature — no parameter omissions, no raw strings where InputUnits are required, no invocations outside a module's `valid_layers` or `valid_roles`. Invocations are shown in the order they were called. If an invocation produced an intermediate result that fed the next invocation, that intermediate result is shown.

---

### Criterion 3: Output Quality

The session output is complete, in the declared format, and structurally substantive. "Substantive" means each face (for StructuredFaces outputs) or each criterion result (for ValidatorAssessment outputs) makes specific, checkable claims — not vague directional statements.

---

### Criterion 4: Assessment Completeness

A ValidatorAssessment is present and shows all five criteria evaluated. The recommendation is `accept`. If the recommendation is `revise` or `re-run`, the session was revised and the final accepted output is what appears in the library entry — not the intermediate rejected version.

---

### Criterion 5: Clone Utility

A Clone Guide is present. It lists every field that must change when adapting the session, with a note on what the correct change looks like. It does not list fields that should stay the same — only fields that must change.

---

### Session ID Assignment

Session IDs (`CS-[NN]`) are assigned by the maintainer on merge. Do not pre-assign an ID in your PR — you will not know what the next available number is. Submit with a descriptive working title in the session metadata; the ID will be assigned at merge.

---

## Book Contributions

Book contributions include corrections, clarifications, new worked examples, additional cross-references, and structural improvements to the three parts, the registry, and the session library.

---

### What Requires a Book Contribution PR

- Factual corrections (wrong module ID, incorrect scope summary, outdated version number)
- Prose clarifications (a section is genuinely ambiguous and can be made clearer)
- New worked examples (adding an example that illuminates a concept the existing text handles abstractly)
- Cross-reference additions (adding a "see also" link to a related module or section)
- Structural improvements (reorganizing a section for better scannability without changing its content)

---

### What Does Not Belong in a Book PR

- Content that contradicts an existing module's declared scope — if the book is wrong about a module, fix the book to match the module (not the reverse)
- New doctrine or new system commitments — these require a module PR or, if canon-level, a direct conversation with the maintainer
- Rewrites of sections you disagree with on stylistic grounds — book prose is intentional

---

### Prose Standards for Book Contributions

Follow the existing voice: second person, practitioner-facing, directive without being prescriptive. The book's voice is precise and direct — it does not hedge, does not use filler transitions, and does not repeat what was already said in a prior section.

If you are adding a worked example, follow the example format established in Part III Chapter 15: InputUnit → invocation → output → assessment. Do not abbreviate the structure.

---

## Versioning Standards

Every module has a version stamp in `module.json`. Every change to a module requires a version increment. The increment type depends on the nature of the change.

---

### Version Format

`MAJOR.MINOR.PATCH`

| Increment | When to use |
|-----------|-------------|
| `PATCH` | Prose corrections (typos, clarity improvements) that do not change the scope, the invocation syntax, or the dependency list |
| `MINOR` | Scope clarifications, additional examples, new `related` entries, documentation improvements that add content without changing the structural specification |
| `MAJOR` | Scope changes, role or layer changes, dependency additions or removals, invocation syntax changes, output schema changes |

**The major version rule:** A `MAJOR` increment changes the module's structural contract. Every module in the `required_by` list must be audited for compatibility after a major increment. The PR must include a dependency impact statement listing all affected modules and confirming compatibility.

**Draft modules:** All draft modules use `0.x.x` versioning. The first `MAJOR` increment on ratification is `1.0.0`. Subsequent major increments follow the standard scheme.

**The golden rule:** When in doubt, increment higher. A `MINOR` increment when a `MAJOR` was warranted is a structural lie — it tells the system that no contract changed when one did.

---

### Changelog Requirements

Every version increment requires a changelog entry. The changelog lives at [`/docs/book/changelog`](./book/changelog). Each entry follows this format:

```markdown
## [MODULE-ID] v[VERSION] — [YYYY-MM-DD]

**Type:** PATCH | MINOR | MAJOR
**Changed by:** [contributor handle]

### Changes
- [Specific change 1]
- [Specific change 2]

### Impact
[For MAJOR only: list of affected modules and compatibility confirmation]
```

Changelog entries are written by the contributor and included in the PR. The maintainer verifies and merges.

---

## Review Criteria

This section defines what reviewers check and what constitutes a passing review. Reviewers do not evaluate subjective quality — they evaluate structural correctness against published standards.

---

### Module Review Criteria

| Criterion | What the Reviewer Checks |
|-----------|-------------------------|
| **ID validity** | Follows `domain-role_short-descriptor`, kebab-case, unique in registry |
| **Role correctness** | The declared role matches the module's actual function |
| **Layer correctness** | The declared layer is appropriate for the content; dependency direction rule is satisfied |
| **Scope precision** | Scope statement is one to three sentences, precisely bounded, testable |
| **Scope compliance** | `module.md` prose does not exceed the declared scope |
| **Dependency completeness** | All declared dependencies exist in the registry; closure verified |
| **No hidden dependencies** | Prose does not implicitly require a module not in `depends_on` |
| **No cycles** | Adding this module does not introduce a dependency cycle |
| **Invocation completeness** | All parameters named, typed, and present in both syntax and `input_schema` |
| **Output schema completeness** | All output fields named and typed |
| **Validator appropriateness** | `validator_id` is a valid validator module appropriate for the output type |
| **Version and status** | `0.1.0` / `draft` for new modules; correct increment type for revisions |

---

### Session Review Criteria

| Criterion | What the Reviewer Checks |
|-----------|-------------------------|
| **Grammar completeness** | All nine fields populated |
| **Field test compliance** | Each field passes its documented field-level test |
| **active_modules closure** | Dependency closure verified for all primary modules |
| **Invocation correctness** | Full signatures, correct parameter types, valid context |
| **Output completeness** | Output is in declared format, all required fields present |
| **Assessment presence** | ValidatorAssessment present, all criteria evaluated, recommendation `accept` |
| **Clone guide presence** | Clone guide lists all fields that must change |
| **Use case novelty** | Session covers a use case not already in the library |

---

### Book Review Criteria

| Criterion | What the Reviewer Checks |
|-----------|-------------------------|
| **Factual accuracy** | Claims match the system's canonical specifications |
| **Scope consistency** | New content does not contradict existing module scopes |
| **Canon consistency** | New content does not contradict or weaken any canon commitment |
| **Voice consistency** | Prose matches the book's established voice |
| **Cross-reference accuracy** | Module IDs referenced are valid and in the registry |
| **No duplication** | New content does not restate what another section already covers clearly |

---

## Contribution Principles

These principles are not rules with enforcement mechanisms — they are the values that explain why the rules exist. Understanding them makes the rules easier to follow and harder to inadvertently violate.

---

**Precision over completeness.**
A module that covers three things precisely is better than a module that covers ten things roughly. When you find yourself widening a scope to include adjacent content, stop and ask whether the adjacent content is a gap that deserves its own module. It usually is.

**Structure over prose.**
The structural specification (`module.json`, `module_links.json`, `module_session.json`) is more important than the prose (`module.md`). A module with imprecise prose but correct structure can be fixed. A module with correct prose but wrong structure propagates errors silently through every session that invokes it. Get the structure right first.

**Gaps are valuable.**
Identifying a genuine gap in the module registry is a contribution even before you fill it. If you find a gap, open an issue. The gap identification is useful on its own — it may prompt a different contributor with the right expertise to fill it, or the maintainer to prioritize it.

**The canon protects everyone.**
The five canon commitments are not restrictions on creativity — they are the shared ground that makes the system coherent across all contributors. A contribution that violates the canon does not expand the system. It creates a fork that is incompatible with the rest of it.

**Ratification is a gift, not a gate.**
The 14-day observation period and the production session requirement are not bureaucratic delays — they are protection for practitioners who will depend on your module. A module that has been tested in real sessions before ratification is a module you can trust. Ratification is the system's way of saying: this module has been tested and it holds.

**Your session record is your evidence.**
The best evidence that a module or session contribution is correct is a production session that uses it and returns `recommendation: accept`. Before submitting anything for ratification, run the session. The output will tell you whether the contribution does what you think it does.

---

→ [Return to Book Index](./book/index)
→ [Browse the Module Registry](./book/registry)
→ [Canonical Session Library](./book/sessions)
→ [Book Changelog](./book/changelog)

---

*TriadicFrameworks — `/docs/contributing.md`*
*Authored by Nawder Loswin. AI-augmented authorship. All rights reserved.*

🔺 **Triadic Support Path**  
**Clarity • Alignment • Lineage**

---

🔺 *Support the Triad*

<div style="font-size: 0.8em; margin-bottom: 0.5rem;">
  <span style="
    display:inline-block;
    padding:3px 8px;
    border-radius:999px;
    background:#1a1a1a;
    color:#fff;
    font-family:Arial, sans-serif;
    font-size:11px;
  ">
    🤖 AI‑Ready Module • TriadicFrameworks
  </span>
</div>

<img src="https://img.shields.io/badge/🛠️Contributing%20Module-🧩Workflow%20Lineage%20Active-4c8eda?style=for-the-badge" alt="🛠️Contributing Module | 🧩Workflow & Lineage Active"/>

<img width="682" height="682" alt="tft_contributing_module" src="https://github.com/user-attachments/assets/1e8a8a49-1ed5-42b7-95b0-5e3e23853125" />
