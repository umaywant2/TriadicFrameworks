# ✅ **`/docs/rtt/Inside/Cisco/manifest/module.json`**

```json
{
  "module": "RTT-Inside-Cisco",
  "version": "2026-05",
  "summary": "RTT operator grammar for Cisco-class systems, including base and grid-scale variants, DSRSP awareness, resonance chamber routing, and ROA compatibility.",
  "category": "RTT-Inside",
  "files": [
    { "path": "README.md", "role": "profile" },
    { "path": "session_context.html", "role": "signature" },

    { "path": "operator_hooks.md", "role": "engine", "analyzer_layer": "operator" },
    { "path": "operator_hooks_grid.md", "role": "engine", "analyzer_layer": "dimensional" },

    { "path": "examples/base_flow_example.md", "role": "example" },
    { "path": "examples/grid_scale_example.md", "role": "example" },
    { "path": "examples/regime_transition_example.md", "role": "example" }
  ]
}
```

---

### Notes on the manifest (all canon‑aligned)

- **`role: profile`** → module identity  
- **`role: signature`** → session context  
- **`role: engine`** → operator grammars  
- **`analyzer_layer`** values match your schema:
  - `operator` for device‑level hooks  
  - `dimensional` for grid‑scale cluster logic  
- **examples/** are placeholders — I can generate them next if you want  
- No substrate exposure, no drift, fully RTT/1 aligned  
