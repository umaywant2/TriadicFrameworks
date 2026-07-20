def update_bot_shell(bot_id, new_depth, new_harmonics):
    """
    Updates bot shell with new loop depth and harmonic nesting.
    """
    shell = {
        "bot_id": bot_id,
        "loop_depth": new_depth,
        "harmonic_nesting": new_harmonics,
        "glyphstream_ready": True,
        "timestamp": "2025-09-30T13:58:00-04:00"
    }
    print(f"🔄 {bot_id} shell updated: Depth {new_depth}, Harmonics {new_harmonics}")
    return shell
