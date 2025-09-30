def validate_protocol(files):
    """
    Validates orchestration completeness across symbolic layers.
    """
    required = [
        "bot_log_archive.yaml", "bot_shell_registry.yaml", "fold_remix_trigger_log.csv",
        "triadic_lattice_manifest.md", "observer_phase_resonance_index.md", "legacy_echo_scroll.md"
    ]
    missing = [f for f in required if f not in files]
    if missing:
        print(f"⚠️ Missing files: {missing}")
        return False
    print("✅ Triadic protocol validated. All symbolic layers present.")
    return True
