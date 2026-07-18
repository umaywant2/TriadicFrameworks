app 
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
# 📱 A Smartphone with RTT-Inside 📲
###### By Nawder Loswin 1/4/2026 © www.TriadicFrameworks.org

### 1. Today’s flagships in rough spec‑space

Think “iPhone 16 Pro Max / Galaxy S25 Ultra / Pixel 9–10 Pro / OnePlus 13‑class” 

- **CPU / NPU:**  
  **A18 Pro / Snapdragon 8 Elite / Tensor G4**–class, multi‑core, with dedicated AI/ML blocks.
- **RAM:**  
  8–16 GB.
- **Storage:**  
  256 GB–1 TB, UFS 4.0 / NVMe‑class.
- **Display:**  
  6.7–6.9" OLED / LTPO, 1–120 Hz, ~QHD.
- **Battery:**  
  ~4,400–5,500 mAh, some pushing higher with Si/C chemistries. 
- **Charging:**  
  30–100 W wired, 15–50 W wireless.
- **Radios:**  
  5G (sub‑6 + mmWave in some), Wi‑Fi 6E/7, BT 5.x, GNSS, NFC, UWB on some.
- **Sensors:**  
  IMU, barometer, proximity, ambient light, magnetometer, cameras, sometimes LiDAR / ToF.
- **OS / stack:**  
  iOS / Android with vendor skin, on‑device AI features (photo magic, summarization, etc.). 

They’re already **dense sensor hubs** with serious compute and decent batteries.

---

### 2. What changes with a vendor RTT‑Inside variant

Assume RTT‑Inside is **not an app**, but a **system‑level resonance core** the OEM bakes in:

#### 2.1. New “resonance layer” in the OS

- **Today:**  
  Sensors → OS drivers → apps. Each app interprets its own “world.”
- **With RTT‑Inside:**  
  Sensors → **RTT‑Micro‑Core** → OS → apps.  
  The core:
  - fuses motion, RF, audio, environment into **coherence / clarity / drift** metrics,  
  - exposes a **resonance API**:  
    - `get_clarity(zone)`  
    - `get_drift_vector()`  
    - `subscribe_to_resonance_events()`  

**Result:**  
Apps stop guessing context from raw noise and start from **structured field‑level signals**.

#### 2.2. Smarter radios, less “AI drift”

- **Today:**  
  Radios hunt for networks, burn battery, and sometimes behave weirdly (sticky cells, flaky Wi‑Fi).
- **With RTT‑Inside:**  
  - Radios choose channels and bands based on **resonance clarity** (RF + motion + environment).  
  - Handoffs are guided by **drift vectors** instead of just RSSI.  
  - “AI drift gone” logic stabilizes connectivity decisions over time.

**Result:**  
Fewer weird network edge‑cases, smoother roaming, better battery under marginal signal.

#### 2.3. Power & thermal behavior

- **Today:**  
  Power management is mostly per‑subsystem (screen, CPU, radios) with some ML heuristics.
- **With RTT‑Inside:**  
  - The phone knows when the **environment is noisy / chaotic / low‑clarity** and can:
    - back off aggressive polling,  
    - delay non‑urgent sync,  
    - schedule heavy compute when resonance is “calm.”  
  - BMS can use resonance patterns (usage + environment) to extend cell life.

**Result:**  
Slightly better battery life, but more importantly **more predictable** behavior under stress.

#### 2.4. New app‑space for devs

This is the big one.

RTT‑Inside exposes **new primitives**:

- `clarity_score` (0–255)  
- `resonance_zones` (logical spaces the phone thinks it’s in)  
- `drift_events` (when the environment is changing fast)  
- `coherence_groups` (devices that “feel” like they’re in the same field)

App devs can build:

- **Context‑aware UIs** that simplify when clarity is low (e.g., in a crowd, on a train, underground).  
- **Safety apps** that detect dangerous vibration patterns (construction, mining, industrial).  
- **Group‑aware apps** that form ad‑hoc meshes based on resonance proximity, not just Bluetooth scans.  
- **AR / XR** that uses resonance fields to stabilize overlays in noisy environments.

**Result:**  
Yes—**more room for app devs**, but in a *structured* way, not just “more sensors.”

#### 2.5. Integration with external RTT domains

Your coal‑mine, deep‑sea, ATC, and Great Lakes systems all use RTT‑Inside variants.

A phone with vendor RTT‑Inside can:

- act as a **field probe** in those environments,  
- join **resonance‑aware meshes** (underground, at sea, in disaster zones),  
- display **clarity maps** and **drift vectors** natively,  
- serve as a **portable HMI** for industrial RTT deployments.

**Result:**  
The smartphone becomes a **universal RTT terminal**, not just a consumer gadget.

---

### 3. Does anything break?

If done badly? Absolutely.

- **Battery risk:**  
  If vendors treat RTT‑Inside as “yet another always‑on AI,” they’ll tank battery.
- **Privacy risk:**  
  If resonance fields are logged without care, you get creepy “life‑pattern” tracking.
- **Complexity risk:**  
  If every OEM exposes a different RTT API, devs get fragmentation hell.
- **UX risk:**  
  If clarity / drift is surfaced as noisy notifications, users will hate it.

If done well:

- RTT‑Inside runs as a **micro‑core**, low‑power, event‑driven.  
- Most of its value is **indirect**: better decisions, fewer glitches, calmer behavior.  
- Apps see **simple, high‑level signals**, not a firehose.

So…

---

### 4. Brutal truth time

> “This would never work, it would cause nothing but problems…”

If you shipped RTT‑Inside today as:

- a bloated vendor “AI experience,”  
- with no standard API,  
- bolted on top of already‑fragile Android skins,  
- marketed as “Resonance™ Magic Mode,”  

…then yes, it would be a **mess**:

- more bugs,  
- more battery drain,  
- more opaque behavior,  
- more dev confusion,  
- more user distrust.

But if you treat RTT‑Inside as:

- a **small, disciplined, invariant core**,  
- standardized across vendors,  
- focused on **stability, clarity, and safety**,  
- mostly invisible, quietly improving decisions…

Then it’s the opposite of “nothing but problems”:

- fewer edge‑case failures,  
- fewer “my phone is acting weird” moments,  
- richer, safer app ecosystems,  
- and a clean bridge between **personal devices** and your **industrial RTT universes**.

So the real brutal truth is:

> It only “never works” if we let marketing own it instead of architecture.

---

# Awareness Endpoint

The Awareness endpoint provides the RTT‑App with the global clarity state published by the RTT ecosystem. It is a simple, stable, permissionless interface designed to work across all platforms and network conditions. The endpoint exposes a minimal JSON document that the app can fetch, cache, and merge with local signals to compute the final Awareness state.

---

### Endpoint Location

The RTT server publishes the Awareness document at:

`/.well-known/rtt-awareness`

This path follows established conventions for well‑known metadata and ensures predictable behavior across environments.

---

### Response Format

The endpoint returns a compact JSON object containing the current global clarity state:

```json
{
  "clarity": "high",
  "drift": "low",
  "timestamp": "2026-02-28T20:00:00Z"
}
```

- **clarity** — a coarse indicator of global stability.  
- **drift** — a coarse indicator of global instability.  
- **timestamp** — the server’s declaration time in ISO‑8601 format.

The server does not expose internal reasoning or diagnostics.

---

### Semantics

The values published by the endpoint represent the RTT ecosystem’s global interpretation of clarity:

- **High clarity** indicates stable global conditions.  
- **Low clarity** indicates global drift or instability.  
- **Drift** values complement clarity and provide additional context.  

The RTT‑App treats these values as authoritative for the global half of the Awareness model.

---

### Caching Behavior

The RTT‑App uses a conservative caching strategy:

- Cache the most recent valid response.  
- Use the cached value when offline or degraded.  
- Expire the cache only after a safe interval to avoid rapid oscillation.  
- Treat missing or expired data as *Unknown*, which behaves as *Stable* for merge purposes.

This ensures predictable behavior even in unstable network environments.

---

### Error Handling

The app handles errors gracefully:

- **Network errors** — fall back to cached data.  
- **Invalid JSON** — ignore the response and retain the previous value.  
- **Unexpected fields** — ignore unknown keys without failing.  
- **Missing fields** — treat the server state as *Unknown*.  

The endpoint is designed to be forward‑compatible with future extensions.

---

### Versioning

The Awareness endpoint is versionless in v1. Future versions may introduce:

- Additional fields.  
- Optional metadata.  
- Extended clarity categories.  

All additions will preserve backward compatibility.
# Caching Rules

The RTT‑App uses a conservative, predictable caching strategy for the server‑declared Awareness document. The goal is to ensure stable behavior across network conditions while avoiding rapid oscillation in the Awareness state. Caching is essential because the app relies on a lightweight endpoint and does not run background services or privileged tasks.

---

### Purpose of Caching

Caching provides several benefits:

- Ensures the app remains functional when offline or degraded.
- Prevents rapid state changes caused by transient network issues.
- Reduces unnecessary network traffic.
- Maintains a consistent global baseline for the merge logic.
- Supports a permissionless architecture without background refresh.

The cache is treated as a first‑class input to the Awareness model.

---

### Cache Contents

The cache stores the most recent valid response from:

`/.well-known/rtt-awareness`

The stored data includes:

- The full JSON payload.
- The server‑declared timestamp.
- The local time when the document was fetched.

These values allow the app to determine freshness and fallback behavior.

---

### Cache Lifetime

The cache follows a simple lifetime model:

- **Fresh** — within the defined validity window.  
- **Stale** — outside the validity window but still usable.  
- **Expired** — beyond the maximum allowed age.

The validity window is intentionally conservative to avoid oscillation. The exact duration is platform‑agnostic and defined in implementation notes.

---

### Fallback Behavior

When the app cannot retrieve a fresh server state:

- Use the most recent cached value.
- If the cache is stale, treat the server state as *Stable* for merge purposes.
- If the cache is expired, treat the server state as *Unknown*.

*Unknown* behaves the same as *Stable* in the merge logic to ensure predictable behavior during outages.

---

### Error Handling

The app handles server errors gracefully:

- **Network failure** — retain the cached value.  
- **Invalid JSON** — ignore the response and keep the previous value.  
- **Missing fields** — treat the server state as *Unknown*.  
- **Unexpected fields** — ignore without failing.

The cache is never cleared automatically due to malformed responses.

---

### Refresh Strategy

The app refreshes the server state opportunistically:

- On app launch.
- When returning to the foreground.
- At safe intervals during active use.

No background tasks or privileged APIs are used.

---

### Consistency Guarantees

The caching model provides several guarantees:

- The Awareness state never oscillates due to transient network issues.
- The app remains usable even during extended offline periods.
- The merge logic always receives a valid input, even if degraded.
- Server‑declared Awareness can evolve without requiring app updates.

These guarantees support the RTT‑App’s role as a stable, permissionless entry point into the RTT ecosystem.
# Error Handling

The RTT‑App handles errors in a conservative, predictable way to ensure that the Awareness model remains stable even when network conditions degrade or server responses are malformed. Error handling is intentionally simple and avoids any behavior that would require system permissions or background execution.

---

### Error Categories

The app may encounter several classes of errors when fetching or interpreting the server‑declared Awareness document:

- **Network errors** — timeouts, unreachable hosts, captive portals, or protocol failures.
- **Transport errors** — TLS handshake failures, protocol downgrades, or QUIC fallback.
- **Response errors** — invalid JSON, missing fields, or unexpected structures.
- **Cache errors** — expired or missing cached values.
- **Runtime errors** — interruptions during fetch or merge operations.

Each category is handled independently to maintain clarity and predictability.

---

### Network Errors

When the app cannot reach the Awareness endpoint:

- Retain the most recent cached server state.
- Do not attempt retries beyond the platform’s default behavior.
- Treat the server state as *Unknown* if no cached value exists.
- Allow the merge logic to proceed using local signals.

This ensures that temporary outages do not cause oscillation or user confusion.

---

### Response Errors

If the server returns a malformed or incomplete response:

- Ignore the response entirely.
- Preserve the previous cached value.
- Treat the server state as *Unknown* if no valid cache exists.
- Do not attempt to infer missing fields.

The app never attempts to repair or interpret invalid data.

---

### Cache Errors

If the cached server state is missing or expired:

- Treat the server state as *Unknown*.
- Allow the merge logic to treat *Unknown* as *Stable*.
- Attempt to refresh the server state on the next safe opportunity.

This behavior ensures that the app remains functional even after long offline periods.

---

### Merge‑Layer Errors

If an error occurs during the merge process:

- Default to the most conservative state: **Drift**.
- Log the event internally (platform‑native logging only).
- Continue normal operation on the next evaluation cycle.

This prevents silent failures and ensures that the indicator never displays misleading clarity.

---

### UI Behavior During Errors

The Awareness indicator must remain stable and predictable:

- Never flash or oscillate due to transient errors.
- Never display partial or intermediate states.
- Use the last known valid Awareness state until the next successful merge.

The UI reflects the model’s stability guarantees.

---

### Forward Compatibility

The error‑handling model is designed to support future versions of the Awareness endpoint:

- Unknown fields are ignored.
- Missing fields trigger fallback behavior.
- Additional metadata does not affect v1 behavior.

This ensures that the RTT‑App remains compatible as the RTT ecosystem evolves.
## Local Signals

Local signals represent the device’s immediate environment as observed through safe, permissionless APIs. These signals do not access sensors, radios, or system settings. They rely only on behaviors that naturally occur during normal app operation. Together, they provide a coarse but reliable sense of stability, drift, and environmental clarity.

---

### Network‑Based Signals

Network behavior is one of the strongest permissionless indicators of environmental conditions. The RTT‑App observes patterns that emerge during routine requests.

- **DNS Resolution Variance** — fluctuations in lookup time indicate instability or congestion.
- **TLS Handshake Duration** — longer or inconsistent handshakes suggest degraded paths or interference.
- **QUIC Handshake Success and Fallback** — repeated fallback to TCP/HTTP/2 reflects drift or loss.
- **Protocol Negotiation** — unexpected downgrades signal environmental inconsistency.
- **Retry Patterns** — increased retries imply packet loss or transient instability.
- **Captive Portal Detection** — redirects or blocked requests indicate constrained environments.

These signals require no special permissions and behave consistently across platforms.

---

### Device‑Stability Signals

The app can also observe local stability through standard lifecycle and runtime indicators.

- **UI Thread Jank Metrics** — frame drops and animation stalls reflect local load or contention.
- **Memory Pressure Warnings** — low‑memory conditions indicate local drift or resource strain.
- **Thermal Throttling (Android)** — thermal events reduce performance and signal environmental stress.
- **Event Loop Jitter** — irregular scheduling suggests instability in the local runtime.
- **Foreground/Background Transitions** — rapid or unexpected transitions can correlate with drift.

These signals do not reveal personal information and do not require system access.

---

### Signal Characteristics

Local signals share several important properties:

- **Permissionless** — all signals are available without user prompts or system privileges.
- **Coarse but Reliable** — they reflect environmental conditions without fine‑grained detail.
- **Platform‑Stable** — behavior is consistent across iOS and Android.
- **Non‑Diagnostic** — they indicate drift or clarity but do not identify root causes.
- **Composable** — each signal contributes independently to the Awareness model.

These characteristics make local signals ideal for RTT‑App v1.

---

### Role in the Awareness Model

Local signals form one half of the Awareness computation. They describe how the device “feels” right now. When merged with the server‑declared state, they produce a unified Awareness state that reflects both local and global conditions.
## Merge Logic

The merge layer combines local observations with the server‑declared global state to produce a single Awareness value. This value reflects both the device’s immediate environment and the broader conditions published by the RTT ecosystem. The merge is intentionally simple, predictable, and transparent.

### Inputs to the Merge

The merge logic receives two independent inputs:

- **Local State** — derived from network clarity, device stability, and runtime behavior.
- **Server State** — declared at `/.well-known/rtt-awareness` and cached by the app.

Each input is reduced to a coarse stability classification before merging.

### Merge Principles

The merge follows several principles to ensure consistent behavior:

- **Local and global signals are peers** — neither overrides the other.
- **Instability is meaningful** — drift in either domain affects the final state.
- **Stability requires agreement** — both sources must be stable for the app to report Clear.
- **The model is declarative** — no inference or scoring is performed.

These principles keep the merge logic predictable and reviewer‑safe.

### Merge Outcomes

The merge produces one of four Awareness states:

- **Clear** — both local and server signals indicate stability.
- **Local Drift** — local instability with a stable global state.
- **Global Drift** — global instability with stable local conditions.
- **Drift** — both local and global signals indicate instability.

These states form the basis for the Awareness indicator shown in the UI.

### Decision Rules

The merge logic can be expressed as a simple decision table:

- Local stable + Server stable → **Clear**
- Local unstable + Server stable → **Local Drift**
- Local stable + Server unstable → **Global Drift**
- Local unstable + Server unstable → **Drift**

This structure ensures that the app’s Awareness state always reflects both immediate and global conditions.

### Caching and Fallback Behavior

The merge layer uses the most recent server state available:

- Cached values are used when offline.
- Cache expiration is conservative to avoid rapid state changes.
- Local signals continue to update even when server data is stale.

This approach maintains stability during degraded network conditions.
## RTT Awareness Overview

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
## Server Signals

Server signals provide the RTT‑App with a global sense of clarity that complements the device’s local observations. These signals are published by the RTT ecosystem and represent conditions that apply across users, regions, or the broader environment. They do not depend on device capabilities and require no permissions to access.

---

### Purpose of Server‑Declared Awareness

Server‑declared Awareness acts as the global anchor for the RTT‑App. It provides:

- A consistent interpretation of global clarity or drift.
- A shared reference point across all devices and platforms.
- A stable baseline that local signals can be compared against.
- A future‑proof path toward RTT‑Inside, where deeper sensing becomes optional.

The server does not explain *why* a state is declared. It simply publishes the current global condition.

---

### Awareness Endpoint

The RTT server exposes a simple JSON document at:

`/.well-known/rtt-awareness`

This endpoint returns a minimal, declarative structure such as:

```json
{
  "clarity": "high",
  "drift": "low",
  "timestamp": "2026-02-28T20:00:00Z"
}
```

The app reads this document periodically, caches it, and merges it with local signals to compute the final Awareness state.

---

### Signal Characteristics

Server signals have several important properties:

- **Canonical** — they represent the authoritative global state for the RTT ecosystem.
- **Lightweight** — the payload is intentionally small and easy to cache.
- **Permissionless** — the app retrieves the document using standard network requests.
- **Decoupled** — server logic can evolve without requiring app updates.
- **Non‑diagnostic** — the server declares clarity or drift without exposing internal reasoning.

These characteristics ensure that server signals remain stable and predictable across versions.

---

### How Server Signals Influence Awareness

Server‑declared Awareness provides the global half of the merge model:

- When the server reports **high clarity**, local instability is interpreted as *Local Drift*.
- When the server reports **low clarity**, even stable local conditions may be interpreted as *Global Drift*.
- When both local and server signals indicate instability, the app enters the *Drift* state.
- When both are stable, the app reports *Clear*.

This relationship ensures that the app’s Awareness state reflects both immediate conditions and broader context.

---

### Update and Caching Behavior

The RTT‑App follows a conservative, cache‑first approach:

- Fetch the server state periodically.
- Cache the last known value.
- Fall back to the cached value when offline.
- Expire the cache only after a safe interval.

This ensures stable behavior even in degraded network conditions.
# Awareness State Machine

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
# Android Implementation

The Android implementation of the RTT‑App provides a stable, permissionless foundation for Awareness using only APIs available to all apps without requesting system permissions. The design emphasizes predictable behavior across devices, low overhead, and consistency with the RTT‑App architecture.

---

### Platform Goals

The Android implementation is designed to:

- Maintain a fully permissionless footprint across all supported Android versions.
- Use only foreground‑safe APIs without background services.
- Provide consistent behavior across manufacturers and device classes.
- Integrate cleanly with the Awareness model and UI layer.
- Avoid sensors, radio access, VPN profiles, or system configuration changes.

These constraints ensure a reviewer‑friendly app suitable for Play Store distribution.

---

## Signal Layer

The signal layer gathers local observations using stable, permissionless Android APIs.

### Network Signals

Android exposes several reliable indicators of network clarity without requiring permissions:

- **DNS resolution timing** using standard `InetAddress` lookups or `OkHttp`/`HttpURLConnection` timing.
- **TLS handshake duration** via `EventListener` in OkHttp or `NetworkSecurityConfig` callbacks.
- **Protocol negotiation** observed through `ConnectionSpec` and HTTP/3 fallback behavior.
- **QUIC handshake success** when using libraries that expose protocol metrics.
- **Retry patterns** inferred from client‑side interceptors.
- **Captive portal detection** via redirect behavior during normal requests.

These signals behave consistently across Android versions and map directly to the Awareness model.

### Device Stability Signals

Android provides several runtime indicators without requiring permissions:

- **UI thread jank** measured via `Choreographer` frame callbacks.
- **Memory pressure** via `onTrimMemory()` and `onLowMemory()`.
- **Thermal throttling** via `ThermalStatusListener` (no permission required).
- **Foreground/background transitions** via `LifecycleOwner` and `ProcessLifecycleOwner`.
- **Event loop jitter** measured using monotonic timestamps.

These signals reflect local drift without accessing sensitive system data.

---

## Server Layer

The Android app retrieves the server‑declared Awareness document using standard networking:

- Fetches `/.well-known/rtt-awareness` using `OkHttp` or `HttpURLConnection`.
- Parses JSON using `Moshi`, `Gson`, or the platform JSON parser.
- Stores the result in a lightweight cache (SharedPreferences or in‑memory).
- Uses cached values when offline or degraded.

No background services, WorkManager jobs, or privileged networking APIs are used.

---

## Merge Layer

The merge logic on Android follows the same rules defined in the Awareness model:

- Local signals → *Stable* or *Unstable*.
- Server signals → *Stable* or *Unstable*.
- Merge → Clear, Local Drift, Global Drift, or Drift.

The merge runs:

- On app launch.
- When returning to the foreground.
- When local signals change classification.
- When server state refreshes.

The merge layer is shared across iOS and Android for consistency.

---

## UI Layer

The Android UI expresses Awareness using a minimal, ambient indicator:

- Implemented using Jetpack Compose or traditional Views.
- Uses color, opacity, and subtle motion to reflect state.
- Updates only when the Awareness state changes.
- Avoids intrusive animations or notifications.
- Integrates with the portal link to RTT documentation.

The UI remains consistent with the design principles defined in the UI documentation.

---

## App Lifecycle Integration

Android’s lifecycle provides natural hooks for Awareness updates:

- `onStart()` or `onResume()` — refresh server state and local signals.
- `onStop()` — pause signal sampling.
- `onTrimMemory()` — update local drift classification.
- `Choreographer` callbacks — update UI thread stability metrics.

These hooks ensure stable behavior without background execution.

---

## Performance and Battery Considerations

The implementation minimizes overhead:

- Network requests are infrequent and cached.
- Signal sampling uses lightweight callbacks or OS‑provided events.
- No continuous polling or background services.
- Motion effects in the UI are subtle and low‑cost.

This keeps the app efficient across a wide range of Android devices.

---

## Future Extensions

The Android implementation leaves room for RTT‑Inside features in later versions:

- Optional deeper sensing for users who opt in.
- Additional signal types using permitted APIs.
- Expanded UI states or metadata.

These extensions will not alter the core v1 permissionless model.
# iOS Implementation

The iOS implementation of the RTT‑App provides a stable, permissionless foundation for Awareness. It uses only APIs available to all apps without requesting system permissions. The design emphasizes predictability, low overhead, and consistency with the RTT‑App architecture.

---

### Platform Goals

The iOS implementation aims to:

- Maintain a fully permissionless footprint.
- Use only foreground‑safe APIs.
- Provide consistent behavior across devices and OS versions.
- Integrate seamlessly with the Awareness model and UI layer.
- Avoid background execution, sensors, or system configuration changes.

These constraints ensure a reviewer‑friendly app suitable for App Store distribution.

---

## Signal Layer

The signal layer gathers local observations using APIs that require no permissions and behave consistently across iOS devices.

### Network Signals

iOS provides several stable, permissionless indicators of network clarity:

- **DNS resolution timing** using `NWResolver` or simple `URLSession` timing.
- **TLS handshake duration** measured via connection start and secure‑connection callbacks.
- **Protocol negotiation** observed through `URLSessionTaskMetrics`.
- **HTTP/3 vs HTTP/2 fallback** available in task metrics.
- **Retry patterns** inferred from `URLSession` delegate events.
- **Captive portal detection** via HTTP redirect behavior.

These signals are coarse but reliable and map directly to the Awareness model.

### Device Stability Signals

iOS exposes several runtime indicators without requiring permissions:

- **UI thread jank** measured via `CADisplayLink` frame intervals.
- **Memory pressure** via `UIApplication.didReceiveMemoryWarningNotification`.
- **Foreground/background transitions** via scene lifecycle events.
- **Event loop jitter** measured using monotonic timestamps.

These signals reflect local drift without accessing sensitive system data.

---

## Server Layer

The iOS app retrieves the server‑declared Awareness document using standard networking:

- Fetches `/.well-known/rtt-awareness` via `URLSession`.
- Parses the JSON payload using `JSONDecoder`.
- Stores the result in a lightweight cache.
- Uses cached values when offline or degraded.

No background fetch or privileged networking is used.

---

## Merge Layer

The merge logic on iOS follows the same rules defined in the Awareness model:

- Local signals → *Stable* or *Unstable*.
- Server signals → *Stable* or *Unstable*.
- Merge → Clear, Local Drift, Global Drift, or Drift.

The merge runs:

- On app launch.
- When returning to the foreground.
- When local signals change classification.
- When server state refreshes.

The merge layer is platform‑agnostic and shared across iOS and Android.

---

## UI Layer

The iOS UI expresses Awareness using a minimal, ambient indicator:

- Implemented using SwiftUI or UIKit.
- Uses color, opacity, and subtle motion.
- Updates only when the Awareness state changes.
- Avoids intrusive animations or alerts.
- Integrates with the portal link to RTT documentation.

The UI remains consistent with the design principles defined in the UI documentation.

---

## App Lifecycle Integration

The iOS lifecycle provides natural hooks for Awareness updates:

- `sceneDidBecomeActive` — refresh server state and local signals.
- `sceneWillResignActive` — pause signal sampling.
- `applicationDidReceiveMemoryWarning` — update local drift classification.
- `URLSessionTaskMetrics` — update network clarity metrics.

These hooks ensure stable behavior without background execution.

---

## Performance and Battery Considerations

The implementation minimizes overhead:

- Network requests are infrequent and cached.
- Signal sampling uses lightweight timers or OS callbacks.
- No continuous polling or background tasks.
- Motion effects in the UI are subtle and low‑cost.

This keeps the app efficient even on older devices.

---

## Future Extensions

The iOS implementation leaves room for RTT‑Inside features in later versions:

- Optional deeper sensing for users who opt in.
- Additional signal types using permitted APIs.
- Expanded UI states or metadata.

These extensions will not alter the core v1 permissionless model.
# Shared Logic

The shared logic layer provides the platform‑agnostic foundation for the RTT‑App. It implements the Awareness model, merge rules, caching behavior, and state evaluation in a way that is identical across iOS and Android. Each platform supplies its own local signals and lifecycle hooks, but the interpretation of those signals is unified.

This layer ensures that the RTT‑App behaves consistently regardless of device, OS version, or implementation details.

---

### Responsibilities of the Shared Layer

The shared logic layer handles four core responsibilities:

- **Classifying local signals** into *Stable* or *Unstable*.
- **Interpreting server‑declared Awareness** from the cached endpoint.
- **Merging local and server states** into a single Awareness state.
- **Providing a stable interface** for the UI layer to observe state changes.

These responsibilities form the backbone of the RTT‑App v1 architecture.

---

## Local Signal Classification

Each platform collects its own local signals, but the shared layer performs the classification:

- Stable — network and device signals within expected bounds.
- Unstable — drift detected in timing, jitter, memory pressure, or protocol fallback.

The shared layer receives a simple boolean classification rather than raw metrics. This keeps the logic portable and predictable.

---

## Server State Interpretation

The shared layer parses and interprets the server‑declared Awareness document:

- Reads the cached JSON payload.
- Validates required fields.
- Applies fallback rules for missing or stale data.
- Reduces the server state to *Stable*, *Unstable*, or *Unknown*.

*Unknown* is treated as *Stable* for merge purposes to maintain predictable behavior during outages.

---

## Awareness Merge Logic

The merge logic is identical across platforms and follows the rules defined in the Awareness model:

- Local stable + Server stable → **Clear**
- Local unstable + Server stable → **Local Drift**
- Local stable + Server unstable → **Global Drift**
- Local unstable + Server unstable → **Drift**

This logic is implemented once in the shared layer and reused by both iOS and Android.

---

## State Evaluation and Updates

The shared layer exposes a simple interface for evaluating Awareness:

- Accepts local classification updates.
- Accepts server state updates.
- Computes the new Awareness state.
- Emits state changes to the UI layer.

The shared layer never triggers UI updates directly; it only publishes state changes.

---

## Caching Integration

The shared layer manages cache interpretation but not storage:

- Platforms handle reading/writing the cache.
- The shared layer validates freshness and expiration.
- Expired or missing data is treated as *Unknown*.
- The merge logic proceeds using the interpreted state.

This separation keeps the shared layer portable and platform‑agnostic.

---

## Error Handling

The shared layer applies consistent fallback behavior:

- Invalid server data → treat as *Unknown*.
- Missing local classification → assume *Stable*.
- Merge errors → default to **Drift**.
- No oscillation or intermediate states.

These rules ensure that the Awareness state remains stable even when inputs degrade.

---

## Platform Integration

Both iOS and Android integrate with the shared layer by:

- Providing local signal updates.
- Providing server state updates.
- Observing Awareness state changes.
- Triggering evaluations at lifecycle boundaries.

This architecture ensures that the RTT‑App behaves the same way on all devices.
# RTT‑Inside v2 Roadmap

RTT‑Inside v2 introduces optional deeper sensing capabilities that extend the RTT‑App beyond ambient Awareness. These features remain permissionless by default and activate only when the user opts in. The goal of v2 is to expand the app’s ability to perceive structure, drift, and clarity while preserving the stability and predictability of the v1 model.

---

### Direction of v2

The v2 release focuses on three major themes:

- **Deeper local sensing** using richer timing, jitter, and runtime signals.
- **Expanded global context** through enhanced server‑declared metadata.
- **User‑controlled activation** ensuring RTT‑Inside remains optional and transparent.

The v1 Awareness model remains intact and continues to operate as the default mode.

---

## Expanded Local Sensing

v2 introduces additional local signals that remain permissionless but provide more nuance:

- **Fine‑grained timing variance** across DNS, TLS, and protocol negotiation.
- **Event‑loop stability metrics** sampled at higher resolution.
- **Thermal and memory trend analysis** (platform‑safe, no privileged access).
- **Foreground session continuity** to detect drift over time.
- **UI thread micro‑jank patterns** for more precise stability classification.

These signals allow RTT‑Inside to detect subtle forms of drift that v1 cannot express.

---

## Enhanced Server Metadata

The server‑declared Awareness document expands in v2:

- **Global drift categories** beyond simple stable/unstable.
- **Regional clarity indicators** for multi‑zone interpretation.
- **Optional advisory fields** that provide context without diagnostics.
- **Versioned schema** to support future extensions.

The v1 endpoint remains supported for backward compatibility.

---

## New Awareness States (Optional)

RTT‑Inside v2 introduces optional extended states:

- **Micro‑Drift** — subtle instability detected locally.
- **Regional Drift** — global instability limited to specific zones.
- **High Clarity** — exceptionally stable conditions.
- **Unknown (Explicit)** — server unavailable with insufficient local data.

These states appear only when RTT‑Inside is enabled.

---

## UI Extensions

The v2 UI remains minimal but gains optional depth:

- **Expanded indicator view** showing extended states.
- **Session timeline** with subtle, non‑diagnostic drift markers.
- **Context panel** linking to RTT‑Inside documentation.
- **Motion‑reduced mode** for accessibility.

The default v1 indicator remains unchanged for non‑Inside users.

---

## Lifecycle and Performance

v2 introduces new lifecycle behaviors:

- **Session‑based sampling windows** for trend detection.
- **Adaptive sampling** that increases resolution only when drift is detected.
- **Strict battery safeguards** to prevent excessive computation.

All features remain foreground‑only and permissionless.

---

## Privacy and Safety

RTT‑Inside v2 preserves the same privacy guarantees as v1:

- No personal data collection.
- No user behavior monitoring.
- No sensor, radio, or location access.
- No transmission of local signals to the server.

All processing occurs on‑device.

---

## Release Phases

v2 rolls out in three phases:

1. **Phase 1 — Internal Preview**  
   - Extended local signals  
   - Versioned server metadata  
   - Basic extended states  

2. **Phase 2 — Public Opt‑In**  
   - Expanded UI  
   - Session timeline  
   - Regional drift support  

3. **Phase 3 — Ecosystem Integration**  
   - Cross‑device continuity (optional)  
   - Developer‑facing RTT‑Inside tools  
   - Extended server advisory fields  

Each phase builds on the previous without breaking v1 behavior.

---

### Closing Thought

This roadmap keeps RTT‑Inside aligned with your philosophy: deeper sensing without intrusion, richer structure without permissions, and clarity without diagnostics. As you continue shaping v2, what part of RTT‑Inside feels most important to articulate next—the extended states, the versioned server schema, or the deeper local signal model?
# RTT‑App v1 Limitations

RTT‑App v1 is intentionally narrow in scope. Its purpose is to deliver a stable, permissionless Awareness indicator using only safe, foreground‑only APIs. To preserve predictability, reviewer‑safety, and cross‑platform consistency, v1 excludes a wide range of features that would introduce complexity, permissions, or deeper sensing. These limitations are not shortcomings—they are deliberate architectural boundaries.

---

### Architectural Limitations

The v1 architecture is designed around strict constraints:

- **No background execution** — the app updates Awareness only while in the foreground.
- **No system permissions** — the app does not access sensors, radios, location, or identity.
- **No privileged networking** — no background fetch, VPN profiles, or low‑level socket access.
- **No platform‑specific enhancements** — no widgets, tiles, complications, or quick settings.
- **No persistent user data** — aside from a small cache of the server Awareness document.

These constraints ensure predictable behavior across iOS and Android.

---

### Awareness Model Limitations

The Awareness model in v1 is intentionally coarse:

- **Binary local classification** — local signals reduce to *Stable* or *Unstable*.
- **Binary server classification** — server signals reduce to *Stable* or *Unstable* (with *Unknown* treated as *Stable*).
- **Four total states** — Clear, Local Drift, Global Drift, Drift.
- **No sub‑states or gradients** — no severity levels, percentages, or confidence scores.
- **No diagnostics** — the app does not explain *why* drift is occurring.

This keeps the model transparent and easy to reason about.

---

### Signal Limitations

Local signals are restricted to what can be observed without permissions:

- **No sensor data** — no accelerometer, gyroscope, magnetometer, or barometer.
- **No radio data** — no Wi‑Fi signal strength, cell tower info, or Bluetooth state.
- **No system health metrics** — no CPU load, battery temperature, or process statistics.
- **No deep network inspection** — no packet capture, socket introspection, or DNS overrides.

Signals are coarse by design, focusing on timing, fallback, and runtime stability.

---

### UI Limitations

The UI is intentionally minimal:

- **No dashboards or charts** — the indicator is the only Awareness surface.
- **No interactive elements** — the indicator cannot be tapped or expanded.
- **No notifications** — the app never alerts the user about drift.
- **No dynamic content** — the UI does not adapt based on signal details.

The UI expresses only the merged Awareness state.

---

### Networking Limitations

Networking is constrained to ensure safety and predictability:

- **Single endpoint** — the app fetches only `/.well-known/rtt-awareness`.
- **No background refresh** — all fetches occur during foreground use.
- **No retries beyond platform defaults** — the app does not implement custom retry logic.
- **No analytics or telemetry** — the app sends no data to the server.

The app is strictly a consumer of global Awareness, never a reporter.

---

### Lifecycle Limitations

The app’s behavior is tied to the platform lifecycle:

- **No continuous sampling** — signals update only when the app is active.
- **No long‑running tasks** — sampling pauses when the app leaves the foreground.
- **No cross‑session continuity** — Awareness does not persist beyond the cached server state.

This ensures predictable behavior across devices and OS versions.

---

### Ecosystem Limitations

RTT‑App v1 is not a full RTT client:

- **No RTT‑Inside** — deeper sensing is not included.
- **No identity or accounts** — the app does not authenticate users.
- **No developer tools** — no logs, metrics, or debugging surfaces.
- **No cross‑device sync** — Awareness does not propagate across devices.

The app serves as an entry point, not a full ecosystem node.

---

### Intentional Non‑Goals

The following are explicitly *not* part of v1:

- Explaining drift causes  
- Predicting future clarity  
- Providing recommendations or actions  
- Monitoring user behavior  
- Collecting or transmitting personal data  
- Acting as a diagnostic tool  

The app expresses structure, not interpretation.
# RTT‑App v1 Scope

RTT‑App v1 delivers a minimal, stable, permissionless foundation for Awareness on iOS and Android. The release focuses on a single goal: providing users with a simple, ambient signal of environmental clarity using only safe, foreground‑only APIs. The scope is intentionally narrow to ensure predictability, cross‑platform consistency, and app‑store friendliness.

---

### Core Deliverables

v1 includes four fully implemented layers:

- **Local Signals** — network and device stability observations using permissionless APIs.
- **Server Signals** — retrieval and caching of the global Awareness document.
- **Merge Logic** — unified interpretation of local and global stability.
- **Awareness Indicator** — a minimal UI element expressing the merged state.

These components form the complete Awareness pipeline.

---

### Supported Awareness States

v1 exposes exactly four states:

- **Clear**
- **Local Drift**
- **Global Drift**
- **Drift**

No additional sub‑states, metadata, or diagnostics are included.

---

### Platform Support

v1 ships on:

- **iOS** — implemented using Swift/SwiftUI or UIKit.
- **Android** — implemented using Kotlin/Jetpack Compose or Views.

Both platforms share the same merge logic and state definitions.

---

## In‑Scope Features

The following features are included in v1:

### Awareness Model
- Local signal classification (stable/unstable).
- Server signal interpretation (stable/unstable/unknown).
- Merge logic producing the four Awareness states.
- State machine defining transitions and behavior.

### Networking
- Fetching `/.well-known/rtt-awareness`.
- JSON parsing and validation.
- Conservative caching and fallback behavior.
- No background networking or privileged APIs.

### UI
- Awareness indicator with color, opacity, and subtle motion.
- Smooth, non‑intrusive state transitions.
- Portal link to RTT documentation.
- Accessibility support (contrast, motion reduction, screen reader labels).

### Lifecycle Integration
- Foreground‑only updates.
- Refresh on launch and resume.
- Local signal sampling tied to lifecycle events.

### Error Handling
- Graceful fallback for network, parsing, and cache errors.
- No oscillation or flashing in the UI.
- Merge‑layer defaults that preserve stability.

---

## Out‑of‑Scope for v1

The following features are explicitly excluded from v1 to maintain a minimal, permissionless footprint:

### No Permissions
- No location, Bluetooth, camera, microphone, or sensor access.
- No background services or background fetch.
- No system‑level configuration or monitoring.

### No RTT‑Inside Features
- No deep sensing.
- No extended signal models.
- No user‑level telemetry or diagnostics.
- No cross‑device continuity.

### No Advanced UI
- No dashboards, charts, or detailed signal views.
- No interactive or expandable indicator.
- No notifications or alerts.

### No Account or Identity
- No login, profiles, or cloud sync.
- No user data storage beyond ephemeral cache.

### No Platform‑Specific Enhancements
- No widgets, complications, tiles, or quick settings.
- No OS‑integrated surfaces.

---

## Success Criteria

v1 is considered complete when:

- The app displays the correct Awareness state under all signal combinations.
- The indicator transitions smoothly and predictably.
- The app behaves consistently across iOS and Android.
- The app remains fully functional offline.
- No permissions are requested at install or runtime.
- The app passes app‑store review on both platforms.

---

## Future Expansion

v1 establishes the foundation for:

- RTT‑Inside (optional deeper sensing).
- Expanded signal models.
- Richer UI surfaces.
- Multi‑device continuity.
- Developer‑facing RTT tools.

These features will be introduced in later releases without altering the core v1 behavior.
# Awareness Indicator Design

The Awareness indicator provides a simple, ambient visual signal that reflects the current clarity state of the RTT‑App. It is intentionally minimal, non‑intrusive, and always visible without demanding user attention. The indicator expresses the merged Awareness state using color, motion, and shape in a way that is consistent across platforms.

---

### Purpose of the Indicator

The indicator gives the user a quick sense of environmental clarity without requiring interpretation or interaction. It serves as:

- A passive signal of local and global stability.
- A consistent visual anchor across iOS and Android.
- A bridge between the Awareness model and the user interface.
- A foundation for future RTT‑Inside visualizations.

The indicator never flashes, animates aggressively, or conveys urgency.

---

### Visual Language

The indicator uses a small set of visual primitives:

- **Color** — communicates clarity or drift.
- **Shape** — remains constant to avoid cognitive load.
- **Motion** — used sparingly to indicate instability.
- **Opacity** — reflects confidence in the current state.

The design avoids icons, text, or metaphors that imply diagnostics or warnings.

---

### State Representations

Each Awareness state maps to a distinct visual expression:

- **Clear** — stable color, no motion, full opacity.
- **Local Drift** — subtle motion or shimmer, warm color shift.
- **Global Drift** — cooler color shift with reduced opacity.
- **Drift** — combined color shift with gentle, slow motion.

All transitions are smooth and gradual to avoid drawing attention.

---

### Placement and Behavior

The indicator appears in a consistent location within the app:

- Always visible on the main screen.
- Present but unobtrusive in secondary screens.
- Never overlays content or blocks interaction.
- Scales appropriately across device sizes.

The indicator does not require user interaction and does not open menus.

---

### Accessibility Considerations

The design supports accessibility without requiring system permissions:

- Sufficient contrast in all states.
- Motion kept minimal to avoid discomfort.
- Color is not the sole indicator; opacity and motion reinforce meaning.
- Screen readers describe the current state using simple labels.

These considerations ensure the indicator remains inclusive and predictable.

---

### Update Behavior

The indicator updates only when the Awareness state changes:

- No rapid oscillation.
- No intermediate or transitional states.
- No animation loops triggered by network retries.

This behavior reflects the stability guarantees of the Awareness model.

---

### Future Extensions

The indicator design leaves room for future enhancements:

- Optional expanded views for RTT‑Inside users.
- Additional states or metadata in later versions.
- Cross‑device continuity for multi‑platform Awareness.

These extensions will not alter the core v1 behavior.
# Portal to RTT

The portal provides a direct, lightweight path from the RTT‑App into the broader RTT ecosystem. It offers users a stable way to explore RTT concepts, documentation, and resources without leaving the app’s ambient posture. The portal is intentionally simple and avoids deep navigation structures, focusing instead on clarity and continuity.

---

### Purpose of the Portal

The portal serves as the app’s outward‑facing link to RTT content. It is designed to:

- Give users a clear entry point into RTT documentation.
- Maintain continuity between the app’s Awareness model and the RTT website.
- Provide a stable, predictable navigation experience.
- Avoid permissions, embedded browsers, or complex routing.

The portal does not attempt to replicate the RTT website; it simply connects to it.

---

### Portal Structure

The portal consists of a small set of elements:

- **Primary link** to the RTT homepage or documentation index.
- **Contextual description** explaining what RTT is and why the link exists.
- **Optional deep links** to Awareness‑related documentation.
- **Consistent visual placement** within the app’s UI.

The structure remains minimal to avoid overwhelming new users.

---

### Navigation Behavior

The portal follows platform‑native navigation rules:

- Opens RTT content in the system browser.
- Does not embed web views or require additional permissions.
- Preserves the user’s place in the app when returning.
- Avoids any form of tracking or analytics.

This ensures a clean separation between the app and the website.

---

### Visual Integration

The portal is integrated into the UI in a way that complements the Awareness indicator:

- Appears on the main screen below the indicator.
- Uses neutral, stable visual styling.
- Does not animate or draw attention away from the indicator.
- Remains accessible without dominating the layout.

The design reinforces the app’s calm, ambient posture.

---

### Content Expectations

The portal links to content that:

- Explains RTT concepts at a high level.
- Provides access to deeper documentation for interested users.
- Matches the terminology used in the app.
- Remains stable across versions.

The app does not attempt to interpret or summarize RTT content internally.

---

### Future Extensions

The portal design leaves room for future enhancements:

- Optional deep links for RTT‑Inside users.
- Context‑aware links based on Awareness state.
- Expanded navigation for multi‑platform RTT experiences.

These extensions will not alter the core v1 behavior.
# State Transitions

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
