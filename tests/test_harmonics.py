from scripts.hippocampus_utils import harmonic_score, half_life_decay

def test_decay_half_life():
    assert half_life_decay(0, 21) == 1
    assert round(half_life_decay(21, 21), 4) == 0.5

def test_harmonic_score_nonzero():
    H = harmonic_score(0.8, 0.9, 0.85, 0.95, 10, 21)
    assert H > 0
    assert H <= 1
