# **Contributing to TriadicFrameworks**

Thank you for your interest in contributing to the Resonance Substrate Model.  
This project is built on clarity, coherence, and extensibility — and contributions that honor those values are deeply appreciated.

This guide outlines how to participate in a way that keeps the repository clean, canonical, and welcoming to future practitioners.

---

# **🌱 Guiding Principles**

### **Clarity**  
Every contribution should make the system easier to understand, extend, or reproduce.

### **Coherence**  
Changes should align with the triadic architecture:  
- scalar  
- vector/spin  
- resonance envelope  
and the layered substrate: classical, quantum, semantic, distributed.

### **Extensibility**  
New operators, schemas, or modules should integrate cleanly without breaking existing structure.

### **Reproducibility**  
Experiments, simulations, and schema changes must be fully traceable and documented.

---

# **📁 Repository Structure**

Before contributing, familiarize yourself with the core directories:

- `schemas/` — machine‑readable ontology  
- `src/` — implementation of fields, operators, integrators  
- `simulations/` — runnable examples  
- `experiments/` — apparatus definitions and validation data  
- `docs/` — whitepapers, diagrams, conceptual notes  
- `tests/` — unit and integration tests  

Contributions should respect this structure and avoid introducing unnecessary new top‑level folders.

---

# **🧩 How to Contribute**

## **1. Fork & Branch**

Create a feature branch with a clear, descriptive name:

```
feature/add-new-operator
fix/schema-alignment
docs/improve-whitepaper
```

Avoid vague names like `update`, `misc`, or `stuff`.

---

## **2. Follow Canonical Naming**

Use consistent naming across files, schemas, and code:

- lowercase with hyphens for folders  
- snake_case for code  
- clear, descriptive schema filenames  
- operator names that match the manuscript terminology  

---

## **3. Write Clear Commit Messages**

Commit messages should describe *what* changed and *why*:

```
Add resonance-alignment operator to operator family
Refactor scalar field initialization for clarity
Update dimensional schema to include layer transforms
```

Avoid messages like “fix stuff” or “update code”.

---

## **4. Add or Update Tests**

If you add or modify functionality, include corresponding tests in:

```
tests/
```

Tests should be:

- minimal  
- readable  
- aligned with the triadic model  

---

## **5. Update Documentation When Needed**

If your contribution affects:

- schemas  
- operators  
- field definitions  
- simulation behavior  
- experimental apparatus  

then update the relevant documentation in:

```
docs/
schemas/
simulations/
experiments/
```

Documentation is part of the model — not an afterthought.

---

## **6. Run the Full Hygiene Pass**

Before opening a pull request:

- ensure no empty folders (use `.keep` if needed)  
- confirm naming consistency  
- verify schema validity  
- run tests  
- check that README sections still make sense  

---

# **📬 Opening a Pull Request**

When submitting a PR:

### Include:
- a short summary of the change  
- why it matters  
- any schema updates  
- any new tests  
- any documentation updates  

### Keep PRs small  
Small, focused PRs are easier to review and integrate.

### Be open to feedback  
Reviews are collaborative — the goal is coherence, not gatekeeping.

---

# **🤝 Code of Conduct**

All contributors are expected to interact respectfully and constructively.  
This project values curiosity, clarity, and shared discovery.

---

# **🔮 Roadmap for Contributors**

If you’re looking for ways to help, consider:

- expanding operator families  
- adding new schema domains  
- improving simulation diagnostics  
- refining experimental apparatus definitions  
- contributing examples or tutorials  
- helping with v0.2 roadmap items  
