#!/bin/bash
# Reset script for ai.nimms.com — removes all setup artifacts

echo "⚠️ Starting teardown of ai.nimms.com environment..."

# 🧼 Deactivate and remove virtual environment
if [ -d "myenv" ]; then
    echo "🔻 Removing Python virtual environment..."
    deactivate || true
    rm -rf myenv
fi

# 🧹 Remove cloned repo
if [ -d "TriadicFrameworks" ]; then
    echo "🗑️ Removing cloned TriadicFrameworks repo..."
    rm -rf TriadicFrameworks
fi

# 🧨 Uninstall Python packages (inside system Python)
echo "📦 Uninstalling Python packages..."
pip uninstall -y tensorflow torch torchvision torchaudio pandas numpy matplotlib || true

# 🧯 Remove NVIDIA driver and CUDA toolkit
echo "🧹 Removing NVIDIA driver and CUDA toolkit..."
sudo apt purge -y nvidia-driver-550 nvidia-cuda-toolkit
sudo apt autoremove -y
sudo apt clean

# 🧾 Optional: Remove logs and model output
rm -rf model_output logs

echo "✅ Teardown complete. System is clean and ready for fresh setup."
