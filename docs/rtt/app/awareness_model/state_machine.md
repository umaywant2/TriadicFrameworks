# Awareness State Machine

The Awareness state machine defines how the RTT‑App transitions between clarity states based on local observations and the server‑declared global state. It provides a stable, predictable model that ensures the app behaves consistently across platforms and conditions.

---

### Overview

The state machine reduces two independent inputs—local stability and global stability—into a single Awareness state. Each state represents a distinct interpretation of environmental clarity. Transitions occur whenever either input changes classification.

The model is intentionally simple. It avoids inference, scoring, or probabilistic behavior, ensuring that the app’s indicator remains transparent and easy to reason about.

---

### States

The Awareness layer exposes four states:

- **Clear** — both local and server signals indicate stability.
- **Local Drift** — local instability with a stable global state.
- **Global Drift** — global instability with stable local conditions.
- **Drift** — both local and global signals indicate instability.

These states form the complete vocabulary of RTT‑App v1.

---

### Inputs

The state machine consumes two coarse classifications:

- **Local State**  
  - *Stable* — network and device signals within normal bounds.  
  - *Unstable* — drift detected in network or device behavior.

- **Server State**  
  - *Stable* — server‑declared clarity is high.  
  - *Unstable* — server‑declared clarity is low.

Each input is evaluated independently.

---

### Transition Rules

The state machine transitions according to the following rules:

- Local stable + Server stable → **Clear**
- Local unstable + Server stable → **Local Drift**
- Local stable + Server unstable → **Global Drift**
- Local unstable + Server unstable → **Drift**

Transitions occur immediately when either input changes classification.

---

### Transition Behavior

The state machine follows several behavioral guarantees:

- **No hysteresis** — transitions are direct and immediate.
- **No hidden states** — all possible outcomes are visible to the user.
- **No scoring** — inputs are binary (stable/unstable), not weighted.
- **No memory** — the current state depends only on current inputs.

These guarantees keep the model predictable and easy to test.

---

### Offline and Degraded Conditions

When the server state is unavailable:

- The app uses the most recently cached server value.
- If the cache is expired, the server state is treated as *Unknown*.
- *Unknown* behaves as *Stable* for the purpose of transitions.

This ensures that the app remains usable even during degraded connectivity.

---

### State Diagram (Textual)

```
           Server Stable                 Server Unstable
         +----------------+            +----------------+
Local    |                |            |                |
Stable   |     CLEAR      |----------->|  GLOBAL DRIFT  |
         |                |            |                |
         +----------------+            +----------------+
                ^   |                         ^   |
                |   |                         |   |
                |   v                         |   v
         +----------------+            +----------------+
Local    |                |            |                |
Unstable |  LOCAL DRIFT   |----------->|     DRIFT      |
         |                |            |                |
         +----------------+            +----------------+
```

This diagram expresses the full transition space for RTT‑App v1.
