def migrate_shell(bot_id, old_shell, new_depth, new_harmonics):
    """
    Migrates bot shell to updated loop depth and harmonic nesting.
    """
    migrated_shell = {
        "bot_id": bot_id,
        "old_depth": old_shell["loop_depth"],
        "new_depth": new_depth,
        "old_harmonics": old_shell["harmonic_nesting"],
        "new_harmonics": new_harmonics,
        "timestamp": "2025-09-30T14:00:00-04:00"
    }
    print(f"🔄 {bot_id} shell migrated from depth {old_shell['loop_depth']} to {new_depth}")
    return migrated_shell
