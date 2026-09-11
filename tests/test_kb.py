import json
import os
import shutil
import sys
import tempfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
KB_PY = ROOT / ".github" / "skills" / "ragless-kb" / "scripts" / "kb.py"
TMP_ROOT = ROOT / "tests" / ".tmp"


def run_kb(kb_root: Path, *args, check=True):
    import subprocess

    env = os.environ.copy()
    env["KB_ROOT"] = str(kb_root)
    proc = subprocess.run(
        [sys.executable, str(KB_PY), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        env=env,
    )
    if check and proc.returncode != 0:
        raise AssertionError(f"kb.py {args} failed ({proc.returncode})\n{proc.stdout}\n{proc.stderr}")
    return proc


@pytest.fixture
def kb_root():
    TMP_ROOT.mkdir(parents=True, exist_ok=True)
    path = Path(tempfile.mkdtemp(prefix="kb-", dir=TMP_ROOT))
    try:
        yield path
    finally:
        shutil.rmtree(path, ignore_errors=True)


def init_kb(kb_root: Path) -> Path:
    inbox = kb_root / "input"
    inbox.mkdir(parents=True)
    (kb_root / "knowledge" / "docs").mkdir(parents=True)
    (kb_root / "knowledge" / "cards").mkdir()
    (kb_root / "knowledge" / "topics").mkdir()
    (kb_root / "AGENTS.md").write_text("# test\n", encoding="utf-8")
    (kb_root / "scripts").mkdir(exist_ok=True)
    return inbox


def write_source(inbox: Path, name: str, body: str) -> Path:
    path = inbox / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")
    return path


LONG_BODY = (
    "Model validation frequency is at least annually for each production model. "
    "Challenger models are reviewed on the same cadence unless an emergency exception is approved "
    "by the Model Risk Committee. Emergency exceptions expire after ninety days.\n"
)


def test_cli_help():
    import subprocess

    proc = subprocess.run([sys.executable, str(KB_PY), "--help"], cwd=ROOT, text=True, capture_output=True)
    assert proc.returncode == 0
    assert "knowledge base" in proc.stdout.lower()


def test_preprocess_alias_on_help(kb_root: Path):
    help_proc = run_kb(kb_root, "--help")
    assert "preprocess" in help_proc.stdout
    assert "ingest" in help_proc.stdout


def test_ingest_converts_txt_and_skips_unchanged(kb_root: Path):
    inbox = init_kb(kb_root)
    write_source(inbox, "validation-policy.txt", LONG_BODY)
    first = run_kb(kb_root, "ingest")
    assert "OK" in first.stdout
    stats = json.loads(first.stdout[first.stdout.rfind("{") :])
    assert stats["added"] == 1
    second = run_kb(kb_root, "ingest")
    stats = json.loads(second.stdout[second.stdout.rfind("{") :])
    assert stats["unchanged"] == 1
    assert stats["added"] == 0
    doc = kb_root / "knowledge" / "docs" / "validation-policy.md"
    assert doc.exists()
    text = doc.read_text(encoding="utf-8")
    assert "source_file" in text
    assert "annually" in text
    assert "input/validation-policy.txt" in text


def test_ingest_preserves_semantic_frontmatter(kb_root: Path):
    inbox = init_kb(kb_root)
    write_source(inbox, "policy.txt", LONG_BODY)
    run_kb(kb_root, "ingest")
    doc = kb_root / "knowledge" / "docs" / "policy.md"
    original = doc.read_text(encoding="utf-8")
    enriched = original.replace('summary: ""', 'summary: "Annual validation rule."')
    enriched = enriched.replace('authority: "unknown"', 'authority: "formal-primary"')
    enriched = enriched.replace("topics: []", 'topics: ["model-risk"]')
    enriched = enriched.replace('document_type: "txt"', 'document_type: "policy"')
    doc.write_text(enriched, encoding="utf-8")
    write_source(inbox, "policy.txt", LONG_BODY + "A second paragraph about challenger models.\n")
    run_kb(kb_root, "ingest")
    updated = doc.read_text(encoding="utf-8")
    assert "Annual validation rule." in updated
    assert "formal-primary" in updated
    assert "model-risk" in updated
    assert 'document_type: "policy"' in updated
    assert "challenger models" in updated


def test_ingest_skips_readme(kb_root: Path):
    inbox = init_kb(kb_root)
    write_source(inbox, "README.md", "# inbox notes\n" + LONG_BODY)
    write_source(inbox, "policy.txt", LONG_BODY)
    proc = run_kb(kb_root, "ingest")
    stats = json.loads(proc.stdout[proc.stdout.rfind("{") :])
    assert stats["added"] == 1
    assert (kb_root / "knowledge" / "docs" / "policy.md").exists()
    assert not (kb_root / "knowledge" / "docs" / "readme.md").exists()


def test_unsupported_extension_is_reported(kb_root: Path):
    inbox = init_kb(kb_root)
    write_source(inbox, "notes.bin", "not a supported document")
    proc = run_kb(kb_root, "ingest")
    stats = json.loads(proc.stdout[proc.stdout.rfind("{") :])
    assert stats["unsupported"] == 1
    assert "UNSUPPORTED" in proc.stdout


def test_search_tokenizes_natural_language(kb_root: Path):
    inbox = init_kb(kb_root)
    write_source(inbox, "validation-policy.txt", LONG_BODY)
    run_kb(kb_root, "ingest")
    run_kb(kb_root, "rebuild")
    proc = run_kb(kb_root, "search", "What is the validation frequency for challenger models?")
    assert "validation-policy" in proc.stdout
    assert "No matches." not in proc.stdout


def test_search_json_includes_original_path(kb_root: Path):
    inbox = init_kb(kb_root)
    write_source(inbox, "validation-policy.txt", LONG_BODY)
    run_kb(kb_root, "ingest")
    run_kb(kb_root, "rebuild")
    proc = run_kb(kb_root, "search", "challenger models", "--json")
    rows = json.loads(proc.stdout)
    assert rows
    assert rows[0]["source_file"].endswith("validation-policy.txt")
    assert rows[0]["path"].startswith("knowledge/docs/")


def test_validate_flags_missing_card_and_orphan(kb_root: Path):
    inbox = init_kb(kb_root)
    source = write_source(inbox, "policy.txt", LONG_BODY)
    run_kb(kb_root, "ingest")
    run_kb(kb_root, "rebuild")
    missing_card = run_kb(kb_root, "validate", check=False)
    assert missing_card.returncode != 0
    assert "missing card" in missing_card.stdout
    source.unlink()
    run_kb(kb_root, "ingest")
    orphan = run_kb(kb_root, "validate", check=False)
    assert "Orphaned source" in orphan.stdout
    assert (kb_root / "knowledge" / "docs" / "policy.md").exists()


def test_eval_hit_at_k(kb_root: Path):
    inbox = init_kb(kb_root)
    write_source(inbox, "validation-policy.txt", LONG_BODY)
    run_kb(kb_root, "ingest")
    run_kb(kb_root, "rebuild")
    eval_dir = kb_root / "eval"
    eval_dir.mkdir()
    (eval_dir / "questions.json").write_text(
        json.dumps(
            {
                "questions": [
                    {
                        "id": "cadence",
                        "question": "What is the validation frequency for challenger models?",
                        "expected_doc_ids": ["validation-policy"],
                        "must_contain": ["annually"],
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    proc = run_kb(kb_root, "eval", "--k", "3", "--json")
    report = json.loads(proc.stdout)
    assert report["hit_at_k"] == 1
    assert report["snippet_hits"] == 1
    assert proc.returncode == 0


def test_fts_query_strips_stopwords():
    scripts = str(ROOT / ".github" / "skills" / "ragless-kb" / "scripts")
    if scripts not in sys.path:
        sys.path.insert(0, scripts)
    import kb as kbmod

    assert kbmod.fts_query("What is the validation frequency?") == "validation OR frequency"


def test_large_eval_generator_tiny(kb_root: Path):
    import subprocess

    gen = ROOT / ".github" / "skills" / "ragless-kb" / "scripts" / "generate_large_eval.py"
    proc = subprocess.run(
        [sys.executable, str(gen), "--root", str(kb_root), "--docs", "12", "--questions", "6", "--seed", "1"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert proc.returncode == 0, proc.stderr
    assert len(list((kb_root / "input").glob("record-*"))) == 12
    payload = json.loads((kb_root / "eval" / "questions.json").read_text(encoding="utf-8"))
    assert len(payload["questions"]) == 6
    run_kb(kb_root, "ingest")
    run_kb(kb_root, "rebuild")
    report = json.loads(run_kb(kb_root, "eval", "--k", "5", "--json").stdout)
    assert report["hit_at_k"] == 6
    assert report["snippet_hits"] == 6


def test_skill_folder_is_self_contained():
    for base in (
        ROOT / ".github" / "skills" / "ragless-kb",
        ROOT / ".cursor" / "skills" / "ragless-kb",
    ):
        for name in (
            "SKILL.md",
            "README.md",
            "cookbook.md",
            "technical-background.md",
            "requirements.txt",
            "scripts/kb.py",
            "scripts/generate_large_eval.py",
            "references/chat.md",
            "references/qa-protocol.md",
        ):
            assert (base / name).is_file(), f"missing {base / name}"
        assert not (base / "agents").exists()
        assert not (base / "prompts").exists()


def test_harness_is_agents_and_skills_only():
    for harness in (ROOT / ".github", ROOT / ".cursor"):
        names = sorted(p.name for p in harness.iterdir() if not p.name.startswith("."))
        assert names == ["agents", "skills"], f"{harness} had {names}"
        agents = sorted(p.name for p in (harness / "agents").glob("*.md"))
        assert agents == ["docs-builder.agent.md", "docs-chat.agent.md"]
        skill = harness / "skills" / "ragless-kb"
        assert (skill / "SKILL.md").is_file()
        assert (skill / "scripts" / "kb.py").is_file()
        assert (skill / "scripts" / "generate_large_eval.py").is_file()
        assert not (skill / "agents").exists()
        assert not (skill / "prompts").exists()
