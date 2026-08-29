# **TriadicFrameworks MCP — Cosmology‑Aligned Multi‑Tool Server (R5 Canon)**  
*(Generated from `module.json`, Freeze A applied)*

- [`module.json`](https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/refs/heads/main/docs/MCP/module.json) — Agentic module schema role assignments
- [`sitemap.json`](https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/refs/heads/main/docs/MCP/sitemap.json) — Agentic module schema role assignments

## 🌌 Overview  
The TriadicFrameworks MCP is a cosmology‑aligned multi‑tool server built on a **four‑layer substrate** that mirrors the fundamental triads of the TriadicFrameworks canon.  
These layers are pedagogical: **the folder layout itself teaches the worldview**.

### **Layer Model (Freeze A)**  
1. **L0_QMROOT — Origin (0D observer primitive)**  
2. **L1_Frequency_Unseen — Oscillation (unseen resonance)**  
3. **L2_Fluids_Seen — Flow (seen, observable)**  
4. **L3_Forces_Unseen — Structure (unseen coherence)**  

Continuity mechanics (L11/L33/L66/L99 + validator pulse) is **not a layer**.  
It is a **composite resonance subsystem inside L3**, located at:

```
docs/MCP/L3_Forces_Unseen/continuity_mechanics/
```

---

## 🜁 **L0_QMROOT — Origin Layer (0D)**  
**Triad:** Origin  
**Description:** The 0D observer primitive. The coherence anchor. The identity of the server.

**Contains:**  
- `getCapabilities.json`  
- `server.json`  
- `auth/*`  
- `errors/*`  
- `discovery/*`  
- `examples/*`  

This layer defines the *existence* of the MCP server.

---

## 🜂 **L1_Frequency_Unseen — Oscillation Layer (Unseen)**  
**Triad:** Frequency  
**Description:** Unseen oscillation, resonance, operator grammar, diagnostics, graph traversal, indexing, and spectral analysis.

**Contains:**  
- diagnostics (alignment, awareness, clarity, coherence, continuity, drift, regime)  
- operator grammar  
- graph traversal tools  
- indexer tools  
- spectral analysis tools  

This layer defines *unseen resonance*.

---

## 🜄 **L2_Fluids_Seen — Flow Layer (Seen)**  
**Triad:** Fluids  
**Description:** Observable flow, metadata extraction, module listing, filesystem tools, learning tools, and session context rendering.

**Contains:**  
- `fs/*` (list, read, search)  
- learning tools (flashcards, quizzes, cheat sheets)  
- module metadata tools  
- examples  

This layer defines *seen flow*.

---

## 🜃 **L3_Forces_Unseen — Structure Layer (Unseen)**  
**Triad:** Forces  
**Description:** Unseen structural coherence, operators, schemas, registries, spine, and composite resonance subsystems.

**Contains:**  
- operators (bind, pull, push, gradient, ruptureForce, fieldShift)  
- schemas (analyzer, drift, lineage, module, operator, session)  
- registries (modules, operators, sitemap, AI registry)  
- spine (canonical, coherence, cosmology, dimensions, protocol, registry, resources, schemas)  
- examples  
- **continuity_mechanics subsystem** (L11/L33/L66/L99 + validator pulse)

This layer defines *unseen structure*.

---

## 🔧 **continuity_mechanics — L3 Subsystem (Composite Resonance)**  
**Triad:** Continuity  
**Description:** Composite resonance envelopes (L11 → L33 → L66 → L99) and the validator pulse (1%).  
This subsystem models continuity mechanics *inside* L3.

**Contains:**  
- `continuity.md`  
- `resonance.md`  
- `dimensions/*`  
- `diagrams/*`  
- `redirects/*`  
- `module.json`  
- `README.md`

This subsystem is **not a layer**.  
It is part of the **Forces** triad.

---

## 🧩 Protocol Surface (`docs/MCP/protocol/`)  
This directory defines the **agent‑facing MCP protocol**:

- `server.json` — local manifest  
- `tools.catalog.json` — tool definitions  
- `resources.catalog.json` — resource definitions  
- `prompts.catalog.json` — prompt definitions  
- `example.schema.json` — example envelope schema  
- `examples.registry.json` — example registry  

Agents should read **protocol/**.  
Students should walk **L0–L3**.

---

## 🖥️ Runtime (`docs/MCP/src/`)  
This directory contains the MCP runtime:

- `mcp/server.py` — stdio JSON‑RPC server  
- `loaders/corpus.py` — unified corpus loader  

The runtime resolves:

- modules  
- operators  
- examples  
- registries  
- continuity mechanics  
- spine metadata  

---

## 🗺️ Root Sitemap (`docs/MCP/sitemap.json`)  
This file lists the **top‑level MCP directories**:

- L0_QMROOT  
- L1_Frequency_Unseen  
- L2_Fluids_Seen  
- L3_Forces_Unseen  
- protocol/  
- src/  
- examples.registry.json  

This sitemap describes the **MCP substrate**, not the dimension atlas.

---

## 📦 Module Definition (`docs/MCP/module.json`)  
This file defines:

- MCP version  
- layer triads  
- freeze table  
- protocol surface  
- runtime surface  
- corpus surface  

The README is generated from this file.

---

## 📚 Examples  
Examples live in:

- `docs/MCP/Conditions_Substrate_Model/`  
- `docs/MCP/L3_Forces_Unseen/examples/`  
- `docs/MCP/protocol/examples.registry.json`  

All examples must validate against:

```
docs/MCP/protocol/example.schema.json
```

---

## 🔗 Canonical References  
- `module.json` — canonical MCP definition  
- `sitemap.json` — canonical MCP substrate map  
- `L3_Forces_Unseen/spine/*` — canonical cosmology documentation  

---

## ✔ Status  
This README reflects:

- Freeze A  
- L0–L3 layer model  
- continuity_mechanics as L3 subsystem  
- protocol/src split  
- updated corpus loader  
- updated runtime  
- updated triad table  
- updated cosmology alignment  
