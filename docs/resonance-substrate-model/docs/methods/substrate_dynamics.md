# Substrate Dynamics

Substrate dynamics describe how triadic fields evolve over time through the application of operators, boundary conditions, and integration schemes. This unified version merges early conceptual notes with the newer structured scaffolding.

---

## 1. Evolution Framework

Field evolution follows a general update rule:

1. Apply operators  
2. Integrate in time  
3. Enforce boundaries  
4. Record diagnostics  

This loop continues until termination criteria are met.

---

## 2. Operator Application

Operators act on fields in a defined sequence or composition:

- **diffusion** smooths scalar and vector fields  
- **alignment** drives directional coherence  
- **coupling** links fields across layers  
- **resonance activation** triggers envelope dynamics  
- **decay** stabilizes the system  

Operator composition may be linear, nonlinear, or gated by resonance conditions.

---

## 3. Time Integration

The substrate supports multiple integration schemes:

- explicit Euler (rapid prototyping)  
- Runge–Kutta (higher stability)  
- semi-implicit methods (stiff operators)  

Timestep selection respects stability constraints such as CFL conditions.

---

## 4. Boundary Conditions

Boundary handlers enforce:

- Dirichlet conditions (fixed values)  
- Neumann conditions (fixed gradients)  
- periodic boundaries (looped domains)  
- custom experimental boundaries (e.g., rotating-frame transforms)  

Boundaries are applied after operator updates to maintain physical consistency.

---

## 5. Stability and Control

Stability is maintained through:

- damping  
- normalization  
- resonance envelope clipping  
- timestep adaptivity  

These mechanisms prevent runaway growth and ensure coherent evolution.

---

## 6. Emergent Behavior

Dynamic interactions among fields and operators can produce:

- coherent resonance pockets  
- rotating or oscillatory patterns  
- alignment waves  
- paradox-class responses  

These emergent structures are central to the substrate’s expressive power.
