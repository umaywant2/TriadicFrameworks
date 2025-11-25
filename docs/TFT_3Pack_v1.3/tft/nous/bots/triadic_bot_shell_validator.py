def validate_shell_structure(shell):
    """
    Validates bot shell for glyphstream readiness and harmonic integrity.
    """
    assert shell["glyphstream_ready"] is True
    assert isinstance(shell["harmonic_nesting"], list)
    assert shell["loop_depth"] == len(shell["harmonic_nesting"]) or shell["loop_depth"] <= 9
    print(f"✅ Shell for {shell['bot_id']} validated.")
    return True
