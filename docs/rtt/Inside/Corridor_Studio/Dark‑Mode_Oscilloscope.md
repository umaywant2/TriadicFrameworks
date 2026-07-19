# 🌑 **Corridor Studio — Dark‑Mode Oscilloscope Edition**

This is the full layout — visually, conceptually, and structurally.

```
*
┌────────────────────────────────────────────────────────────────────────────┐
│  Corridor Header (task, spec, status, controls)                            │
│  ─ dark glass panel with neon accents                                      │
├────────────────────────────────────────────────────────────────────────────┤
│  LEFT: Timeline Inspector     │   CENTER: Q‑Metric Oscilloscope            │
│  ─ scrollable steps           │   ─ drift, entropy, latency, branching     │
│  ─ status badges              │   ─ rewind markers                         │
│  ─ lineage hints              │   ─ spec threshold overlays                │
│                               │   ─ hover crosshair                        │
├───────────────────────────────┴────────────────────────────────────────────┤
│  Step Details Panel (right)                                                │
│  ─ action, observation, lineage tree                                       │
│  ─ Q‑metric snapshot                                                       │
├────────────────────────────────────────────────────────────────────────────┤
│  Mini‑Map (compressed corridor)                                            │
│  ─ draggable viewport                                                      │
│  ─ zoom/pan for main oscilloscope                                          │
├────────────────────────────────────────────────────────────────────────────┤
│  VCD‑Style Status Bands                                                    │
│  ─ stable / warning / halted                                               │
│  ─ discrete colored tracks                                                 │
├────────────────────────────────────────────────────────────────────────────┤
│  Diff Panel (optional)                                                     │
│  ─ compare two corridors                                                   │
│  ─ drift deltas, entropy deltas, status diffs                              │
└────────────────────────────────────────────────────────────────────────────┘
```

Everything sits in a **dark‑mode, neon‑accented, oscilloscope‑like UI**.

---

# 🎨 **Dark‑Mode Oscilloscope Theme**

This theme is designed to feel like:

- a Tektronix scope  
- a flight‑deck instrument  
- a resonance‑aware diagnostic console  

### **Color Palette**

| Purpose | Color |
|--------|--------|
| Background | `#0b0d10` (deep black‑blue) |
| Panel glass | `#111418` |
| Neon primary | `#00eaff` (cyan) |
| Neon secondary | `#ff6bcb` (magenta) |
| Drift line | `#00eaff` |
| Entropy line | `#ffb347` |
| Latency drift | `#7fff00` |
| Branching pressure | `#ff6bcb` |
| Stable band | `#0f3d2e` |
| Warning band | `#3d2f0f` |
| Halted band | `#3d0f0f` |

### **Typography**

- **Mono:** JetBrains Mono or IBM Plex Mono  
- **Sans:** Inter or Space Grotesk  
- **Glow:** subtle text‑shadow for neon elements  

### **UI Effects**

- **Glass panels:**  
  `background: rgba(255,255,255,0.03); backdrop-filter: blur(4px);`

- **Neon edges:**  
  `box-shadow: 0 0 8px rgba(0,234,255,0.4);`

- **Oscilloscope grid:**  
  faint horizontal/vertical lines behind the waveform

---

# 🧩 **Unified Corridor Studio Page (React Layout)**

Here’s the full structure in one place — no code bloat, just the skeleton:

```tsx
export default function CorridorStudio({ trace }) {
  const [selectedStep, setSelectedStep] = useState(null);

  return (
    <div className="h-screen flex flex-col bg-[#0b0d10] text-gray-200">

      {/* HEADER */}
      <Header trace={trace} />

      {/* MAIN GRID */}
      <div className="flex flex-grow overflow-hidden">

        {/* LEFT: TIMELINE */}
        <div className="w-1/4 border-r border-gray-700 overflow-y-auto">
          <CorridorTimeline
            steps={trace.steps}
            statuses={trace.statuses}
            selectedStep={selectedStep}
            onSelectStep={setSelectedStep}
          />
        </div>

        {/* CENTER: OSCILLOSCOPE */}
        <div className="flex-grow flex flex-col overflow-hidden">
          <QMetricOscilloscope
            qHistory={trace.qHistory}
            rewinds={trace.rewinds}
            spec={trace.header.corridor_spec}
          />

          <MiniMap qHistory={trace.qHistory} />
        </div>

        {/* RIGHT: DETAILS */}
        <div className="w-1/4 border-l border-gray-700 overflow-y-auto">
          <StepDetails
            steps={trace.steps}
            qHistory={trace.qHistory}
            selectedStep={selectedStep}
          />
        </div>
      </div>

      {/* VCD STATUS BANDS */}
      <CorridorVCDView
        qHistory={trace.qHistory}
        statuses={trace.statuses}
      />

      {/* OPTIONAL DIFF PANEL */}
      {/* <CorridorDiffView left={traceA} right={traceB} /> */}
    </div>
  );
}
```

This is the **complete Corridor Studio** in one coherent layout.

---

# 🔌 **Embedding Corridor Studio into triadicframeworks.org**

Our GitHub Pages site can host this in two ways:

---

## **Option A — Embed as an iframe (recommended)**

Deploy Corridor Studio as a standalone Next.js app:

```
studio.triadicframeworks.org
```

Then embed it anywhere:

```html
<iframe
  src="https://studio.triadicframeworks.org/corridor/DEMO123"
  style="width:100%; height:90vh; border:none; border-radius:8px;"
></iframe>
```

This keeps our main site clean and lets Corridor Studio evolve independently.

---

## **Option B — Inline widget inside triadicframeworks.org**

Bundle Corridor Studio as a static JS widget:

```
/assets/corridor/studio.js
/assets/corridor/studio.css
```

Then embed:

```html
<div id="corridor-studio"></div>

<script src="/assets/corridor/studio.js"></script>
<script>
  CorridorStudio.mount("#corridor-studio", {
    traceUrl: "/traces/demo.ctf"
  });
</script>
```

This gives us a **self‑contained lab module** inside our existing pages.

---

# 🚀 What we now have

We’ve just defined:

- a **full Corridor Studio layout**  
- a **dark‑mode oscilloscope theme**  
- a **unified operator console** for RTT‑Inside corridors  
- a path to embed it into triadicframeworks.org  

This is the first **agent waveform debugger** — a real instrument for reasoning systems.
