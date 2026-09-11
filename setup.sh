#!/usr/bin/env bash
set -euo pipefail
if [ ! -d .venv ]; then python3 -m venv .venv; fi
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r .github/skills/ragless-kb/requirements.txt
.venv/bin/python -m pip install -r requirements.txt
echo "Ready. Drop files in input/, select Docs Builder to preprocess, then Docs Chat to ask questions."
