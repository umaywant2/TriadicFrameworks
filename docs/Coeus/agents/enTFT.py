# enTFT — Encryption sleeve logic for coin validation and trace integrity

class enTFT:
    def __init__(self):
        self.sleeves = {}

    def wrap(self, coin_id, metadata):
        sleeve = f"enTFT::{coin_id}::{hash(str(metadata))}"
        self.sleeves[coin_id] = sleeve
        print(f"[enTFT] Wrapped {coin_id} → {sleeve}")
        return sleeve

    def validate(self, coin_id, sleeve):
        expected = self.sleeves.get(coin_id)
        result = sleeve == expected
        print(f"[enTFT] Validation for {coin_id}: {result}")
        return result
