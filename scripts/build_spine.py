#!/usr/bin/env python3

from __future__ import annotations

import html
import json
import re
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SPINE = DOCS / "spine"
GRAMMAR = SPINE / "grammar"

SPINE_MANIFEST = SPINE / "spine-manifest.json"
GRAMMAR_JSON = GRAMMAR / "grammar.json"
GRAMMAR_HTML = GRAMMAR / "index.html"

EXCLUDED_DIRS = {
    ".git",
    ".github",
    "node_modules",
    "vendor",
    "__pycache__",
}

# Markdown/code forms that are often structurally significant in
# TriadicFrameworks documents.
OPERATOR_RE = re.compile(
    r"""
    (?:
        [∇∆ΔΣ∂⊗⊕∘→↔⇌]
        [A-Za-z0-9_{}\\()\-]*
    )
    |
    (?:
        \b[A-Z][A-Z0-9_-]{1,15}\b
    )
    |
    (?:
        \b[A-Za-z][A-Za-z0-9_-]*
        \s*(?:::|->|=>|↔|→)\s*
        [A-Za-z][A-Za-z0-9_-]*\b
    )
    """,
    re.VERBOSE,
)

BOLD_TERM_RE = re.compile(r"\*\*([^*\n]{2,80})\*\*")
CODE_TERM_RE = re.compile(r"`([^`\n]{2,100})`")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)

STOP_TERMS = {
    "README",
    "NOTE",
    "TODO",
    "HTTP",
    "HTTPS",
    "HTML",
    "JSON",
    "YAML",
    "MARKDOWN",
}


@dataclass
class GrammarTerm:
    term: str
    modules: set[str] = field(default_factory=set)
    files: set[str] = field(default_factory=set)
    occurrences: int = 0
    kinds: set[str] = field(default_factory=set)


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def excluded(path: Path) -> bool:
    return any(part in EXCLUDED_DIRS for part in path.parts)


def discover_module_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("module.json")
        if not excluded(path)
    )


def discover_markdown_files() -> list[Path]:
    return sorted(
        path
        for path in DOCS.rglob("*.md")
        if not excluded(path)
    )


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def module_identity(path: Path, payload: dict[str, Any]) -> str:
    for key in ("id", "module_id", "slug", "name", "title"):
        value = payload.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()

    return path.parent.name


def build_module_inventory(
    module_files: list[Path],
) -> tuple[list[dict[str, Any]], dict[Path, str]]:

    inventory: list[dict[str, Any]] = []
    module_roots: dict[Path, str] = {}

    for module_file in module_files:
        payload = load_json(module_file)
        module_id = module_identity(module_file, payload)

        module_roots[module_file.parent.resolve()] = module_id

        inventory.append(
            {
                "module": module_id,
                "module_json": relative(module_file),
                "directory": relative(module_file.parent),
                "metadata": payload,
            }
        )

    inventory.sort(
        key=lambda item: (
            item["module"].casefold(),
            item["module_json"],
        )
    )

    return inventory, module_roots


def owning_module(
    markdown: Path,
    module_roots: dict[Path, str],
) -> str:

    current = markdown.parent.resolve()

    while current != ROOT.parent:
        if current in module_roots:
            return module_roots[current]

        if current == ROOT:
            break

        current = current.parent

    try:
        rel = markdown.relative_to(DOCS)
        if rel.parts:
            return rel.parts[0]
    except ValueError:
        pass

    return "_root"


def normalize_term(term: str) -> str:
    term = html.unescape(term)
    term = re.sub(r"\s+", " ", term).strip()
    term = term.strip(" :;,.!?()[]{}")
    return term


def valid_term(term: str) -> bool:
    if len(term) < 2 or len(term) > 100:
        return False

    if term.upper() in STOP_TERMS:
        return False

    if term.startswith(("http://", "https://")):
        return False

    if re.fullmatch(r"\d+(?:\.\d+)*", term):
        return False

    return True


def add_term(
    terms: dict[str, GrammarTerm],
    raw_term: str,
    module: str,
    source_file: Path,
    kind: str,
) -> None:

    term = normalize_term(raw_term)

    if not valid_term(term):
        return

    key = term.casefold()

    if key not in terms:
        terms[key] = GrammarTerm(term=term)

    item = terms[key]
    item.modules.add(module)
    item.files.add(relative(source_file))
    item.occurrences += 1
    item.kinds.add(kind)


def extract_grammar(
    markdown_files: list[Path],
    module_roots: dict[Path, str],
) -> dict[str, GrammarTerm]:

    terms: dict[str, GrammarTerm] = {}

    for markdown in markdown_files:
        text = markdown.read_text(
            encoding="utf-8",
            errors="replace",
        )

        module = owning_module(markdown, module_roots)

        for match in HEADING_RE.finditer(text):
            add_term(
                terms,
                match.group(1),
                module,
                markdown,
                "heading",
            )

        for match in BOLD_TERM_RE.finditer(text):
            add_term(
                terms,
                match.group(1),
                module,
                markdown,
                "defined-term",
            )

        for match in CODE_TERM_RE.finditer(text):
            add_term(
                terms,
                match.group(1),
                module,
                markdown,
                "inline-code",
            )

        for match in OPERATOR_RE.finditer(text):
            add_term(
                terms,
                match.group(0),
                module,
                markdown,
                "operator",
            )

    return terms


def classify_terms(
    terms: dict[str, GrammarTerm],
) -> tuple[list[GrammarTerm], dict[str, list[GrammarTerm]]]:

    common: list[GrammarTerm] = []
    per_module: dict[str, list[GrammarTerm]] = defaultdict(list)

    for item in terms.values():

        # Shared between two or more modules means it belongs to the
        # common structural grammar layer.
        if len(item.modules) >= 2:
            common.append(item)
            continue

        for module in item.modules:
            per_module[module].append(item)

    common.sort(key=lambda item: item.term.casefold())

    for module in per_module:
        per_module[module].sort(
            key=lambda item: item.term.casefold()
        )

    return common, dict(sorted(per_module.items()))


def term_json(item: GrammarTerm) -> dict[str, Any]:
    return {
        "term": item.term,
        "modules": sorted(item.modules),
        "files": sorted(item.files),
        "occurrences": item.occurrences,
        "kinds": sorted(item.kinds),
    }


def write_module_manifest(
    inventory: list[dict[str, Any]],
) -> None:

    output = {
        "schema": "triadicframeworks.spine.modules/v1",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "module_count": len(inventory),
        "modules": inventory,
    }

    SPINE.mkdir(parents=True, exist_ok=True)

    SPINE_MANIFEST.write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def write_grammar_json(
    markdown_files: list[Path],
    common: list[GrammarTerm],
    per_module: dict[str, list[GrammarTerm]],
) -> None:

    output = {
        "schema": "triadicframeworks.spine.grammar/v1",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "markdown_files_scanned": len(markdown_files),
        "classification": {
            "common_rule":
                "Term occurs in two or more modules.",
            "remaining_rule":
                "Terms occurring in one module remain module-local.",
        },
        "common": [
            term_json(item)
            for item in common
        ],
        "modules": {
            module: [
                term_json(item)
                for item in items
            ]
            for module, items in per_module.items()
        },
    }

    GRAMMAR.mkdir(parents=True, exist_ok=True)

    GRAMMAR_JSON.write_text(
        json.dumps(output, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def render_term(item: GrammarTerm) -> str:
    modules = ", ".join(sorted(item.modules))
    files = ", ".join(sorted(item.files))
    kinds = ", ".join(sorted(item.kinds))

    return f"""
      <li>
        <strong>{html.escape(item.term)}</strong>
        <div class="meta">
          {item.occurrences} occurrence(s)
          · {html.escape(kinds)}
          · {html.escape(modules)}
        </div>
        <div class="files">{html.escape(files)}</div>
      </li>
    """


def write_grammar_html(
    module_count: int,
    markdown_count: int,
    common: list[GrammarTerm],
    per_module: dict[str, list[GrammarTerm]],
) -> None:

    common_html = "\n".join(
        render_term(item)
        for item in common
    )

    module_sections = []

    for module, items in per_module.items():
        body = "\n".join(render_term(item) for item in items)

        module_sections.append(
            f"""
            <section class="module">
              <h2>{html.escape(module)}</h2>
              <p>{len(items)} module-local grammar term(s)</p>
              <ul>{body}</ul>
            </section>
            """
        )

    document = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta
    name="viewport"
    content="width=device-width,initial-scale=1"
  >
  <title>TriadicFrameworks · Grammar Spine</title>

  <style>
    :root {{
      color-scheme: dark;
      --bg: #090d12;
      --panel: #101720;
      --text: #e7edf5;
      --muted: #8fa0b4;
      --line: #263443;
      --accent: #76d7c4;
    }}

    body {{
      margin: 0;
      font-family:
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;
      background: var(--bg);
      color: var(--text);
    }}

    main {{
      max-width: 1180px;
      margin: 0 auto;
      padding: 3rem 1.25rem 5rem;
    }}

    h1 {{
      font-size: clamp(2rem, 5vw, 4rem);
      margin-bottom: .4rem;
    }}

    h2 {{
      border-bottom: 1px solid var(--line);
      padding-bottom: .5rem;
    }}

    .status {{
      color: var(--accent);
    }}

    .meta,
    .files {{
      font-size: .86rem;
      color: var(--muted);
      margin-top: .25rem;
    }}

    section {{
      margin: 2.5rem 0;
      padding: 1.3rem;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 12px;
    }}

    li {{
      margin: 1rem 0;
    }}

    strong {{
      color: var(--accent);
    }}
  </style>
</head>

<body>
<main>

  <p class="status">
    RTT: rtt=1 · coherence=declared ·
    drift=bounded · paradox=structural
  </p>

  <h1>Grammar Spine</h1>

  <p>
    Automatically extracted structural grammar for
    TriadicFrameworks.
  </p>

  <p>
    {module_count} discovered module.json file(s) ·
    {markdown_count} Markdown file(s) scanned
  </p>

  <section>
    <h2>Common Grammar</h2>
    <p>
      Terms occurring across two or more modules are promoted
      into the shared grammar layer.
    </p>

    <ul>
      {common_html}
    </ul>
  </section>

  {''.join(module_sections)}

</main>
</body>
</html>
"""

    GRAMMAR_HTML.write_text(
        document,
        encoding="utf-8",
    )


def main() -> None:
    module_files = discover_module_files()
    markdown_files = discover_markdown_files()

    inventory, module_roots = build_module_inventory(
        module_files
    )

    terms = extract_grammar(
        markdown_files,
        module_roots,
    )

    common, per_module = classify_terms(terms)

    write_module_manifest(inventory)

    write_grammar_json(
        markdown_files,
        common,
        per_module,
    )

    write_grammar_html(
        len(inventory),
        len(markdown_files),
        common,
        per_module,
    )

    print(
        "Spine build complete:",
        f"{len(inventory)} modules;",
        f"{len(markdown_files)} markdown files;",
        f"{len(common)} common grammar terms;",
        f"{sum(len(v) for v in per_module.values())}",
        "module-local terms.",
    )


if __name__ == "__main__":
    main()
