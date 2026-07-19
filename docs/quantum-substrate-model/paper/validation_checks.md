## Validation Checks

This section enumerates the structural validation checks for the Quantum Substrate Model (QSM). These checks define the conditions under which the model is considered structurally valid within its declared scope.

The checks are operational and declarative rather than empirical. They do not assert physical correspondence, numerical accuracy, or experimental verification.

---

### 1. Substrate Declaration Check

The model must explicitly declare the existence of a substrate layer upon which regime structure is defined.

- The substrate is treated as structurally neutral.
- No empirical or physical interpretation is embedded at this level.
- All regime behavior is defined relative to the substrate.

---

### 2. Regime Explicitness Check

All regimes defined within the model must be explicitly declared.

- Regimes are not inferred implicitly.
- Each regime has clearly stated boundaries or conditions.
- Undeclared regimes are considered out of scope.

---

### 3. Dimensional Consistency Check

Dimensional structure, if present, must be internally consistent within each declared regime.

- Dimensions are treated as structural descriptors, not physical quantities.
- Cross‑regime dimensional relationships must be explicitly stated.
- Dimensional ambiguity constitutes a validation failure.

---

### 4. Operator Mediation Check

Interactions between substrate regions or regimes must occur through explicitly defined operators.

- Operators mediate interactions rather than enforce outcomes.
- Operator behavior is constrained by regime boundaries.
- Direct, unmediated regime interaction is disallowed.

---

### 5. Regime Boundary Integrity Check

Regime boundaries must be structurally enforced.

- Interactions are valid only within declared regime boundaries.
- Boundary crossings are classified as regime transitions or exits.
- Boundary violations are non‑catastrophic and do not imply model failure.

---

### 6. Regime Transition Declaration Check

If regime transitions are permitted, their conditions must be explicitly declared.

- Transition criteria are structural rather than dynamic.
- Undefined transitions are treated as regime exit.
- Transition semantics do not propagate upward into higher‑level models.

---

### 7. Non‑Entanglement Check

The QSM must not impose semantics, objectives, or optimization criteria on higher‑level models.

- Higher‑level models remain semantically independent.
- Regime structure does not prescribe interpretation.
- Structural constraints do not imply behavioral intent.

---

### 8. Failure Semantics Check

Failure conditions must be framed as regime exit rather than error.

- Regime exit does not invalidate the substrate.
- No corrective enforcement is applied at the substrate level.
- Failure semantics are descriptive, not prescriptive.

---

### 9. Scope Compliance Check

The model must remain within its declared scope.

- No empirical claims are introduced.
- No physical realism is asserted.
- No simulation or numerical assumptions are embedded.

---

## Validation Summary

A Quantum Substrate Model instance is considered structurally valid if all checks above are satisfied within the declared operating scope. These checks are intended to support clarity, interpretability, and reproducibility without enforcing implementation‑specific behavior or empirical correspondence.
