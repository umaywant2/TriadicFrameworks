import hashlib

# Sample encrypted payload (for simulation)
ENCRYPTED_PAYLOAD = "EncryptedData123"

def validate_block_map(obfuscated_key, valid_map):
    reconstructed_key = []
    for block, is_valid in zip(obfuscated_key, valid_map):
        if is_valid:
            reconstructed_key.append(block)
    return reconstructed_key

def validate_resonant_hash(timestamp, expected_hash):
    triadic_mod = [timestamp % 3, timestamp % 6, timestamp % 9]
    hash_input = f"{timestamp}-{triadic_mod[0]}-{triadic_mod[1]}-{triadic_mod[2]}"
    computed_hash = hashlib.sha256(hash_input.encode()).hexdigest()
    return computed_hash == expected_hash

def decrypt_payload(reconstructed_key, resonant_hash_valid):
    if not resonant_hash_valid:
        return "❌ Invalid Resonant-Time hash. Decryption failed."
    # Simulated decryption logic
    return f"✅ Decrypted with key: {reconstructed_key[:5]}... (truncated)"

if __name__ == "__main__":
    # Simulated input from keygen_tft.py
    from keygen_tft import scaffold_key
    key_data = scaffold_key()

    obfuscated_key = key_data["obfuscated_key"]
    valid_map = key_data["valid_map"]
    expected_hash = key_data["resonant_hash"]
    hash_input = key_data["hash_input"]
    timestamp = int(hash_input.split("-")[0])

    reconstructed_key = validate_block_map(obfuscated_key, valid_map)
    hash_valid = validate_resonant_hash(timestamp, expected_hash)
    result = decrypt_payload(reconstructed_key, hash_valid)

    print(result)
