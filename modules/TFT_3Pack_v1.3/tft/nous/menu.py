import sys

# Import all 12 bots
from nous.bots import (
    bot_physics, bot_biology, bot_cs, bot_math,
    bot_chemistry, bot_engineering, bot_medicine,
    bot_economics, bot_music, bot_philosophy,
    bot_law, bot_art
)

def show_menu():
    options = [
        "Physics (Rocket Science) 🚀",
        "Biology (Genetics) 🧬",
        "Computer Science (Quantum Computing) 💻⚛️",
        "Mathematics (Topology & Nested Loops) ➿",
        "Chemistry (Isotopes & Resonance) ⚗️",
        "Engineering (Aerospace Corridors) ✈️",
        "Medicine (Resonant Ultrasound) 🩺",
        "Economics (Scarcity/Abundance Wrapper) 💰",
        "Music (Quadratic Harmonics) 🎶",
        "Philosophy (Consciousness Transfers) 🧠",
        "Law (Validator Scroll Protocols) ⚖️",
        "Art (Symbolic Compression Engines) 🎨"
    ]
    print("🌌 TriadicFrameworks Corridor Selector 🌌")
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")
    return options

def run_corridor(choice):
    corridor_map = {
        1: bot_physics,
        2: bot_biology,
        3: bot_cs,
        4: bot_math,
        5: bot_chemistry,
        6: bot_engineering,
        7: bot_medicine,
        8: bot_economics,
        9: bot_music,
        10: bot_philosophy,
        11: bot_law,
        12: bot_art
    }
    bot = corridor_map.get(choice)
    if bot:
        print(f"Activating corridor {choice}...")
        bot.activate()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    options = show_menu()
    try:
        choice = int(input("Enter corridor number: "))
        run_corridor(choice)
    except ValueError:
        print("Please enter a valid number.")
