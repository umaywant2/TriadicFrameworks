# UI Output Format — TriadicFrameworks Prompts

The Output Format defines the canonical rendering rules for all prompt artifacts in the
TriadicFrameworks Prompts site.  
It ensures that modules, templates, stacks, engines, worksheets, diagnostics, teaching
bundles, and posters all share a consistent visual and structural grammar.

This page is the front door for all output‑format specifications.

---

## Purpose

The Output Format governs:

- how prompt blocks are rendered  
- how worksheets and diagnostics are structured  
- how teaching bundles and posters are formatted  
- how UI modules maintain consistency across engines and stacks  
- how RTT operator grammar appears visually  
- how drift, coherence, substrate, dimensional, and domain prompts are displayed  
- how multi‑layer artifacts maintain structural neutrality  

It is the canonical formatting reference for the Prompts UI.

---

## Core Output Rules

### 1. Prompt Block Structure  
All prompt blocks follow the same structure:

```
## Prompt Title
Prompt description or instruction.

**Prompt:**  
- *Canonical prompt line.*
```

Rules:

- Titles use `##`  
- Prompt lines use italics  
- Lists use hyphens  
- No decorative formatting  
- No color, icons, or emojis in prompt blocks  

---

### 2. Worksheet Structure  
Worksheets follow a strict multi‑section layout:

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
- Always rendered with `##` section headers  
- No embedded images unless part of a teaching bundle  

---

### 3. Diagnostic Block Structure  
Diagnostics use a compact block format:

```
### Diagnostic
- Identity signal
- Drift signal
- Coherence signal
- Regime‑point signal
- Substrate signal
- Dimensional signal
- Domain signal
```

Rules:

- Always 7 signals  
- Always in RTT canonical order  
- Always bullet‑listed  
- No nested lists  

---

### 4. Teaching Bundle Format  
Teaching bundles use a multi‑layer layout:

```
# Teaching Bundle Title

## Lesson Overview
Summary…

## Teaching Sequence
1. Capture
2. Analyze
3. Drift
4. Coherence
5. Synthesis

## Worksheets
Links or embedded worksheet blocks…

## Posters
Links or embedded poster blocks…

## Examples
Example blocks…
```

Rules:

- Sequence always follows Capture → Analyze → Drift → Coherence → Synthesis  
- Posters must follow poster formatting rules  
- Worksheets must follow worksheet formatting rules  

---

### 5. Poster Format  
Posters use a large‑format layout:

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

- Always 9 sections  
- Always in RTT canonical order  
- Blocks may contain diagrams (SVG) or text  
- No decorative emojis or icons  

---

### 6. Engine Output Format  
RTT engines use a specialized output format:

```
# RTT Engine Name

## Overview
Description…

## Operators
List…

## Drift‑Tensor
List…

## Coherence Anchors
List…

## Regime‑Points
List…

## Substrate Behavior
List…

## Dimensional Rails
List…

## Domain Behavior
List…

## Examples
Example blocks…
```

Rules:

- Always 9 sections  
- Always in RTT canonical order  
- Examples must use prompt block formatting  

---

### 7. Module Output Format  
Modules follow the canonical module layout:

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

- Always include Manifest  
- Always include Examples  
- Always follow RTT canonical order  

---

## Cross‑Links

- `index.md` — UI front‑door  
- `unlock-logic.md` — unlock rules  
- `dependency-graph.md` — dependency graph  
- `flows.md` — UI flows  
- `wireframe.md` — wireframe layout  
- `overlays.md` — spine overlays  

---

## Manifest

See `module.json` for the full registry of UI modules, templates, stacks, engines,
examples, and navigation structure.
