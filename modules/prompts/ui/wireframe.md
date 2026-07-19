# UI Wireframe — TriadicFrameworks Prompts

The UI Wireframe defines the canonical visual layout for prompt modules, templates,
stacks, engines, worksheets, posters, exams, and teaching bundles across the
TriadicFrameworks Prompts site.  
It ensures that all artifacts share a consistent structural presentation, regardless of
engine, stack, or domain.

This page is the front door for all wireframe specifications.

---

## Purpose

The Wireframe governs:

- how modules are visually structured  
- how templates are rendered in the UI  
- how stacks appear in navigation and teaching flows  
- how worksheets and diagnostics are laid out  
- how teaching bundles and posters are visually organized  
- how RTT engines present their multi‑layer structure  
- how UI consistency is maintained across the Prompts site  

It is the canonical visual blueprint for the Prompts UI.

---

## Core Wireframe Structure

All prompt artifacts follow a shared structural pattern:

```
# Title

## Section 1 — Identity
Block…

## Section 2 — Operators
Block…

## Section 3 — Drift
Block…

## Section 4 — Coherence
Block…

## Section 5 — Regime‑Points
Block…

## Section 6 — Substrate
Block…

## Section 7 — Dimensions
Block…

## Section 8 — Domains
Block…

## Section 9 — Synthesis
Block…
```

Rules:

- Always 9 sections  
- Always in RTT canonical order  
- Always use `##` for section headers  
- Blocks may contain text, diagrams, or examples  
- No decorative emojis or icons  

---

## Module Wireframe

Modules follow a specialized version of the core wireframe:

```
# Module Title

## Identity
Block…

## Purpose
Block…

## Operators
Block…

## Drift
Block…

## Coherence
Block…

## Substrate
Block…

## Dimensions
Block…

## Domains
Block…

## Examples
Block…

## Manifest
Block…
```

Rules:

- Always include Purpose  
- Always include Examples  
- Always include Manifest  
- Always follow RTT canonical order  

---

## Template Wireframe

Templates follow a simplified wireframe:

```
# Template Title

## Purpose
Block…

## Template Sections
Prompt blocks…
```

Rules:

- Template sections must follow template grammar  
- No diagrams unless part of a teaching bundle  
- Prompt blocks must follow prompt block formatting  

---

## Stack Wireframe

Stacks follow a multi‑section layout:

```
# Stack Title

## Purpose
Block…

## Prompt Families
List…

## Usage
Block…

## Cross‑Links
Block…

## Manifest
Block…
```

Rules:

- Prompt families must be grouped by function  
- Usage must reference engines and modules  
- Manifest must reference module.json  

---

## Engine Wireframe

RTT engines follow a strict multi‑layer layout:

```
# RTT Engine Name

## Overview
Block…

## Operators
Block…

## Drift‑Tensor
Block…

## Coherence Anchors
Block…

## Regime‑Points
Block…

## Substrate Behavior
Block…

## Dimensional Rails
Block…

## Domain Behavior
Block…

## Examples
Block…
```

Rules:

- Always 9 sections  
- Always in RTT canonical order  
- Examples must use prompt block formatting  

---

## Worksheet Wireframe

Worksheets follow the canonical worksheet layout:

```
# Worksheet Title

## Section 1 — Identity
Prompt block…

## Section 2 — Operators
Prompt block…

## Section 3 — Drift
Prompt block…

## Section 4 — Coherence
Prompt block…

## Section 5 — Regime‑Points
Prompt block…

## Section 6 — Substrate
Prompt block…

## Section 7 — Dimensions
Prompt block…

## Section 8 — Domains
Prompt block…

## Section 9 — Synthesis
Prompt block…
```

Rules:

- Always 9 sections  
- Always in RTT canonical order  
- No diagrams unless part of a teaching bundle  

---

## Poster Wireframe

Posters follow a large‑format layout:

```
# Poster Title

## Identity
Block…

## Operators
Block…

## Drift
Block…

## Coherence
Block…

## Regime‑Points
Block…

## Substrate
Block…

## Dimensions
Block…

## Domains
Block…

## Synthesis
Block…
```

Rules:

- Blocks may contain diagrams (SVG) or text  
- No decorative emojis or icons  
- Always 9 sections  

---

## Teaching Bundle Wireframe

Teaching bundles follow a multi‑layer instructional layout:

```
# Teaching Bundle Title

## Lesson Overview
Block…

## Teaching Sequence
1. Capture
2. Analyze
3. Drift
4. Coherence
5. Synthesis

## Worksheets
Blocks or links…

## Posters
Blocks or links…

## Examples
Blocks…
```

Rules:

- Sequence must follow canonical RTT teaching flow  
- Worksheets and posters must follow their wireframes  
- Examples must use prompt block formatting  

---

## Cross‑Links

- `index.md` — UI front‑door  
- `unlock-logic.md` — unlock rules  
- `dependency-graph.md` — dependency graph  
- `flows.md` — UI flows  
- `output-format.md` — output formatting  
- `overlays.md` — spine overlays  

---

## Manifest

See `module.json` for the full registry of UI modules, templates, stacks, engines,
examples, and navigation structure.
