# NoS: Minimal AI instrument

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
