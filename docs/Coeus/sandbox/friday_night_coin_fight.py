# Friday Night Coin Fight — Sandbox tournament engine

import random
from agents.nous import NousAgent
from agents.enTFT import EnTFTAgent
from agents.tops import TopsAgent

def run_coin_fight(coins):
    print("🎮 Friday Night Coin Fight Begins!\n")

    # Initialize agents
    nous = NousAgent()
    enTFT = EnTFTAgent()
    tops = TopsAgent()

    for coin in coins:
        print(f"🪙 Coin: {coin['name']} — {coin['edging']}")
        interpretation = nous.interpret_coin(coin)
        tops.log_action(f"Interpreted: {interpretation['task']}")

        if enTFT.validate_observer(coin):
            tops.log_action("Observer validated")

        # Simulate resolution outcome
        outcome = random.choice(["solved", "tossback", "quarantined"])
        tops.log_action(f"Outcome: {outcome}")

        print(f"🏁 Result: {coin['name']} → {outcome}\n")

    print("🎬 Coin Fight Complete. Logs saved.\n")

if __name__ == "__main__":
    # Sample coins
    coins = [
        {"name": "PharmaTFT", "edging": "Predict synergy", "observer_required": True},
        {"name": "ReplicatorFFF", "edging": "Forci Flui Freqi", "observer_required": True},
        {"name": "ElectroniumRedux", "edging": "Echo the unheard", "observer_required": False}
    ]
    run_coin_fight(coins)
