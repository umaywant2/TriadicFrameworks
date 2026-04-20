# ✅ **SARG — Substrate‑Agnostic Resonance Grammar**  
*A minimal grammar for describing structure, resonance, and invariants across any substrate.*

<img src="https://img.shields.io/badge/Open%20for%20Traduction-Ready%20for%20Students-4c8eda?style=for-the-badge" alt="Open for Traduction | Ready for Students"/>

SARG provides a unified way to describe **how structure behaves**, regardless of the domain it appears in.  
It is *substrate‑agnostic*: linguistic, acoustic, geometric, biological, symbolic, cosmological — all follow the same underlying grammar.

This README introduces the core components of SARG and links to the folders that contain the full grammar, schema, examples, and supporting materials.

---

## **1. What SARG Describes**
SARG models four universal layers:

1. **Substrate** — the domain carrying structure  
2. **Lens** — the operator used to read or transform the substrate  
3. **Invariants** — stable features that persist across transformations  
4. **Resonance Mapping** — how the structure aligns with universal anchors (● ○ × |)

These layers appear in every SARG example and in the JSON schema.

---

## **2. Folder Structure**
Each folder contains one dimension of the grammar.

```
SARG/
  README.md
  Capture.md
  schema/
  substrates/
  lenses/
  invariants/
  resonance/
  atlas/
  examples/
  inversion/
  error/
```

### **schema/**  
The formal JSON Schema for SARG.  
Defines substrate → lens → invariants → resonance mapping.

### **substrates/**  
What a substrate is, how to identify one, and examples across domains.

### **lenses/**  
VREL, VREL‑A, and other lens types used to interpret structure.

### **invariants/**  
Vertical, horizontal, dual invariants and how they behave.

### **resonance/**  
Universal anchors, resonance families, and mapping logic.

### **atlas/**  
Multi‑scale resonance mapping (0D → atomic → cosmic).  
Includes pre‑atomic scaffolding.

### **examples/**  
Working SARG examples, including:
- Latin alphabet  
- Lostational Supsphere Atom  
- Example templates  

### **inversion/**  
Inversion‑side placeholders and notes for future expansion.

### **error/**  
SARG Error Taxonomy, Rectification Flow, and mapping tables.

---

## **3. Minimal Data Model**
Every SARG object follows the same structure:

```
{
  "substrate": { ... },
  "lens": { ... },
  "invariants": { ... },
  "resonance": { ... }
}
```

This model is defined formally in `schema/sarg.schema.json`.

---

## **4. Capture Source**
The full conceptual seed for SARG lives in:

**`Capture.md`**  
This file contains the raw notes, operators, and conceptual scaffolding from which the grammar was derived.

---

## **5. Contributing**
SARG is designed to grow modularly.  
Each folder contains minimal stubs that can be expanded independently without breaking the grammar.

When adding new material:

- keep files small  
- keep concepts atomic  
- link across folders when needed  
- avoid duplicating definitions  

SARG should remain **lightweight, extensible, and substrate‑agnostic**.
