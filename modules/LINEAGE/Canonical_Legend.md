# Diagram Legend — TriadicFrameworks (Canonical)

| Symbol | Name | Meaning | Visual Standard |
|--------|-------|----------|------------------|
| ■ (indigo‑violet stroke) | **Core Node** | Primary lineage origin (e.g., Forecast vs Actuals) | `node-core` |
| ■ (dark slate stroke) | **Lineage Node** | Module‑specific lineage (IE, MSM, GSM, TEL, SARG) | `node` |
| ■ (wide slate box) | **Downstream Cluster** | Multi‑module or multi‑echo grouping | `node-cluster` |
| → (thin indigo arrow) | **Echo Arrow** | TEL/SARG propagation of patterns | `edge-echo` |
| → (medium violet arrow) | **Structural Arrow** | RTT/1–2–3 or substrate‑driven flow | `edge-struct` |
| → (thick slate arrow) | **Cross‑Module Arrow** | IE ↔ MSM ↔ GSM interactions | `edge-cross` |

**Color Palette (canonical):**

- Core stroke: `#8E7CFF`  
- Lineage stroke: `#4B4B7A`  
- Cluster stroke: `#2A2A4A`  
- Echo arrow: `#7777B8`  
- Structural arrow: `#9A7CFF`  
- Cross‑module arrow: `#5A5A7A`  

**Background gradient (canonical):**

```
#050509 → #11112A → #1B1235
```

---

# ✅ 2) Canonical Legend Block (SVG Snippet)

This is the **drop‑in SVG fragment** you can paste into any diagram.  
It is self‑contained, uses the same CSS classes as all diagrams, and stays visually consistent.

```svg
<!-- Canonical Legend Block -->
<g transform="translate(40, 480)">
  <text x="0" y="0" class="title" font-size="14">Legend</text>

  <!-- Core Node -->
  <rect x="0" y="20" width="120" height="26" class="node-core"/>
  <text x="130" y="38" class="node-sub">Core Node</text>

  <!-- Lineage Node -->
  <rect x="0" y="60" width="120" height="26" class="node"/>
  <text x="130" y="78" class="node-sub">Lineage Node</text>

  <!-- Downstream Cluster -->
  <rect x="0" y="100" width="120" height="26" class="node-cluster"/>
  <text x="130" y="118" class="node-sub">Downstream Cluster</text>

  <!-- Echo Arrow -->
  <line x1="0" y1="150" x2="40" y2="150" class="edge-echo"/>
  <text x="130" y="154" class="node-sub">Echo Arrow</text>

  <!-- Structural Arrow -->
  <line x1="0" y1="180" x2="40" y2="180" class="edge-struct"/>
  <text x="130" y="184" class="node-sub">Structural Arrow</text>

  <!-- Cross‑Module Arrow -->
  <line x1="0" y1="210" x2="40" y2="210" class="edge-cross"/>
  <text x="130" y="214" class="node-sub">Cross‑Module Arrow</text>
</g>
```

---

# ✅ 3) Canonical Legend CSS (for all diagrams)

This ensures every diagram renders identically.

```svg
<style>
  /* Core node */
  .node-core {
    fill: #1E1E3A;
    stroke: #8E7CFF;
    stroke-width: 1.4;
    rx: 14; ry: 14;
  }

  /* Lineage node */
  .node {
    fill: #141424;
    stroke: #4B4B7A;
    stroke-width: 1.2;
    rx: 12; ry: 12;
  }

  /* Downstream cluster */
  .node-cluster {
    fill: #141424;
    stroke: #2A2A4A;
    stroke-width: 1.2;
    rx: 12; ry: 12;
  }

  /* Echo arrow */
  .edge-echo {
    stroke: #7777B8;
    stroke-width: 1.6;
    marker-end: url(#arrow);
  }

  /* Structural arrow */
  .edge-struct {
    stroke: #9A7CFF;
    stroke-width: 1.8;
    marker-end: url(#arrow);
  }

  /* Cross‑module arrow */
  .edge-cross {
    stroke: #5A5A7A;
    stroke-width: 2.0;
    marker-end: url(#arrow);
  }

  /* Text */
  .node-text { fill: #FFFFFF; font-weight: 600; }
  .node-sub { fill: #C8C8E8; }
</style>
```

---

# 🌟 What this gives you

Every diagram in the canon — Toolbox, IE, MSM, GSM, TEL, SARG — now shares:

- identical node shapes  
- identical stroke weights  
- identical arrow semantics  
- identical color palette  
- identical legend semantics  

This is the **visual grammar** of TriadicFrameworks diagrams.
