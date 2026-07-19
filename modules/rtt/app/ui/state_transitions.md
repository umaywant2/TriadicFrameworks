# State Transitions

State transitions define how the Awareness indicator changes when the merged Awareness state moves between Clear, Local Drift, Global Drift, and Drift. Transitions are designed to be smooth, unobtrusive, and easy to interpret without drawing attention or implying urgency. The goal is to maintain a sense of ambient clarity while avoiding rapid or distracting changes.

---

### Transition Principles

The transition model follows several principles that keep the UI stable and predictable:

- **Smoothness** — all transitions use gradual changes in color, opacity, or motion.
- **No flashing** — the indicator never blinks or pulses rapidly.
- **No intermediate states** — transitions move directly from one state to another.
- **No oscillation** — the indicator does not flicker between states due to transient signals.
- **Consistency** — transitions behave the same on iOS and Android.

These principles ensure that the indicator remains ambient rather than attention‑seeking.

---

### Transition Types

Each Awareness state has a distinct visual expression, and transitions modify only the properties that differ between states:

- **Color transitions** — gradual shifts between clarity and drift palettes.
- **Opacity transitions** — subtle changes to reflect confidence or global instability.
- **Motion transitions** — gentle introduction or removal of shimmer or drift motion.
- **Timing transitions** — consistent durations to maintain a calm visual rhythm.

Transitions never alter the indicator’s shape or layout.

---

### State‑to‑State Behavior

The transitions between states follow a predictable pattern:

- **Clear → Local Drift**  
  Introduces warm color shift and subtle motion over a short, smooth interval.

- **Clear → Global Drift**  
  Introduces cooler color shift and slight opacity reduction.

- **Clear → Drift**  
  Combines both color shift and motion, applied gradually.

- **Local Drift → Clear**  
  Removes motion first, then restores clarity color.

- **Global Drift → Clear**  
  Restores opacity and clarity color simultaneously.

- **Local Drift → Global Drift**  
  Motion fades out while color shifts toward the global palette.

- **Global Drift → Local Drift**  
  Motion fades in while color shifts toward the local palette.

- **Any state → Drift**  
  Adds both motion and color shift in a controlled, slow transition.

- **Drift → Any state**  
  Removes motion first, then adjusts color and opacity.

These transitions ensure that the indicator never feels abrupt or unstable.

---

### Timing and Duration

Transitions use consistent timing across all states:

- **Short transitions** for color and opacity changes.  
- **Medium transitions** for motion introduction or removal.  
- **No instantaneous changes**, even when signals update rapidly.

This timing model reinforces the app’s ambient, non‑urgent posture.

---

### Handling Rapid Input Changes

If local or server signals fluctuate quickly:

- The indicator completes the current transition before starting a new one.
- The state machine updates immediately, but the UI transitions remain smooth.
- The indicator never flickers or jumps between states.

This behavior preserves visual stability even when underlying signals are noisy.

---

### Accessibility Considerations

Transitions are designed to remain comfortable for all users:

- Motion is subtle and slow to avoid discomfort.
- Color changes maintain sufficient contrast.
- Screen readers announce state changes using simple labels without describing animations.

These considerations ensure that the indicator remains inclusive and predictable.
