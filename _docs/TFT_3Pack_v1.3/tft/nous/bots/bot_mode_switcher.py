def switch_mode(bot_id, mode):
    """
    Switches bot execution mode (scan, confirm, remix, archive).
    """
    valid_modes = ["scan", "confirm", "remix", "archive"]
    if mode not in valid_modes:
        raise ValueError("Invalid mode.")
    print(f"🔄 {bot_id} switched to {mode} mode.")
    return {"bot_id": bot_id, "mode": mode}
