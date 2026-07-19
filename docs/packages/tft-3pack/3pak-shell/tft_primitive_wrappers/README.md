# 📦 **tft_primitive_wrappers**  
###### By Nawder Loswin 1/4/2026 © www.TriadicFrameworks.org

### TriadicFrameworks — 3PAK Shell Primitive Wrappers

The **tft_primitive_wrappers** directory contains the executable shell wrappers for the three TFT Primitives that form the core of the **tft‑3pack** cycle.  
These wrappers provide a clean, resonance‑aligned command‑line interface for invoking the primitives inside the 3PAK Shell environment.

Each wrapper is intentionally lightweight, safe, and predictable — mirroring the triadic rhythm of **begin → transform → close**.

---

## 🔧 Purpose of This Directory

This folder exists to:

- expose the three TFT primitives as shell‑level commands  
- integrate them with the 3PAK environment (`threepak_note`, logs, state)  
- provide a consistent interface for triadic workflows  
- support scripting, automation, and developer experimentation  

The wrappers do not contain business logic — they simply trigger the conceptual primitives and record state markers.

---

## 📂 Included Wrappers

### **1. `primitive1.sh` — Initialization**
Represents the *beginning* of the triadic cycle.

- records an initialization marker  
- updates 3PAK state  
- logs the action  
- prints a friendly confirmation  

Used when starting a new cycle or resetting context.

---

### **2. `primitive2.sh` — Transformation**
Represents the *middle movement* of the cycle.

- records a transformation marker  
- updates state  
- logs the action  

Used when shifting context, reframing, or applying a mid‑cycle adjustment.

---

### **3. `primitive3.sh` — Closure**
Represents the *completion* of the cycle.

- records a closure marker  
- seals the lineage step  
- logs the action  

Used when finalizing a workflow or ending a triadic arc.

---

## 🚀 How to Use These Wrappers

Once the 3PAK Shell is initialized:

```bash
primitive1.sh     # Begin
primitive2.sh     # Transform
primitive3.sh     # Close
```

Each command writes to:

- `$THREEPAK_STATE`  
- `$THREEPAK_LOG`  

This makes the 3‑Pack cycle observable, scriptable, and reproducible.

---

## 🧭 Role in the 3‑Pack Ecosystem

These wrappers are the **operational surface** of the tft‑3pack system.  
They connect:

- the conceptual primitives  
- the 3PAK environment  
- the WRSADC boundary  
- developer workflows  

They allow the triadic rhythm to be executed in real time.

---

## 🧙 Mythmatical Architect’s Note

A primitive is a gesture.  
A wrapper is the hand that performs it.  
Together, they let the 3‑Pack breathe inside the shell —  
a simple, elegant cycle of beginning, turning, and completing.

## Quicklinks
- [3pak-shell profile.d README](https://www.triadicframeworks.org/packages/tft-3pack/3pak-shell/profile.d/README.html)
- [3pak-shell README](https://www.triadicframeworks.org/packages/tft-3pack/3pak-shell/README.html)
