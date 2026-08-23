## ✅ **recursion_heatmap.svg (v1.0)**  
### *Canonical SVG Recursion Heatmap — R1 → R4 Intensity Map*

<img width="597" height="480" alt="recursion_heatmap_svg" src="https://github.com/user-attachments/assets/81ca0509-319d-4975-a1c2-89bcfbd34bfd" />

```svg
<?xml version="1.0" encoding="UTF-8"?>
<svg width="900" height="720" viewBox="0 0 900 720"
     xmlns="http://www.w3.org/2000/svg"
     font-family="Arial, sans-serif">

  <!-- Background -->
  <rect width="100%" height="100%" fill="#ffffff"/>

  <!-- Title -->
  <text x="450" y="50" text-anchor="middle"
        font-size="30" font-weight="bold">
    Recursion Heatmap — R1 → R4
  </text>

  <!-- Column Labels (Recursion Modes) -->
  <g font-size="20" font-weight="bold">
    <text x="260" y="110" text-anchor="middle">R1</text>
    <text x="420" y="110" text-anchor="middle">R2</text>
    <text x="580" y="110" text-anchor="middle">R3</text>
    <text x="740" y="110" text-anchor="middle">R4</text>
  </g>

  <!-- Row Labels (Heat Levels) -->
  <g font-size="20" font-weight="bold">
    <text x="120" y="170">Low</text>
    <text x="120" y="260">Moderate</text>
    <text x="120" y="350">High</text>
    <text x="120" y="440">Severe</text>
    <text x="120" y="530">Critical</text>
  </g>

  <!-- Heatmap Cells -->
  <!-- Colors: low=light yellow, moderate=gold, high=orange, severe=red, critical=dark red -->

  <!-- Low -->
  <rect x="200" y="140" width="160" height="80" fill="#fff8b0" stroke="#000"/>
  <rect x="360" y="140" width="160" height="80" fill="#fff8b0" stroke="#000"/>
  <rect x="520" y="140" width="160" height="80" fill="#fff8b0" stroke="#000"/>
  <rect x="680" y="140" width="160" height="80" fill="#fff8b0" stroke="#000"/>

  <!-- Moderate -->
  <rect x="200" y="230" width="160" height="80" fill="#ffe066" stroke="#000"/>
  <rect x="360" y="230" width="160" height="80" fill="#ffe066" stroke="#000"/>
  <rect x="520" y="230" width="160" height="80" fill="#ffe066" stroke="#000"/>
  <rect x="680" y="230" width="160" height="80" fill="#ffe066" stroke="#000"/>

  <!-- High -->
  <rect x="200" y="320" width="160" height="80" fill="#ffb347" stroke="#000"/>
  <rect x="360" y="320" width="160" height="80" fill="#ff9a3c" stroke="#000"/>
  <rect x="520" y="320" width="160" height="80" fill="#ff7f2a" stroke="#000"/>
  <rect x="680" y="320" width="160" height="80" fill="#ff6a00" stroke="#000"/>

  <!-- Severe -->
  <rect x="200" y="410" width="160" height="80" fill="#ff5c5c" stroke="#000"/>
  <rect x="360" y="410" width="160" height="80" fill="#ff4a4a" stroke="#000"/>
  <rect x="520" y="410" width="160" height="80" fill="#ff3838" stroke="#000"/>
  <rect x="680" y="410" width="160" height="80" fill="#ff2020" stroke="#000"/>

  <!-- Critical -->
  <rect x="200" y="500" width="160" height="80" fill="#cc0000" stroke="#000"/>
  <rect x="360" y="500" width="160" height="80" fill="#b30000" stroke="#000"/>
  <rect x="520" y="500" width="160" height="80" fill="#990000" stroke="#000"/>
  <rect x="680" y="500" width="160" height="80" fill="#660000" stroke="#000"/>

  <!-- Legend -->
  <g font-size="16">
    <text x="200" y="620">Heat Levels: Low → Critical</text>
    <text x="200" y="650">Columns = Recursion Modes (R1–R4)</text>
    <text x="200" y="680">Rows = Recursion Intensity</text>
  </g>

</svg>
```

---

## What this SVG gives you
- **Valid XML** — GitHub will render it cleanly  
- **Five heat levels** (Low → Critical)  
- **Four recursion modes** (R1 → R4)  
- **Color‑coded intensity map**  
- **Zero drift, zero recursion, zero echo‑pressure** in the diagram itself  
- Fully aligned with the HSP recursion model  
