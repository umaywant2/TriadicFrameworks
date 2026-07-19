# TriadicFrameworks — UI Modules

The UI layer of the TriadicFrameworks Prompts site defines how prompt modules are
presented, unlocked, sequenced, and rendered.  
It provides the structural rules that govern navigation, dependency resolution,
wireframe layout, and output formatting across all engines, stacks, and templates.

This page serves as the overview for all UI‑level prompt modules.

---

## Unlock Logic

**File:** `ui/unlock-logic.md`  
Unlock logic defines how modules become available based on prerequisites, engine
selection, stack traversal, or template usage.  
It ensures that prompts appear in the correct order and that users follow canonical
workflow paths.

Unlock logic is used by:

- RTT engines (RTT/1, RTT/2, RTT/3, RTT/12, RTT∞)  
- IPD‑12  
- Structural, diagnostic, operator, substrate, domain, teaching, and research stacks  
- All templates (capture, analyze, drift, coherence, etc.)

---

## Dependency Graph

**File:** `ui/dependency-graph.md`  
The dependency graph describes how modules relate to one another.  
It maps:

- engine → stack dependencies  
- stack → template dependencies  
- template → UI dependencies  
- RTT∞ deep‑layer traversal  
- IPD‑12 paradox → capture → coherence flows

The dependency graph is used by the S3 Spine Visualizer to render module relationships.

---

## Wireframe

**File:** `ui/wireframe.md`  
The wireframe defines the visual layout of prompt modules, including:

- module front doors  
- section navigation  
- prompt blocks  
- diagnostic blocks  
- worksheets  
- posters  
- curriculum pages  
- exam pages

Wireframes ensure consistent presentation across all modules.

---

## Wireframes Directory

**Directory:** `ui/wireframes/`  
Contains specialized wireframes for:

- IPD‑12  
- RTT engines  
- RTT∞ deep‑layer modules  
- teaching modules  
- diagnostic modules  
- structural modules

Each wireframe provides a visual blueprint for module layout.

---

## Output Format

**File:** `ui/output-format.md`  
Defines the canonical output format for prompts, including:

- prompt block structure  
- operator grammar formatting  
- diagnostic output  
- worksheet structure  
- teaching bundle layout  
- exam formatting  
- poster and flowchart embedding rules

Output format ensures consistency across the entire prompts site.

---

## Cross‑Links

### Prompts Site  
https://www.triadicframeworks.org/prompts/

### Docsbook  
https://docs.triadicframeworks.org/docs/

### S3 Spine Visualizer  
https://www.triadicframeworks.org/spine

### GitHub Source  
https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/prompts/ui

---

## Related Files

- `modules.md` — full module registry  
- `engines.md` — RTT engines overview  
- `stacks.md` — stack overview  
- `templates.md` — template overview  
- `p_Capture.md` — capture grammar reference  

---

## Manifest

See `module.json` for the full registry of UI modules, engines, stacks, templates, and
navigation structure.


