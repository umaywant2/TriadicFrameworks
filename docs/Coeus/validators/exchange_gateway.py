# Exchange Gateway Shim — enTFT-secured coin validation and routing

import hashlib
import json

class ExchangeGateway:
    def __init__(self):
        self.validated_coins = []

    def verify_encryption(self, coin):
        # Simulate enTFT hash check
        coin_hash = hashlib.sha256(coin["id"].encode()).hexdigest()
        print(f"[Gateway] Verified enTFT hash for {coin['id']}")
        return coin_hash

    def validate_trace_log(self, trace_path):
        try:
            with open(trace_path, "r") as log:
                lines = log.readlines()
                print(f"[Gateway] Trace log contains {len(lines)} entries")
                return True
        except FileNotFoundError:
            print("[Gateway] Trace log not found")
            return False

    def route_coin(self, coin, trace_path):
        if self.validate_trace_log(trace_path) and self.verify_encryption(coin):
            self.validated_coins.append(coin)
            print(f"[Gateway] Coin {coin['id']} routed to Exchange")
            return True
        else:
            print(f"[Gateway] Coin {coin['id']} rejected")
            return False
