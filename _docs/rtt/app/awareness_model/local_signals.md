## Local Signals

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
