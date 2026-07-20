# UI Unlock Logic — TriadicFrameworks Prompts

The Unlock Logic defines how prompt modules, templates, stacks, and engines become
available in the TriadicFrameworks Prompts UI.  
It governs sequencing, prerequisites, dependency resolution, and conditional unlocks
based on user progress, engine selection, stack traversal, and template usage.

This page is the canonical reference for unlock behavior in the Prompts system.

---

## Purpose

Unlock Logic ensures that:

- foundational concepts appear before advanced ones  
- RTT engines unlock progressively (RTT/1 → RTT/2 → RTT/3 → RTT/12 → RTT∞)  
- stacks unlock based on structural prerequisites  
- templates unlock based on teaching or analysis flows  
- modules unlock based on engine, stack, or template usage  
- UI flows remain consistent across the Prompts site  
- users follow canonical RTT sequences without skipping layers  

Unlock Logic is the backbone of the Prompts UI.

---

## Unlock Layers

Unlock rules operate across five layers:

1. **Templates Layer**  
   Capture → Analyze → Drift → Coherence → Operator → Domain → Substrate → Teaching → Research

2. **Stacks Layer**  
   Structural → Diagnostic → Operator → Substrate → Domain → Teaching → Research

3. **Engines Layer**  
   RTT/1 → RTT/2 → RTT/3 → RTT/12 → RTT∞ → IPD‑12

4. **Modules Layer**  
   Structural, Substrate, Domain, Teaching, Research, Applied, Examples

5. **UI Layer**  
   Flows, wireframes, overlays, dependency views

Each layer has its own unlock rules and dependencies.

---

## Template Unlock Rules

Templates unlock in canonical RTT order:

- `p_Capture` unlocks first  
- `p_Analyze` unlocks after Capture  
- `p_Drift` unlocks after Analyze  
- `p_Coherence` unlocks after Drift  
- `p_Operator` unlocks after Coherence  
- `p_Domain` unlocks after Operator  
- `p_Substrate` unlocks after Domain  
- `p_Teaching` unlocks after Substrate  
- `p_Research` unlocks after Teaching

Rules:

- Templates cannot be accessed out of order  
- Each template requires completion or viewing of its predecessor  
- Teaching and Research templates unlock only after full template traversal  

---

## Stack Unlock Rules

Stacks unlock based on structural prerequisites:

- `structural-stack` unlocks first  
- `diagnostic-stack` unlocks after structural  
- `operator-stack` unlocks after diagnostic  
- `substrate-stack` unlocks after operator  
- `domain-stack` unlocks after substrate  
- `teaching-stack` unlocks after domain  
- `research-stack` unlocks after teaching

Rules:

- Stacks follow the same order as RTT analysis layers  
- Stacks unlock automatically when prerequisites are satisfied  
- Teaching and Research stacks require full stack traversal  

---

## Engine Unlock Rules

RTT engines unlock progressively:

- **RTT/1** unlocks first  
- **RTT/2** unlocks after RTT/1  
- **RTT/3** unlocks after RTT/2  
- **RTT/12** unlocks after RTT/3  
- **RTT∞** unlocks after RTT/12  
- **IPD‑12** unlocks after RTT∞

Rules:

- Engines cannot be accessed out of order  
- Each engine requires viewing or completing the previous engine  
- IPD‑12 unlocks only after full RTT traversal  

---

## Module Unlock Rules

Modules unlock based on engine, stack, and template usage:

- Structural modules unlock after structural-stack  
- Substrate modules unlock after substrate-stack  
- Domain modules unlock after domain-stack  
- Teaching modules unlock after teaching-stack  
- Research modules unlock after research-stack  
- Applied modules unlock after relevant domain or substrate modules  
- Example modules unlock after any module is viewed

Rules:

- Modules require both stack and template prerequisites  
- Applied modules may require multiple stacks  
- Example modules are always unlocked last  

---

## UI Flow Unlock Rules

UI flows unlock based on template and stack traversal:

- Capture → Analyze → Drift → Coherence → Synthesis  
- Structural → Operator → Substrate → Domain → Teaching → Research  
- RTT/1 → RTT/2 → RTT/3 → RTT/12 → RTT∞

Rules:

- Flows cannot skip steps  
- Synthesis unlocks only after full flow traversal  
- UI overlays unlock after dependency graph is viewed  

---

## Unlock Conditions

Unlock conditions include:

- **Prerequisite Completion**  
  Viewing or completing required templates, stacks, or modules.

- **Engine Selection**  
  Selecting an engine unlocks engine‑specific modules and templates.

- **Stack Traversal**  
  Traversing a stack unlocks related templates and modules.

- **Template Usage**  
  Using a template unlocks the next template in sequence.

- **UI Interaction**  
  Viewing dependency graphs or wireframes unlocks overlays.

---

## Cross‑Links

- `index.md` — UI front‑door  
- `dependency-graph.md` — dependency graph  
- `flows.md` — UI flows  
- `wireframe.md` — wireframe layout  
- `output-format.md` — output formatting  
- `overlays.md` — spine overlays  

---

## Manifest

See `module.json` for the full registry of UI modules, templates, stacks, engines,
examples, and navigation structure.

