# Book Changelog

> **Version history for the TriadicFrameworks Book.**
> This changelog tracks changes to the book's documentation files — the index,
> the three parts, the registry, the session library, the canon page, the glossary,
> the contributing guidelines, and this changelog itself.
>
> **This is not the module changelog.** Individual module version history is tracked
> per-module in each module's `module.json` version stamp and its corresponding
> changelog entry in that module's PR. Registry-level version history is tracked
> in the registry version stamp. This file covers the book as a documentation artifact.

---

## Format

Every entry follows this structure:

```markdown
## Book v[MAJOR.MINOR.PATCH] — [YYYY-MM-DD]

**Summary:** One sentence describing the release.
**Maintained by:** [author handle or name]

### Added
- [New file or section added]

### Changed
- [Existing content modified — describe what changed and why]

### Fixed
- [Errors corrected — describe what was wrong and what is now correct]

### Removed
- [Content removed — describe what was removed and why]

### Notes
[Optional: context, rationale, or guidance for practitioners reading this entry]
```

**Versioning rules for the book:**

| Increment | When to use |
|-----------|-------------|
| `MAJOR` | Structural reorganization of the book (new parts, removed sections, reordered chapters, renamed files) |
| `MINOR` | New files added, new sections within existing files, substantial additions that expand coverage |
| `PATCH` | Corrections, clarifications, cross-reference fixes, typos, formatting improvements |

**How to add an entry:** Insert new entries at the top of the log, below this Format section. Entries are ordered newest-first. Never edit a closed entry — if a prior entry contained an error, correct it with a new PATCH entry that references the original.

---

## Book v1.0.0 — 2026-09-25

**Summary:** Initial release — the complete TriadicFrameworks Book, all ten files authored from first principles in a single session.
**Maintained by:** Nawder Loswin

### Added

**`/docs/book/index.md`** — Book index and front door.
The canonical entry point for the TriadicFrameworks Book. Establishes the five-step Start Here path, states all five canon commitments at introductory depth, defines the four-file module architecture, specifies the nine session grammar fields, introduces the three-part reader journey (Orient, Navigate, Apply), explains how the book is maintained, and provides the system Quick Reference glossary.

**`/docs/book/part-i.md`** — Part I: Orient (Chapters 1–6).
Six chapters covering the minimum viable understanding required to engage the system without confusion. Chapter 1: Recursive Triadic Thinking — the three structural faces, why three (not two or four), recursion as a load-bearing concept, and a two-pass worked example. Chapter 2: The Canon Unpacked — each of the five commitments with operational meaning and failure-mode analysis. Chapter 3: Module vs. Document — the five properties a module has that a document does not, with a concrete illustration. Chapter 4: The Four-File Architecture — each file's purpose, field-level tables, the prescribed reading order, and what happens when any file is missing. Chapter 5: The Vocabulary — all ten roles and five layers defined with examples, the role × layer position table, and the dependency direction rule. Chapter 6: How Canon Constrains Everything — the concentric boundary model, the four most common constraint violations, and why irreversibility is a feature. Exit checklist: 18 binary items.

**`/docs/book/part-ii.md`** — Part II: Navigate (Chapters 7–12).
Six chapters covering the skill of moving through the module system without a guide. Chapter 7: Reading a Module — annotated four-step walkthroughs of all four files using `rtt-op-core` as the example module. Chapter 8: Traversing the Dependency Graph — forward traversal (surface to foundation) with a complete worked chain, backward traversal for impact analysis, hidden dependency detection, and cycle detection and breaking. Chapter 9: Module Groups and `modules_group.json` — all five group-entry fields, membership rules, and the six-step group creation procedure. Chapter 10: Finding Relevant Modules — the four-stage module discovery protocol with a complete end-to-end worked example. Chapter 11: Identifying Gaps and Proposing New Modules — the three gap types, true vs. apparent gap distinction, the gap identification protocol, the four anchoring decisions, minimum valid draft schema, and ID naming convention. Chapter 12: The Module Registry — all 12 primary groups with layer affinity, the registry navigation decision tree, and version discipline guidance. Exit checklist: 22 binary items.

**`/docs/book/part-iii.md`** — Part III: Apply (Chapters 13–17).
Five chapters covering live session execution. Chapter 13: Populating the 9-Field Session Grammar — field-by-field population rules, field tests, common errors, a fully populated example session. Chapter 14: Operator Invocation — the invocation grammar, three fully worked invocations (`RTT.pass`, `Clarity.evaluate`, `Scope.check`), chaining rules, and the five non-negotiable rules of invocation. Chapter 15: Running a Complete RTT Pass — end-to-end execution from raw input to validated depth=2 output, including InputUnit preparation, session initialization, both passes with full face text, and the validator invocation. Chapter 16: Applying Spectral Clarity and the Nawderian Theorem — the theorem stated and unpacked, the five clarity criteria defined, a complete ValidatorAssessment for the Chapter 15 output, and the three-row recommendation action table. Chapter 17: The Four Canonical Session Failure Modes — each failure mode with symptoms, root cause, detection method, recovery procedure, and the specific trap each contains. Exit checklist: 20 binary items.

**`/docs/book/registry.md`** — Module Registry.
The authoritative index of all 118 active modules across 12 primary groups. Each group section includes: group metadata (ID, layer affinity, description, navigation guidance) and a module table (ID, label, role, layer, one-line scope). Groups covered: `core-engine` (8), `session-grammar` (11), `clarity-system` (8), `operator-suite` (14), `protocol-suite` (11), `validator-suite` (12), `grammar-suite` (8), `lens-suite` (10), `map-suite` (12), `bridge-suite` (8), `anchor-suite` (8), `index-suite` (8). Closes with a 118-entry master alphabetical index (ID, label, group) and registry metadata block (total count, version, last updated).

**`/docs/book/sessions.md`** — Canonical Session Library.
Eight fully worked canonical sessions practitioners can reference, clone, and adapt. Each session includes: complete 9-field grammar, all operator invocations with full signatures, complete output in declared format, ValidatorAssessment with all criteria evaluated and `recommendation: accept`, and a Clone Guide specifying exactly which fields to change when adapting. Sessions: CS-01 (Baseline RTT Analysis, depth=1), CS-02 (Two-Pass Recursive RTT Analysis, depth=2), CS-03 (Scope Compliance Check), CS-04 (Dependency Audit with forward traversal), CS-05 (Gap Identification and Module Draft), CS-06 (Multi-Lens RTT Analysis with temporal + stakeholder lenses active), CS-07 (Session Diagnosis and Repair of a fully malformed session), CS-08 (Clarity Evaluation of an Existing Output). Library Notes section covers session combination chains, situational guidance table (12 rows), common adaptation errors (5 named errors), session submission criteria, and registry cross-reference.

**`/docs/contributing.md`** — Contribution Guidelines.
Complete contribution standards for the TriadicFrameworks repository. Covers: what can and cannot be contributed (the five non-contributable areas), the eight-step PR process (issue → branch → write → self-review → open PR → review → ratification → merge), complete module authoring standards (the four anchoring decisions, all four file requirements with field-level tables, role-specific `module.md` content requirements, prose standards, invocation syntax rules), the ratification flow (five ratification criteria, ratification request format, fast-track ratification eligibility), session library contribution criteria (five criteria with reviewer checks), book contribution standards, versioning standards (MAJOR/MINOR/PATCH with the golden rule), review criteria tables for modules, sessions, and book contributions, and seven contribution principles.

**`/docs/book/canon.md`** — Canon Standalone Anchor Page.
The authoritative reference for the five canon commitments, designed to be cited rather than read as a tutorial. Each commitment is presented with: the canonical statement (verbatim, quotable), the backing anchor module ID, operational meaning, what the commitment prohibits, and what breaks if violated. Includes the canon declaration, a reference summary table, citation guidance (correct and incorrect citation examples), and a section clarifying what the canon is not (not the complete system, not a checklist, not the same as the book, not negotiable per-session). Links to Part I Chapter 2 for the tutorial treatment.

**`/docs/book/glossary.md`** — Full System Glossary.
Authoritative definitions of all defined terms in the TriadicFrameworks system, organized into 13 domain sections with a master alphabetical index. Sections: Core System Concepts (8 entries), The RTT Engine (10 entries), Module Architecture (14 entries), The Role Enum (10 entries — all roles defined), The Layer Enum (7 entries — all layers plus derived concepts), The Session Grammar (15 entries — all nine fields plus session lifecycle terms), Output Formats (6 entries — all FormatEnum values), The Clarity System (14 entries), Operator Invocation (8 entries), The Dependency System (12 entries), Session Failure Modes (4 entries — all four canonical modes), Versioning and Module Status (8 entries), Attribution and Authorship (3 entries). Master alphabetical index: 130+ terms with section links.

**`/docs/book/changelog.md`** — This file.
Book version history, format specification, contribution instructions, and initial v1.0.0 release entry.

### Notes

This release constitutes the complete initial TriadicFrameworks Book. Every file was authored from first principles in a single session on 2026-09-25, using AI-augmented authorship under the direction of Nawder Loswin. The book is internally consistent — all cross-references, module IDs, session grammar fields, clarity criteria, and role/layer enum values are coherent across all ten files.

The 118 modules registered in `registry.md` are specifications — their `module.json`, `module.md`, `module_links.json`, and `module_session.json` files are pending authoring as individual PRs per the contributing guidelines. The registry entry for each module is the declaration that the module should exist; the four-file specification is the contribution that makes it exist. Contributors should use `CS-05` (Gap Identification and Module Draft) as the session template for authoring any registered module whose four files have not yet been written.

Three immediate priorities for v1.1.0:
1. Author the four-file specifications for modules in `core-engine` and `session-grammar` — these are the highest-dependency modules and block the most downstream work
2. Author `CS-09` through `CS-12` in the session library — the current eight sessions cover the primary use cases; the next four should cover multi-module conflict detection, registry-level navigation, version increment workflow, and a complete module ratification walkthrough
3. Add the `anchor-suite` modules' four-file specifications — the canon anchor modules are referenced throughout the book and should be among the first fully specified

---

## Upcoming

The following are planned for near-term releases. They are not commitments — they are the maintainer's current intent. Scope and timing may shift as the system develops.

| Target Version | Planned Content |
|---------------|----------------|
| v1.1.0 | Four-file specifications for `core-engine` and `session-grammar` modules; CS-09 through CS-12 in the session library |
| v1.2.0 | Four-file specifications for `clarity-system` and `anchor-suite` modules; first group-level deep dive (`/docs/book/groups/core-engine`) |
| v1.3.0 | Four-file specifications for `operator-suite` and `validator-suite` modules; operator reference guide |
| v2.0.0 | Structural reorganization if warranted by practitioner feedback; possible addition of Part IV (Extend) covering advanced module authoring and system extension patterns |

---

→ [Return to Book Index](./index)
→ [Contributing Guidelines](../contributing)
→ [Module Registry](./registry)

---

*TriadicFrameworks Book — `/docs/book/changelog.md`*
*Authored by Nawder Loswin. AI-augmented authorship. All rights reserved.*
