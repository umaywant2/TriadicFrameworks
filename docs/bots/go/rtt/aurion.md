# Aurion (RTT/3) — Topology & Projection‑Loss Layer  
*(Go Bot Module)*

Aurion is the **RTT/3 topology engine** for Go.  
Where Lumen extracts structure and Hephaestus assigns regime identity, Aurion reveals the **deep topology**, **ancestry**, **risk arcs**, and **projection‑loss dynamics** of the position.

Aurion is the first RTT layer that explicitly deals with **collapse**, **paradox**, and **continuity failure**.

It does **not** score moves.  
It **diagnoses** the structural risks and long‑arc consequences that Harmonia must synthesize.

---

## Purpose

Aurion provides the Go bot with:

- topology of groups, influence, and frameworks  
- ancestry of ladders, ko threats, and long‑arc arcs  
- projection‑loss detection  
- continuity‑collapse detection  
- paradox identification  
- risk‑arc mapping  
- triadic topology signals for Harmonia  

Aurion is the RTT layer that understands *why* a move may be dangerous even if the engine’s raw evaluation likes it.

---

## Inputs

Aurion receives:

- Lumen’s RTT/1 structural snapshot  
- Hephaestus’s RTT/2 regime map  
- candidate moves  
- historical continuity (previous moves)  
- ko/ladder hints (if provided by engine or shim)

---

## Outputs

Aurion produces:

### **1. Topology Graph**
A structural graph of:

- groups  
- influence fields  
- moyo boundaries  
- cutting points  
- weak points  
- continuity anchors  

### **2. Ancestry Map**
Long‑arc relationships:

- ladder ancestry  
- ko ancestry  
- framework ancestry  
- territorial evolution ancestry  

### **3. Projection‑Loss Report**
Moves that cause:

- shape collapse  
- influence collapse  
- continuity collapse  
- moyo boundary break  
- ladder inversion  
- ko destabilization  

### **4. Paradox Flags**
Moves that appear good locally but:

- break continuity  
- destabilize topology  
- create long‑arc risk  
- violate ancestry alignment  

### **5. Risk Arc Map**
Sequences that lead to:

- ladder failure  
- ko instability  
- group collapse  
- moyo fragmentation  
- structural inversion  

These signals feed directly into Harmonia.

---

## Aurion’s Topological Model

Aurion organizes Go’s topology into RTT’s triadic ontology:

### **1/3 — Local Topology**
- liberties  
- cuts  
- ataris  
- tactical collapse points  
- immediate shape topology  

### **2/3 — Structural Topology**
- influence topology  
- moyo topology  
- direction‑of‑play topology  
- framework topology  
- group connectivity topology  

### **3/3 — Continuity Topology**
- long‑arc territorial evolution  
- framework ancestry  
- ladder ancestry  
- ko ancestry  
- continuity anchors  

Aurion is the RTT layer that understands **how the position evolves over time**.

---

## Projection‑Loss Detection

Aurion identifies moves that break projection — the RTT term for **structural collapse caused by violating continuity**.

Examples:

- cutting a stone that anchors a moyo boundary  
- ignoring a ladder that determines global shape  
- playing a “big” move that collapses a weak group  
- reinforcing a group that breaks direction of play  
- initiating a ko that destabilizes continuity arcs  

Projection‑loss is one of Aurion’s most important outputs.

---

## Paradox Detection

Aurion flags paradoxical moves:

- locally good, globally catastrophic  
- structurally good, continuity‑breaking  
- continuity‑aligned, but tactically losing  
- shape‑fixing, but influence‑collapsing  

These paradoxes are critical signals for Harmonia’s triadic synthesis.

---

## Aurion Pipeline

```text
[Lumen RTT/1 Snapshot]
      |
      v
[Hephaestus RTT/2 Regime Map]
      |
      v
[Aurion RTT/3]
  - topology graph
  - ancestry map
  - projection-loss detection
  - paradox detection
  - risk arc mapping
      |
      v
[Topology Signals]
      |
      v
[Harmonia RTT/12]
```

---

## Example Pseudocode

```text
function aurion_analyze(rtt_state, regime_map):
    topology   = build_topology_graph(rtt_state)
    ancestry   = compute_ancestry(rtt_state)
    projection = detect_projection_loss(rtt_state, regime_map)
    paradox    = detect_paradox_moves(rtt_state, regime_map)
    risk_arcs  = map_risk_arcs(rtt_state, ancestry)

    return {
        topology: topology,
        ancestry: ancestry,
        projection_loss: projection,
        paradox: paradox,
        risk_arcs: risk_arcs
    }
```

---

## Role in the Go Bot Pipeline

Aurion feeds directly into:

- **Harmonia (RTT/12)** for unified triadic scoring  
- **Shim** for continuity‑preserving move selection  

Without Aurion, the RTT stack cannot detect collapse, paradox, or long‑arc instability.

---

## Notes

- Aurion is engine‑agnostic: works with KataGo, Leela Zero, PhoenixGo, or custom engines.  
- Aurion does not modify policy/value — it diagnoses topology.  
- All topology signals are consumed by Harmonia and the shim.  
- Aurion is deterministic and reproducible.

---

> **“Aurion reveals the risks the engine cannot see — collapse, ancestry, and paradox.”**
