
- [``]()

# 📁 `_specs` — Canonical Specifications

The `_specs` directory contains formal specification documents for TriadicFrameworks.  
These files define low‑level mechanics, kernel behavior, and structural rules used by RTT and related engines.

This directory is intentionally small and highly focused.  
Each file inside `_specs` represents a **canonical specification** — not a tutorial, not a guide, but a structural definition.

---

## 📄 Included Specification Files

### `RTT_Kernel_v0.1.md`
The foundational specification for the RTT Kernel.  
Defines the initial operator loop, pulse behavior, clarity mechanics, and kernel‑level execution rules.

This document is referenced by:

- RTT Developer Quick‑Start  
- RTT Engine Implementations  
- RTT Experiment Blocks  
- Module‑level metadata validators  

---

## 🧩 How to Reference Specs in Docs

Inside any module:

```md
See: `docs/_specs/RTT_Kernel_v0.1.md`
```

Or include directly:

```md
{{#include ../_specs/RTT_Kernel_v0.1.md}}
```

Specs ensure your documentation remains **canonical**, **consistent**, and **drift‑proof**.

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
