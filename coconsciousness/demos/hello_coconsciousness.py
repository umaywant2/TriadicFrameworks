import time
import threading
from coconsciousness.tft_utils import tau_from_tft

SYNC_THRESHOLD = 0.5

def loop(name, phase_offset=0.0):
    while True:
        t = time.time()
        tau_val = tau_from_tft(t, phase_offset)  # now powered by TFT
        in_sync = abs(tau_val) < SYNC_THRESHOLD
        print(f"[{name}] τ={tau_val:.2f} {'🟢' if in_sync else '🔴'}")
        time.sleep(0.5)

if __name__ == "__main__":
    threading.Thread(target=loop, args=("Looker", 0)).start()
    threading.Thread(target=loop, args=("Planner", 1)).start()
