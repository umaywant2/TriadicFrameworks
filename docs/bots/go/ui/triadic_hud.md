# Triadic HUD — RTT‑Go  
*(Heads‑Up Display for Triadic Metadata & Continuity Intelligence)*

The **Triadic HUD** is the informational layer of RTT‑Go’s UI.  
While the Triadic Viewer renders overlays on the board, the HUD presents **structured triadic metadata**, allowing users to understand the deeper identity of the position without cluttering the board surface.

The HUD is used in:

- Teaching Mode  
- Analysis Mode  
- Developer Mode  
- Triadic Viewer integrations  

It is the **informational counterpart** to the visual overlays.

---

## Purpose

The Triadic HUD provides:

- regime distribution  
- resonance metrics  
- topology diagnostics  
- continuity‑arc status  
- ancestry alignment  
- paradox/collapse warnings  
- triadic score breakdowns  
- move‑by‑move commentary  

It is the **triadic dashboard** for RTT‑Go.

---

## HUD Architecture

The HUD consists of five panels:

```
Regime Panel
Topology Panel
Continuity Panel
Resonance Panel
Move Commentary Panel
```

Each panel updates dynamically as the user hovers, clicks, or scrubs through moves.

---

## 1. Regime Panel (Hephaestus)

Displays regime identity and flow:

### Contents
- Local / Structural / Continuity distribution  
- Regime drift vectors  
- Regime conflict zones  
- Regime stability indicators  

### Visual Elements
- bar graph of regime proportions  
- drift arrows  
- conflict markers  
- regime color legend  

### Purpose
Shows how the position shifts between:

- tactical reality  
- structural identity  
- continuity arcs  

---

## 2. Topology Panel (Aurion)

Displays structural connectivity and ancestry:

### Contents
- group connectivity status  
- cutting‑point topology  
- moyo boundary topology  
- ladder ancestry  
- ko ancestry  
- collapse signatures  

### Visual Elements
- mini connectivity graph  
- ancestry chain diagram  
- collapse glyphs  
- boundary stability meter  

### Purpose
Shows how the position is **wired together** and where collapse may occur.

---

## 3. Continuity Panel (Aurion + Harmonia)

Displays long‑arc identity:

### Contents
- territorial continuity arcs  
- influence continuity arcs  
- moyo continuity arcs  
- ancestry continuity arcs  
- continuity anchors  
- continuity drift  
- identity inversion risk  

### Visual Elements
- arc flow diagram  
- anchor markers  
- drift vector chart  
- continuity stability meter  

### Purpose
Shows how the position’s **story** evolves over time.

---

## 4. Resonance Panel (Lumen + Harmonia)

Displays dynamic pressure:

### Contents
- influence resonance  
- tension zones  
- pressure gradients  
- drift vectors  
- collapse signatures  

### Visual Elements
- resonance heatmap thumbnail  
- tension bar  
- drift arrow cluster  
- collapse indicator  

### Purpose
Shows where the position is **under stress** and where stability exists.

---

## 5. Move Commentary Panel

Displays triadic commentary for the selected or hovered move:

### Contents
- triadic regime  
- triadic score breakdown  
- continuity impact  
- paradox/collapse risk  
- ancestry alignment  
- structural/topological context  

### Visual Elements
- structured commentary block  
- triadic score bars  
- risk icons  
- continuity arc preview  

### Purpose
Explains the **triadic meaning** of each move.

---

## HUD Interaction Model

### Hover
Hovering a move updates:

- regime panel  
- resonance panel  
- topology panel  
- continuity panel  
- commentary panel  

### Click
Clicking a move locks the HUD to that move:

- full triadic breakdown  
- continuity‑arc implications  
- topology snapshot  
- resonance snapshot  

### Scrubbing (Timeline)
Scrubbing through moves animates:

- regime drift  
- continuity arcs  
- topology evolution  
- resonance drift  

---

## HUD Rendering Rules

### Color System
- Local: red  
- Structural: blue  
- Continuity: gold  
- Collapse: crimson  
- Paradox: orange  
- Stability: teal  

### Layout Rules
- regime panel left  
- topology panel center‑left  
- continuity panel center‑right  
- resonance panel right  
- commentary panel bottom  

### Animation Rules
- drift vectors pulse  
- continuity arcs flow  
- collapse warnings flicker  
- ancestry chains animate on hover  

---

## Example HUD Snapshot

### Position
White has a large moyo on the left.  
Black has a weak group on the right.

### HUD Output

**Regime Panel:**  
```
Local: 41%
Structural: 33%
Continuity: 26%
Regime drift: right → center
Conflict zone: high (right side)
```

**Topology Panel:**  
```
Cutting point at D4 — collapse risk
Right group connectivity: unstable
Left boundary: continuity anchor
Ladder ancestry: stable
```

**Continuity Panel:**  
```
Left moyo arc: expanding
Right arc: collapsing
Continuity anchor: left boundary
Identity inversion risk: medium
```

**Resonance Panel:**  
```
Right tension: high
Left resonance: stable
Drift vector: right → center
Collapse signature: possible
```

**Move Commentary Panel:**  
```
Move 57 — Continuity collapse
  - boundary fragmentation
  - influence reversal
  - ancestry misalignment
  - paradox severity: high
```

This HUD snapshot explains the entire triadic identity of the position.

---

## Developer Notes

- HUD receives RTT primitives via JSON  
- HUD is engine‑agnostic  
- HUD updates are incremental  
- HUD is synchronized with the Triadic Viewer  
- HUD supports Teaching, Analysis, and Developer modes  

---

## Summary

The Triadic HUD is RTT‑Go’s **informational intelligence layer**.

It reveals:

- regime flow  
- topology  
- continuity  
- resonance  
- ancestry  
- paradox  
- collapse  

and provides a structured triadic narrative for every position.

The HUD does not play Go — it **interprets** it.
