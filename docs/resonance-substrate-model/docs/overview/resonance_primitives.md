# Resonance Primitives  
## Formal Definitions of the SET Field Components

The resonance‑substrate model is built on three irreducible field primitives:  
Spin (S), Charge (C), and Temperature (T).  
Together they form the SET triad, which defines the substrate‑level state at each point in the underlying medium.

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
- [docs overview comparison to gr models](comparison_to_gr_models.md)
- [docs overview glossary](glossary.md)
- [docs overview introduction](introduction.md)
- [docs overview README](README.md)
- [docs overview theoretical background](theoretical_background.md)
- [docs simulations boundary conditions](../simulations/boundary_conditions.md)
- [docs simulations numerical methods](../simulations/numerical_methods.md)
- [docs simulations README](../simulations/README.md)
- [docs simulations solver_architecture](../simulations/solver_architecture.md)
- [docs simulations validation metrics](../simulations/validation_metrics.md)
- [docs simulations core README](../simulations/core/README.md)
- [previous folder](../)

---

## 1. Spin Field (S)

### 1.1 Definition
The Spin Field \( S(\mathbf{x}, t) \) is a vector field representing the local rotational alignment of substrate elements.



\[
S : \mathbb{R}^3 \times \mathbb{R} \rightarrow \mathbb{R}^3
\]



### 1.2 Interpretation
- Encodes rotational coupling  
- Governs angular response to external interactions  
- Determines spin‑relative motion effects  

### 1.3 Primitive Properties
- Magnitude \( |S| \) corresponds to rotational coherence  
- Direction corresponds to alignment axis  
- Spatial gradients \( \nabla S \) determine resonance thresholds  

---

## 2. Charge Field (C)

### 2.1 Definition
The Charge Field \( C(\mathbf{x}, t) \) is a scalar or vector field representing local interaction bias.



\[
C : \mathbb{R}^3 \times \mathbb{R} \rightarrow \mathbb{R} \quad \text{or} \quad \mathbb{R}^3
\]



### 2.2 Interpretation
- Encodes potential gradients  
- Determines directional bias for substrate interactions  
- Governs envelope formation  

### 2.3 Primitive Properties
- Spatial gradient \( \nabla C \) drives interaction flow  
- Temporal derivative \( \partial_t C \) indicates local bias change  
- Coupling with \( S \) produces resonance envelopes  

---

## 3. Temperature Field (T)

### 3.1 Definition
The Temperature Field \( T(\mathbf{x}, t) \) is a scalar field representing stochastic and dissipative contributions.



\[
T : \mathbb{R}^3 \times \mathbb{R} \rightarrow \mathbb{R}
\]



### 3.2 Interpretation
- Encodes thermal noise  
- Governs dissipation and decoherence  
- Modulates stability of resonance envelopes  

### 3.3 Primitive Properties
- Higher \( T \) reduces coherence  
- Spatial gradients \( \nabla T \) influence envelope boundaries  
- Coupling with \( S \) and \( C \) determines envelope lifetime  

---

## 4. SET Triad

### 4.1 Combined State
The substrate state at each point is:



\[
\Phi(\mathbf{x}, t) = \{ S(\mathbf{x}, t), C(\mathbf{x}, t), T(\mathbf{x}, t) \}
\]



### 4.2 Resonance Condition
A resonance envelope forms when:



\[
|\nabla S| + |\nabla C| - \alpha |\nabla T| > \Theta
\]



Where:
- \( \alpha \) is a dissipation coefficient  
- \( \Theta \) is a resonance threshold  

### 4.3 Evolution Equations (General Form)


\[
\partial_t S = \mathcal{O}_S(S, C, T)
\]




\[
\partial_t C = \mathcal{O}_C(S, C, T)
\]




\[
\partial_t T = \mathcal{O}_T(S, C, T)
\]



Where \( \mathcal{O}_S, \mathcal{O}_C, \mathcal{O}_T \) are substrate operators defined in the model.

---

## 5. Substrate Operators (Summary)

### 5.1 Alignment Operator


\[
\mathcal{A}(S) = f(\nabla S)
\]



### 5.2 Propagation Operator


\[
\mathcal{P}(C) = g(\nabla^2 C)
\]



### 5.3 Dissipation Operator


\[
\mathcal{D}(T) = h(\nabla^2 T)
\]



Full definitions appear in `docs/methods/operator_definitions.md`.


