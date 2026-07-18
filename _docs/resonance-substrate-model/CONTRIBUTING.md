## Quicklinks

- [applications complex systems](applications/complex-systems.md)
- [CHANGELOG](CHANGELOG.md)
- [docs README](docs/README.md)
- [data README](data/README.md)
- [experiments README](experiments/README.md)
- [papers substrate model whitepaper manuscript](papers/substrate_model_whitepaper/manuscript.md)
- [papers README](papers/README.md)
- [reference Keywords](reference/Keywords.md)
- [schemas README](schemas/README.md)
- [simulations README](simulations/README.md)
- [tools README](tools/README.md)
- [README](README.md)
- [RELEASE NOTES](RELEASE_NOTES.md)
- [previous folder](../)

# **🚀 Contributing Quick‑Start**

New to the project? Start here.  
This is the fastest path to making a meaningful contribution to TriadicFrameworks.

## **1. Fork the Repo & Create a Branch**
```bash
git checkout -b feature/my-improvement
```
Use clear, descriptive names:
- `feature/add-alignment-operator`
- `fix/vector-field-init`
- `docs/update-simulation-notes`

## **2. Pick a Good First Task**
Great entry points include:
- improving documentation in `docs/`
- adding examples to `simulations/`
- refining schemas in `schemas/`
- writing small tests in `tests/`
- fixing typos or clarifying comments in `src/`

These tasks help you learn the structure without diving into deep internals.

## **3. Follow Canonical Naming**
Keep everything consistent:
- folders → `lowercase-with-hyphens`
- code → `snake_case`
- schemas → descriptive, stable names
- operators → match manuscript terminology

Consistency is part of the architecture.

## **4. Run Tests Before Submitting**
```bash
pytest
```
If you add functionality, add or update tests in `tests/`.

## **5. Update Docs When Needed**
If your change affects:
- fields  
- operators  
- schemas  
- simulations  
- experiments  

update the relevant docs.  
Documentation is a first‑class artifact in this project.

## **6. Open a Pull Request**
Include:
- what you changed  
- why it matters  
- any schema or doc updates  
- any tests added  

Small, focused PRs are easiest to review.

## **7. Be Kind, Clear, and Curious**
We value:
- clarity  
- coherence  
- reproducibility  
- shared discovery  

Reviews are collaborative and constructive.

---

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

---

