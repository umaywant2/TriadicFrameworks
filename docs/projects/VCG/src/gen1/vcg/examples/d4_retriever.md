
---

## `/src/gen1/vcg/examples/d4_retriever.md`

```markdown
# D4 – Retriever Example Workload

## Purpose
Dimension 4 retrieves relevant context or data for incoming requests, such as documents for RAG (retrieval‑augmented generation).

---

## Flow
1. **Wait for token** from VCG orchestrator via `/run/vcg/d4.sock`.
2. **Receive messages** from D2 via VCG routing.
3. **Query** a local or remote datastore.
4. **Send results** to D5 (model service) via VCG routing.

---

## Example Implementation (Python)

```python
import json
from vcg_client import await_window, recv_route, send_route

DIM_ID = "D4"
SOCK_PATH = f"/run/vcg/{DIM_ID.lower()}.sock"

def main():
    while True:
        await_window(SOCK_PATH)
        msg = recv_route(DIM_ID)
        query = f"SELECT * FROM docs WHERE sensor_id={msg['sensor_id']}"
        results = [{"doc": "Example context for sensor 42"}]
        send_route(from_d=DIM_ID, to_d="D5", payload=json.dumps(results))

if __name__ == "__main__":
    main()
