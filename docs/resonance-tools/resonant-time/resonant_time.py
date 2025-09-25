```python
# resonant_time.py

class ResonantTime:
    """
    Core class for modeling Resonant-Time.
    Encodes triadic interplay of E (Arrow), M (Clock), and OC (Originating Change).
    """

    def __init__(self):
        self.sequence = []

    def define(self):
        return {
            "E": "Arrow / Conservative Change",
            "M": "Clock / Symmetric Change",
            "OC": "Originating Change / Asymmetric Spark",
            "Resonant-Time": "Dimension of asymmetric resonance; emerges only when E, M, and OC interlock."
        }

    def cycle(self, steps=3):
        triad = ["E", "M", "OC"]
        self.sequence = [triad[i % 3] for i in range(steps)]
        return self.sequence

    def compare(self):
        return {
            "Relativity": "Clocks without arrows",
            "Thermodynamics": "Arrows without clocks",
            "Resonant-Time": "Arrows + Clocks + Originating Change (true temporal resonance)"
        }

