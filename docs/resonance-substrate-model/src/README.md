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
