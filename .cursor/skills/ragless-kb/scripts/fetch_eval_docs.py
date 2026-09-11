#!/usr/bin/env python3
"""Download public-domain eval PDFs into the workspace input/ folder."""
from __future__ import annotations

import ssl
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kb import get_root

ROOT = get_root()
INPUT = ROOT / "input"

# US government works (NIST). Suitable for local eval and redistribution.
DOCUMENTS = [
    {
        "filename": "NIST.AI.100-1.pdf",
        "url": "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf",
        "title": "NIST AI Risk Management Framework 1.0",
    },
    {
        "filename": "NIST.AI.600-1.pdf",
        "url": "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf",
        "title": "NIST Generative AI Profile",
    },
    {
        "filename": "NIST.SP.1270.pdf",
        "url": "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf",
        "title": "NIST SP 1270 Towards Identifying and Managing Bias in AI",
    },
]


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 10_000:
        print(f"SKIP {dest.name} (already present, {dest.stat().st_size} bytes)")
        return
    print(f"GET {url}")
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "skill-ragless-eval/1.0"})
    with urllib.request.urlopen(req, context=ctx, timeout=120) as response:
        data = response.read()
    if len(data) < 1000 or not data.startswith(b"%PDF"):
        raise RuntimeError(f"Download did not look like a PDF: {url} ({len(data)} bytes)")
    dest.write_bytes(data)
    print(f"OK {dest.name} ({len(data)} bytes)")


def main() -> int:
    INPUT.mkdir(parents=True, exist_ok=True)
    failed = 0
    for item in DOCUMENTS:
        dest = INPUT / item["filename"]
        try:
            download(item["url"], dest)
        except Exception as exc:
            failed += 1
            print(f"FAILED {item['filename']}: {exc}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
