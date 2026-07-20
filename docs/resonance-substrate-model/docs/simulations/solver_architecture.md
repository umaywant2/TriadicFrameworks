# Solver Architecture

This document describes the architecture of the simulation solver used in the Resonance Substrate Model.

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
- [docs simulations validation metrics](validation_metrics.md)
- [docs simulations core README](core/README.md)
- [previous folder](../)

---

## 1. Overview
The solver is structured as a modular pipeline that processes field states, applies operators, and advances the system through time.

## 2. Core Components
- **State Manager** — stores scalar, vector, spin, and resonance fields  
- **Operator Engine** — applies diffusion, decay, alignment, and coupling operators  
- **Time Integrator** — advances fields using explicit or implicit schemes  
- **Boundary Handler** — enforces boundary conditions  
- **Diagnostics Module** — collects metrics and logs  

## 3. Execution Flow
1. Load initial state  
2. Apply operators  
3. Integrate in time  
4. Enforce boundaries  
5. Record diagnostics  
6. Repeat until termination criteria are met  

## 4. Extensibility
- plugin-style operator modules  
- configurable integration schemes  
- multi-resolution grid support  

