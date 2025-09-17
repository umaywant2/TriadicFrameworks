
---

## `/src/gen1/vcg/examples/d5_model_service.md`

```markdown
# D5 – Model Service Example Workload

## Purpose
Dimension 5 runs an AI model (e.g., LLaMA via llama.cpp) to process requests with context from D4.

---

## Flow
1. **Wait for token** from VCG orchestrator via `/run/vcg/d5.sock`.
2. **Receive context** from D4.
3. **Run inference** using local CPU/GPU.
4. **Send output** to D8 (aggregator) via VCG routing.

---

## Example Implementation (Python)

```python
import json
from vcg_client import await_window, recv_route, send_route
from llama_cpp import Llama

DIM_ID = "D5"
SOCK_PATH = f"/run/vcg/{DIM_ID.lower()}.sock"

llm = Llama(model_path="/models/llama-7b.gguf", n_ctx=512)

def main():
    while True:
        await_window(SOCK_PATH)
        context = recv_route(DIM_ID)
        prompt = f"Given context: {context}, summarize key points."
        output = llm(prompt, max_tokens=128)
        send_route(from_d=DIM_ID, to_d="D8", payload=json.dumps(output))

if __name__ == "__main__":
    main()
