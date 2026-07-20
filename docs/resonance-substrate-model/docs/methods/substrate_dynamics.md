# Substrate Dynamics

Substrate dynamics describe how triadic fields evolve over time through the application of operators, boundary conditions, and integration schemes. This unified version merges early conceptual notes with the newer structured scaffolding.

---

# Quicklinks

- [docs README](../README.md)
- [docs api integration examples](../api/integration_examples.md)
- [docs api README](../api/README.md)
- [docs api schema overview](../api/schema_overview.md)
- [docs api using the schemas](../api/using_the_schemas.md)
- [docs experiments faraday paradox experiment](../experiments/faraday_paradox_experiment.md)
- [docs experiments README](../experiments/README.md)
- [docs experiments replication checklist](../experiments/replication_checklist.md)
- [docs experiments resonance alignment tests](../experiments/resonance_alignment_tests.md)
- [docs experiments rotating conductor tests](../experiments/rotating_conductor_tests.md)
- [docs methods dimensional layers](dimensional_layers.md)
- [docs methods field equations](field_equations.md)
- [docs methods operator definitions](operator_definitions.md)
- [docs methods README](README.md)
- [docs methods triadic fields](triadic_fields.md)
- [docs onboarding model map](../onboarding/model_map.md)
- [docs onboarding reading guide](../onboarding/reading_guide.md)
- [docs onboarding triadic quickstart](../onboarding/triadic_quickstart.md)
- [docs onboarding verification tests](../onboarding/verification_tests.md)
- [docs overview comparison to gr models](../overview/comparison_to_gr_models.md)
- [docs overview glossary](../overview/glossary.md)
- [docs overview introduction](../overview/introduction.md)
- [docs overview README](../overview/README.md)
- [docs overview resonance primitives](../overview/resonance_primitives.md)
- [docs overview theoretical background](../overview/theoretical_background.md)
- [docs simulations boundary conditions](../simulations/boundary_conditions.md)
- [docs simulations numerical methods](../simulations/numerical_methods.md)
- [docs simulations README](../simulations/README.md)
- [docs simulations solver_architecture](../simulations/solver_architecture.md)
- [docs simulations validation metrics](../simulations/validation_metrics.md)
- [docs simulations core README](../simulations/core/README.md)
- [previous folder](../)

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
