# Resonance Substrate Model — Schema Directory

This directory contains the machine‑readable schemas that define the
structural, operational, and ontological components of the Resonance
Substrate Model (RSM). These schemas ensure reproducibility, clarity,
and interoperability across simulations, experiments, and downstream
TriadicFrameworks modules.

## Purpose of the Schema Layer

The schema system provides:

- **Field primitives** (scalar, vector/spin, resonance envelope)
- **Operator definitions** (diffusion, alignment, coupling, activation, stabilization)
- **Dimensional structures** (grids, coordinates, layers)
- **Energy and substrate dynamics**
- **Quantum and semantic extensions**
- **Sensing and measurement constructs**
- **Identity and language entities**
- **Networking and distributed‑layer structures**
- **Simulation configuration and validation rules**
- **Universe‑core abstractions** for cross‑domain coherence

Each schema family corresponds to a conceptual layer of the RSM ontology.

## Directory Structure

- `coeus/` — cognitive, symbolic, and semantic schema primitives  
- `dimensional/` — coordinate systems, grids, and multi‑layer geometry  
- `energy/` — energy flow, dissipation, and resonance‑amplitude structures  
- `experiments/` — apparatus, measurement, and replication schemas  
- `fields/` — scalar, vector/spin, and resonance‑envelope field definitions  
- `operators/` — operator definitions and parameter constraints  
- `primitives/` — low‑level building blocks used across all schema families  
- `quantum/` — spin, phase, coherence, and quantum‑layer constructs  
- `sensing/` — measurement, calibration, and uncertainty models  
- `simulations/` — simulation configuration, solver parameters, and validation rules  
- `universe-core/` — high‑level abstractions for cross‑domain coherence

## Schema Format

All schemas follow:

- **JSON Schema Draft‑07** (unless otherwise noted)
- **TriadicFrameworks naming conventions**
- **RSM v1.0 ontology alignment**

Each schema includes:

- `title`  
- `description`  
- `type`  
- `properties`  
- `required` fields  
- `examples` (when applicable)

## How These Schemas Are Used

- The **simulation engine** validates all configs against these schemas.  
- The **CLI tools** (`validate.py`, `inspect_schema.py`) operate directly on them.  
- The **documentation** in `docs/api/` is generated from these schemas.  
- The **experiments** reference them for apparatus and measurement consistency.

## Contributing

When adding or modifying schemas:

1. Maintain backward compatibility when possible.  
2. Include examples for new fields.  
3. Update the simulation schema if new operators or fields are introduced.  
4. Ensure naming consistency across schema families.  
5. Validate using the CLI tools before committing.

This directory forms the canonical ontology for the Resonance Substrate Model.

---

## Quicklinks

- [schemas coeus README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/schemas/coeus/README.md)
- [schemas dimensional README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/schemas/dimensional/README.md)
- [schemas distributed README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/schemas/distributed/README.md)
- [schemas energy README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/schemas/energy/README.md)
- [schemas experiments README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/schemas/experiments/README.md)
- [schemas fields README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/schemas/fields/README.md)
- [schemas finance README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/schemas/finance/README.md)
- [schemas identity README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/schemas/identity/README.md)
- [schemas infrastructure README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/schemas/infrastructure/README.md)
- [schemas lab README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/schemas/lab/README.md)
- [schemas language README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/schemas/language/README.md)
- [schemas networking README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/schemas/networking/README.md)
- [schemas operators README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/schemas/operators/README.md)
- [schemas primitives README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/schemas/primitives/README.md)
- [schemas quantum README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/schemas/quantum/README.md)
- [schemas sensing README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/schemas/sensing/README.md)
- [schemas simulations README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/schemas/simulations/README.md)
- [schemas universe-core README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/schemas/universe-core/README.md)
