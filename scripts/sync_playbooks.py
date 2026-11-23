"""Write each skill and contract as a JSON doc for the Dashboard's `playbooks` collection.

Scheduled runs can't reach this repo, so the agents read their instructions from the Dashboard.
Run this after changing any skill or contract, then upload the files with ArtifactData batch
(collection "playbooks", doc id = file name without .json).
"""
import json, pathlib, subprocess, sys, datetime
root = pathlib.Path(__file__).resolve().parent.parent
out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else root / "build" / "playbooks")
out.mkdir(parents=True, exist_ok=True)
commit = subprocess.run(["git", "-C", str(root), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
docs = {p.parent.name: p for p in (root / ".claude" / "skills").glob("*/SKILL.md")}
docs.update({"policy": root / "contracts/policy.md", "data-model": root / "contracts/data-model.md", "templates": root / "schedules/templates.md"})
for name, path in sorted(docs.items()):
    (out / f"{name}.json").write_text(json.dumps({"name": name, "source": str(path.relative_to(root)), "commit": commit,
        "updated": datetime.date.today().isoformat(), "text": path.read_text()}, ensure_ascii=False))
    print(name, path.stat().st_size)
