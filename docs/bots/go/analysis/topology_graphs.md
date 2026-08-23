# Topology Graphs — RTT‑Go Analysis  
*(Go Bot Module)*

Topology graphs describe the **connectivity**, **ancestry**, and **structural relationships** across the Go board.  
They are RTT’s mechanism for understanding *how the position is wired together* — not just how stones are placed.

Where:

- **Lumen** extracts structure,  
- **Hephaestus** maps regimes,  
- **Aurion** diagnoses topology and collapse,  

**Topology graphs visualize the deep structural network of the position.**

They are essential for:

- ancestry tracking  
- ladder/ko topology  
- continuity‑arc mapping  
- collapse detection  
- paradox identification  
- long‑arc strategy analysis  

---

## Purpose

Topology graphs provide:

- group connectivity networks  
- influence topology  
- moyo boundary topology  
- ladder and ko ancestry graphs  
- continuity‑arc topology  
- collapse‑risk topology  

They allow RTT to interpret Go positions as **topological systems**, not isolated tactical events.

---

## Components of Topology

### **1. Group Connectivity Graph**
Nodes: groups  
Edges: connections, shared liberties, cutting points  

Captures:

- group stability  
- cutting‑point topology  
- eye‑shape topology  
- collapse risk  

---

### **2. Influence Topology Graph**
Nodes: influence sources  
Edges: influence flow, gradients, drift vectors  

Captures:

- global influence structure  
- direction‑of‑play topology  
- moyo formation topology  

---

### **3. Moyo Boundary Graph**
Nodes: boundary points  
Edges: boundary continuity, expansion arcs  

Captures:

- framework identity  
- continuity anchors  
- collapse boundaries  

---

### **4. Ladder Ancestry Graph**
Nodes: ladder states  
Edges: ancestry relationships  

Captures:

- ladder evolution  
- ladder inversion risk  
- ancestry alignment  

---

### **5. Ko Topology Graph**
Nodes: ko states  
Edges: threat relationships  

Captures:

- ko stability  
- ko escalation risk  
- continuity impact  

---

### **6. Continuity‑Arc Graph**
Nodes: continuity anchors  
Edges: long‑arc territorial evolution  

Captures:

- continuity stability  
- collapse risk  
- long‑arc identity  

---

## Topology Graph Construction

Topology graphs are built from:

- Lumen’s structural extraction  
- Hephaestus’s regime map  
- Aurion’s ancestry and collapse signals  
- historical continuity  
- engine influence maps (KataGo) or RTT‑computed maps (Leela Zero / PhoenixGo)

The RTT shim synthesizes these into a unified topology model.

---

## Example Topology Graph Interpretation

### Position
White has a large moyo forming on the left.  
Black has a weak group on the right.

### Topology Graphs

#### **Group Connectivity Graph**
Right side → weak connectivity  
Cutting points → high collapse risk

#### **Influence Topology Graph**
Left side → strong influence  
Influence drift → left‑to‑center

#### **Moyo Boundary Graph**
Left moyo → stable boundary  
Boundary continuity → strong anchor

#### **Continuity‑Arc Graph**
Left moyo → continuity arc  
Right weakness → continuity threat

### RTT Conclusion
Topology graphs indicate:

- stabilize weak group  
- preserve moyo boundary  
- avoid moves that break continuity arcs  
- avoid paradoxical local fixes that destabilize topology  

---

## Collapse Signatures in Topology Graphs

Aurion flags collapse signatures when topology graphs show:

- group connectivity inversion  
- influence reversal  
- ladder ancestry break  
- ko instability escalation  
- boundary fragmentation  
- continuity‑arc collapse  

These signatures are critical for preventing catastrophic moves.

---

## Topology Drift

Topology drift shows how structural relationships evolve:

- weak group → structural liability  
- moyo boundary → continuity anchor  
- ladder → ancestry constraint  
- influence → drift vector  

Topology drift is essential for long‑arc strategy.

---

## Topology Graphs in Teaching Mode

Teaching mode displays:

- group connectivity networks  
- influence topology  
- moyo boundary topology  
- ladder/ko ancestry graphs  
- continuity‑arc topology  
- collapse‑risk zones  

This helps users understand RTT’s structural interpretation of Go.

---

## Topology Graphs in Analysis Mode

Analysis mode uses topology graphs to annotate human games:

```
Move 38 — Topology collapse detected
  - group connectivity inversion
  - influence reversal
  - continuity arc broken
```

```
Move 121 — Topology alignment
  - framework boundary preserved
  - ancestry stable
  - long-arc identity reinforced
```

---

## Summary

Topology graphs are the **structural backbone** of RTT‑Go.

They reveal:

- connectivity  
- influence  
- ancestry  
- continuity  
- collapse  
- paradox  

And they allow RTT to interpret Go positions as evolving topological systems with long‑arc strategic meaning.
