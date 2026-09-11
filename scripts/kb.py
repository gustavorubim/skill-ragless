#!/usr/bin/env python3
"""Forward to the self-contained skill CLI (this demo repo only)."""
from pathlib import Path
import runpy

TARGET = Path(__file__).resolve().parents[1] / ".github" / "skills" / "ragless-kb" / "scripts" / "kb.py"
runpy.run_path(str(TARGET), run_name="__main__")
