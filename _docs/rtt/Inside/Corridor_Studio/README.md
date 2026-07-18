# Corridor Studio

## 🛑 Important! 
Drift is On-by-Default long sessions lose anchors, turn off drift.

## ✋ You *must copy and paste* this string *every time you start an AI session*:
```text
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

## ❇️ Now you are ready.

---

# **1. Corridor Studio — Page Layout (React/Next.js)**

Think of this as the cockpit for an RTT‑Inside corridor:  
left = navigation, center = waveforms, right = details, bottom = diff/minimap.

```
*
┌──────────────────────────────────────────────────────────────┐
│ Corridor Header (task, spec, status)                         │
├───────────────┬───────────────────────────────┬──────────────┤
│ Timeline      │ Q‑Metric Waveforms (D3)       │ Step Details │
│ (Inspector)   │ + Rewind Markers              │ + Lineage    │
│               │ + Spec Thresholds             │              │
├───────────────┴───────────────────────────────┴──────────────┤
│ Mini‑Map (zoom/pan)                                          │
├──────────────────────────────────────────────────────────────┤
│ Diff Panel (optional)                                        │
└──────────────────────────────────────────────────────────────┘
```

### **1.1. High‑level React layout**

```tsx
// app/corridor/[id]/studio/page.tsx
"use client";

import { CorridorViewer } from "@/components/CorridorViewer";
import { CorridorVCDView } from "@/components/CorridorVCDView";
import { CorridorDiffView } from "@/components/CorridorDiffView";
import { MiniMap } from "@/components/MiniMap";

export default function CorridorStudio({ params }) {
  const { id } = params;
  const [trace, setTrace] = useState(null);

  useEffect(() => {
    fetch(`/api/corridor/${id}`).then(r => r.json()).then(setTrace);
  }, [id]);

  if (!trace) return <div>Loading corridor…</div>;

  return (
    <div className="flex flex-col gap-4 p-4 h-screen overflow-hidden">
      <Header trace={trace} />

      <div className="grid grid-cols-3 gap-4 flex-grow min-h-0">
        <CorridorTimeline
          steps={trace.steps}
          statuses={trace.statuses}
          selectedStep={selectedStep}
          onSelectStep={setSelectedStep}
        />

        <div className="col-span-2 flex flex-col gap-4 min-h-0">
          <QMetricWaveformPanel
            qHistory={trace.qHistory}
            rewinds={trace.rewinds}
            spec={trace.header.corridor_spec}
          />

          <StepDetails
            steps={trace.steps}
            qHistory={trace.qHistory}
            selectedStep={selectedStep}
          />
        </div>
      </div>

      <MiniMap qHistory={trace.qHistory} />

      <CorridorVCDView
        qHistory={trace.qHistory}
        statuses={trace.statuses}
      />

      {/* Optional diff panel */}
      {/* <CorridorDiffView left={traceA} right={traceB} /> */}
    </div>
  );
}
```

This gives us a **full‑screen, multi‑panel studio** with:

- scrollable timeline  
- interactive waveform  
- VCD‑style status bands  
- minimap  
- diff panel (optional)  

Everything is modular.

---

# **2. Embedding Corridor Studio into triadicframeworks.org**

Our site is GitHub Pages + static HTML.  
To embed Corridor Studio, we have two options:

---

## **Option A — Embed as an iframe “lab module”**

This is the simplest and cleanest.

1. Deploy Corridor Studio as a standalone Next.js app (e.g., `studio.triadicframeworks.org`).
2. Embed it inside any page:

```html
<iframe
  src="https://studio.triadicframeworks.org/corridor/DEMO123"
  style="width:100%; height:90vh; border:none; border-radius:8px;"
></iframe>
```

This gives us:

- isolation  
- no JS conflicts  
- easy versioning  
- easy embedding in multiple pages  

---

## **Option B — Inline React bundle inside GitHub Pages**

If we want Corridor Studio *inside* the existing site:

1. Build the viewer as a standalone React bundle (Vite or Next export).  
2. Drop the compiled JS/CSS into:

```
triadicframeworks.org/assets/corridor/
```

3. Add a `<div id="corridor-studio"></div>` to our page.  
4. Hydrate it with:

```html
<script src="/assets/corridor/studio.js"></script>
<script>
  CorridorStudio.mount("#corridor-studio", {
    traceUrl: "/traces/demo.ctf"
  });
</script>
```

This gives us a **self‑contained widget** that behaves like a lab instrument.

---

# **3. Corridor Studio — Conceptual Model**

Here’s the mental model we’re building:

### **Corridor = execution manifold**  
A structured, lineage‑aware, Q‑metric‑bounded reasoning path.

### **Corridor Studio = instrumentation console**  
A place to:

- inspect  
- replay  
- compare  
- debug  
- visualize  
- rewind  

…just like hardware engineers do with VCD, waveform viewers, and trace analyzers.

### **Four views = four dimensions of stability**

| View | Purpose |
|------|---------|
| Timeline | Sequence of actions + status |
| Waveform | Q‑metric evolution (semantic drift, entropy, etc.) |
| VCD Panel | Discrete corridor states (stable/warning/halted) |
| Diff Tool | Compare two runs structurally |

Together, they form a **Resonance‑Aware Debugger**.

---

# **4. What this unlocks**

Once Corridor Studio exists, we can:

- run experiments on agent stability  
- compare different LLMs on the same corridor  
- visualize drift and entropy in real time  
- debug agent loops like hardware pipelines  
- publish corridor traces as research artifacts  
- embed live corridor monitors in our docs  

This is the first **agent waveform debugger** in the world.
