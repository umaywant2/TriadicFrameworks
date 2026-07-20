# Research Toolbox Glyph — Animation Spec

**Glyph:** `research_toolbox_glyph_animated.svg`  
**Module:** Research Toolbox (research-toolbox)  
**Purpose:** Subtle triadic motion indicating **substrate + RTT/1/2/3 engine** without visual noise.

---

## 1. Elements

**Core elements:**

- **Outer ring:**  
  - ID: `outer-ring`  
  - Shape: circle, radius ≈ 90, centered at (120, 120)  
  - Stroke: triadic gradient (`#7C4DFF → #40C4FF → #B388FF`)

- **RTT nodes:**  
  - RTT/1 (top), RTT/2 (bottom-left), RTT/3 (bottom-right)  
  - Class: `glyph-node rtt-node rtt-node-[1|2|3]`  
  - Shape: circle, radius ≈ 10–12  
  - Stroke: `#7C4DFF` base

- **Substrate node:**  
  - ID: `substrate-pulse` (group)  
  - Inner circle radius ≈ 14  
  - Label: `S1–S4`

- **Orbits:**  
  - 3 dashed circles (r ≈ 60, 40, 22)  
  - Class: `glyph-orbit`  
  - Stroke: `#2E2E5E`, dashed

---

## 2. Animations

### 2.1 Outer ring rotation

- **Target:** `#outer-ring`  
- **Keyframes:** `@keyframes spin`  
- **Behavior:** continuous, slow rotation

```css
#outer-ring {
  transform-origin: 120px 120px;
  animation: spin 18s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}
```

**Semantics:**  
- Represents **ongoing research flow** and **triadic engine cycling**.

---

### 2.2 Substrate pulse

- **Target:** `#substrate-pulse` (group)  
- **Keyframes:** `@keyframes pulse`  
- **Behavior:** gentle scale + opacity pulse

```css
#substrate-pulse {
  transform-origin: 120px 120px;
  animation: pulse 4.5s ease-in-out infinite;
}

@keyframes pulse {
  0%   { transform: scale(1);   opacity: 0.5; }
  50%  { transform: scale(1.15); opacity: 1.0; }
  100% { transform: scale(1);   opacity: 0.5; }
}
```

**Semantics:**  
- Indicates the **four-source substrate (S1–S4)** as a living, active base.

---

### 2.3 RTT node glow (triadic stagger)

- **Targets:** `.rtt-node`, with subclasses `.rtt-node-1`, `.rtt-node-2`, `.rtt-node-3`  
- **Keyframes:** `@keyframes rttGlow`  
- **Behavior:** staggered stroke-width + color glow

```css
.rtt-node {
  animation: rttGlow 6s ease-in-out infinite;
}

.rtt-node-1 { animation-delay: 0s; }
.rtt-node-2 { animation-delay: 1s; }
.rtt-node-3 { animation-delay: 2s; }

@keyframes rttGlow {
  0%   { stroke-width: 1.4; stroke: #7C4DFF; }
  40%  { stroke-width: 2.2; stroke: #B388FF; }
  100% { stroke-width: 1.4; stroke: #7C4DFF; }
}
```

**Semantics:**

- **RTT/1 → RTT/2 → RTT/3** firing sequence.  
- Shows the **engine as triadic, not linear**.

---

## 3. Motion constraints

- **No translation** of nodes or labels.  
- **No flashing** or high-frequency flicker.  
- **No color inversion**; stay within dark + triadic accent palette.  
- Animation must remain **subtle**, suitable for a hero or badge context.

---

## 4. Accessibility notes

- Motion is **slow and low-amplitude** to avoid distraction.  
- All critical semantics (RTT/1, RTT/2, RTT/3, S1–S4) are readable **without animation**.  
- The static glyph (`research_toolbox_glyph.svg`) is the canonical fallback.
