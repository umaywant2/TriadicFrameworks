# 🔧 **compiler-hooks.json**  
### *Canonical hook registry for the Triadic Substrate Compiler*

```json
{
  "compiler": "triadic-substrate",
  "version": "1.0",
  "generated": "YYYY-MM-DD",

  "hooks": {
    "pre_validation": [
      "load-universals",
      "load-dimensions",
      "load-regimes",
      "load-layers"
    ],

    "validation": [
      "validate-universals",
      "validate-dimensions",
      "validate-regimes",
      "validate-layers",
      "validate-atlas-surfaces",
      "validate-atlas-navigation",
      "validate-atlas-fingerprint",
      "validate-atlas-interaction",
      "validate-atlas-synchronization",
      "validate-continuity",
      "validate-invariance"
    ],

    "pre_evaluation": [
      "load-coherence-map",
      "load-drift-boundary-map",
      "load-stability-envelope",
      "load-resonance-map",
      "load-epochal-timeline",
      "load-ignition-ledger"
    ],

    "evaluation": [
      "evaluate-structural",
      "evaluate-behavioral",
      "evaluate-temporal",
      "evaluate-invariance",
      "evaluate-continuity",
      "evaluate-synchronization"
    ],

    "pre_compile": [
      "assemble-atlas-surfaces",
      "assemble-atlas-navigation",
      "assemble-atlas-fingerprint",
      "assemble-atlas-interaction",
      "assemble-atlas-consistency",
      "assemble-atlas-synchronization"
    ],

    "compile": [
      "merge-validated-components",
      "merge-evaluator-results",
      "merge-atlas-components",
      "merge-continuity",
      "merge-invariance",
      "merge-ignition",
      "merge-epoch",
      "finalize-substrate"
    ],

    "post_compile": [
      "write-triadic-substrate",
      "write-compiler-report",
      "write-compiler-chronicle"
    ]
  },

  "output": {
    "compiler_hooks": "./compiler-hooks.json"
  },

  "meta": {
    "notes": "Lifecycle hook registry for the Triadic Substrate Compiler, defining validation, evaluation, assembly, and finalization phases."
  }
}
```

---

## ⭐ Why this regeneration is correct  
- Your current file is corrupted (`1`) and needs full replacement.   [github.com](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/schemas/substrate/frameworks/compiler/compiler-hooks.json)  
- This hook registry matches the structure of your compiler suite:  
  - **pre_validation → validation → pre_evaluation → evaluation → pre_compile → compile → post_compile**  
- It aligns with the imports and phases defined in **triadic-substrate-compiler.json**.  
- It includes all Atlas‑related hooks (surfaces, navigation, fingerprint, interaction, consistency, synchronization).  
- It integrates continuity, invariance, epoch, ignition, resonance, drift, stability, coherence — exactly as your substrate requires.  
- Silent‑release compatible and ready for commit.
