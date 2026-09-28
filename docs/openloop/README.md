
- [`module.json`](https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/refs/heads/main/docs/openloop/module.json) — Agentic module schema role assignments

# TriadicFrameworks · Open Loop Suite

**Path:** `docs/openloop/`  
**Version:** 1.0.0  
**Author:** Nawder Loswin  
**Last reviewed:** 2026-09-27  
**Canonical URL:** https://www.triadicframeworks.org/docs/openloop/

---

## What this suite is

The Open Loop suite is a six-module, ring-structured framework for cross-domain AI operations. It defines:

- A **five-step operational loop** for every cross-domain action
- A **canonical operator grammar** for identity verification, risk classification, geospatial grounding, language normalization, parallel execution, and lineage indexing
- A **three-ring model** (Trust → Motion → Meaning) that governs pipeline order and accountability
- A **lineage store** that closes the loop: no operation is complete until OpenData indexes the lineage note

The suite is named `openloop` after the five-step loop — not after any external standard or protocol. The `Open*` prefix on each module (`OpenIAM`, `OpenRisk`, `OpenGeo`, `OpenLLM`, `OpenGPU`, `OpenData`) signals aperture: the module's signature, operators, drift surface, and lineage hooks are exposed to cross-domain inspection.

---

## Pipeline order

This is a pipeline, not a directory. Operations flow in this order:

| Step | Module | Verb | Domain | Ring |
|---|---|---|---|---|
| 1 | OpenIAM | VERIFY | Identity & Access Management | Trust |
| 2 | OpenRisk | CLASSIFY | Risk Regime Classification | Trust |
| 3 | OpenGeo | ANCHOR | Geospatial & Temporal Grounding | Motion |
| 4 | OpenLLM | NORMALIZE | Language Model Infrastructure | Motion |
| 5 | OpenGPU | SCHEDULE | Parallel Execution Substrate | Motion |
| 6 | OpenData | INDEX | Data Surface & Lineage Registry | Meaning |

---

## The five-step Open Loop

Every cross-domain operation runs this loop regardless of which module is active:

```
1. READ SIGNATURE      — confirm identity contract for this module
2. SCAN SIBLING META   — compare Open* modules for dimension_vector mismatches
3. CLASSIFY DRIFT      — assign drift type + severity via OpenRisk
4. APPLY OPERATOR      — execute canonical grammar: VERB(subject, target, [modifier])
5. WRITE LINEAGE       — INDEX note in lineage/<module>/<timestamp>.md via OpenData
```

Loop step 5 is mandatory. A loop that does not produce a lineage note is not closed.

---

## Operator grammar reference

All operators follow this canonical grammar:

```
VERB(subject, target, [modifier])
```

### Full operator table

| Verb | Module | Purpose |
|---|---|---|
| VERIFY | OpenIAM | Confirm identity and credential |
| REVOKE | OpenIAM | Invalidate credential immediately |
| DELEGATE | OpenIAM | Transfer access scope |
| ESCALATE | OpenIAM, OpenRisk | Elevate to human steward |
| ALIGN | all | Cross-domain signature reconciliation |
| CLASSIFY | OpenRisk | Assign T0–T3 risk tier |
| GATE | OpenRisk | Block operation pending required operator |
| ABSORB | OpenRisk | Contain bounded drift within current tier |
| PROPAGATE | OpenRisk, OpenGeo, OpenData | Broadcast context downstream |
| ANCHOR | OpenGeo | Establish spatial/temporal ground truth |
| OFFSET | OpenGeo | Apply displacement to existing anchor |
| PROJECT | OpenGeo | Transform coordinate reference system |
| NORMALIZE | OpenLLM | Standardize language model output |
| COLLAPSE | OpenLLM | Reduce semantic ambiguity |
| REFRAME | OpenLLM | Shift semantic frame to match target context |
| ANNOTATE | OpenLLM, OpenData | Attach semantic label or steward note |
| SCHEDULE | OpenGPU | Queue job for execution |
| PARTITION | OpenGPU | Split job into parallel workers |
| PIPELINE | OpenGPU | Chain execution stages |
| FLUSH | OpenGPU | Terminate job and release resources |
| INGEST | OpenData | Accept and validate artifact |
| VALIDATE | OpenData | Check schema conformance without committing |
| INDEX | OpenData | Write lineage note to store — closes the loop |

### Composition example

```
VERIFY(agent_007, access_chain)
  → FAIL (trust_score 0.55 < floor 0.70)
  → ESCALATE(agent_007, steward)
  → VERIFY(agent_007, access_chain)
  → PASS
  → CLASSIFY(operation, T1)
  → ANCHOR(operation, coordinates, temporal_ref)
  → NORMALIZE(payload, target_schema)
  → SCHEDULE(job, parallel)
  → INDEX(lineage/IAM/2026-09-26-001.md, IAM)
```

---

## Three rings

| Ring | Position | Concern | Primary modules |
|---|---|---|---|
| Trust | Innermost | Identity, governance, signature validity | OpenIAM, OpenRisk |
| Motion | Middle | Operator application, drift propagation, loop execution | OpenGeo, OpenLLM, OpenGPU |
| Meaning | Outer | Semantic coherence, output interpretation, cross-domain alignment | OpenData, OpenLLM |

---

## Coherence floors (declared)

These are declared operational floors — not empirically benchmarked values. A module below its floor will not accept a cross-domain payload without a GATE or ESCALATE from OpenRisk.

| Module | Floor | Notes |
|---|---|---|
| OpenIAM | 0.85 | Highest — Trust-ring anchor |
| OpenData | 0.82 | Second-highest — lineage record must be coherent |
| OpenRisk | 0.80 | Classification gate |
| OpenLLM | 0.78 | Generative surface |
| OpenGeo | 0.76 | Grounding layer |
| OpenGPU | 0.72 | Lowest — execution tolerates more variance |

---

## File structure

```
docs/openloop/
├── index.md            — Suite navigation hub, condensed drift event on first screen
├── index.html          — HTML front door with canonical head block
├── README.md           — This file
├── LLM.md              — OpenLLM surface
├── IAM.md              — OpenIAM surface (Trust anchor)
├── Risk.md             — OpenRisk surface
├── Geo.md              — OpenGeo surface
├── GPU.md              — OpenGPU surface
├── Data.md             — OpenData surface (loop terminal)
├── module.json         — Per-module manifest
├── modules.json        — Cross-suite registry of all Open* modules
├── quad.json           — Four-quadrant view by ring and regime
├── nav.json            — Suite navigation structure
└── sitemap.xml         — XML sitemap for search engines and AI crawlers

lineage/
├── LLM/
│   └── 2026-09-26-001.md   — LLM→IAM ALIGN drift event
├── IAM/
├── Risk/
├── Geo/
├── GPU/
└── Data/
```

---

## Setup

No build step required. All surface files are standalone Markdown. The HTML front door (`index.html`) uses no external dependencies.

### Verify canonical URLs

All files in this suite point to `https://www.triadicframeworks.org/`. Check these fields for correctness before publishing:

- `module.json` → `canonical_url`
- `modules.json` → module entries `canonical_url`
- `sitemap.xml` → all `<loc>` elements
- `index.html` → `<link rel="canonical">` and Open Graph `og:url`

Run a quick check from the repo root:

```bash
grep -r "triadicframeworks\.com" docs/openloop/
```

Any matches are bugs — the live domain is `.org`.

---

## Contribution guide

### Adding a new surface file

1. Create `docs/openloop/<ModuleName>.md` following the ten-section template in any existing surface file.
2. Add the module to `modules.json` with its `dimension_vector`, `coherence_threshold`, `operator_affinity`, and `rings`.
3. Add the module to `module.json` file list with its `role` and `analyzer_layer`.
4. Add a nav entry to `nav.json` with `url` (no `.md` extension).
5. Add a `<url>` block to `sitemap.xml`.
6. Add the module to `quad.json` under the appropriate quadrant and ring map.
7. Write a lineage note to `lineage/<ModuleName>/YYYY-MM-DD-001.md` and submit it for indexing via OpenData.

### Modifying a coherence floor

A coherence floor change is a MAJOR version event.

1. Write a lineage note explaining the change and rationale before any file is modified.
2. Update the floor in the surface `.md` §1 Identity table and §2 signature YAML.
3. Update `modules.json` `coherence_threshold`.
4. Update `quad.json` `coherence_spectrum`.
5. Increment the MAJOR version in all affected files.
6. Index the lineage note via OpenData.

### Modifying operator grammar

1. Update the operator table in the relevant surface `.md` §5.
2. Update `operator_affinity` in `modules.json`.
3. Update this README's operator table.
4. Write a lineage note and index it.

---

## Removing old subfolders

If you need to remove superseded subfolders (e.g., old per-module directories that have been consolidated into surface `.md` files), run from the repo root:

```bash
# Remove a specific subfolder
git rm -r docs/openloop/<subfolder>/
git commit -m "Remove superseded <subfolder> — consolidated into <Module>.md"

# Remove the old openapi suite root if switching from docs/openapi/ to docs/openloop/
git rm -r docs/openapi/
git commit -m "Remove docs/openapi/ — superseded by docs/openloop/ (suite rename 2026-09-27)"
```

Stamp the old root as legacy before removing it — write a lineage note at `lineage/<module>/YYYY-MM-DD-legacy.md` with `event_type: legacy_stamp`.

---

## Legacy note

The prior OpenWarden root (thirteen-module architecture) was stamped `legacy: true` on 2026-09-26. Redirect notice is active at the old URL. All new operations use the six-module `openloop` suite.

---

## License

Open educational use permitted. See `https://www.triadicframeworks.org/` for full terms.

---

*TriadicFrameworks · Open Loop Suite · README · v1.0.0 · Nawder Loswin · 2026*
