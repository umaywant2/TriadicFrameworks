# Regime Maps — RTT‑Go Analysis  
*(Go Bot Module)*

Regime maps visualize how **local**, **structural**, and **continuity** forces interact across the Go board.  
They are the RTT mechanism for understanding *what kind of move* each candidate represents and *how the position’s identity is distributed*.

Where:

- **Lumen** extracts structure,  
- **Hephaestus** assigns regime identity,  
- **Aurion** reveals topology and collapse risk,  

**Regime maps show the spatial distribution of triadic regimes across the board.**

They are essential for:

- continuity‑preserving move selection  
- paradox detection  
- long‑arc strategy analysis  
- teaching/analysis overlays  
- debugging RTT behavior  

---

## Purpose

Regime maps provide:

- spatial regime classification  
- local/structural/continuity weighting  
- regime conflict detection  
- regime drift visualization  
- regime‑aligned move clustering  

They allow RTT to interpret Go positions as **triadic landscapes**, not isolated tactical snapshots.

---

## Regime Types

### **1/3 — Local Regime**
Local regime zones include:

- cuts  
- ataris  
- shape defects  
- tactical pressure  
- liberty races  
- snapback zones  

These areas represent **immediate tactical reality**.

---

### **2/3 — Structural Regime**
Structural regime zones include:

- influence fields  
- moyo boundaries  
- direction of play  
- framework identity  
- large‑scale shape  

These areas represent **global positional structure**.

---

### **3/3 — Continuity Regime**
Continuity regime zones include:

- long‑arc territorial evolution  
- ancestry alignment  
- continuity anchors  
- framework evolution  
- collapse‑risk boundaries  

These areas represent **the identity of the position over time**.

---

## Regime Map Construction

Regime maps are built from:

- Lumen’s structural extraction  
- Hephaestus’s regime classification  
- Aurion’s topology and ancestry  
- historical continuity  
- engine influence maps (KataGo) or RTT‑computed maps (Leela Zero / PhoenixGo)

The RTT shim synthesizes these into a unified regime map.

---

## Regime Map Layers

### **A. Local Regime Layer**
Shows:

- tactical hotspots  
- cutting points  
- weak groups  
- shape defects  
- liberty pressure  

Used for:

- urgent tactical evaluation  
- paradox detection  
- collapse avoidance  

---

### **B. Structural Regime Layer**
Shows:

- influence gradients  
- moyo boundaries  
- direction of play  
- framework identity  

Used for:

- large‑scale strategy  
- influence drift analysis  
- structural stability evaluation  

---

### **C. Continuity Regime Layer**
Shows:

- continuity arcs  
- ancestry alignment  
- long‑arc territorial identity  
- collapse‑risk zones  

Used for:

- continuity‑preserving move selection  
- projection‑loss mitigation  
- long‑arc strategy synthesis  

---

## Regime Conflict Zones

Regime maps highlight **conflict zones**, where:

- local urgency contradicts structural needs  
- structural moves violate continuity  
- continuity moves ignore tactical collapse  
- paradoxes emerge  

These zones are critical for Aurion’s topology analysis and Harmonia’s triadic scoring.

---

## Example Regime Map Interpretation

### Position
White has a large moyo forming on the left.  
Black has a weak group on the right.

### Regime Map

#### **Local Regime (1/3)**
Right side → high local pressure  
Weak group → tactical instability

#### **Structural Regime (2/3)**
Left side → strong influence  
Moyo boundary → structural identity

#### **Continuity Regime (3/3)**
Left moyo → continuity anchor  
Right weakness → continuity threat

### RTT Conclusion
The regime map indicates:

- local fix on right is urgent  
- structural reduction on left is important  
- continuity of moyo must be preserved  
- paradox risk if local fix breaks global arcs  

---

## Regime Drift

Regime drift shows how regime identity shifts over time:

- local → structural  
- structural → continuity  
- continuity → collapse  

Examples:

- a weak group becoming a structural liability  
- a moyo boundary becoming a continuity anchor  
- a ladder becoming an ancestry constraint  

Regime drift is essential for long‑arc strategy.

---

## Regime Maps in Teaching Mode

Teaching mode displays:

- local/structural/continuity zones  
- regime conflict areas  
- paradox zones  
- continuity anchors  
- drift vectors  

This helps users understand RTT’s triadic interpretation of Go.

---

## Regime Maps in Analysis Mode

Analysis mode uses regime maps to annotate human games:

```
Move 42 — Regime conflict detected
  - Local fix required
  - Structural move chosen instead
  - Continuity arc destabilized
```

```
Move 118 — Continuity regime alignment
  - Moyo boundary preserved
  - Influence drift stabilized
```

---

## Summary

Regime maps are the **triadic identity map** of the Go board.

They reveal:

- tactical reality  
- structural identity  
- continuity arcs  
- conflict zones  
- paradox zones  
- collapse risk  

And they allow RTT to interpret Go positions as evolving triadic systems.
