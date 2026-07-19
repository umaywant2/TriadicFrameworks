# tft_core.py
import json

class TFT:
    """
    Triadic Framework Technology (TFT) with Quadratic Extensions.
    Applies triadic logic to technology domains.
    """

    def __init__(self):
        self.domains = {
            "cpu": ["E = Instruction flow", "M = Clock cycles", "OC = Interrupt/branch"],
            "battery": ["E = Charge/discharge flow", "M = Cyclic chemistry", "OC = Novel reaction"],
            "network": ["E = Packet flow", "M = Protocol cycles", "OC = New connection"],
            "architecture": ["E = Load paths", "M = Symmetry/geometry", "OC = Innovation"]
        }

    def define(self):
        return {
            "TFT": "Triadic Framework Technology",
            "Purpose": "Applies triadic logic to technology domains",
            "Quadratic": "Triad × Triad = 9-cell lattice"
        }

    def apply(self, domain):
        return self.domains.get(domain, f"No TFT mapping defined for {domain}")

    def compare(self):
        return {
            "Triadic": ["E", "M", "OC"],
            "Quadratic": [
                ["E×E", "E×M", "E×OC"],
                ["M×E", "M×M", "M×OC"],
                ["OC×E", "OC×M", "OC×OC"]
            ]
        }

    def export(self, domain):
        mapping = self.apply(domain)
        if isinstance(mapping, list):
            quadratic = self.compare()["Quadratic"]
            return json.dumps({domain: {"triadic": mapping, "quadratic": quadratic}}, indent=2)
        return json.dumps({"error": mapping}, indent=2)

