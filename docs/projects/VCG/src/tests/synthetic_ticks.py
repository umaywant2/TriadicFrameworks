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
