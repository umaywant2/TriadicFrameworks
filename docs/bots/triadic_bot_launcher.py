def launch_bots(shard, job_id):
    """
    Launches bots based on shard string (e.g., 'FLQ') for a given job.
    """
    active_bots = {
        "F": "Forci_bot",
        "L": "Flui_bot",
        "Q": "Freqi_bot"
    }
    launched = [active_bots[c] for c in shard if c in active_bots]

    print(f"Launching bots for job {job_id}: {', '.join(launched)}")
    return launched
