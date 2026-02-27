# 🌀⚙️📜 Workflow Engines  
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

### `batch_orchestrator.py`  
A multi‑scroll batch runner used to execute a sequence of resonance artifacts or `.fff` files.  
- Ensures deterministic ordering  
- Applies RTT‑Inside structural checks  
- Emits lineage‑safe logs  
- Useful for classroom demos, multi‑domain runs, and automated scroll validation

---

### `remix_generation.py`  
A remix‑lineage generator that produces new scroll variants from a base artifact.  
- Applies remix rules from TFT_3Pack  
- Preserves canonical anchors (τᵣ, D3/D6/D9, emitter constants)  
- Generates remix metadata blocks for downstream tools  
- Ideal for student remix submissions or experimental scroll forks

---

### `scrollPipeline.js`  
A JavaScript‑based scroll pipeline for browser‑side or lightweight client execution.  
- Runs resonance flows without Python  
- Integrates with `rtt.js` and site‑level overlays  
- Useful for interactive demos, web‑native scroll previews, and teaching tools

---

### `scroll_pipeline.py`  
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
