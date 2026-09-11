#!/usr/bin/env python3
"""Forward to the self-contained skill script (this demo repo only)."""
from pathlib import Path
import runpy

TARGET = Path(__file__).resolve().parents[1] / ".github" / "skills" / "ragless-kb" / "scripts" / "fetch_eval_docs.py"
runpy.run_path(str(TARGET), run_name="__main__")
