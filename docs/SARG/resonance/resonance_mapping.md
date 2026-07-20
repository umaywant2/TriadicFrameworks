# **Resonance Mapping**  
*A SARG resonance reference document*

Resonance mapping describes **how a substrate aligns with the four universal anchors**:

- **●** point  
- **○** loop  
- **×** intersection  
- **|** axis  

These anchors act as the minimal resonance primitives that appear across all domains.  
Resonance mapping is the process of identifying which anchors dominate, how they combine, and what structural behavior they imply.

---

## **1. What Resonance Mapping Does**

Resonance mapping answers three questions:

### **1. Which anchors appear in the structure?**  
Does the substrate express point‑like, loop‑like, intersecting, or axial behavior?

### **2. How do these anchors combine?**  
Do they form a family (e.g., circle‑dominant, cross‑axis, point‑axis hybrid)?

### **3. What does this imply about the system’s behavior?**  
Resonance families often correlate with:

- stability  
- drift  
- tension  
- periodicity  
- coherence  
- dimensional behavior  

This is why resonance mapping is central to SARG.

---

## **2. Mapping Anchors to Invariants**

Each anchor corresponds to a class of invariants:

| Anchor | Invariant Type | Meaning |
|--------|----------------|---------|
| **●** | point invariants | singularity, atomic center, minimal unit |
| **○** | loop invariants | cycles, enclosures, periodicity |
| **×** | intersection invariants | crossings, tension, dual‑axis alignment |
| **|** | axis invariants | direction, extension, structural spine |

A SARG object may express one or more of these simultaneously.

---

## **3. Mapping Anchors to Substrate Behavior**

### **● Point‑Dominant**  
- atomic  
- discrete  
- node‑based  
- minimal coherence units  

### **○ Loop‑Dominant**  
- periodic  
- cyclic  
- self‑enclosing  
- stable under rotation  

### **× Cross‑Dominant**  
- tension  
- interference  
- branching  
- synthesis or conflict  

### **| Axis‑Dominant**  
- directional  
- vector‑driven  
- structural alignment  
- growth or extension  

---

## **4. Resonance Families**

A resonance family is a **pattern of anchor dominance**.

Examples:

- **circle‑dominant** → ○ ○ ●  
- **cross‑axis** → × |  
- **point‑axis hybrid** → ● |  
- **loop‑intersection** → ○ ×  

Families help compare substrates across domains.

---

## **5. Resonance Block in SARG**

Every SARG object includes a resonance block:

```
"resonance": {
  "anchors": ["○", "×"],
  "family": "loop-intersection",
  "notes": "cyclic structure with crossing tension"
}
```

- **anchors** — the universal anchors present  
- **family** — the dominant pattern  
- **notes** — optional contextual details  

---

## **6. Relationship to Other Files**

- `universal_anchors.md` — defines the four anchors  
- `resonance_families.md` — describes families built from anchor combinations  
- `invariant_types.md` — shows how invariants relate to anchors  
- `examples/` — real SARG objects using resonance mapping  
- `sarg.schema.json` — formal structure for the resonance block  
