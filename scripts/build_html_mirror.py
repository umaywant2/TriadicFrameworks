#!/usr/bin/env python3
"""
TriadicFrameworks docs -> HTML Mirror Builder

Canonical source:
    /docs/**/*

Generated mirror:
    /html/**/*

The mirror includes:
    - Markdown rendered as HTML
    - Existing .html files copied as HTML
    - .json files copied as text
    - .svg files copied byte-for-byte

Publication mappings:
    docs/README.md        -> html/index.html
    docs/index.html       -> html/repo-index.html
    docs/**/index.md      -> html/**/index_md.html

During publication, occurrences of:
    www.triadicframeworks.org

are rewritten to:
    docs.triadicframeworks.org

inside rendered Markdown, copied HTML, and copied JSON files.

For copied index.html navigation files, Markdown targets inside:
    const DOC_MAP = { ... };

are rewritten from:
    .md
to:
    .html

SVG files are preserved byte-for-byte.

Usage:
    python scripts/build_html_mirror.py
    python scripts/build_html_mirror.py --check
    python scripts/build_html_mirror.py --verbose

Dependencies:
    pip install markdown
"""

from __future__ import annotations

import argparse
import html
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import urlsplit, urlunsplit

try:
    import markdown
except ImportError:
    print(
        "ERROR: Python-Markdown is not installed.\n"
        "Install it with:\n\n"
        "    pip install markdown\n",
        file=sys.stderr,
    )
    raise SystemExit(2)


# ---------------------------------------------------------------------------
# Paths and publication rules
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent

DOCS_ROOT = REPO_ROOT / "docs"
HTML_ROOT = REPO_ROOT / "html"
SITEMAP_TARGET = HTML_ROOT / "sitemap.html"

MARKDOWN_SUFFIXES = {".md", ".markdown"}
COPY_SUFFIXES = {".html", ".json", ".svg"}
TEXT_COPY_SUFFIXES = {".html", ".json"}
MANAGED_SUFFIXES = {".html", ".json", ".svg"}

SOURCE_HOSTNAME = "www.triadicframeworks.org"
PUBLIC_HOSTNAME = "docs.triadicframeworks.org"


# ---------------------------------------------------------------------------
# Markdown configuration
# ---------------------------------------------------------------------------

MARKDOWN_EXTENSIONS = [
    "extra",
    "admonition",
    "toc",
    "sane_lists",
]

MARKDOWN_EXTENSION_CONFIGS = {
    "toc": {
        "permalink": False,
    },
}


# ---------------------------------------------------------------------------
# Generated HTML
# ---------------------------------------------------------------------------

HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="generator" content="TriadicFrameworks build_html_mirror.py">
  <meta name="source" content="{source_path}">
  <title>{title}</title>
  <style>
    :root {{
      color-scheme: light dark;
      --content-width: 960px;
    }}

    html {{
      line-height: 1.5;
      font-family:
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;
    }}

    body {{
      max-width: var(--content-width);
      margin: 0 auto;
      padding: 2rem 1.25rem 4rem;
    }}

    img,
    video {{
      max-width: 100%;
      height: auto;
    }}

    table {{
      border-collapse: collapse;
      max-width: 100%;
      display: block;
      overflow-x: auto;
    }}

    th,
    td {{
      border: 1px solid #8888;
      padding: 0.45rem 0.65rem;
      text-align: left;
    }}

    pre {{
      overflow-x: auto;
      padding: 1rem;
      border-radius: 0.4rem;
      background: #8882;
    }}

    code {{
      overflow-wrap: anywhere;
    }}

    blockquote {{
      margin-left: 0;
      padding-left: 1rem;
      border-left: 4px solid #8888;
    }}

    .generated-notice {{
      padding: 0.75rem 1rem;
      margin-bottom: 2rem;
      border: 1px solid #8886;
      border-radius: 0.4rem;
      background: #8881;
      font-size: 0.875rem;
    }}
  </style>
</head>
<body>
  <!--
    GENERATED FILE
    Source: {source_path}
    Do not edit directly.
    Regenerate from canonical source.
  -->

  <aside class="generated-notice">
    <strong>Generated mirror.</strong>
    Canonical source:
    <code>{source_path}</code>
    &middot;
    <a href="{sitemap_href}">Sitemap</a>
  </aside>

  <main>
{body}
  </main>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------

@dataclass
class BuildStats:
    markdown_sources: int = 0
    asset_sources: int = 0
    changed: int = 0
    unchanged: int = 0
    removed: int = 0
    errors: int = 0


# ---------------------------------------------------------------------------
# Front matter
# ---------------------------------------------------------------------------

_FRONT_MATTER_RE = re.compile(
    r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*\r?\n?",
    flags=re.DOTALL,
)


def strip_front_matter(text: str) -> tuple[str, dict[str, str]]:
    """Remove simple YAML-style front matter without requiring PyYAML."""
    match = _FRONT_MATTER_RE.match(text)

    if not match:
        return text, {}

    raw_front_matter = match.group(1)
    body = text[match.end():]
    metadata: dict[str, str] = {}

    for line in raw_front_matter.splitlines():
        if (
            not line.strip()
            or line.lstrip().startswith("#")
            or ":" not in line
        ):
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if not key:
            continue

        if (
            len(value) >= 2
            and value[0] == value[-1]
            and value[0] in ("'", '"')
        ):
            value = value[1:-1]

        metadata[key] = value

    return body, metadata


# ---------------------------------------------------------------------------
# Publication transformations
# ---------------------------------------------------------------------------

_HTML_URL_ATTR_RE = re.compile(
    r'(?P<prefix>\b(?:href|src)=")'
    r'(?P<url>[^"]+)'
    r'(?P<suffix>")',
    flags=re.IGNORECASE,
)

_DOC_MAP_RE = re.compile(
    r"(?P<doc_map>"
    r"\bconst\s+DOC_MAP\s*=\s*\{"
    r".*?"
    r"\}\s*;"
    r")",
    flags=re.DOTALL,
)

_DOC_MAP_MARKDOWN_TARGET_RE = re.compile(
    r"\.(?:md|markdown)(?=['\"])",
    flags=re.IGNORECASE,
)


def rewrite_public_hostname(text: str) -> str:
    """Rewrite the canonical hostname for the published HTML mirror."""
    return text.replace(
        SOURCE_HOSTNAME,
        PUBLIC_HOSTNAME,
    )


def rewrite_index_doc_map(content: str) -> str:
    """
    Rewrite Markdown targets inside a copied index.html DOC_MAP.

    Only the const DOC_MAP section is modified.

    Examples:
        '/docs/Foo/README.md'
            -> '/docs/Foo/README.html'

        "/docs/Foo/index.markdown"
            -> "/docs/Foo/index.html"

    Markdown references outside DOC_MAP are left untouched.
    """

    def replace_doc_map(match: re.Match[str]) -> str:
        doc_map = match.group("doc_map")

        return _DOC_MAP_MARKDOWN_TARGET_RE.sub(
            ".html",
            doc_map,
        )

    return _DOC_MAP_RE.sub(
        replace_doc_map,
        content,
    )


def rewrite_markdown_url(url: str) -> str:
    """Convert a local Markdown target to its mirrored HTML target."""
    if not url:
        return url

    lowered = url.lower()

    if (
        lowered.startswith(
            (
                "http://",
                "https://",
                "mailto:",
                "tel:",
                "data:",
            )
        )
        or url.startswith(("#", "//"))
    ):
        return url

    parts = urlsplit(url)
    path = parts.path
    lowered_path = path.lower()

    if lowered_path.endswith("/index.md"):
        path = path[:-9] + "/index_md.html"
    elif lowered_path.endswith("/index.markdown"):
        path = path[:-15] + "/index_md.html"
    elif lowered_path.endswith(".md"):
        path = path[:-3] + ".html"
    elif lowered_path.endswith(".markdown"):
        path = path[:-9] + ".html"
    else:
        return url

    return urlunsplit(
        (
            parts.scheme,
            parts.netloc,
            path,
            parts.query,
            parts.fragment,
        )
    )


def rewrite_html_links(rendered_html: str) -> str:
    """Rewrite local .md/.markdown links in generated href/src attributes."""

    def replace(match: re.Match[str]) -> str:
        rewritten = rewrite_markdown_url(
            match.group("url")
        )

        return (
            match.group("prefix")
            + rewritten
            + match.group("suffix")
        )

    return _HTML_URL_ATTR_RE.sub(
        replace,
        rendered_html,
    )


# ---------------------------------------------------------------------------
# Source discovery and target mapping
# ---------------------------------------------------------------------------

def discover_files(
    suffixes: set[str],
) -> list[Path]:
    """Return matching files under /docs in deterministic order."""
    files = [
        path
        for path in DOCS_ROOT.rglob("*")
        if path.is_file()
        and path.suffix.lower() in suffixes
    ]

    return sorted(
        files,
        key=lambda path: (
            path.relative_to(DOCS_ROOT)
            .as_posix()
            .lower()
        ),
    )


def discover_markdown_files() -> list[Path]:
    """Return all Markdown sources under /docs."""
    return discover_files(MARKDOWN_SUFFIXES)


def discover_asset_files() -> list[Path]:
    """Return all copied HTML, JSON, and SVG assets under /docs."""
    return discover_files(COPY_SUFFIXES)


def target_for_markdown(source: Path) -> Path:
    """Map a Markdown source to its final HTML publication target."""
    relative = source.relative_to(
        DOCS_ROOT
    )

    if relative == Path("README.md"):
        return HTML_ROOT / "index.html"

    if relative.name.lower() in {
        "index.md",
        "index.markdown",
    }:
        return (
            HTML_ROOT
            / relative
        ).with_name("index_md.html")

    return (
        HTML_ROOT
        / relative
    ).with_suffix(".html")


def target_for_asset(source: Path) -> Path:
    """Map a copied HTML/JSON/SVG source to its publication target."""
    relative = source.relative_to(
        DOCS_ROOT
    )

    if relative == Path("index.html"):
        return HTML_ROOT / "repo-index.html"

    return HTML_ROOT / relative


def build_target_map(
    markdown_sources: Iterable[Path],
    asset_sources: Iterable[Path],
) -> dict[Path, Path]:
    """Build and validate the complete source-to-target publication map."""
    target_map: dict[Path, Path] = {}
    owners: dict[Path, Path] = {}

    for source in asset_sources:
        target = target_for_asset(source)
        resolved = target.resolve()

        if resolved in owners:
            raise ValueError(
                "Target collision: "
                f"{source} and {owners[resolved]} "
                f"-> {target}"
            )

        owners[resolved] = source

    for source in markdown_sources:
        target = target_for_markdown(source)
        resolved = target.resolve()

        if resolved in owners:
            raise ValueError(
                "Target collision: "
                f"{source} and {owners[resolved]} "
                f"-> {target}"
            )

        target_map[source] = target
        owners[resolved] = source

    return target_map


def expected_output_files(
    target_map: dict[Path, Path],
) -> set[Path]:
    """Return the complete set of expected mirror output paths."""
    return {
        target.resolve()
        for target in target_map.values()
    }
    

# ---------------------------------------------------------------------------
# Title extraction and Markdown rendering
# ---------------------------------------------------------------------------

_ATX_HEADING_RE = re.compile(
    r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$",
    flags=re.MULTILINE,
)

_MARKDOWN_LINK_RE = re.compile(
    r"!?\[([^\]]+)\]\([^)]*\)"
)

_MARKDOWN_INLINE_RE = re.compile(
    r"[*_`~]"
)


def title_from_markdown(
    markdown_text: str,
    metadata: dict[str, str],
    source: Path,
) -> str:
    """Choose a useful HTML document title."""
    metadata_title = metadata.get("title")

    if metadata_title:
        return metadata_title.strip()

    heading = _ATX_HEADING_RE.search(
        markdown_text
    )

    if heading:
        title = heading.group(1)

        title = _MARKDOWN_LINK_RE.sub(
            lambda match: match.group(1),
            title,
        )

        title = _MARKDOWN_INLINE_RE.sub(
            "",
            title,
        ).strip()

        if title:
            return title

    return source.stem


def render_markdown(source_text: str) -> str:
    """Render Markdown into publication-ready HTML."""
    source_text = rewrite_public_hostname(
        source_text
    )

    md = markdown.Markdown(
        extensions=MARKDOWN_EXTENSIONS,
        extension_configs=MARKDOWN_EXTENSION_CONFIGS,
        output_format="html5",
    )

    rendered = md.convert(
        source_text
    )

    return rewrite_html_links(
        rendered
    )


def sitemap_href_for_target(
    target: Path,
) -> str:
    """Return a relative URL from a generated page to sitemap.html."""
    relative = os.path.relpath(
        SITEMAP_TARGET,
        start=target.parent,
    )

    return Path(relative).as_posix()


def build_markdown_document(
    source: Path,
    target: Path,
) -> str:
    """Build the complete HTML document for one Markdown source."""
    source_text = source.read_text(
        encoding="utf-8",
        errors="strict",
    )

    markdown_body, metadata = strip_front_matter(
        source_text
    )

    title = title_from_markdown(
        markdown_body,
        metadata,
        source,
    )

    rendered_body = render_markdown(
        markdown_body
    )

    canonical_source = (
        Path("/docs")
        / source.relative_to(DOCS_ROOT)
    ).as_posix()

    sitemap_href = sitemap_href_for_target(
        target
    )

    return HTML_TEMPLATE.format(
        source_path=html.escape(
            canonical_source,
            quote=True,
        ),
        title=html.escape(
            title,
            quote=True,
        ),
        sitemap_href=html.escape(
            sitemap_href,
            quote=True,
        ),
        body=rendered_body,
    )


# ---------------------------------------------------------------------------
# File writing and copying
# ---------------------------------------------------------------------------

def write_text_if_changed(
    target: Path,
    content: str,
    *,
    check: bool,
) -> str:
    """Write UTF-8 text only when its target content differs."""
    existing: str | None = None

    if target.exists():
        existing = target.read_text(
            encoding="utf-8",
            errors="strict",
        )

    if existing == content:
        return "unchanged"

    if not check:
        target.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        target.write_text(
            content,
            encoding="utf-8",
            newline="\n",
        )

    return "changed"


def write_bytes_if_changed(
    target: Path,
    content: bytes,
    *,
    check: bool,
) -> str:
    """Write binary content only when its target content differs."""
    existing: bytes | None = None

    if target.exists():
        existing = target.read_bytes()

    if existing == content:
        return "unchanged"

    if not check:
        target.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        target.write_bytes(
            content
        )

    return "changed"


def transform_text_asset(
    source: Path,
    content: str,
) -> str:
    """
    Apply publication transformations to a copied text asset.

    All copied HTML and JSON files receive the hostname rewrite.

    Copied files specifically named index.html also receive the
    DOC_MAP Markdown-target rewrite.
    """
    content = rewrite_public_hostname(
        content
    )

    if source.name.lower() == "index.html":
        content = rewrite_index_doc_map(
            content
        )

    return content


def copy_asset(
    source: Path,
    target: Path,
    *,
    check: bool,
) -> str:
    """Copy one support asset, applying publication rewriting where needed."""
    suffix = source.suffix.lower()

    if suffix in TEXT_COPY_SUFFIXES:
        content = source.read_text(
            encoding="utf-8",
            errors="strict",
        )

        content = transform_text_asset(
            source,
            content,
        )

        return write_text_if_changed(
            target,
            content,
            check=check,
        )

    return write_bytes_if_changed(
        target,
        source.read_bytes(),
        check=check,
    )


# ---------------------------------------------------------------------------
# Orphan reconciliation and validation
# ---------------------------------------------------------------------------

def discover_managed_outputs() -> list[Path]:
    """Return all managed files currently present under /html."""
    if not HTML_ROOT.exists():
        return []

    outputs = [
        path
        for path in HTML_ROOT.rglob("*")
        if path.is_file()
        and path.suffix.lower() in MANAGED_SUFFIXES
    ]

    return sorted(
        outputs,
        key=lambda path: (
            path.relative_to(HTML_ROOT)
            .as_posix()
            .lower()
        ),
    )


def remove_orphans(
    expected: set[Path],
    *,
    check: bool,
    verbose: bool,
) -> int:
    """Remove or report managed outputs that have no current source."""
    removed = 0

    for output_file in discover_managed_outputs():
        if output_file.resolve() in expected:
            continue

        removed += 1

        relative = output_file.relative_to(
            REPO_ROOT
        )

        if verbose or check:
            action = (
                "ORPHAN"
                if check
                else "REMOVE"
            )

            print(
                f"[{action}] "
                f"{relative.as_posix()}"
            )

        if not check:
            output_file.unlink()

    if not check:
        remove_empty_directories(
            HTML_ROOT
        )

    return removed


def remove_empty_directories(
    root: Path,
) -> None:
    """Remove empty generated directories after orphan cleanup."""
    if not root.exists():
        return

    directories = sorted(
        (
            path
            for path in root.rglob("*")
            if path.is_dir()
        ),
        key=lambda path: len(path.parts),
        reverse=True,
    )

    for directory in directories:
        try:
            directory.rmdir()
        except OSError:
            # Directory is not empty.
            pass


def validate_mirror(
    expected: set[Path],
) -> tuple[list[Path], list[Path]]:
    """Return missing and orphaned managed outputs."""
    actual = {
        path.resolve()
        for path in discover_managed_outputs()
    }

    missing = sorted(
        expected - actual,
        key=lambda path: (
            path.as_posix().lower()
        ),
    )

    orphaned = sorted(
        actual - expected,
        key=lambda path: (
            path.as_posix().lower()
        ),
    )

    return missing, orphaned


# ---------------------------------------------------------------------------
# Processing helpers
# ---------------------------------------------------------------------------

def record_result(
    *,
    result: str,
    action: str,
    source: Path,
    target: Path,
    stats: BuildStats,
    check: bool,
    verbose: bool,
) -> None:
    """Record and optionally print one copy or render operation."""
    source_rel = source.relative_to(
        REPO_ROOT
    )

    target_rel = target.relative_to(
        REPO_ROOT
    )

    if result == "changed":
        stats.changed += 1

        if verbose or check:
            displayed_action = (
                "STALE"
                if check
                else action
            )

            print(
                f"[{displayed_action}] "
                f"{source_rel.as_posix()} -> "
                f"{target_rel.as_posix()}"
            )

        return

    stats.unchanged += 1

    if verbose:
        print(
            "[OK]    "
            f"{source_rel.as_posix()} -> "
            f"{target_rel.as_posix()}"
        )


def process_assets(
    asset_sources: Iterable[Path],
    target_map: dict[Path, Path],
    stats: BuildStats,
    *,
    check: bool,
    verbose: bool,
) -> None:
    """Copy all support assets into the HTML mirror."""
    for source in asset_sources:
        target = target_map[source]

        try:
            result = copy_asset(
                source,
                target,
                check=check,
            )

            record_result(
                result=result,
                action="COPY",
                source=source,
                target=target,
                stats=stats,
                check=check,
                verbose=verbose,
            )

        except Exception as exc:
            stats.errors += 1

            source_rel = source.relative_to(
                REPO_ROOT
            )

            print(
                f"[ERROR] "
                f"{source_rel.as_posix()}: "
                f"{exc}",
                file=sys.stderr,
            )


def process_markdown(
    markdown_sources: Iterable[Path],
    target_map: dict[Path, Path],
    stats: BuildStats,
    *,
    check: bool,
    verbose: bool,
) -> None:
    """Render all Markdown sources into the HTML mirror."""
    for source in markdown_sources:
        target = target_map[source]

        try:
            content = build_markdown_document(
                source,
                target,
            )

            result = write_text_if_changed(
                target,
                content,
                check=check,
            )

            record_result(
                result=result,
                action="WRITE",
                source=source,
                target=target,
                stats=stats,
                check=check,
                verbose=verbose,
            )

        except Exception as exc:
            stats.errors += 1

            source_rel = source.relative_to(
                REPO_ROOT
            )

            print(
                f"[ERROR] "
                f"{source_rel.as_posix()}: "
                f"{exc}",
                file=sys.stderr,
            )


# ---------------------------------------------------------------------------
# Status reporting
# ---------------------------------------------------------------------------

def print_summary(
    stats: BuildStats,
) -> None:
    """Print the final mirror processing summary."""
    print()
    print("Mirror Summary")
    print("-" * 32)
    print(
        f"Markdown sources : "
        f"{stats.markdown_sources}"
    )
    print(
        f"Copied assets    : "
        f"{stats.asset_sources}"
    )
    print(
        f"Files changed    : "
        f"{stats.changed}"
    )
    print(
        f"Files unchanged  : "
        f"{stats.unchanged}"
    )
    print(
        f"Orphan files     : "
        f"{stats.removed}"
    )
    print(
        f"Processing errors: "
        f"{stats.errors}"
    )


def print_validation_paths(
    missing: Iterable[Path],
    orphaned: Iterable[Path],
) -> None:
    """Print missing and orphaned paths relative to the repository."""
    for path in missing:
        print(
            "[MISSING] "
            + path.relative_to(
                REPO_ROOT
            ).as_posix()
        )

    for path in orphaned:
        print(
            "[ORPHAN] "
            + path.relative_to(
                REPO_ROOT
            ).as_posix()
        )


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def build(
    *,
    check: bool,
    verbose: bool,
) -> int:
    """Build or validate the complete docs-to-HTML mirror."""
    if not DOCS_ROOT.is_dir():
        print(
            (
                "ERROR: docs directory does not exist: "
                f"{DOCS_ROOT}"
            ),
            file=sys.stderr,
        )

        return 2

    markdown_sources = discover_markdown_files()
    asset_sources = discover_asset_files()

    try:
        target_map = build_target_map(
            markdown_sources,
            asset_sources,
        )
    except ValueError as exc:
        print(
            f"ERROR: {exc}",
            file=sys.stderr,
        )

        return 2

    expected = expected_output_files(
        target_map
    )

    stats = BuildStats(
        markdown_sources=len(markdown_sources),
        asset_sources=len(asset_sources),
    )

    mode = (
        "CHECK"
        if check
        else "BUILD"
    )

    print()
    print("TriadicFrameworks HTML Mirror")
    print("=" * 32)
    print(f"Mode              : {mode}")
    print(f"Source            : {DOCS_ROOT}")
    print(f"Mirror            : {HTML_ROOT}")
    print()

    # Copy support assets first. Markdown rendering is the final projection.
    process_assets(
        asset_sources,
        target_map,
        stats,
        check=check,
        verbose=verbose,
    )

    process_markdown(
        markdown_sources,
        target_map,
        stats,
        check=check,
        verbose=verbose,
    )

    stats.removed = remove_orphans(
        expected,
        check=check,
        verbose=verbose,
    )

    print_summary(
        stats
    )

    if stats.errors:
        print()
        print("MIRROR STATUS: ERROR")
        return 1

    if check and (
        stats.changed
        or stats.removed
    ):
        print()
        print("MIRROR STATUS: OUT OF SYNC")
        print(
            "Run scripts/build_html_mirror.py "
            "to reconcile the mirror."
        )

        return 1

    missing, orphaned = validate_mirror(
        expected
    )

    if missing or orphaned:
        print()

        status = (
            "OUT OF SYNC"
            if check
            else "ERROR"
        )

        print(
            f"MIRROR STATUS: {status}"
        )

        print_validation_paths(
            missing,
            orphaned,
        )

        return 1

    print()
    print("MIRROR STATUS: OK")

    return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Build and validate the "
            "TriadicFrameworks "
            "/docs -> /html mirror."
        )
    )

    parser.add_argument(
        "--check",
        action="store_true",
        help=(
            "Do not modify files. Exit nonzero if generated "
            "or copied content would change, or if orphaned "
            "mirror files exist."
        ),
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print each mirror operation.",
    )

    return parser.parse_args()


def main() -> int:
    """Run the HTML mirror command."""
    args = parse_args()

    return build(
        check=args.check,
        verbose=args.verbose,
    )


if __name__ == "__main__":
    raise SystemExit(main())
