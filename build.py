#!/usr/bin/env python3
"""
build.py — TriadicFrameworks Static Site Generator
====================================================
Converts every Markdown file under docs/ into a pre-rendered HTML page in
site/, injecting the exact variable set required by:

    templates/base.html   — master layout
    templates/page.html   — individual doc page  (extends base)
    templates/index.html  — site landing/directory (extends base)

Variable contract (verified against templates):
  base.html  : lang, page_title, site_name, description, author, keywords,
               canonical_url, og_image, date, modified, twitter_handle,
               rtt_fields {dict}, source_file, source_repo, build_timestamp,
               build_year, base_url, toc, breadcrumbs [{label, url}],
               source_edit_url
  page.html  : + body
  index.html : + site_description, pages [{url, title, description,
                                           date, rtt_stability}]

Usage:
    python build.py                    # full build
    python build.py --clean            # wipe site/ then full build
    python build.py --file docs/x.md  # rebuild one file only
    python build.py --watch            # incremental on file change (watchdog)
    python build.py --drafts           # include rtt_stability=draft pages

Requirements (see requirements.txt):
    markdown>=3.5  PyYAML>=6.0  Jinja2>=3.1  Pygments>=2.17
    python-slugify>=8.0  watchdog>=4.0 (watch mode only)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import re
import shutil
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# ── Third-party (validated against requirements.txt) ─────────────────────────
try:
    import markdown
    import yaml
    from jinja2 import Environment, FileSystemLoader, select_autoescape, TemplateNotFound
except ImportError as exc:
    sys.exit(
        f"❌ Missing dependency: {exc.name}\n"
        "   Run: pip install -r requirements.txt"
    )

# ── Local config ──────────────────────────────────────────────────────────────
sys.path.insert(0, str(Path(__file__).parent))
try:
    from config import (
        BASE_URL,
        DOCS_DIR,
        EXCLUDE_FILES,
        INDEX_PRIORITY,
        LANG,
        MARKDOWN_EXT_CONFIGS,
        MARKDOWN_EXTENSIONS,
        OG_IMAGE,
        RTT_DEFAULTS,
        RTT_FRONTMATTER_MAP,
        SITE_AUTHOR,
        SITE_DESCRIPTION,
        SITE_DIR,
        SITE_NAME,
        SITEMAP_CHANGEFREQ,
        SITEMAP_PRIORITY,
        STATIC_DIR,
        TEMPLATE_DIR,
        TWITTER_HANDLE,
    )
except ImportError:
    sys.exit("❌ config.py not found — run build.py from the repo root.")


# ─────────────────────────────────────────────────────────────────────────────
# Logging
# ─────────────────────────────────────────────────────────────────────────────

LOG_FORMAT = "%(levelname)-8s %(message)s"
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO)
log = logging.getLogger("ssg")


# ─────────────────────────────────────────────────────────────────────────────
# Build-time constants
# ─────────────────────────────────────────────────────────────────────────────

BUILD_TIMESTAMP: str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
BUILD_YEAR:      int = datetime.now(timezone.utc).year

# GitHub edit link base — resolves to the raw file in the default branch
_REPO_ROOT       = RTT_DEFAULTS.get("rtt:source-repo", "").rstrip("/")
SOURCE_EDIT_BASE = f"{_REPO_ROOT}/blob/main/"

# YAML front-matter fence
_FM_RE = re.compile(r"^---[ \t]*\r?\n(.*?)\r?\n---[ \t]*\r?\n", re.DOTALL)


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def _parse_front_matter(text: str) -> tuple[dict[str, Any], str]:
    """
    Split YAML front matter from Markdown source.

    Returns:
        (meta_dict, body_without_fence)

    The regex accepts both LF and CRLF line endings and tolerates trailing
    whitespace on the fence lines.  An invalid YAML block logs a warning and
    returns an empty dict rather than raising.
    """
    m = _FM_RE.match(text)
    if not m:
        return {}, text
    try:
        meta = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as exc:
        log.warning("  ⚠  YAML parse error in front matter: %s", exc)
        meta = {}
    if not isinstance(meta, dict):
        log.warning("  ⚠  Front matter is not a mapping — ignoring.")
        meta = {}
    return meta, text[m.end():]


def _render_markdown(source: str) -> tuple[str, str]:
    """
    Render Markdown → HTML.

    Returns:
        (html_body, toc_html)   — toc_html is "" when no [TOC] marker exists.

    A fresh Markdown instance is created per page so that extension state
    (e.g. the TOC tree) never bleeds between files.
    """
    md   = markdown.Markdown(
        extensions=MARKDOWN_EXTENSIONS,
        extension_configs=MARKDOWN_EXT_CONFIGS,
    )
    html = md.convert(source)
    toc  = getattr(md, "toc", "")
    # Strip the toc wrapper when it contains no actual items (empty doc case)
    if toc and toc.strip() in ('<div class="toc">\n</div>', ""):
        toc = ""
    return html, toc


def _url_path(md_path: Path, docs_root: Path) -> str:
    """
    Map a docs-relative Markdown path to a clean URL path.

        docs/index.md                  →  /
        docs/introduction.md           →  /introduction/
        docs/concepts/triadic-model.md →  /concepts/triadic-model/

    Leading slash always present; trailing slash always present.
    """
    rel   = md_path.relative_to(docs_root)
    parts = list(rel.with_suffix("").parts)   # drop .md

    if parts[-1].lower() == "index":
        parts.pop()                           # docs/foo/index.md → /foo/

    if not parts:
        return "/"
    return "/" + "/".join(parts) + "/"


def _output_path(url_path: str, site_dir: Path) -> Path:
    """
    Translate a clean URL path to an output filesystem path.

        /                         →  site/index.html
        /introduction/            →  site/introduction/index.html
        /concepts/triadic-model/  →  site/concepts/triadic-model/index.html
    """
    clean = url_path.strip("/")
    if clean:
        return site_dir / clean / "index.html"
    return site_dir / "index.html"


def _canonical(url_path: str) -> str:
    """Absolute canonical URL for a given path."""
    base = BASE_URL.rstrip("/")
    if url_path == "/":
        return base + "/"
    return base + url_path


def _breadcrumbs(url_path: str) -> list[dict[str, str]]:
    """
    Build the breadcrumb trail for a page.

    Always starts with Home.  Intermediate segments link to their own
    canonical URL; the final segment has an empty url (current page).

    Example:
        /concepts/triadic-model/  →
            [
                {"label": "Home",          "url": "https://…/"},
                {"label": "Concepts",      "url": "https://…/concepts/"},
                {"label": "Triadic Model", "url": ""},
            ]
    """
    base   = BASE_URL.rstrip("/")
    crumbs: list[dict[str, str]] = [{"label": "Home", "url": base + "/"}]

    parts = [p for p in url_path.strip("/").split("/") if p]
    for i, part in enumerate(parts):
        label   = part.replace("-", " ").replace("_", " ").title()
        is_last = i == len(parts) - 1
        url     = "" if is_last else base + "/" + "/".join(parts[: i + 1]) + "/"
        crumbs.append({"label": label, "url": url})

    return crumbs


def _collect_rtt(meta: dict[str, Any]) -> dict[str, str]:
    """
    Merge site-wide RTT defaults with per-page front matter overrides.

    Front matter keys use underscores (rtt_stability) and map to
    colon-namespaced meta names (rtt:stability) via RTT_FRONTMATTER_MAP.
    List values are joined with ", " for a single <meta content> attribute.
    """
    rtt = dict(RTT_DEFAULTS)
    for fm_key, meta_name in RTT_FRONTMATTER_MAP.items():
        if fm_key not in meta:
            continue
        value = meta[fm_key]
        if isinstance(value, list):
            value = ", ".join(str(v) for v in value)
        rtt[meta_name] = str(value)
    return rtt


def _coerce_str(value: Any) -> str:
    """Convert any scalar to str; return '' for None/missing."""
    if value is None:
        return ""
    if isinstance(value, list):
        return ", ".join(str(v) for v in value)
    return str(value)


def _sha1(path: Path) -> str:
    """8-char SHA-1 of file content for incremental-build cache keys."""
    h = hashlib.sha1(usedforsecurity=False)
    h.update(path.read_bytes())
    return h.hexdigest()[:8]


# ─────────────────────────────────────────────────────────────────────────────
# Jinja2 environment factory
# ─────────────────────────────────────────────────────────────────────────────

def _make_jinja_env() -> Environment:
    """
    Construct the Jinja2 environment.

    - autoescape enabled for HTML files only.
    - trim_blocks / lstrip_blocks keep template output whitespace-clean.
    - Custom 'slugify' filter available in all templates.
    """
    env = Environment(
        loader        = FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape    = select_autoescape(["html"]),
        trim_blocks   = True,
        lstrip_blocks = True,
    )
    env.filters["slugify"] = lambda s: re.sub(r"[^\w-]", "-", s.lower()).strip("-")
    return env


# ─────────────────────────────────────────────────────────────────────────────
# Shared template context
# ─────────────────────────────────────────────────────────────────────────────

def _site_ctx() -> dict[str, Any]:
    """
    Return the portion of the Jinja2 context that is identical for every page.
    Centralising these values eliminates the most common class of
    'UndefinedError' bugs caused by missing keys in individual render calls.
    """
    return {
        "site_name":        SITE_NAME,
        "site_description": SITE_DESCRIPTION,
        "author":           SITE_AUTHOR,
        "lang":             LANG,
        "base_url":         BASE_URL.rstrip("/"),
        "og_image":         OG_IMAGE,
        "twitter_handle":   TWITTER_HANDLE,
        "build_timestamp":  BUILD_TIMESTAMP,
        "build_year":       BUILD_YEAR,
        "source_repo":      _REPO_ROOT,
    }


# ─────────────────────────────────────────────────────────────────────────────
# Single-page builder
# ─────────────────────────────────────────────────────────────────────────────

def build_page(
    md_path:        Path,
    docs_root:      Path,
    site_dir:       Path,
    jinja_env:      Environment,
    *,
    include_drafts: bool = True,
) -> dict[str, Any] | None:
    """
    Render one Markdown file to HTML and write it to site/.

    Returns a page record on success, or None when the file is excluded/skipped.

    Page record schema
    ------------------
    url           str  absolute canonical URL
    url_path      str  root-relative path, e.g. /concepts/triadic-model/
    title         str
    description   str
    date          str  ISO 8601 or ""
    modified      str  ISO 8601 or ""
    source_file   str  docs-relative path, e.g. concepts/triadic-model.md
    rtt_stability str  draft | stable | deprecated
    """
    rel_path = md_path.relative_to(docs_root)

    # ── Exclusion ─────────────────────────────────────────────────────────────
    if md_path.name.lower() in EXCLUDE_FILES:
        log.debug("  skip (excluded)  %s", rel_path)
        return None

    # ── Read ──────────────────────────────────────────────────────────────────
    try:
        raw = md_path.read_text(encoding="utf-8")
    except OSError as exc:
        log.error("  ✗ cannot read %s: %s", rel_path, exc)
        return None

    meta, body_md = _parse_front_matter(raw)

    # ── Draft filter ──────────────────────────────────────────────────────────
    stability = str(meta.get("rtt_stability", RTT_DEFAULTS.get("rtt:stability", "draft")))
    if stability == "draft" and not include_drafts:
        log.info("  skip (draft)     %s", rel_path)
        return None

    log.info("  build            %s", rel_path)

    # ── URL plumbing ──────────────────────────────────────────────────────────
    url_path_str  = _url_path(md_path, docs_root)
    out_path      = _output_path(url_path_str, site_dir)
    canonical_url = _canonical(url_path_str)
    breadcrumbs   = _breadcrumbs(url_path_str)

    # ── Markdown render ───────────────────────────────────────────────────────
    body_html, toc_html = _render_markdown(body_md)

    # ── Front matter ──────────────────────────────────────────────────────────
    page_title  = _coerce_str(meta.get("title")) or \
                  md_path.stem.replace("-", " ").replace("_", " ").title()
    description = _coerce_str(meta.get("description") or meta.get("summary")) \
                  or SITE_DESCRIPTION
    date        = _coerce_str(meta.get("date"))
    modified    = _coerce_str(meta.get("modified") or meta.get("last_modified"))
    keywords    = _coerce_str(meta.get("keywords"))

    # ── RTT ───────────────────────────────────────────────────────────────────
    rtt_fields = _collect_rtt(meta)

    # ── Source edit link ──────────────────────────────────────────────────────
    source_file_rel = str(rel_path).replace("\\", "/")
    source_edit_url = SOURCE_EDIT_BASE + "docs/" + source_file_rel

    # ── Template context ──────────────────────────────────────────────────────
    ctx: dict[str, Any] = {
        **_site_ctx(),
        "page_title":      page_title,
        "description":     description,
        "date":            date,
        "modified":        modified,
        "keywords":        keywords,
        "canonical_url":   canonical_url,
        "breadcrumbs":     breadcrumbs,
        "toc":             toc_html,
        "body":            body_html,
        "rtt_fields":      rtt_fields,
        "source_file":     "docs/" + source_file_rel,
        "source_edit_url": source_edit_url,
    }

    # ── Render ────────────────────────────────────────────────────────────────
    try:
        template = jinja_env.get_template("page.html")
    except TemplateNotFound:
        log.error("  ✗ templates/page.html not found — check TEMPLATE_DIR in config.py")
        return None

    html_out = template.render(**ctx)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html_out, encoding="utf-8")

    return {
        "url":           canonical_url,
        "url_path":      url_path_str,
        "title":         page_title,
        "description":   description,
        "date":          date,
        "modified":      modified,
        "source_file":   source_file_rel,
        "rtt_stability": rtt_fields.get("rtt:stability", "draft"),
    }


# ─────────────────────────────────────────────────────────────────────────────
# Index page
# ─────────────────────────────────────────────────────────────────────────────

def build_index(
    pages:     list[dict[str, Any]],
    site_dir:  Path,
    jinja_env: Environment,
) -> None:
    """
    Render site/index.html as a sorted directory of all built pages.

    Sort order: stable → draft → deprecated; within each group, date desc,
    title asc.
    """
    def _sort_key(p: dict) -> tuple:
        order = {"stable": 0, "draft": 1, "deprecated": 2}
        return (
            order.get(p.get("rtt_stability", "draft"), 1),
            p.get("date") or "0000-00-00",
            p.get("title", ""),
        )

    ctx: dict[str, Any] = {
        **_site_ctx(),
        "page_title":    f"{SITE_NAME} — Documentation",
        "description":   SITE_DESCRIPTION,
        "canonical_url": _canonical("/"),
        "breadcrumbs":   [],
        "toc":           "",
        "date":          "",
        "modified":      "",
        "keywords":      "",
        "rtt_fields":    dict(RTT_DEFAULTS),
        "source_file":   "index",
        "source_edit_url": _REPO_ROOT,
        "pages":         sorted(pages, key=_sort_key),
    }

print("DEBUG: Writing homepage to:", site_dir / "index.html")
print("DEBUG: HTML length:", len(html_out))
print("DEBUG: HTML preview:", html_out[:200])
    
    try:
        template = jinja_env.get_template("index.html")
    except TemplateNotFound:
        log.error("  ✗ templates/index.html not found")
        return

    html_out = template.render(**ctx)
    (site_dir / "index.html").write_text(html_out, encoding="utf-8")
    log.info("  index            site/index.html  (%d pages)", len(pages))


# ─────────────────────────────────────────────────────────────────────────────
# Sitemap
# ─────────────────────────────────────────────────────────────────────────────

def build_sitemap(pages: list[dict[str, Any]], site_dir: Path) -> None:
    """
    Generate site/sitemap.xml (sitemaps.org 0.9 protocol).

    Index URL always appears first with priority 1.0.  Content pages follow
    in canonical URL order.  lastmod falls back to today when absent.
    """
    today = BUILD_TIMESTAMP[:10]

    def _url_block(loc: str, lastmod: str, changefreq: str, priority: str) -> list[str]:
        return [
            "  <url>",
            f"    <loc>{loc}</loc>",
            f"    <lastmod>{lastmod[:10]}</lastmod>",
            f"    <changefreq>{changefreq}</changefreq>",
            f"    <priority>{priority}</priority>",
            "  </url>",
        ]

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
        '        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9',
        '          http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">',
    ]

    lines += _url_block(_canonical("/"), today, "daily", INDEX_PRIORITY)

    for page in sorted(pages, key=lambda p: p["url"]):
        lastmod = page.get("modified") or page.get("date") or today
        lines += _url_block(page["url"], lastmod, SITEMAP_CHANGEFREQ, SITEMAP_PRIORITY)

    lines.append("</urlset>")

    out = site_dir / "sitemap.xml"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    log.info("  sitemap          site/sitemap.xml  (%d URLs)", len(pages) + 1)


# ─────────────────────────────────────────────────────────────────────────────
# robots.txt
# ─────────────────────────────────────────────────────────────────────────────

def build_robots(site_dir: Path) -> None:
    """Write site/robots.txt, allowing all crawlers and advertising the sitemap."""
    sitemap_url = _canonical("/").rstrip("/") + "/sitemap.xml"
    (site_dir / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {sitemap_url}\n",
        encoding="utf-8",
    )
    log.info("  robots           site/robots.txt")


# ─────────────────────────────────────────────────────────────────────────────
# Static assets
# ─────────────────────────────────────────────────────────────────────────────

def copy_static(site_dir: Path) -> None:
    """
    Mirror static/ → site/static/ using shutil.copy2 (preserves mtimes).

    Creates site/static/ even when static/ does not exist so <link> tags
    referencing /static/style.css never produce hard 404s.
    """
    src = Path(STATIC_DIR)
    dst = site_dir / "static"

    if not src.exists():
        dst.mkdir(parents=True, exist_ok=True)
        log.warning("  static/          source dir not found — created empty site/static/")
        return

    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)

    count = sum(1 for f in dst.rglob("*") if f.is_file())
    log.info("  static           %d file(s) → site/static/", count)


# ─────────────────────────────────────────────────────────────────────────────
# Build manifest
# ─────────────────────────────────────────────────────────────────────────────

def write_manifest(pages: list[dict[str, Any]], site_dir: Path) -> None:
    """
    Write site/build-manifest.json for CI/CD traceability.

    Keys are always present; values are always strings or lists of the same
    page-record shape, so downstream consumers need no null-checks.
    """
    manifest = {
        "generator":       "TriadicFrameworks SSG",
        "version":         "1.0.0",
        "build_timestamp": BUILD_TIMESTAMP,
        "base_url":        BASE_URL,
        "total_pages":     len(pages),
        "pages":           pages,
    }
    (site_dir / "build-manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    log.info("  manifest         site/build-manifest.json")


# ─────────────────────────────────────────────────────────────────────────────
# Full build orchestrator
# ─────────────────────────────────────────────────────────────────────────────

def run_build(
    docs_dir:       Path,
    site_dir:       Path,
    *,
    single_file:    Path | None = None,
    include_drafts: bool        = True,
) -> list[dict[str, Any]]:
    """
    Orchestrate a complete (or single-file) build pass.

    Returns the list of page records so callers (watch loop, tests) can inspect
    what was built without re-reading the filesystem.
    """
    t0        = time.monotonic()
    jinja_env = _make_jinja_env()

    if single_file:
        md_files = [single_file]
        log.info("── Single-file build: %s", single_file)
    else:
        md_files = sorted(docs_dir.rglob("*.md"))
        log.info("── Full build  docs/ → site/  (%d .md files found)", len(md_files))

    pages: list[dict[str, Any]] = []

    for md_path in md_files:
        record = build_page(
            md_path, docs_dir, site_dir, jinja_env,
            include_drafts=include_drafts,
        )
        if record is not None:
            pages.append(record)

    if not single_file:
        build_index(pages, site_dir, jinja_env)
        build_sitemap(pages, site_dir)
        build_robots(site_dir)
        copy_static(site_dir)
        write_manifest(pages, site_dir)

    log.info("── ✅ Done  %d page(s) in %.2fs → %s", len(pages), time.monotonic() - t0, site_dir)
    return pages


# ─────────────────────────────────────────────────────────────────────────────
# Watch mode
# ─────────────────────────────────────────────────────────────────────────────

def watch_mode(docs_dir: Path, site_dir: Path, include_drafts: bool) -> None:
    """
    Incremental rebuild loop using watchdog.

    .md changes → single-file rebuild.
    Template or static changes → full rebuild.
    """
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
    except ImportError:
        log.error("watchdog not installed.  Run: pip install watchdog")
        sys.exit(1)

    class _Handler(FileSystemEventHandler):

        def _handle(self, path_str: str) -> None:
            path = Path(path_str)
            if TEMPLATE_DIR in path_str or STATIC_DIR in path_str:
                log.info("🔄 Template/static changed — full rebuild")
                run_build(docs_dir, site_dir, include_drafts=include_drafts)
                return
            if path.suffix.lower() != ".md":
                return
            log.info("🔄 Changed: %s", path)
            try:
                run_build(docs_dir, site_dir, single_file=path,
                          include_drafts=include_drafts)
            except Exception as exc:  # noqa: BLE001
                log.error("  Build error: %s", exc)

        def on_modified(self, event):
            if not event.is_directory:
                self._handle(event.src_path)

        def on_created(self, event):
            if not event.is_directory:
                self._handle(event.src_path)

    repo_root = str(docs_dir.parent)
    observer  = Observer()
    observer.schedule(_Handler(), repo_root, recursive=True)
    observer.start()
    log.info("👀 Watching %s  (Ctrl-C to stop)", repo_root)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        observer.stop()
        observer.join()
        log.info("🛑 Watcher stopped.")


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────

def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="build.py",
        description="TriadicFrameworks SSG — build docs/ → site/",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  python build.py                    full build
  python build.py --clean            wipe site/ then build
  python build.py --file docs/x.md  rebuild one file
  python build.py --watch            incremental watch loop
  python build.py --drafts           include draft pages in output
  python build.py --verbose          debug-level logging
""",
    )
    p.add_argument("--clean",   action="store_true", help="Wipe site/ before building")
    p.add_argument("--watch",   action="store_true", help="Watch for changes and rebuild")
    p.add_argument("--file",    metavar="PATH",      help="Rebuild a single Markdown file")
    p.add_argument("--drafts",  action="store_true", help="Include rtt_stability=draft pages")
    p.add_argument("--verbose", action="store_true", help="Enable debug logging")
    return p.parse_args()


def main() -> None:
    args = _parse_args()

    if args.verbose:
        log.setLevel(logging.DEBUG)

    docs_dir = Path(DOCS_DIR)
    site_dir = Path(SITE_DIR)

    if not docs_dir.exists():
        log.error("docs/ not found at %s — check DOCS_DIR in config.py", docs_dir)
        sys.exit(1)

    tpl_dir = Path(TEMPLATE_DIR)
    for required in ("base.html", "page.html", "index.html"):
        if not (tpl_dir / required).exists():
            log.error("Required template missing: templates/%s", required)
            sys.exit(1)

    if args.clean and site_dir.exists():
        shutil.rmtree(site_dir)
        log.info("🧹 Cleaned %s", site_dir)

    site_dir.mkdir(parents=True, exist_ok=True)

    single_file: Path | None = None
    if args.file:
        single_file = Path(args.file)
        if not single_file.exists():
            log.error("File not found: %s", single_file)
            sys.exit(1)
        if single_file.suffix.lower() != ".md":
            log.error("--file must point to a .md file, got: %s", single_file)
            sys.exit(1)

    include_drafts = args.drafts

    if args.watch:
        run_build(docs_dir, site_dir, include_drafts=include_drafts)
        watch_mode(docs_dir, site_dir, include_drafts)
    else:
        run_build(docs_dir, site_dir, single_file=single_file,
                  include_drafts=include_drafts)


if __name__ == "__main__":
    main()
