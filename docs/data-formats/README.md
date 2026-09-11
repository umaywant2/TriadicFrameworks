<img width="1194" height="672" alt="Data_formats_" src="https://github.com/user-attachments/assets/077f4e96-0419-4a8e-9d1b-b42048453a5a" />

- [`module.json`](https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/refs/heads/main/docs/data-formats/module.json) — Agentic module schema role assignments

# 🗂️ Data Formats — Canonical Schemas

The `data-formats` directory contains all canonical data schemas used across TriadicFrameworks.  
These schemas define the structure, validation rules, and required fields for core diagnostic and transmission formats.

Each file in this directory represents a **formal data contract** — ensuring consistency, drift‑resistance, and interoperability across RTT engines, diagnostics, and tooling.

---

## 📄 Included Data Format Schemas

### `TCT_DEF_Schema.md`
Defines the **Triadic Coupling Table (TCT)** schema.  
Used for domain‑to‑domain coupling definitions, resonance pathways, and cross‑system diagnostics.

### `TDRC_Violation_Log_Schema.md`
Schema for **Triadic Drift & Resonance Compliance (TDRC)** violation logs.  
Captures drift events, clarity failures, and compliance deviations in RTT or system‑level simulations.

### `TLMF_Schema.md`
Defines the **Triadic Layer Mapping Format (TLMF)**.  
Used for mapping operator layers, dimensional envelopes, and coherence regimes.

---

## 🧩 How to Reference Data Schemas

Inside any module:

```md
See: `docs/data-formats/TCT_DEF_Schema.md`
```

Or include directly:

```md
{{#include ../data-formats/TLMF_Schema.md}}
```

These schemas ensure your documentation remains **structured**, **canonical**, and **drift‑proof**.

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
