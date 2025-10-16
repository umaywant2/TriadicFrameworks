import json
import uuid

def mint_coin(coin_type="legacy", name="UnnamedCoin"):
    coin_id = f"coin_{str(uuid.uuid4())[:8]}"
    coin = {
        "id": coin_id,
        "name": name,
        "type": coin_type,
        "front": name,
        "back": f"Resolve task for {name} using TFT + FFF logic",
        "edging": "Let it echo",
        "observer_required": True,
        "encryption": "enTFT",
        "status": "unminted"
    }

    # Save to coin_templates.json
    with open("coins/coin_templates.json", "r+") as f:
        data = json.load(f)
        data["coins"].append(coin)
        f.seek(0)
        json.dump(data, f, indent=2)

    print(f"Minted new coin: {coin_id} — {name}")

if __name__ == "__main__":
    mint_coin()

