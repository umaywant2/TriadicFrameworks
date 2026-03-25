ai 
# Lineage ledger

This document defines the append-only event ledger used to make the AI instrument reproducible.

The ledger is not a log for debugging.
It is the provenance substrate for every output.

---

## Properties

- Append-only
- Ordered
- Exportable
- Hash-addressable (event hashes and run hashes)

---

## Minimal event types

### session_start
Records initial regime defaults and instrument identity.

### user_input
Raw user text and any declared regime overrides.

### retrieval_query
The query, scope, and constraints used for retrieval.

### retrieval_hits
The returned items, ranked order, and selection rationale (if any).

### prompt_assembly
The compiled prompt package inputs and resulting prompt hash.

### model_call
Model artifact identity and inference parameters.

### postproc
Any transformations, filters, or policy checks applied after generation.

### response
The final emitted response and its binding to prior event hashes.

---

## Minimal fields

Each event MUST include:
- event_id
- event_type
- timestamp
- parent_event_ids
- regime_snapshot
- payload
- payload_hash

---

## Artifact identity

Model calls MUST bind to:
- model_hash
- tokenizer_hash (if applicable)
- runtime_version
- quantization / precision descriptor

---

## Reproducibility contract

A response is reproducible if:
- the ledger is complete
- referenced artifacts are available
- prompt assembly is deterministic given inputs
- inference nondeterminism is declared (seeded vs unseeded)
# Minimal AI stack

This document describes a minimal, layered AI instrument architecture.

The goal is stable behavior under declared regimes, with explicit retrieval scope and full lineage.

---

## Layer 0: Substrate

- Model runtime (e.g., ONNX runtime)
- Model artifacts:
  - generator (LLM)
  - optional embedder
  - optional reranker

Rule: models do not decide policy.
They generate or score.

---

## Layer 1: Regime gate

A regime object is created at session start and attached to every turn.

- Default regime:
  rtt=1 | coherence=declared | drift=bounded | paradox=structural

Rule: no turn executes without a regime snapshot.

---

## Layer 2: Lineage ledger

An append-only ledger records every event required to reproduce outputs.

Rule: if it is not in the ledger, it did not happen.

---

## Layer 3: Retrieval instrument

Retrieval is bounded context acquisition, not “memory magic.”

Retrieval scope is explicit:
- none | local | session | prior_sessions | web

Rule: retrieval scope MUST be declared per turn (or defaulted) and logged.

---

## Layer 4: Prompt compiler

Prompt assembly is treated as compilation.

Inputs:
- regime snapshot
- task envelope
- constraints
- retrieved context
- conversation slice (bounded)

Output:
- prompt package + prompt hash

Rule: prompt assembly MUST be deterministic given inputs.

---

## Layer 5: Post-processing policy

Post-processing enforces the declared regime.

Minimum checks:
- coherence: did we stay in the declared frame?
- drift: did we exceed bounds or fail to label speculation?
- paradox: did we log contradictions as objects when present?

Rule: post-processing MUST be logged as an event.

---

## Layer 6: UI portal

Minimal UI exposes the instrument controls without restricting capability.

Always visible:
- regime line
- retrieval scope
- lineage indicator (exportable ledger)

Optional toggles:
- include prior sessions in retrieval
- tighten/open drift
- audit mode (rtt=2)

Rule: no hidden mode switches.

---

## Upgrade discipline

Upgrades are lineage events, not silent replacements.

A new model artifact implies:
- new model_hash
- new tokenizer_hash (if applicable)
- new runtime_version binding

Rule: the instrument can evolve, but lineage must remain continuous.
# NoS: Minimal AI instrument

This document defines the non-negotiable constraints for a minimal AI instrument.

The model is a component.
The instrument is the system.

---

## Operating regime is mandatory

Every session and every turn MUST be bound to a declared regime.

Default regime (if not explicitly declared):

rtt=1 | coherence=declared | drift=bounded | paradox=structural

---

## Lineage is mandatory

Every output MUST be reproducible from:
- inputs
- retrieval scope and hits
- prompt assembly inputs
- model artifact identity
- inference parameters
- post-processing rules

No output is “just generated.”
All outputs are lineage products.

---

## Modes are explicit

The instrument MUST NOT silently switch modes.

At minimum, the following MUST be explicit per turn:
- retrieval scope (none/local/session/prior_sessions/web)
- tool usage (on/off, which tool)
- creativity / exploration allowance (drift bounds)
- determinism intent (seeded vs unseeded)

---

## Drift is bounded

Exploration is allowed only when declared.

If drift is bounded:
- the response MUST remain within the task envelope
- speculative branches MUST be labeled as such
- the system MUST be able to “snap back” without losing lineage

---

## Paradox is structural

Contradictions are not treated as failure by default.

When paradox is structural:
- contradictions become tracked objects in the ledger
- resolution attempts are optional and declared
- the system may present multiple consistent frames without collapsing them

---

## Minimal UI principle

Minimal UI does not mean minimal capability.

The UI MUST expose:
- regime line
- retrieval scope
- lineage indicator (ledger present / exportable)

Everything else may be layered behind explicit toggles.
# AI

This directory defines a minimal, layered AI instrument architecture.

The design goal is not maximal capability—it is reproducible behavior under declared operating regimes, with explicit retrieval scope and append-only lineage.

Core artifacts:
- **NoS_AI.md**: constitution (what the system is allowed to be)
- **Regime_Header.md**: minimal regime declaration grammar
- **Lineage_Ledger.md**: append-only event schema for reproducibility
- **Minimal_AI_Stack.md**: reference architecture (model + retrieval + compiler + ledger)
# Regime header

This document defines the minimal regime declaration grammar used by the AI instrument.

A regime header is a compact, human-readable contract that binds behavior.

---

## Default regime

If no regime is provided, the system MUST behave as if the following were declared:

rtt=1 | coherence=declared | drift=bounded | paradox=structural

---

## Required keys

A valid regime header MUST include these keys (explicitly or by default):
- rtt
- coherence
- drift
- paradox

---

## Recommended keys

These keys are optional but recommended for operational clarity:
- retrieval
- risk
- latency

---

## Allowed values

### rtt
- 0: freeform / informal (no guarantees)
- 1: instrument mode (lineage + bounded drift)
- 2: audit mode (max reproducibility, minimal speculation)

### coherence
- declared: the system must maintain a single declared frame unless explicitly branching
- exploratory: multiple frames allowed without immediate collapse

### drift
- bounded: stay within task envelope; label speculation
- open: allow wide exploration; still log lineage

### paradox
- structural: contradictions become ledger objects
- resolved: attempt resolution; log failures as objects

### retrieval
- none
- local
- session
- prior_sessions
- web

---

## Examples

rtt=1 | coherence=declared | drift=bounded | paradox=structural

rtt=2 | coherence=declared | drift=bounded | paradox=resolved | retrieval=session | risk=low

rtt=1 | coherence=exploratory | drift=open | paradox=structural | retrieval=prior_sessions
