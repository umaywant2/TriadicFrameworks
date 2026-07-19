# **Operator Definitions**  
*A unified, canonical reference for all substrate operators*

Operators define how fields evolve, interact, and transform within the Resonance Substrate Model. They are the core mathematical and conceptual tools that drive substrate dynamics across classical, quantum, semantic, and distributed layers.

This document merges the early conceptual framing with the newer structured taxonomy to provide a complete, extensible foundation.

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
- [docs methods README](README.md)
- [docs methods substrate dynamics](substrate_dynamics.md)
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

## **1. Diffusion Operator**

### Purpose  
Smooths or spreads field values across the substrate, modeling transport, dissipation, and coherence propagation.

### Applies To  
- scalar fields  
- vector fields  
- resonance envelopes (optional, controlled diffusion)

### Variants  
- **isotropic diffusion** — uniform spreading  
- **anisotropic diffusion** — directionally biased  
- **manifold-aware diffusion** — respects curvature and metric structure  

### Notes  
Early versions emphasized diffusion as a “substrate equalizer.”  
The unified model treats it as a first-class operator with tunable geometry and stability constraints.

---

## **2. Alignment Operator**

### Purpose  
Encourages local or global coherence among directional or spin-like fields.

### Applies To  
- spin-fields  
- vector fields  
- semantic alignment structures (higher layers)

### Behavior  
- normalizes local vectors  
- pulls neighbors toward shared orientation  
- may include damping or resonance-weighted influence  

### Notes  
Earlier drafts described alignment as “coherence pressure.”  
This merged version formalizes it as a directional operator with explicit normalization rules.

---

## **3. Coupling Operator**

### Purpose  
Links multiple fields so that changes in one influence another.

### Common Couplings  
- scalar ↔ vector  
- resonance envelope ↔ spin-field  
- classical layer ↔ quantum layer  
- semantic layer ↔ resonance layer  

### Forms  
- linear coupling  
- nonlinear coupling  
- thresholded or gated coupling  

### Notes  
The early operator doc emphasized “cross-field influence.”  
This unified version formalizes coupling as a structured, configurable operator family.

---

## **4. Resonance Activation Operator**

### Purpose  
Determines when and where resonance envelopes activate, intensify, or decay.

### Activation Modes  
- threshold-based  
- gradient-based  
- operator-driven (e.g., alignment-triggered)  
- coherence-driven (quantum layer influence)

### Behavior  
- amplifies local field activity  
- creates localized “resonance pockets”  
- interacts with diffusion and alignment operators  

### Notes  
Early drafts described resonance activation as “field ignition.”  
This merged version integrates it into the operator taxonomy with explicit activation logic.

---

## **5. Decay / Stabilization Operator**

### Purpose  
Prevents runaway growth, oscillation, or instability in evolving fields.

### Applies To  
- scalar fields  
- spin-fields  
- resonance envelopes  
- coherence structures  

### Forms  
- exponential decay  
- damping  
- normalization  
- clipping or bounding  

### Notes  
This operator was implicit in early drafts; now it is explicitly defined as a stabilizing component of the substrate.

---

## **6. Projection and Mapping Operators**

### Purpose  
Translate fields across layers, dimensions, or coordinate systems.

### Examples  
- classical → quantum projection  
- semantic → resonance modulation  
- manifold coordinate transforms  
- layer-to-layer embeddings  

### Notes  
Early drafts hinted at “dimensional bridges.”  
This unified version formalizes them as projection operators with clear roles.

---

## **7. Custom and Experimental Operators**

### Purpose  
Support domain-specific or experimental behaviors.

### Examples  
- rotating-frame transforms (Faraday paradox experiments)  
- external field injection  
- semantic packet modulation  
- coherence perturbation operators  

### Notes  
This section preserves the exploratory spirit of the early operator doc while giving it a structured home.

---

# **Summary**

This merged operator document now reflects:

- the **conceptual richness** of the early drafts  
- the **structured clarity** of the newer scaffolds  
- the **extensibility** needed for future layers and experiments  
