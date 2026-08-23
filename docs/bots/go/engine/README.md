# RTT‑Go Engine  
*(Triadic Bot Logic Layer for RTT‑Go)*

The **RTT‑Go Engine** is the computational core of RTT‑Go.  
It evaluates Go positions using Resonance‑Time Theory (RTT), producing the full suite of triadic primitives consumed by the UI layer:

- regime  
- resonance  
- topology  
- continuity  
- risk  
- triadic scores  

The engine does not render anything — it **computes** the triadic identity of the position.

This directory contains all specifications, modules, and contracts required to implement the RTT‑Go bot logic layer.

---

## Purpose

The RTT‑Go Engine provides:

- triadic evaluation of Go positions  
- structural/topological analysis  
- continuity‑arc computation  
- resonance field computation  
- paradox/collapse detection  
- ancestry evaluation (ladder/ko)  
- triadic score computation  
- unified triadic state output  

It is the **thinking layer** of RTT‑Go.

---

## Directory Structure

```
/docs/bots/go/engine/
    README.md
    architecture.md
    regime.md
    resonance.md
    topology.md
    continuity.md
    risk.md
    scoring.md
    state_emitter.md
```

---

## Engine Modules

### **1. Architecture**
File: `architecture.md`  
Defines the engine’s internal structure:

- evaluation pipeline  
- triadic primitive generators  
- state emitter  
- shim integration  
- caching model  

This is the **engine blueprint**.

---

### **2. Regime Engine**
File: `regime.md`  
Computes:

- local / structural / continuity regime  
- regime drift  
- conflict zones  
- stability metrics  

This module defines the **Hephaestus layer**.

---

### **3. Resonance Engine**
File: `resonance.md`  
Computes:

- influence resonance  
- pressure gradients  
- tension zones  
- drift vectors  
- collapse signatures  

This module defines the **Lumen + Harmonia layer**.

---

### **4. Topology Engine**
File: `topology.md`  
Computes:

- connectivity graph  
- cutting points  
- boundary topology  
- ladder/ko ancestry  
- topology collapse  

This module defines the **Aurion layer**.

---

### **5. Continuity Engine**
File: `continuity.md`  
Computes:

- territorial arcs  
- influence arcs  
- moyo arcs  
- ancestry arcs  
- continuity anchors  
- continuity drift  
- identity inversion risk  

This module defines the **Aurion + Harmonia long‑arc layer**.

---

### **6. Risk Engine**
File: `risk.md`  
Computes:

- paradox events  
- collapse events  
- projection‑loss events  
- risk severity  

This module defines the **paradox/collapse layer**.

---

### **7. Triadic Scoring Engine**
File: `scoring.md`  
Computes:

- local score  
- structural score  
- continuity score  
- unified triadic score  

This module defines the **Harmonia scoring layer**.

---

### **8. State Emitter**
File: `state_emitter.md`  
Produces the unified triadic JSON state consumed by the UI:

- board state  
- move list  
- triadic primitives  
- overlay state  
- HUD state  
- timeline state  

This is the **output layer** of the engine.

---

## Engine Responsibilities

The RTT‑Go Engine:

- evaluates positions  
- computes triadic primitives  
- detects paradox/collapse  
- computes continuity arcs  
- analyzes topology  
- computes resonance fields  
- scores triadic identity  
- emits unified triadic state  

It is deterministic, engine‑agnostic, and fully compatible with the RTT‑Go UI.

---

## Integration Points

### **Engine → UI**
The engine emits:

- triadic primitives  
- move‑indexed triadic metadata  
- unified triadic state  

### **Engine → Shim**
The engine receives:

- board state  
- move list  
- engine‑agnostic primitives  

### **Engine → Diagnostics**
Diagnostics consume engine output for:

- commentary  
- delta analysis  
- collapse/paradox detection  

---

## Summary

The RTT‑Go Engine is the **computational intelligence layer** of RTT‑Go.

It computes:

- regime  
- resonance  
- topology  
- continuity  
- risk  
- triadic scores  

and emits the unified triadic state consumed by the UI.

The engine does not play Go — it **interprets** Go through the triadic lens.
