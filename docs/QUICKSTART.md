# 🚀 **RTT Quickstart (Re‑Imagined)**  
*A student‑first, Copilot‑friendly introduction to Resonance‑Time Theory*

---

## **0. What RTT *is* (in 60 seconds)**  
RTT is a substrate‑level grammar for:

- resonance  
- lostation  
- dual‑envelope systems  
- SET/FFF decomposition  
- lineage‑safe scroll execution  

Everything in TriadicFrameworks — scrolls, remix engines, pipelines — is built on these operators.

---

## **1. Learn RTT with Copilot (Start Here)**  
Before touching code, new users should *experience* RTT through guided examples.

### **Example 1 — What is a Lostational Supsphere?**  
Ask Copilot:  
> “Explain a lostational supsphere using a storm, a planet, and an atom.”

### **Example 2 — SET Decomposition**  
Ask Copilot:  
> “Show how S, E, and T appear in chemistry, weather, and orbital mechanics.”

### **Example 3 — FFF Lattice**  
Ask Copilot:  
> “Explain the FFF lattice around Earth and how it shapes magnetospheric flows.”

### **Example 4 — Scroll Interpretation**  
Ask Copilot:  
> “Interpret this scroll and explain what the emitter and frequency do.”

```
emitter: demo
frequency: 144
```

These examples give users the *mental model* needed before touching the tools.

---

## **2. Run Your First Scroll (Browser‑Native)**  
No installs. No setup.  
Just run a scroll directly in the browser pipeline.

```js
import { runScroll } from "./scrollPipeline.js";

const scroll = `
emitter: demo
frequency: 144
`;

const result = runScroll(scroll);
console.log(result.output);
```

This mirrors the example on the current page   [triadicframeworks.org](https://www.triadicframeworks.org) but now sits in the right place in the learning flow.

---

## **3. Clone the Repo (When Ready)**  
Once users understand RTT concepts and scrolls, *then* they clone:

```
git clone https://github.com/umaywant2/TriadicFrameworks.git
```

Repo structure:

- `scroll_pipeline.py` — Python scroll engine  
- `scrollPipeline.js` — browser scroll engine  
- `remix_generation.py` — lineage‑safe remixing  
- `batch_orchestrator.py` — multi‑scroll execution  

---

## **4. Run Scrolls Locally (Python)**

```python
from scroll_pipeline import run_scroll

scroll = """
emitter: demo
frequency: 144
"""

result = run_scroll(scroll)
print(result["output"])
```

---

## **5. Remix Scrolls (Lineage‑Safe)**

```python
from remix_generation import remix_scroll

base = """
emitter: demo
frequency: 144
"""

variant = remix_scroll(base)
print(variant["metadata"]["remix_id"])
```

---

## **6. Batch Execution (Multi‑Scroll)**

```python
from batch_orchestrator import batch_run

paths = ["scrolls/a.fff", "scrolls/b.fff"]
report = batch_run(paths, output_dir="reports")

print(report["count"], "scrolls executed")
```

---

# 🎯 **Why This New Quickstart Works**

It matches the TriadicFrameworks philosophy:

- **Minimal**  
- **Student‑first**  
- **Scroll‑centric**  
- **AI‑friendly**  
- **Canon‑aligned**  
- **No drift**  
- **No assumptions**  

And it solves the real problem:  
**RTT concepts must come *before* tools.**

This version teaches RTT → then scrolls → then tools → then workflows.
