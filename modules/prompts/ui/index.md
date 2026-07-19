# TriadicFrameworks — UI Layer

The UI layer defines how prompt modules, templates, stacks, and engines are presented,
sequenced, unlocked, and rendered across the TriadicFrameworks Prompts site.  
It provides the structural rules that govern navigation, dependency resolution,
wireframe layout, and output formatting.

This page is the front door for all UI‑level documentation.

---

## UI Responsibilities

The UI layer manages:

- **Unlock Logic** — how modules become available based on prerequisites  
- **Dependency Graphs** — how engines, stacks, templates, and modules relate  
- **Flows & Sequences** — how users move through Capture → Analyze → Drift → Coherence → Synthesis  
- **Wireframes** — visual layout for modules, worksheets, posters, exams, and teaching packs  
- **Output Formats** — canonical formatting for prompt blocks, worksheets, diagnostics, and teaching bundles  
- **Overlays** — S3 Spine Visualizer overlays for engines, stacks, and modules  

The UI layer ensures consistency across the entire Prompts site.

---

## UI Directory Structure

### `unlock-logic.md`  
Defines how modules unlock based on prerequisites, engine selection, stack traversal, or template usage.

### `dependency-graph.md`  
Documents the dependency relationships between templates, stacks, engines, modules, and UI flows.

### `flows.md`  
Describes canonical UI flows such as Capture → Analyze → Drift → Coherence → Synthesis.

### `wireframe.md`  
Defines the visual layout for prompt modules, worksheets, posters, exams, and teaching bundles.

### `wireframes/`  
Contains specialized wireframes for RTT engines, IPD‑12, teaching modules, diagnostic modules, structural modules, and RTT∞ deep‑layer modules.

### `output-format.md`  
Defines canonical formatting rules for prompt blocks, worksheets, diagnostics, teaching bundles, and posters.

### `overlays.md`  
Documents S3 Spine Visualizer overlays and how UI elements map to the spine.

---

## UI Layer Functions

The UI layer provides:

- **Navigation Rules**  
  How modules, stacks, templates, and engines appear and sequence in the Prompts site.

- **Unlock Rules**  
  How prerequisites determine module availability.

- **Dependency Resolution**  
  How engines, stacks, templates, and modules depend on one another.

- **Wireframe Rendering**  
  How modules are visually structured.

- **Output Formatting**  
  How prompt blocks, worksheets, diagnostics, and teaching bundles are formatted.

- **Spine Integration**  
  How UI elements map to the S3 Spine Visualizer.

---

## Cross‑Links

### Prompts Site  
https://www.triadicframeworks.org/prompts/ui/

### Docsbook  
https://docs.triadicframeworks.org/docs/

### S3 Spine Visualizer  
https://www.triadicframeworks.org/spine

### GitHub Source  
https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/prompts/ui

---

## Related Directories

- `../templates/` — prompt templates  
- `../stacks/` — structural stacks  
- `../engines/` — RTT engines  
- `../modules/` — module registry  
- `../examples/` — example modules  

---

## Root Files

- `index.md` — UI front‑door  
- `unlock-logic.md` — unlock rules  
- `dependency-graph.md` — dependency graph  
- `flows.md` — UI flows  
- `wireframe.md` — wireframe layout  
- `output-format.md` — output formatting  
- `overlays.md` — spine overlays  

---

## Manifest

See `module.json` for the full registry of UI modules, templates, stacks, engines,
examples, and navigation structure.

