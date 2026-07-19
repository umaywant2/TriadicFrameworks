# Badge Logic 🏷️  
*(RTT‑Aligned System Signaling)*

Badges are the **primary output** of NawderOS.

They are not alerts.  
They are not errors.  
They are not commands.

Badges are **signals** — structured observations about system coherence over time.

---

## Why Badges Exist

RTT emphasizes:
- observation over enforcement
- coherence over control
- lineage over anonymity

Badges exist to make those principles **machine‑visible**.

If something matters, it should emit a badge.  
If it doesn’t emit a badge, it didn’t happen (as far as RTT is concerned).

---

## What a Badge Is (and Isn’t)

### A badge **is**:
- append‑only
- machine‑readable
- context‑rich
- boring 😄

### A badge **is not**:
- a policy decision
- a remediation trigger
- a panic signal
- a judgment

Badges describe *what happened*, not *what to do*.

---

## Core Badge Structure 📐

Every badge follows the same basic structure:

```json
{
  "badge_type": "STRING",
  "timestamp": "ISO-8601",
  "module": "STRING",
  "context": { },
  "severity": "INFO | NOTICE | DRIFT"
}
```

This structure is intentionally simple and stable.

---

## Badge Fields Explained

### `badge_type`
A short, stable identifier.

Examples:
- `CORRIDOR_BREACH`
- `WRAP_DRIFT`
- `SUBSTRATE_BASELINE`
- `SUBSTRATE_DRIFT`

Badge types should be:
- descriptive
- consistent
- boring

---

### `timestamp`
When the observation occurred.

Badges care about **time** — RTT is literally about time 😄

---

### `module`
Which module emitted the badge.

This preserves lineage and makes debugging sane.

---

### `context`
A free‑form object containing relevant metadata.

Examples:
- PID
- memory region
- kernel version
- module name

Context should explain *why* the badge exists without interpretation.

---

### `severity`
A coarse indicator of coherence state.

Allowed values:
- `INFO` — expected observation
- `NOTICE` — unusual but non‑critical
- `DRIFT` — coherence deviation detected

Severity is **not** urgency.

---

## Common Badge Types 🧩

### `SUBSTRATE_BASELINE`
Emitted at boot.

Purpose:
- record what the system believes it is
- establish a reference point

---

### `SUBSTRATE_DRIFT`
Emitted when foundational assumptions change.

Purpose:
- detect silent system evolution
- preserve lineage

---

### `CORRIDOR_BREACH`
Emitted when behavior exits a declared corridor.

Purpose:
- highlight coherence boundary crossings
- enable later analysis

---

### `WRAP_DRIFT`
Emitted during unexpected boundary transitions.

Purpose:
- observe context loss or mismatch
- flag risky transitions

---

## Badge Emission Rules 📜

To keep badges trustworthy:

- Never block system execution
- Never trigger enforcement
- Never modify system state
- Never hide or suppress badges

If emitting a badge would cause harm, **don’t emit it**.

---

## Badge Consumers 🔍

Badges are meant to be consumed by:
- humans
- logs
- simulations
- visualization tools
- educational tooling

They are **not** meant to be acted on automatically.

Interpretation belongs outside the kernel.

---

## Forking and Badges 🍴

Forks may:
- add new badge types
- extend context fields
- redefine severity semantics

Forks should **not**:
- overload existing badge meanings
- silently change badge behavior
- remove lineage information

If you change badge semantics, document it.

---

## Why This Matters

Badges are how RTT stays honest.

They:
- make assumptions visible
- preserve history
- prevent silent drift
- enable learning

They don’t solve problems.  
They make problems *legible*.

And legibility is power 🙂
