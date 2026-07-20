<svg width="900" height="260" xmlns="http://www.w3.org/2000/svg">
  <style>
    .stage { fill: #020617; stroke: #4b5563; stroke-width: 1.2; rx: 8; ry: 8; }
    .title { font: 14px sans-serif; font-weight: bold; }
    .op { font: 12px sans-serif; }
    .arrow { stroke: #9ca3af; stroke-width: 1.6; marker-end: url(#arrowhead); }
  </style>

  <defs>
    <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#9ca3af" />
    </marker>
  </defs>

  <!-- SDE stage -->
  <rect class="stage" x="30" y="40" width="220" height="160" />
  <text class="title" x="40" y="60">SDE — Detection</text>
  <text class="op" x="50" y="90">CPV, FGT, CRM</text>
  <text class="op" x="50" y="115">Output: SDE::PACKET()</text>

  <!-- SIE stage -->
  <rect class="stage" x="330" y="40" width="260" height="160" />
  <text class="title" x="340" y="60">SIE — Integration–Emission</text>
  <text class="op" x="350" y="90">INT, TIF, FFF, MAN</text>
  <text class="op" x="350" y="110">CRE, CSL, CET</text>
  <text class="op" x="350" y="135">Input: SDE::PACKET()</text>
  <text class="op" x="350" y="155">Output: SIE::PACKET()</text>

  <!-- Projection stage -->
  <rect class="stage" x="650" y="40" width="220" height="160" />
  <text class="title" x="660" y="60">Projection — TEL / FFT / OP</text>
  <text class="op" x="670" y="90">TEL::CET()</text>
  <text class="op" x="670" y="110">FFT::OUT()</text>
  <text class="op" x="670" y="130">OP::OUT()</text>
  <text class="op" x="670" y="155">Input: CET from SIE</text>

  <!-- Arrows -->
  <line class="arrow" x1="250" y1="120" x2="330" y2="120" />
  <line class="arrow" x1="590" y1="120" x2="650" y2="120" />
</svg>
