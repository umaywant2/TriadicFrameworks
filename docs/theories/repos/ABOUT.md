# ABOUT — `docs/theories/repos/`

> **TriadicFrameworks Canonical Documentation**
> Scope: Quantum-theoretic module registry for the `/docs/theories/repos/` directory.
> Status: Canonical · Living Document

---

## Purpose

The `repos/` directory within `docs/theories/` serves as the **canonical module registry** for all quantum-theoretic repositories operating under the TriadicFrameworks canon. It is not an aggregator of code; it is a curated ontological record — a structured declaration of what each module *is*, what conceptual territory it holds, and how it articulates with adjacent modules across the triadic dependency chain.

Modules housed here are not stand-alone libraries. Each is a **load-bearing node** in a deliberately layered theoretical architecture. Their individual coherence matters; their relational coherence is the point.

---

## Scope

This directory governs exactly three modules, arranged in strict triadic order:

| Layer | Module | Triadic Role |
|-------|--------|-------------|
| I — Primitive | `quantum_basis` | Mathematical substrate and state-space vocabulary |
| II — Structure | `quantum-lattice` | Topological scaffold and relational arrangement of quantum states |
| III — Interface | `LattiQ` | Operational synthesis bridge to higher-level canon constructs |

The scope is **intentionally bounded**. These three modules constitute one complete triadic unit — a closed functional arc from raw formalism to applied interface. Additions to this directory require canonical review; new modules must occupy a defined triadic slot, not augment an existing one.

---

## Conceptual Stance

TriadicFrameworks operates on the conviction that theoretical architecture, like physical systems, exhibits **irreducible triadic structure**: every coherent domain resolves into a primitive substrate, a structural arrangement of that substrate, and an interfacing layer that makes the structure legible and composable within a broader system.

This is not a pattern imposed on the quantum modules — it is the pattern these modules *embody*. The quantum-theoretic cluster was the first to make the triadic scaffold explicit:

- **Primitives without structure** are unordered — mathematically present but operationally inert.
- **Structure without primitives** is form without content — valid topology over empty space.
- **Interface without the layers beneath it** is abstraction without ground — a vocabulary with no referent.

All three modules exist because none is sufficient alone. The directory exists to enforce and document that necessity.

---

## Module Roles

### `quantum_basis` — Layer I · Primitive

`quantum_basis` defines the foundational mathematical vocabulary from which all other quantum-theoretic modules in this canon are constructed. It establishes:

- The **state-space primitives**: basis vectors, Hilbert space representations, and the algebraic rules governing their composition.
- The **canonical unit types** used uniformly across `quantum-lattice` and `LattiQ` — ensuring type coherence is enforced at the substrate level rather than retrofitted at integration seams.
- The **formal postulates** that constrain what counts as a valid quantum-theoretic object within TriadicFrameworks. This is the canon's source of truth for quantum ontology.

`quantum_basis` has **no upstream dependencies** within this directory. It is the dependency terminus — the floor.

---

### `quantum-lattice` — Layer II · Structure

`quantum-lattice` receives the primitives defined by `quantum_basis` and arranges them into **topologically coherent relational structures**. It is the architectural middle layer: it does not invent new primitives, nor does it expose external interfaces. It builds.

Responsibilities include:

- Defining the **lattice topology** — the partial-order and join/meet structures through which quantum states relate to one another.
- Encoding **entanglement geometries** and superposition arrangements as first-class structural objects rather than emergent side-effects.
- Providing the **traversal and composition rules** that `LattiQ` will expose operationally — the grammar before the vocabulary is published.

`quantum-lattice` depends on `quantum_basis`. It is the module most likely to evolve as the theoretical framework matures, because structure is where theoretical refinement lives.

---

### `LattiQ` — Layer III · Interface

`LattiQ` is the **synthesis module** — the operational surface that makes the quantum-theoretic cluster composable with the broader TriadicFrameworks canon. It is the module external systems and higher-order theories interact with directly.

Responsibilities include:

- **Translating** the internal constructs of `quantum-lattice` into the canonical interface types expected by TriadicFrameworks consumers.
- **Enforcing abstraction boundaries** — callers of `LattiQ` need not and should not reason about lattice topology or basis primitives directly; `LattiQ` mediates that complexity.
- **Providing extension hooks** where the quantum-theoretic cluster can be composed with other triadic clusters in the canon — the documented integration seam.

`LattiQ` depends on both `quantum_basis` (for type compatibility) and `quantum-lattice` (for structural semantics). It is the **public face of this triadic unit**.

---

## Integration Role within TriadicFrameworks Canon

The three modules in this directory collectively constitute the **quantum-theoretic primitive cluster** of TriadicFrameworks. As a cluster, they serve the broader canon in two directions:

**Downward (foundational):** They provide the mathematical and structural grounding for any TriadicFrameworks theory that incorporates quantum-theoretic reasoning. Any canon module that makes claims about quantum state, superposition, entanglement, or measurement must ground those claims through this cluster — specifically through `LattiQ`'s interface.

**Upward (compositional):** The cluster is designed to be composed with other triadic clusters via `LattiQ`. This is the canonical pattern: triadic clusters do not reach into one another's internals; they compose through their Layer III interface modules. Cross-cluster dependencies are always `LattiQ`-to-Layer-III bindings.

This architecture ensures that theoretical evolution within the quantum-theoretic cluster (e.g., refinements to `quantum-lattice`'s topology) does not propagate instability outward into the broader canon — provided the `LattiQ` interface contract is maintained.

---

## Governance

| Concern | Policy |
|---------|--------|
| Adding a module | Requires triadic slot justification and canonical review |
| Modifying `quantum_basis` | Breaking changes require full cluster versioning |
| Modifying `quantum-lattice` | Must preserve all `LattiQ`-exposed structural contracts |
| Modifying `LattiQ` | Interface changes require cross-canon impact assessment |
| Deprecating a module | Permitted only if the triadic slot is retired or replaced as a unit |

---

## See Also

- `docs/theories/ABOUT.md` — Parent scope: the full theories directory and its place in TriadicFrameworks
- `LattiQ/README.md` — Interface specification and integration guide
- `quantum-lattice/README.md` — Structural topology reference
- `quantum_basis/README.md` — Primitive definitions and formal postulates

---

*This document is maintained as part of the TriadicFrameworks canonical record. It describes architecture and intent, not implementation. For implementation details, consult each module's own documentation.*
