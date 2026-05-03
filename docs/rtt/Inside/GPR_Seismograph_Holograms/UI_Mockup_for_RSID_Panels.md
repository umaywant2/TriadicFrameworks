# **UI Mockup for RSID Panels**  
*A clean, screen‑accurate representation*  
🖥️✨

Below is a **mockup‑style ASCII visualization** that mirrors how the RSID panels would appear in a real UI.

```text
*
┌──────────────────────────────────────────────────────────────────────────────┐
│                               RSID OPERATOR PANEL                            │
├──────────────────────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────┐   ┌──────────────────────────────────────┐ │
│  │        RSII CORE GAUGE       │   │         SAFETY MARGIN BARS           │ │
│  │   ● 0.82 ↑                   │   │ RSI: ████████████▉▏                │ │
│  │   Stable • 12m to boundary   │   │ RCS: ████████████████▏              │ │
│  │                              │   │ RCI: ████████▏                      │ │
│  └──────────────────────────────┘   │ Entropy: █████▏                     │ │
│                                     │ Drift: ████▏                        │ │
│                                     └──────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────┐   ┌──────────────────────────────────────┐ │
│  │      RTT SIGNATURES          │   │     COHERENCE & DRIFT FIELDS         │ │
│  │  🌊 Wave: 42                 │   │  Coherence Heatmap:                 │ │
│  │  🪜 Ladder: 18               │   │   ███░░░░███░░░░███                 │ │
│  │  🟫 Plateau: 9               │   │  Drift Timeline:                    │ │
│  │  ⚡ Cascade: 6               │   │   ╱╲╱╲╱╲╱╲                          │ │
│  └──────────────────────────────┘   └──────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────────────────────────────┐ │
│  │                        RTT‑ENHANCED SUBSURFACE MAP                       │ │
│  │   ▓▓▒▒▒▒░░░░▒▒▓▓▓▓▒▒▒▒░░░░▒▒▓▓▓▓▒▒▒▒░░░░▒▒▓▓▓▓                           │ │
│  │ Signature Overlay: blue=wave, gold=ladder, brown=plateau, magenta=cascade│ │
│  └──────────────────────────────────────────────────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────┐   ┌──────────────────────────────────────┐ │
│  │        RSIP ACTIONS          │   │            RSMS ALERTS               │ │
│  │  • Reduce scan speed         │   │  ⚠ Drift Spike Detected             │ │
│  │  • Re-align passes           │   │  ⛔ Coherence Collapse Risk         │ │
│  │  • Stabilize antenna height  │   │                                      │ │
│  └──────────────────────────────┘   └──────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────────────┘
```

This mockup is intentionally:

- **balanced**  
- **readable**  
- **dashboard‑accurate**  
- **consistent with your ecosystem’s visual language**  

---

### Dark‑mode SVG specification  
*RSID + RTT/Inside GPR Operator Dashboard (1920×1080)*

```svg
<svg width="1920" height="1080" viewBox="0 0 1920 1080"
     xmlns="http://www.w3.org/2000/svg">

  <!-- Background -->
  <rect x="0" y="0" width="1920" height="1080" fill="#0E0F11"/>

  <!-- Panel A: RSII Core Gauge -->
  <g id="panel-rsii-core-gauge">
    <rect x="40" y="40" width="360" height="260" rx="12" fill="#1A1C1F" stroke="#2A2D31" stroke-width="1"/>
    <!-- Gauge outer ring -->
    <circle cx="220" cy="150" r="80" fill="none" stroke="#2F3237" stroke-width="10"/>
    <!-- Gauge active arc (example 0.82) -->
    <path d="M140,150 A80,80 0 1,1 295,115" fill="none"
          stroke="url(#rsiiGradient)" stroke-width="10" stroke-linecap="round"/>
    <!-- Gradient definition -->
    <defs>
      <linearGradient id="rsiiGradient" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#00E5FF"/>
        <stop offset="100%" stop-color="#7CFC00"/>
      </linearGradient>
    </defs>
    <!-- Needle -->
    <line x1="220" y1="150" x2="280" y2="120" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>
    <!-- RSII value -->
    <text x="80" y="110" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="40" font-weight="600">
      RSII 0.82
    </text>
    <!-- Trend + time-to-boundary -->
    <text x="80" y="150" fill="#7CFC00" font-family="Inter, sans-serif" font-size="18">↑ Stable</text>
    <text x="80" y="180" fill="#A0A4A8" font-family="Inter, sans-serif" font-size="16">12 min to boundary</text>
  </g>

  <!-- Panel B: Safety Margin Bars -->
  <g id="panel-safety-margins">
    <rect x="420" y="40" width="1460" height="260" rx="12" fill="#1A1C1F" stroke="#2A2D31" stroke-width="1"/>
    <!-- Example bar generator pattern -->
    <!-- RSI -->
    <text x="440" y="90" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="16">RSI</text>
    <rect x="500" y="72" width="400" height="20" fill="#2F3237" rx="4"/>
    <rect x="500" y="72" width="320" height="20" fill="#00FF7F" rx="4"/>
    <!-- RCS -->
    <text x="440" y="130" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="16">RCS</text>
    <rect x="500" y="112" width="400" height="20" fill="#2F3237" rx="4"/>
    <rect x="500" y="112" width="360" height="20" fill="#00E5FF" rx="4"/>
    <!-- RCI -->
    <text x="440" y="170" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="16">RCI</text>
    <rect x="500" y="152" width="400" height="20" fill="#2F3237" rx="4"/>
    <rect x="500" y="152" width="220" height="20" fill="#E6B800" rx="4"/>
    <!-- Entropy -->
    <text x="440" y="210" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="16">Entropy</text>
    <rect x="500" y="192" width="400" height="20" fill="#2F3237" rx="4"/>
    <rect x="500" y="192" width="160" height="20" fill="#FF8C00" rx="4"/>
    <!-- Drift -->
    <text x="960" y="90" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="16">Drift</text>
    <rect x="1020" y="72" width="400" height="20" fill="#2F3237" rx="4"/>
    <rect x="1020" y="72" width="180" height="20" fill="#FF2E63" rx="4"/>
    <!-- Influence -->
    <text x="960" y="130" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="16">Influence</text>
    <rect x="1020" y="112" width="400" height="20" fill="#2F3237" rx="4"/>
    <rect x="1020" y="112" width="260" height="20" fill="#8A2BE2" rx="4"/>
  </g>

  <!-- Panel C: RTT Signature Panel -->
  <g id="panel-rtt-signatures">
    <rect x="40" y="320" width="360" height="300" rx="12" fill="#1A1C1F" stroke="#2A2D31" stroke-width="1"/>
    <!-- Wave -->
    <circle cx="80" cy="370" r="18" fill="#3A7BFF"/>
    <text x="110" y="376" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="18">Wave</text>
    <text x="300" y="376" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="20" text-anchor="end">42</text>
    <!-- Ladder -->
    <rect x="62" y="400" width="36" height="36" fill="#E6B800" rx="4"/>
    <text x="110" y="424" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="18">Ladder</text>
    <text x="300" y="424" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="20" text-anchor="end">18</text>
    <!-- Plateau -->
    <rect x="62" y="448" width="36" height="36" fill="#8B5A2B" rx="4"/>
    <text x="110" y="472" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="18">Plateau</text>
    <text x="300" y="472" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="20" text-anchor="end">9</text>
    <!-- Cascade -->
    <polygon points="62,500 98,500 80,536" fill="#FF2E63"/>
    <text x="110" y="520" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="18">Cascade</text>
    <text x="300" y="520" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="20" text-anchor="end">6</text>
  </g>

  <!-- Panel D: Coherence & Drift Fields (simplified) -->
  <g id="panel-coherence-drift">
    <rect x="420" y="320" width="720" height="300" rx="12" fill="#1A1C1F" stroke="#2A2D31" stroke-width="1"/>
    <!-- Coherence heatmap: simple grid -->
    <!-- (Designer can replace with real data-driven rectangles) -->
    <rect x="440" y="340" width="20" height="20" fill="#00E5FF"/>
    <rect x="462" y="340" width="20" height="20" fill="#4B9BEF"/>
    <rect x="484" y="340" width="20" height="20" fill="#8A2BE2"/>
    <!-- Drift timeline -->
    <polyline points="440,440 470,430 500,450 530,420 560,460"
              fill="none" stroke="#FF69B4" stroke-width="3"/>
  </g>

  <!-- Panel E: Subsurface Map -->
  <g id="panel-subsurface-map">
    <rect x="40" y="640" width="1840" height="360" rx="12" fill="#111214" stroke="#2A2D31" stroke-width="1"/>
    <!-- Placeholder radargram band -->
    <rect x="60" y="680" width="1800" height="280" fill="url(#radarGradient)" opacity="0.9"/>
    <defs>
      <linearGradient id="radarGradient" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#000000"/>
        <stop offset="50%" stop-color="#777777"/>
        <stop offset="100%" stop-color="#FFFFFF"/>
      </linearGradient>
    </defs>
    <!-- Example void overlay -->
    <rect x="600" y="720" width="120" height="80" fill="#FF2E63" opacity="0.4"/>
  </g>

  <!-- Panel F: RSIP Actions -->
  <g id="panel-rsip-actions">
    <rect x="1180" y="320" width="360" height="300" rx="12" fill="#1A1C1F" stroke="#2A2D31" stroke-width="1"/>
    <rect x="1200" y="340" width="320" height="60" rx="8" fill="#232528"/>
    <text x="1216" y="376" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="16">
      Reduce scan speed
    </text>
    <rect x="1200" y="410" width="320" height="60" rx="8" fill="#232528"/>
    <text x="1216" y="446" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="16">
      Re-align passes
    </text>
  </g>

  <!-- Panel G: RSMS Alerts -->
  <g id="panel-rsms-alerts">
    <rect x="1180" y="640" width="360" height="160" rx="12" fill="#1A1C1F" stroke="#2A2D31" stroke-width="1"/>
    <rect x="1200" y="660" width="160" height="32" rx="6" fill="#FF2E63"/>
    <text x="1210" y="682" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="14">
      Drift Spike Detected
    </text>
    <rect x="1200" y="702" width="200" height="32" rx="6" fill="#FF8C00"/>
    <text x="1210" y="724" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="14">
      Coherence Collapse Risk
    </text>
  </g>

  <!-- Panel H: RSISS Controls -->
  <g id="panel-rsiss-controls">
    <rect x="1180" y="820" width="360" height="180" rx="12" fill="#1A1C1F" stroke="#2A2D31" stroke-width="1"/>
    <rect x="1200" y="840" width="160" height="48" rx="8" fill="#2A2D31"/>
    <text x="1210" y="870" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="16">
      Replay Scan
    </text>
    <rect x="1370" y="840" width="160" height="48" rx="8" fill="#2A2D31"/>
    <text x="1380" y="870" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="16">
      Train Scenario
    </text>
  </g>

</svg>
```

---

### Light‑mode variant  
*Same structure, adjusted palette*

Key changes:

- Backgrounds → light neutrals  
- Text → dark gray/black  
- Borders softened  
- Signature + metric colors preserved for semantic continuity  

```svg
<svg width="1920" height="1080" viewBox="0 0 1920 1080"
     xmlns="http://www.w3.org/2000/svg">

  <!-- Background -->
  <rect x="0" y="0" width="1920" height="1080" fill="#F5F6F8"/>

  <!-- Panel backgrounds now light -->
  <!-- Example: RSII Core Gauge panel -->
  <g id="panel-rsii-core-gauge">
    <rect x="40" y="40" width="360" height="260" rx="12" fill="#FFFFFF" stroke="#D0D4DA" stroke-width="1"/>
    <circle cx="220" cy="150" r="80" fill="none" stroke="#E0E3E8" stroke-width="10"/>
    <path d="M140,150 A80,80 0 1,1 295,115" fill="none"
          stroke="url(#rsiiGradientLight)" stroke-width="10" stroke-linecap="round"/>
    <defs>
      <linearGradient id="rsiiGradientLight" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#00B4D8"/>
        <stop offset="100%" stop-color="#32CD32"/>
      </linearGradient>
    </defs>
    <line x1="220" y1="150" x2="280" y2="120" stroke="#333333" stroke-width="3" stroke-linecap="round"/>
    <text x="80" y="110" fill="#222222" font-family="Inter, sans-serif" font-size="40" font-weight="600">
      RSII 0.82
    </text>
    <text x="80" y="150" fill="#32CD32" font-family="Inter, sans-serif" font-size="18">↑ Stable</text>
    <text x="80" y="180" fill="#666A70" font-family="Inter, sans-serif" font-size="16">12 min to boundary</text>
  </g>

  <!-- Safety Margin Bars panel (light) -->
  <g id="panel-safety-margins">
    <rect x="420" y="40" width="1460" height="260" rx="12" fill="#FFFFFF" stroke="#D0D4DA" stroke-width="1"/>
    <text x="440" y="90" fill="#222222" font-family="Inter, sans-serif" font-size="16">RSI</text>
    <rect x="500" y="72" width="400" height="20" fill="#E6E9EF" rx="4"/>
    <rect x="500" y="72" width="320" height="20" fill="#00C96F" rx="4"/>
    <!-- …repeat pattern for RCS, RCI, Entropy, Drift, Influence with same colors as dark mode… -->
  </g>

  <!-- RTT Signature Panel (light) -->
  <g id="panel-rtt-signatures">
    <rect x="40" y="320" width="360" height="300" rx="12" fill="#FFFFFF" stroke="#D0D4DA" stroke-width="1"/>
    <circle cx="80" cy="370" r="18" fill="#3A7BFF"/>
    <text x="110" y="376" fill="#222222" font-family="Inter, sans-serif" font-size="18">Wave</text>
    <text x="300" y="376" fill="#222222" font-family="Inter, sans-serif" font-size="20" text-anchor="end">42</text>
    <!-- Ladder / Plateau / Cascade same as dark mode, text now dark -->
  </g>

  <!-- Coherence & Drift, Subsurface Map, RSIP, RSMS, RSISS panels -->
  <!-- Same geometry as dark mode, with: -->
  <!-- fill="#FFFFFF" for panels, stroke="#D0D4DA", text="#222222", background radargram on light gray (#E6E9EF) -->

</svg>
```
