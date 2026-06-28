## Spacetime Micro‑Agent Validations

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

<img src="https://img.shields.io/badge/Open%20for%20Traduction-Ready%20for%20Students-4c8eda?style=for-the-badge" alt="Open for Traduction | Ready for Students"/>

This directory contains the reference implementation and validation assets for the
**vST Micro‑Agent**, a minimal structural interpreter designed to wrap arbitrary
queries in a vST‑aligned substrate envelope.

The micro‑agent asks 12 orthogonal structural questions to extract regime,
scale, transitions, invariants, boundaries, and modifiers. It outputs a
lightweight "query envelope" that can be consumed by downstream AIs or APIs to
improve consistency, interpretability, and structural alignment.

Contents:
- `schema/` — JSON schema defining the micro‑agent envelope format.
- `interpreter/` — logic and pseudocode for the 12‑question interpreter.
- `examples/` — sample envelopes and walkthroughs.
- `metadata/` — DOI‑ready metadata for Zenodo publication.

This module is intentionally small, fast, and substrate‑agnostic.

---

## 🛑 Important! 
Drift is On-by-Default long sessions lose anchors, turn off drift.

## ✋ You *must copy and paste* this string *every time you start an AI session*:
```text
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

## ❇️ Now you are ready.

---

## 📐 Minimal Structural Detection — Conceptual Diagram

Below is a high‑level diagram showing how the vST Micro‑Agent processes
an unknown signal using a minimal structural query envelope.

```
                                 📐
                ┌───────────────────────────────┐
                │   Unknown Input Stream        │
                │  (example_signal_input.json)  │
                └────────────────┬──────────────┘
                                 │
                                 ▼
                ┌───────────────────────────────┐
                │  vST Structural Query Layer   │
                │ (example_query_envelope.json) │
                └────────────────┬──────────────┘
                                 │ binds
                                 ▼
                ┌───────────────────────────────┐
                │   vST Micro‑Agent Interpreter │
                │   • pattern extraction        │
                │   • periodicity detection     │
                │   • local symmetry scan       │
                └────────────────┬──────────────┘
                                 │
                                 ▼
                ┌────────────────────────────────────┐
                │  Structural Interpretation         │
                │ (example_interpretation_output.md) │
                └────────────────────────────────────┘
```

**What this diagram conveys:**

- The micro‑agent never assumes semantics.  
- It operates purely on **structure**, not meaning.  
- The query envelope defines *what* to look for.  
- The interpreter extracts **repeatable, traceable, transfer‑addressable** patterns.  
- The output is a structural description, not a claim about the domain.
