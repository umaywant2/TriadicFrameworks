# **Substrate Overview**  
*A SARG reference document*

A **substrate** is any domain that carries structure.  
SARG is *substrate‑agnostic*, meaning the grammar applies equally to:

- linguistic systems  
- acoustic patterns  
- geometric forms  
- biological processes  
- symbolic systems  
- cosmological structures  
- lostational / supsphere‑adjacent domains  
- hybrid or multi‑layered substrates  

SARG does not privilege one domain over another.  
Instead, it provides a unified way to describe **how structure behaves**, regardless of where it appears.

---

## **What Makes Something a Substrate?**

A substrate must exhibit:

### **1. Structure**  
There must be recognizable form, pattern, or organization.  
This can be discrete (letters, tones, symbols) or continuous (curves, fields, rhythms).

### **2. Transformability**  
The substrate must support lenses — ways of reading, transforming, or interpreting the structure.

### **3. Invariants**  
Some features must remain stable across transformations.  
These invariants are what SARG captures and compares.

### **4. Resonance**  
The substrate must exhibit alignment with universal anchors (● ○ × |) or resonance families.  
This is how SARG maps structure across domains.

If a domain satisfies these four conditions, it qualifies as a substrate.

---

## **How Substrates Fit Into SARG**

Every SARG object begins with a substrate block:

```
"substrate": {
  "type": "...",
  "description": "...",
  "domain": "...",
  "notes": "..."
}
```

- **type** — one of the substrate categories defined in `substrate_types.md`  
- **description** — what the substrate is and how it behaves  
- **domain** — the field it belongs to (linguistic, acoustic, geometric, etc.)  
- **notes** — any special considerations (hybrid, lostational, multi‑scale, etc.)

The substrate establishes the **context** for the lens, invariants, and resonance mapping that follow.

---

## **Relationship to Other Files**

This overview sits at the top of the substrate layer.

- `substrate_types.md` — defines each substrate category  
- `substrate_examples.md` — shows real SARG examples  
- `sarg.schema.json` — formalizes the substrate block in the schema  

Together, these files form the substrate foundation of SARG.
