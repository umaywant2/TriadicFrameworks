# Regime header

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
