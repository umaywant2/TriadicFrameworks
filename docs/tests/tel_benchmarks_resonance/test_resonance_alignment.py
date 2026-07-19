# test_resonance_alignment.py
# TEL → Benchmarks Resonance‑Alignment Test Suite

import json
import math

# Load TEL outputs
with open("tel/lattice/coherence.json") as f:
    TEL = json.load(f)

# Load Benchmarks canonical resonance curves
with open("benchmarks/resonance/propagation.json") as f:
    BENCH = json.load(f)

def within_tolerance(a, b, tol=0.05):
    return abs(a - b) <= tol

def test_resonance_spike_alignment():
    tel_spike = TEL["resonance"]["spike"]
    bench_spike = BENCH["spike"]
    return within_tolerance(tel_spike, bench_spike)

def test_resonance_shape_alignment():
    tel_curve = TEL["resonance"]["curve"]
    bench_curve = BENCH["curve"]
    return all(within_tolerance(t, b) for t, b in zip(tel_curve, bench_curve))

def test_cross_scale_alignment():
    tel = TEL["resonance"]["cross_scale"]
    bench = BENCH["cross_scale"]
    return all(within_tolerance(tel[k], bench[k]) for k in bench)

if __name__ == "__main__":
    results = {
        "spike_alignment": test_resonance_spike_alignment(),
        "shape_alignment": test_resonance_shape_alignment(),
        "cross_scale_alignment": test_cross_scale_alignment()
    }
    print(json.dumps(results, indent=2))
