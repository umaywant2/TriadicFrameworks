import importlib.util
import sys
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "build_html_mirror.py"
)

SPEC = importlib.util.spec_from_file_location(
    "build_html_mirror",
    SCRIPT_PATH,
)

assert SPEC is not None
assert SPEC.loader is not None

mirror = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = mirror
SPEC.loader.exec_module(mirror)


def test_doc_map_rewrites_single_quoted_md_targets():
    source = """
const DOC_MAP = {
    "README": '/docs/Foo/README.md',
    "Overview": '/docs/Foo/overview.md',
};
"""

    expected = """
const DOC_MAP = {
    "README": '/docs/Foo/README.html',
    "Overview": '/docs/Foo/overview.html',
};
"""

    assert mirror.rewrite_index_doc_map(source) == expected


def test_doc_map_rewrites_double_quoted_md_targets():
    source = """
const DOC_MAP = {
    "README": "/docs/Foo/README.md",
    "Overview": "/docs/Foo/overview.md",
};
"""

    expected = """
const DOC_MAP = {
    "README": "/docs/Foo/README.html",
    "Overview": "/docs/Foo/overview.html",
};
"""

    assert mirror.rewrite_index_doc_map(source) == expected


def test_doc_map_does_not_modify_content_outside_doc_map():
    source = """
<a href="/docs/outside.md">Outside</a>

const DOC_MAP = {
    "README": '/docs/Foo/README.md',
};

<script>
const OTHER_MAP = {
    "Other": '/docs/other.md',
};
</script>
"""

    result = mirror.rewrite_index_doc_map(source)

    assert 'href="/docs/outside.md"' in result
    assert "'/docs/Foo/README.html'" in result
    assert "'/docs/other.md'" in result


def test_doc_map_preserves_non_markdown_targets():
    source = """
const DOC_MAP = {
    "HTML": '/docs/Foo/index.html',
    "JSON": '/docs/Foo/module.json',
    "SVG": '/docs/Foo/diagram.svg',
    "Anchor": '#section',
};
"""

    assert mirror.rewrite_index_doc_map(source) == source


def test_doc_map_rewrites_multiple_markdown_entries():
    source = """
const DOC_MAP = {
    "One": '/docs/One.md',
    "Two": '/docs/Two.md',
    "Three": '/docs/Three.md',
};
"""

    result = mirror.rewrite_index_doc_map(source)

    assert "'/docs/One.html'" in result
    assert "'/docs/Two.html'" in result
    assert "'/docs/Three.html'" in result
    assert ".md'" not in result


def test_missing_doc_map_is_unchanged():
    source = """
<html>
<body>
<a href="/docs/Foo/README.md">README</a>
</body>
</html>
"""

    assert mirror.rewrite_index_doc_map(source) == source


def test_similarly_named_javascript_object_is_unchanged():
    source = """
const DOCUMENT_MAP = {
    "README": '/docs/Foo/README.md',
};
"""

    assert mirror.rewrite_index_doc_map(source) == source


def test_doc_map_only_rewrites_md_before_quote():
    source = """
const DOC_MAP = {
    "Markdown": '/docs/Foo/README.md',
    "Backup": '/docs/Foo/README.md.backup',
    "Text": 'README.md is canonical',
};
"""

    result = mirror.rewrite_index_doc_map(source)

    assert "'/docs/Foo/README.html'" in result
    assert "'/docs/Foo/README.md.backup'" in result
    assert "'README.md is canonical'" in result


def test_index_navigation_rewrites_readme_fallback():
    source = """
function loadFromHash() {
    const key = window.location.hash.replace('#', '');
    if (DOC_MAP[key]) {
        loadDoc(DOC_MAP[key]);
    } else {
        loadDoc('README.md');
    }
}
"""

    result = mirror.rewrite_index_navigation(source)

    assert "loadDoc('README.html');" in result
    assert "loadDoc('README.md');" not in result
