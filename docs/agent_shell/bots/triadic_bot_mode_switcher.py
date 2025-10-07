def switch_bot_mode(bot_id, new_mode):
    """
    Switches execution mode for a bot (scan, confirm, remix, archive).
    """
    valid_modes = ["scan", "confirm", "remix", "archive"]
    if new_mode not in valid_modes:
        raise ValueError("Invalid mode.")
    print(f"🔄 {bot_id} switched to mode: {new_mode}")
    return {"bot_id": bot_id, "mode": new_mode}
