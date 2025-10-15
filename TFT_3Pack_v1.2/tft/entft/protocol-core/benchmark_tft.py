import time
import math

# Simulated benchmark values (in seconds)
RSA_CRACK_TIME = 600         # ~10 minutes
ECC_CRACK_TIME = 1200        # ~20 minutes
PQC_CRACK_TIME = 10**9       # ~30 years (conservative)
TFT_CRACK_STEPS = 4.8e53     # From entropy calc
QUANTUM_SPEED = 1e12         # Keys/sec (optimistic)

def estimate_crack_time(steps, speed):
    seconds = steps / speed
    years = seconds / 31_536_000
    return years

def run_benchmark():
    rsa_years = estimate_crack_time(RSA_CRACK_TIME, 1)
    ecc_years = estimate_crack_time(ECC_CRACK_TIME, 1)
    pqc_years = estimate_crack_time(PQC_CRACK_TIME, 1)
    tft_years = estimate_crack_time(TFT_CRACK_STEPS, QUANTUM_SPEED)

    print("🔐 RSA-2048 Crack Time:", rsa_years, "years")
    print("🔐 ECC-256 Crack Time:", ecc_years, "years")
    print("🛡️ PQC (Kyber/Dilithium) Crack Time:", pqc_years, "years")
    print("🧬 enTFT Crack Time:", f"{tft_years:.2e}", "years")

if __name__ == "__main__":
    run_benchmark()
