---
title: "SSG Pipeline Capture"
description: "Documents the static site generator build pipeline for TriadicFrameworks documentation."
date: "2026-07-14"
modified: "2026-07-14"
rtt_doc_id: "DOC-030"
rtt_stability: stable
rtt_layer: "T"
rtt_audience:
  - developer
  - maintainer
keywords: "SSG, static site generator, build pipeline, GitHub Pages, TriadicFrameworks"
author: "Nawder Loswin"
---

# SSG Pipeline Capture

Documents the build pipeline that converts TriadicFrameworks Markdown documentation
into a pre-rendered HTML site deployed to GitHub Pages at
`https://umaywant2.github.io/TriadicFrameworks`.

## Pipeline Overview

```
docs/*.md  ──►  build.py  ──►  site/  ──►  GitHub Pages
               (Python)        (HTML)       (OIDC deploy)
```

Three stages: **source ingestion** → **transformation** → **deployment**.

## Source Rules

| Condition | Behaviour |
|-----------|-----------|
| Filename in `EXCLUDE_FILES` | Skipped (readme.md, license.md, _template.md, etc.) |
| `rtt_stability: draft` | Skipped in production; included with `--drafts` flag |
| `docs/foo.md` | Output → `site/foo/index.html`, canonical `/foo/` |
| `docs/foo/index.md` | Output → `site/foo/index.html`, canonical `/foo/` (collapses) |

## Entry Point

```bash
python build.py [--clean] [--watch] [--file PATH] [--drafts] [--verbose]
```

| Flag | Effect |
|------|--------|
| `--clean` | Delete `site/` before building |
| `--watch` | Rebuild on file changes in docs/, templates/, static/ |
| `--file PATH` | Build a single source file only |
| `--drafts` | Include draft-stability pages |
| `--verbose` | Emit per-file debug logging |

## Per-File Transformation Steps

1. Read `.md` source file
2. Parse YAML front matter (PyYAML)
3. Merge RTT defaults + per-page front matter overrides via `RTT_FRONTMATTER_MAP`
4. Convert Markdown → HTML (8 extensions: toc, codehilite, fenced_code, tables,
   footnotes, admonition, attr_list, def_list)
5. Extract TOC as HTML string
6. Build breadcrumb trail from URL path segments
7. Resolve canonical URL, OG image, GitHub edit link
8. Render Jinja2 template (`page.html` or `index.html`)
9. Write `site/<path>/index.html`

## Output Structure

```
site/
├── index.html
├── introduction/index.html
├── concepts/triadic-model/index.html
├── reference/api/index.html
├── static/
│   ├── style.css
│   ├── favicon.svg
│   ├── favicon-32.png
│   ├── apple-touch-icon.png
│   ├── site.webmanifest
│   └── og-default.png
├── sitemap.xml
├── robots.txt
└── build-manifest.json
```

## Configuration (`config.py`)

| Setting | Default | Env-var override |
|---------|---------|-----------------|
| `BASE_URL` | `https://umaywant2.github.io/TriadicFrameworks` | `TF_BASE_URL` |
| `SITE_NAME` | `TriadicFrameworks` | `TF_SITE_NAME` |
| `SITE_AUTHOR` | `Nawder Loswin` | `TF_SITE_AUTHOR` |
| `SITE_DESCRIPTION` | *(see config.py)* | `TF_SITE_DESCRIPTION` |
| `TWITTER_HANDLE` | *(see config.py)* | `TF_TWITTER_HANDLE` |
| `OG_IMAGE` | `{BASE_URL}/static/og-default.png` | `TF_OG_IMAGE` |

## CI/CD (`.github/workflows/build.yml`)

**`build` job** — Checks out repo, installs `requirements.txt`, resolves `BASE_URL`
and `OG_IMAGE` from repository variables, runs `python build.py --clean --verbose`,
verifies output, uploads `site/` as a GitHub Pages artifact.

**`deploy` job** — Uses OIDC (`pages:write`, `id-token:write`) to deploy via
`actions/deploy-pages@v4`. Runs only on pushes to `main`.

Triggers: push to `main` (path-filtered), pull requests (build only, no deploy),
`workflow_dispatch` with optional `include_drafts` boolean input.

## RTT Metadata

Every rendered page carries RTT `<meta>` tags injected by `base.html`. Default
values are in `config.py → RTT_DEFAULTS`; per-page overrides map via
`RTT_FRONTMATTER_MAP` (12 field mappings).

RTT session string declared on every page:

```
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

## Dependencies

```
markdown>=3.5,<4        # Markdown → HTML + 8 extensions
PyYAML>=6.0,<7          # Front matter parsing
Jinja2>=3.1,<4          # HTML templating
Pygments>=2.17,<3       # Syntax highlighting (codehilite)
watchdog>=4.0,<5        # File watching (--watch mode only)
```

Install: `pip install -r requirements.txt`

---

*© 2026 Byte Books Publishing · LCCN 2026917007 · Author: Nawder Loswin*
