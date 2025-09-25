```python
# tfe_core.py

class TriadicFrameworks:
    """
    Core class for Triadic Frameworks for Everything (TFE).
    Encodes triadic scaffolding across domains.
    """

    def __init__(self):
        self.domains = {
            "physics": ["E=Arrow (force)", "M=Clock (oscillation)", "OC=Origin (asymmetry)"],
            "architecture": ["E=Load paths", "M=Symmetry/geometry", "OC=Innovation/novel form"],
            "pedagogy": ["E=Curriculum flow", "M=Assessment cycles", "OC=Creative spark"],
        }

    def define(self):
        return {
            "TFE": "Triadic Frameworks for Everything",
            "Purpose": "Encodes triadic grammar (E, M, OC) across domains",
            "Role": "Skeleton of the resonance suite"
        }

    def apply(self, domain):
        return self.domains.get(domain, f"No triadic mapping defined for {domain}")

    def list_domains(self):
        return list(self.domains.keys())
