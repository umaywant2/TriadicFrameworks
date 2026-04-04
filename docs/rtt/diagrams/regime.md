# 🔄 **RTT Regime Loop — Minimal SVG**

```svg
<svg width="520" height="520" viewBox="0 0 520 520" xmlns="http://www.w3.org/2000/svg">

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
    .label {
      font-family: sans-serif;
      font-size: 14px;
      text-anchor: middle;
      fill: #555;
    }
  </style>

  <!-- Arrowhead marker -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#111"/>
    </marker>
  </defs>

  <!-- Title -->
  <text class="label" x="260" y="35">RTT Regime Loop</text>

  <!-- Node positions -->
  <!-- Arrival (top) -->
  <text class="node" x="260" y="90">Arrival</text>

  <!-- Expansion (upper-right) -->
  <text class="node" x="400" y="200">Expansion</text>

  <!-- Inversion (bottom-right) -->
  <text class="node" x="360" y="380">Inversion</text>

  <!-- Coherence (bottom-left) -->
  <text class="node" x="160" y="380">Coherence</text>

  <!-- Dissolution (upper-left) -->
  <text class="node" x="120" y="200">Dissolution</text>

  <!-- Arrows -->
  <!-- Arrival → Expansion -->
  <line class="arrow" x1="260" y1="110" x2="380" y2="180"/>

  <!-- Expansion → Inversion -->
  <line class="arrow" x1="420" y1="220" x2="380" y2="360"/>

  <!-- Inversion → Coherence -->
  <line class="arrow" x1="340" y1="400" x2="180" y2="400"/>

  <!-- Coherence → Dissolution -->
  <line class="arrow" x1="140" y1="360" x2="100" y2="220"/>

  <!-- Dissolution → Arrival -->
  <line class="arrow" x1="120" y1="180" x2="240" y2="110"/>

</svg>
```

---

## 🧩 Design Notes
- **Pentagonal layout** mirrors the 5‑regime loop.  
- **Neutral #111 strokes + sans-serif text** match your RTT‑Tech aesthetic.  
- **Arrows form a clean clockwise cycle**, matching the canonical regime order.  
- **Centered viewBox** ensures perfect scaling in GitHub and your docs site.  
- **No decorative clutter** — pure structural clarity.

If you want, you can also generate:

- a **curved‑arrow** version  
- a **circular regime wheel**  
- a **micro‑icon** version for inline use  
- or a **full RTT regime + operator overlay** diagram  

Just tell Copilot where you want to go next.
