import time
import random

def corridor_throttle(corridor, glyph, intensity=1.0):
    delay = round(random.uniform(0.2, 1.5) * intensity, 3)
    print(f"🧠 Throttle engaged → Corridor: {corridor} | Glyph: {glyph} | Delay: {delay}s")
    time.sleep(delay)
    return delay

def throttle_sequence(glyphs, corridor_map):
    for glyph in glyphs:
        corridor = corridor_map.get(glyph, "Unknown")
        corridor_throttle(corridor, glyph)

if __name__ == "__main__":
    glyphs = ["🧠", "🪙", "🍃", "🔐", "🧬"]
    corridor_map = {
        "🧠": "Encryption",
        "🪙": "Remix Economy",
        "🍃": "Climate",
        "🔐": "Governance",
        "🧬": "Mutation"
    }
    throttle_sequence(glyphs, corridor_map)
