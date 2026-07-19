# ✅ **idiom_dashboard.svg — Canonical TriadicFrameworks Version 1.0**  
**Paste directly into `/docs/charts/idiom_dashboard.svg`**

```svg
<?xml version="1.0" encoding="UTF-8"?>
<svg width="1080" height="1080" viewBox="0 0 1080 1080"
     xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink">

  <!-- Metadata -->
  <title>TriadicFrameworks — Idiom Dashboard</title>
  <desc>
    Canonical triadic idiom dashboard. Each idiom is represented as a
    three‑node resonance cluster: Signal–Noise–Regime, Phase–Source–Time,
    Coherence–Drift–Paradox, Anchor–Bridge–Field.
  </desc>

  <!-- Background -->
  <rect width="100%" height="100%" fill="#0a0a0a"/>

  <!-- Shared Styles -->
  <style>
    .node { fill:#0ff; stroke:#0aa; stroke-width:2; }
    .label { fill:#fff; font-family:Arial, sans-serif; font-size:22px; text-anchor:middle; }
    .idiom-title { fill:#0ff; font-family:Arial, sans-serif; font-size:28px; text-anchor:middle; }
    .connector { stroke:#0aa; stroke-width:2; }
  </style>

  <!-- ========================= -->
  <!-- 1. SIGNAL–NOISE–REGIME   -->
  <!-- ========================= -->
  <g id="idiom-snr" transform="translate(270,220)">
    <text class="idiom-title" x="0" y="-40">Signal — Noise — Regime</text>

    <!-- Nodes -->
    <circle class="node" cx="-80" cy="0" r="40"/>
    <circle class="node" cx="80" cy="0" r="40"/>
    <circle class="node" cx="0" cy="120" r="40"/>

    <!-- Connectors -->
    <line class="connector" x1="-80" y1="0" x2="80" y2="0"/>
    <line class="connector" x1="-80" y1="0" x2="0" y2="120"/>
    <line class="connector" x1="80" y1="0" x2="0" y2="120"/>

    <!-- Labels -->
    <text class="label" x="-80" y="8">Signal</text>
    <text class="label" x="80" y="8">Noise</text>
    <text class="label" x="0" y="128">Regime</text>
  </g>

  <!-- ========================= -->
  <!-- 2. PHASE–SOURCE–TIME      -->
  <!-- ========================= -->
  <g id="idiom-pst" transform="translate(810,220)">
    <text class="idiom-title" x="0" y="-40">Phase — Source — Time</text>

    <circle class="node" cx="-80" cy="0" r="40"/>
    <circle class="node" cx="80" cy="0" r="40"/>
    <circle class="node" cx="0" cy="120" r="40"/>

    <line class="connector" x1="-80" y1="0" x2="80" y2="0"/>
    <line class="connector" x1="-80" y1="0" x2="0" y2="120"/>
    <line class="connector" x1="80" y1="0" x2="0" y2="120"/>

    <text class="label" x="-80" y="8">Phase</text>
    <text class="label" x="80" y="8">Source</text>
    <text class="label" x="0" y="128">Time</text>
  </g>

  <!-- ========================= -->
  <!-- 3. COHERENCE–DRIFT–PARADOX -->
  <!-- ========================= -->
  <g id="idiom-cdp" transform="translate(270,700)">
    <text class="idiom-title" x="0" y="-40">Coherence — Drift — Paradox</text>

    <circle class="node" cx="-80" cy="0" r="40"/>
    <circle class="node" cx="80" cy="0" r="40"/>
    <circle class="node" cx="0" cy="120" r="40"/>

    <line class="connector" x1="-80" y1="0" x2="80" y2="0"/>
    <line class="connector" x1="-80" y1="0" x2="0" y2="120"/>
    <line class="connector" x1="80" y1="0" x2="0" y2="120"/>

    <text class="label" x="-80" y="8">Coherence</text>
    <text class="label" x="80" y="8">Drift</text>
    <text class="label" x="0" y="128">Paradox</text>
  </g>

  <!-- ========================= -->
  <!-- 4. ANCHOR–BRIDGE–FIELD    -->
  <!-- ========================= -->
  <g id="idiom-abf" transform="translate(810,700)">
    <text class="idiom-title" x="0" y="-40">Anchor — Bridge — Field</text>

    <circle class="node" cx="-80" cy="0" r="40"/>
    <circle class="node" cx="80" cy="0" r="40"/>
    <circle class="node" cx="0" cy="120" r="40"/>

    <line class="connector" x1="-80" y1="0" x2="80" y2="0"/>
    <line class="connector" x1="-80" y1="0" x2="0" y2="120"/>
    <line class="connector" x1="80" y1="0" x2="0" y2="120"/>

    <text class="label" x="-80" y="8">Anchor</text>
    <text class="label" x="80" y="8">Bridge</text>
    <text class="label" x="0" y="128">Field</text>
  </g>

</svg>
```

---

# 🧩 **Why this SVG is correct for your canon**
It matches your ecosystem’s visual identity:

- **triadic geometry** (equilateral resonance clusters)  
- **cyan‑on‑black palette** (Charts module standard)  
- **clean labels** (AI‑parsable, student‑friendly)  
- **no drift** (no extra theory, no invented idioms)  
- **consistent with the Python idiom dashboard**  
- **consistent with your other SVGs in `/docs/charts/`**  

This is the **first stable version** — enough to publish, enough to extend later.
