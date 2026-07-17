workflows 
## 📘 API reference blocks (scroll‑centric module layout)

These blocks follow the structure of the Workflows README and the style of your site’s documentation.   [github.com](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/workflows)

### **batch_orchestrator.py**

```
batch_run(items, output_dir=None) → dict

items:
    list of .fff file paths, in‑memory scroll objects, or mixed lists

output:
    {
      "timestamp": "...",
      "count": N,
      "results": [
        { "input": ..., "output": ... },
        ...
      ]
    }
```

### **remix_generation.py**

```
remix_scroll(scroll_obj, rules=None) → dict

Produces a remix variant of a scroll object.
Preserves canonical anchors and adds remix metadata.
```

### **scroll_pipeline.py (Python)**

```
run_scroll(scroll_text) → dict

Parses and executes a scroll.
Returns:
    { "output": ..., "warnings": [...], "metadata": {...} }
```

### **scrollPipeline.js (JavaScript)**

```
runScroll(scrollText) → object

Browser‑native scroll execution.
Mirrors the Python pipeline API.
```
# 🔷 Workflow Diagram (Refreshed, Scroll‑Centric)

This diagram shows how the four workflow engines relate to each other using the updated scroll‑centric topology:

- **Scrolls** remain the canonical center  
- **Pipelines** are execution paths (Python + JS symmetry)  
- **Remix** generates lineage variants  
- **Batch** coordinates multi‑scroll execution  
- **Engines orbit the scroll artifact, not each other**

---

## 🔷 Text‑Based Diagram (Single‑Glance)

```
                               🔷
                 ┌──────────────────────────┐
                 │   remix_generation.py    │
                 │   (Remix Lineage Engine) │
                 └──────────────▲───────────┘
                                │
                        produces variants
                                │
        ┌───────────────────────┴────────────────────────┐
        │                                                │
        │                Scrolls (.fff)                  │
        │        (canonical RTT artifacts)               │
        │                                                │
        └───────────────────────┬────────────────────────┘
                                │
                         executed by
                                │
 ┌──────────────────────────────┼──────────────────────────────┐
 │                              │                              │
 │     ┌────────────────────┐   │     ┌───────────────────┐    │
 │     │ scroll_pipeline.py │   │     │ scrollPipeline.js │    │
 │     │   (Python Engine)  │   │     │    (JS Engine)    │    │
 │     └────────────────────┘   │     └───────────────────┘    │
 │                              │                              │
 └──────────────────────────────┴───────────────┬──────────────┘
                                                │
                                        executes many
                                                │
                                   ┌──────────────────────────┐
                                   │  batch_orchestrator.py   │
                                   │     (Batch Runner)       │
                                   └──────────────────────────┘
```

### Interpretation  
- **Remix Generation** creates new scroll variants.  
- **Scroll Pipelines** (Python + JS) execute scrolls in different runtime environments.  
- **Batch Orchestrator** runs many scrolls or variants in sequence.  
- **Scrolls** remain the invariant center; engines are operators around them.  

This matches the modernized architecture shown in your Workflows page and the scroll‑centric Quickstart.

---

## 🔷 Updated Triadic Glyph (Scroll‑Centric)

A glyph for this subsystem should reflect the updated relationships:

```
                 🌀 Scroll Artifact
        ┌───────────────┼────────────────┬────────────────┐
        │               │                │                │
        │         🌐 JS Pipeline   🐍 Python Pipeline   🎨 Remix Engine
        │               │                │                │
        └───────────────┴────────────────┴────────────────┘
                                ▼
                         📦 Batch Orchestrator
```

### Interpretation  
- The scroll artifact is the invariant center.  
- Pipelines and Remix orbit horizontally as sibling engines.  
- Batch anchors the system by coordinating multi‑scroll execution.  
- The glyph mirrors the structural relationships in the diagram above.  

---

## 🔷 Notes for maintainers  
- `/docs/engine/` has been archived; no engine‑era modules appear in this diagram.  
- All workflows now use the scroll‑centric module layout (`tft.scrolls.*`).  
- Pipelines maintain Python/JS symmetry.  
- Remix and Batch remain orthogonal operators.  
## ⚡ Quickstart snippets (drop‑in for README or website)

These follow the QUICKSTART style from your site and GitHub docs.   [github.com](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/workflows)

### **Run a single scroll (Python)**

```python
from scroll_pipeline import run_scroll

scroll = """
emitter: demo
frequency: 144
"""

result = run_scroll(scroll)
print(result["output"])
```

### **Run multiple scrolls (batch orchestrator)**

```python
from batch_orchestrator import batch_run

paths = ["scrolls/a.fff", "scrolls/b.fff"]
report = batch_run(paths, output_dir="reports")

print(report["count"], "scrolls executed")
```

### **Generate a remix variant**

```python
from remix_generation import remix_scroll

scroll = """
emitter: demo
frequency: 144
"""

variant = remix_scroll(scroll)
print(variant["metadata"]["remix_id"])
```

### **Run a scroll in the browser (JS)**

```javascript
import { runScroll } from "./scrollPipeline.js";

const scroll = `
emitter: demo
frequency: 144
`;

const result = runScroll(scroll);
console.log(result.output);
```

These snippets mirror the API shapes of the refreshed engines and match the tone of your existing QUICKSTART docs.

        🌀⚙️📜
   Scroll • Engine • Artifact
# 🌀⚙️📜 Workflow Engines  
### Operational layer for RTT‑Inside: batches, pipelines, and remix generation

This directory contains **lightweight, substrate‑agnostic workflow modules** used across TriadicFrameworks for scroll generation, batch execution, remix lineage creation, and resonance‑aware pipeline orchestration.

Each workflow is intentionally minimal: no external dependencies, no hidden state, and no assumptions about the host environment. They are designed to be **portable**, **inspectable**, and **safe to remix**.

> ## 🗂️ Index Card
> Lightweight, substrate‑agnostic execution tools for scrolls, batches, and remix lineages.
>
> - **📦 Batch Orchestrator** — deterministic multi‑scroll execution  
> - **🎨 Remix Generator** — lineage‑safe remix creation  
> - **🌐 Scroll Pipeline (JS)** — browser‑native execution path  
> - **🐍 Scroll Pipeline (Python)** — programmatic scroll engine  
>
> These engines form the operational layer of RTT‑Inside, bridging scroll artifacts with executable pipelines across languages and environments.

---

## 📁 Contents of [`workflows`](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/workflows) folder

### 🛤️ corridor_batch_validator.py  
Corridor‑level batch validator using RTT‑QEB primitives.  
- Fetches corridor metadata  
- Normalizes rail signatures  
- Computes RCI and glyph  
- Compares against stored metadata  
- Emits a timestamped YAML validation report  

---

### 📦 batch_orchestrator.py  
A scroll‑centric batch runner for executing multiple `.fff` artifacts through the Python scroll pipeline.

- Accepts file paths, in‑memory scroll objects, or mixed lists  
- Loads and normalizes scrolls when needed  
- Executes each scroll via `scroll_pipeline.py`  
- Captures outputs, lineage metadata, and warnings  
- Aggregates results into a deterministic batch report  
- Optionally writes a timestamped YAML report for archival or analysis  

This engine is substrate‑agnostic and forms the batch‑execution counterpart to the Python and JS scroll pipelines.

---

### 🎨 `remix_generation.py`  
A remix‑lineage generator that produces new scroll variants from a base artifact.  
- Applies remix rules from TFT_3Pack  
- Preserves canonical anchors (τᵣ, D3/D6/D9, emitter constants)  
- Generates remix metadata blocks for downstream tools  
- Ideal for student remix submissions or experimental scroll forks

---

### 🌐 `scrollPipeline.js`  
A JavaScript‑based scroll pipeline for browser‑side or lightweight client execution.  
- Runs resonance flows without Python  
- Integrates with `rtt.js` and site‑level overlays  
- Useful for interactive demos, web‑native scroll previews, and teaching tools

---

### 🐍 `scroll_pipeline.py`  
The Python counterpart to the JS pipeline.  
- Provides a stable API for scroll parsing, validation, and execution  
- Supports `.fff` format operations  
- Can be embedded into notebooks, CLI tools, or batch systems

---

## 🔧 Purpose of This Folder  
The workflows directory acts as the **operational layer** of TriadicFrameworks:

- A place for **small, composable engines**  
- A bridge between **RTT theory** and **practical execution**  
- A toolkit for **students, developers, and researchers** working with scrolls, `.fff` files, or resonance‑aware pipelines  
- A foundation for future integrations (AI drift calibration, substrate‑mind science, dimensional‑core validators)

These workflows intentionally avoid domain‑specific assumptions so they can run across the entire TriadicFrameworks ecosystem.

---

## 🧩 Relationship to TFT_3Pack v1.3  
These workflows complement the tools found in:

`/docs/TFT_3Pack_v1.3/scripts/`  
`/docs/TFT_3Pack_v1.3/tft/`  
`/docs/TFT_3Pack_v1.3/examples/`

Where TFT_3Pack provides **formats, examples, and shell tools**, the `/workflows/` folder provides **programmable engines** for:

- Batch processing  
- Scroll remixing  
- Pipeline execution  
- Cross‑language integration (Python ↔ JS)

Together, they form the **execution backbone** of RTT‑Inside.

---

## 🧭 When to Use These Workflows  
Use this folder when you need:

- To run multiple scrolls in sequence  
- To generate remix lineages  
- To embed scroll execution into a Python or JS project  
- To validate `.fff` files programmatically  
- To build new tools on top of RTT‑Inside primitives

---

## 🗺️ Future Extensions  
Planned additions include:

- Regime‑aware pipeline overlays  
- Scroll‑to‑TFT converters  
- AI‑drift‑resilient execution wrappers  
- Dimensional‑core validators  
- Cross‑ontology translators

These will follow the same principles: minimal, portable, remix‑friendly.
