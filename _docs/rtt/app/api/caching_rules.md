# Caching Rules

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
