# numbers_core.py
import json

class TriadicNumbers:
    """
    Core class for Triadic Number Genesis (1D–9D).
    Encodes dimensional triads and symbolic mappings.
    """

    def __init__(self):
        self.genesis_map = {
            1: ["Line", "Arrow", "Origin"],
            2: ["Plane", "Symmetry", "Asymmetry"],
            3: ["Volume", "Cycle", "Spark"],
            4: ["Time", "Flow", "Event"],
            5: ["Resonance", "Loop", "Disruption"],
            6: ["Recursion", "Pattern", "Novelty"],
            7: ["Legacy", "Memory", "Rebirth"],
            8: ["Lattice", "Network", "Fractal"],
            9: ["Infinity", "Mythos", "Singularity"]
        }

    def genesis(self, upto=9):
        return {d: self.genesis_map[d] for d in range(1, upto+1)}

    def map_sequence(self, sequence):
        """
        Map a symbolic sequence (E, M, OC) into triadic numbers.
        Example: "E M OC" -> [1D, 2D, 3D]
        """
        tokens = sequence.split()
        mapping = []
        for i, token in enumerate(tokens):
            dim = (i % 9) + 1
            mapping.append({f"{dim}D": {"symbol": token, "triad": self.genesis_map[dim]}})
        return mapping

    def export(self, upto=9):
        return json.dumps(self.genesis(upto), indent=2)

