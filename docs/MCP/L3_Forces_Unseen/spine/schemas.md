# ⚡ S3 Spine — Schemas (R5 Canon)  
### Schema Reference for the Unseen Force‑Regime Structural Graph  
**Layer:** L3_Forces_Unseen  
**Triad:** forces  
**Lineage:** qmroot → frequency → fluids → forces  

The S3 Spine uses a set of canonical schemas to define its **structural**, **semantic**, **dimensional**, **operator**, **example**, and **protocol** systems.  
This page documents all schemas relevant to the spine subsystem and explains how they interconnect.

---

## 1. Example Envelope Schema  
**File:** `example.schema.json`

Defines the **six‑envelope example structure** used across all S3 example files.

| Field | Purpose |
|-------|---------|
| **canonical** | Pure structural interpretation |
| **reality** | Machine‑level interpretation |
| **imagination** | Symbolic interpretation |
| **information** | Informational / cosmology interpretation |
| **error** | Rupture / instability interpretation |
| **qmroot** | Origin‑state interpretation |

This schema ensures consistency across:

- `canonical.001.json`  
- `reality.001.json`  
- `imagination.001.json`  
- `information.001.json`  
- `error.001.json`  
- `qmroot.001.json`

---

## 2. Module Schema  
**File:** `module.schema.json`

Defines the structure of **module manifests**, including:

- canonical  
- layer  
- triad  
- regime  
- lineage  
- module metadata  
- file references  
- structural definitions  
- semantic axes  
- dimensional sets  
- operator lists  
- envelope references  

The S3 Spine’s `module.json` conforms to this schema and includes:

- `S3.graph.json`  
- `operator_interaction_map.json`  
- `operator_sequencing_rules.json`  
- `dimensional_mapping.json`  
- `spine.examples.registry.json`  
- `protocol.md`  
- `server.json`  

---

## 3. Graph Schema  
**File:** `graph.schema.json` (implicit)

Defines the structure of the S3 Spine graph:

- nodes  
- edges  
- causal direction  
- semantic axes  
- dimensional purity  

The S3 Spine graph is stored in:

- `S3.graph.json`  
- `S3.dot`

Nodes:

- gradient  
- field  
- rupture  
- integrity  

Edges:

- gradient → field  
- field → rupture  
- field → integrity  
- rupture → integrity  

---

## 4. Operator Interaction Schema  
**File:** `operator_interaction_map.json`

Defines:

- operator categories (primary / secondary)  
- semantic axes  
- dimensional sets  
- effects on each node  
- cosmology alignment  

Operators:

- push  
- pull  
- fieldShift  
- gradient  
- ruptureForce  
- bind  

---

## 5. Operator Sequencing Schema  
**File:** `operator_sequencing_rules.json`

Defines:

- valid sequences  
- forbidden sequences  
- semantic constraints  
- dimensional constraints  
- causal correctness rules  

Valid:

- gradient → field  
- field → rupture  
- field → integrity  
- rupture → integrity  

Forbidden:

- rupture → gradient  
- integrity → gradient  
- rupture → field  
- integrity → rupture  

---

## 6. Dimensional Mapping Schema  
**File:** `dimensional_mapping.json`

Defines the **10 canonical dimensions**:

- L4, L5, L16, LH  
- L8, L10, L26  
- L12  
- L32, LI  

Mapped to:

- gradientIntensity  
- fieldCoherence  
- rupturePotential  
- forceIntegrity  

---

## 7. Envelope Registry Schema  
**File:** `spine.examples.registry.json`

Defines:

- example IDs  
- envelope type  
- JSON file reference  
- documentation reference  
- sitemap + index  

---

## 8. Protocol Schema  
**File:** `protocol.md`

Defines:

- MCP binding  
- server capabilities  
- registry loading rules  
- graph traversal rules  
- operator validation rules  
- dimensional validation rules  

---

## 9. Server Schema  
**File:** `server.json`

Defines:

- server identity  
- capabilities  
- endpoints  
- registry bindings  
- cosmology lineage  
- graph references  

---

## 10. AI Metadata Schema  
**File:** `ai.metadata.json`

Defines:

- identity metadata  
- cosmology metadata  
- structural metadata  
- semantic metadata  
- dimensional metadata  
- operator metadata  
- envelope metadata  
- registry metadata  
- protocol metadata  

---

## 11. Session Context

```
Canon: R5
Modules: L3_Forces_Unseen / spine / schemas
Drift: none (freeze‑aligned)
Coherence: force‑state coherence
Version: 1.0.0
Format: schemas.md
Front door: docs/MCP/L3_Forces_Unseen/spine/
Audience: MCP implementers, RTT researchers, cosmology engineers
```

---

## ✔ Summary

Your regenerated `schemas.md` now provides:

- complete schema coverage  
- correct file references  
- correct causal chain  
- correct dimensional + semantic alignment  
- correct operator system  
- correct envelope system  
- full R5 canonical structure  
- removal of GitHub editor artifacts  

It is **fully canonical**, **drift‑free**, and **ready for commit**.
