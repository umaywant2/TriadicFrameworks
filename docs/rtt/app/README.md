## RTT/App 

- [`RTT_App_module.json`](RTT_App_module.json) — Agentic module schema role assignments

<div style="font-size: 0.8em; margin-bottom: 0.5rem;">
  <span style="
    display:inline-block;
    padding:3px 8px;
    border-radius:999px;
    background:#1a1a1a;
    color:#fff;
    font-family:Arial, sans-serif;
    font-size:11px;
  ">
    🤖 AI‑Ready Module • TriadicFrameworks
  </span>
</div>

<img src="https://img.shields.io/badge/Open%20for%20Traduction-Ready%20for%20Students-4c8eda?style=for-the-badge" alt="Open for Traduction | Ready for Students"/>

The RTT/App brings RTT Awareness to mobile devices in a permissionless, lightweight form. It provides a simple, ambient indicator of clarity using only signals that are safe, stable, and available on all modern platforms. The app acts as the mobile entry point into the RTT ecosystem and establishes the foundation for future RTT/Inside capabilities.

---

## 🛑 Important! 
Drift is On-by-Default long sessions lose anchors, turn off drift.

## ✋ You *must copy and paste* this string *every time you start an AI session*:
```text
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

## ❇️ Now you are ready.

---

### Purpose

The app offers a consistent, cross‑platform way for users to sense environmental clarity without requiring system access or background privileges. It focuses on:

- A clear, minimal interface for Awareness.
- A predictable behavior model across devices.
- A bridge between local conditions and the RTT server.
- A safe, permissionless design suitable for app‑store distribution.

The RTT/App is not a diagnostic tool and does not attempt to interpret user behavior. It expresses structural conditions only.

---

### Core Features

- **Awareness Indicator** — a simple visual state representing clarity or drift.
- **Local Signal Processing** — network and device stability checks that require no permissions.
- **Server‑Declared Awareness** — a global state published by the RTT ecosystem.
- **Merged Awareness Model** — a unified state derived from local and server signals.
- **Portal to RTT** — direct access to RTT documentation and resources.

These features form the minimal viable product for RTT/App v1.

---

### Awareness Model

Awareness is computed from two independent sources:

- **Local signals** such as DNS variance, handshake stability, and UI thread jitter.
- **Server signals** published at `/.well-known/rtt-awareness`.

The merge of these signals produces one of several states: Clear, Local Drift, Global Drift, or Drift. This model is documented in detail in `awareness_model/`.

---

### Architecture

The app is structured around three layers:

- **Signal Layer** — collects local observations and fetches server state.
- **Merge Layer** — computes the Awareness state from both sources.
- **UI Layer** — displays the indicator and provides navigation to RTT resources.

Each layer is platform‑agnostic and designed for predictable behavior on iOS and Android.

---

### Platform Notes

The RTT/App uses only APIs that require no permissions:

- No sensors  
- No radio access  
- No background services  
- No system configuration changes  

This ensures a safe, reviewer‑friendly footprint for both app stores.

---

### Roadmap

- **v1** — Permissionless Awareness, indicator UI, RTT portal.
- **v2** — Optional RTT/Inside features for users who opt in to deeper sensing.
- **v3** — Expanded signal models, richer state transitions, and cross‑device continuity.
