# Triadic Decomposition of Atomic Clock Systems

This document defines the minimal triadic structure shared by all atomic
clock architectures. The decomposition isolates the functional roles
within any timekeeping system and provides a substrate‑agnostic model
for analysis, comparison, and drift detection.

## 1. Resonant System (R)

The resonant system provides the stable physical transition whose cycles
define the clock’s fundamental timescale.

Examples:
- hyperfine transitions (cesium, rubidium)
- optical transitions (strontium, ytterbium)
- ion‑trap transitions
- hydrogen maser resonance

Role:
- supplies the invariant frequency anchor
- determines the ultimate stability limit
- encodes the resonance cycles that accumulate as time

## 2. Interrogation System (I)

The interrogation system probes the resonant system and extracts
measurable information about its phase or frequency.

Examples:
- Ramsey interrogation sequences
- laser stabilization and optical cavities
- frequency combs
- detection electronics

Role:
- converts resonance into measurable signals
- maintains coherence during interrogation
- couples the resonant system to the feedback loop

## 3. Feedback System (F)

The feedback system stabilizes the clock output by correcting deviations
detected during interrogation.

Examples:
- phase‑locked loops
- servo controllers
- drift compensation algorithms
- frequency steering mechanisms

Role:
- maintains alignment between measured and target frequency
- suppresses environmental and instrumental drift
- produces the final clock signal

## Triadic Form

Clock = (R, I, F)

This triadic form is architecture‑independent and applies equally to
microwave, optical, ion‑trap, and maser clocks. It provides the minimal
structural substrate for resonance‑based analysis and supports the
invariants used in vST drift detection.
