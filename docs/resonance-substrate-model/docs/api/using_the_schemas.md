# Using the Schemas

Schemas define the structure, constraints, and relationships of data used throughout the Resonance Substrate Model. This document explains how to load, validate, and work with these schemas in external tools or applications.

---

## 1. Purpose of the Schemas
Schemas ensure:
- consistent field definitions  
- reproducible simulation configurations  
- standardized experiment metadata  
- compatibility across layers and modules  

---

## 2. Loading Schemas
Schemas are typically stored as JSON or YAML files and can be loaded using standard parsing libraries.

Example workflow:
1. load schema file  
2. validate configuration against schema  
3. construct substrate objects from validated data  

---

## 3. Validation
Validation ensures:
- required fields are present  
- field types match expectations  
- operator parameters fall within allowed ranges  

Validation errors should be treated as configuration issues rather than runtime failures.

---

## 4. Extending Schemas
Schemas can be extended to support:
- new operators  
- custom experiment types  
- additional metadata fields  
- domain-specific configurations  

Extensions should maintain backward compatibility whenever possible.

# Quicklinks

- [docs api integration examples](integration_examples.md)
- [docs api README](README.md)
- [docs api schema overview](schema_overview.md)
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
- [docs simulations boundary conditions](../simulations/boundary_conditions.md)
- [docs simulations numerical methods](../simulations/numerical_methods.md)
- [docs simulations README](../simulations/README.md)
- [docs simulations solver_architecture](../simulations/solver_architecture.md)
- [docs simulations validation metrics](../simulations/validation_metrics.md)
- [docs simulations core README](../simulations/core/README.md)
- [previous folder](../)
