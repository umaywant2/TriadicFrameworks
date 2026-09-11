<img width="1194" height="672" alt="Shared_" src="https://github.com/user-attachments/assets/64901720-797e-4151-b09d-cd2968e79c63" />

- [`module.json`](https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/refs/heads/main/docs/_shared/module.json) — Agentic module schema role assignments

# 📁 `_shared` — Global Components & Schema

The `_shared` directory contains reusable components and schema definitions used across the TriadicFrameworks documentation system.  
These files ensure consistency, reduce duplication, and provide a single source of truth for shared UI elements and structural rules.

---

## 🌐 Included Components

### `components_header.html`
Shared header block used across Docsbook pages.  
Provides consistent navigation, branding, and top‑of‑page structure.

### `components_footer.html`
Shared footer block containing global links, license notes, and canonical metadata anchors.

### `components_session-context.html`
Reusable session‑context block used in modules that display canonical session metadata (Canon, Drift, Coherence, Version, Format, etc.).

---

## 📐 Schema

### `schema/module.schema.json`
The canonical JSON Schema defining the structure of all module.json files across TriadicFrameworks.  
This schema ensures:

- structural consistency  
- drift detection  
- automation compatibility  
- AI‑ready metadata integrity  

All modules reference this schema either directly or implicitly.

---

## 🧩 How to Use These Shared Components

In any Docsbook page:

```md
{{#include ../_shared/components_header.html}}
```

Or for session context:

```md
{{#include ../_shared/components_session-context.html}}
```

These inclusions keep your documentation **modular**, **consistent**, and **drift‑proof**.

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
```
