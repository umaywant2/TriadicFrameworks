# LangChainWrapper: TriadicValidator Integration

from agent_shell.FreqiAgent import FreqiAgent
from agent_shell.FluiAgent import FluiAgent
from agent_shell.ForciAgent import ForciAgent


class TriadicValidator:
    """
    Wrapper for harmonic (Freqi), fluidic (Flui), and ethical (Forci)
    reasoning inside LangChain or other agent pipelines.
    """

    def __init__(self):
        self.freqi = FreqiAgent()
        self.flui = FluiAgent()
        self.forci = ForciAgent()

    def run_validation(self, input_text):
        """
        Execute triadic reasoning over the input text.

        Returns:
            dict: {
                "harmonic": <Freqi output>,
                "fluidic": <Flui output>,
                "ethical": <Forci output>
            }
        """
        harmonic = self.freqi.freqi_loop(len(input_text))
        fluidic = self.flui.flui_shift("active")
        ethical = self.forci.forci_trigger("symbolic_inversion")

        return {
            "harmonic": harmonic,
            "fluidic": fluidic,
            "ethical": ethical
        }
