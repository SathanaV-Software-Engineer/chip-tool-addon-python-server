#!/bin/bash

echo "[INIT] Starting CHIP Tool Server..."
# export CHIP_TOOL_PATH=/usr/bin/chip-tool  # or actual path to chip-tool
# export CHIPTOOL_PORT=6000
python3 /app/chip_tool_server.py
