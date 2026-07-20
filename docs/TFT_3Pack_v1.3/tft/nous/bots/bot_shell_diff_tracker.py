def track_shell_diff(old_shell, new_shell):
    """
    Compares bot shell versions and logs harmonic evolution.
    """
    diff = {
        "bot_id": old_shell["bot_id"],
        "depth_change": new_shell["loop_depth"] - old_shell["loop_depth"],
        "harmonic_diff": list(set(new_shell["harmonic_nesting"]) - set(old_shell["harmonic_nesting"])),
        "timestamp": new_shell["timestamp"]
    }
    print(f"🔍 Shell diff for {diff['bot_id']}: Depth Δ {diff['depth_change']}, Harmonics Δ {diff['harmonic_diff']}")
    return diff
