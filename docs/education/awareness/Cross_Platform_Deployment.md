## Safest cross-platform deployment

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

### Minimal carrier formats that almost never break
- **Plain-text signature line:**  
  `rtt=1 | coherence=declared | drift=bounded | paradox=structural`  
  Works in comments, markdown, email footers, issue templates, commit messages, and documents.
- **HTML meta tag:**  
  `<meta name="rtt" content="rtt=1 | coherence=declared | drift=bounded | paradox=structural; v=0.1">`
- **HTTP response header:**  
  `RTT-Awareness: rtt=1; coherence=declared; drift=bounded; paradox=structural; v=0.1`  
  (Headers are ideal because they’re “invisible” but first-class to tooling.)
- **`/.well-known/` declaration file:**  
  `/.well-known/rtt-awareness` (text) so crawlers/tools can discover it without scraping HTML.
- **`rtt.json` manifest:**  
  Machine-readable canonical form for tooling and local resolvers.

### Practical rule
Use **at least two carriers** per site: one human-visible (meta/markdown) + one machine-stable (header or well-known). That gives us resilience when one layer is stripped.

---

## Self-updating without breaking trust

“Self-updating” is where projects accidentally become spooky. The safe pattern is: **pull-based, signed, and pinned by default**.

### A sane update model
- **Pinned default:** Sites pin to a specific manifest version (e.g., `v=0.1.0`) and only update when explicitly allowed.
- **Optional update channel:** `stable` / `candidate` / `local` channels.
- **Signed manifest:** Publish a small `rtt.manifest.json` plus a detached signature file. Local tools verify before adopting.
- **ETag/Last-Modified polling:** Cheap update checks without hammering servers.

### Manifest sketch
```json
{
  "schema": "rtt-awareness-manifest",
  "version": "0.1.0",
  "declaration": "rtt=1 | coherence=declared | drift=bounded | paradox=structural",
  "ruleset": "https://example.org/rtt/ruleset/0.1.0",
  "channel": "stable",
  "updated": "2026-02-06"
}
```

---

## Letting sites inherit RTT awareness

“Inheritance” should feel like CSS inheritance: **local overrides, upstream defaults, explicit precedence**.

### Inheritance primitives
- **Base declaration:** site-wide default in one place (header or well-known file).
- **Scoped override:** per-path or per-document overrides (meta tag in page, frontmatter in markdown).
- **Precedence order (simple and predictable):**
  1. **Document-local** (frontmatter/meta)
  2. **Path-local** (directory manifest)
  3. **Site-wide** (`/.well-known/…` or server header)
  4. **Upstream** (imported manifest)

### “Import” mechanism
Allow a site to point to an upstream canon:

- In `/.well-known/rtt-awareness`:
  `import: https://www.triadicframeworks.org/.well-known/rtt-awareness`

Then the resolver merges: upstream → local overrides. No magic—just declared composition.

---

## Tiny local resolver that simulates the full substrate

We want something that can *act like the world* locally: ingest declarations, resolve inheritance, and expose a stable view.

### Minimal architecture
- **Input adapters:** read from
  - local files/folders (docs trees)
  - HTTP headers
  - HTML meta tags
  - well-known declarations
  - manifests
- **Resolver core:** merges declarations by precedence; produces an “effective awareness” object.
- **Simulator:** represents “substrate” as a graph of regimes/contexts and runs constraint checks (drift bounds, coherence gates, recurrence assumptions).
- **Outputs:**
  - CLI summary (`rtt resolve <url-or-path>`)
  - local web UI (optional)
  - JSON export for other tools

### Concrete lowest-friction implementation
- **Local reverse proxy** (single binary/script) that:
  - fetches a page
  - reads headers + HTML meta
  - computes effective RTT awareness
  - optionally injects a small “awareness panel” into the HTML *only on localhost*
- Or **browser extension** that does the same resolution in-page (no server changes required).

### Effective resolution object
```json
{
  "effective_declaration": {
    "rtt": "1",
    "coherence": "declared",
    "drift": "bounded",
    "paradox": "structural"
  },
  "sources": [
    {"type": "well-known", "uri": "https://site/.well-known/rtt-awareness"},
    {"type": "meta", "uri": "https://site/page"}
  ],
  "version": "0.1.0"
}
```

---

## Pairing: **browser extension (observer)** + **`/.well-known/` (carrier)**

This keeps RTT awareness **pull-based, local-first, opt-in, and reversible**—no platform permissions required beyond what a user installs.

---

# Carrier: `/.well-known/rtt-awareness`

## File format v0

Plain text is the most resilient across hosts/CDNs and easiest to debug:

```text
schema: rtt-awareness
version: 0.1.0
declaration: rtt=1 | coherence=declared | drift=bounded | paradox=structural
channel: stable
updated: 2026-02-06

# optional inheritance
import: https://www.triadicframeworks.org/.well-known/rtt-awareness

# optional scoping (prefix match)
scope /docs/: rtt=1 | coherence=declared | drift=bounded | paradox=structural
scope /labs/: rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

### Inheritance semantics
- **Upstream first**, then local overrides.
- **Local scope overrides** beat site root.
- **Page-level meta** (if we later add it) beats everything.

---

# Self-updating: safe-by-default update model

Because the extension is local, “self-updating” really means: *the extension periodically re-reads the site’s own well-known file* plus any declared imports.

## Rules
- **Default is pinned:** honor whatever `version:` is returned; do not “upgrade” semantics automatically.
- **Channel only selects *which* manifest we fetch**, not what we interpret.
- **Caching:** store `(url, etag, lastModified, fetchedAt, parsedManifest)` and revalidate with conditional requests.
- **Failure mode:** if fetch fails, keep last-known-good and mark status stale.

This makes the system behave like DNS caching: stable, conservative, and predictable.
