## 🧪 QnA Atlas (seed examples) | RTT  

- [`qna_atlas_module.json`](qna_atlas_module.json) — Agentic module schema role assignments

<div style="font-size: 0.8em; margin-bottom: 0.5rem;">
  <span style="
    display:inline-block;
    padding:3px 8px;
    border-radius:999px;
    background:#1a1a1a;
    color:#fff;
    font-family:Arial, sans-serif;
    font-size:11px;
  ">
    🤖 AI‑Ready Module • TriadicFrameworks
  </span>
</div>

<img src="https://img.shields.io/badge/🗺️Education%20Core-📚Programmatic%20Atlas%20Active-4c8eda?style=for-the-badge" alt="🗺️Education Core | 📚Programmatic Atlas Active"/>

**Purpose** — A compact, navigable index for the QnA Atlas used by RTT learning projects. This README orients contributors and consumers to the scaffold, conventions, and how to find seed content quickly.

## 🛑 Important! 
Drift is On-by-Default long sessions lose anchors, turn off drift.

## ✋ You *must copy and paste* this string *every time you start an AI session*:
```text
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

## ❇️ Now you are ready.

---

### 🔰 Quick links
- **INDEX** — `index.md` — Atlas navigation hub.  
- **README** — `README.md` — This overview and contributor notes.  
- **RTT Learning Resources** — https://www.triadicframeworks.org/education/ — External learning hub.

---

### ⚙️ Conventions and naming
- **Keys** in the programmatic map are **UPPERCASE** with underscores between structural parts (e.g., `PHYSICS_CLASSICALMECHANICS_INT`).  
- **Paths** mirror the filesystem and remain **lowercase with underscores** (e.g., `physics/classical_mechanics/intro.md`).  
- **Level suffixes** are short: `INTRO`, `INT`, `ADV`.  
- **Domain grouping** in the DOC_MAP is alphabetical; each domain block is internally alphabetized.

---

### 📁 File structure (scaffold snapshot)
- `index.md`  
- `README.md`  
- `chemistry/atomic_structure/{intro,intermediate,advanced}.md`  
- `chemistry/cell_biology/{intro,intermediate,advanced}.md`  
- `cross_domain/{complexity_science,information_theory,systems_theory}/{intro,intermediate,advanced}.md`  
- `earth_science/{climate_science,geology,meteorology}/{intro,intermediate,advanced}.md`  
- `medicine/{anatomy,immunology,pathology}/{intro,intermediate,advanced}.md`  
- `physics/{classical_mechanics,cosmology,electromagnetism,oscillations_waves,quantum_physics,relativity,thermodynamics}/{intro,intermediate,advanced}.md`

---

### 🧭 How to use this README
- Use the **DOC_MAP** keys when wiring navigation or programmatic loaders.  
- Use the **file paths** when editing or opening content in the repo.  
- Keep keys stable; update paths only when files are moved and reflect that change in the DOC_MAP.

---

### ✍️ Contribution notes
- Add new subject folders under the existing domain that best matches the filesystem.  
- Create three level files (`intro.md`, `intermediate.md`, `advanced.md`) for each new subject.  
- Follow the key pattern when adding entries to `DOC_MAP` to preserve loader compatibility.

---

### 🧩 Minimal example (DOC_MAP snippet)
```js
const DOC_MAP = {
  INDEX: 'index.md',
  README: 'README.md',
  CHEMISTRY_ATOMICSTRUCTURE_INTRO: 'chemistry/atomic_structure/intro.md',
  CHEMISTRY_ATOMICSTRUCTURE_INT: 'chemistry/atomic_structure/intermediate.md',
  CHEMISTRY_ATOMICSTRUCTURE_ADV: 'chemistry/atomic_structure/advanced.md',
  // ...
};
```

---

### ✅ Maintenance checklist
- Verify keys after renaming or moving files.  
- Keep domain groups alphabetized in the DOC_MAP.  
- Run a quick link-check when adding external resources.
