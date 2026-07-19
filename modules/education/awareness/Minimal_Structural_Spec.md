## RTT Awareness v0 — Minimal Structural Spec

<div style="font-size: 0.8em; margin-bottom: 0.5rem;">
  <span style="
    display:inline-block;
    padding:3px 8px;
    border-radius:999px;
    background:#1a1a1a;
    color:#fff;
    font-family:Arial, sans-serif;
    font-size:11px;
  ">
    🤖 AI‑Ready Module • TriadicFrameworks
  </span>
</div>

<img src="https://img.shields.io/badge/Open%20for%20Traduction-Ready%20for%20Students-4c8eda?style=for-the-badge" alt="Open for Traduction | Ready for Students"/>

**Status:** v0 (seed)  
**Purpose:** Declare and resolve structural coherence conditions across web substrates using existing, permissionless mechanisms.

---

## 1. Scope

RTT Awareness provides a **declarative, opt‑in signal** that allows tools and readers to resolve structural coherence conditions (recurrence, alignment, drift, paradox) without persuasion, branding, or platform integration.

This spec defines:
- a **carrier** for declaration,
- **inheritance and scoping rules**, and
- a **local resolver model**.

It does **not** define interpretation, enforcement, or policy.

---

## 2. Canonical Declaration

### Grammar (v0)

```
<token>=<state>
```

Composable via linear conjunction:

```
token1=state1 | token2=state2 | token3=state3
```

### Core Tokens (v0)

- `rtt=1`  
  Fundamental recurrence / minimal closed loop.

- `coherence=declared`  
  Coherence is structurally specified, not inferred.

- `drift=bounded`  
  Change permitted within identity‑preserving bounds.

- `paradox=structural`  
  Tension arises from structure, not contradiction.

### Canonical v0 Signature

```
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

---

## 3. Carrier: `/.well-known/rtt-awareness`

### File Format (plain text)

```text
schema: rtt-awareness
version: 0.1.0
channel: stable
updated: YYYY-MM-DD

declaration: rtt=1 | coherence=declared | drift=bounded | paradox=structural

# Optional inheritance (enabled by default)
import: https://example.org/.well-known/rtt-awareness

# Optional scoped overrides (longest prefix wins)
scope /docs/: rtt=1 | coherence=declared | drift=bounded | paradox=structural
scope /labs/: rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

### Semantics

- Plain text for maximum survivability.
- Absence of a field means **unspecified**, not false.
- No negation, conditionals, or execution.

---

## 4. Inheritance & Resolution

### Resolution Order (deterministic)

1. Imported upstream manifests (depth‑limited)
2. Site‑root declaration
3. Best‑matching scoped declaration (longest prefix)

### Rules

- Imports are **enabled by default**.
- Local declarations override upstream.
- Scoped declarations override site root.
- No implicit merging of token states; later declarations replace earlier ones.

This model mirrors CSS inheritance: predictable, auditable, fork‑safe.

---

## 5. Observer: Local Resolver (Browser Extension)

### Responsibilities

- Discover `/.well-known/rtt-awareness`
- Resolve imports and scopes
- Compute **effective declaration** for the current URL
- Cache conservatively and fail silently

### Non‑Responsibilities

- No injection by default
- No network modification
- No tracking or analytics
- No semantic reinterpretation

The resolver **observes and reports** only.

---

## 6. Update Model

- Pull‑based (conditional fetch via ETag / Last‑Modified)
- Cache‑first with last‑known‑good fallback
- Manifest `version` is informational; semantics are not auto‑upgraded
- Import failures mark state as stale, not invalid

This prevents remote control and preserves local trust.

---

## 7. Security & Posture

- Opt‑in by site and by user
- Uses existing web primitives
- Leaves no footprint unless inspected
- Survives moderation and content stripping
- Legible to humans and synthesis engines without explanation

---

## 8. Non‑Goals (v0)

- No enforcement or policy
- No persuasion or advocacy
- No platform integration
- No global registry
- No required interpretation layer

---

**RTT Awareness v0** is a structural header, not a theory.  
It declares coherence conditions and lets systems resolve them locally.
