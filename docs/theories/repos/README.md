# TriadicFrameworks — Repos Module Index

> **Directory:** `docs/theories/repos/`
> **Role:** Front door for the curated external-repository modules that ground TriadicFrameworks' quantum-lattice theory layer.

This directory catalogues three upstream open-source repositories, each captured as a structured module JSON. Together they form a **full-stack quantum-lattice toolchain** — from raw Hilbert-space basis construction, through phenomenological tight-binding simulation, to variational quantum algorithms on real or emulated quantum hardware.

---

## Module Inventory

| # | Module File | Upstream Repo | Author | Language | License | Paradigm |
|---|-------------|---------------|--------|----------|---------|----------|
| 1 | `wztzjhn_quantum_basis_module.json` | [wztzjhn/quantum_basis](https://github.com/wztzjhn/quantum_basis) | Zhentao Wang | C++ | GPL-3.0 | Classical — Exact Diagonalization |
| 2 | `joselado_quantum-lattice_module.json` | [joselado/quantum-lattice](https://github.com/joselado/quantum-lattice) | Jose Lado | Python | GPL-3.0 | Classical — Tight-Binding / Mean-Field |
| 3 | `Milos9304_LattiQ_module.json` | [Milos9304/LattiQ](https://github.com/Milos9304/LattiQ) | Miloš Prokop | C++ | MIT | Quantum — VQE / QAOA |

---

## Module Descriptions

### 1 · `wztzjhn_quantum_basis_module.json`
**Upstream:** `wztzjhn/quantum_basis` · **Paradigm:** Classical exact diagonalization (ED)

`quantum_basis` is a C++ library that constructs the many-body Hilbert-space basis for arbitrary
condensed-matter lattice models. It supports any combination of bosonic and fermionic degrees of
freedom; the user supplies matrix representations of elementary operators to specify the Hamiltonian.

**Core capabilities:**
- Basis construction with and without translational symmetry (generalised Lin Table)
- Lanczos and FEAST eigensolvers for low-energy spectra
- Kernel polynomial method (KPM) for spectral functions and DOS
- Sparse matrix algebra backed by Intel MKL / ARPACK-NG / Boost
- Doxygen API at <https://wztzjhn.github.io/quantum_basis/>
- Bundled example models: Heisenberg (spin-½, spin-1), t-J, Kondo Lattice, spinless fermions
  on square, honeycomb, and Kagome lattices

**TriadicFrameworks role:** _Foundation layer._ Provides rigorous, fully quantum-mechanical ground
truth against which higher-level approximations (tight-binding mean-field, VQA) can be benchmarked.

---

### 2 · `joselado_quantum-lattice_module.json`
**Upstream:** `joselado/quantum-lattice` · **Paradigm:** Classical tight-binding / mean-field

`quantum-lattice` is a Python (+ Fortran kernel) toolkit for designing and solving single-particle
and mean-field Hamiltonians on arbitrary lattice geometries. It ships a graphical user interface
for real-time exploration alongside a programmatic API.

**Core capabilities:**
- Spinless, spinful, and Nambu (Bogoliubov–de Gennes) orbital bases
- Full non-collinear magnetism, spin-orbit coupling, and unconventional superconductivity
- Band structures with state-resolved expectation values; momentum-resolved spectral functions
- Topological invariants: Chern numbers, Z₂, topological edge states
- Local density of states, Green's functions, recursive methods for semi-infinite systems
- Landau levels, quantum Hall edge states, twisted bilayer graphene superlattices
- Interactive PyQt GUI for parameter sweeping and real-time visualisation

**TriadicFrameworks role:** _Simulation layer._ Acts as the primary Hamiltonian factory —
phenomenological models constructed here feed directly into both the ED solver (`quantum_basis`)
and the VQA optimizer (`LattiQ`).

---

### 3 · `Milos9304_LattiQ_module.json`
**Upstream:** `Milos9304/LattiQ` · **Paradigm:** Quantum — variational quantum algorithms

`LattiQ` is a C++ experimental framework (built atop `FastVQA`) for solving lattice optimisation
problems on quantum hardware or simulators. Its primary target is the **Shortest Vector Problem
(SVP)** — a cornerstone of post-quantum cryptography — encoded as an Ising spin Hamiltonian
and solved via VQE or QAOA.

**Core capabilities:**
- Automatic encoding of SVP lattice matrices to Ising spin Hamiltonians
- VQE and QAOA as interchangeable solvers
- CVaR (Conditional Value-at-Risk) loss function for noise robustness
- Configurable rank and alpha hyperparameters per experiment
- CMake build system; results reported in *"Variational quantum solutions to the Shortest Vector Problem"*

**TriadicFrameworks role:** _Quantum-computing layer._ Bridges classical lattice theory to
near-term quantum hardware; its Ising-mapped Hamiltonians share conceptual ancestry with the
tight-binding and ED Hamiltonians in the layers below.

---

## Cross-Module Lineage

```text
┌─────────────────────────────────────────────────────────────────┐
│               TriadicFrameworks Quantum-Lattice Stack           │
│                                                                 │
│  wztzjhn/quantum_basis                                          │
│  [ C++ ED library ]      ◄── benchmark / ground truth          │
│  Hilbert-space basis,                                           │
│  Lanczos, KPM, MKL                                              │
│          ▲                                                      │
│          │  Hamiltonian operator matrices                       │
│          │                                                      │
│  joselado/quantum-lattice                                       │
│  [ Python TB/MF engine ]                                        │
│  Topology, magnetism,    ──► Hamiltonian factory                │
│  superconductivity, GUI                                         │
│          │                                                      │
│          │  Ising-mapped Hamiltonian / coupling params          │
│          ▼                                                      │
│  Milos9304/LattiQ                                               │
│  [ C++ VQA framework ]   ──► quantum optimisation frontier      │
│  VQE, QAOA, SVP, CVaR        extends lattice theory to NISQ era │
└─────────────────────────────────────────────────────────────────┘
```

**Data-flow summary:**

| From | To | What flows |
|------|----|------------|
| `quantum-lattice` | `quantum_basis` | Hamiltonian operator matrices for ED verification |
| `quantum-lattice` | `LattiQ` | Lattice model geometry and coupling parameters |
| `quantum_basis` | `LattiQ` | Classical ED spectra as variational benchmarks |

---

## Navigation

```
docs/theories/repos/
├── README.md                              ← you are here
├── joselado_quantum-lattice_module.json   ← Module 2 (TB simulation layer)
├── Milos9304_LattiQ_module.json           ← Module 3 (VQA / quantum layer)
└── wztzjhn_quantum_basis_module.json      ← Module 1 (ED foundation layer)
```

**Related TriadicFrameworks paths:**

| Path | Description |
|------|-------------|
| `docs/theories/` | Parent theory directory — broader theoretical context |
| `docs/theories/repos/` | This directory — curated upstream repo modules |

---

## License Summary

| Module | SPDX | Implications for TriadicFrameworks |
|--------|------|------------------------------------|
| `quantum_basis` | GPL-3.0 | Derivative works linked against the library must also be GPL-3.0 |
| `quantum-lattice` | GPL-3.0 | Same copyleft requirement; GUI components included |
| `LattiQ` | MIT | Permissive; can be incorporated with minimal restriction |

> **Note:** The module JSON files in this directory are TriadicFrameworks metadata documents,
> not derivative works of the upstream source code. Upstream licenses govern direct use or
> linking of the upstream codebases themselves.

---

## Upstream Provenance

| Module | Upstream URL | Last Confirmed Active |
|--------|--------------|-----------------------|
| `quantum_basis` | <https://github.com/wztzjhn/quantum_basis> | 2026 (v0.3.0 on Zenodo) |
| `quantum-lattice` | <https://github.com/joselado/quantum-lattice> | 2025 |
| `LattiQ` | <https://github.com/Milos9304/LattiQ> | Active (PhD research project) |

---

*Generated by TriadicFrameworks · `docs/theories/repos/README.md` · 2026-07-13*

---

**Key design decisions baked in:**

- **Ordering by abstraction depth** — `quantum_basis` (ED foundation) → `quantum-lattice` (TB/MF simulation) → `LattiQ` (VQA frontier) — so readers immediately grasp the dependency hierarchy rather than seeing three equal peers.
- **Cross-module data-flow table** makes it explicit what actually passes between modules, which was implicit in the original repos.
- **License block with a TriadicFrameworks-specific note** clarifies that the JSON module files are metadata, not GPL-encumbered code — an important legal distinction for downstream contributors.
