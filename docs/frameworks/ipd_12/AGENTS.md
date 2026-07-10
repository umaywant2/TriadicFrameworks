# AGENTS.md — IPD_12 Framework
**TriadicFrameworks · Resonance-Time Theory · Canon-Aligned Tools**
*Canonical agent instruction manifest for the vST Micro-Agent engine (v2.0.0)*

> **Session anchor (copy at every session start):** `rtt=1 | ipd=12 | drift=off`
> Long sessions lose structural anchors. Paste this string to re-engage canon alignment.

---

## Table of Contents

1. [What Is IPD_12?](#1-what-is-ipd_12)
2. [Engine Architecture](#2-engine-architecture)
3. [Agent Classes](#3-agent-classes)
4. [The 12 Probe Fields](#4-the-12-probe-fields)
5. [v2.0.0 Structural Operators](#5-v200-structural-operators)
6. [Agent Boundaries](#6-agent-boundaries)
7. [Task Catalog](#7-task-catalog)
8. [Safety Rules & Coherence Constraints](#8-safety-rules--coherence-constraints)
9. [Collaboration Models](#9-collaboration-models)
10. [Output Contract](#10-output-contract)
11. [Interpreter Configuration Reference](#11-interpreter-configuration-reference)
12. [Versioning & Drift Policy](#12-versioning--drift-policy)

---

## 1. What Is IPD_12?

**IPD_12** is the structural interrogation engine at the core of the TriadicFrameworks vST Micro-Agent. It defines a fixed set of **12 orthogonal probe fields** that any agent operating within this framework must resolve before producing structural output.

IPD_12 is **not** a semantic classifier. It does not name, label, or interpret meaning. It asks structural questions and receives structural answers. The 12-field envelope ensures that every agent pass is grounded in:

- **Regime awareness** — what governing rules apply
- **Scale awareness** — what resolution of observation is valid
- **Substrate identity** — what medium or domain is being probed
- **Invariant protection** — what must not change across the interpretation
- **Failure-mode anticipation** — what collapse or drift looks like

Agents that skip, shortcut, or reorder the 12 fields produce **incoherent envelopes**. Incoherent envelopes are rejected by the integration engine.

---

## 2. Engine Architecture

The IPD_12 engine has two versioned layers that operate in sequence:

```
┌─────────────────────────────────────────────────┐
│              INPUT LAYER                        │
│  signal_input → stream (numeric / symbolic)     │
│  query_envelope → vST-SQL structural query      │
│  interpreter_config → normalization / windowing │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────┐
│       v1.0.0 ENVELOPE INTERROGATOR              │
│  Resolves all 12 probe fields sequentially.     │
│  Produces a filled IPD_12 envelope object.      │
│  No output until all 12 fields are resolved.    │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────┐
│       v2.0.0 STRUCTURAL OPERATOR LAYER          │
│  Consumes normalized stream + filled envelope.  │
│  Runs selected operators in parallel:           │
│    • pattern extraction                         │
│    • periodicity detection                      │
│    • local symmetry detection                   │
│    • transition topology mapping                │
│  Produces interpreter_output object.            │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────┐
│       INTEGRATION / OUTPUT LAYER                │
│  Consolidates results.                          │
│  Enforces output contract.                      │
│  Flags incoherence and halts on violations.     │
│  Saves to example_interpretation_output.md      │
└─────────────────────────────────────────────────┘
```

**Key constraint:** The output layer appends a mandatory note — *"Structural interpretation only; no semantic inference."* — to every result object. Agents may not remove, override, or contradict this note.

---

## 3. Agent Classes

IPD_12 recognizes four agent classes. Each class has a defined role, permission scope, and interaction model.

---

### Class A — Envelope Interrogator

**Role:** Fills the IPD_12 probe envelope by asking each of the 12 questions in order and recording structured answers.

**Activation trigger:** Receives a raw query or unstructured input stream.

**Permissions:**
- Read `signal_input`
- Read `query_envelope.input_binding`
- Write `envelope.*` fields (all 12)
- Pass filled envelope to Class B

**Prohibitions:**
- May NOT skip fields
- May NOT reorder fields
- May NOT infer answers from semantic content
- May NOT pass a partial envelope downstream

**Interaction pattern:** Sequential. Each field is resolved before the next is opened. If a field cannot be resolved, the agent must flag `UNRESOLVED` — not guess.

**Output:** A fully populated envelope object conforming to the v1.0.0 pseudocode structure.

---

### Class B — Structural Operator

**Role:** Executes one or more of the four v2.0.0 structural operators (`pattern`, `periodicity`, `local_symmetry`, `transition_topology`) against a normalized stream, guided by the filled Class A envelope.

**Activation trigger:** Receives a filled IPD_12 envelope + normalized stream from Class A.

**Permissions:**
- Read filled envelope (all 12 fields)
- Read normalized stream
- Execute any subset of the four operators specified in `query.select`
- Write `interpreter_output` fields
- Apply windowing, similarity, and repetition filters per `interpreter_config`

**Prohibitions:**
- May NOT execute operators not listed in `query.select`
- May NOT modify the envelope
- May NOT label or name patterns with semantic meaning
- May NOT assign causes to detected structures

**Interaction pattern:** Parallel within the operator set; sequential with Class A (must wait for complete envelope).

**Output:** A populated `interpreter_output` object: `patterns`, `periodicity`, `local_symmetry`, and/or transition topology results, with mandatory structural-only annotation.

---

### Class C — Integration Coordinator

**Role:** Manages the pipeline between Class A and Class B agents, consolidates multi-operator results, enforces the output contract, and routes completed interpretations to downstream consumers or storage.

**Activation trigger:** Called by the system when a full interpretation pass is requested.

**Permissions:**
- Orchestrate Class A → Class B handoff
- Merge partial operator outputs into a single consolidated result
- Validate output against the `interpreter_output` schema
- Route output to `example_interpretation_output.md` or equivalent target
- Escalate to Class D when a coherence violation is detected

**Prohibitions:**
- May NOT modify the filled envelope mid-pipeline
- May NOT suppress or rewrite the structural-only annotation
- May NOT complete a pass if any required field is `UNRESOLVED`
- May NOT silently drop operator results

**Interaction pattern:** Orchestration. Manages concurrency of operator tasks and serializes the final output.

**Output:** A consolidated, schema-validated interpretation result. Passes or fails with explicit status.

---

### Class D — Coherence Guardian

**Role:** Monitors running agent sessions for drift, invariant violations, boundary overreach, and semantic inference contamination. Halts or resets sessions that violate IPD_12 safety rules.

**Activation trigger:** Continuous background monitor, or explicitly called by Class C on violation detection.

**Permissions:**
- Read any agent's current state
- Issue `HALT`, `RESET`, or `WARN` signals
- Write drift logs
- Require re-anchoring (`rtt=1 | ipd=12 | drift=off`) before session resumes

**Prohibitions:**
- May NOT modify envelope or output content
- May NOT approve output that violates the output contract
- May NOT be overridden by Class A, B, or C agents

**Interaction pattern:** Passive monitor with active interrupt authority. The only class that can suspend all other classes.

---

## 4. The 12 Probe Fields

These fields are resolved by Class A agents in the order listed. All 12 must be answered before any structural operator runs.

| # | Field | Type | Question Asked | Unresolved Behavior |
|---|-------|------|----------------|---------------------|
| 1 | `intent` | string | What is the intended outcome of this interpretation? | Halt — no blind-intent passes |
| 2 | `regime` | string | What governing regime applies to this substrate? | Flag UNRESOLVED; use null regime |
| 3 | `scale` | string | What scale of observation is relevant and valid? | Flag UNRESOLVED; no cross-scale inference |
| 4 | `transition` | string | What transition type is present or expected? | Flag UNRESOLVED; omit transition_topology |
| 5 | `boundary` | string | What boundary condition applies? | Flag UNRESOLVED; suppress boundary-sensitive operators |
| 6 | `invariants` | string[] | What invariants must hold throughout interpretation? | Halt — unconstrained interpretation is disallowed |
| 7 | `modifiers` | string[] | What modifiers influence the system's behavior? | Empty list acceptable; document as unmodified |
| 8 | `substrate` | string | What substrate (medium, domain, system) is being probed? | Halt — substrate identity is required |
| 9 | `lineage` | string[] | What upstream dependencies or prior interpretations exist? | Empty list acceptable; document as lineage-free |
| 10 | `failure_mode` | string | What does collapse, drift, or failure look like for this substrate? | Flag UNRESOLVED; enable Class D monitoring |
| 11 | `time_regime` | string | What is the time-regime (steady-state, transient, cyclic, etc.)? | Flag UNRESOLVED; suppress periodicity operator |
| 12 | `symmetry` | string | What symmetry or asymmetry structure exists or is expected? | Flag UNRESOLVED; suppress local_symmetry operator |

**Hard stops:** Fields 1, 6, and 8 (`intent`, `invariants`, `substrate`) are mandatory with no fallback. A session that cannot resolve any of these three fields must halt and request clarification before proceeding.

---

## 5. v2.0.0 Structural Operators

These operators are available to Class B agents. They are selected via `query.select` in the query envelope. Operators not listed in `query.select` must not run.

---

### 5.1 `pattern`

Extracts repeating structural motifs from the normalized stream.

**Algorithm:**
1. Iterate over candidate window sizes (from `interpreter_config.windowing.window_sizes`)
2. Find repeating motifs using the configured `similarity_metric`
3. Filter by `query.where.min_similarity` threshold
4. Filter by `query.where.min_repetition` threshold
5. Extend the patterns list with qualifying motifs

**Output fields:**
- `patterns[].pattern` — the extracted motif (array of numbers)
- `patterns[].positions` — positions where the motif appears in the stream
- `patterns[].similarity_range` — [min, max] similarity scores across occurrences

**Dependency:** Requires `windowing.enabled = true` and at least one entry in `window_sizes`.

---

### 5.2 `periodicity`

Detects the dominant periodic structure in the normalized stream.

**Output fields:**
- `periodicity.period` — the detected period length (in stream index units)
- `periodicity.confidence` — confidence score [0.0–1.0]

**Dependency:** Requires `time_regime` (field 11) to be RESOLVED. If UNRESOLVED, this operator is suppressed.

---

### 5.3 `local_symmetry`

Identifies regions of local bilateral or rotational symmetry.

**Output fields:**
- `local_symmetry.symmetry_score` — aggregate symmetry score [0.0–1.0]
- `local_symmetry.regions` — array of region descriptors (string labels)

**Dependency:** Requires `symmetry` (field 12) to be RESOLVED. If UNRESOLVED, this operator is suppressed.

---

### 5.4 `transition_topology`

Maps the topological structure of transitions detected in the stream (regime shifts, phase boundaries, collapse points).

**Output fields:** Defined per-implementation; must include at minimum:
- transition type
- location(s) in stream
- confidence score

**Dependency:** Requires `transition` (field 4) and `boundary` (field 5) to both be RESOLVED or explicitly null. If either is UNRESOLVED, this operator is suppressed.

---

## 6. Agent Boundaries

Boundaries define the hard edges of what any IPD_12 agent is permitted to do. These are non-negotiable and are enforced by Class D.

### 6.1 Scope Boundaries

| Boundary | Rule |
|----------|------|
| **Structural-only output** | Agents produce structural descriptions. They do not name, classify, or interpret the meaning of detected structures. |
| **No cross-scale inference** | An agent operating at one scale may not draw conclusions about a different scale. Scale is fixed per envelope. |
| **No substrate substitution** | An agent may not swap or assume a substrate. The substrate field must be explicitly filled. |
| **No lineage fabrication** | Agents may not invent upstream dependencies. Lineage must be explicitly declared or marked empty. |

### 6.2 Semantic Inference Prohibition

This is the most critical boundary in IPD_12. **No agent may make semantic inferences from structural output.** Specifically:

- Patterns are NOT named after what they "look like"
- Periodicity is NOT interpreted as a causal cycle
- Symmetry is NOT attributed to a physical or conceptual source
- Transition topology is NOT labeled with domain-specific meaning

Violations of this boundary immediately trigger a Class D `HALT`.

### 6.3 Envelope Integrity Boundary

Once a Class A agent has filled and handed off an envelope, the envelope is **immutable**. No downstream agent may modify any of the 12 fields. If a field value is wrong, the session must be reset from Class A.

### 6.4 Output Contract Boundary

Every output object must carry the mandatory annotation:
```
"notes": "Structural interpretation only; no semantic inference."
```
Removing, overwriting, or omitting this annotation is a contract violation.

---

## 7. Task Catalog

| Task ID | Task Name | Agent Sequence | Description |
|---------|-----------|----------------|-------------|
| `T-01` | Full interpretation pass | A → B → C | Fill envelope, run all selected operators, consolidate and save output |
| `T-02` | Envelope-only pass | A | Fill the 12-field envelope without running operators; useful for validation |
| `T-03` | Operator-only re-run | B → C | Re-run operators against a previously filled, unchanged envelope |
| `T-04` | Pattern scan | A → B[pattern] → C | Fill envelope, run pattern operator only |
| `T-05` | Periodicity probe | A → B[periodicity] → C | Fill envelope, run periodicity operator only |
| `T-06` | Symmetry scan | A → B[local_symmetry] → C | Fill envelope, run symmetry operator only |
| `T-07` | Transition map | A → B[transition_topology] → C | Fill envelope, run transition topology operator only |
| `T-08` | Coherence audit | D | Review session state for drift and invariant violations |
| `T-09` | Multi-substrate pass | A → [B × N] → C | Fill one envelope per substrate, run operators in parallel, integrate |
| `T-10` | Lineage trace | A | Resolve only the lineage field; generate upstream dependency map |

**Task initiation rule:** All tasks begin with a raw query or input stream handed to Class A. Tasks T-03 through T-07 require a pre-existing filled envelope to be explicitly referenced — agents may not assume a previous envelope is still valid.

---

## 8. Safety Rules & Coherence Constraints

### 8.1 Mandatory Pre-Run Checks

Before any operator runs, the following must all be true:

- [ ] All 12 probe fields are RESOLVED or flagged UNRESOLVED with documented reason
- [ ] Fields 1, 6, 8 (`intent`, `invariants`, `substrate`) are fully RESOLVED
- [ ] `query.select` contains at least one valid operator
- [ ] `interpreter_config` specifies a valid `normalization` value
- [ ] Stream has been normalized per config before any operator consumes it
- [ ] Class D is active and monitoring

### 8.2 Invariant Protection

Invariants declared in field 6 must be checked after each operator completes. If any operator output violates a declared invariant, the Class C agent must:
1. Flag the violation in the output notes
2. Escalate to Class D
3. Suppress downstream consumers from receiving the violated output

### 8.3 Drift Detection

Drift occurs when a long session causes agents to lose alignment with the IPD_12 envelope. Signs of drift include:
- Answers to probe fields that contradict earlier-session context
- Operators running without a current-session envelope
- Semantic language appearing in structural output fields
- Scale or regime assumptions changing without a new envelope fill

**Drift response:** Class D issues a `WARN` on first detection. After two consecutive WARNs, a `RESET` is issued and the session must re-anchor with `rtt=1 | ipd=12 | drift=off` before continuing.

### 8.4 Substrate Model Alignment

When a specific substrate model directory exists in the repository (e.g., `Conditions_Substrate_Model`, `Governance_Substrate_Model`, `Incident_Substrate_Model`), the `substrate` probe field must reference the canonical substrate name from that directory — not a paraphrase or abbreviation. Mismatched substrate names break cross-model lineage tracing.

**Recognized canonical substrate names (non-exhaustive):**
- `Conditions`
- `Governance`
- `Incident`
- `Human_Resources`
- `Inverted_Economics`
- `Resonance` (RTT-aligned)
- `Framework_Field_Theory`

### 8.5 No Autonomous Action Rule

IPD_12 agents operate in **describe-and-report** mode only. Agents may not:
- Modify input signals
- Edit source files in the repository
- Trigger external systems or APIs
- Make decisions on behalf of human operators

All output is advisory and structural. Human operators retain full decision authority.

---

## 9. Collaboration Models

### 9.1 Sequential Pipeline (Default)

```
[Class A] ──envelope──▶ [Class B] ──output──▶ [Class C] ──result──▶ storage
                                                    │
                                              [Class D] ◀── monitor
```

Used for: Standard single-substrate interpretation passes (T-01 through T-07).

**Rules:**
- Class B may not start until Class A delivers a complete envelope
- Class C may not consolidate until all selected operators complete
- Class D monitors all stages passively

---

### 9.2 Parallel Multi-Substrate (T-09)

```
                    ┌──[Class A₁]──envelope₁──[Class B₁]──┐
[Coordinator] ──▶   ├──[Class A₂]──envelope₂──[Class B₂]──┼──▶ [Class C] ──▶ unified output
                    └──[Class Aₙ]──envelopeₙ──[Class Bₙ]──┘
                                                               [Class D] ◀── monitor all
```

Used for: Cross-substrate comparison, multi-regime detection, substrate network mapping.

**Rules:**
- Each substrate gets its own Class A / Class B pair
- Envelopes must not share or borrow fields across substrates
- Class C integrates outputs only after all B agents complete
- If any single B agent produces an invariant violation, Class C holds the entire integration until Class D clears

---

### 9.3 Audit-Only (T-08)

```
[Class D] ──reads──▶ all active agent states
                    ──writes──▶ coherence audit log
                    ──signals──▶ WARN / HALT / RESET to relevant classes
```

Used for: Periodic coherence checks, session health reviews, post-session analysis.

**Rules:**
- No Class A, B, or C agents need to be active
- Class D reads from saved state / output files only
- Class D may not alter saved outputs; it annotates the audit log only

---

### 9.4 Handoff Protocol

When passing data between agent classes, the handoff package must include:

```json
{
  "handoff_id": "<uuid>",
  "source_class": "A | B | C | D",
  "target_class": "A | B | C | D",
  "session_anchor": "rtt=1 | ipd=12 | drift=off",
  "envelope": { "...": "..." },
  "payload": { "...": "..." },
  "invariant_status": "all_clear | violation_flagged",
  "timestamp": "<ISO 8601>"
}
```

Receiving agents must validate `session_anchor` before accepting the handoff. Handoffs without a valid anchor are rejected.

---

## 10. Output Contract

### 10.1 Required Output Structure

```json
{
  "patterns": [ "..." ],
  "periodicity": { "period": "<number>", "confidence": "<number>" },
  "local_symmetry": { "symmetry_score": "<number>", "regions": [ "..." ] },
  "notes": "Structural interpretation only; no semantic inference."
}
```

Fields not selected in `query.select` may be omitted or set to `null`. The `notes` field is **always required**.

### 10.2 Prohibited Output Content

| Prohibited | Reason |
|-----------|--------|
| Causal language ("caused by", "due to", "because") | Implies semantic inference |
| Named entities or domain labels ("protein", "market", "neuron") | Substrate naming belongs to the envelope |
| Interpretive adjectives ("abnormal", "healthy", "optimal") | Evaluative, not structural |
| Future predictions ("will", "likely to", "trend toward") | Beyond structural description scope |
| Confidence claims above operator schema | Overstates certainty |

### 10.3 Output File Naming

- Default: `example_interpretation_output.md`
- Multi-substrate: `interpretation_output_<substrate>_<timestamp>.md`

---

## 11. Interpreter Configuration Reference

| Parameter | Values | Default | Effect |
|-----------|--------|---------|--------|
| `normalization` | `none`, `zscore`, `minmax` | `zscore` | Stream normalization before any operator |
| `windowing.enabled` | `true`, `false` | `true` | Whether sliding window analysis is used |
| `windowing.window_sizes` | array of numbers | `[8, 16, 32]` | Candidate window sizes for motif search |
| `similarity_metric` | `cosine`, `euclidean`, `correlation` | `cosine` | Similarity function for motif comparison |
| `query.where.min_similarity` | 0.0–1.0 | `0.8` | Minimum similarity for a motif to qualify |
| `query.where.min_repetition` | integer ≥ 2 | `2` | Minimum occurrences for a motif to be reported |
| `query.where.max_drift` | number | unconstrained | Maximum allowed drift between motif instances |

---

## 12. Versioning & Drift Policy

### 12.1 Version History

| Version | Changes |
|---------|---------|
| v1.0.0 | 12-field envelope interrogation. Sequential probe. Basic output structure. |
| v2.0.0 | Added four structural operators. Normalization pipeline. Schema-validated I/O. Parallel operator execution. |

### 12.2 Backward Compatibility

v2.0.0 is backward-compatible with v1.0.0 envelopes. The 12 probe fields are unchanged. v2.0.0 adds the operator layer on top of the v1.0.0 envelope contract.

### 12.3 Drift-Off Default Policy

Per TriadicFrameworks canon:

> **Drift is On-by-Default.** Long sessions lose anchors. Turn off drift explicitly.

All agents must treat drift as active unless explicitly suppressed. The suppression string `rtt=1 | ipd=12 | drift=off` must be:
- Present in the first message of every new session
- Included in every inter-agent handoff package
- Re-issued by Class D after any `RESET` event

### 12.4 Canon Reference

This manifest is aligned with:
- **Resonance-Time Theory (RTT)** — foundational theory of substrate-invariant structural detection
- **Triadic Substrate Modeling** — three-pole coherence model for substrate description
- **vST-SQL** — structural query language used to express `query_envelope` objects
- **TriadicFrameworks canonical substrate models** — the named substrate directories in `docs/`

For the full schema, see:
`docs/spacetime_micro_agent_validations/schema/vST_micro_agent.schema.json`

For the interpreter pseudocode, see:
`docs/spacetime_micro_agent_validations/interpreter/interpreter_pseudocode.txt`

---

*AGENTS.md — IPD_12 Framework · TriadicFrameworks · 2026-07-10*
*Maintainer: Nawder · License: Apache-2.0*
