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
