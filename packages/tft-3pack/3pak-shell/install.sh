#!/usr/bin/env bash
#
# 3PAK Shell — Installer
# TriadicFrameworks — tft‑3pack

set -e

echo ""
echo "📦 Installing 3PAK Shell..."
echo "-----------------------------------------"

THREEPAK_HOME="${THREEPAK_HOME:-$HOME/.3pak}"
mkdir -p "$THREEPAK_HOME"

touch "$THREEPAK_HOME/state"
touch "$THREEPAK_HOME/3pak.log"

echo "✨ 3PAK environment initialized at: $THREEPAK_HOME"
echo "-----------------------------------------"
echo ""
