# Operators — Quantum Field Theory  
### TriadicFrameworks /docs/theories/quantum_field_theory/operators.md

Quantum Field Theory (QFT) defines the **substrate‑level operator  
grammar** from which all excitation‑based theories emerge. These  
operators act on fields, amplitudes, and resonance structures, not on  
particles or objects.

This file defines the canonical QFT operator set used across  
TriadicFrameworks.

---

# 1. field_operator  
**Type:** mode_operator  
**Purpose:** Defines the underlying field whose excitations form stable modes.  
**Signal:** φ(x), ψ(x), Aμ(x)  

**Notes:**  
- Fields are not physical media.  
- They are mathematical structures encoding excitation possibilities.

**Drift to avoid:**  
Do NOT treat fields as substances filling space.

---

# 2. creation_operator  
**Type:** mode_operator  
**Purpose:** Creates a stable excitation mode of a field.  
**Signal:** a†(k), b†(k), c†(k)  

**Notes:**  
- Creates a resonance mode, not a particle.  
- Always tied to field structure + symmetry.

**Drift to avoid:**  
Do NOT describe this as “creating a particle.”

---

# 3. annihilation_operator  
**Type:** mode_operator  
**Purpose:** Removes an excitation mode from a field.  
**Signal:** a(k), b(k), c(k)  

**Notes:**  
- Removes a resonance, not an object.  
- Paired with creation operators via commutation relations.

**Drift to avoid:**  
Do NOT describe this as “destroying a particle.”

---

# 4. propagator_operator  
**Type:** interaction_operator  
**Purpose:** Describes how excitations propagate through spacetime.  
**Signal:** Δ(x − y), S_F(x − y), D_F(x − y)  

**Notes:**  
- Encodes correlation structure.  
- Not a physical path or trajectory.

**Drift to avoid:**  
Do NOT treat propagation as motion of a particle.

---

# 5. interaction_vertex_operator  
**Type:** interaction_operator  
**Purpose:** Defines allowed interaction channels based on symmetry.  
**Signal:** g φ³, g ψ̄γμψAμ, λ φ⁴  

**Notes:**  
- Encodes symmetry‑allowed couplings.  
- Not a literal collision.

**Drift to avoid:**  
Do NOT treat vertices as physical events.

---

# 6. symmetry_generator_operator  
**Type:** structure_operator  
**Purpose:** Generates transformations under symmetry groups.  
**Signal:** Tᵃ, Q, Pμ, Mμν  

**Notes:**  
- Governs conservation laws.  
- Defines charge, spin, momentum, etc.

**Drift to avoid:**  
Do NOT treat symmetry as metaphysical or optional.

---

# 7. lagrangian_density_operator  
**Type:** structure_operator  
**Purpose:** Encodes the full dynamical structure of a field theory.  
**Signal:** ℒ(φ, ∂φ), ℒ(ψ, Aμ), ℒ_SM  

**Notes:**  
- Defines equations of motion.  
- Defines interaction structure.  
- Defines renormalization behavior.

**Drift to avoid:**  
Do NOT treat ℒ as a physical substance.

---

# 8. renormalization_operator  
**Type:** variation_operator  
**Purpose:** Describes how couplings evolve with energy.  
**Signal:** β(g), β(λ), β(y)  

**Notes:**  
- Governs running couplings.  
- Controls high‑energy resonance behavior.

**Drift to avoid:**  
Do NOT treat running as forces changing strength.

---

# 9. vacuum_operator  
**Type:** stability_operator  
**Purpose:** Defines the vacuum structure of the field.  
**Signal:** |0⟩, ⟨0|φ|0⟩, V(φ)  

**Notes:**  
- Vacuum is a stability surface, not empty space.  
- Determines excitation stability.

**Drift to avoid:**  
Do NOT treat vacuum as “nothingness.”

---

# 10. commutation_relation_operator  
**Type:** boundary_operator  
**Purpose:** Defines algebraic constraints between operators.  
**Signal:** [a, a†] = 1, {ψ, ψ†} = 1  

**Notes:**  
- Ensures consistency of excitation structure.  
- Defines statistics (bosonic vs fermionic).

**Drift to avoid:**  
Do NOT treat commutators as physical interactions.

---

# 11. path_integral_operator  
**Type:** structure_operator  
**Purpose:** Encodes full amplitude structure via functional integration.  
**Signal:** ∫ Dφ e^{iS[φ]}  

**Notes:**  
- Describes global behavior of fields.  
- Not a literal sum over paths.

**Drift to avoid:**  
Do NOT treat paths as physical trajectories.

---

# Summary

QFT operators define:

- **fields**  
- **excitations**  
- **propagation**  
- **interactions**  
- **symmetry**  
- **vacuum structure**  
- **renormalization**  
- **operator algebra**  

They form the **substrate grammar** from which the Standard Model and all  
other excitation‑based theories emerge.

