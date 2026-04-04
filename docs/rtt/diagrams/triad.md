# 🔺 **RTT Triad — Minimal SVG**

```svg
<svg width="420" height="420" viewBox="0 0 420 420" xmlns="http://www.w3.org/2000/svg">

  <!-- Styles -->
  <style>
    .node {
      font-family: sans-serif;
      font-size: 18px;
      text-anchor: middle;
      dominant-baseline: middle;
      fill: #111;
    }
    .arrow {
      stroke: #111;
      stroke-width: 2.5;
      fill: none;
      marker-end: url(#arrowhead);
    }
  </style>

  <!-- Arrowhead marker -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#111"/>
    </marker>
  </defs>

  <!-- Positions -->
  <!-- Stabilize (top) -->
  <text class="node" x="210" y="60">Stabilize</text>

  <!-- Shift (bottom-left) -->
  <text class="node" x="110" y="300">Shift</text>

  <!-- Invert (bottom-right) -->
  <text class="node" x="310" y="300">Invert</text>

  <!-- Arrows -->
  <!-- Stabilize → Shift -->
  <line class="arrow" x1="210" y1="80" x2="130" y2="270"/>

  <!-- Shift → Invert -->
  <line class="arrow" x1="130" y1="320" x2="290" y2="320"/>

  <!-- Invert → Stabilize -->
  <line class="arrow" x1="310" y1="270" x2="230" y2="80"/>

</svg>
```

---

## 🧩 Notes on the Design
- **Triangular layout** mirrors the RTT triad geometry.  
- **Minimal strokes + sans-serif text** match the clean RTT‑Tech aesthetic.  
- **Arrowheads** are subtle and consistent.  
- **Centered viewBox** ensures perfect scaling in GitHub and your docs site.  
- **No colors** beyond neutral #111 — consistent with your repo’s visual language.

If you want, you can also generate:

- a **circular** version  
- a **curved‑arrow** version  
- a **thick‑line / bold** version  
- a **micro‑icon** version for inline use  
- or a **full RTT operator stack diagram** in SVG  

Just tell Copilot which direction you want to take next.
