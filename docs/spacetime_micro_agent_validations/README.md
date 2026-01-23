# Spacetime Micro‑Agent Validations

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
