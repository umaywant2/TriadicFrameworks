# Boundary Conditions

This document defines the boundary condition types supported by the Resonance Substrate Model.

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
- [docs simulations numerical methods](numerical_methods.md)
- [docs simulations README](README.md)
- [docs simulations solver_architecture](solver_architecture.md)
- [docs simulations validation metrics](validation_metrics.md)
- [docs simulations core README](core/README.md)
- [previous folder](../)

---

## 1. Dirichlet Boundaries
Fixed-value boundaries for fields such as:
- temperature  
- charge  
- resonance envelope  

## 2. Neumann Boundaries
Gradient-based boundaries used for:
- diffusion processes  
- spin-field alignment constraints  

## 3. Periodic Boundaries
Used for:
- rotating field tests  
- resonance envelope continuity  
- toroidal or looped domains  

## 4. Custom Boundaries
User-defined boundary handlers for:
- dynamic field injection  
- rotating-frame transformations  
- experimental analogs (e.g., Faraday paradox setups)  

