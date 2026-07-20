#!/usr/bin/env bash
#
# WRSADC Shell — Install Script
# TriadicFrameworks — Resonance‑Time Theory Canon
#
# This script sets up a lightweight local environment for the WRSADC Shell.
# It does not install system‑wide dependencies. It simply prepares a clean
# workspace so developers can wrap modules with RTT‑Inside alignment.

set -e

echo ""
echo "🔧 WRSADC Shell — Installer"
echo "-----------------------------------------"
echo "Preparing local environment…"
echo ""

# Create local environment directory
SHELL_DIR="./.wrsadc"
if [ ! -d "$SHELL_DIR" ]; then
  mkdir -p "$SHELL_DIR"
  echo "📁 Created local shell directory: $SHELL_DIR"
else
  echo "📁 Local shell directory already exists: $SHELL_DIR"
fi

# Create placeholder runtime files
touch "$SHELL_DIR/runtime.log"
touch "$SHELL_DIR/context.state"
touch "$SHELL_DIR/observer.map"

echo "📝 Initialized runtime artifacts:"
echo "   - runtime.log"
echo "   - context.state"
echo "   - observer.map"
echo ""

# Add a simple environment marker
echo "WRSADC_SHELL_ACTIVE=1" > "$SHELL_DIR/env"
echo "🌱 Environment marker created."

echo ""
echo "✨ WRSADC Shell is now initialized."
echo "You can wrap modules or processes using this shell boundary."
echo "-----------------------------------------"
echo "Done."
echo ""
