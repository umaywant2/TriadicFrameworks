import json

# Load bot registry
with open('bots.json', 'r') as f:
    bots = json.load(f)

def summon_bot(stub):
    for bot in bots:
        if bot['invocation_stub'] == stub or bot['glyph'] == stub:
            print(f"🔹 {bot['glyph']} {bot['name']} — {bot['description']}")
            return bot
    print("⚠️ Bot not found.")
    return None

def filter_bots(domain=None, tier=None, trigger=None):
    results = []
    for bot in bots:
        if (not domain or bot['domain'] == domain) and \
           (not tier or bot['tier'] == tier) and \
           (not trigger or bot['activation_trigger'] == trigger):
            results.append(bot)
    return results

# Example usage
if __name__ == "__main__":
    summon_bot("triadi")  # or summon_bot("🧠")
    core_bots = filter_bots(domain="Core")
    for b in core_bots:
        print(f"{b['glyph']} {b['name']} — {b['function']}")

