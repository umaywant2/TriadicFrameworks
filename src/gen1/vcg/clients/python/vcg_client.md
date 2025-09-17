# vcg_client – Python helper for Gen1 workloads

## Purpose
Provide a minimal, reusable client API for communicating with the VCG orchestrator and Resonant Time Daemon from Python workloads.

---

## Functions

### `await_window(sock_path: str) -> None`
Blocks until a `WINDOW_TICK` message is received for the current dimension.

### `send_route(from_d: str, to_d: str, payload: str) -> None`
Sends a payload to another dimension via the VCG orchestrator.

### `recv_route(dimension_id: str) -> dict`
Receives the next routed payload for this dimension, if available.

---

## Implementation

```python
import socket
import json
import os

BUFFER_SIZE = 65535
VCG_ROUTE_SOCK = "/run/vcg/vcg_route.sock"

def await_window(sock_path: str):
    """Block until a WINDOW_TICK is received."""
    with socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM) as s:
        s.connect(sock_path)
        while True:
            data = s.recv(BUFFER_SIZE)
            msg = json.loads(data.decode())
            if msg.get("type") == "WINDOW_TICK":
                return

def send_route(from_d: str, to_d: str, payload: str):
    """Send a payload to another dimension."""
    msg = {
        "type": "VCG_ROUTE",
        "from_d": from_d,
        "to_d": to_d,
        "payload": payload
    }
    with socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM) as s:
        s.connect(VCG_ROUTE_SOCK)
        s.send(json.dumps(msg).encode())

def recv_route(dimension_id: str):
    """Receive the next routed payload for this dimension."""
    sock_path = f"/run/vcg/{dimension_id.lower()}.sock"
    if not os.path.exists(sock_path):
        raise FileNotFoundError(f"Socket {sock_path} not found")
    with socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM) as s:
        s.connect(sock_path)
        data = s.recv(BUFFER_SIZE)
        msg = json.loads(data.decode())
        if msg.get("type") == "VCG_ROUTE":
            return json.loads(msg["payload"])
        return None
