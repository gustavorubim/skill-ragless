#!/usr/bin/env bash
set -euo pipefail
if ! command -v uv >/dev/null 2>&1; then
  echo "uv is required. Install it from https://docs.astral.sh/uv/getting-started/installation/" >&2
  exit 1
fi
if [ ! -d .venv ]; then uv venv; fi
uv pip install -r .github/skills/ragless-kb/requirements.txt
uv pip install -r requirements.txt
echo "Ready. Drop files in input/, select Docs Builder to preprocess, then Docs Chat to ask questions."
