# Shared Logic

The shared logic layer provides the platform‑agnostic foundation for the RTT‑App. It implements the Awareness model, merge rules, caching behavior, and state evaluation in a way that is identical across iOS and Android. Each platform supplies its own local signals and lifecycle hooks, but the interpretation of those signals is unified.

This layer ensures that the RTT‑App behaves consistently regardless of device, OS version, or implementation details.

---

### Responsibilities of the Shared Layer

The shared logic layer handles four core responsibilities:

- **Classifying local signals** into *Stable* or *Unstable*.
- **Interpreting server‑declared Awareness** from the cached endpoint.
- **Merging local and server states** into a single Awareness state.
- **Providing a stable interface** for the UI layer to observe state changes.

These responsibilities form the backbone of the RTT‑App v1 architecture.

---

## Local Signal Classification

Each platform collects its own local signals, but the shared layer performs the classification:

- Stable — network and device signals within expected bounds.
- Unstable — drift detected in timing, jitter, memory pressure, or protocol fallback.

The shared layer receives a simple boolean classification rather than raw metrics. This keeps the logic portable and predictable.

---

## Server State Interpretation

The shared layer parses and interprets the server‑declared Awareness document:

- Reads the cached JSON payload.
- Validates required fields.
- Applies fallback rules for missing or stale data.
- Reduces the server state to *Stable*, *Unstable*, or *Unknown*.

*Unknown* is treated as *Stable* for merge purposes to maintain predictable behavior during outages.

---

## Awareness Merge Logic

The merge logic is identical across platforms and follows the rules defined in the Awareness model:

- Local stable + Server stable → **Clear**
- Local unstable + Server stable → **Local Drift**
- Local stable + Server unstable → **Global Drift**
- Local unstable + Server unstable → **Drift**

This logic is implemented once in the shared layer and reused by both iOS and Android.

---

## State Evaluation and Updates

The shared layer exposes a simple interface for evaluating Awareness:

- Accepts local classification updates.
- Accepts server state updates.
- Computes the new Awareness state.
- Emits state changes to the UI layer.

The shared layer never triggers UI updates directly; it only publishes state changes.

---

## Caching Integration

The shared layer manages cache interpretation but not storage:

- Platforms handle reading/writing the cache.
- The shared layer validates freshness and expiration.
- Expired or missing data is treated as *Unknown*.
- The merge logic proceeds using the interpreted state.

This separation keeps the shared layer portable and platform‑agnostic.

---

## Error Handling

The shared layer applies consistent fallback behavior:

- Invalid server data → treat as *Unknown*.
- Missing local classification → assume *Stable*.
- Merge errors → default to **Drift**.
- No oscillation or intermediate states.

These rules ensure that the Awareness state remains stable even when inputs degrade.

---

## Platform Integration

Both iOS and Android integrate with the shared layer by:

- Providing local signal updates.
- Providing server state updates.
- Observing Awareness state changes.
- Triggering evaluations at lifecycle boundaries.

This architecture ensures that the RTT‑App behaves the same way on all devices.
