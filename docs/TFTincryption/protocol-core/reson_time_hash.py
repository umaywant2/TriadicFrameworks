import hashlib
import time

# Configuration
MODULATION_BASES = [3, 6, 9]  # Tesla triadic pattern

def get_timestamp_ms():
    return int(time.time() * 1000)

def triadic_modulation(timestamp):
    return [timestamp % base for base in MODULATION_BASES]

def generate_resonant_hash(timestamp=None):
    if timestamp is None:
        timestamp = get_timestamp_ms()
    modulation = triadic_modulation(timestamp)
    hash_input = f"{timestamp}-{'-'.join(map(str, modulation))}"
    resonant_hash = hashlib.sha256(hash_input.encode()).hexdigest()
    return resonant_hash, hash_input

if __name__ == "__main__":
    hash_val, input_str = generate_resonant_hash()
    print("⏳ Timestamp Input:", input_str)
    print("🧬 Resonant-Time Hash:", hash_val)
