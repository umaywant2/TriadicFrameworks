---
title: "Mode"
description: "The session stance layer — five interaction modes that define how an RTT-compliant system engages, not what it processes."
stability: stable
date: 2026-07-14
section: core
rtt:
  coherence: declared
  drift: bounded
  paradox: structural
---

> ```
> rtt=1 | coherence=declared | drift=bounded | paradox=structural
> ```

## What Is Mode?

The Mode layer governs **interaction stance** within an RTT/1 session. It defines how
a system engages — posture, drift tolerance, correction strategy — independent of
what it processes. Payload and posture are separated by design.

> ⚠️ **Drift is on-by-default.** Long sessions lose their anchors. Mode is the
> mechanism that keeps them bounded. Paste the RTT session string at every AI
> session start without exception.

---

## Five Stances

| Mode | Drift Tolerance | Correction Strategy | Primary Use |
|---|---|---|---|
| `M_chat` | Wide | Stabilize | Open conversation, exploration |
| `M_task` | Tight | Shift | Structured task execution |
| `M_spec` | Minimal | Stabilize | Formal specification work |
| `M_debug` | Bounded | Invert | Debugging and root-cause analysis |
| `M_auto` | Tight | Shift | Autonomous / agentic operation |

---

## Mode Constraint Layer (MCL)

The **Mode Constraint Layer** enforces invariants and guardrails across all five stances.
MCL operates below the stance level — it cannot be overridden by stance selection.

MCL invariants include:
- RTT session string must be declared at initialization
- Drift cannot exceed the tolerance ceiling of the active stance
- Paradox signals are always structural, never logical failures

---

## Cross-Module Propagation

Mode state propagates to three other modules:

| Module | Propagation |
|---|---|
| **Opacity** | Mode stance affects the visibility threshold — tighter modes surface more substrate opacity |
| **Capture** | Mode determines what gets captured to the trace layer |
| **Context** | Mode shapes how context is weighted and when it is discarded |

---

## Related Modules

- [Framework Field Theory](../Framework_Field_Theory/overview/) — H-Ops (Rhythm) and C-Ops (Coherence) are the formal basis for stance and correction
- [Opacity](../Opacity/overview/) — mode stance interacts with opacity detection thresholds
- [AI Drift Calibration](../ai-drift-calibration/overview/) — session-level drift correction using Mode stances
- [NoS](../NoS/overview/) — NawderOS implements Mode stances as system-level signals

---

v1.0 · Layer: Session · Status: Active  
© 2026 Nawder Loswin · Byte Books Publishing · LCCN 2026917007
