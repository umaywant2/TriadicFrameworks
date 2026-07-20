## ⚡ Quickstart snippets (drop‑in for README or website)

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
