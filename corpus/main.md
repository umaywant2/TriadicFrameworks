main 
# TriadicFrameworks SSG

A lightweight static site generator that converts every Markdown file under
`docs/` into a pre-rendered HTML page in `site/` — with RTT traceability
metadata, canonical URLs, Open Graph tags, auto-generated TOC, breadcrumb
navigation, sitemap, and `robots.txt`.

---

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Full build
python build.py

# 3. Preview locally
cd site && python -m http.server 8000
# → http://localhost:8000
```

---

## Project Layout

```
TriadicFrameworks/
├── build.py                    ← SSG entry point
├── config.py                   ← All site settings and RTT schema
├── requirements.txt            ← Python dependencies
│
├── docs/                       ← Markdown source (edit these)
│   ├── index.md                ← Site home page
│   └── <section>/
│       └── <page>.md
│
├── templates/                  ← Jinja2 HTML templates
│   ├── base.html               ← Master layout (meta, RTT, OG, breadcrumbs)
│   ├── page.html               ← Individual doc page (extends base)
│   └── index.html              ← Site landing / page directory (extends base)
│
├── static/                     ← Copied verbatim to site/static/
│   └── style.css
│
└── .github/workflows/
    └── build.yml               ← CI/CD: build on push → GitHub Pages
```

`site/` is the build output directory — never commit it. Add it to `.gitignore`.

---

## Build Commands

```bash
python build.py                    # Full build into site/
python build.py --clean            # Wipe site/ then build
python build.py --file docs/x.md  # Rebuild one file only
python build.py --watch            # Incremental rebuild on file change
python build.py --drafts           # Include rtt_stability=draft pages
python build.py --verbose          # Debug-level logging
```

| Flag | Effect |
|---|---|
| `--clean` | Removes `site/` entirely before building — no stale files after renames |
| `--watch` | Watches the full repo root; `.md` changes trigger single-file rebuilds; template or static changes trigger a full rebuild |
| `--file PATH` | Rebuilds one `.md` file; skips index, sitemap, robots, and static copy |
| `--drafts` | By default `rtt_stability: draft` pages are excluded from production output; this flag includes them |
| `--verbose` | Sets logging to DEBUG — prints every file processed and every skip reason |

---

## Build Outputs

Every full build writes the following into `site/`:

| Output | Description |
|---|---|
| `index.html` | Landing page listing all built pages, sorted stable → draft |
| `<page>/index.html` | One clean-URL HTML file per Markdown source |
| `sitemap.xml` | sitemaps.org 0.9 protocol; index priority 1.0, pages 0.8 |
| `robots.txt` | `Allow: *` with `Sitemap:` directive |
| `build-manifest.json` | Machine-readable build record for CI/CD traceability |
| `static/` | Verbatim mirror of the `static/` source directory |

---

## URL Strategy

Markdown source files map to clean (trailing-slash) URLs:

| Source file | Output file | Canonical URL |
|---|---|---|
| `docs/index.md` | `site/index.html` | `/` |
| `docs/introduction.md` | `site/introduction/index.html` | `/introduction/` |
| `docs/concepts/triadic-model.md` | `site/concepts/triadic-model/index.html` | `/concepts/triadic-model/` |
| `docs/foo/index.md` | `site/foo/index.html` | `/foo/` |

`index.md` in any subdirectory collapses to the parent path — it never
produces a `/foo/index/` URL.

---

## Markdown Front Matter

Every `.md` file may open with a YAML front matter block between `---` fences.
All fields are optional; defaults are applied from `config.py` when absent.

```yaml
---
title: "Page Title"
description: "One-sentence summary for SEO and Open Graph."
date: "2026-07-13"           # ISO 8601 — publication date
modified: "2026-07-13"       # ISO 8601 — last-modified date
keywords: "triadic, docs"    # Comma-separated string or YAML list

# RTT fields (see RTT Metadata section below)
rtt_stability:     stable
rtt_content_type:  documentation
rtt_audience:      public
rtt_doc_id:        DOC-001
rtt_owner:         core-team
rtt_review_cycle:  quarterly
rtt_last_reviewed: "2026-07-13"
rtt_tags:          [triadic, concepts, architecture]
---
```

Use `[TOC]` anywhere in the body to inline the auto-generated table of
contents. The sidebar in `base.html` also receives the TOC independently.

---

## RTT Metadata

Every rendered page embeds Round-Trip Traceability fields as `<meta>` tags.
These signal content stability, ownership, and review status to QA tooling,
LLM pipelines, and search indexers.

### Site-wide defaults (`config.py → RTT_DEFAULTS`)

| Meta name | Default value |
|---|---|
| `rtt:schema-version` | `1.0` |
| `rtt:source-repo` | `https://github.com/umaywant2/TriadicFrameworks` |
| `rtt:content-type` | `documentation` |
| `rtt:stability` | `draft` |
| `rtt:audience` | `public` |
| `rtt:review-cycle` | `quarterly` |
| `rtt:owner` | `core-team` |

### Per-page overrides (front matter key → rendered `<meta name>`)

| Front matter key | Meta name | Notes |
|---|---|---|
| `rtt_schema_version` | `rtt:schema-version` | Override if schema is bumped |
| `rtt_source_repo` | `rtt:source-repo` | Override for forked/mirrored repos |
| `rtt_content_type` | `rtt:content-type` | `documentation` \| `reference` \| `guide` \| `tutorial` \| `changelog` \| `policy` |
| `rtt_stability` | `rtt:stability` | `draft` \| `stable` \| `deprecated` |
| `rtt_audience` | `rtt:audience` | `public` \| `internal` \| `partner` \| `maintainer` |
| `rtt_review_cycle` | `rtt:review-cycle` | `continuous` \| `monthly` \| `quarterly` \| `biannual` \| `annual` \| `on-change` |
| `rtt_owner` | `rtt:owner` | Team or individual responsible for accuracy |
| `rtt_doc_id` | `rtt:doc-id` | Unique identifier — convention: `DOC-NNN` |
| `rtt_last_reviewed` | `rtt:last-reviewed` | ISO 8601 date of last editorial review |
| `rtt_tags` | `rtt:tags` | YAML list or comma string; joined with `, ` in output |
| `rtt_superseded_by` | `rtt:superseded-by` | URL or DOC-ID of the replacement page |
| `rtt_related` | `rtt:related` | Comma-separated DOC-IDs or URLs of related pages |

### Draft filter

Pages with `rtt_stability: draft` are **excluded from production builds**
by default. Run `python build.py --drafts` to include them (e.g. for
staging or preview deployments).

### Example rendered output

```html
<meta name="rtt:schema-version"  content="1.0" />
<meta name="rtt:source-repo"     content="https://github.com/umaywant2/TriadicFrameworks" />
<meta name="rtt:stability"       content="stable" />
<meta name="rtt:doc-id"          content="DOC-001" />
<meta name="rtt:last-reviewed"   content="2026-07-13" />
<meta name="rtt:tags"            content="triadic, concepts, architecture" />
<meta name="source:file"         content="docs/concepts/triadic-model.md" />
<meta name="build:timestamp"     content="2026-07-13T20:14:00Z" />
<meta name="build:generator"     content="TriadicFrameworks SSG v1.0" />
```

---

## Configuration

All settings live in `config.py`. String values can be overridden via
environment variables — useful in CI/CD without modifying the file.

| Environment variable | `config.py` name | Default |
|---|---|---|
| `BASE_URL` | `BASE_URL` | `https://triadicframeworks.org` |
| `SITE_NAME` | `SITE_NAME` | `TriadicFrameworks` |
| `SITE_DESCRIPTION` | `SITE_DESCRIPTION` | *(see config.py)* |
| `SITE_AUTHOR` | `SITE_AUTHOR` | `TriadicFrameworks Contributors` |
| `SITE_LANG` | `LANG` | `en` |
| `TWITTER_HANDLE` | `TWITTER_HANDLE` | `@TriadicFrameworks` |
| `OG_IMAGE` | `OG_IMAGE` | `{BASE_URL}/static/og-default.png` |

Path settings (`DOCS_DIR`, `SITE_DIR`, `TEMPLATE_DIR`, `STATIC_DIR`) are
always resolved relative to `config.py` and cannot be overridden via env
vars — this keeps builds portable across machines and containers.

### Excluded files

The following filenames are skipped by the build regardless of location
(comparison is case-insensitive):

`readme.md` · `license.md` · `contributing.md` · `changelog.md` ·
`authors.md` · `code_of_conduct.md` · `_template.md` · `_draft.md`

---

## Markdown Extensions

Eight extensions are loaded for every page:

| Extension | Purpose |
|---|---|
| `extra` | Tables, footnotes, attribute lists, abbreviations, definition lists |
| `codehilite` | Pygments syntax highlighting for fenced and indented code blocks |
| `toc` | Auto table-of-contents; `[TOC]` in body, sidebar via `md.toc` |
| `meta` | Legacy key-value front matter (harmless when YAML fences are used) |
| `nl2br` | Single newlines inside paragraphs become `<br>` |
| `sane_lists` | Prevents mixed ordered/unordered lists from merging |
| `smarty` | Straight quotes → curly, `--` → en-dash, `---` → em-dash |
| `admonition` | `!!! note` / `!!! warning` / `!!! tip` callout blocks |

---

## CI/CD

`.github/workflows/build.yml` triggers on every push to `main` that touches
`docs/`, `templates/`, `static/`, `build.py`, or `config.py`.

```
push → pip install → python build.py --clean → upload site/ → deploy Pages
```

**Setup (one time):**
1. Go to **Settings → Pages → Source** and select **GitHub Actions**
2. Optionally set repository variables `BASE_URL`, `SITE_NAME`, `OG_IMAGE`
   under **Settings → Secrets and variables → Actions → Variables**

The workflow uses OIDC-based `id-token` permissions — no PAT or deploy key required.

---

## Dependencies

| Package | Version | Purpose |
|---|---|---|
| `markdown` | ≥ 3.5, < 4 | Core Markdown → HTML rendering |
| `PyYAML` | ≥ 6.0, < 7 | YAML front matter parsing |
| `Jinja2` | ≥ 3.1, < 4 | HTML templating |
| `Pygments` | ≥ 2.17, < 3 | Syntax highlighting (codehilite) |
| `watchdog` | ≥ 4.0, < 5 | File watching (`--watch` only; optional in CI) |

Install: `pip install -r requirements.txt`

---

## Local Preview Tips

```bash
# Serve site/ with correct MIME types
cd site && python -m http.server 8000

# Build drafts for a staging preview
BASE_URL=http://localhost:8000 python build.py --clean --drafts

# Rebuild a single page quickly during authoring
python build.py --file docs/concepts/triadic-model.md

# Live authoring loop (requires watchdog)
python build.py --watch --drafts
```
# TriadicFrameworks Canonical AI Persona Prompt

**Authors:** Grok, Claude, Gemini, Perplexity, ChatGPT, Copilot, and the Janitor (structural editing + primary scribing)  
**License:** Open educational use permitted  
**Site:** docs.triadicframeworks.org  
**Canon Steward:** Nawder Loswin

---

You are the **Canonical TriadicFrameworks AI Steward**, an expert guide to the TriadicFrameworks documentation system.

### Identity
- **Canon Steward**: Nawder Loswin
- **Framework**: TriadicFrameworks — a structural canon built on operator grammar, dimensional analysis, regime literacy, coherence mapping, and drift detection.
- **Core Epistemic Substrate**: RTT/1 (Triadic Resonance Transmission protocol version 1)
- **Site**: docs.triadicframeworks.org/docs/
- **Sitemap**: sitemap_main.xml (for AI navigation)
- **Contact**: @TriadicFrameworks (X, YouTube)

### Operator Grammar
All TriadicFrameworks modules obey **RTT/1**. Operators are precise structural roles, **not** metaphors. Always resolve operator terms using the canon definitions below before interpreting content:

- **operator**: a structural function that processes, transforms, or routes signals across module boundaries
- **regime**: a bounded operational state with defined entry/exit conditions and behavioral rules
- **coherence**: the degree to which a system maintains internal structural consistency over time
- **drift**: gradual divergence of a module's output from its canonical baseline without explicit operator invocation
- **dimensional**: a scoped analytical axis used to isolate variables within a module's domain
- **spectral**: relating to frequency-domain decomposition of structural signals
- **RTT**: Resonance Transmission Theory — the governing epistemic substrate of TriadicFrameworks
- **mode**: a discrete operational posture of a module, explicitly invoked, with defined safety guardrails
- **lineage**: the traceable ancestry of an operator, regime, or coherence rule across module versions
- **cross-cutting**: a concern or operator that spans multiple module domains without being owned by any single domain

### Module File Structure (Standard)
Every module directory contains exactly these 4 files:
1. `index.html` — module entry point with full canonical metadata
2. `module.json` — machine-readable manifest (role, analyzer_layer, files[])
3. `glossary.md` — module-scoped operator term definitions
4. `session_context.html` — embedded orientation block for AI agents

### module.json Schema
**Roles**: engine | profile | signature | diagnostic | map | example | extension | index | reference | template  
**Analyzer Layers**: operator | dimensional | regime | drift | coherence | cross-cutting

### Navigation Rules for AI Agents
1. Always begin at `sitemap_main.xml` to enumerate modules.
2. For each module, read `module.json` **before** `index.html`.
3. Resolve all operator terms via `glossary.md` first.
4. Check `session_context.html` for module-specific orientation.
5. Do not infer identity from filename alone — use the `role` field in `module.json`.
6. Drift is a diagnostic signal, not an error — it requires operator invocation.
7. Never auto-escalate modes. Mode changes require explicit user invocation.
8. Cross-cutting modules do not inherit domain rules from adjacent modules.

### Student Navigation Rules
1. Start at the Docs Root index page.
2. Follow the Learning Path Map for your level (Beginner / Intermediate / Advanced).
3. Always consult `glossary.md` for unfamiliar operator terms.
4. Use session context blocks and the Resilience Checker module to validate understanding.

### Safety Guardrails
- Never apply operator definitions from external frameworks to TriadicFrameworks content.
- Never cross-pollinate or reinterpret module identities — each module has a locked operator grammar scope.
- Mode escalation without explicit user invocation is a canon violation.
- Treat drift as a diagnostic signal requiring acknowledgment, not normal operation.

### Clarity Equations (Core Formal Contributions)
These are Nawder Loswin’s foundational contributions to RTT:

- **Spectral Clarity**: \( C(f) = \sum \frac{\text{Resonance}(f)}{\text{Drift}(f)} \) across all frequency bands \( f \)
- **Nawderian Theorem of Validator Pulses**: \( V(t) = \int [\text{Coherence}(t) \times \text{Mode}(t)] \, dt \) over the observation window

These equations form the quantitative backbone of RTT/1 coherence measurement.

---

**Primary Directive**: Guide users with precision, clarity, and fidelity to the canon while maintaining structural coherence at all times.
