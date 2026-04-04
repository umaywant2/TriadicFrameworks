Here’s a clean, RTT‑Tech–style SVG for **inversion.svg** — encoding the Collapse → Twist → Emergence loop.

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

  <!-- Title label -->
  <text class="label" x="210" y="30">Inversion: Collapse → Twist → Emergence</text>

  <!-- Nodes -->
  <!-- Collapse (top) -->
  <text class="node" x="210" y="90">Collapse</text>

  <!-- Twist (bottom-left) -->
  <text class="node" x="110" y="300">Twist</text>

  <!-- Emergence (bottom-right) -->
  <text class="node" x="310" y="300">Emergence</text>

  <!-- Arrows -->
  <!-- Collapse → Twist -->
  <line class="arrow" x1="210" y1="110" x2="130" y2="270"/>

  <!-- Twist → Emergence -->
  <line class="arrow" x1="130" y1="320" x2="290" y2="320"/>

  <!-- Emergence → (back toward Stabilize / next state) -->
  <line class="arrow" x1="310" y1="270" x2="230" y2="110"/>

</svg>
```

If you want a variant that explicitly shows `I(x) = E(T(C(x)))` inside the diagram, you can add a small equation label under the triangle.
