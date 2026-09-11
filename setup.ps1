$ErrorActionPreference = "Stop"
if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Error "uv is required. Install it from https://docs.astral.sh/uv/getting-started/installation/ (irm https://astral.sh/uv/install.ps1 | iex)"
}
if (-not (Test-Path .venv)) { uv venv }
uv pip install -r .github/skills/ragless-kb/requirements.txt
uv pip install -r requirements.txt
Write-Host "Ready. Drop files in input\, select Docs Builder to preprocess, then Docs Chat to ask questions."
