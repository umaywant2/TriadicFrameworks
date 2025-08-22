import time, math

def loop(name, phase_offset=0):
    while True:
        t = time.time()
        tau = math.sin(t + phase_offset)  # stand-in for TFT transform
        in_sync = abs(tau) < 0.5
        print(f"[{name}] τ={tau:.2f} {'🟢' if in_sync else '🔴'}")
        time.sleep(0.5)

# Simulate two loops in separate rhythms
if __name__ == "__main__":
    import threading
    threading.Thread(target=loop, args=("Looker", 0)).start()
    threading.Thread(target=loop, args=("Planner", 1)).start()
