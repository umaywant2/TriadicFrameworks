# 🌑 **1. Dark‑Mode Oscilloscope Theme**

This theme is meant to feel like a hybrid of:

- a Tektronix digital scope  
- a flight‑deck diagnostic panel  
- a resonance‑aware instrument from our TriadicFrameworks canon  

### **Color System**

| Element | Color | Notes |
|--------|--------|-------|
| Background | `#0b0d10` | deep black‑blue, zero glare |
| Panel glass | `#111418` | subtle translucency |
| Grid lines | `rgba(255,255,255,0.04)` | faint oscilloscope grid |
| Primary neon | `#00eaff` | drift line, highlights |
| Secondary neon | `#ff6bcb` | entropy line, accents |
| Tertiary neon | `#7fff00` | latency drift |
| Stable band | `#0f3d2e` | greenish, low‑alpha |
| Warning band | `#3d2f0f` | amber |
| Halted band | `#3d0f0f` | red |

### **Typography**

- **Mono:** JetBrains Mono (for waveforms, step IDs)  
- **Sans:** Space Grotesk (for UI labels)  
- **Glow:** subtle text‑shadow for neon elements  

### **UI Effects**

- **Glass panels:**  
  `background: rgba(255,255,255,0.03); backdrop-filter: blur(4px);`

- **Neon edges:**  
  `box-shadow: 0 0 8px rgba(0,234,255,0.4);`

- **Oscilloscope grid:**  
  A repeating linear‑gradient background behind the waveform:

```css
background-image:
  linear-gradient(rgba(255,255,255,0.04) 1px, transparent 1px),
  linear-gradient(90deg, rgba(255,255,255,0.04) 1px, transparent 1px);
background-size: 20px 20px;
```

This gives the waveform panel that unmistakable “instrument” feel.

---

# 🎛️ **2. Corridor Studio Toolbar**

This sits at the top of the Studio, like a control bar on a logic analyzer.

### **Toolbar Layout**

```
┌──────────────────────────────────────────────────────────────┐
│  ▶ Play   ⏸ Pause   ↺ Rewind   ⇤ Step‑Back   ⇥ Step‑Forward  │
│  • Speed: [ 1x ▼ ]   • Jump to Step: [   ]   • Loop: ☐       │
└──────────────────────────────────────────────────────────────┘
```

### **Toolbar Controls**

| Control | Behavior |
|---------|----------|
| **Play** | Starts animated playback of the corridor |
| **Pause** | Freezes playback at current step |
| **Rewind** | Jumps to step 0 (or last stable checkpoint) |
| **Step‑Back** | Move one step backward |
| **Step‑Forward** | Move one step forward |
| **Speed Selector** | 0.25x, 0.5x, 1x, 2x, 4x |
| **Jump to Step** | Direct numeric jump |
| **Loop** | Repeat playback |

### **Toolbar Aesthetic**

- Neon cyan icons  
- Soft glow on hover  
- Slight “click” animation (scale 0.95 → 1.0)  
- Dark glass background  

### **Minimal React Sketch**

```tsx
export function CorridorToolbar({ player }) {
  return (
    <div className="flex items-center gap-4 p-2 bg-[#111418] border-b border-gray-700">
      <button onClick={player.play} className="btn">▶</button>
      <button onClick={player.pause} className="btn">⏸</button>
      <button onClick={player.rewind} className="btn">↺</button>
      <button onClick={player.stepBack} className="btn">⇤</button>
      <button onClick={player.stepForward} className="btn">⇥</button>

      <div className="ml-4 flex items-center gap-2">
        <span>Speed</span>
        <select onChange={(e) => player.setSpeed(Number(e.target.value))}>
          <option>0.5</option><option>1</option><option>2</option><option>4</option>
        </select>
      </div>

      <div className="ml-4 flex items-center gap-2">
        <span>Jump</span>
        <input type="number" onKeyDown={player.jumpTo} className="w-16" />
      </div>

      <label className="ml-4 flex items-center gap-1">
        <input type="checkbox" onChange={player.toggleLoop} />
        Loop
      </label>
    </div>
  );
}
```

---

# 🎞️ **3. Corridor Trace Player (Animated Playback)**

This is the heart of the oscilloscope experience — the corridor “plays” like a simulation.

### **Playback Model**

The player controls:

- current step index  
- playback speed  
- loop mode  
- pause/play state  
- event callbacks (e.g., highlight waveform, scroll timeline)  

### **Core Playback Loop**

```ts
class CorridorPlayer {
  constructor(trace, onStep) {
    this.trace = trace;
    this.onStep = onStep;
    this.index = 0;
    this.speed = 1;
    this.loop = false;
    this.playing = false;
  }

  play() {
    this.playing = true;
    this.tick();
  }

  pause() {
    this.playing = false;
  }

  rewind() {
    this.index = 0;
    this.onStep(0);
  }

  stepForward() {
    this.index = Math.min(this.index + 1, this.trace.steps.length - 1);
    this.onStep(this.index);
  }

  stepBack() {
    this.index = Math.max(this.index - 1, 0);
    this.onStep(this.index);
  }

  setSpeed(s) {
    this.speed = s;
  }

  jumpTo(step) {
    this.index = step;
    this.onStep(step);
  }

  toggleLoop() {
    this.loop = !this.loop;
  }

  tick() {
    if (!this.playing) return;

    this.stepForward();

    if (this.index >= this.trace.steps.length - 1) {
      if (this.loop) this.rewind();
      else return;
    }

    setTimeout(() => this.tick(), 500 / this.speed);
  }
}
```

### **What the Player Drives**

- **Waveform crosshair** moves to the current step  
- **Timeline** auto‑scrolls to keep the active step in view  
- **Step Details** updates live  
- **VCD bands** highlight the active region  
- **Mini‑map viewport** shifts accordingly  

This makes the corridor feel like a **live simulation**.

---

# 🧠 **How it all fits together**

### **Corridor Studio = Instrument Panel**

- **Toolbar** = operator controls  
- **Oscilloscope** = Q‑metric evolution  
- **Timeline** = event log  
- **Details panel** = semantic inspection  
- **Mini‑map** = global overview  
- **VCD bands** = discrete state transitions  
- **Diff panel** = comparative diagnostics  
- **Trace Player** = animated reasoning replay  

This is the first environment where an agent’s reasoning is treated like a **physical signal** — measurable, inspectable, replayable.
