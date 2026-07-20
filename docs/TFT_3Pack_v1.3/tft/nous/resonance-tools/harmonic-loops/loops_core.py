# loops_core.py
import json

class HarmonicLoops:
    """
    Core class for Harmonic Nested Loops.
    Models feedback, oscillation, and recursion.
    """

    def __init__(self):
        self.structure = {}

    def nest(self, depth=2):
        """Generate nested loops up to given depth."""
        def build(level):
            if level == 0:
                return "∅"
            return {"loop": build(level-1)}
        self.structure = build(depth)
        return self.structure

    def feedback(self, iterations=5):
        """Simulate resonance amplification over iterations."""
        return [f"Resonance level {i+1}" for i in range(iterations)]

    def export(self, depth=2):
        """Export nested loop structure as JSON."""
        return json.dumps(self.nest(depth), indent=2)

