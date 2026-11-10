from pathlib import Path

import pytest

from scripts.build_spine import (
    GrammarTerm,
    add_term,
    classify_terms,
    module_identity,
    normalize_term,
    owning_module,
    valid_term,
)


def test_normalize_term_collapses_whitespace():
    assert normalize_term("  Resonance   Time  ") == "Resonance Time"


def test_normalize_term_removes_surrounding_punctuation():
    assert normalize_term("  (Coherence),  ") == "Coherence"


@pytest.mark.parametrize(
    "term",
    [
        "Coherence",
        "ΔR",
        "RTT",
        "Observer_State",
        "A -> B",
    ],
)
def test_valid_grammar_terms(term):
    assert valid_term(term)


@pytest.mark.parametrize(
    "term",
    [
        "",
        "1",
        "1.2.3",
        "README",
        "TODO",
        "https://example.com",
    ],
)
def test_rejects_non_grammar_terms(term):
    assert not valid_term(term)


def test_module_identity_prefers_explicit_id(tmp_path):
    module_file = tmp_path / "alpha" / "module.json"

    payload = {
        "id": "rtt.alpha",
        "name": "Alpha Module",
    }

    assert module_identity(module_file, payload) == "rtt.alpha"


def test_module_identity_falls_back_to_name(tmp_path):
    module_file = tmp_path / "alpha" / "module.json"

    payload = {
        "name": "Alpha Module",
    }

    assert module_identity(module_file, payload) == "Alpha Module"


def test_module_identity_falls_back_to_directory(tmp_path):
    module_file = tmp_path / "alpha" / "module.json"

    assert module_identity(module_file, {}) == "alpha"


def test_add_term_records_provenance(tmp_path, monkeypatch):
    import scripts.build_spine as build_spine

    monkeypatch.setattr(build_spine, "ROOT", tmp_path)

    source = tmp_path / "docs" / "alpha" / "index.md"
    source.parent.mkdir(parents=True)
    source.write_text("# Alpha", encoding="utf-8")

    terms = {}

    add_term(
        terms,
        "Coherence",
        "alpha",
        source,
        "defined-term",
    )

    item = terms["coherence"]

    assert item.term == "Coherence"
    assert item.modules == {"alpha"}
    assert item.files == {"docs/alpha/index.md"}
    assert item.occurrences == 1
    assert item.kinds == {"defined-term"}


def test_add_term_merges_case_insensitively(tmp_path, monkeypatch):
    import scripts.build_spine as build_spine

    monkeypatch.setattr(build_spine, "ROOT", tmp_path)

    source = tmp_path / "docs" / "alpha.md"
    source.parent.mkdir(parents=True)

    terms = {}

    add_term(
        terms,
        "Coherence",
        "alpha",
        source,
        "heading",
    )

    add_term(
        terms,
        "coherence",
        "alpha",
        source,
        "inline-code",
    )

    assert len(terms) == 1

    item = terms["coherence"]

    assert item.occurrences == 2
    assert item.kinds == {"heading", "inline-code"}


def test_term_in_one_module_remains_module_local():
    terms = {
        "resonance": GrammarTerm(
            term="Resonance",
            modules={"rtt"},
            files={"docs/rtt/index.md"},
            occurrences=3,
            kinds={"heading"},
        )
    }

    common, per_module = classify_terms(terms)

    assert common == []
    assert "rtt" in per_module
    assert per_module["rtt"][0].term == "Resonance"


def test_term_in_two_modules_becomes_common():
    terms = {
        "coherence": GrammarTerm(
            term="Coherence",
            modules={"rtt", "clarity"},
            files={
                "docs/rtt/index.md",
                "docs/clarity/index.md",
            },
            occurrences=4,
            kinds={"defined-term"},
        )
    }

    common, per_module = classify_terms(terms)

    assert len(common) == 1
    assert common[0].term == "Coherence"

    assert "rtt" not in per_module
    assert "clarity" not in per_module


def test_occurrence_count_does_not_make_term_common():
    """
    Critical invariant:

    Common means cross-module, not merely frequent.
    """

    terms = {
        "operator": GrammarTerm(
            term="Operator",
            modules={"rtt"},
            files={"docs/rtt/index.md"},
            occurrences=100,
            kinds={"defined-term"},
        )
    }

    common, per_module = classify_terms(terms)

    assert common == []
    assert per_module["rtt"][0].term == "Operator"


def test_owning_module_uses_nearest_module_root(
    tmp_path,
    monkeypatch,
):
    import scripts.build_spine as build_spine

    monkeypatch.setattr(build_spine, "ROOT", tmp_path)
    monkeypatch.setattr(
        build_spine,
        "DOCS",
        tmp_path / "docs",
    )

    module_root = tmp_path / "docs" / "rtt"

    markdown = (
        module_root
        / "operators"
        / "coherence.md"
    )

    markdown.parent.mkdir(parents=True)
    markdown.write_text("# Coherence", encoding="utf-8")

    module_roots = {
        module_root.resolve(): "rtt",
    }

    assert owning_module(markdown, module_roots) == "rtt"


def test_common_classification_is_deterministic():
    terms = {
        "zeta": GrammarTerm(
            term="Zeta",
            modules={"alpha", "beta"},
        ),
        "alpha": GrammarTerm(
            term="Alpha",
            modules={"alpha", "beta"},
        ),
    }

    common, _ = classify_terms(terms)

    assert [item.term for item in common] == [
        "Alpha",
        "Zeta",
    ]

def test_end_to_end_grammar_extraction(tmp_path, monkeypatch):
    import scripts.build_spine as build_spine

    docs = tmp_path / "docs"

    alpha = docs / "alpha"
    beta = docs / "beta"

    alpha.mkdir(parents=True)
    beta.mkdir(parents=True)

    (alpha / "module.json").write_text(
        '{"id": "alpha"}',
        encoding="utf-8",
    )

    (beta / "module.json").write_text(
        '{"id": "beta"}',
        encoding="utf-8",
    )

    (alpha / "index.md").write_text(
        """
# Alpha Grammar

**Coherence**

`AlphaOperator`
""",
        encoding="utf-8",
    )

    (beta / "index.md").write_text(
        """
# Beta Grammar

**Coherence**

`BetaOperator`
""",
        encoding="utf-8",
    )

    monkeypatch.setattr(build_spine, "ROOT", tmp_path)
    monkeypatch.setattr(build_spine, "DOCS", docs)

    module_files = build_spine.discover_module_files()

    _, module_roots = build_spine.build_module_inventory(
        module_files
    )

    markdown_files = build_spine.discover_markdown_files()

    terms = build_spine.extract_grammar(
        markdown_files,
        module_roots,
    )

    common, per_module = build_spine.classify_terms(terms)

    common_names = {
        item.term.casefold()
        for item in common
    }

    assert "coherence" in common_names

    assert any(
        item.term == "AlphaOperator"
        for item in per_module["alpha"]
    )

    assert any(
        item.term == "BetaOperator"
        for item in per_module["beta"]
    )
