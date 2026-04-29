## Merge Logic

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
