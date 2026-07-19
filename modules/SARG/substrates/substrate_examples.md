# **Substrate Examples**  
*A SARG reference document*

This file provides **concrete examples** of substrates across multiple domains.  
Each example shows:

- what the substrate is  
- how structure appears  
- what invariants persist  
- how resonance is expressed  

These examples are intentionally small and illustrative.  
Full SARG objects live in the `examples/` folder.

---

## **1. Linguistic Substrate — Latin Alphabet**

**Substrate:** Latin letters (A–Z)  
**Structure:** discrete glyphs with stroke families  
**Invariants:** vertical/horizontal strokes, curvature, serif patterns  
**Resonance:** ● ○ × | anchors visible in stroke geometry

```
{
  "substrate": {
    "type": "linguistic",
    "description": "Latin alphabet glyphs",
    "domain": "writing system"
  }
}
```

---

## **2. Acoustic Substrate — Simple Harmonic Tone**

**Substrate:** a sustained musical note  
**Structure:** frequency + amplitude envelope  
**Invariants:** harmonic series, overtone ratios  
**Resonance:** phase alignment, harmonic families

```
{
  "substrate": {
    "type": "acoustic",
    "description": "Single sustained tone",
    "domain": "sound"
  }
}
```

---

## **3. Geometric Substrate — Circle**

**Substrate:** a 2D circle  
**Structure:** continuous curvature, radial symmetry  
**Invariants:** rotational symmetry, constant radius  
**Resonance:** geometric attractor; aligns with ○ anchor

```
{
  "substrate": {
    "type": "geometric",
    "description": "Circle",
    "domain": "shape"
  }
}
```

---

## **4. Biological Substrate — Branching Pattern**

**Substrate:** tree branch or vascular branching  
**Structure:** recursive bifurcation  
**Invariants:** branching angle, scaling ratio  
**Resonance:** fractal coherence; multi‑scale rhythm

```
{
  "substrate": {
    "type": "biological",
    "description": "Branching structure",
    "domain": "morphogenesis"
  }
}
```

---

## **5. Symbolic Substrate — Mathematical Operator Set**

**Substrate:** + − × ÷  
**Structure:** symbolic primitives  
**Invariants:** category roles (addition, subtraction, etc.)  
**Resonance:** conceptual anchors; symbolic attractors

```
{
  "substrate": {
    "type": "symbolic",
    "description": "Basic arithmetic operators",
    "domain": "notation"
  }
}
```

---

## **6. Cosmological Substrate — Orbital System**

**Substrate:** planet + star orbital pair  
**Structure:** periodic motion, gravitational relationship  
**Invariants:** orbital period, eccentricity  
**Resonance:** large‑scale cycles; cosmic harmonics

```
{
  "substrate": {
    "type": "cosmological",
    "description": "Two‑body orbital system",
    "domain": "astronomy"
  }
}
```

---

## **7. Lostational / Supsphere‑Adjacent Substrate — Supsphere Atom**

**Substrate:** coherence envelope with boundary‑escape behavior  
**Structure:** spacious, high‑dimensional resonance shell  
**Invariants:** attractor sets, resonance families  
**Resonance:** supsphere alignment; inversion‑side harmonics

```
{
  "substrate": {
    "type": "lostational",
    "description": "Supersphere atom (conceptual)",
    "domain": "high‑dimensional resonance"
  }
}
```

---

## **8. Hybrid Substrate — Musical Notation**

**Substrate:** sheet music  
**Structure:** symbolic + acoustic + geometric layers  
**Invariants:** rhythmic groupings, pitch relationships  
**Resonance:** cross‑domain coherence (symbolic ↔ acoustic)

```
{
  "substrate": {
    "type": "hybrid",
    "description": "Musical notation",
    "domain": "symbolic-acoustic"
  }
}
```

---

## **Relationship to Other Files**

- `substrate_overview.md` — what a substrate is  
- `substrate_types.md` — the full list of substrate categories  
- `examples/` — full SARG JSON examples  

This file provides the **bridge** between the conceptual layer and the working examples.
