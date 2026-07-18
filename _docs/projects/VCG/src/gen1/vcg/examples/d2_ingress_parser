# D2 – Ingress Parser Example Workload

## Purpose
Dimension 2 handles incoming data streams, parses them into structured messages, and hands them off to downstream dimensions (e.g., D4 retriever).

---

## Flow
1. **Wait for token** from VCG orchestrator via `/run/vcg/d2.sock`.
2. **Read input** from a simulated source (e.g., TCP socket, file tail, or generated test data).
3. **Parse** into JSON or protobuf messages.
4. **Route** to D4 via `VCG_ROUTE` call.

---

## Example Implementation (Python)

```python
import socket
import json
from vcg_client import await_window, send_route

DIM_ID = "D2"
SOCK_PATH = f"/run/vcg/{DIM_ID.lower()}.sock"

def main():
    while True:
        await_window(SOCK_PATH)
        raw_data = "sensor_id=42,temp=21.5,hum=40"
        msg = {"sensor_id": 42, "temp": 21.5, "hum": 40}
        send_route(from_d=DIM_ID, to_d="D4", payload=json.dumps(msg))

if __name__ == "__main__":
    main()
