# **RSID Prototype — Minimal React Skeleton**  
*Panels: RSII Gauge, Safety Bars, RTT Signatures, Coherence/Drift, Subsurface Map, RSIP Actions, RSMS Alerts, RSISS Controls*

Below is a **single‑file React layout**, followed by **modular CSS**.

---

# **1. React Component Skeleton (RSIDDashboard.jsx)**

```jsx
import React from "react";
import "./rsid.css";

export default function RSIDDashboard() {
  return (
    <div className="rsid-root">

      {/* Panel A — RSII Core Gauge */}
      <section className="panel panel-rsii">
        <h2 className="panel-title">RSII Core Gauge</h2>
        <div className="gauge-circle"></div>
        <div className="gauge-readout">
          <span className="value">0.82</span>
          <span className="trend positive">↑ Stable</span>
          <span className="subtext">12 min to boundary</span>
        </div>
      </section>

      {/* Panel B — Safety Margin Bars */}
      <section className="panel panel-safety">
        <h2 className="panel-title">Safety Margins</h2>
        <SafetyBar label="RSI" value={0.80} color="var(--green)" />
        <SafetyBar label="RCS" value={0.90} color="var(--cyan)" />
        <SafetyBar label="RCI" value={0.55} color="var(--gold)" />
        <SafetyBar label="Entropy" value={0.30} color="var(--orange)" />
        <SafetyBar label="Drift" value={0.45} color="var(--magenta)" />
        <SafetyBar label="Influence" value={0.65} color="var(--purple)" />
      </section>

      {/* Panel C — RTT Signature Panel */}
      <section className="panel panel-signatures">
        <h2 className="panel-title">RTT Signatures</h2>
        <SignatureRow icon="🌊" label="Wave" count={42} />
        <SignatureRow icon="🪜" label="Ladder" count={18} />
        <SignatureRow icon="🟫" label="Plateau" count={9} />
        <SignatureRow icon="⚡" label="Cascade" count={6} />
      </section>

      {/* Panel D — Coherence & Drift */}
      <section className="panel panel-coherence">
        <h2 className="panel-title">Coherence & Drift</h2>
        <div className="coherence-heatmap"></div>
        <div className="drift-timeline"></div>
      </section>

      {/* Panel E — Subsurface Map */}
      <section className="panel panel-map">
        <h2 className="panel-title">RTT‑Enhanced Subsurface Map</h2>
        <div className="radargram"></div>
      </section>

      {/* Panel F — RSIP Actions */}
      <section className="panel panel-rsip">
        <h2 className="panel-title">RSIP Actions</h2>
        <ActionCard text="Reduce scan speed" />
        <ActionCard text="Re-align passes" />
        <ActionCard text="Stabilize antenna height" />
      </section>

      {/* Panel G — RSMS Alerts */}
      <section className="panel panel-alerts">
        <h2 className="panel-title">RSMS Alerts</h2>
        <AlertBadge level="critical" text="Drift Spike Detected" />
        <AlertBadge level="warning" text="Coherence Collapse Risk" />
      </section>

      {/* Panel H — RSISS Controls */}
      <section className="panel panel-rsiss">
        <h2 className="panel-title">RSISS Controls</h2>
        <button className="btn">Replay Scan</button>
        <button className="btn">Train Scenario</button>
      </section>

    </div>
  );
}

/* --- Subcomponents --- */

function SafetyBar({ label, value, color }) {
  return (
    <div className="safety-row">
      <span className="safety-label">{label}</span>
      <div className="safety-bar-bg">
        <div className="safety-bar-fill" style={{ width: `${value * 100}%`, background: color }}></div>
      </div>
    </div>
  );
}

function SignatureRow({ icon, label, count }) {
  return (
    <div className="signature-row">
      <span className="sig-icon">{icon}</span>
      <span className="sig-label">{label}</span>
      <span className="sig-count">{count}</span>
    </div>
  );
}

function ActionCard({ text }) {
  return <div className="action-card">{text}</div>;
}

function AlertBadge({ level, text }) {
  return <div className={`alert-badge ${level}`}>{text}</div>;
}
```

---

# **2. Minimal CSS (rsid.css)**  
*Dark‑mode default, light‑mode ready*

```css
/* Root layout */
.rsid-root {
  display: grid;
  grid-template-columns: 400px 1fr 400px;
  grid-template-rows: auto auto auto;
  gap: 20px;
  padding: 20px;
  background: #0E0F11;
  color: #FFFFFF;
  font-family: Inter, sans-serif;
}

/* Panels */
.panel {
  background: #1A1C1F;
  border: 1px solid #2A2D31;
  border-radius: 12px;
  padding: 16px;
}

.panel-title {
  margin: 0 0 12px 0;
  font-size: 18px;
  font-weight: 600;
}

/* RSII Gauge */
.gauge-circle {
  width: 140px;
  height: 140px;
  border-radius: 50%;
  border: 10px solid #2F3237;
  margin: 0 auto;
}

.gauge-readout {
  text-align: center;
  margin-top: 12px;
}

.gauge-readout .value {
  font-size: 36px;
  font-weight: 700;
}

.trend.positive {
  color: #7CFC00;
}

.subtext {
  color: #A0A4A8;
  font-size: 14px;
}

/* Safety Bars */
.safety-row {
  display: flex;
  align-items: center;
  margin: 8px 0;
}

.safety-label {
  width: 80px;
}

.safety-bar-bg {
  flex: 1;
  height: 12px;
  background: #2F3237;
  border-radius: 4px;
}

.safety-bar-fill {
  height: 12px;
  border-radius: 4px;
}

/* Signature Panel */
.signature-row {
  display: flex;
  justify-content: space-between;
  margin: 8px 0;
}

.sig-icon {
  font-size: 24px;
}

.sig-label {
  flex: 1;
  margin-left: 8px;
}

.sig-count {
  font-weight: 700;
}

/* Coherence & Drift */
.coherence-heatmap {
  height: 120px;
  background: linear-gradient(90deg, #00E5FF, #8A2BE2);
  border-radius: 6px;
  margin-bottom: 12px;
}

.drift-timeline {
  height: 80px;
  background: #232528;
  border-radius: 6px;
}

/* Subsurface Map */
.radargram {
  height: 240px;
  background: linear-gradient(90deg, #000, #777, #FFF);
  border-radius: 6px;
}

/* RSIP Actions */
.action-card {
  background: #232528;
  padding: 12px;
  border-radius: 8px;
  margin: 8px 0;
}

/* Alerts */
.alert-badge {
  padding: 8px 12px;
  border-radius: 6px;
  margin: 6px 0;
  font-weight: 600;
}

.alert-badge.critical {
  background: #FF2E63;
}

.alert-badge.warning {
  background: #FF8C00;
}

/* RSISS Controls */
.btn {
  background: #2A2D31;
  color: #FFFFFF;
  padding: 10px 16px;
  border-radius: 8px;
  border: none;
  margin-right: 12px;
  cursor: pointer;
}
```
