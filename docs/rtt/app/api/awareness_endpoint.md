# Awareness Endpoint

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
