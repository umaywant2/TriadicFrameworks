# ✅ **`/docs/rtt/Inside/Python/manifest/module.json`**  
### *drop‑in‑ready, canon‑aligned*  
*(Source: active tab content   [github.com](https://github.com/umaywant2/TriadicFrameworks/edit/main/docs/rtt/Inside/Python/manifest/module.json))*

```json
{
  "module": "RTT-Inside-Python",
  "version": "2026-05",
  "summary": "RTT operator grammar for Python-class semantic systems, including form scanning, drift detection, invariant evaluation, resonance chamber routing, and ROA compatibility.",
  "category": "RTT-Inside",

  "files": [
    { "path": "README.md", "role": "profile" },
    { "path": "session_context.html", "role": "signature" },

    { "path": "operator_hooks.md", "role": "engine", "analyzer_layer": "operator" },
    { "path": "operator_hooks_semantic.md", "role": "engine", "analyzer_layer": "dimensional" },

    { "path": "examples/causal_trace_example.md", "role": "example" },
    { "path": "Inside-Cisco_Inside-Python_Inside-Internet2_cross_module_examples.md", "role": "example" },
    { "path": "Inside-Cisco_Inside-Python_Inside-Internet2_triadic_full_stack_example.md", "role": "example" }
  ]
}
```

---

## Canon Notes

- **role: profile** → module identity  
- **role: signature** → session context  
- **role: engine** → operator grammars (base + semantic)  
- **role: example** → causal trace + cross‑module + triadic full‑stack  
- **analyzer_layer** follows your schema:
  - `operator` → INTENT_PY → RTT_PY chain  
  - `dimensional` → semantic layer (forms, drift, invariants)  

Everything is aligned with the Cisco + Internet2 manifests for cross‑module consistency.
