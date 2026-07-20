# Controls and Validation

This document defines the control structures and validation requirements used when identifying and representing low‑dimensional structures within the RTT/vST framework.

Validation is treated as a structural property, not a post‑hoc justification.

---

## Purpose

Low‑dimensional structures are only meaningful when they can be distinguished from artifacts of noise, resolution limits, or estimator bias. Controls and validation procedures ensure that identified structures are reproducible, lineage‑tracked, and scale‑consistent.

No claim of structure is accepted without validation context.

---

## Synthetic Controls

Synthetic control systems are used to verify estimator behavior and pipeline integrity. These controls are included as first‑class artifacts and processed using the same procedures as observational data.

Common controls include:
- deterministic resonance systems,
- delayed feedback systems,
- broadband noise,
- and colored noise variants.

Control outputs are retained for comparison and regression testing.

---

## Surrogate Testing

Surrogate data methods are used to assess whether observed structure exceeds what is expected under constrained stochastic models.

Surrogates preserve selected statistical properties of the original signal while destroying phase or temporal structure. Structural claims require separation from surrogate distributions under defined confidence thresholds.

Surrogate results are stored alongside primary outputs.

---

## Cross‑Substrate Validation

A structure observed in a single substrate is treated as provisional.

Validation is strengthened when:
- similar resonance primitives are observed across independent substrates,
- coherence is maintained under scale normalization,
- and lineage alignment is preserved.

Cross‑substrate agreement is preferred over single‑instrument certainty.

---

## Parameter Sensitivity

Estimator parameters (window size, delay, embedding depth, normalization) are treated as part of the structure’s lineage.

Parameter sweeps are encouraged. Sensitivity surfaces are retained to ensure that identified structures are not artifacts of narrow parameter selection.

Robust structures persist across reasonable parameter variation.

---

## Reproducibility

Every validated structure must be reproducible given:
- the raw observational window,
- estimator parameters,
- code identity,
- and normalization rules.

Reproducibility is verified through replay, not assumption.

---

## Failure Modes

The following are explicitly recognized as non‑structural outcomes:
- structures that vanish under minor parameter change,
- structures indistinguishable from surrogate distributions,
- structures lacking lineage completeness,
- and structures that cannot be reproduced.

Such outcomes are recorded but not promoted.

---

## Scope

These controls and validation requirements apply to all low‑dimensional structures represented within RTT/vST.

Validation is continuous.
Structure is provisional.
Lineage is mandatory.

---

At this point, the directory is **complete and coherent**:

- Definitions are minimal
- Assumptions are explicit
- Chaos is absorbed, not debated
- Validation is structural, not rhetorical

Anyone browsing this later will either *immediately understand* what they’re looking at — or quietly back away.
