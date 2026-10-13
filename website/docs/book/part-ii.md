# Part II — Navigate

> **Who this is for:** Practitioners who have completed Part I and can answer every item on its exit checklist.
> **What it requires:** Part I fluency. Comfort with JSON. Willingness to slow down and read precisely.
> **What it produces:** The ability to move through the TriadicFrameworks module system without a guide — reading, tracing, assembling, and extending it independently.

---

Part II is the system's interior.

Where Part I gave you a map of the territory, Part II puts you inside the territory and teaches you how to navigate it. This is the reference layer of the book — you will return to it constantly, not read it once and move on. The chapters are ordered for first-time readers, but they are structured for repeated lookup.

There are six chapters. First-time readers: proceed in order. Returning practitioners: use the chapter list below as a direct index.

---

## Chapters

- [Chapter 7 — Reading a Module: The Full Specification Walk](#chapter-7--reading-a-module-the-full-specification-walk)
- [Chapter 8 — Traversing the Dependency Graph](#chapter-8--traversing-the-dependency-graph)
- [Chapter 9 — Module Groups and modules_group.json](#chapter-9--module-groups-and-modules_groupjson)
- [Chapter 10 — Finding Relevant Modules for a Problem](#chapter-10--finding-relevant-modules-for-a-problem)
- [Chapter 11 — Identifying Gaps and Proposing New Modules](#chapter-11--identifying-gaps-and-proposing-new-modules)
- [Chapter 12 — The Module Registry: Orientation](#chapter-12--the-module-registry-orientation)
- [Exit Checklist — You Can Navigate When...](#exit-checklist--you-can-navigate-when)

---

## Chapter 7 — Reading a Module: The Full Specification Walk

Reading a module is not the same as reading a document. A document rewards linear reading — you start at the top and move to the bottom. A module rewards *structured* reading — you follow a defined sequence across four files, each one constraining how you read the next.

This chapter walks you through the complete specification read for a module. By the end, you will be able to open any module in the system and extract its full meaning — identity, content, relationships, and runtime behavior — without assistance.

### The Correct Sequence

As established in Part I, the reading order is fixed:

```
1. module.json          ← What the module IS
2. module_links.json    ← What the module CONNECTS TO
3. module.md            ← What the module SAYS
4. module_session.json  ← How the module BEHAVES at runtime
```

Violating this order is the single most common source of module misreading. The prose in `module.md` is persuasive — it is written to be clear and readable. If you read it before `module.json`, you will unconsciously extend the module's scope beyond what the manifest declares. The manifest is precise. The prose is expressive. Always let the precise constrain the expressive.

---

### Step 1: Reading `module.json`

Open `module.json` first. Read every field before forming any opinion about the module.

```json
{
  "id": "rtt-operator-core",
  "label": "RTT Operator — Core",
  "role": "operator",
  "layer": "operational",
  "scope": "Defines the invocation signature, input schema, and output schema for a single RTT pass on any well-formed input unit.",
  "version": "1.4.0",
  "status": "active",
  "dependencies": [
    "rtt-anchor-definition",
    "session-grammar-field-input",
    "session-grammar-field-output-format"
  ],
  "tags": ["core", "engine", "transformation"]
}
```

**Reading each field:**

**`id`** — This is the module's permanent identity. It does not change across versions. If you are referencing this module from another module's `module_links.json`, you use this ID. Never use the label — labels can change. IDs are stable.

**`label`** — The human-readable name. Useful for navigation; not useful for reference. Do not cite labels in operational contexts.

**`role`** — This tells you immediately what the module *does*. `operator` means this module performs a transformation. You now know: it takes inputs, applies a process, and produces outputs. Everything in `module.md` will be about that transformation — nothing else.

**`layer`** — `operational` means this module is invoked at runtime, inside sessions. It is not a static reference — it is an active participant. This also tells you its dependency constraints: it may depend on `structural` and `foundational` modules, but not on `surface` ones.

**`scope`** — Read this field as a *contract*. The module promises to cover exactly what the scope states — no more, no less. If you find yourself expecting the module to explain RTT's history or philosophical grounding, you are reading outside the scope. This module covers the invocation signature, input schema, and output schema for a single RTT pass. That is all.

**`version`** — `1.4.0` means this module has been updated four minor revisions since its first major release. If you have cached knowledge of an earlier version, assume it has changed. Always check the version stamp when returning to a module after time away.

**`status`** — `active` means this module is in full operation. Other valid statuses: `draft` (not yet ratified), `deprecated` (still present, but superseded — check `module_links.json` for `superseded_by`), `archived` (removed from active use).

**`dependencies`** — Three dependencies are declared. Before this module can be validly invoked, all three must be resolved in the session context. Write them down. You will verify them in Step 2.

**`tags`** — Informational. Useful for search and grouping, not for structural reasoning.

**After reading `module.json`, you know:** What this module is, what it does, where it lives in the stack, exactly what it covers, and what it depends on. You have not yet read a word of prose.

---

### Step 2: Reading `module_links.json`

```json
{
  "id": "rtt-operator-core",
  "depends_on": [
    "rtt-anchor-definition",
    "session-grammar-field-input",
    "session-grammar-field-output-format"
  ],
  "required_by": [
    "clarity-operator-spectral",
    "session-protocol-initialization",
    "scope-check-operator"
  ],
  "related": [
    "rtt-operator-recursive-extension",
    "rtt-lens-temporal",
    "rtt-map-full-pass-anatomy"
  ],
  "supersedes": ["rtt-operator-v0-legacy"],
  "superseded_by": null
}
```

**Reading each field:**

**`depends_on`** — Confirms what `module.json` declared. These three modules must be active in a session for `rtt-operator-core` to be validly invoked. If any are absent, the session has a dependency gap. Note: dependencies are transitive — each of these three modules has its own `depends_on` chain. You are not done at this level; you may need to trace further.

**`required_by`** — Three modules require this one. This is critical for impact analysis: if you are considering modifying `rtt-operator-core`, you must check all three of these modules to understand what downstream effects your change will have. Never modify a module without reading its `required_by` list first.

**`related`** — These are not structural dependencies. They are editorial neighbors — modules in adjacent scope that a practitioner might want to read alongside this one. `rtt-operator-recursive-extension` handles multi-pass recursion (beyond a single pass), so it is a natural companion. These are suggestions, not requirements.

**`supersedes`** — This module replaces `rtt-operator-v0-legacy`. If you encounter that ID anywhere in the system, treat it as pointing to this module.

**`superseded_by`** — `null` means this module has not been replaced. It is the current version.

**After reading `module_links.json`, you know:** The module's full dependency chain entry point, its downstream impact surface, its editorial neighbors, and its version lineage.

---

### Step 3: Reading `module.md`

Now — and only now — read the prose. Read it within the boundaries you have established:

- **Scope boundary:** The module covers the invocation signature, input schema, and output schema for a single RTT pass. If a paragraph steps outside this boundary, it is a scope violation. Note it; do not let it expand your understanding of the module's domain.
- **Role boundary:** This is an `operator`. The prose should be procedural and transformation-focused. If it reads like a philosophy essay, something is wrong.
- **Layer boundary:** This is `operational`. The prose should address runtime behavior, not historical context.

Read the prose actively — flag any claims that seem to exceed the scope, any instructions that seem inconsistent with the declared role, and any examples that reference modules not listed in `module_links.json`. These are signals of authoring errors, not features.

---

### Step 4: Reading `module_session.json`

```json
{
  "id": "rtt-operator-core",
  "invocation_syntax": "RTT.pass(input: <InputUnit>, depth: <integer>, output_format: <FormatEnum>)",
  "input_schema": {
    "input": "A well-formed InputUnit — any thought, claim, decision, or artifact with a declared scope.",
    "depth": "Integer ≥ 1. Specifies the number of recursive passes. Default: 1.",
    "output_format": "A value from the FormatEnum. Specifies the structure of the output unit."
  },
  "output_schema": {
    "generative_face": "String. The parsed origin of the input.",
    "present_face": "String. The parsed current state of the input.",
    "terminal_face": "String. The parsed forward direction of the input.",
    "pass_depth": "Integer. The depth at which this output was produced.",
    "next_input": "InputUnit. The output repackaged as input for the next pass, if depth > 1."
  },
  "valid_layers": ["operational", "structural"],
  "valid_roles": ["operator", "protocol"],
  "validator_id": "clarity-validator-rtт-output"
}
```

**Reading each field:**

**`invocation_syntax`** — This is the exact call signature. Copy it precisely when invoking this operator in a session. `RTT.pass(input: <InputUnit>, depth: <integer>, output_format: <FormatEnum>)`. Three parameters: the input unit, the recursion depth, and the output format. All three are required. A call with missing parameters is malformed.

**`input_schema`** — Defines what each parameter must be. `input` must be a "well-formed InputUnit" — a unit of thought with a declared scope. If your input has no declared scope, you must declare one before invoking the operator. `depth` defaults to 1 — a single RTT pass. `output_format` must be a value from the FormatEnum.

**`output_schema`** — Defines what you will receive. Every invocation of this operator produces exactly these five fields. If you are building a downstream module that consumes RTT output, design its input schema against this output schema.

**`valid_layers`** — This operator may be invoked in `operational` and `structural` layer contexts. It may not be invoked in `surface`, `foundational`, or `meta` contexts. If a session's `layer_context` field is `foundational`, this operator is not available.

**`valid_roles`** — This operator may be invoked by `operator` and `protocol` role modules. A `grammar` module cannot directly invoke it.

**`validator_id`** — After invocation, outputs are evaluated by `clarity-validator-rtт-output`. You do not call this manually — it is applied automatically when the session's validator field is active.

**After reading `module_session.json`, you know:** Exactly how to call this module, what to give it, what to expect back, where it may and may not be used, and how its outputs are validated.

---

### The Complete Read: Summary

| Step | File | What You Learn |
|------|------|----------------|
| 1 | `module.json` | Identity, role, layer, scope, version, status, dependencies |
| 2 | `module_links.json` | Upstream dependencies, downstream impact, neighbors, lineage |
| 3 | `module.md` | Content — bounded by the manifest |
| 4 | `module_session.json` | Invocation syntax, input/output schemas, valid contexts, validator |

A practitioner who completes all four steps for any module in the system has a complete, checkable, version-stamped understanding of that module. A practitioner who reads only `module.md` has an impression.

---

## Chapter 8 — Traversing the Dependency Graph

Every module exists in a web of dependencies. Navigating that web — tracing a chain from a surface output back to its foundational anchors, or forward from an anchor to its surface expressions — is the core navigation skill of Part II.

This chapter teaches both directions of traversal, the rules that govern each, and the failure modes that trap practitioners who traverse without discipline.

### The Dependency Graph: What It Is

The full set of `depends_on` and `required_by` relationships across all modules in the system constitutes the **dependency graph**. It is a directed acyclic graph (DAG) — directed because dependencies have direction (A depends on B ≠ B depends on A), and acyclic because a module cannot depend on itself, directly or through a chain.

The dependency graph has a natural orientation: it flows from `surface` down through `operational` and `structural` to `foundational`. Surface modules depend on operational modules, which depend on structural modules, which depend on foundational anchors. Nothing flows upward.

### Forward Traversal: Surface to Foundation

Forward traversal asks: *given this surface output, what foundational anchors support it?*

This is the direction you traverse when you want to understand *why* an output is valid — what the chain of commitments and specifications is that makes this output legitimate.

**The procedure:**

1. Start at the surface module (or the output's producing module).
2. Read its `module_links.json`. Note every entry in `depends_on`.
3. For each dependency, read *its* `module_links.json`. Note its `depends_on`.
4. Repeat until you reach modules whose `depends_on` list is empty or contains only `foundational`-layer modules.
5. The set of `foundational`-layer modules at the bottom of the chain are the anchors supporting the original output.

**Worked Example — Forward Traversal:**

Starting module: `clarity-operator-spectral` (role: `operator`, layer: `operational`)

```
clarity-operator-spectral
  └─ depends_on:
       ├─ rtt-operator-core          (operational)
       │    └─ depends_on:
       │         ├─ rtt-anchor-definition           (foundational) ✓ ANCHOR
       │         ├─ session-grammar-field-input      (structural)
       │         │    └─ depends_on:
       │         │         └─ session-grammar-anchor (foundational) ✓ ANCHOR
       │         └─ session-grammar-field-output-format (structural)
       │              └─ depends_on:
       │                   └─ session-grammar-anchor (foundational) ✓ ANCHOR
       └─ nawderian-theorem-validator-pulses (foundational) ✓ ANCHOR
```

**Result of forward traversal:** `clarity-operator-spectral` ultimately rests on three foundational anchors:
1. `rtt-anchor-definition` — the definition of RTT itself
2. `session-grammar-anchor` — the 9-field session grammar specification
3. `nawderian-theorem-validator-pulses` — the Spectral Clarity theorem

Any output produced by `clarity-operator-spectral` is only as valid as these three anchors. If you question the output, you must question one of these anchors — and questioning a foundational anchor is a canon-level matter, not a module-level one.

### Backward Traversal: Foundation to Surface

Backward traversal asks: *given this foundational anchor, what surface modules ultimately express it?*

This is the direction you traverse when you want to understand the *impact* of a foundational module — everything in the system that will be affected if the anchor changes.

**The procedure:**

1. Start at the foundational anchor.
2. Read its `module_links.json`. Note every entry in `required_by`.
3. For each dependent, read *its* `module_links.json`. Note its `required_by`.
4. Repeat until you reach modules whose `required_by` list is empty (surface modules or terminal operational modules with no further dependents).
5. The full set of visited modules is the **impact surface** of the foundational anchor.

**Why backward traversal matters for change management:**

Before modifying any module — especially a foundational or structural one — run a backward traversal to determine its full impact surface. A change to a foundational anchor may cascade through dozens of operational and surface modules. If you do not traverse the impact surface before making the change, you will produce invisible inconsistencies that are extremely difficult to diagnose after the fact.

This is the single most important practice in module maintenance.

### Identifying Hidden Dependencies

A **hidden dependency** is a dependency that does not appear in `module_links.json` but functionally exists — because the module's prose makes claims that require another module to be valid.

Hidden dependencies arise from authoring errors: the author of `module.md` made a claim that depends on another module's content but forgot to declare it in `module_links.json`. The structural specification is incomplete.

**How to detect a hidden dependency:**

1. Read `module.md` carefully.
2. For every claim, ask: *does this claim require any module that is not in `depends_on`?*
3. If yes, you have found a hidden dependency.

**What to do with a hidden dependency:**

Do not silently absorb it. Report it as a structural bug. The fix is to add the missing module to `depends_on` in `module_links.json`, verify the dependency chain does not create a cycle, and increment the module's version.

### Cycle Detection

The dependency graph must be acyclic. A cycle occurs when Module A depends on Module B, which depends on Module C, which depends on Module A. Cycles are structural failures — they mean the system cannot resolve the dependency chain, because each module in the cycle requires another to be valid first.

**How to detect a cycle:**

During any traversal, maintain a visited set. If you encounter a module ID you have already visited in the current traversal path, you have detected a cycle. Stop. Do not attempt to resolve it by continuing — the cycle must be broken at the authoring level.

**How to break a cycle:**

Find the dependency in the cycle that is the weakest structural claim — the one that could be expressed as a `related` link rather than a `depends_on` link. Remove it from `depends_on` and add it to `related`. This breaks the cycle while preserving the editorial relationship.

---

## Chapter 9 — Module Groups and `modules_group.json`

Individual modules are the atoms of the system. Module groups are the molecules — clusters of related modules that share a domain, purpose, or structural region. Groups are the primary navigation unit for practitioners who know what domain they are working in but not which specific modules apply.

### What `modules_group.json` Is

`modules_group.json` is a single file at the repository root that defines all module groups in the system. It is not a module itself — it is a registry of groupings.

```json
{
  "groups": [
    {
      "id": "core-engine",
      "label": "Core Engine",
      "description": "The foundational and operational modules that constitute the RTT engine and its primary operators.",
      "layer_affinity": "foundational",
      "modules": [
        "rtt-anchor-definition",
        "rtt-operator-core",
        "rtt-operator-recursive-extension",
        "rtt-map-full-pass-anatomy",
        "rtt-lens-temporal",
        "rtt-lens-stakeholder"
      ]
    },
    {
      "id": "session-grammar",
      "label": "Session Grammar",
      "description": "The nine field modules and their governing anchor that constitute the complete session grammar specification.",
      "layer_affinity": "structural",
      "modules": [
        "session-grammar-anchor",
        "session-grammar-field-session-id",
        "session-grammar-field-intent",
        "session-grammar-field-scope",
        "session-grammar-field-active-modules",
        "session-grammar-field-role-context",
        "session-grammar-field-layer-context",
        "session-grammar-field-input",
        "session-grammar-field-output-format",
        "session-grammar-field-validator"
      ]
    },
    {
      "id": "clarity-system",
      "label": "Clarity System",
      "description": "The Spectral Clarity model, the Nawderian Theorem of Validator Pulses, and all validators derived from them.",
      "layer_affinity": "operational",
      "modules": [
        "nawderian-theorem-validator-pulses",
        "clarity-operator-spectral",
        "clarity-validator-rtt-output",
        "clarity-validator-session-output",
        "clarity-lens-signal-coherence",
        "clarity-map-validator-pulse-anatomy"
      ]
    }
  ]
}
```

### Reading a Group Entry

Each group entry has five fields:

| Field | What It Holds |
|-------|--------------|
| `id` | The group's unique identifier — used in session `active_modules` when activating a full group |
| `label` | Human-readable name |
| `description` | What the group covers and why these modules belong together |
| `layer_affinity` | The layer that best characterizes this group's center of gravity. Not all modules in the group are at this layer, but most are. |
| `modules` | Ordered list of module IDs in this group. Order is significant: it reflects recommended reading order for newcomers to the group. |

### Group Membership Rules

A module can belong to more than one group. This is intentional — some modules sit at the intersection of two domains and legitimately serve both.

However, a module's primary group should be determinable from its `module.json` alone. The `role` and `layer` combination, combined with the `scope` field, should make it clear which group is the primary home. Secondary group memberships are auxiliary.

If a module belongs to three or more groups, it is likely a signal that the module's scope is too wide. Consider splitting it.

### Constructing a New Group

When a new domain of modules emerges that does not fit any existing group, a new group must be created. The process:

**Step 1: Establish the group's scope.**
Write a one-paragraph description of what the group covers and what it does not. Apply RTT to this description before finalizing it — the three faces will surface gaps in the scope definition.

**Step 2: Identify candidate modules.**
Search the module registry for modules whose `scope` field intersects with the new group's description. Cast wide at first; you will narrow.

**Step 3: Verify layer affinity.**
Determine the layer that characterizes most of the candidate modules. If the candidates are spread evenly across three or more layers, the group's scope is too wide — split it into two groups with clearer layer affinity.

**Step 4: Determine membership.**
For each candidate module, ask: does this module's `scope` fall primarily within the new group's description? If yes, include it. If its scope falls at the boundary, add it with a note that it may belong to an adjacent group as well.

**Step 5: Establish the reading order.**
Order the `modules` array from foundational to surface within the group. Practitioners new to the group should be able to read in array order without encountering forward dependencies.

**Step 6: Add to `modules_group.json`.**
Write the new group entry, increment the file's version stamp, and submit for ratification.

---

## Chapter 10 — Finding Relevant Modules for a Problem

The system contains approximately 120 named modules across more than a dozen groups. When a practitioner encounters a novel problem, the question is not "which module do I use?" — it is "how do I find the modules that apply to this problem without reading all 120?"

This chapter defines the **module discovery protocol** — the structured procedure for identifying relevant modules from a problem statement.

### The Module Discovery Protocol

The protocol has four stages. Each stage narrows the candidate set. By the end, you have a short list of directly relevant modules and a clear picture of what else needs to be active in the session to support them.

---

**Stage 1: Parse the problem with RTT.**

Before touching the module system, apply RTT to the problem statement itself.

- *Generative face:* What situation gave rise to this problem? What is its origin context?
- *Present face:* What is the problem, right now, in its current form? What is structurally broken or missing?
- *Terminal face:* What does the problem need to become? What is the desired output state?

The terminal face is the most important for module discovery — it tells you what the session needs to produce. The output type determines which role of module you need most. For example:

| Terminal face output type | Primary role to look for |
|--------------------------|--------------------------|
| A structural pattern | `grammar` |
| A repeatable procedure | `protocol` |
| A transformed version of the input | `operator` |
| An evaluation of quality or correctness | `validator` |
| An organizing view of a domain | `map` or `index` |
| An interpretive frame | `lens` |

---

**Stage 2: Determine the operating layer.**

Ask: at what depth does this problem need to be solved?

- If the problem is about what an output *says* or *looks like* → `surface`
- If the problem is about how things are *structured or related* → `structural`
- If the problem is about how a *session or process should run* → `operational`
- If the problem is about *what the system fundamentally commits to* → `foundational`
- If the problem is about *understanding the system itself* → `meta`

The answer tells you which layer's modules are the primary candidates.

---

**Stage 3: Browse the relevant groups.**

With a primary role and primary layer identified, open `modules_group.json` and find groups whose `layer_affinity` matches the operating layer. Within those groups, look for modules whose `role` in `module.json` matches the primary role from Stage 1.

Read the `scope` fields of the matching candidates. The scope field is your filter — a module whose scope does not directly address the terminal face of your problem is not the right module, even if its role and layer match.

Narrow to a short list of 2–5 candidate modules.

---

**Stage 4: Trace the dependency chains of your candidates.**

For each candidate module on your short list, run a forward traversal (Chapter 8) to determine its full dependency chain. The union of all dependency chains across your short list is the minimum module set your session must include in `active_modules`.

Add this full set to your session's `active_modules` field. You are now ready to initialize the session.

---

### Worked Example: Assembling a Module Set

**Problem statement:** *"I have a draft output from a previous session. I need to evaluate whether it is clear — not whether it is well-written, but whether it is structurally coherent and meets the correctness criteria of the system."*

**Stage 1 — RTT parse:**
- *Generative:* A prior session produced an output. The output's validity is uncertain.
- *Present:* An unvalidated output exists. The gap is the absence of a systematic clarity evaluation.
- *Terminal:* A structured assessment of the output's clarity — stating which criteria it satisfies, which it does not, and which require additional input.

Terminal output type: an evaluation of quality/correctness → primary role: **`validator`**.

**Stage 2 — Operating layer:**
The problem is about *running a check on a session output* → **`operational`** layer.

**Stage 3 — Browse groups:**
Looking for `validator`-role modules in groups with `operational` layer affinity. The `clarity-system` group matches. Candidate modules from that group:

- `clarity-validator-rtt-output` — *scope: validates that a single RTT pass output contains all three structural faces and that each face is internally coherent.*
- `clarity-validator-session-output` — *scope: validates that a complete session output satisfies the session's declared intent, scope, and output-format specification.*

The problem involves a session output (not just a single RTT pass output), so `clarity-validator-session-output` is the primary module.

**Stage 4 — Trace dependencies:**

```
clarity-validator-session-output
  └─ depends_on:
       ├─ nawderian-theorem-validator-pulses    (foundational) ✓
       ├─ session-grammar-anchor               (foundational) ✓
       ├─ session-grammar-field-intent         (structural)
       │    └─ depends_on: session-grammar-anchor ✓ (already included)
       ├─ session-grammar-field-scope          (structural)
       │    └─ depends_on: session-grammar-anchor ✓ (already included)
       └─ session-grammar-field-output-format  (structural)
            └─ depends_on: session-grammar-anchor ✓ (already included)
```

**Minimum module set for `active_modules`:**
```
- clarity-validator-session-output
- nawderian-theorem-validator-pulses
- session-grammar-anchor
- session-grammar-field-intent
- session-grammar-field-scope
- session-grammar-field-output-format
```

The session is now ready to initialize with a fully resolved `active_modules` set.

---

## Chapter 11 — Identifying Gaps and Proposing New Modules

A gap is a module that should exist in the system but does not. Gaps are not failures — they are the system's growth frontier. Every gap identified and filled makes the system more complete.

This chapter teaches how to detect gaps, distinguish true gaps from apparent ones, and propose new modules in valid schema.

### What a Gap Looks Like

A gap manifests in one of three ways:

**Type 1: A missing dependency.** During a forward traversal, you discover that a module's `depends_on` list references a module ID that does not exist in the registry. The dependency is declared but the module has not been authored. This is a hard gap — the module with the missing dependency is incomplete until the gap is filled.

**Type 2: A missing role/layer intersection.** During the module discovery protocol, you determine that your problem requires a `protocol`-role module at the `structural` layer in a specific domain — and no such module exists. The system can handle your problem, but awkwardly, using modules that are adjacent but not precise. This is a soft gap — the system functions, but a targeted module would improve precision and reproducibility.

**Type 3: A missing group.** A set of related modules exists in the registry but no group has been defined to cluster them. Practitioners cannot find them efficiently because `modules_group.json` has no entry that surfaces them together. This is a navigational gap — the modules exist, but the discovery path is broken.

### Distinguishing True Gaps from Apparent Ones

Before proposing a new module, verify the gap is real.

**An apparent gap** occurs when the needed module exists but is named differently than expected, or is in a group you did not think to check. Before declaring a gap, run a broad search of `modules_group.json` and the module registry using synonyms and adjacent terms. If you find a module with a different ID but a matching scope, there is no gap — there is a discovery path issue (consider proposing a `bridge` or an `index` update instead).

**A true gap** is confirmed when:
1. No existing module has a scope that covers the needed content.
2. The needed content cannot be reasonably served by combining two adjacent modules.
3. The needed content is genuinely within the system's canon — it is not an extension that violates the five commitments.

### The Gap Identification Protocol

When you suspect a gap, apply this protocol before acting:

1. **Articulate the gap precisely.** Write one sentence stating what module is missing, including its role, layer, and scope. If you cannot write this sentence, the gap is not yet clear enough to fill.

2. **Search for alternatives.** Browse all groups with the relevant `layer_affinity`. Read scope fields of all modules in the relevant role category. Exhaust alternatives before concluding the gap is real.

3. **Apply RTT to the gap.** What gave rise to this gap (generative face)? What is the gap's current form — what exactly is missing (present face)? What would filling the gap enable (terminal face)? The terminal face is the justification for the new module.

4. **Determine the new module's four anchoring decisions** (see next section).

5. **Draft the proposal** and submit it for ratification.

### The Four Decisions Before Authoring

Every new module requires four decisions to be made and committed to before any content is written. These four decisions determine the module's position in the system — and once the module is in the registry, changing these decisions is a major structural event.

**Decision 1: Role.** What functional type is this module? Refer to the Role enum. If you cannot identify a single role without ambiguity, the module's purpose is not yet clear enough — clarify it before proceeding.

**Decision 2: Layer.** At what depth does this module live? Refer to the Layer enum. Apply the dependency rule: the module will depend on modules at this layer and below. It will not depend on modules above. Does this constraint work for the content you need to express?

**Decision 3: Scope.** Write the scope statement. One to three sentences, precisely bounding what the module claims to know. The scope statement is a promise. If you find yourself hedging — "this module covers X and sometimes Y and also touches on Z" — you have not decided on the scope. Decide.

**Decision 4: Dependencies.** What modules does this module depend on? List every module whose content must be valid for this module's content to be meaningful. Trace each dependency to verify it exists in the registry. If a dependency does not exist, you have discovered a nested gap — fill it first.

### Proposing a New Module: The Minimum Valid Schema

A module proposal is a set of four draft files. The minimum valid content for a proposal:

**Draft `module.json`:**
```json
{
  "id": "[domain]-[role-short]-[descriptor]",
  "label": "[Human-Readable Label]",
  "role": "[role-from-enum]",
  "layer": "[layer-from-enum]",
  "scope": "[Precise one-to-three sentence scope statement.]",
  "version": "0.1.0",
  "status": "draft",
  "dependencies": ["[list]", "[of]", "[dependency]", "[ids]"],
  "tags": ["[relevant]", "[tags]"]
}
```

**Draft `module_links.json`:**
```json
{
  "id": "[same-id-as-module.json]",
  "depends_on": ["[same as dependencies in module.json]"],
  "required_by": [],
  "related": ["[adjacent modules — editorial, not structural]"],
  "supersedes": [],
  "superseded_by": null
}
```

> Note: `required_by` is always empty in a proposal — no existing modules can reference a module that does not yet exist. It will be populated as other modules are updated to declare this new module as a dependency.

**Draft `module.md`:**
Write the canonical prose content — bounded strictly to the declared scope. A draft module should include at minimum: a definition of the module's core concept, a worked example, and any constraints on how the module may be used.

**Draft `module_session.json`:**
Specify the invocation syntax, input schema, output schema, valid layers, valid roles, and validator ID. If the validator for this module does not yet exist, flag this in the proposal — it is a nested gap.

### ID Naming Convention

Module IDs follow the pattern: `[domain]-[role-short]-[descriptor]`

| Segment | Rules |
|---------|-------|
| `domain` | The primary domain or group this module belongs to (e.g., `rtт`, `session-grammar`, `clarity`) |
| `role-short` | A short form of the role (e.g., `op` for operator, `anch` for anchor, `proto` for protocol, `val` for validator) |
| `descriptor` | A specific, unique descriptor for this module within its domain and role |

Examples:
- `rtт-op-core` — RTT domain, operator role, core variant
- `session-grammar-field-intent` — session grammar domain, field role, intent descriptor
- `clarity-val-session-output` — clarity domain, validator role, session output descriptor

IDs are kebab-case, lowercase, and must be unique across the entire registry. Choose the ID carefully — it is permanent.

---

## Chapter 12 — The Module Registry: Orientation

The module registry is the full set of approximately 120 active modules in the TriadicFrameworks system. This chapter provides an orientation to the registry's major regions — not a comprehensive index (that lives at [`/docs/book/registry`](./registry)), but a practitioner's map for understanding where things are and how to navigate to them.

### The Major Groups

The registry is organized into 12 primary groups and several auxiliary groups. The primary groups are:

---

**`core-engine`** — Layer affinity: `foundational`

The RTT definition anchor, the RTT operator suite (core, recursive extension, multi-depth), the RTT lens suite (temporal, stakeholder, spectral), and the RTT map modules. This is the system's innermost ring — everything else depends on something here.

*When to navigate here:* When you need to understand or invoke RTT at the mechanism level. When a session's outputs are inconsistent with expectation and you need to verify the engine is being applied correctly.

---

**`session-grammar`** — Layer affinity: `structural`

The session grammar anchor and all nine field modules. The grammar is specified here in complete form — each field as its own module with its own scope, type, validation rules, and default.

*When to navigate here:* When constructing or diagnosing a session. When a field value is ambiguous or contested. When you need the complete specification of a specific field's valid values.

---

**`clarity-system`** — Layer affinity: `operational`

The Nawderian Theorem of Validator Pulses, the Spectral Clarity operator, and all validators derived from the theorem. This group is invoked whenever an output needs formal clarity evaluation.

*When to navigate here:* When evaluating the quality of a session output. When a validator assessment is unclear and you need to trace its criteria back to the theorem.

---

**`operator-suite`** — Layer affinity: `operational`

All operator-role modules beyond the RTT operators. This includes the scope-check operator, the conflict-detection operator, the gap-identification operator, the dependency-trace operator, and the module-authoring operator.

*When to navigate here:* When you need to perform a specific transformation on an input and RTT alone is insufficient. When you need a procedural tool for a structural task.

---

**`protocol-suite`** — Layer affinity: `operational`

All protocol-role modules: session initialization, session closing, module authoring, conflict resolution, version-increment, and dependency-audit protocols.

*When to navigate here:* When you need a step-by-step procedure for a system maintenance or session management task.

---

**`validator-suite`** — Layer affinity: `operational`

All validator-role modules beyond those in the clarity system: scope validators, dependency validators, manifest completeness validators, and output-format validators.

*When to navigate here:* When a session output needs evaluation against a specific criterion other than Spectral Clarity. When you need to verify a module's structural integrity.

---

**`grammar-suite`** — Layer affinity: `structural`

All grammar-role modules: the session grammar (also in its own group), the operator invocation grammar, the module manifest grammar, the scope statement grammar, and the ID naming grammar.

*When to navigate here:* When you need to verify that a structural pattern — a session, a module, an invocation — is syntactically correct.

---

**`lens-suite`** — Layer affinity: `structural`

All lens-role modules: temporal, stakeholder, spectral, causal, and resolution-depth lenses.

*When to navigate here:* When a session needs an interpretive frame applied to its inputs or outputs. When you want to examine the same content from a different angle without changing the content.

---

**`map-suite`** — Layer affinity: `meta`

All map-role modules: the full RTT pass anatomy map, the module registry map, the dependency graph map, the session lifecycle map, and the clarity evaluation map.

*When to navigate here:* When you need a navigational view of a region of the system — not to invoke anything, but to understand how the pieces in that region relate to each other.

---

**`bridge-suite`** — Layer affinity: `structural`

All bridge-role modules. Bridges are narrow — each one connects exactly two adjacent regions of the system.

*When to navigate here:* When you are working across two module groups and need the defined translation layer between them.

---

**`anchor-suite`** — Layer affinity: `foundational`

All anchor-role modules not already captured in `core-engine` or `session-grammar`. These include the canon commitment anchors (one per canon commitment), the attribution anchor, and the clarity standard anchor.

*When to navigate here:* When you need to trace an output all the way to its foundational commitments. When a claim is contested and you need to ground it in the canon.

---

**`index-suite`** — Layer affinity: `meta`

All index-role modules: group indexes, domain indexes, and the master registry index. The master registry index is the closest thing the system has to a table of contents for all 120 modules.

*When to navigate here:* When you know the domain but not the specific module. When you are exploring a new region of the system for the first time.

---

### Registry Navigation Decision Tree

Use this decision tree to locate the right starting point in the registry for any problem:

```
What do you need?
│
├─ To understand a foundational concept
│    └─ Start at: anchor-suite → core-engine
│
├─ To construct or diagnose a session
│    └─ Start at: session-grammar → protocol-suite
│
├─ To transform an input
│    └─ Start at: operator-suite → core-engine (RTT operators)
│
├─ To evaluate an output
│    └─ Start at: clarity-system → validator-suite
│
├─ To interpret content from a new angle
│    └─ Start at: lens-suite
│
├─ To understand how system regions relate
│    └─ Start at: map-suite
│
├─ To verify structural correctness
│    └─ Start at: grammar-suite → validator-suite
│
├─ To connect two system regions
│    └─ Start at: bridge-suite
│
└─ To find a module in an unfamiliar domain
     └─ Start at: index-suite → master registry index
```

### A Note on Registry Growth

The registry is not static. Modules are added, deprecated, and occasionally restructured as the system matures. When you return to the registry after time away, check the master registry index first — it carries a version stamp and a changelog that will tell you what has changed since your last visit.

Never assume a module you remember from a previous session is still in its previous state. Always read `module.json` freshly. Version stamps exist for this reason.

---

## Exit Checklist — You Can Navigate When...

Before moving to Part III, verify you can answer every item below without referring back to this document.

**On Reading a Module:**
- [ ] You can name the four files in the correct reading order and state why the order is non-negotiable.
- [ ] You can read a `module.json` and extract: identity, role, layer, scope, version, status, and dependency list.
- [ ] You can read a `module_links.json` and identify: upstream dependencies, downstream impact surface, editorial neighbors, and version lineage.
- [ ] You can read a `module.md` within the constraints of the manifest — flagging any scope violations you detect.
- [ ] You can read a `module_session.json` and construct a valid operator invocation from its syntax field.

**On Dependency Traversal:**
- [ ] You can perform a forward traversal from a surface module to its foundational anchors.
- [ ] You can perform a backward traversal from a foundational anchor to its full impact surface.
- [ ] You can detect a hidden dependency and describe the correct fix.
- [ ] You can detect a dependency cycle and describe how to break it.

**On Module Groups:**
- [ ] You can read a group entry in `modules_group.json` and extract all five fields.
- [ ] You know the three membership rules for groups.
- [ ] You can construct a new group entry for a novel domain, applying the six-step procedure.

**On Module Discovery:**
- [ ] You can apply the four-stage module discovery protocol to a novel problem.
- [ ] You can determine a primary role from a problem's terminal face.
- [ ] You can determine an operating layer from a problem's present face.
- [ ] You can assemble a complete, dependency-resolved `active_modules` set for a session.

**On Gaps and New Modules:**
- [ ] You can distinguish a true gap from an apparent one.
- [ ] You can apply the gap identification protocol to a suspected gap.
- [ ] You can make the four anchoring decisions required before authoring any module.
- [ ] You can produce a minimum valid draft of all four module files.
- [ ] You can construct a valid module ID following the naming convention.

**On the Registry:**
- [ ] You can name all twelve primary groups and state each one's layer affinity.
- [ ] You can use the registry navigation decision tree to identify a starting point for any problem.
- [ ] You know the first thing to check when returning to the registry after time away.

---

**If every box is checked, you can navigate the system without a guide.**

→ [Proceed to Part III — Apply](./part-iii)

---

*TriadicFrameworks Book — `/docs/book/part-ii.md`*
*Authored by Nawder Loswin. AI-augmented authorship. All rights reserved.*
