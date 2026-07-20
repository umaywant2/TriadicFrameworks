# UI Dependency Graph — TriadicFrameworks Prompts

The UI Dependency Graph describes how TriadicFrameworks prompt artifacts depend on and
unlock each other across the Prompts site: templates, stacks, engines, modules, and
UI logic.  
It is the structural map behind the interactive UI — showing which artifacts must be
loaded, understood, or completed before others become available.

This page is the front door for the UI dependency model.

---

## Purpose

The UI Dependency Graph is used to:

- document dependencies between templates, stacks, engines, and modules  
- define unlock rules for the Prompts UI  
- show how teaching flows progress across RTT/1 → RTT∞  
- surface which artifacts are “prerequisites” for others  
- support spine visualizations and dependency overlays  
- maintain structural neutrality while exposing UI logic  

It is the canonical reference for UI‑level relationships in the Prompts system.

---

## Graph Layers

The dependency graph is organized into layers:

- **Templates Layer** — capture, analyze, drift, coherence, operator, domain, substrate, teaching, research  
- **Stacks Layer** — structural, diagnostic, operator, substrate, domain, teaching, research  
- **Engines Layer** — RTT engines, IPD‑12, substrate‑aware engines  
- **Modules Layer** — domain modules, applied modules, teaching modules, research modules  
- **UI Layer** — unlock rules, flows, overlays, and visual affordances  

Each layer exposes nodes and edges that define how prompts are used and sequenced.

---

## Node Types

The graph uses several canonical node types:

- **Template Nodes** — `p_Capture`, `p_Analyze`, `p_Drift`, `p_Coherence`, `p_Operator`, `p_Domain`, `p_Substrate`, `p_Teaching`, `p_Research`  
- **Stack Nodes** — `structural-stack`, `diagnostic-stack`, `operator-stack`, `substrate-stack`, `domain-stack`, `teaching-stack`, `research-stack`  
- **Engine Nodes** — RTT/1, RTT/2, RTT/3, RTT/12, RTT∞, IPD‑12  
- **Module Nodes** — structural, substrate, domain, teaching, research, applied, examples  
- **UI Nodes** — flows, unlock rules, overlays, dependency views, teaching packs  

Each node type participates in dependency edges.

---

## Edge Types

Edges describe how nodes depend on or unlock each other:

- **Prerequisite Edges** — one artifact must be understood or completed before another  
- **Unlock Edges** — one artifact unlocks UI access to another  
- **Support Edges** — one artifact provides scaffolding or context for another  
- **Synthesis Edges** — one artifact aggregates or summarizes others  
- **Teaching Edges** — one artifact is used to teach another  

Examples:

- `p_Capture` → `p_Analyze` (prerequisite)  
- `p_Analyze` → `p_Drift` (support)  
- `p_Drift` → `p_Coherence` (support)  
- `operator-stack` → `p_Operator` (support)  
- `structural-stack` → `domain-stack` (prerequisite)  
- `teaching-stack` → `p_Teaching` (support)  
- RTT/1 → RTT/2 → RTT/3 → RTT/12 → RTT∞ (prerequisite chain)  

---

## UI Unlock Rules

The Prompts UI uses the dependency graph to:

- **Gate advanced artifacts** behind foundational ones  
- **Sequence teaching flows** (e.g., Capture → Analyze → Drift → Coherence → Synthesis)  
- **Highlight required stacks** for specific engines or modules  
- **Drive overlays** in the S3 Spine Visualizer  
- **Expose dependency views** for templates, stacks, and modules  

Unlock rules are defined in UI configuration files and reflected in this graph.

---

## Usage

The UI Dependency Graph is used in:

- Prompts site navigation  
- S3 Spine Visualizer overlays  
- Teaching packs and classroom flows  
- Module and stack documentation  
- Engine front‑doors (RTT, IPD‑12)  
- Research and applied workflows  

It is the backbone of how the Prompts UI behaves.

---

## Cross‑Links

### Prompts Site  
https://www.triadicframeworks.org/prompts/ui/dependency-graph/

### Docsbook  
https://docs.triadicframeworks.org/docs/

### S3 Spine Visualizer  
https://www.triadicframeworks.org/spine

### GitHub Source  
https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/prompts/ui

---

## Related Files

- `index.md` — UI front‑door  
- `flows.md` — UI flows and sequences  
- `unlock-rules.md` — UI unlock logic  
- `overlays.md` — visual overlays and spine integration  
- `../templates/index.md` — templates front‑door  
- `../stacks/index.md` — stacks front‑door  
- `../engines/index.md` — engines front‑door  

---

## Manifest

See `module.json` for the full registry of UI modules, templates, stacks, engines,
examples, and navigation structure.

