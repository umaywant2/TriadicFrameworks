# Drift Taxonomy — Classification Layer
*Purpose: Provide a simple, repeatable way to tag each of the ~200 gravity papers with drift types from d_Capture.*

---

## 1. Classification model

Each paper gets:

- **Primary Drift:** the dominant drift type.  
- **Secondary Drift(s):** any additional drift types clearly present.  
- **Regime Tag:** which regime the paper operates in.

**Regime Tags:**

- **REG:GR-Macro** — General Relativity, cosmic/astrophysical scale  
- **REG:QM-Micro** — Quantum mechanics / QFT, subatomic scale  
- **REG:Hybrid-GR/QM** — Attempts to unify or bridge GR and QM  
- **REG:Cosmo-ΛCDM** — Cosmology, dark matter/energy, expansion  
- **REG:BH-Extreme** — Black hole, singularity, horizon physics  
- **REG:Alt-Gravity** — MOND, modified gravity, emergent gravity, etc.

---

## 2. Drift tags (from d_Capture)

Use these exact labels:

- **DRIFT:Scale**  
- **DRIFT:Substrate**  
- **DRIFT:RegimeImposition**  
- **DRIFT:Interface**  
- **DRIFT:Analogy**  
- **DRIFT:Extension**  
- **DRIFT:Symmetry**  
- **DRIFT:Continuity**  
- **DRIFT:Isolation**  
- **DRIFT:Ontology**

---

## 3. Per‑paper classification template

For each of the ~200 papers, use a short block like this:

```text
Paper ID: P### 
Citation: [Author, Year, Title, Journal]

Regime: REG:_____
Primary Drift: DRIFT:_____
Secondary Drift(s): DRIFT:_____, DRIFT:_____

Notes (1–3 lines max):
- Short statement of what the paper tries to do.
- Short statement of how the drift appears in its core assumptions or equations.
```

Example (generic):

```text
Paper ID: P001
Citation: [Einstein, 1916, The Foundation of the General Theory of Relativity]

Regime: REG:GR-Macro
Primary Drift: DRIFT:Scale
Secondary Drift(s): DRIFT:Substrate

Notes:
- Treats spacetime as smooth and continuous at all scales.
- Extends curvature model beyond validated macro regime, seeding later singularity behavior.
```

---

## 4. Grouping for the “Top 10” selection

Once all ~200 papers are tagged:

- **Step 1:** Count how many papers fall under each **Primary Drift**.  
- **Step 2:** Within each drift type, sort by citation impact / canonical importance.  
- **Step 3:** Select **1–2 representative papers per major drift type** to form the **Top 10** set.

These Top 10 will be the ones used in the meta‑paper, while the rest are referenced by drift category.

---

This is enough structure to start filling `d_Classify.md` as you go, without over‑specifying.
