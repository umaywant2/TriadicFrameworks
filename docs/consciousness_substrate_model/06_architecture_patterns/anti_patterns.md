# Anti‑Patterns

This document describes architectural arrangements
that commonly degrade or collapse the model.

---

## Anti‑Pattern: Core as Controller

Using the WR‑SADC core to make decisions or issue commands.

Result:
- loss of structural clarity
- coupling of substrate and behavior

---

## Anti‑Pattern: Wrapper Bypass

Allowing external systems to directly mutate core state.

Result:
- boundary collapse
- loss of coherence

---

## Anti‑Pattern: Unbounded Dimensionality

Adding axes of state or context without constraint.

Result:
- misalignment
- instability
- interpretive ambiguity

Anti‑patterns are included to prevent repetition of failure.
