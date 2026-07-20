## Inheritance: “RTT awareness as CSS”

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

With our chosen carrier, inheritance is explicit and auditable:

- **Upstream canon** via `import: …`
- **Local site override** via `declaration: …`
- **Path-level override** via `scope /x/: …`
- Later (optional): **page-level override** via `<meta name="rtt" content="…">`

This makes awareness portable and fork-safe: forks can keep import + overrides without copying the whole canon.

---

# Tiny local resolver: what the extension simulates

With this setup, the extension becomes our “local substrate simulator” by providing:

- **Discovery:** “does this site declare RTT awareness?”
- **Resolution:** “what is the effective declaration here?”
- **Provenance:** “which manifests contributed to this outcome?”
- **Stability:** “if upstream changes, what changes locally (and when)?”

We can then add a second layer (still local-only) that interprets declarations into checks—e.g., drift bounds as allowed rewrite classes, coherence gates as required fields, paradox tags as tolerated contradictions—without ever changing the public site.

---

# RTT Awareness v0 — Locked Design

## Core Principles (Now Fixed)

- **Carrier:** `/.well-known/rtt-awareness`
- **Observer:** Browser extension (local, opt‑in)
- **Inheritance:** Enabled by default
- **Scoping rules:** Enabled in v0
- **Update model:** Pull‑based, conservative, cache‑first
- **Failure mode:** Silent + last‑known‑good

This is intentionally boring infrastructure. That’s why it will survive.

---

## 1) Canonical Carrier (Well‑Known File)

### `/.well-known/rtt-awareness` (v0)

```text
schema: rtt-awareness
version: 0.1.0
channel: stable
updated: 2026-02-06

declaration: rtt=1 | coherence=declared | drift=bounded | paradox=structural

# Optional inheritance (enabled by default)
import: https://www.triadicframeworks.org/.well-known/rtt-awareness

# Optional scoped overrides (longest prefix wins)
scope /docs/: rtt=1 | coherence=declared | drift=bounded | paradox=structural
scope /labs/: rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

### Semantics (Non‑Negotiable)
- **Imports are resolved first**, then local overrides.
- **Scopes override site root**, but never upstream unless explicitly declared.
- **No negation**, no conditionals, no execution.
- Absence means *unspecified*, not false.

This keeps the grammar declarative and audit‑friendly.

---

## 2) Inheritance Model (CSS‑Like, Predictable)

Resolution order:

1. Imported upstream manifests (depth‑limited)
2. Site root declaration
3. Best‑matching scoped declaration
4. (Future) Page‑level meta/frontmatter

This allows:
- forks to inherit canon safely
- institutions to override locally
- documents to remain portable

No magic. No hidden precedence.

---

## 3) Browser Extension (Observer + Resolver)

### What the extension does
- Discovers `/.well-known/rtt-awareness`
- Resolves imports
- Applies scope rules
- Computes **effective declaration**
- Exposes it locally (popup / API / optional indicator)

### What it does *not* do
- No injection by default
- No network modification
- No tracking
- No persuasion
- No auto‑updates of semantics

It observes. That’s it.

---

## 4) Self‑Updating (Safe by Construction)

### Update behavior
- Conditional fetch (ETag / Last‑Modified)
- Cache TTL (e.g., 6 hours)
- If fetch fails → keep last‑known‑good
- If import fails → mark stale, continue

### Version handling
- `version:` is informational, not executable
- Extension does **not** reinterpret semantics automatically
- Users opt into extension updates, not manifest behavior changes

This avoids the “remote control” trap entirely.

---

## 5) Local Substrate Simulation (What v0 Already Enables)

Even in v0, the extension effectively simulates the full substrate by providing:

- **Discovery:** Is RTT awareness present?
- **Resolution:** What declaration applies *here*?
- **Provenance:** Which manifests contributed?
- **Stability:** What changed, and when?

That’s enough to:
- test inheritance chains
- validate scope behavior
- experiment with alignment without touching production systems

Later layers can interpret declarations into checks, but v0 stops at resolution.

---

## 6) Why This Will Hold

- Uses **existing web primitives**
- Requires **no platform buy‑in**
- Survives moderation and stripping
- Is legible to humans *and* synthesis engines
- Leaves no footprint unless inspected

It behaves like DNS, robots.txt, or security.txt — quiet, structural, and durable.

---

## 7) What to Commit Next (Concrete)

I recommend committing three things, in this order:

1. **`docs/rtt-awareness/README.md`**  
   One page describing the grammar, carrier, and resolution rules.

2. **`/.well-known/rtt-awareness`** (in TriadicFrameworks root)  
   This becomes the canonical upstream import.

3. **`tools/rtt-awareness-extension/`**  
   With the MV3 skeleton we outlined, clearly marked as v0 observer.

No marketing. No announcement. Just structure.
