#!/usr/bin/env python3
import math, datetime as dt
from typing import List, Dict, Tuple

def half_life_decay(days_since: float, half_life_days: float) -> float:
    return math.pow(0.5, days_since / half_life_days)

def harmonic_score(similarity: float, alignment: float, relevance: float,
                   validator: float, days_since: float, half_life_days: float) -> float:
    decay = half_life_decay(days_since, half_life_days)
    return round((similarity * alignment * relevance) * decay * validator, 4)

def resonance_parity(triads: List[Dict], goal_tag: str) -> float:
    aligned = sum(t['H'] for t in triads if goal_tag in t.get('tags', []))
    total = sum(t['H'] for t in triads)
    return round(aligned / total, 4) if total else 0.0

def drift_score(embedding_today: List[float], embedding_last: List[float]) -> float:
    # Cosine distance
    dot = sum(a*b for a, b in zip(embedding_today, embedding_last))
    mag_a = math.sqrt(sum(a*a for a in embedding_today))
    mag_b = math.sqrt(sum(b*b for b in embedding_last))
    return round(1 - (dot / (mag_a * mag_b)), 4)

def make_triad(a: str, b: str, c: str,
               roles: Tuple[str, str, str], harmonics: Dict,
               decay_meta: Dict, provenance: Dict, tags: List[str]=[]) -> Dict:
    H = harmonic_score(harmonics['similarity'], harmonics['authority'],
                       harmonics['relevance'], harmonics['validator'],
                       decay_meta['days_since'], decay_meta['half_life_days'])
    return {
        "id": f"T:{a}|{b}|{c}",
        "roles": dict(zip(["A","B","C"], roles)),
        "harmonics": harmonics,
        "decay": decay_meta,
        "H": H,
        "provenance": provenance,
        "tags": tags
    }
