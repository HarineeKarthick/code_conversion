#!/usr/bin/env bash
# Idempotent repository setup for the code_conversion Tkinter GUI app.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# 1. System packages: Tk runtime for the GUI, a headless X server plus tooling
#    to run/verify it without a monitor, and build headers required by Pillow.
if command -v apt-get >/dev/null 2>&1; then
  sudo apt-get update -qq
  sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -qq \
    python3-tk python3-venv python3-dev \
    xvfb x11-utils scrot xdotool \
    libjpeg-dev zlib1g-dev
fi

# 2. Python virtualenv with pinned dependencies (idempotent).
if [ ! -d .venv ]; then
  python3 -m venv .venv
fi
# shellcheck disable=SC1091
. .venv/bin/activate
python -m pip install --quiet --upgrade pip
python -m pip install --quiet -r requirements.txt

# 3. code_conversion.py loads its background image from a hard-coded absolute
#    path. Materialize that path from the in-repo asset so the GUI runs
#    unmodified on any machine.
LOGO_DEST="/home/harinee/Desktop/logo.jpg"
if [ ! -f "$LOGO_DEST" ]; then
  sudo mkdir -p "$(dirname "$LOGO_DEST")"
  sudo cp "$REPO_ROOT/logo.jpg" "$LOGO_DEST"
  sudo chmod -R a+rX /home/harinee
fi

echo "install.sh complete"
