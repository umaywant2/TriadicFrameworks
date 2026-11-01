#!/usr/bin/env python3
"""
TriadicFrameworks Markdown -> HTML Mirror Builder

Canonical source:
    /docs/**/*.md

Generated mirror:
    /html/**/*.html

Examples:
    docs/README.md
        -> html/README.html

    docs/rtt/Harmonic_Stability_Profile/README.md
        -> html/rtt/Harmonic_Stability_Profile/README.html

The HTML tree is generated content. Do not edit it directly.

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
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent

DOCS_ROOT = REPO_ROOT / "docs"
HTML_ROOT = REPO_ROOT / "html"


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
    Regenerate from canonical Markdown source.
  -->

  <aside class="generated-notice">
    <strong>Generated mirror.</strong>
    Canonical source:
    <code>{source_path}</code>
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
    sources: int = 0
    generated: int = 0
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
    """
    Remove simple YAML-style front matter without requiring PyYAML.

    We only extract basic scalar key/value pairs needed for presentation,
    especially `title`. Complex YAML remains intentionally uninterpreted.
    """
    match = _FRONT_MATTER_RE.match(text)

    if not match:
        return text, {}

    raw_front_matter = match.group(1)
    body = text[match.end():]

    metadata: dict[str, str] = {}

    for line in raw_front_matter.splitlines():
        if not line.strip():
            continue

        if line.lstrip().startswith("#"):
            continue

        if ":" not in line:
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
# Link rewriting
# ---------------------------------------------------------------------------

# HTML attributes emitted by Markdown which commonly contain local paths.
_HTML_URL_ATTR_RE = re.compile(
    r'(?P<prefix>\b(?:href|src)=")'
    r'(?P<url>[^"]+)'
    r'(?P<suffix>")',
    flags=re.IGNORECASE,
)


def rewrite_markdown_url(url: str) -> str:
    """
    Convert an internal Markdown target to its mirrored HTML target.

    Examples:
        README.md
            -> README.html

        ../Law/index.md#section
            -> ../Law/index.html#section

        ./foo.md?x=1#bar
            -> ./foo.html?x=1#bar

    External URLs, anchors, mailto:, etc. are untouched.
    """
    if not url:
        return url

    lowered = url.lower()

    if (
        lowered.startswith(("http://", "https://", "mailto:", "tel:", "data:"))
        or url.startswith(("#", "//"))
    ):
        return url

    parts = urlsplit(url)
    path = parts.path

    if path.lower().endswith(".md"):
        path = path[:-3] + ".html"
    elif path.lower().endswith(".markdown"):
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
    """Rewrite .md/.markdown links in generated href/src attributes."""

    def replace(match: re.Match[str]) -> str:
        original = match.group("url")
        rewritten = rewrite_markdown_url(original)

        return match.group("prefix") + rewritten + match.group("suffix")

    return _HTML_URL_ATTR_RE.sub(replace, rendered_html)


# ---------------------------------------------------------------------------
# Source discovery
# ---------------------------------------------------------------------------

def discover_markdown_files() -> list[Path]:
    """Return every Markdown source under /docs in deterministic order."""
    files = [
        path
        for path in DOCS_ROOT.rglob("*")
        if path.is_file() and path.suffix.lower() in {".md", ".markdown"}
    ]

    return sorted(
        files,
        key=lambda path: path.relative_to(DOCS_ROOT).as_posix().lower(),
    )


def target_for_source(source: Path) -> Path:
    """Map a /docs Markdown path to its corresponding /html path."""
    relative = source.relative_to(DOCS_ROOT)
    return (HTML_ROOT / relative).with_suffix(".html")


def expected_html_files(sources: Iterable[Path]) -> set[Path]:
    return {target_for_source(source).resolve() for source in sources}


# ---------------------------------------------------------------------------
# Title extraction
# ---------------------------------------------------------------------------

_ATX_HEADING_RE = re.compile(
    r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$",
    flags=re.MULTILINE,
)

_MARKDOWN_LINK_RE = re.compile(r"!?\[([^\]]+)\]\([^)]*\)")
_MARKDOWN_INLINE_RE = re.compile(r"[*_`~]")


def title_from_markdown(
    markdown_text: str,
    metadata: dict[str, str],
    source: Path,
) -> str:
    """Choose a useful HTML document title."""
    metadata_title = metadata.get("title")

    if metadata_title:
        return metadata_title.strip()

    heading = _ATX_HEADING_RE.search(markdown_text)

    if heading:
        title = heading.group(1)
        title = _MARKDOWN_LINK_RE.sub(lambda match: match.group(1), title)
        title = _MARKDOWN_INLINE_RE.sub("", title).strip()

        if title:
            return title

    return source.stem


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def render_markdown(source_text: str) -> str:
    md = markdown.Markdown(
        extensions=MARKDOWN_EXTENSIONS,
        extension_configs=MARKDOWN_EXTENSION_CONFIGS,
        output_format="html5",
    )

    rendered = md.convert(source_text)
    return rewrite_html_links(rendered)


def build_document(source: Path) -> str:
    source_text = source.read_text(
        encoding="utf-8",
        errors="strict",
    )

    markdown_body, metadata = strip_front_matter(source_text)
    title = title_from_markdown(markdown_body, metadata, source)
    rendered_body = render_markdown(markdown_body)

    canonical_source = (
        Path("/docs") / source.relative_to(DOCS_ROOT)
    ).as_posix()

    return HTML_TEMPLATE.format(
        source_path=html.escape(canonical_source, quote=True),
        title=html.escape(title, quote=True),
        body=rendered_body,
    )


# ---------------------------------------------------------------------------
# File writing
# ---------------------------------------------------------------------------

def write_if_changed(
    target: Path,
    content: str,
    *,
    check: bool,
) -> str:
    """
    Return:
        "generated" - target must be created or updated
        "unchanged" - existing output already matches
    """
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

    return "generated"


# ---------------------------------------------------------------------------
# Orphan reconciliation
# ---------------------------------------------------------------------------

def discover_generated_html() -> list[Path]:
    if not HTML_ROOT.exists():
        return []

    return sorted(
        (
            path
            for path in HTML_ROOT.rglob("*.html")
            if path.is_file()
        ),
        key=lambda path: path.relative_to(HTML_ROOT).as_posix().lower(),
    )


def remove_orphans(
    expected: set[Path],
    *,
    check: bool,
    verbose: bool,
) -> int:
    removed = 0

    for html_file in discover_generated_html():
        if html_file.resolve() in expected:
            continue

        removed += 1
        relative = html_file.relative_to(REPO_ROOT)

        if verbose or check:
            action = "ORPHAN" if check else "REMOVE"
            print(f"[{action}] {relative.as_posix()}")

        if not check:
            html_file.unlink()

    if not check:
        remove_empty_directories(HTML_ROOT)

    return removed


def remove_empty_directories(root: Path) -> None:
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


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_mirror(
    sources: list[Path],
) -> tuple[list[Path], list[Path]]:
    expected = expected_html_files(sources)
    actual = {
        path.resolve()
        for path in discover_generated_html()
    }

    missing = sorted(
        expected - actual,
        key=lambda path: path.as_posix().lower(),
    )

    orphaned = sorted(
        actual - expected,
        key=lambda path: path.as_posix().lower(),
    )

    return missing, orphaned


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def build(
    *,
    check: bool,
    verbose: bool,
) -> int:
    if not DOCS_ROOT.is_dir():
        print(
            f"ERROR: docs directory does not exist: {DOCS_ROOT}",
            file=sys.stderr,
        )
        return 2

    sources = discover_markdown_files()
    stats = BuildStats(sources=len(sources))
    expected = expected_html_files(sources)
    mode = "CHECK" if check else "BUILD"

    print()
    print("TriadicFrameworks HTML Mirror")
    print("=" * 32)
    print(f"Mode              : {mode}")
    print(f"Source            : {DOCS_ROOT}")
    print(f"Mirror            : {HTML_ROOT}")
    print()

    for source in sources:
        target = target_for_source(source)
        source_rel = source.relative_to(REPO_ROOT)
        target_rel = target.relative_to(REPO_ROOT)

        try:
            content = build_document(source)
            result = write_if_changed(target, content, check=check)

            if result == "generated":
                stats.generated += 1

                if verbose or check:
                    action = "STALE" if check else "WRITE"
                    print(
                        f"[{action}] "
                        f"{source_rel.as_posix()} -> "
                        f"{target_rel.as_posix()}"
                    )
            else:
                stats.unchanged += 1

                if verbose:
                    print(
                        f"[OK]    "
                        f"{source_rel.as_posix()} -> "
                        f"{target_rel.as_posix()}"
                    )

        except Exception as exc:
            stats.errors += 1
            print(
                f"[ERROR] {source_rel.as_posix()}: {exc}",
                file=sys.stderr,
            )

    stats.removed = remove_orphans(
        expected,
        check=check,
        verbose=verbose,
    )

    print()
    print("Mirror Summary")
    print("-" * 32)
    print(f"Markdown sources : {stats.sources}")
    print(f"HTML changed     : {stats.generated}")
    print(f"HTML unchanged   : {stats.unchanged}")
    print(f"Orphan HTML      : {stats.removed}")
    print(f"Conversion errors: {stats.errors}")

    if stats.errors:
        print()
        print("MIRROR STATUS: ERROR")
        return 1

    if check:
        if stats.generated or stats.removed:
            print()
            print("MIRROR STATUS: OUT OF SYNC")
            print(
                "Run scripts/build_html_mirror.py "
                "to reconcile the mirror."
            )
            return 1

        # The check above compares generated content, but perform the
        # structural invariant check too.
        missing, orphaned = validate_mirror(sources)

        if missing or orphaned:
            print()
            print("MIRROR STATUS: OUT OF SYNC")

            for path in missing:
                print("[MISSING] " + path.relative_to(REPO_ROOT).as_posix())

            for path in orphaned:
                print("[ORPHAN] " + path.relative_to(REPO_ROOT).as_posix())

            return 1

        print()
        print("MIRROR STATUS: OK")
        return 0

    # After a normal build, validate the physical tree.
    missing, orphaned = validate_mirror(sources)

    if missing or orphaned:
        print()

        for path in missing:
            print(
                "[MISSING] " + path.relative_to(REPO_ROOT).as_posix(),
                file=sys.stderr,
            )

        for path in orphaned:
            print(
                "[ORPHAN] " + path.relative_to(REPO_ROOT).as_posix(),
                file=sys.stderr,
            )

        print()
        print("MIRROR STATUS: ERROR")
        return 1

    print()
    print("MIRROR STATUS: OK")
    return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build and validate the TriadicFrameworks "
            "/docs -> /html Markdown mirror."
        )
    )

    parser.add_argument(
        "--check",
        action="store_true",
        help=(
            "Do not modify files. Exit nonzero if generated HTML "
            "would change or orphan HTML exists."
        ),
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print each mirror operation.",
    )

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return build(
        check=args.check,
        verbose=args.verbose,
    )


if __name__ == "__main__":
    raise SystemExit(main())
