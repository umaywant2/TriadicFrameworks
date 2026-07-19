# UI Flows — TriadicFrameworks Prompts

UI Flows define how users move through the TriadicFrameworks Prompts system.  
They specify the canonical sequences for templates, stacks, engines, modules, teaching
bundles, diagnostics, and synthesis workflows.

Flows ensure that the Prompts UI behaves consistently across all engines, stacks,
templates, and modules.

This page is the front door for all UI flow documentation.

---

## Purpose

UI Flows provide:

- **Canonical sequencing** for RTT workflows  
- **Navigation rules** for templates, stacks, engines, and modules  
- **Teaching sequences** for classroom and self‑study use  
- **Diagnostic flows** for structural, drift, coherence, and substrate analysis  
- **Synthesis flows** for multi‑layer alignment  
- **UI behavior** that matches RTT operator grammar  

Flows are the behavioral backbone of the Prompts UI.

---

## Core Flow: RTT Canonical Sequence

All RTT‑aligned flows follow the same nine‑layer sequence:

1. **Identity**  
2. **Operators**  
3. **Drift**  
4. **Coherence**  
5. **Regime‑Points**  
6. **Substrate**  
7. **Dimensions**  
8. **Domains**  
9. **Synthesis**

This sequence governs:

- template usage  
- stack traversal  
- engine presentation  
- module layout  
- worksheet structure  
- poster structure  
- teaching bundles  

---

## Template Flow

Templates follow the canonical RTT teaching and analysis sequence:

1. `p_Capture`  
2. `p_Analyze`  
3. `p_Drift`  
4. `p_Coherence`  
5. `p_Operator`  
6. `p_Domain`  
7. `p_Substrate`  
8. `p_Teaching`  
9. `p_Research`

Rules:

- Templates unlock in order  
- Each template requires viewing or completing the previous  
- Teaching and Research templates unlock only after full traversal  

---

## Stack Flow

Stacks follow the structural progression of RTT:

1. **Structural Stack**  
2. **Diagnostic Stack**  
3. **Operator Stack**  
4. **Substrate Stack**  
5. **Domain Stack**  
6. **Teaching Stack**  
7. **Research Stack**

Rules:

- Stacks unlock based on prerequisites  
- Each stack supports specific templates and modules  
- Teaching and Research stacks require full traversal  

---

## Engine Flow

RTT engines unlock progressively:

1. **RTT/1**  
2. **RTT/2**  
3. **RTT/3**  
4. **RTT/12**  
5. **RTT∞**  
6. **IPD‑12**

Rules:

- Engines cannot be accessed out of order  
- Each engine requires viewing or completing the previous  
- IPD‑12 unlocks only after full RTT traversal  

---

## Module Flow

Modules follow a multi‑layer flow:

1. **Structural Modules**  
2. **Substrate Modules**  
3. **Domain Modules**  
4. **Teaching Modules**  
5. **Research Modules**  
6. **Applied Modules**  
7. **Examples**

Rules:

- Modules unlock based on engine + stack + template prerequisites  
- Applied modules may require multiple stacks  
- Example modules unlock last  

---

## Teaching Flow

Teaching bundles follow the canonical instructional sequence:

1. **Capture**  
2. **Analyze**  
3. **Drift**  
4. **Coherence**  
5. **Synthesis**

Rules:

- Worksheets follow the same sequence  
- Posters follow the same sequence  
- Teaching stacks and templates must be unlocked first  

---

## Diagnostic Flow

Diagnostics follow the seven‑signal RTT diagnostic sequence:

1. **Identity Signal**  
2. **Drift Signal**  
3. **Coherence Signal**  
4. **Regime‑Point Signal**  
5. **Substrate Signal**  
6. **Dimensional Signal**  
7. **Domain Signal**

Rules:

- Diagnostics appear in compact blocks  
- Signals must follow canonical order  
- No nested lists  

---

## Synthesis Flow

Synthesis flows aggregate all layers:

1. Structural  
2. Drift  
3. Coherence  
4. Regime‑Points  
5. Substrate  
6. Dimensions  
7. Domains  
8. Cross‑Domain Alignment  
9. Final Synthesis

Rules:

- Synthesis unlocks only after full flow traversal  
- Synthesis appears in templates, modules, engines, worksheets, and posters  

---

## UI Behavior

UI Flows determine:

- which modules appear next  
- which templates unlock  
- which stacks become available  
- which engine layers are visible  
- which overlays appear in the S3 Spine Visualizer  
- how navigation behaves across the Prompts site  

Flows ensure that the UI remains consistent with RTT operator grammar.

---

## Cross‑Links

- `index.md` — UI front‑door  
- `unlock-logic.md` — unlock rules  
- `dependency-graph.md` — dependency graph  
- `wireframe.md` — wireframe layout  
- `output-format.md` — output formatting  
- `overlays.md` — spine overlays  

---

## Manifest

See `module.json` for the full registry of UI modules, templates, stacks, engines,
examples, and navigation structure.

