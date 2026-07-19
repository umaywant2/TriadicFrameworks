# iOS Implementation

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
