<img width="1194" height="672" alt="Hooks_" src="https://github.com/user-attachments/assets/1f1dc860-2679-47ea-b1ae-9ddb266751b9" />

- [`module.json`](https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/refs/heads/main/docs/hooks/module.json) — Agentic module schema role assignments

# 🪝 Hooks — Canonical Event & Trigger Layer

The `hooks` directory contains the event‑driven trigger layer for TriadicFrameworks.  
Hooks define how modules respond to actions, state changes, or resonance events across the canon.

This directory provides:

- canonical hook definitions  
- event → action mappings  
- automation triggers  
- cross‑module integration points  
- lightweight HTML index for browsing  

Hooks are part of the **automation substrate**, enabling modules to react to internal or external signals.

---

## 📄 Included Hook Files

### `index.html`
A lightweight HTML index for browsing available hooks.  
Used by internal tooling, documentation viewers, and module‑level automation systems.

### `data/hooks.json`
The canonical hook registry.  
Defines:

- hook names  
- trigger conditions  
- event categories  
- associated actions  
- metadata for automation engines  

This file is consumed by RTT automation layers, module builders, and integration tools.

---

## 🧩 How to Reference Hooks

Inside any module:

```md
See: `docs/hooks/data/hooks.json`
```

Or include directly:

```md
{{#include ../hooks/index.html}}
```

Hooks keep your documentation **reactive**, **automated**, and **integration‑ready**.

---

<div style="font-size: 0.8em; margin-bottom: 0.5rem;">
  <span style="
    display:inline-block;
    padding:3px 8px;
    border-radius:999px;
    background:#1a1a1a;
    color:#fff;
    font-family:Arial, sans-serif;
    font-size:11px;
  ">
    🤖 AI‑Ready Module • TriadicFrameworks
  </span>
</div>
