<?xml version="1.0" encoding="UTF-8"?>
<svg width="960" height="540" viewBox="0 0 960 540"
     xmlns="http://www.w3.org/2000/svg">

  <!-- Background -->
  <rect x="0" y="0" width="960" height="540" fill="#ffffff"/>

  <!-- Title -->
  <text x="480" y="60" text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-size="24" fill="#222222">
    Crystal–Mycelial Engine — Regime Flow
  </text>

  <!-- Subtitle -->
  <text x="480" y="90" text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-size="16" fill="#555555">
    Biological → Hybrid → Mineral (geometry → alignment → lattice)
  </text>

  <!-- BGR box -->
  <rect x="80" y="150" width="240" height="90" rx="8" ry="8"
        fill="#f5fbff" stroke="#1f78b4" stroke-width="2"/>
  <text x="200" y="180" text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-size="18" fill="#1f78b4">
    BGR — Biological Growth
  </text>
  <text x="200" y="205" text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-size="13" fill="#333333">
    moisture 0.55–0.65 • P/E/G/M
  </text>

  <!-- HRR box -->
  <rect x="360" y="150" width="240" height="90" rx="8" ry="8"
        fill="#f7fbf5" stroke="#33a02c" stroke-width="2"/>
  <text x="480" y="180" text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-size="18" fill="#33a02c">
    HRR — Hybrid Resonance
  </text>
  <text x="480" y="205" text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-size="13" fill="#333333">
    ion 0.65–0.75 • S/HybridOps/E/G
  </text>

  <!-- MLR box -->
  <rect x="640" y="150" width="240" height="90" rx="8" ry="8"
        fill="#fff9f5" stroke="#e31a1c" stroke-width="2"/>
  <text x="760" y="180" text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-size="18" fill="#e31a1c">
    MLR — Mineral Lock‑In
  </text>
  <text x="760" y="205" text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-size="13" fill="#333333">
    supersaturation ≥ 0.85 • P/M/E/S
  </text>

  <!-- Horizontal arrows (regime sequence) -->
  <line x1="320" y1="195" x2="360" y2="195"
        stroke="#555555" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="600" y1="195" x2="640" y2="195"
        stroke="#555555" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Arrow marker -->
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10"
            refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L8,3 L0,6 Z" fill="#555555"/>
    </marker>
  </defs>

  <!-- Envelope transitions text -->
  <text x="320" y="235" text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-size="12" fill="#555555">
    moisture ↓
  </text>
  <text x="600" y="235" text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-size="12" fill="#555555">
    supersaturation ↑
  </text>

  <!-- Substrate transition lane -->
  <text x="480" y="280" text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-size="14" fill="#333333">
    Substrate Transition
  </text>

  <!-- Substrate boxes -->
  <rect x="80" y="310" width="240" height="70" rx="6" ry="6"
        fill="#f5f5ff" stroke="#6a3d9a" stroke-width="1.5"/>
  <text x="200" y="335" text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-size="13" fill="#333333">
    Biological Channels
  </text>
  <text x="200" y="355" text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-size="11" fill="#555555">
    P.trace_extend • G.nutrient_gradient
  </text>

  <rect x="360" y="310" width="240" height="70" rx="6" ry="6"
        fill="#f5fff5" stroke="#6a3d9a" stroke-width="1.5"/>
  <text x="480" y="335" text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-size="13" fill="#333333">
    Hybrid Layer (aligned)
  </text>
  <text x="480" y="355" text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-size="11" fill="#555555">
    S.channel_fill • HybridOps.resonance_bridge
  </text>

  <rect x="640" y="310" width="240" height="70" rx="6" ry="6"
        fill="#fff5f5" stroke="#6a3d9a" stroke-width="1.5"/>
  <text x="760" y="335" text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-size="13" fill="#333333">
    Mineral Lattice (locked)
  </text>
  <text x="760" y="355" text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-size="11" fill="#555555">
    P.front_propagate • M.domain_memory
  </text>

  <!-- Substrate arrows -->
  <line x1="320" y1="345" x2="360" y2="345"
        stroke="#555555" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="600" y1="345" x2="640" y2="345"
        stroke="#555555" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Memory path lane -->
  <text x="480" y="410" text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-size="14" fill="#333333">
    Memory Path
  </text>

  <text x="200" y="435" text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-size="11" fill="#555555">
    M.route_memory (bio)
  </text>
  <text x="480" y="435" text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-size="11" fill="#555555">
    HybridOps.memory_transfer (hybrid)
  </text>
  <text x="760" y="435" text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
        font-size="11" fill="#555555">
    M.domain_memory (mineral)
  </text>

  <line x1="240" y1="430" x2="360" y2="430"
        stroke="#999999" stroke-width="1.2" marker-end="url(#arrow)"/>
  <line x1="520" y1="430" x2="640" y2="430"
        stroke="#999999" stroke-width="1.2" marker-end="url(#arrow)"/>

</svg>
