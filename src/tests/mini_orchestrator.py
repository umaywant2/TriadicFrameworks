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
