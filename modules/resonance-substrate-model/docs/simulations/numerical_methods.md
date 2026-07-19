# Numerical Methods

This document summarizes the numerical methods used in the Resonance Substrate Model simulations.

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
- [docs methods dimensional layers](../methods/dimensional_layers.md)
- [docs methods field equations](../methods/field_equations.md)
- [docs methods operator definitions](../methods/operator_definitions.md)
- [docs methods README](../methods/README.md)
- [docs methods substrate dynamics](../methods/substrate_dynamics.md)
- [docs methods triadic fields](../methods/triadic_fields.md)
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
- [docs simulations boundary conditions](boundary_conditions.md)
- [docs simulations README](README.md)
- [docs simulations solver_architecture](solver_architecture.md)
- [docs simulations validation metrics](validation_metrics.md)
- [docs simulations core README](core/README.md)
- [previous folder](../)

---

## 1. Discretization
- finite difference schemes for scalar and vector fields  
- finite volume methods for flux-based operators  
- optional spectral methods for smooth domains  

## 2. Time Integration
- explicit Euler for rapid prototyping  
- Runge–Kutta methods for improved stability  
- semi-implicit schemes for stiff operators  

## 3. Stability Considerations
- CFL conditions for diffusion and advection  
- timestep adaptivity  
- error estimation and correction  

## 4. Grid Structures
- uniform Cartesian grids  
- support for multi-resolution or nested grids  

