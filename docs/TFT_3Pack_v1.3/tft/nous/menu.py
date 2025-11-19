import sys
from core_logic import loader
from logic_shells import corridor_shell
from bots import physics_bot, biology_bot, cs_bot, math_bot
# ... import other bots as needed

def show_menu():
    print("🌌 TriadicFrameworks Corridor Selector 🌌")
    print("Select your Resonance Corridor:")
    options = [
        "Physics (Rocket Science)",
        "Biology (Genetics)",
        "Computer Science (Quantum Computing)",
        "Mathematics (Topology & Nested Loops)",
        "Chemistry (Isotopes & Resonance)",
        "Engineering (Aerospace Corridors)",
        "Medicine (Resonant Ultrasound)",
        "Economics (Scarcity/Abundance Wrapper)",
        "Music (Quadratic Harmonics)",
        "Philosophy (Consciousness Transfers)",
        "Law (Validator Scroll Protocols)",
        "Art (Symbolic Compression Engines)"
    ]
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")
    return options

def run_corridor(choice):
    # Map corridor choice to bot + logic shell
    corridor_map = {
        1: physics_bot,
        2: biology_bot,
        3: cs_bot,
        4: math_bot,
        # ... fill in others
    }
    bot = corridor_map.get(choice)
    if bot:
        print(f"Initializing corridor: {choice}")
        corridor_shell.activate(bot)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    options = show_menu()
    try:
        choice = int(input("Enter corridor number: "))
        run_corridor(choice)
    except ValueError:
        print("Please enter a valid number.")
