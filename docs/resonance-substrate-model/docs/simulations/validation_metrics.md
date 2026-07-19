# Validation Metrics

This document outlines the metrics used to validate simulations within the Resonance Substrate Model.

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
- [docs simulations numerical methods](numerical_methods.md)
- [docs simulations README](README.md)
- [docs simulations solver_architecture](solver_architecture.md)
- [docs simulations core README](core/README.md)
- [previous folder](../)

---

## 1. Field-Level Metrics
- **L2 error norm** — deviation from analytical or reference solutions  
- **Gradient consistency** — smoothness and stability of field derivatives  
- **Energy conservation** — tracking total system energy over time  

## 2. Operator-Level Metrics
- **Diffusion stability index**  
- **Alignment convergence rate**  
- **Spin-field coherence score**  

## 3. System-Level Metrics
- **Resonance envelope activation accuracy**  
- **Temporal stability under perturbation**  
- **Cross-layer consistency checks**  

## 4. Benchmarking
- comparison against known analytical solutions  
- reproducibility across runs  
- sensitivity to grid resolution and timestep  

