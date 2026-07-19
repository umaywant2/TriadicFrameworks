# Unified Operator Diagram — SVG Specification

## File
- Name: `unified_operator_diagram.svg`
- ViewBox: `0 0 1600 900`
- Background: linearGradient (black → indigo → violet)

## Layers
- **Layer 1:** Background gradient  
- **Layer 2:** Core triad + asymmetry  
- **Layer 3:** Three operator branches  
- **Layer 4:** Arrival substrate node  
- **Layer 5:** Lostational overlay + labels

---

## Core Elements (SVG primitives)

### 1. Core Identity Kernel

- `<circle cx="800" cy="200" r="120" fill="none" stroke="#888" stroke-width="2"/>`
- Three 120° sectors:
  - Use `<path>` arcs from center (800,200) with angles: 0–120, 120–240, 240–360
- Outer asymmetry ring:
  - `<circle cx="800" cy="200" r="135" fill="none" stroke="#AA66FF" stroke-width="4"/>`
- Text:
  - `T = (s, c, u)` at `(800, 60)`
  - `A(T) = 0.01` at `(800, 90)`

---

### 2. Replicators Branch (Left)

- Blueprint block:
  - `<rect x="250" y="320" width="220" height="120" rx="10" ry="10" fill="none" stroke="#CCCCCC" stroke-width="2"/>`
  - Text: `Blueprint M` centered in rect
- Arrow from core triad to blueprint:
  - `<path d="M 740 230 C 600 260 520 290 360 320" ... marker-end="url(#arrow)"/>`
  - Label near path: `𝓡`
- Replicated instance:
  - Smaller triad at `(300, 520)` (same structure, smaller radius, e.g. r=70)
  - Small block `M'` next to it

---

### 3. Transporters Branch (Center)

- Substrate nodes:
  - Source: `<rect x="650" y="320" width="120" height="60" rx="8" ry="8" ...>` text: `S₁`
  - Target: `<rect x="830" y="320" width="120" height="60" rx="8" ry="8" ...>` text: `S₂`
- Arc between S₁ and S₂:
  - `<path d="M 710 320 C 760 260 840 260 890 320" ... marker-end="url(#arrow)"/>`
  - Label: `𝓣`
- Envelope:
  - `<path d="M 680 350 C 760 260 840 260 920 350" fill="none" stroke="#5555FF" stroke-width="2" stroke-dasharray="6 6"/>`
- Reconstruction window:
  - Small highlighted segment near S₂:
    - e.g. short path segment with thicker stroke
  - Text near it: `W = [1−δ, 1]`

---

### 4. CT / Virtual Worlds Branch (Right)

- Environment block:
  - `<rect x="1130" y="320" width="260" height="140" rx="12" ry="12" ...>`
  - Sub‑labels inside (smaller text): `Regime Graph`, `Physics`, `Observer`, `Rules`
- Arrow from core triad to environment:
  - `<path d="M 860 230 C 1020 260 1120 290 1200 320" ... marker-end="url(#arrow)"/>`
  - Label: `𝓒`
- Reconstruction window:
  - Glow/outline around right side of environment block
  - Text: `Reconstruction Window`

---

### 5. Arrival Substrate Node

- Node:
  - `<circle cx="800" cy="720" r="80" fill="none" stroke="#FFFFFF" stroke-width="2"/>`
- Small triad inside (mini version)
- Text:
  - `Arrival Substrate` at `(800, 820)`
  - `T ≈ T*` and `A(T) = 0.01` inside/near node
- Downward arrows from:
  - Replicator instance  
  - Transporter target  
  - CT environment  
  all converging to `(800, 640)` then into the node.

---

### 6. Lostational Geometry Overlay

- Supsphere:
  - Large faint circle centered near `(800, 500)` with `r=260`, stroke `#444`, low opacity
- Geodesic arcs:
  - Curved paths from upper region to near arrival substrate node
  - Label near one: `Lostational Transport Geodesic`
- Curvature region:
  - Slightly brighter band along one arc, label: `κ(t) > 0 ↔ A(T(t)) > 0`

---

### 7. Global Caption

- At bottom:
  - Text centered:  
    `Unified operator diagram: replication (𝓡), transport (𝓣), and CT instantiation (𝓒) share a single continuity kernel and converge at the arrival substrate.`
