Gen1 testing harness
Purpose
Let you run the D2 → D4 → D5 → D8 pipeline before the full orchestrator exists:

Fakes minimal “orchestrator” behavior: receives VCG_ROUTE and forwards to target dimension socket.

Works with RTD in standalone mode (or without RTD by sending synthetic WINDOW_TICKs).

Option A: Python mini‑orchestrator
```python
# tests/mini_orchestrator.py
import os, socket, json, selectors

RUN = "/run/vcg"
ROUTE_SOCK = f"{RUN}/vcg_route.sock"

def ensure_sock(path):
    try: os.unlink(path)
    except FileNotFoundError: pass
    s = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    s.bind(path)
    return s

def main():
    os.makedirs(RUN, exist_ok=True)
    sel = selectors.DefaultSelector()
    route = ensure_sock(ROUTE_SOCK)
    sel.register(route, selectors.EVENT_READ, data="route")

    print("[mini-orch] ready on", ROUTE_SOCK)
    while True:
        for key, _ in sel.select(timeout=1.0):
            if key.data == "route":
                data, _ = route.recvfrom(65535)
                msg = json.loads(data.decode())
                if msg.get("type") == "VCG_ROUTE":
                    to_d = msg["to_d"].lower()
                    dst = f"{RUN}/{to_d}.sock"
                    s = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
                    try:
                        s.connect(dst)
                        s.send(data)
                    except Exception as e:
                        print("[mini-orch] drop (no dst?):", dst, e)
                    finally:
                        s.close()

if __name__ == "__main__":
    main()
```
- Run: sudo python3 tests/mini_orchestrator.py

## Option B: Synthetic tick generator (if RTD not running)
```python
# tests/synthetic_ticks.py
import os, socket, json, time

RUN = "/run/vcg"
DIMENSIONS = [f"d{i}" for i in range(1,10)]
HZ = 10.0

def main():
    os.makedirs(RUN, exist_ok=True)
    period = 1.0 / HZ
    seq = 0
    while True:
        t_start_ns = time.time_ns()
        for d in DIMENSIONS:
            msg = {
                "type": "WINDOW_TICK",
                "dimension_id": d.upper(),
                "seq": seq,
                "t_start_ns": t_start_ns,
                "t_end_ns": t_start_ns + int(period * 1e9),
                "phase_deg": 0.0,
                "cadence_hz": HZ
            }
            path = f"{RUN}/{d}.sock"
            s = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
            try:
                s.connect(path)
                s.send(json.dumps(msg).encode())
            except Exception:
                pass
            finally:
                s.close()
        seq += 1
        time.sleep(period)

if __name__ == "__main__":
    main()
```
- Run: sudo python3 tests/synthetic_ticks.py

---

## Directory and run checklist
- **Sockets:** Ensure these exist or are connectable:
  - /run/vcg/d2.sock, /run/vcg/d4.sock, /run/vcg/d5.sock, /run/vcg/d8.sock
  - /run/vcg/vcg_route.sock
- **Order:**
  - Start mini orchestrator.
  - Start RTD (or synthetic tick generator).
  - Start example workloads D2, D4, D5, D8.
- **Expected:** D2 parses and routes to D4; D4 retrieves and routes to D5; D5 infers and routes to D8; D8 prints aggregated output.

---

## Notes and next steps
- This harness is intentionally minimal. The real orchestrator will add token minting, QoS amplitude, and barriers.
- When you wire in the orchestrator, keep mini_orchestrator.py around as a dev tool for quick repros.
- We can add a small Makefile target to spin all this up with one command; say the word and I’ll scaffold it.
