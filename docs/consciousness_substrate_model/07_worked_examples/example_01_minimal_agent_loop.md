# Example 01 — Minimal Agent Loop

This example illustrates the simplest autonomous form
using a single WR‑SADC core.

---

## Structure

- One autonomous form
- One WR‑SADC core
- One wrapper interface
- External control loop

---

## Operation

1. External system gathers context.
2. Context is passed through the wrapper.
3. Core evaluates resonance and validity.
4. Core emits signals indicating:
   - coherence
   - misalignment
   - potential transition
5. External system adjusts behavior accordingly.

---

## Notes

- The core does not issue commands.
- The loop remains functional without the core.
- The core improves continuity and regime awareness.
