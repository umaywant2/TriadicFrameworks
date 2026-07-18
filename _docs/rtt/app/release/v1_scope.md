# RTT‑App v1 Scope

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
