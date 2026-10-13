# Module Registry

> **The authoritative index of all TriadicFrameworks modules.**
> 118 active modules across 12 primary groups. Use this as a reference, not a read-through.

---

## How to Use This Registry

This registry is organized by group. Each group section contains:
- Group metadata: ID, layer affinity, and description
- A module table: ID, label, role, layer, and one-line scope summary

**For first-time browsing:** use the Group Quick-Nav below to find the group most relevant to your problem. Read the group description first, then scan the scope column of the module table.

**For targeted lookup:** use the [Master Alphabetical Index](#master-alphabetical-index) at the bottom to find a module by ID when you already know part of its name.

**For role-based lookup:** see [`index-by-role`](#index-suite) in the index-suite for a cross-group view organized by functional type.

**Legend**

| Column | Meaning |
|--------|---------|
| ID | Stable unique identifier — use this in `active_modules`, `depends_on`, and `required_by` |
| Label | Human-readable name — for navigation only, not reference |
| Role | Functional type from the Role enum |
| Layer | Depth in the cognitive stack from the Layer enum |
| Scope | One-line summary of what this module covers — read the full `module.json` for the precise contract |

---

## Group Quick-Nav

| # | Group | Layer Affinity | Module Count |
|---|-------|---------------|-------------|
| 1 | [core-engine](#1-core-engine) | foundational | 8 |
| 2 | [session-grammar](#2-session-grammar) | structural | 11 |
| 3 | [clarity-system](#3-clarity-system) | operational | 8 |
| 4 | [operator-suite](#4-operator-suite) | operational | 14 |
| 5 | [protocol-suite](#5-protocol-suite) | operational | 11 |
| 6 | [validator-suite](#6-validator-suite) | operational | 12 |
| 7 | [grammar-suite](#7-grammar-suite) | structural | 8 |
| 8 | [lens-suite](#8-lens-suite) | structural | 10 |
| 9 | [map-suite](#9-map-suite) | meta | 12 |
| 10 | [bridge-suite](#10-bridge-suite) | structural | 8 |
| 11 | [anchor-suite](#11-anchor-suite) | foundational | 8 |
| 12 | [index-suite](#12-index-suite) | meta | 8 |
| | **Total** | | **118** |

---

## 1. core-engine

**Group ID:** `core-engine`
**Layer Affinity:** `foundational`
**Description:** The RTT definition anchor, the RTT operator suite, and the RTT lens and map modules that constitute the system's innermost ring. Every other module in the registry depends on something here. Navigate here when you need to understand or invoke RTT at the mechanism level, or when session outputs are inconsistent and you need to verify the engine is being applied correctly.

| ID | Label | Role | Layer | Scope |
|----|-------|------|-------|-------|
| `rtt-anchor-definition` | RTT — Core Definition | anchor | foundational | Defines RTT: the three structural faces, the recursive pass mechanic, and the InputUnit/OutputUnit contract |
| `rtt-op-core` | RTT Operator — Core | operator | operational | Single-depth RTT pass: invocation signature, InputUnit intake, and StructuredFaces output production |
| `rtt-op-recursive-extension` | RTT Operator — Recursive Extension | operator | operational | Multi-depth RTT pass: chains depth>1 passes and packages next_input between recursive depths |
| `rtt-op-multi-domain` | RTT Operator — Multi-Domain | operator | operational | Applies simultaneous RTT passes across two or more declared input domains with a unified output |
| `rtt-map-pass-anatomy` | RTT Map — Pass Anatomy | map | meta | Charts the internal structure of a single RTT pass: face generation sequence, validation order, and output packaging |
| `rtt-lens-temporal` | RTT Lens — Temporal | lens | structural | Foregrounds time-dependence in RTT face generation: emphasizes sequencing and change across faces |
| `rtt-lens-stakeholder` | RTT Lens — Stakeholder | lens | structural | Foregrounds whose interests are at stake across each RTT face: surfaces implicit stakeholder assumptions |
| `rtt-lens-causal` | RTT Lens — Causal | lens | structural | Foregrounds causal chains within each RTT face: origins, mechanisms, and consequences |

---

## 2. session-grammar

**Group ID:** `session-grammar`
**Layer Affinity:** `structural`
**Description:** The session grammar anchor and all nine field modules that together constitute the complete 9-field session grammar specification. Each field is its own module with its own scope, type definition, validation rules, and population constraints. Navigate here when constructing or diagnosing any session, when a field value is ambiguous, or when you need the precise specification of a specific field's valid values and tests.

| ID | Label | Role | Layer | Scope |
|----|-------|------|-------|-------|
| `session-grammar-anchor` | Session Grammar — Anchor | anchor | foundational | Canonical specification of the 9-field session grammar: field list, ordering, population rules, and malformation criteria |
| `session-grammar-field-session-id` | Session Field — session_id | field | structural | Specification of the session_id field: format convention, uniqueness requirement, and stability rules |
| `session-grammar-field-intent` | Session Field — intent | field | structural | Specification of the intent field: actionability test, testability test, and prohibited phrasing patterns |
| `session-grammar-field-scope` | Session Field — scope | field | structural | Specification of the scope field: inclusion/exclusion format, narrowing requirement, and mid-session check protocol |
| `session-grammar-field-active-modules` | Session Field — active_modules | field | structural | Specification of the active_modules field: dependency closure requirement, ordering convention, and completeness test |
| `session-grammar-field-role-context` | Session Field — role_context | field | structural | Specification of the role_context field: valid Role enum values and multi-role declaration rules |
| `session-grammar-field-layer-context` | Session Field — layer_context | field | structural | Specification of the layer_context field: valid Layer enum values and cross-layer session rules |
| `session-grammar-field-input` | Session Field — input | field | structural | Specification of the input field: InputUnit schema, scope alignment requirement, and completeness test |
| `session-grammar-field-output-format` | Session Field — output_format | field | structural | Specification of the output_format field: FormatEnum valid values and format-validator compatibility matrix |
| `session-grammar-field-validator` | Session Field — validator | field | structural | Specification of the validator field: required active_modules presence and output-format compatibility test |
| `session-grammar-proto-init` | Session Grammar — Initialization Protocol | protocol | operational | Step-by-step session initialization procedure: field population order, field tests, and completion gate |

---

## 3. clarity-system

**Group ID:** `clarity-system`
**Layer Affinity:** `operational`
**Description:** The Nawderian Theorem of Validator Pulses, the Spectral Clarity operator, all validators derived from the theorem, and the clarity standard anchor. Navigate here when evaluating the quality of a session output, when a validator assessment is unclear and you need to trace its criteria back to the theorem, or when confirming what the system's clarity standard actually requires.

| ID | Label | Role | Layer | Scope |
|----|-------|------|-------|-------|
| `nawderian-theorem-validator-pulses` | Nawderian Theorem of Validator Pulses | anchor | foundational | Canonical statement of the Nawderian Theorem: clarity as signal coherence across validator layers, not subjective understanding |
| `clarity-anchor-standard` | Clarity Standard — Anchor | anchor | foundational | Declares the clarity standard all outputs are held to: primacy of the theorem over subjective evaluation |
| `clarity-op-spectral` | Clarity Operator — Spectral | operator | operational | Applies the Spectral Clarity model to an OutputUnit: invokes the theorem, runs all five criteria, produces a ValidatorAssessment |
| `clarity-val-rtt-output` | Clarity Validator — RTT Output | validator | operational | Evaluates a StructuredFaces output against all five clarity criteria: face completeness, substantiveness, pass differentiation, scope compliance, intent fulfillment |
| `clarity-val-session-output` | Clarity Validator — Session Output | validator | operational | Evaluates a complete session output against its declared intent, scope, and output-format specification |
| `clarity-lens-signal-coherence` | Clarity Lens — Signal Coherence | lens | structural | Foregrounds signal coherence in any content: surfaces hedged claims, vague assertions, and incoherent structures |
| `clarity-grammar-validator-assessment` | Clarity Grammar — ValidatorAssessment | grammar | structural | Specifies the ValidatorAssessment structure: required fields, criterion result format, flag format, and recommendation enum |
| `clarity-map-validator-pulse-anatomy` | Clarity Map — Validator Pulse Anatomy | map | meta | Charts the internal structure of a validator pulse: criterion sequence, assessment generation, and recommendation derivation |

---

## 4. operator-suite

**Group ID:** `operator-suite`
**Layer Affinity:** `operational`
**Description:** All operator-role modules beyond the RTT operators in core-engine. These are the system's workhorses — every transformation performed on an input, every structural check, every field test is an operator invocation. Navigate here when you need to perform a specific transformation and RTT alone is insufficient, or when you need a procedural tool for a structural or session task.

| ID | Label | Role | Layer | Scope |
|----|-------|------|-------|-------|
| `scope-check-op` | Scope Check Operator | operator | operational | Checks a module's prose content against its manifest scope: identifies overclaiming, underclaiming, and scope violations |
| `conflict-detect-op` | Conflict Detection Operator | operator | operational | Detects structural conflicts between two modules with overlapping scopes: identifies incompatible claims at the same layer |
| `gap-identify-op` | Gap Identification Operator | operator | operational | Applies the gap identification protocol to a suspected missing module: returns a structured gap report with type, evidence, and nested gap check |
| `dependency-trace-op` | Dependency Trace Operator | operator | operational | Performs forward or backward traversal of the dependency graph from a starting module: returns the full traversal path |
| `module-author-op` | Module Authoring Operator | operator | operational | Generates a minimum valid four-file module draft from the four anchoring decisions: role, layer, scope, and dependencies |
| `input-prepare-op` | Input Preparation Operator | operator | operational | Wraps a raw input in a valid InputUnit by eliciting and declaring its scope |
| `output-package-op` | Output Packaging Operator | operator | operational | Packages an OutputUnit as a valid next-pass InputUnit: extracts next_input and validates scope continuity |
| `intent-test-op` | Intent Field Test Operator | operator | operational | Applies the intent field test to a candidate intent statement: returns pass/fail with specific failure reason |
| `scope-test-op` | Scope Field Test Operator | operator | operational | Applies the scope field test to a candidate scope statement: returns pass/fail with specific failure reason |
| `active-modules-test-op` | Active Modules Field Test Operator | operator | operational | Applies the active_modules field test: checks dependency closure for every module in the list |
| `format-check-op` | Format Check Operator | operator | operational | Verifies that a session output structurally matches its declared output_format specification |
| `chain-validate-op` | Chain Validation Operator | operator | operational | Validates an operator chain: checks output_schema → input_schema alignment for every consecutive pair |
| `session-field-test-op` | Session Field Test Operator | operator | operational | Applies the field-level specification test for any named session grammar field: returns pass/fail with reason |
| `pass-depth-extend-op` | Pass Depth Extension Operator | operator | operational | Evaluates whether additional RTT depth is structurally warranted: checks pass differentiation and unexplored face space |

---

## 5. protocol-suite

**Group ID:** `protocol-suite`
**Layer Affinity:** `operational`
**Description:** All protocol-role modules — step-by-step repeatable procedures for session management, module authoring, conflict resolution, version control, and system maintenance. Navigate here when you need a procedure, not a transformation. Protocols invoke operators; operators do not invoke protocols.

| ID | Label | Role | Layer | Scope |
|----|-------|------|-------|-------|
| `session-init-proto` | Session Initialization Protocol | protocol | operational | Step-by-step session initialization: field population order, field tests, active_modules assembly, and completion gate |
| `session-close-proto` | Session Closing Protocol | protocol | operational | Step-by-step session closing: validator application, output packaging, session record creation, and archival |
| `session-resume-proto` | Session Resumption Protocol | protocol | operational | Step-by-step session resumption: record retrieval, field re-verification, output state assessment, and continuation point determination |
| `module-author-proto` | Module Authoring Protocol | protocol | operational | Step-by-step module authoring: four anchoring decisions, four-file draft creation, scope compliance check, ratification submission |
| `conflict-resolve-proto` | Conflict Resolution Protocol | protocol | operational | Step-by-step conflict resolution between two modules: detection, scope adjudication, version increment, downstream impact audit |
| `version-increment-proto` | Version Increment Protocol | protocol | operational | Step-by-step version increment: change classification, version stamp update, changelog entry, dependent module notification |
| `dependency-audit-proto` | Dependency Audit Protocol | protocol | operational | Step-by-step dependency audit: forward traversal, hidden dependency detection, cycle detection, and remediation |
| `gap-fill-proto` | Gap Filling Protocol | protocol | operational | Step-by-step gap filling: gap confirmation, nested gap check, four anchoring decisions, draft creation, ratification submission |
| `group-create-proto` | Group Creation Protocol | protocol | operational | Step-by-step module group creation: scope, candidate identification, layer affinity, membership, reading order, modules_group.json update |
| `registry-update-proto` | Registry Update Protocol | protocol | operational | Step-by-step registry update: module addition, group assignment, master index update, version stamp increment |
| `failure-mode-recover-proto` | Failure Mode Recovery Protocol | protocol | operational | Step-by-step recovery for each of the four canonical session failure modes: detection, diagnosis, and corrective action |

---

## 6. validator-suite

**Group ID:** `validator-suite`
**Layer Affinity:** `operational`
**Description:** All validator-role modules beyond those in the clarity-system. These validators cover module structural integrity, session grammar completeness, operator invocation correctness, and session record validity. Navigate here when a session output needs evaluation against a criterion other than Spectral Clarity, or when verifying the structural integrity of a module, invocation, or session record.

| ID | Label | Role | Layer | Scope |
|----|-------|------|-------|-------|
| `scope-val` | Scope Validator | validator | operational | Validates that a module's prose content does not exceed its declared manifest scope |
| `dependency-val` | Dependency Validator | validator | operational | Validates that a module's dependency list is complete and cycle-free |
| `manifest-complete-val` | Manifest Completeness Validator | validator | operational | Validates that all four module files are present and all required fields are non-empty |
| `format-val` | Format Validator | validator | operational | Validates that a session output matches its declared output_format specification, field by field |
| `intent-val` | Intent Fulfillment Validator | validator | operational | Validates that a session output fulfills its declared intent: applies the intent field test post-session |
| `scope-compliance-val` | Scope Compliance Validator | validator | operational | Validates that a session output contains no references outside the session's declared scope |
| `invocation-val` | Invocation Validator | validator | operational | Validates that an operator invocation is syntactically complete: all required parameters present, correct types, valid context |
| `chain-val` | Chain Validator | validator | operational | Validates an operator chain: schema alignment, active_modules presence, and layer context compatibility |
| `module-id-val` | Module ID Validator | validator | structural | Validates that a module ID conforms to the naming convention: domain-role_short-descriptor, kebab-case, unique |
| `session-record-val` | Session Record Validator | validator | operational | Validates a complete session record: all nine fields present, output included, validator assessment included, closure confirmed |
| `active-modules-closure-val` | Active Modules Closure Validator | validator | operational | Validates the full dependency closure of an active_modules list: confirms every transitive dependency is present |
| `session-grammar-complete-val` | Session Grammar Completeness Validator | validator | operational | Validates that all nine session grammar fields are non-empty and have passed their individual field-level tests |

---

## 7. grammar-suite

**Group ID:** `grammar-suite`
**Layer Affinity:** `structural`
**Description:** All grammar-role modules — the structural patterns that define valid forms for sessions, operators, manifests, scope statements, module IDs, and data units. Navigate here when you need to verify that a structural pattern is syntactically correct, or when authoring a new module and you need the exact specification of what a valid manifest, scope statement, or ID looks like.

| ID | Label | Role | Layer | Scope |
|----|-------|------|-------|-------|
| `session-grammar-spec` | Session Grammar Specification | grammar | structural | Complete structural specification of the 9-field session grammar: field types, ordering, and population rules |
| `operator-invocation-grammar` | Operator Invocation Grammar | grammar | structural | Invocation grammar for all operator calls: Namespace.method(param: value) syntax, required/optional parameter rules |
| `module-manifest-grammar` | Module Manifest Grammar | grammar | structural | Required structure of module.json: all fields, types, valid values, and required/optional status |
| `scope-statement-grammar` | Scope Statement Grammar | grammar | structural | Required structure of a scope statement: coverage declaration, exclusion declaration, and boundary precision rules |
| `module-id-grammar` | Module ID Grammar | grammar | structural | Naming convention for module IDs: domain-role_short-descriptor pattern, kebab-case, and uniqueness requirement |
| `input-unit-grammar` | InputUnit Grammar | grammar | structural | Required structure of an InputUnit: content field, scope field, and well-formedness criteria |
| `output-unit-grammar` | OutputUnit Grammar | grammar | structural | Required structure of an OutputUnit: face fields, pass_depth, next_input, and packaging rules |
| `validator-assessment-grammar` | ValidatorAssessment Grammar | grammar | structural | Required structure of a ValidatorAssessment: criteria_results array, overall_coherence, flags, and recommendation field |

---

## 8. lens-suite

**Group ID:** `lens-suite`
**Layer Affinity:** `structural`
**Description:** All lens-role modules — perspectives that can be applied to any content to foreground a specific structural dimension without changing the content itself. Lenses are combinable; multiple may be active in a session simultaneously. Navigate here when a session needs an interpretive frame, or when you want to examine the same content from a different angle to surface claims that a neutral reading would miss.

| ID | Label | Role | Layer | Scope |
|----|-------|------|-------|-------|
| `lens-temporal` | Temporal Lens | lens | structural | Foregrounds time-dependence in any content: sequencing, duration, and change over time across all structural faces |
| `lens-stakeholder` | Stakeholder Lens | lens | structural | Foregrounds whose interests are at stake in any content: surfaces implicit stakeholder assumptions and unaccounted perspectives |
| `lens-causal` | Causal Lens | lens | structural | Foregrounds causal chains in any content: origins, mechanisms, and consequences within each structural face |
| `lens-spectral-clarity` | Spectral Clarity Lens | lens | structural | Applies the Spectral Clarity model as a viewing frame: surfaces hedged, vague, or incoherent claims in any content |
| `lens-resolution-depth` | Resolution Depth Lens | lens | structural | Foregrounds the resolution level of claims: distinguishes surface-level assertions from structural-level ones |
| `lens-scope-boundary` | Scope Boundary Lens | lens | structural | Foregrounds scope boundaries in any content: makes explicit what is and is not included |
| `lens-dependency` | Dependency Lens | lens | structural | Foregrounds dependency relationships in any content: surfaces what requires what to be valid |
| `lens-version` | Version Provenance Lens | lens | structural | Foregrounds version and temporal provenance: surfaces which claims are current and which may be outdated |
| `lens-intervention` | Intervention Lens | lens | structural | Foregrounds intervention points in any content: surfaces where action could change the terminal face |
| `lens-abstraction-level` | Abstraction Level Lens | lens | structural | Foregrounds the level of abstraction of claims: surfaces when claims are too abstract to act on or too specific to generalize |

---

## 9. map-suite

**Group ID:** `map-suite`
**Layer Affinity:** `meta`
**Description:** All map-role modules — navigational charts of regions of the system. Maps do not invoke anything; they provide orientational views of how the system's pieces relate to each other. Navigate here when you need to understand the shape of a region before entering it, when planning a complex multi-module session, or when explaining the system to a newcomer.

| ID | Label | Role | Layer | Scope |
|----|-------|------|-------|-------|
| `map-rtt-pass-anatomy` | Map — RTT Pass Anatomy | map | meta | Charts the internal structure of a single RTT pass: face generation, validation order, and output packaging |
| `map-module-registry` | Map — Module Registry | map | meta | Top-level navigational map of the full module registry: 12 groups, layer affinities, and entry points |
| `map-dependency-graph` | Map — Dependency Graph | map | meta | Navigational chart of the system's dependency graph: major clusters, flow direction, and cycle-risk regions |
| `map-session-lifecycle` | Map — Session Lifecycle | map | meta | Charts the complete session lifecycle: initialization, execution, validation, closure, and resumption |
| `map-clarity-evaluation` | Map — Clarity Evaluation | map | meta | Charts the clarity evaluation sequence: theorem application, criterion order, assessment generation, recommendation derivation |
| `map-role-layer-space` | Map — Role × Layer Space | map | meta | Charts the role × layer position space: all valid combinations, empty positions, and position constraints |
| `map-canon-constraint-model` | Map — Canon Constraint Model | map | meta | Charts the concentric boundary structure: canon, foundational, structural, operational, and surface layers |
| `map-failure-mode-recovery` | Map — Failure Mode Recovery | map | meta | Charts the four canonical session failure modes: detection signals, recovery entry points, and trap patterns |
| `map-operator-chain-patterns` | Map — Operator Chain Patterns | map | meta | Charts common operator chain patterns: the two-step canonical pattern, multi-operator chains, valid and invalid configurations |
| `map-book-structure` | Map — Book Structure | map | meta | Charts the TriadicFrameworks Book: three-part structure, chapter relationships, and cross-part cross-references |
| `map-reader-journey` | Map — Reader Journey | map | meta | Charts the three-part reader journey: Orient, Navigate, Apply — with chapter relationships and prerequisite paths |
| `map-group-relationships` | Map — Group Relationships | map | meta | Charts relationships between the twelve primary module groups: dependencies, bridges, and navigational adjacencies |

---

## 10. bridge-suite

**Group ID:** `bridge-suite`
**Layer Affinity:** `structural`
**Description:** All bridge-role modules — narrow translation layers connecting two otherwise separate regions of the system. Each bridge connects exactly two regions. Navigate here when you are working across two module groups and need the defined translation layer between them, or when an operator's output needs to feed an input in a different domain.

| ID | Label | Role | Layer | Scope |
|----|-------|------|-------|-------|
| `bridge-rtt-to-session` | Bridge — RTT → Session | bridge | structural | Connects the RTT core engine to the session grammar: translates RTT operator outputs into session field values |
| `bridge-session-to-clarity` | Bridge — Session → Clarity | bridge | structural | Connects the session grammar to the clarity system: translates session output into Clarity.evaluate() inputs |
| `bridge-module-to-registry` | Bridge — Module → Registry | bridge | structural | Connects individual module specs to the registry: translates module.json fields into registry entry format |
| `bridge-operator-to-validator` | Bridge — Operator → Validator | bridge | structural | Connects operator outputs to validator inputs: translates OutputUnit schemas into ValidatorAssessment input schemas |
| `bridge-lens-to-rtt` | Bridge — Lens → RTT | bridge | structural | Connects the lens suite to RTT operator invocations: translates active lens contexts into RTT pass modifiers |
| `bridge-grammar-to-manifest` | Bridge — Grammar → Manifest | bridge | structural | Connects grammar-suite specs to module manifest authoring: translates grammar rules into manifest field requirements |
| `bridge-protocol-to-session` | Bridge — Protocol → Session | bridge | structural | Connects protocol-suite procedures to session grammar: translates protocol steps into field population actions |
| `bridge-map-to-navigation` | Bridge — Map → Navigation | bridge | structural | Connects map-suite content to practitioner navigation workflows: translates map structures into step-by-step navigation paths |

---

## 11. anchor-suite

**Group ID:** `anchor-suite`
**Layer Affinity:** `foundational`
**Description:** All anchor-role modules not already captured in core-engine or session-grammar — the five canon commitment anchors, the attribution anchor, and the three enum anchors. Navigate here when tracing an output all the way to its foundational commitments, when a claim is contested and needs grounding in the canon, or when you need the precise authoritative statement of any enum.

| ID | Label | Role | Layer | Scope |
|----|-------|------|-------|-------|
| `canon-anchor-rtt-engine` | Canon Anchor — RTT as Engine | anchor | foundational | Declares that RTT is the non-negotiable governing engine: not one tool among many, but the structural substrate |
| `canon-anchor-clarity-standard` | Canon Anchor — Clarity Standard | anchor | foundational | Declares that clarity is precision under pressure, not comfort: the Nawderian Theorem as the sole clarity criterion |
| `canon-anchor-module-unit` | Canon Anchor — Module as Unit | anchor | foundational | Declares that modules are the unit of knowledge: prose alone is insufficient; the four-file architecture is required |
| `canon-anchor-session-unit` | Canon Anchor — Session as Unit | anchor | foundational | Declares that sessions are the unit of application: the 9-field grammar is required for every application context |
| `canon-anchor-attribution` | Canon Anchor — Honest Attribution | anchor | foundational | Declares the honest attribution standard: Nawder Loswin as author, AI as precision instrument |
| `role-enum-anchor` | Role Enum — Anchor | anchor | foundational | Declares the complete Role enum: ten roles, their definitions, and the one-role-per-module constraint |
| `layer-enum-anchor` | Layer Enum — Anchor | anchor | foundational | Declares the complete Layer enum: five layers, their definitions, and the downward dependency direction rule |
| `format-enum-anchor` | FormatEnum — Anchor | anchor | foundational | Declares the complete FormatEnum: valid output format values, required field structures, and validator compatibility rules |

---

## 12. index-suite

**Group ID:** `index-suite`
**Layer Affinity:** `meta`
**Description:** All index-role modules — organized registries for navigating specific regions of the system. The master registry index is the closest thing the system has to a comprehensive table of contents. Group-level indexes provide focused entry points for their domain. Navigate here when you know the domain but not the specific module, or when exploring a new region of the system for the first time.

| ID | Label | Role | Layer | Scope |
|----|-------|------|-------|-------|
| `index-master-registry` | Master Registry Index | index | meta | Master index of all 118 modules: sorted by group, with ID, label, role, layer, and one-line scope per entry |
| `index-core-engine` | Index — Core Engine | index | meta | Navigational index of the core-engine group: module list, recommended reading order, and entry-point guidance |
| `index-session-grammar` | Index — Session Grammar | index | meta | Navigational index of the session-grammar group: field module list, initialization order, and field cross-references |
| `index-clarity-system` | Index — Clarity System | index | meta | Navigational index of the clarity-system group: module list, evaluation sequence, and theorem cross-reference |
| `index-operator-suite` | Index — Operator Suite | index | meta | Navigational index of the operator-suite group: operator list, invocation syntax references, and chain pattern cross-references |
| `index-protocol-suite` | Index — Protocol Suite | index | meta | Navigational index of the protocol-suite group: protocol list, trigger conditions, and session-grammar cross-references |
| `index-validator-suite` | Index — Validator Suite | index | meta | Navigational index of the validator-suite group: validator list, applicable output formats, and clarity-system cross-references |
| `index-by-role` | Cross-Group Index by Role | index | meta | Cross-group index of all modules organized by role: every module of each role type listed together regardless of group |

---

## Master Alphabetical Index

All 118 modules, sorted alphabetically by ID, with label and group.

| ID | Label | Group |
|----|-------|-------|
| `active-modules-closure-val` | Active Modules Closure Validator | validator-suite |
| `active-modules-test-op` | Active Modules Field Test Operator | operator-suite |
| `bridge-grammar-to-manifest` | Bridge — Grammar → Manifest | bridge-suite |
| `bridge-lens-to-rtt` | Bridge — Lens → RTT | bridge-suite |
| `bridge-map-to-navigation` | Bridge — Map → Navigation | bridge-suite |
| `bridge-module-to-registry` | Bridge — Module → Registry | bridge-suite |
| `bridge-operator-to-validator` | Bridge — Operator → Validator | bridge-suite |
| `bridge-protocol-to-session` | Bridge — Protocol → Session | bridge-suite |
| `bridge-rtt-to-session` | Bridge — RTT → Session | bridge-suite |
| `bridge-session-to-clarity` | Bridge — Session → Clarity | bridge-suite |
| `canon-anchor-attribution` | Canon Anchor — Honest Attribution | anchor-suite |
| `canon-anchor-clarity-standard` | Canon Anchor — Clarity Standard | anchor-suite |
| `canon-anchor-module-unit` | Canon Anchor — Module as Unit | anchor-suite |
| `canon-anchor-rtt-engine` | Canon Anchor — RTT as Engine | anchor-suite |
| `canon-anchor-session-unit` | Canon Anchor — Session as Unit | anchor-suite |
| `chain-val` | Chain Validator | validator-suite |
| `chain-validate-op` | Chain Validation Operator | operator-suite |
| `clarity-anchor-standard` | Clarity Standard — Anchor | clarity-system |
| `clarity-grammar-validator-assessment` | Clarity Grammar — ValidatorAssessment | clarity-system |
| `clarity-lens-signal-coherence` | Clarity Lens — Signal Coherence | clarity-system |
| `clarity-map-validator-pulse-anatomy` | Clarity Map — Validator Pulse Anatomy | clarity-system |
| `clarity-op-spectral` | Clarity Operator — Spectral | clarity-system |
| `clarity-val-rtt-output` | Clarity Validator — RTT Output | clarity-system |
| `clarity-val-session-output` | Clarity Validator — Session Output | clarity-system |
| `conflict-detect-op` | Conflict Detection Operator | operator-suite |
| `conflict-resolve-proto` | Conflict Resolution Protocol | protocol-suite |
| `dependency-audit-proto` | Dependency Audit Protocol | protocol-suite |
| `dependency-trace-op` | Dependency Trace Operator | operator-suite |
| `dependency-val` | Dependency Validator | validator-suite |
| `failure-mode-recover-proto` | Failure Mode Recovery Protocol | protocol-suite |
| `format-check-op` | Format Check Operator | operator-suite |
| `format-enum-anchor` | FormatEnum — Anchor | anchor-suite |
| `format-val` | Format Validator | validator-suite |
| `gap-fill-proto` | Gap Filling Protocol | protocol-suite |
| `gap-identify-op` | Gap Identification Operator | operator-suite |
| `group-create-proto` | Group Creation Protocol | protocol-suite |
| `index-by-role` | Cross-Group Index by Role | index-suite |
| `index-clarity-system` | Index — Clarity System | index-suite |
| `index-core-engine` | Index — Core Engine | index-suite |
| `index-master-registry` | Master Registry Index | index-suite |
| `index-operator-suite` | Index — Operator Suite | index-suite |
| `index-protocol-suite` | Index — Protocol Suite | index-suite |
| `index-session-grammar` | Index — Session Grammar | index-suite |
| `index-validator-suite` | Index — Validator Suite | index-suite |
| `input-prepare-op` | Input Preparation Operator | operator-suite |
| `input-unit-grammar` | InputUnit Grammar | grammar-suite |
| `intent-test-op` | Intent Field Test Operator | operator-suite |
| `intent-val` | Intent Fulfillment Validator | validator-suite |
| `invocation-val` | Invocation Validator | validator-suite |
| `layer-enum-anchor` | Layer Enum — Anchor | anchor-suite |
| `lens-abstraction-level` | Abstraction Level Lens | lens-suite |
| `lens-causal` | Causal Lens | lens-suite |
| `lens-dependency` | Dependency Lens | lens-suite |
| `lens-intervention` | Intervention Lens | lens-suite |
| `lens-resolution-depth` | Resolution Depth Lens | lens-suite |
| `lens-scope-boundary` | Scope Boundary Lens | lens-suite |
| `lens-spectral-clarity` | Spectral Clarity Lens | lens-suite |
| `lens-stakeholder` | Stakeholder Lens | lens-suite |
| `lens-temporal` | Temporal Lens | lens-suite |
| `lens-version` | Version Provenance Lens | lens-suite |
| `manifest-complete-val` | Manifest Completeness Validator | validator-suite |
| `map-book-structure` | Map — Book Structure | map-suite |
| `map-canon-constraint-model` | Map — Canon Constraint Model | map-suite |
| `map-clarity-evaluation` | Map — Clarity Evaluation | map-suite |
| `map-dependency-graph` | Map — Dependency Graph | map-suite |
| `map-failure-mode-recovery` | Map — Failure Mode Recovery | map-suite |
| `map-group-relationships` | Map — Group Relationships | map-suite |
| `map-module-registry` | Map — Module Registry | map-suite |
| `map-operator-chain-patterns` | Map — Operator Chain Patterns | map-suite |
| `map-reader-journey` | Map — Reader Journey | map-suite |
| `map-role-layer-space` | Map — Role × Layer Space | map-suite |
| `map-rtt-pass-anatomy` | Map — RTT Pass Anatomy | map-suite |
| `map-session-lifecycle` | Map — Session Lifecycle | map-suite |
| `module-author-op` | Module Authoring Operator | operator-suite |
| `module-author-proto` | Module Authoring Protocol | protocol-suite |
| `module-id-grammar` | Module ID Grammar | grammar-suite |
| `module-id-val` | Module ID Validator | validator-suite |
| `module-manifest-grammar` | Module Manifest Grammar | grammar-suite |
| `nawderian-theorem-validator-pulses` | Nawderian Theorem of Validator Pulses | clarity-system |
| `operator-invocation-grammar` | Operator Invocation Grammar | grammar-suite |
| `output-package-op` | Output Packaging Operator | operator-suite |
| `output-unit-grammar` | OutputUnit Grammar | grammar-suite |
| `pass-depth-extend-op` | Pass Depth Extension Operator | operator-suite |
| `registry-update-proto` | Registry Update Protocol | protocol-suite |
| `role-enum-anchor` | Role Enum — Anchor | anchor-suite |
| `rtt-anchor-definition` | RTT — Core Definition | core-engine |
| `rtt-lens-causal` | RTT Lens — Causal | core-engine |
| `rtt-lens-stakeholder` | RTT Lens — Stakeholder | core-engine |
| `rtt-lens-temporal` | RTT Lens — Temporal | core-engine |
| `rtt-map-pass-anatomy` | RTT Map — Pass Anatomy | core-engine |
| `rtt-op-core` | RTT Operator — Core | core-engine |
| `rtt-op-multi-domain` | RTT Operator — Multi-Domain | core-engine |
| `rtt-op-recursive-extension` | RTT Operator — Recursive Extension | core-engine |
| `scope-check-op` | Scope Check Operator | operator-suite |
| `scope-compliance-val` | Scope Compliance Validator | validator-suite |
| `scope-statement-grammar` | Scope Statement Grammar | grammar-suite |
| `scope-test-op` | Scope Field Test Operator | operator-suite |
| `scope-val` | Scope Validator | validator-suite |
| `session-close-proto` | Session Closing Protocol | protocol-suite |
| `session-field-test-op` | Session Field Test Operator | operator-suite |
| `session-grammar-anchor` | Session Grammar — Anchor | session-grammar |
| `session-grammar-complete-val` | Session Grammar Completeness Validator | validator-suite |
| `session-grammar-field-active-modules` | Session Field — active_modules | session-grammar |
| `session-grammar-field-input` | Session Field — input | session-grammar |
| `session-grammar-field-intent` | Session Field — intent | session-grammar |
| `session-grammar-field-layer-context` | Session Field — layer_context | session-grammar |
| `session-grammar-field-output-format` | Session Field — output_format | session-grammar |
| `session-grammar-field-role-context` | Session Field — role_context | session-grammar |
| `session-grammar-field-scope` | Session Field — scope | session-grammar |
| `session-grammar-field-session-id` | Session Field — session_id | session-grammar |
| `session-grammar-field-validator` | Session Field — validator | session-grammar |
| `session-grammar-proto-init` | Session Grammar — Initialization Protocol | session-grammar |
| `session-grammar-spec` | Session Grammar Specification | grammar-suite |
| `session-init-proto` | Session Initialization Protocol | protocol-suite |
| `session-record-val` | Session Record Validator | validator-suite |
| `session-resume-proto` | Session Resumption Protocol | protocol-suite |
| `validator-assessment-grammar` | ValidatorAssessment Grammar | grammar-suite |
| `version-increment-proto` | Version Increment Protocol | protocol-suite |

---

## Registry Metadata

| Field | Value |
|-------|-------|
| Total modules | 118 |
| Active modules | 118 |
| Draft modules | 0 |
| Deprecated modules | 0 |
| Registry version | 1.0.0 |
| Last updated | 2026-09-25 |
| Maintained by | Nawder Loswin |

> When the registry changes, the version stamp increments per the `version-increment-proto`. Always check the version stamp when returning to the registry after time away. The first thing to verify is whether any module you rely on has been incremented since your last session.

---

→ [Return to Book Index](./index)
→ [Browse the Canonical Session Library](./sessions)
→ [Contributing Guidelines](../contributing)

---

*TriadicFrameworks Book — `/docs/book/registry.md`*
*Authored by Nawder Loswin. AI-augmented authorship. All rights reserved.*
