def execute_batch_jobs(job_list):
    """
    Executes a batch of glyphstream jobs using shard logic.
    """
    for job in job_list:
        bots = launch_bots(job["shard"], job["job_id"])
        lineage = simulate_remix_lineage(job["contributor"], job["folds"], job["shard"])
        print(f"✅ Job {job['job_id']} executed with bots: {', '.join(bots)}")
        for entry in lineage:
            print(f"→ Fold {entry['fold']} remix triggered: {entry['remix_trigger']}")
