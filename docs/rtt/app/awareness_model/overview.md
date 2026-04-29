## RTT Awareness Overview

RTT Awareness provides a lightweight, permissionless layer that helps the RTT‑App sense and express environmental clarity. It does not inspect the system, modify device settings, or rely on privileged APIs. Instead, it combines two stable signal sources:

- **Local signals** derived from network behavior and device stability.
- **Server‑declared signals** published by the RTT ecosystem.

The merge of these two sources produces a single Awareness state that reflects how stable, clear, or drift‑prone the user’s environment currently feels.

---

### Purpose of the Awareness Layer

The Awareness layer gives the user a simple, ambient indicator of clarity without requiring sensors, permissions, or background services. It acts as the app’s “first sense,” offering:

- A quick read on environmental stability.
- A consistent interpretation across devices.
- A bridge between the RTT‑App and the broader RTT ecosystem.

Awareness is not diagnostic and does not attempt to infer intent or behavior. It is a structural signal, not a personal one.

---

### What Awareness Measures

Awareness focuses on conditions that can be observed without permissions:

- **Network clarity** such as DNS variance, handshake stability, and protocol fallback.
- **Device stability** such as UI thread jitter or memory pressure.
- **Global regime state** declared by the RTT server.

These signals are coarse but reliable. They allow the app to express clarity and drift in a way that is meaningful, consistent, and safe.

---

### Awareness States

The Awareness layer reduces all inputs into a small set of states:

- **Clear** — local signals stable, server state stable.
- **Local Drift** — local instability with a stable global state.
- **Global Drift** — global instability with a stable local state.
- **Drift** — both local and global signals unstable.

These states form the foundation for the app’s indicator UI and for any future features that depend on environmental clarity.

---

### Design Principles

The Awareness model follows several principles:

- **Permissionless** — no access to sensors, radios, or system settings.
- **Predictable** — stable behavior across platforms and devices.
- **Composable** — local and server signals can evolve independently.
- **Minimal** — no complex inference or opaque scoring.
- **Transparent** — the user can understand the meaning of each state.

These principles ensure that Awareness remains safe, lightweight, and aligned with the RTT philosophy.
