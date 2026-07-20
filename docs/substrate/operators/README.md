# Operator System

The `operators/` directory implements the five operator families defined in the manuscript:

- **Diffusion**  
- **Alignment**  
- **Coupling**  
- **Activation**  
- **Stabilization**
- **Arrival**

Each operator acts on one or more of the triadic fields:

- scalar field `phi`
- vector field `V`
- resonance envelope `R`

Operators are pure functions:  
they take field states + coefficients and return updated fields.  
This keeps the substrate modular, testable, and easy to extend.
