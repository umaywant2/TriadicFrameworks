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
