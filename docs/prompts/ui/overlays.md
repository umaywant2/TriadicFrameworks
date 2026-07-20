# UI Overlays — TriadicFrameworks Prompts

UI Overlays define how visual layers are rendered on top of the S3 Spine Visualizer and
the Prompts UI.  
They provide structural, diagnostic, operator, substrate, dimensional, and domain
overlays that help users understand RTT engines, stacks, templates, and modules.

This page is the front door for all overlay documentation.

---

## Purpose

Overlays are used to:

- visualize RTT operator grammar  
- show drift‑tensor behavior across layers  
- highlight coherence anchors  
- reveal substrate‑tensor transitions  
- display dimensional rails and transitions  
- map domain behavior across the six canonical domains  
- expose dependencies between templates, stacks, engines, and modules  
- support teaching bundles and diagnostic flows  

Overlays are the visual intelligence layer of the Prompts UI.

---

## Overlay Types

The UI supports several canonical overlay types:

### 1. Structural Overlays  
Show identity, boundary, commitment, and topology.

Used in:

- structural-stack  
- RTT/1  
- module identity sections  

---

### 2. Drift Overlays  
Visualize geometric, operational, temporal, conceptual, and domain drift.

Used in:

- drift-stack  
- RTT/2  
- drift templates  
- diagnostic flows  

---

### 3. Coherence Overlays  
Highlight purpose, constraint, goal, and continuity coherence.

Used in:

- coherence-stack  
- RTT/3  
- coherence templates  
- teaching bundles  

---

### 4. Regime‑Point Overlays  
Show presence, absence, tension, basin behavior, and attractors.

Used in:

- diagnostic-stack  
- RTT/12  
- regime‑point modules  
- advanced teaching flows  

---

### 5. Substrate Overlays  
Visualize substrate behavior across physical, cultural, cognitive, civic, biological, and computational media.

Used in:

- substrate-stack  
- RTT∞  
- substrate templates  
- cross‑substrate modules  

---

### 6. Dimensional Overlays  
Show dimensional rails, drift, coherence, prime‑state transitions, collapse, and integration.

Used in:

- dimensional-stack  
- RTT∞  
- dimensional templates  
- teaching bundles  

---

### 7. Domain Overlays  
Visualize domain behavior across psychology, physics, economics, governance, AI/agents, and biology.

Used in:

- domain-stack  
- domain templates  
- cross‑domain modules  
- research bundles  

---

### 8. Dependency Overlays  
Show relationships between templates, stacks, engines, modules, and UI flows.

Used in:

- dependency-graph.md  
- unlock-logic.md  
- flows.md  

---

## Overlay Behavior

Overlays follow these rules:

- overlays activate only when prerequisites are met  
- overlays stack visually in canonical RTT order  
- overlays may be toggled individually or in groups  
- overlays never override core UI content  
- overlays always reflect the current engine, stack, or module  
- overlays integrate directly with the S3 Spine Visualizer  

---

## Overlay Activation Rules

Overlays activate based on:

### 1. Template Usage  
Using a template unlocks its corresponding overlay.

### 2. Stack Traversal  
Traversing a stack unlocks overlays for that stack.

### 3. Engine Selection  
Selecting an RTT engine activates engine‑specific overlays.

### 4. Module Viewing  
Viewing a module activates overlays relevant to that module’s layer.

### 5. UI Interaction  
Viewing dependency graphs or wireframes unlocks dependency overlays.

---

## S3 Spine Integration

Overlays map directly onto the S3 Spine Visualizer:

- structural overlays map to the spine’s identity layer  
- drift overlays map to the drift‑tensor rails  
- coherence overlays map to the coherence anchors  
- regime‑point overlays map to attractor basins  
- substrate overlays map to substrate‑tensor transitions  
- dimensional overlays map to dimensional rails  
- domain overlays map to domain nodes  
- dependency overlays map to cross‑layer edges  

The spine becomes a multi‑layer RTT visualization when overlays are active.

---

## Overlay Wireframe

All overlays follow a shared wireframe:

```
# Overlay Title

## Overview
Block…

## Layer Mapping
Block…

## Activation Rules
Block…

## UI Behavior
Block…

## Spine Integration
Block…

## Examples
Block…

## Manifest
Block…
```

---

## Cross‑Links

- `index.md` — UI front‑door  
- `unlock-logic.md` — unlock rules  
- `dependency-graph.md` — dependency graph  
- `flows.md` — UI flows  
- `wireframe.md` — wireframe layout  
- `output-format.md` — output formatting  

---

## Manifest

See `module.json` for the full registry of UI modules, templates, stacks, engines,
examples, and navigation structure.
