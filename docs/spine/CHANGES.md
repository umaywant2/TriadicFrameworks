# Spine semantic refresh — 2026-11-19

## Confirmed rule
Canon consists of modules with Operators and Nodes for RTT use, plus the owner's confirmed set: all earlier 47 candidates, Grammar, Principles and Lineage. Everything else remains viewable with the Spine but is kept apart from canon.

## What was inspected
All 698 attached JSON files were inspected. Every JSON file is a module manifest; there were no separate supporting JSON files in `spine_jsons.zip`.

For each record, the register now contains:
- operator-definition fields and extracted operator identities;
- explicit node fields and extracted node identities;
- RTT-use evidence;
- the nearest module parent and declared parent references;
- a matched R5/R5.1 graph node where available;
- canon/example regime and Spine/organ/limb/example placement.

Operator scores, file names, policies, counts and analyzed subjects such as data-center operators were not treated as operator definitions.

## Result
- Canon: 74
- Examples: 614
- Unreadable: 10
- Spine records confirmed from the supplied graph patches: 31
- Organs (canon outside those confirmed graph nodes): 43
- Limbs (non-canon RTT/structural descendants): 86
- Unattached examples: 528
- Unplaced unreadable records: 10

## Canon added by the semantic audit
- `Chosen_Ones/module.json`
- `corpus/corpus_module.json`
- `FFF_Gravity/FFF_Gravity_module.json`
- `MCP/L1_Frequency_Unseen/ai/ai.module.json`
- `MCP/L3_Forces_Unseen/spine/module.json`
- `Structural_Love/module.json`

These six manifests explicitly carry operator definitions and node definitions in RTT/canon context. Legacy `old.*` records were not promoted.

## Files
- `spine.json` — preserved canon triads and declared context; updated regime, body-position and AI traversal definitions.
- `module_register.json` — complete 698-record semantic register.
- `module_graph_patch_r52_examples.json` — owner-approved patch adding one navigation-only examples region; declared total becomes 198.

No source module manifest was edited, renamed or deleted.

## Remaining limit
The separately attached `module_graph.json` is byte-for-byte identical to the R5 patch already in `spine_copy.zip`: it contains 30 `nodes_additions`, not the full 196-node registry. Together with the R5.1 Clarity patch, only 31 Spine records can be confirmed by graph identity. The 43 organs are canon, but some may turn out to be Spine nodes if a complete registry exists elsewhere.
