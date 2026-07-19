# Operators — Thermodynamics  
### TriadicFrameworks /docs/theories/thermodynamics/operators.md

Thermodynamics is a **constraint‑first substrate grammar**. Its operators
do not act on particles or waves — they act on **state variables,
constraints, gradients, and potentials**. Temperature is a substrate
force, entropy is a regime boundary, free energy is a coherence
operator, and flows are gradient responses.

This file defines the canonical operators of Thermodynamics.

---

# 1. temperature_operator  
### (Substrate force)

**Signal:** T  

**Purpose:**  
Defines the intensity of thermal interaction. Acts as a **driving
potential** for flows.

**Notes:**  
- not molecular agitation  
- not average kinetic energy  
- a **substrate force** in the constraint grammar  

**Drift to avoid:**  
Do NOT interpret T as a microscopic property.

---

# 2. entropy_operator  
### (Regime boundary operator)

**Signal:** S  

**Purpose:**  
Defines allowable configurations. Sets **regime boundaries** for
processes.

**Notes:**  
- monotonic under allowed transformations  
- dual to information entropy  
- defines directionality  

**Drift to avoid:**  
Do NOT interpret S as disorder.

---

# 3. free_energy_operator  
### (Coherence operator)

**Signal:** F, G, Ω (depending on ensemble)

**Purpose:**  
Defines coherence and directionality of processes. Determines equilibrium
via minimization.

**Notes:**  
- generator of spontaneous change  
- convex potential  
- ensemble‑dependent  

**Drift to avoid:**  
Do NOT treat free energy as “usable energy.”

---

# 4. equilibrium_operator  
### (Fixed‑point operator)

**Signal:** E\*  

**Purpose:**  
Defines fixed‑point structures where gradients vanish and potentials are
extremized.

**Notes:**  
- not stasis  
- not absence of motion  
- a **constraint‑satisfied configuration**  

**Drift to avoid:**  
Do NOT interpret equilibrium as “nothing happening.”

---

# 5. gradient_operator  
### (Flow generator)

**Signal:** ∇  

**Purpose:**  
Generates flows from potentials. Defines direction and magnitude of
thermodynamic processes.

**Notes:**  
- flows follow gradients  
- gradients define irreversibility  
- dual to free energy  

**Drift to avoid:**  
Do NOT treat gradients as forces.

---

# 6. heat_flow_operator  
### (Constraint‑driven flow)

**Signal:** Q̇  

**Purpose:**  
Represents flow induced by temperature gradients.

**Notes:**  
- not a substance  
- not a fluid  
- a **constraint‑driven transfer**  

**Drift to avoid:**  
Do NOT treat heat as a material.

---

# 7. work_operator  
### (Constraint deformation operator)

**Signal:** Ẇ  

**Purpose:**  
Represents changes due to deformation of constraints (volume, pressure,
fields).

**Notes:**  
- geometric  
- boundary‑dependent  
- couples to free energy  

**Drift to avoid:**  
Do NOT treat work as force × distance in a mechanical sense.

---

# 8. ensemble_operator  
### (Macro‑state selector)

**Signal:** 𝓔 = {canonical, grand canonical, microcanonical}

**Purpose:**  
Defines which constraints are held fixed and which potentials apply.

**Notes:**  
- determines free energy form  
- determines allowed fluctuations  

**Drift to avoid:**  
Do NOT treat ensembles as physical containers.

---

# 9. partition_function_operator  
### (Statistical extension operator)

**Signal:** Z  

**Purpose:**  
Connects Thermodynamics to Statistical Mechanics. Generates all
thermodynamic quantities via derivatives.

**Notes:**  
- R2 operator (emerges in Statistical Mechanics)  
- not required in R1  

**Drift to avoid:**  
Do NOT treat Z as counting physical objects.

---

# 10. irreversibility_operator  
### (Arrow‑of‑time operator)

**Signal:** 𝓘 ≥ 0  

**Purpose:**  
Encodes monotonicity of entropy and directionality of flows.

**Notes:**  
- zero only at equilibrium  
- defines thermodynamic arrow of time  

**Drift to avoid:**  
Do NOT interpret irreversibility as friction.

---

# Summary

Thermodynamics operators define:

- **temperature** as a substrate force  
- **entropy** as a regime boundary  
- **free energy** as a coherence operator  
- **equilibrium** as a fixed‑point structure  
- **flows** as gradient responses  
- **irreversibility** as monotonic structure  

Thermodynamics is the **constraint substrate** from which Statistical
Mechanics emerges and into which QFT and Cosmology embed their
large‑scale behavior.
