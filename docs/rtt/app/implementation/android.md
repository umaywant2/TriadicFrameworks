# Android Implementation

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
