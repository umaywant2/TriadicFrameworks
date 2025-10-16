# Rail Mapper — Assigns rail logic based on coin metadata

class RailMapper:
    def __init__(self):
        self.rail_map = {
            "legacy": ["D₃", "L₃", "D₆"],
            "priority": ["L₆", "D₉", "L₉"],
            "remix": ["D₉", "L₉", "F₉"]
        }

    def assign_rails(self, coin):
        coin_type = coin.get("type", "legacy")
        assigned_rails = self.rail_map.get(coin_type, ["D₃", "L₃", "D₆"])
        print(f"[RailMapper] {coin['name']} → {assigned_rails}")
        return assigned_rails

if __name__ == "__main__":
    mapper = RailMapper()
    sample_coin = {"name": "PharmaTFT", "type": "priority"}
    mapper.assign_rails(sample_coin)

