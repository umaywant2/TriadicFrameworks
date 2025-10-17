import time
import math

def harmonic_resonance(glyphs, cycles=3):
    for cycle in range(cycles):
        print(f"\n🔁 Cycle {cycle + 1}")
        for i, glyph in enumerate(glyphs):
            phase = math.sin((cycle + 1) * (i + 1))
            print(f"Glyph {glyph} → Phase {round(phase, 3)} → Resonance {'🧬' if phase > 0.5 else '🪙' if phase < -0.5 else '🧠'}")
            time.sleep(0.2)

if __name__ == "__main__":
    glyph_sequence = ["🧠", "🪙", "🍃", "🔐", "🧬"]
    harmonic_resonance(glyph_sequence)
