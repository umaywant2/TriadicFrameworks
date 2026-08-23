## Server Signals

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
