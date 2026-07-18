# Minimal AI stack

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
