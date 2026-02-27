from engine.simulate import run_sim
from engine.metrics import validate_runs
from engine.hashing import config_hash

def main(manifest_path, validator_cfg, repeats=5):
    cfg = load_yaml(manifest_path)
    sims = []
    for r in range(repeats):
        sim_out = run_sim(cfg, repeat_idx=r)
        sims.append(sim_out)
    report = validate_runs(sims, validator_cfg, cfg)
    report["config_hash"] = config_hash(cfg)
    save_report(report, cfg)
