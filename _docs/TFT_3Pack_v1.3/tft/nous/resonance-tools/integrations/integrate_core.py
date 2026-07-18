# integrate_core.py
from resonant_time import ResonantTime
from tft_core import TFT
from fff_core import FFF
from numbers_core import TriadicNumbers

class Integrations:
    """
    Meta-tool: orchestrates Resonant-Time, TFT, and FFF.
    """

    def __init__(self):
        self.rt = ResonantTime()
        self.tft = TFT()
        self.fff = FFF()
        self.numbers = TriadicNumbers()

    def define(self):
        return {
            "Integrations": "Meta-tool combining Resonant-Time, TFT, and FFF",
            "Purpose": "Demonstrates orchestration of temporal, technological, and physical triads"
        }

    def demo_pipeline(self):
        cycle = self.rt.cycle(3)
        mapped = self.numbers.map_sequence(" ".join(cycle))
        cpu_map = self.tft.apply("cpu")
        forces = self.fff.simulate_forces(2)

        return {
            "Resonant-Time": cycle,
            "Triadic Numbers": mapped,
            "TFT (CPU)": cpu_map,
            "FFF (Forces)": forces
        }

    def dashboard(self, domain="cpu"):
        return {
            "Domain": domain,
            "Time": self.rt.cycle(3, ascii=True),
            "TFT": self.tft.apply(domain),
            "FFF": {
                "forces": self.fff.simulate_forces(1),
                "fluids": self.fff.simulate_fluids(1),
                "frequency": self.fff.simulate_frequency(1)
            }
        }

