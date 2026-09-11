$ErrorActionPreference = "Stop"
if (-not (Test-Path .venv)) { python -m venv .venv }
& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -r .github\skills\ragless-kb\requirements.txt
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
Write-Host "Ready. Drop files in input\, then select Docs Builder and say preprocess (or /ragless-kb preprocess). Cookbook: .github/skills/ragless-kb/cookbook.md"
