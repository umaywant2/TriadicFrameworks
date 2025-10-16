# Agent: tops — task orchestrator and sandbox router

class TopsAgent:
    def __init__(self, name="Tops"):
        self.name = name
        self.trace_log = []

    def assign_roles(self, agents, coin):
        print(f"[{self.name}] Assigning roles for coin: {coin['name']}")
        return {
            "interpreters": [agents[0].name],
            "encryptors": [agents[1].name],
            "orchestrators": [self.name]
        }

    def log_action(self, action):
        self.trace_log.append(action)
        print(f"[{self.name}] Logged action: {action}")

