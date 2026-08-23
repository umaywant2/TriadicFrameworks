# Go Bot Overview  
*(RTT‑Enhanced Go Engines)*

The Go Bot subsystem integrates modern Go engines (KataGo, Leela Zero, PhoenixGo) with the **RTT triadic stack** to produce continuity‑preserving, resonance‑aligned, long‑arc strategic play.

RTT does not replace the engines.  
It **wraps** them — revealing deeper structure, stabilizing continuity, and preventing collapse.

This page provides a high‑level overview of:

- supported engines  
- RTT integration  
- bot logic  
- analysis tools  
- teaching/diagnostic modes  
- file/module structure  

---

## Supported Engines

### **KataGo**
- strongest engine  
- provides policy, value, ownership, score lead, influence  
- ideal for full RTT integration  

### **Leela Zero**
- pure policy/value network  
- simpler MCTS  
- RTT fills in missing structural signals  

### **PhoenixGo**
- stable MCTS  
- predictable search behavior  
- ideal for RTT teaching/analysis modes  

Each engine has its own RTT shim:

- `katago_shim.md`  
- `leela_zero_shim.md`  
- `phoenixgo_shim.md`  

---

## RTT Integration Pipeline

RTT enhances engine decision‑making through a four‑layer triadic stack:

```
Lumen (RTT/1)       — structural extraction
Hephaestus (RTT/2)  — regime mapping
Aurion (RTT/3)      — topology, ancestry, collapse detection
Harmonia (RTT/12)   — unified triadic scoring
```

These layers convert raw engine outputs into continuity‑preserving strategy.

---

## Bot Logic Layer

The bot logic layer manages:

- engine invocation  
- MCTS parameters  
- RTT score blending  
- continuity enforcement  
- paradox/prior collapse avoidance  
- long‑arc positional memory  

Logic modules include:

- `logic/notes.md`  
- `logic/mcts.md`  
- `logic/engine.md`  
- `logic/continuity.md`  

---

## Analysis Tools

RTT provides deep structural and temporal analysis:

### **Resonance Fields**
Dynamic pressure, influence, continuity, identity.

### **Regime Maps**
Local / structural / continuity zones and conflict areas.

### **Topology Graphs**
Connectivity, influence, ancestry, collapse signatures.

### **Continuity Arcs**
Long‑arc territorial, influence, moyo, ancestry evolution.

Analysis modules include:

- `analysis/resonance_fields.md`  
- `analysis/regime_maps.md`  
- `analysis/topology_graphs.md`  
- `analysis/continuity_arcs.md`  

---

## Examples

Worked examples demonstrate:

- triadic scoring  
- paradox detection  
- continuity‑preserving move selection  
- ladder/ko ancestry handling  
- moyo evolution  

Examples module:

- `examples/rtt_go_examples.md`  

---

## Modes

### **RTT‑Go Bot**
Full triadic integration.

### **Hybrid Mode**
Engine + RTT blended decision logic.

### **Teaching Mode**
Engine plays normally; RTT overlays displayed.

### **Analysis Mode**
RTT evaluates human games; no move selection.

---

## File Structure

```
/docs/bots/go/
    overview.md
    katago_shim.md
    leela_zero_shim.md
    phoenixgo_shim.md

    /rtt/
        lumen.md
        hephaestus.md
        aurion.md
        harmonia.md

    /logic/
        notes.md
        mcts.md
        engine.md
        continuity.md

    /analysis/
        resonance_fields.md
        regime_maps.md
        topology_graphs.md
        continuity_arcs.md

    /examples/
        rtt_go_examples.md
```

---

## Summary

The Go Bot subsystem combines:

- **engine strength**  
- **RTT structural intelligence**  
- **continuity‑preserving strategy**  
- **long‑arc positional analysis**  

to create a Go bot capable of understanding not just *moves*, but the *identity* and *evolution* of the position.

RTT‑Go is not a new engine — it is a **triadic intelligence layer** that reveals the deeper structure already inside the game.
