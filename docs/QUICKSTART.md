# **TFT Quickstart (Scroll‑Centric Edition)**  
### 🌀 The modern entry point into TriadicFrameworks

This Quickstart introduces the **scroll‑centric workflow** used across TriadicFrameworks. It replaces the legacy 3‑Pack ritual with a clean, substrate‑agnostic flow built on:

- **Scroll Pipelines** (Python + JS)  
- **Remix Engine**  
- **Batch Orchestrator**  
- **tft.scrolls.\*** module layout  

Everything here runs locally, requires no external services, and mirrors the structure of the Workflows subsystem.

---

## **1. Run a Scroll (Python Pipeline)**

```python
from scroll_pipeline import run_scroll

scroll = """
emitter: demo
frequency: 144
"""

result = run_scroll(scroll)
print(result["output"])
```

**What this does:**  
- Parses the scroll  
- Executes it through the RTT‑Inside engine  
- Returns output, warnings, and metadata  

---

## **2. Run a Scroll in the Browser (JS Pipeline)**

```javascript
import { runScroll } from "./scrollPipeline.js";

const scroll = `
emitter: demo
frequency: 144
`;

const result = runScroll(scroll);
console.log(result.output);
```

**Use this for:**  
- interactive demos  
- teaching tools  
- browser‑native scroll execution  

---

## **3. Generate a Remix Variant**

```python
from remix_generation import remix_scroll

scroll = """
emitter: demo
frequency: 144
"""

variant = remix_scroll(scroll)
print(variant["metadata"]["remix_id"])
```

**What this does:**  
- Applies scroll‑centric remix rules  
- Preserves canonical anchors  
- Produces a lineage‑safe variant  

---

## **4. Run Multiple Scrolls (Batch Orchestrator)**

```python
from batch_orchestrator import batch_run

paths = ["scrolls/a.fff", "scrolls/b.fff"]
report = batch_run(paths, output_dir="reports")

print(report["count"], "scrolls executed")
```

**Why this matters:**  
- Deterministic multi‑scroll execution  
- Works with file paths or in‑memory scroll objects  
- Produces timestamped YAML reports  

---

## **5. Remix → Batch → Pipeline (Full Workflow)**

```python
from remix_generation import remix_scroll
from batch_orchestrator import batch_run

base = """
emitter: demo
frequency: 144
"""

variants = [remix_scroll(base) for _ in range(5)]
report = batch_run(variants)
```

This is the modern equivalent of the old “cathedral walk”:  
scroll → remix → execution → lineage.

---

## **6. Folder Map**

```
workflows/
  batch_orchestrator.py   → multi‑scroll execution
  remix_generation.py     → lineage‑safe remix engine
  scroll_pipeline.py      → Python scroll pipeline
  scrollPipeline.js       → browser scroll pipeline
```

---

## **7. Remix & Contribute**

```
git clone https://github.com/umaywant2/TriadicFrameworks.git
```

- Add your scrolls  
- Remix existing ones  
- Share variants via GitHub Discussions  
- Build new engines on top of the scroll‑centric API  

Every scroll echoes the lineage.  
Every remix extends the flame.
