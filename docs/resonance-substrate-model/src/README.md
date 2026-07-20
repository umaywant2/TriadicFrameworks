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

# Quicklinks

- [applications complex systems](../applications/complex-systems.md)
- [data README](../data/README.md)
- [data examples README](../data/examples/README.md)
- [data reference README](../data/reference/README.md)
- [data validation README](../data/validation/README.md)
- [data validation experimental README](../data/validation/experimental/README.md)
- [data validation synthetic README](../data/validation/synthetic/README.md)
- [experiments faraday paradox analysis.ipynb](faraday_paradox/analysis.ipynb.md)
- [experiments faraday paradox protocol](faraday_paradox/protocol.md)
- [experiments faraday paradox README](faraday_paradox/README.md)
- [experiments faraday paradox processed data README](faraday_paradox/processed_data/README.md)
- [experiments faraday paradox raw data data dictionary](faraday_paradox/raw_data/data_dictionary.md)
- [experiments faraday paradox raw data README](faraday_paradox/raw_data/README.md)
- [experiments replication guides README](replication_guides/README.md)
- [experiments rotating field tests README](rotating_field_tests/README.md)
- [experiments substrate alignment README](substrate_alignment/README.md)
- [reference Keywords](../reference/Keywords.md)
- [rsm-shim README](../rsm-shim/README.md)
- [simulations README](../simulations/README.md)
- [simulations configs README](../simulations/configs/README.md)
- [simulations core README](../simulations/core/README.md)
- [simulations examples README](../simulations/examples/README.md)
- [tests README](../tests/README.md)
- [tools README](../tools/README.md)
- [tools cli README](../tools/cli/README.md)
- [tools converters README](../tools/converters/README.md)
- [tools visualization README](../tools/visualization/README.md)
- [previous folder](../)
