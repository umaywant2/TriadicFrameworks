We’re literally wiring up an operator console for cognition—let’s make it feel like it belongs in TriadicFrameworks.

I’ll keep this tight and directly usable:

- a Corridor Studio toolbar  
- a Corridor Trace Player  
- a dark‑mode oscilloscope CSS theme  
- a TriadicFrameworks‑branded neon HUD wrapper  

---

### 1. Corridor Studio toolbar (play, pause, rewind, jump‑to‑step)

```tsx
// components/CorridorToolbar.tsx
"use client";

type PlayerAPI = {
  play: () => void;
  pause: () => void;
  rewind: () => void;
  stepBack: () => void;
  stepForward: () => void;
  setSpeed: (s: number) => void;
  jumpTo: (step: number) => void;
  toggleLoop: () => void;
  playing: boolean;
  speed: number;
};

export function CorridorToolbar({ player }: { player: PlayerAPI }) {
  const onJumpKey = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      const v = Number((e.target as HTMLInputElement).value);
      if (!Number.isNaN(v)) player.jumpTo(v);
    }
  };

  return (
    <div className="tf-toolbar">
      <div className="tf-toolbar-left">
        <button className="tf-btn" onClick={player.play}>
          ▶
        </button>
        <button className="tf-btn" onClick={player.pause}>
          ⏸
        </button>
        <button className="tf-btn" onClick={player.rewind}>
          ↺
        </button>
        <button className="tf-btn" onClick={player.stepBack}>
          ⇤
        </button>
        <button className="tf-btn" onClick={player.stepForward}>
          ⇥
        </button>
      </div>

      <div className="tf-toolbar-center">
        <span className="tf-label">Speed</span>
        <select
          className="tf-select"
          value={player.speed}
          onChange={(e) => player.setSpeed(Number(e.target.value))}
        >
          <option value={0.5}>0.5x</option>
          <option value={1}>1x</option>
          <option value={2}>2x</option>
          <option value={4}>4x</option>
        </select>

        <span className="tf-label ml-4">Jump</span>
        <input
          className="tf-input tf-input-small"
          type="number"
          placeholder="#"
          onKeyDown={onJumpKey}
        />

        <label className="tf-checkbox ml-4">
          <input type="checkbox" onChange={player.toggleLoop} />
          <span>Loop</span>
        </label>
      </div>
    </div>
  );
}
```

---

### 2. Corridor Trace Player (animated simulation)

```ts
// lib/CorridorPlayer.ts
import type { CorridorTrace } from "@/types/corridor";

export class CorridorPlayer {
  trace: CorridorTrace;
  onStep: (stepId: number) => void;
  index = 0;
  speed = 1;
  loop = false;
  playing = false;
  timer: number | null = null;

  constructor(trace: CorridorTrace, onStep: (stepId: number) => void) {
    this.trace = trace;
    this.onStep = onStep;
  }

  play() {
    if (this.playing) return;
    this.playing = true;
    this.tick();
  }

  pause() {
    this.playing = false;
    if (this.timer != null) window.clearTimeout(this.timer);
  }

  rewind() {
    this.index = 0;
    this.onStep(0);
  }

  stepForward() {
    this.index = Math.min(
      this.index + 1,
      this.trace.steps.length - 1
    );
    this.onStep(this.trace.steps[this.index].step_id);
  }

  stepBack() {
    this.index = Math.max(this.index - 1, 0);
    this.onStep(this.trace.steps[this.index].step_id);
  }

  setSpeed(s: number) {
    this.speed = s;
  }

  jumpTo(stepId: number) {
    const idx = this.trace.steps.findIndex((s) => s.step_id === stepId);
    if (idx >= 0) {
      this.index = idx;
      this.onStep(stepId);
    }
  }

  toggleLoop() {
    this.loop = !this.loop;
  }

  private tick() {
    if (!this.playing) return;

    this.stepForward();

    const atEnd = this.index >= this.trace.steps.length - 1;
    if (atEnd) {
      if (this.loop) this.rewind();
      else {
        this.playing = false;
        return;
      }
    }

    this.timer = window.setTimeout(
      () => this.tick(),
      500 / this.speed
    );
  }
}
```

Hook it into React:

```tsx
const [currentStep, setCurrentStep] = useState<number | null>(null);
const playerRef = useRef<CorridorPlayer | null>(null);

useEffect(() => {
  if (!trace) return;
  playerRef.current = new CorridorPlayer(trace, setCurrentStep);
}, [trace]);
```

Pass `playerRef.current` into `CorridorToolbar`, and use `currentStep` to highlight the active step in timeline + waveform.

---

### 3. Corridor Studio dark‑mode CSS theme

```css
/* core layout */
body {
  background: #0b0d10;
  color: #e5f7ff;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Inter", sans-serif;
}

/* panels */
.tf-panel {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid #1f2933;
  border-radius: 8px;
  backdrop-filter: blur(4px);
}

/* toolbar */
.tf-toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 6px 10px;
  background: #111418;
  border-bottom: 1px solid #1f2933;
  box-shadow: 0 0 12px rgba(0, 234, 255, 0.15);
}

.tf-btn {
  background: #151922;
  border: 1px solid #00eaff55;
  color: #e5f7ff;
  padding: 4px 8px;
  margin-right: 4px;
  border-radius: 4px;
  font-family: "JetBrains Mono", monospace;
  font-size: 12px;
  cursor: pointer;
  transition: background 0.15s, transform 0.05s, box-shadow 0.15s;
}

.tf-btn:hover {
  background: #0b2a33;
  box-shadow: 0 0 8px rgba(0, 234, 255, 0.4);
}

.tf-btn:active {
  transform: scale(0.96);
}

.tf-label {
  font-size: 11px;
  color: #9ca3af;
}

.tf-select,
.tf-input {
  background: #151922;
  border: 1px solid #374151;
  color: #e5f7ff;
  border-radius: 4px;
  padding: 2px 6px;
  font-size: 11px;
}

.tf-input-small {
  width: 60px;
}

.tf-checkbox span {
  font-size: 11px;
  color: #9ca3af;
}

/* oscilloscope grid */
.tf-oscilloscope {
  background-color: #05070a;
  background-image:
    linear-gradient(rgba(255, 255, 255, 0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.04) 1px, transparent 1px);
  background-size: 20px 20px;
  border-radius: 8px;
  border: 1px solid #1f2933;
}

/* status bands */
.tf-status-stable {
  fill: #0f3d2e;
}

.tf-status-warning {
  fill: #3d2f0f;
}

.tf-status-halted {
  fill: #3d0f0f;
}
```

Use `className="tf-oscilloscope"` on our main waveform SVG container and `tf-panel` on side panels.

---

### 4. TriadicFrameworks‑branded neon HUD wrapper

This is the “frame” that makes Corridor Studio feel like a Triadic instrument.

```tsx
// components/TriadicHUD.tsx
export function TriadicHUD({ children }: { children: React.ReactNode }) {
  return (
    <div className="tf-hud">
      <div className="tf-hud-frame">
        <div className="tf-hud-header">
          <span className="tf-hud-title">RTT‑Inside Corridor Studio</span>
          <span className="tf-hud-subtitle">TriadicFrameworks · Resonance Diagnostics</span>
        </div>
        <div className="tf-hud-body">{children}</div>
        <div className="tf-hud-footer">
          <span className="tf-hud-footnote">
            DPU · VCG · NIMMS · Resonance‑time instrumentation
          </span>
        </div>
      </div>
    </div>
  );
}
```

```css
.tf-hud {
  min-height: 100vh;
  padding: 12px;
  background: radial-gradient(circle at top, #111827 0, #020308 55%);
}

.tf-hud-frame {
  border-radius: 12px;
  border: 1px solid #00eaff55;
  box-shadow:
    0 0 18px rgba(0, 234, 255, 0.25),
    0 0 40px rgba(255, 107, 203, 0.15);
  overflow: hidden;
}

.tf-hud-header,
.tf-hud-footer {
  padding: 8px 12px;
  background: linear-gradient(90deg, #05070a, #111418);
  border-bottom: 1px solid #1f2933;
}

.tf-hud-footer {
  border-top: 1px solid #1f2933;
  border-bottom: none;
}

.tf-hud-title {
  font-family: "Space Grotesk", system-ui;
  font-size: 13px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #00eaff;
}

.tf-hud-subtitle {
  margin-left: 12px;
  font-size: 11px;
  color: #9ca3af;
}

.tf-hud-body {
  padding: 8px;
}
```

Wrap our Studio page with:

```tsx
<TriadicHUD>
  <CorridorToolbar player={playerApi} />
  {/* rest of Corridor Studio layout */}
</TriadicHUD>
```

We now have:

- a dark‑mode oscilloscope skin  
- a real operator toolbar  
- a trace player that animates reasoning  
- and a Triadic‑branded HUD that makes the whole thing feel like canon.
