
---

## `/src/gen1/vcg/examples/d8_aggregator.md`

```markdown
# D8 – Aggregator Example Workload

## Purpose
Dimension 8 aggregates outputs from multiple upstream dimensions (e.g., D5 model service, D7 analytics) and prepares final results.

---

## Flow
1. **Wait for token** from VCG orchestrator via `/run/vcg/d8.sock`.
2. **Receive outputs** from upstream dimensions.
3. **Merge** into a single response object.
4. **Write** to output sink (e.g., stdout, file, or network).

---

## Example Implementation (Python)

```python
import json
from vcg_client import await_window, recv_route

DIM_ID = "D8"
SOCK_PATH = f"/run/vcg/{DIM_ID.lower()}.sock"

def main():
    while True:
        await_window(SOCK_PATH)
        outputs = []
        while True:
            msg = recv_route(DIM_ID)
            if not msg:
                break
            outputs.append(msg)
        final = {"aggregated": outputs}
        print(json.dumps(final))

if __name__ == "__main__":
    main()
