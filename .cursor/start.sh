#!/usr/bin/env bash
# Per-boot startup: provide a headless X display so the Tkinter GUI can run
# without a physical monitor. Idempotent and returns once the display is ready.
set -euo pipefail

DISPLAY_NUM=":99"

if ! xdpyinfo -display "$DISPLAY_NUM" >/dev/null 2>&1; then
  rm -f "/tmp/.X${DISPLAY_NUM#:}-lock"
  Xvfb "$DISPLAY_NUM" -screen 0 1024x768x24 >/tmp/xvfb-99.log 2>&1 &
  for _ in $(seq 1 30); do
    if xdpyinfo -display "$DISPLAY_NUM" >/dev/null 2>&1; then
      break
    fi
    sleep 0.5
  done
fi

if xdpyinfo -display "$DISPLAY_NUM" >/dev/null 2>&1; then
  echo "Xvfb ready on ${DISPLAY_NUM}. Run the app with: DISPLAY=${DISPLAY_NUM} .venv/bin/python code_conversion.py"
else
  echo "Xvfb failed to start on ${DISPLAY_NUM}" >&2
  exit 1
fi
