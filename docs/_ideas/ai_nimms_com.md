## 🧠 Updated Setup Guide for `ai.nimms.com`

### ✅ GPU Compatibility Notes
- **GPU**: RTX 3050
- **Driver**: `nvidia-driver-550`
- **CUDA Toolkit**: `cuda-toolkit-12-4` (confirmed compatible)
- **PyTorch CUDA version**: `cu124` (for CUDA 12.4)

---

### 🛠️ `setup_ai_nimms.sh` — Full Script

```bash
#!/bin/bash
# Setup script for ai.nimms.com — RTX 3050, MX Linux

set -e  # Exit on error

echo "🔧 Updating system..."
sudo apt update

echo "📦 Installing base packages..."
sudo apt install -y python3 python3-pip python3-venv build-essential git

echo "🐍 Creating virtual environment..."
python3 -m venv myenv
source myenv/bin/activate

echo "🎮 Installing NVIDIA driver and CUDA toolkit..."
sudo apt install -y nvidia-driver-550
sudo apt install -y nvidia-cuda-toolkit

echo "🧪 Verifying GPU..."
nvidia-smi

echo "🧠 Installing AI frameworks..."
pip install --upgrade pip
pip install tensorflow
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu124

echo "📁 Cloning your repo..."
git clone https://github.com/umaywant2/TriadicFrameworks.git
cd TriadicFrameworks/docs/_ideas

echo "📚 Installing additional libraries..."
pip install pandas numpy matplotlib

echo "✅ Setup complete. Ready to train your model."
```

---

### 🧩 Notes for First-Time Success

- This script assumes MX Linux has access to `nvidia-driver-550` and `cuda-toolkit-12-4`. If not, you can manually install from [NVIDIA’s official driver page](https://www.nvidia.com/en-us/drivers/).
- PyTorch command uses `cu124` to match CUDA 12.4.
- You can add symbolic stubs or validator glyphs to this script for lineage clarity.
