def tally_votes(blade_scores):
    avg_scores = {
        blade: sum(scores) / len(scores)
        for blade, scores in blade_scores.items()
    }
    return avg_scores

def check_resonance(avg_scores):
    return all(score >= 2.5 for score in avg_scores.values())
