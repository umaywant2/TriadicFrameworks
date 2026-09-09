import os
import json
import shutil

ROOT = "docs"
CLARITY_ROOT = os.path.join(ROOT, "Clarity_Canon")

STRUCTURAL_KEYS = {
    "generative": ["resonance_source","structural_seed","temporal_onset"],
    "transformational": ["resonant_input","structural_transformation","temporal_modulation"],
    "coherence": ["resonant_field","structural_alignment","temporal_continuity"],
}
HARMONIC_KEYS = {
    "resonance_harmonic": ["resonant_mode","harmonic_factor","temporal_phase"],
    "structural_harmonic": ["structural_pattern","harmonic_coupling","temporal_cycle"],
    "coherence_harmonic": ["coherence_field","harmonic_alignment","temporal_stability"],
}
COHERENCE_KEYS = {
    "coherence_core": ["coherence_field","coherence_alignment","coherence_stability"],
    "coherence_harmonic": ["harmonic_alignment","harmonic_balance","harmonic_resonance"],
    "coherence_temporal": ["temporal_continuity","temporal_stability","temporal_resonance"],
}

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def write(path, text):
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def write_json(path, obj):
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2)

def scaffold_clarity_canon():
    print("✔ Scaffolding /docs/Clarity_Canon")

    # Root docs
    write(
        os.path.join(CLARITY_ROOT, "README.md"),
        "# Clarity Canon\n\nA clean, auto‑generated, teaching‑grade RTT canon aligned with MCP.\n",
    )
    write(
        os.path.join(CLARITY_ROOT, "index.html"),
        "<!DOCTYPE html><html><head><meta charset=\"utf-8\"><title>Clarity Canon</title></head>"
        "<body><h1>Clarity Canon</h1><p>Teaching‑grade RTT canon, auto‑generated from TriadicFrameworks.</p></body></html>",
    )
    write(
        os.path.join(CLARITY_ROOT, "session_context.md"),
        "# Clarity Canon Session Context\n\nThis canon is designed for teaching, examples, and MCP‑aligned operators.\n",
    )
    write_json(
        os.path.join(CLARITY_ROOT, "metadata.json"),
        {
            "name": "Clarity Canon",
            "purpose": "Teaching‑grade RTT canon, auto‑generated and self‑healing.",
            "version": "1.0.0",
            "source": "TriadicFrameworks",
            "mcp_aligned": True,
        },
    )
    write(
        os.path.join(CLARITY_ROOT, "DOC_MAP.md"),
        "# Clarity Canon Document Map\n\n- core/\n- triads/\n- modules/\n- maps/\n- observatory/\n- mcp/\n",
    )

    # Core
    core = os.path.join(CLARITY_ROOT, "core")
    write(
        os.path.join(core, "clarity_principles.md"),
        "# Clarity Principles\n\nThis document describes the core principles of spectral clarity and RTT teaching.\n",
    )
    write(
        os.path.join(core, "clarity_equations.md"),
        "# Clarity Equations\n\nPlaceholder for formal clarity equations and validator pulses.\n",
    )
    write(
        os.path.join(core, "clarity_operators.md"),
        "# Clarity Operators\n\nOperator‑grade descriptions of RTT actions, aligned with MCP routes.\n",
    )
    write(
        os.path.join(core, "clarity_examples.md"),
        "# Clarity Examples\n\nMinimal, noise‑free examples demonstrating RTT concepts.\n",
    )

    # Triads
    triads_dir = os.path.join(CLARITY_ROOT, "triads")
    write_json(os.path.join(triads_dir, "structural_triads.json"), STRUCTURAL_KEYS)
    write_json(os.path.join(triads_dir, "harmonic_triads.json"), HARMONIC_KEYS)
    write_json(os.path.join(triads_dir, "coherence_triads.json"), COHERENCE_KEYS)

    # Modules
    modules_dir = os.path.join(CLARITY_ROOT, "modules")
    template = {
        "module": {
            "name": "clarity_example_module",
            "category": "clarity_teaching",
            "canon_ref": "/docs/spine/spine.json",
            "inherit": {
                "canon": True,
                "session_context": True,
                "triad_alias_resolution": True,
            },
            "rtt": {
                "layer": 1,
                "source": "https://www.triadicframeworks.org/_ideas/Resonance-Time_Theory.html",
            },
            "ai": {
                "initialization": {
                    "load_spine_first": True,
                    "load_canon_first": True,
                    "apply_session_context": True,
                    "triad_validation": True,
                },
                "metadata": {
                    "purpose": "Teaching RTT via Clarity Canon.",
                    "audience": "Operators, students, autonomous agents.",
                    "keywords": ["RTT","Clarity","Triads","Teaching"],
                    "version": "1.0.0",
                    "mode": "teaching",
                },
            },
            "triads": {
                "structural_triads": {},
                "harmonic_triads": {},
                "coherence_triads": {},
            },
            "dependencies": [],
        }
    }
    write_json(os.path.join(modules_dir, "clarity_module_template.json"), template)
    write_json(os.path.join(modules_dir, "clarity_module_example.json"), template)

    # Maps
    maps_dir = os.path.join(CLARITY_ROOT, "maps")
    write(
        os.path.join(maps_dir, "clarity_map.md"),
        "# Clarity Map\n\nHigh‑level map of Clarity Canon structures and teaching flows.\n",
    )
    write(
        os.path.join(maps_dir, "clarity_purity_map.svg"),
        "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"800\" height=\"400\">"
        "<rect x=\"0\" y=\"0\" width=\"800\" height=\"400\" fill=\"#ffffff\"/>"
        "<text x=\"20\" y=\"40\" font-family=\"system-ui\" font-size=\"20\">Clarity Purity Map (placeholder)</text>"
        "</svg>",
    )
    write(
        os.path.join(maps_dir, "clarity_consistency_map.svg"),
        "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"800\" height=\"400\">"
        "<rect x=\"0\" y=\"0\" width=\"800\" height=\"400\" fill=\"#ffffff\"/>"
        "<text x=\"20\" y=\"40\" font-family=\"system-ui\" font-size=\"20\">Clarity Consistency Map (placeholder)</text>"
        "</svg>",
    )

    # Observatory
    observatory_dir = os.path.join(CLARITY_ROOT, "observatory")
    write(
        os.path.join(observatory_dir, "clarity_observatory.html"),
        "<!DOCTYPE html><html><head><meta charset=\"utf-8\">"
        "<title>Clarity Canon Observatory</title></head>"
        "<body><h1>Clarity Canon Observatory</h1>"
        "<p>Observatory for structural, purity, and consistency views of the Clarity Canon.</p></body></html>",
    )
    write_json(os.path.join(observatory_dir, "clarity_fingerprint.json"), {})
    write_json(os.path.join(observatory_dir, "clarity_delta.json"), {})

    # MCP
    mcp_dir = os.path.join(CLARITY_ROOT, "mcp")
    write_json(
        os.path.join(mcp_dir, "clarity_mcp_manifest.json"),
        {
            "name": "Clarity Canon MCP",
            "description": "MCP‑aligned manifest for the Clarity Canon teaching substrate.",
            "version": "1.0.0",
        },
    )
    write_json(
        os.path.join(mcp_dir, "clarity_mcp_routes.json"),
        {
            "routes": [
                {"name": "get_clarity_principles", "path": "/core/clarity_principles.md"},
                {"name": "get_clarity_equations", "path": "/core/clarity_equations.md"},
                {"name": "get_clarity_examples", "path": "/core/clarity_examples.md"},
            ]
        },
    )
    write(
        os.path.join(mcp_dir, "clarity_mcp_examples.md"),
        "# Clarity MCP Examples\n\nExample MCP interactions with the Clarity Canon.\n",
    )

def main():
    print("\n=== TriadicFrameworks Clarity Canon Builder ===\n")

    scaffold_clarity_canon()

    print("\n✔ Clarity Canon scaffolded at /docs/Clarity_Canon")
    print("✨ First teaching‑grade, MCP‑aligned, auto‑generated canon structure is ready.\n")

if __name__ == "__main__":
    main()
