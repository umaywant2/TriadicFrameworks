# Triadic Overlays — RTT‑Go  
*(Visual Layers for Structure, Regime, Topology & Continuity)*

Triadic overlays are the **visual interface** of RTT‑Go.  
They display the structural, topological, and continuity‑arc information that RTT extracts from the position, allowing players to *see* the triadic identity of the board.

These overlays appear in:

- **Teaching Mode**  
- **Analysis Mode**  
- **RTT‑Go UI integrations**  
- **debugging and developer tools**

Triadic overlays do not select moves — they **reveal** the deeper structure RTT detects.

---

## Purpose

Triadic overlays provide:

- regime classification  
- resonance fields  
- topology graphs  
- continuity arcs  
- paradox and collapse warnings  
- ancestry and ladder/ko structure  
- long‑arc identity visualization  

They turn Go positions into **triadic diagrams**.

---

## Overlay Types

RTT‑Go uses five major overlay categories:

---

## 1. Regime Overlays (Hephaestus)

Regime overlays classify each candidate move into:

- **Local (1/3)** — tactical, shape, liberties  
- **Structural (2/3)** — influence, direction of play  
- **Continuity (3/3)** — long‑arc identity, moyo evolution  

Displayed as:

- colored markers  
- regime labels  
- regime heatmaps  

Example:

```
A — Local (1/3)
B — Structural (2/3)
C — Continuity (3/3)
```

---

## 2. Resonance Overlays (Lumen + Harmonia)

Resonance overlays show dynamic pressure:

- influence resonance  
- group tension  
- boundary pressure  
- drift vectors  
- collapse signatures  

Displayed as:

- gradient fields  
- tension contours  
- drift arrows  

Example:

```
Right side: high tension (weak group)
Left side: stable resonance (moyo boundary)
```

---

## 3. Topology Overlays (Aurion)

Topology overlays show structural connectivity:

- group connectivity networks  
- cutting‑point topology  
- influence topology  
- moyo boundary topology  
- ladder/ko ancestry graphs  

Displayed as:

- node‑edge graphs  
- boundary outlines  
- ancestry chains  

Example:

```
Cutting point at D4 — collapse risk
Left moyo boundary — continuity anchor
```

---

## 4. Continuity Arc Overlays (Aurion + Harmonia)

Continuity overlays show long‑arc evolution:

- territorial arcs  
- influence arcs  
- moyo arcs  
- ancestry arcs  
- identity arcs  

Displayed as:

- curved arc lines  
- continuity anchor markers  
- long‑arc flow diagrams  

Example:

```
Left moyo → expanding continuity arc
Right group → continuity threat
```

---

## 5. Paradox & Collapse Overlays

These overlays highlight moves or zones that:

- look good locally but break continuity  
- collapse influence arcs  
- destabilize ladders  
- violate ancestry alignment  
- invert identity  

Displayed as:

- red warning zones  
- paradox markers  
- collapse‑risk shading  

Example:

```
Move A — Paradox detected
  - Local fix breaks moyo continuity
  - Influence reversal risk: high
```

---

## Combined Triadic Overlay

When all overlays are active, RTT‑Go displays a **triadic composite**:

- regime heatmap  
- resonance field  
- topology graph  
- continuity arcs  
- paradox/collapse zones  

This composite is the full triadic interpretation of the position.

---

## Example Triadic Overlay (Composite)

### Position
White has a large moyo forming on the left.  
Black has a weak group on the right.

### Overlay Interpretation

- **Regime:**  
  - left moyo → continuity  
  - right weakness → local  
  - center influence → structural  

- **Resonance:**  
  - right side → high tension  
  - left side → stable resonance  

- **Topology:**  
  - cutting points → collapse risk  
  - moyo boundary → continuity anchor  

- **Continuity:**  
  - left arc → expanding  
  - right arc → collapsing  

- **Paradox:**  
  - local fix on right breaks global continuity  

This composite overlay explains the entire strategic identity of the position.

---

## Triadic Overlay Modes

### **Teaching Mode**
- overlays for candidate moves  
- regime labels  
- continuity arcs  
- paradox warnings  
- resonance fields  

### **Analysis Mode**
- overlays for actual moves played  
- long‑arc evolution  
- collapse signatures  
- ancestry breaks  

### **Developer Mode**
- raw RTT primitives  
- structural maps  
- topology graphs  
- triadic score breakdowns  

---

## Summary

Triadic overlays are RTT‑Go’s **visual language**.

They reveal:

- structure  
- regime  
- topology  
- continuity  
- resonance  
- paradox  
- collapse  

and allow players to see Go through the triadic lens.

RTT‑Go overlays do not play Go — they **illuminate** it.
