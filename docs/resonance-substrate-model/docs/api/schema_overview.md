# Schema Overview

This document provides a conceptual overview of the schema system used in the Resonance Substrate Model.

---

## 1. Schema Categories

### Field Schemas
Define scalar, vector, spin-field, and resonance envelope structures.

### Operator Schemas
Specify operator parameters, types, and composition rules.

### Simulation Schemas
Describe grid configuration, timesteps, boundary conditions, and solver settings.

### Experiment Schemas
Capture metadata, apparatus details, and run configurations.

### Distributed Layer Schemas
Define node identities, communication channels, and synchronization rules.

---

## 2. Schema Structure
Most schemas follow a common pattern:
- `id` — unique identifier  
- `type` — schema category  
- `fields` — required and optional parameters  
- `constraints` — validation rules  
- `metadata` — descriptive information  

---

## 3. Schema Relationships
Schemas may reference one another:
- simulation schemas reference operator schemas  
- experiment schemas reference field schemas  
- distributed schemas reference simulation schemas  

This modularity enables flexible composition.

---

## 4. Purpose
The schema system provides:
- consistency across modules  
- clarity for contributors  
- a stable foundation for tooling and automation  

# Quicklinks

- [docs api integration examples](integration_examples.md)
- [docs api README](README.md)
- [docs api using the schemas](using_the_schemas.md)
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
