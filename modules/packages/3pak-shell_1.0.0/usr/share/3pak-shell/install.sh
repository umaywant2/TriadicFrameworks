#!/usr/bin/env bash
# install.sh — Installer for 3pak-shell
# Safe, minimal, and distro-friendly.

set -e

PREFIX="/usr/local"
TARGET_DIR="$PREFIX/share/3pak-shell"
PROFILE_DIR="/etc/profile.d"
SCRIPT_NAME="wrsadc_shell.sh"

echo "[3pak-shell] Installing to $TARGET_DIR..."

# Create target directory
sudo mkdir -p "$TARGET_DIR"

# Copy core script
sudo cp "$SCRIPT_NAME" "$TARGET_DIR/$SCRIPT_NAME"
sudo chmod 755 "$TARGET_DIR/$SCRIPT_NAME"

echo "[3pak-shell] Core installed."

# Optional profile hook
HOOK_FILE="$PROFILE_DIR/3pak-shell.sh"

if [ ! -f "$HOOK_FILE" ]; then
    echo "[3pak-shell] Adding profile hook at $HOOK_FILE..."
    sudo bash -c "cat > $HOOK_FILE" <<EOF
# 3pak-shell auto-loader
if [ -f "$TARGET_DIR/$SCRIPT_NAME" ]; then
    source "$TARGET_DIR/$SCRIPT_NAME"
    wrsadc_init "3pak-shell"
fi
EOF
    sudo chmod 644 "$HOOK_FILE"
else
    echo "[3pak-shell] Profile hook already exists. Skipping."
fi

echo "[3pak-shell] Installation complete."
echo "Open a new shell to activate 3pak-shell."
