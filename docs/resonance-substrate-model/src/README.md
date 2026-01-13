# 📁 `src/` — README (purpose of the source folder)

## **resonance‑substrate‑model / src**
This directory contains the **core source code** for the Resonance Substrate Model. Everything here is implementation‑facing: the algorithms, operators, data structures, and computational primitives that realize the substrate’s behavior.

### **What lives here**
- **Core model operators**  
  Resonance kernels, substrate update rules, diffusion‑like propagation, and temporal‑phase alignment logic.
- **Numerical routines**  
  Discretization, stability helpers, finite‑volume/finite‑difference utilities, and integration scaffolds.
- **Data structures**  
  Substrate state objects, lattice/graph representations, resonance‑time buffers, and field containers.
- **Internal utilities**  
  Logging, configuration parsing, diagnostics, and shared helpers used across tests and demos.

### **Purpose**
This folder is the **authoritative implementation layer** of the model. Everything here is meant to be:
- deterministic  
- reproducible  
- testable  
- modular  
- ready for integration into higher‑level simulations or external systems

If the model evolves, this is the folder that evolves with it.

---

## Quicklinks

- [tools README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/tools/README.md)
- [tools visualization README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/tools/visualization/README.md)
- [tools converters README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/tools/converters/README.md)
- [tools cli README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/tools/cli/README.md)
- [tests README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/tests/README.md)
- [simulations README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/simulations/README.md)
- [simulations examples README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/simulations/examples/README.md)
- [simulations core README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/simulations/core/README.md)
- [simulations configs README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/resonance-substrate-model/simulations/configs/README.md)
