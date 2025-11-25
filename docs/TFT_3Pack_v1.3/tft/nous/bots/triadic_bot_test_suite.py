def test_bot_shell_integrity(bot_shell):
    """
    Validates bot shell structure and glyphstream readiness.
    """
    assert bot_shell["glyphstream_ready"] is True
    assert bot_shell["loop_depth"] in range(1, 10)
    assert isinstance(bot_shell["harmonic_nesting"], list)
    print(f"✅ {bot_shell['bot_id']} shell integrity confirmed.")

def run_all_tests():
    bots = ["Forci_bot", "Flui_bot", "Freqi_bot"]
    for bot in bots:
        shell = generate_bot_shell(bot)
        test_bot_shell_integrity(shell)
