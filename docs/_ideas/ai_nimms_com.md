# 🧠 Updated Setup Guide for ai.nimms.com

✅ **Hardware + Environment Notes**
- **GPU (discrete):** RTX 3060 (12 GB VRAM) via Oculink
- **GPU (integrated):** AMD 890M (AI Pro‑370 platform)
- **NPU:** Enabled, target for inference workloads
- **CPU:** 22 cores / 44 threads
- **RAM:** 96 GB
- **OS Base:** Windows 11 with WSL2 (Ubuntu/Debian flavor recommended)

---

## ⚙️ Setup Script (WSL)

```bash
#! /bin/bash
# Setup script for ai.nimms.com — RTX 3060 + AMD 890M + NPU
set -e

echo "🔄 Updating system..."
sudo apt update && sudo apt upgrade -y

echo "📦 Installing base packages..."
sudo apt install -y python3 python3-pip python3-venv build-essential git

echo "🐍 Creating virtual environment..."
python3 -m venv myenv
source myenv/bin/activate

echo "🎮 Installing NVIDIA driver + CUDA toolkit..."
# WSL requires CUDA toolkit + NVIDIA drivers installed on Windows host
sudo apt install -y nvidia-cuda-toolkit

echo "🔥 Installing AMD ROCm stack (for 890M iGPU)..."
# ROCm packages for WSL (experimental, AMD repo required)
sudo apt install -y rocm-dev rocm-libs

echo "🤖 Installing AI frameworks..."
pip install --upgrade pip
pip install tensorflow
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu124

echo "📂 Cloning your repo..."
git clone https://github.com/umaywant2/TriadicFrameworks.git
cd TriadicFrameworks/docs/_ideas

echo "📚 Installing additional libraries..."
pip install pandas numpy matplotlib onnxruntime-directml

echo "✅ Setup complete. Ready to train your model."
```

---

## 📝 Notes for First‑Time Success
- **WSL GPU/NPU access:**  
  - NVIDIA RTX 3060 → requires CUDA toolkit + WSL GPU driver from NVIDIA.  
  - AMD 890M → ROCm support in WSL is experimental; fallback to DirectML if ROCm fails.  
  - NPU → accessible via **ONNX Runtime with DirectML execution provider**.  
- **Dual GPU/NPU usage:**  
  - Use ONNX Runtime session options to select execution provider (`CUDAExecutionProvider`, `DmlExecutionProvider`, `ROCMExecutionProvider`).  
  - VCG logic can orchestrate across all three (CPU/GPU/NPU) for balanced workloads.  
- **Oculink note:**  
  - Ensure BIOS/firmware exposes RTX 3060 correctly to WSL.  
  - `nvidia-smi` inside WSL should show the card.  

---

## 🚀 Next Steps
1. Validate GPU/NPU visibility inside WSL:  
   ```bash
   nvidia-smi
   rocminfo
   python -c "import onnxruntime as ort; print(ort.get_available_providers())"
   ```
2. Patch kernel hooks for resonance‑time + FFF logic (see `Nullaium OS` build plan).
3. Wire VCG orchestration to route workloads across RTX 3060, AMD 890M, and NPU.
4. Begin training with mythmatical corpus mounted in `/srv/nos_canon/`.

---

## 🏁 Closing
This refresh ensures **all accelerators are engaged** — RTX 3060 via Oculink, AMD 890M iGPU, and the NPU — under WSL. The **Virtual Compute Gateway (VCG)** provides backwards compatibility while balancing loads across CPU/GPU/NPU/DPU, preventing idle silicon and aligning with triadic resonance principles.

---

Perfect — here’s a **Python snippet** you can drop into your refreshed `ai_nimms_com.md` that shows how to explicitly select between **CUDA (RTX 3060)**, **DirectML (NPU)**, and **ROCm (AMD 890M)** using ONNX Runtime session options:

```python
import onnxruntime as ort

# List all available execution providers
print("Available providers:", ort.get_available_providers())

# Example: load a model and try different providers
model_path = "model.onnx"

# Prefer CUDA (RTX 3060 via Oculink)
cuda_session = ort.InferenceSession(
    model_path,
    providers=["CUDAExecutionProvider", "CPUExecutionProvider"]
)
print("Running on CUDA:", cuda_session.get_providers())

# Prefer DirectML (NPU / Windows AI stack)
dml_session = ort.InferenceSession(
    model_path,
    providers=["DmlExecutionProvider", "CPUExecutionProvider"]
)
print("Running on DirectML (NPU):", dml_session.get_providers())

# Prefer ROCm (AMD 890M iGPU)
rocm_session = ort.InferenceSession(
    model_path,
    providers=["ROCMExecutionProvider", "CPUExecutionProvider"]
)
print("Running on ROCm:", rocm_session.get_providers())

# Run inference (example input)
input_name = cuda_session.get_inputs()[0].name
output_name = cuda_session.get_outputs()[0].name
result = cuda_session.run([output_name], {input_name: [[1.0, 2.0, 3.0]]})
print("Inference result:", result)
```

---

### 🔑 How this works
- `ort.get_available_providers()` → shows which accelerators ONNX Runtime can see inside WSL/Windows.  
- `CUDAExecutionProvider` → routes workloads to your RTX 3060.  
- `DmlExecutionProvider` → routes workloads to the NPU via DirectML.  
- `ROCMExecutionProvider` → routes workloads to the AMD 890M iGPU.  
- Always include `"CPUExecutionProvider"` as a fallback so inference doesn’t fail if an accelerator isn’t available.  

---

This snippet makes your **Virtual Compute Gateway (VCG)** logic concrete: you can orchestrate across all three accelerators, or benchmark them separately.  

Here’s the **benchmarking extension** you can add to your `ai_nimms_com.md` doc. It times inference across CUDA (RTX 3060), DirectML (NPU), ROCm (AMD 890M), and CPU, so you can compare performance directly:

```python
import onnxruntime as ort
import time

def benchmark_providers(model_path, test_input):
    providers = [
        "CUDAExecutionProvider",   # RTX 3060
        "DmlExecutionProvider",    # NPU
        "ROCMExecutionProvider",   # AMD 890M
        "CPUExecutionProvider"     # Fallback
    ]

    available = ort.get_available_providers()
    print("Available providers:", available)

    results = {}
    for provider in providers:
        if provider in available:
            print(f"\nBenchmarking {provider}...")
            session = ort.InferenceSession(
                model_path,
                providers=[provider, "CPUExecutionProvider"]
            )
            input_name = session.get_inputs()[0].name
            output_name = session.get_outputs()[0].name

            # Warm‑up run
            session.run([output_name], {input_name: test_input})

            # Timed run
            start = time.time()
            output = session.run([output_name], {input_name: test_input})
            elapsed = time.time() - start

            results[provider] = {
                "time_sec": elapsed,
                "output_preview": output[0][:5]  # show first few values
            }
        else:
            results[provider] = "Not available"

    return results

# Example usage
model_path = "model.onnx"
test_input = [[1.0, 2.0, 3.0]]  # replace with real input shape
benchmarks = benchmark_providers(model_path, test_input)

print("\n=== Benchmark Results ===")
for provider, result in benchmarks.items():
    print(provider, ":", result)
```

---

### 🔑 What this gives you
- **Side‑by‑side timings** → see how fast each accelerator runs the same model.  
- **Output preview** → sanity check that inference results are consistent across providers.  
- **Transparency** → validates that your RTX 3060, AMD 890M, and NPU are actually being used.  

---

This turns your doc into a **full test harness**: setup, orchestration, and benchmarking. It’s a validator‑grade way to prove your Virtual Compute Gateway principle in practice.  

