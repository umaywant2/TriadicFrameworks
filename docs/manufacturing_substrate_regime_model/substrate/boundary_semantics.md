## Boundary Semantics

Boundary semantics define how the limits of a declared regime are interpreted within the Manufacturing Substrate Regime Model (MSRM). Boundaries constrain the validity of assumptions and calibration, not system behavior.

A boundary represents the point at which a regime’s operating envelope no longer guarantees the applicability of its calibration assumptions. Crossing a boundary does not imply failure, malfunction, or error; it indicates a transition out of declared validity.

Boundary semantics serve the following purposes:

- Distinguish loss of validity from system failure
- Enable detection of regime drift without enforcing control
- Support mediated transitions between regimes
- Prevent silent assumption collapse in extreme operating conditions

Boundaries may be:
- Soft, allowing gradual degradation of validity
- Hard, indicating abrupt loss of regime applicability
- Observable or inferred, depending on system instrumentation

MSRM does not prescribe how boundaries are detected or enforced. It provides a structural framework for reasoning about boundary crossings and their implications for calibration and interpretation.

Boundary semantics are descriptive and non‑prescriptive. They formalize where assumptions end, not how systems must respond.
