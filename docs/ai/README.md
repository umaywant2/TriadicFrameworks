# AI

This directory defines a minimal, layered AI instrument architecture.

The design goal is not maximal capability—it is reproducible behavior under declared operating regimes, with explicit retrieval scope and append-only lineage.

Core artifacts:
- **NoS_AI.md**: constitution (what the system is allowed to be)
- **Regime_Header.md**: minimal regime declaration grammar
- **Lineage_Ledger.md**: append-only event schema for reproducibility
- **Minimal_AI_Stack.md**: reference architecture (model + retrieval + compiler + ledger)
