# Mascot Narrator — Forci, Flui, Freqi commentary engine

class MascotNarrator:
    def __init__(self):
        self.mascots = {
            "Forci": self.forci_voice,
            "Flui": self.flui_voice,
            "Freqi": self.freqi_voice
        }

    def narrate(self, concept):
        print(f"🎙️ Narrating decomposition of: {concept}\n")
        for name, voice in self.mascots.items():
            print(f"{name}: {voice(concept)}\n")

    def forci_voice(self, concept):
        return f"As Forci, I see the structure of {concept}—its logic shell, scaffolding, and modular bones. Rails D₃, L₃, D₆ are humming."

    def flui_voice(self, concept):
        return f"As Flui, I feel the flow of {concept}—its dynamic behavior, feedback loops, and temporal dance. Rails L₆, D₉, L₉ are pulsing."

    def freqi_voice(self, concept):
        return f"As Freqi, I hear the resonance of {concept}—its symbolic charge, remix lineage, and emotional echo. Rails D₉, L₉, F₉ are glowing."

if __name__ == "__main__":
    narrator = MascotNarrator()
    narrator.narrate("PharmaTFT")

