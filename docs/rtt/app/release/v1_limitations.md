# RTT‑App v1 Limitations

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
