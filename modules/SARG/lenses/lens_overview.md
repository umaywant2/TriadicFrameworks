# **Lens Overview**  
*A SARG reference document*

A **lens** is the operator used to read, interpret, or transform a substrate.  
Where the substrate provides *structure*, the lens provides *perspective* — it determines **what becomes visible**, **what becomes invariant**, and **how resonance is revealed**.

Lenses are substrate‑agnostic: the same lens can be applied to linguistic, acoustic, geometric, symbolic, biological, cosmological, or lostational substrates.

---

## **1. What a Lens Does**

A lens performs three core functions:

### **1. Reveals Structure**  
It highlights specific features of the substrate — strokes, harmonics, axes, cycles, intersections, attractors, etc.

### **2. Produces Invariants**  
Each lens stabilizes certain features across transformations.  
These become the **vertical**, **horizontal**, and **dual** invariants in SARG.

### **3. Aligns with Resonance**  
A lens determines how the substrate maps to the universal anchors:

- **●** point  
- **○** loop  
- **×** intersection  
- **|** axis  

Different lenses reveal different resonance families.

---

## **2. Lens Types in SARG**

SARG currently recognizes two primary lens families, with room for expansion:

### **VREL — Vertical Resonance Extraction Lens**  
Focuses on:

- vertical invariants  
- structural axes  
- stroke families  
- directional coherence  

Common in linguistic, geometric, and symbolic substrates.

---

### **VREL‑A — Acoustic Variant**  
Focuses on:

- harmonic families  
- overtone structure  
- rhythmic invariants  
- phase coherence  

Common in acoustic, biological, and cosmological substrates.

---

## **3. Lens Behavior Across Substrates**

A lens is not tied to a domain.  
Instead, it adapts to the substrate:

- On **linguistic** substrates, VREL extracts stroke families.  
- On **acoustic** substrates, VREL‑A extracts harmonic invariants.  
- On **geometric** substrates, VREL extracts axes and symmetries.  
- On **symbolic** substrates, VREL reveals relational structure.  
- On **biological** substrates, VREL‑A reveals oscillatory coherence.  
- On **lostational** substrates, both lenses reveal dimensional drift and resonance shells.

The lens determines *what counts* as structure.

---

## **4. Lens Block in SARG**

Every SARG object includes a lens block:

```
"lens": {
  "type": "VREL",
  "variant": "standard",
  "notes": "extracts vertical and dual invariants"
}
```

- **type** — the lens family (e.g., VREL, VREL‑A)  
- **variant** — optional subtype  
- **notes** — any special considerations  

---

## **5. Relationship to Other Files**

- `VREL.md` — details of the vertical resonance lens  
- `VREL-A.md` — acoustic variant  
- `invariant_types.md` — invariants produced by lenses  
- `resonance_mapping.md` — how lenses reveal anchors  
- `examples/` — SARG objects using different lenses  
