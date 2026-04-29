# Error Handling

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
