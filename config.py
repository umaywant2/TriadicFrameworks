"""
config.py — TriadicFrameworks SSG Configuration 
================================================
Single source of truth for every build-time setting.

Import contract (consumed verbatim by build.py):
    BASE_URL          DOCS_DIR          EXCLUDE_FILES
    INDEX_PRIORITY    LANG              MARKDOWN_EXT_CONFIGS
    MARKDOWN_EXTENSIONS               OG_IMAGE
    RTT_DEFAULTS      RTT_FRONTMATTER_MAP
    SITE_AUTHOR       SITE_DESCRIPTION  SITE_DIR
    SITE_NAME         SITEMAP_CHANGEFREQ SITEMAP_PRIORITY
    STATIC_DIR        TEMPLATE_DIR      TWITTER_HANDLE

Every string setting that is likely to differ between local dev and CI/CD
can be overridden by setting the corresponding environment variable before
running build.py.  Path settings (DOCS_DIR, SITE_DIR, etc.) are always
resolved relative to this file — never override them with env vars, because
absolute paths break portability across machines and containers.

Quick-start override examples (shell / GitHub Actions env:):
    BASE_URL=https://www.triadicframeworks.org python build.py
    SITE_NAME="TF Docs"  python build.py --clean
"""

from __future__ import annotations

import os
from pathlib import Path

# ─────────────────────────────────────────────────────────────────────────────
# §1  Repo root — anchor for all relative paths
# ─────────────────────────────────────────────────────────────────────────────

# config.py lives at the repo root, so its parent IS the root.
_ROOT: Path = Path(__file__).parent.resolve()


# ─────────────────────────────────────────────────────────────────────────────
# §2  Site Identity
# ─────────────────────────────────────────────────────────────────────────────

SITE_NAME: str = os.getenv("SITE_NAME", "TriadicFrameworks")
"""
Human-readable site name.  Appears in:
  <title>, <header>, og:site_name, twitter:site, site footer.
"""

SITE_DESCRIPTION: str = os.getenv(
    "SITE_DESCRIPTION",
    "Structured methodology for building coherent, traceable, and composable systems.",
)
"""
Default meta description used on pages that declare no description in their
front matter, and on the index landing page.
"""

SITE_AUTHOR: str = os.getenv("SITE_AUTHOR", "TriadicFrameworks Contributors")
"""
Value of <meta name="author">.  Also used as the JSON-LD author name when
schema.org markup is added to templates.
"""

LANG: str = os.getenv("SITE_LANG", "en")
"""
BCP-47 language tag written to <html lang="…">.  Used by screen readers and
search-engine language clustering.  Examples: "en", "en-US", "fr", "de".
"""

TWITTER_HANDLE: str = os.getenv("TWITTER_HANDLE", "@NawderLoswin")
"""
Value of <meta name="twitter:site">.  Must include the leading @ symbol.
Leave the env var blank ("") to suppress the tag without modifying this file.
"""


# ─────────────────────────────────────────────────────────────────────────────
# §3  URLs
# ─────────────────────────────────────────────────────────────────────────────

BASE_URL: str = os.getenv(
    "BASE_URL",
    "https://www.triadicframeworks.org",
).rstrip("/")
"""
Root URL of the deployed site — no trailing slash.

Used to construct:
  - Canonical URLs  (<link rel="canonical">)
  - Open Graph og:url / og:image absolute references
  - Sitemap <loc> entries
  - robots.txt Sitemap: directive
  - "Edit on GitHub" source links

Local dev: leave at default or set BASE_URL=http://localhost:8000
CI/CD:     set BASE_URL to the production origin in workflow env vars.
"""

OG_IMAGE: str = os.getenv(
    "OG_IMAGE",
    f"{BASE_URL}/static/og-default.png",
)
"""
Absolute URL of the fallback Open Graph image.  Pages that declare an
og_image in front matter will override this value per-page (requires a
custom template block — see base.html).

Minimum recommended dimensions: 1200×630 px, < 8 MB.
"""


# ─────────────────────────────────────────────────────────────────────────────
# §4  Filesystem Paths
#     All resolved relative to _ROOT so the build works from any CWD.
# ─────────────────────────────────────────────────────────────────────────────

DOCS_DIR: str = str(_ROOT / "docs")
"""
Absolute path to the Markdown source directory.
build.py recursively globs *.md under this directory.
"""

SITE_DIR: str = str(_ROOT / "site")
"""
Absolute path to the build output directory.
Created automatically if absent; wiped by --clean.
Never commit this directory — add site/ to .gitignore.
"""

TEMPLATE_DIR: str = str(_ROOT / "templates")
"""
Absolute path to the Jinja2 template directory.
Required files: base.html, page.html, index.html.
build.py validates their presence at startup.
"""

STATIC_DIR: str = str(_ROOT / "static")
"""
Absolute path to the static-asset source directory.
Contents are mirrored verbatim to site/static/ at the end of each build.
If this directory is absent the build continues and creates an empty
site/static/ so <link href="…/static/style.css"> tags never 404.
"""


# ─────────────────────────────────────────────────────────────────────────────
# §5  Build Exclusions
# ─────────────────────────────────────────────────────────────────────────────

EXCLUDE_FILES: frozenset[str] = frozenset({
    # Repository meta-docs — not part of the public site
    "readme.md",
    "license.md",
    "contributing.md",
    "changelog.md",
    "authors.md",
    "code_of_conduct.md",
    # Template / scaffold placeholders
    "_template.md",
    "_draft.md",
})
"""
Lowercase filenames (basename only) that build.py silently skips.
Comparison is case-insensitive: CHANGELOG.MD and Changelog.md both match.
"""


# ─────────────────────────────────────────────────────────────────────────────
# §6  Sitemap Settings
# ─────────────────────────────────────────────────────────────────────────────

SITEMAP_CHANGEFREQ: str = "weekly"
"""
Default <changefreq> for content pages in sitemap.xml.
Valid values (sitemaps.org): always | hourly | daily | weekly | monthly |
yearly | never.  The index page always uses "daily" regardless of this value.
"""

SITEMAP_PRIORITY: str = "0.8"
"""
Default <priority> for content pages.  Range: 0.0–1.0 as a string.
The index page always uses INDEX_PRIORITY (1.0) regardless of this value.
"""

INDEX_PRIORITY: str = "1.0"
"""
<priority> for the site index (/) in sitemap.xml.
Kept separate so the index can be boosted independently of content pages.
"""


# ─────────────────────────────────────────────────────────────────────────────
# §7  Markdown Extensions
#     Passed verbatim to markdown.Markdown(extensions=…, extension_configs=…).
#     Extension names must match the registered entry-point names in the
#     python-markdown package (verified against markdown>=3.5).
# ─────────────────────────────────────────────────────────────────────────────

MARKDOWN_EXTENSIONS: list[str] = [
    "extra",         # Tables, footnotes, attribute lists, abbreviations,
                     # definition lists, fenced code (superset of fenced_code).
    "codehilite",    # Pygments-powered syntax highlighting for indented
                     # and fenced code blocks.
    "toc",           # Auto-generates a table of contents; exposes md.toc
                     # (HTML string) and md.toc_tokens (list) after convert().
    "meta",          # Reads legacy "key: value" front-matter (no fences).
                     # Harmless when YAML front matter is stripped first by
                     # build.py — the extension finds nothing and sets md.Meta={}.
    "nl2br",         # Converts single newlines in paragraphs to <br>.
    "sane_lists",    # Prevents mixed ordered/unordered list types from merging.
    "smarty",        # Converts straight quotes → curly, -- → en-dash, etc.
    "admonition",    # !!! note / !!! warning / !!! tip callout blocks.
]

MARKDOWN_EXT_CONFIGS: dict[str, dict] = {
    "codehilite": {
        "guess_lang":    False,
        "linenums":      False,
        "css_class":     "codehilite",
        "pygments_style":"default",
        "noclasses":     False,
    },
    "toc": {
        "permalink":       True,
        "permalink_class": "toc-permalink",
        "permalink_title": "Permanent link to this heading",
        "title":           "Contents",
        "toc_depth":       "2-3",
    },
    "smarty": {
        "smart_dashes":        True,
        "smart_quotes":        True,
        "smart_ellipses":      True,
        "smart_angled_quotes": False,
    },
}


# ─────────────────────────────────────────────────────────────────────────────
# §8  RTT (Round-Trip Traceability) Schema
# ─────────────────────────────────────────────────────────────────────────────

RTT_DEFAULTS: dict[str, str] = {
    "rtt:schema-version": "1.0",

    "rtt:source-repo": "https://github.com/umaywant2/TriadicFrameworks",
    # ⚠ MUST be present — build.py reads this key directly to construct
    #   SOURCE_EDIT_BASE and <meta name="source:repo">.

    "rtt:content-type": "documentation",
    # Allowed: documentation | reference | guide | tutorial | changelog | policy

    "rtt:stability": "draft",
    # ⚠ MUST be present — build.py reads this key as the draft-filter fallback.
    # Allowed: draft | stable | deprecated
    # Rendered as a coloured badge in the article header (style.css).

    "rtt:audience": "public",
    # Allowed: public | internal | partner | maintainer

    "rtt:review-cycle": "quarterly",
    # Allowed: continuous | monthly | quarterly | biannual | annual | on-change

    "rtt:owner": "core-team",
    # Freeform; per-page front matter should always override this default.
}

RTT_FRONTMATTER_MAP: dict[str, str] = {
    # ── Mirrors of RTT_DEFAULTS (overridable per-page) ────────────────────────
    "rtt_schema_version": "rtt:schema-version",
    "rtt_source_repo":    "rtt:source-repo",
    "rtt_content_type":   "rtt:content-type",
    "rtt_stability":      "rtt:stability",
    "rtt_audience":       "rtt:audience",
    "rtt_review_cycle":   "rtt:review-cycle",
    "rtt_owner":          "rtt:owner",

    # ── Per-page-only fields (no site-wide default) ───────────────────────────
    "rtt_doc_id":        "rtt:doc-id",
    # Unique document identifier.  Convention: DOC-NNN (zero-padded).

    "rtt_last_reviewed": "rtt:last-reviewed",
    # ISO 8601 date of the most recent editorial review.

    "rtt_tags":          "rtt:tags",
    # YAML list or comma-separated string; joined with ", " in output.
    # e.g.  rtt_tags: [triadic, concepts]  →  content="triadic, concepts"

    "rtt_superseded_by": "rtt:superseded-by",
    # URL or DOC-ID of the replacement page (set when stability=deprecated).

    "rtt_related":       "rtt:related",
    # Comma-separated DOC-IDs or URLs of closely related pages.
}


# ─────────────────────────────────────────────────────────────────────────────
# §9  Derived constants (external tooling only — not imported by build.py)
# ─────────────────────────────────────────────────────────────────────────────

SOURCE_REPO: str       = RTT_DEFAULTS["rtt:source-repo"]
SOURCE_EDIT_BASE: str  = SOURCE_REPO.rstrip("/") + "/blob/main/"
SITE_URL_CANONICAL: str = BASE_URL.rstrip("/") + "/"


# ─────────────────────────────────────────────────────────────────────────────
# §10  Export declaration
# ─────────────────────────────────────────────────────────────────────────────

__all__: list[str] = [
    # Required by build.py (19 names — keep in sync with its import block)
    "BASE_URL", "DOCS_DIR", "EXCLUDE_FILES", "INDEX_PRIORITY", "LANG",
    "MARKDOWN_EXT_CONFIGS", "MARKDOWN_EXTENSIONS", "OG_IMAGE",
    "RTT_DEFAULTS", "RTT_FRONTMATTER_MAP", "SITE_AUTHOR", "SITE_DESCRIPTION",
    "SITE_DIR", "SITE_NAME", "SITEMAP_CHANGEFREQ", "SITEMAP_PRIORITY",
    "STATIC_DIR", "TEMPLATE_DIR", "TWITTER_HANDLE",
    # Convenience aliases (external tooling only)
    "SOURCE_REPO", "SOURCE_EDIT_BASE", "SITE_URL_CANONICAL",
]

