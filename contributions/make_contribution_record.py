#!/usr/bin/env python3
"""Generate the quarterly contribution record from git history and the records directory.

Credit follows the proposal's own principle: merged change requests (commits on main that touch the master
document, schemas, templates, tools or sim), sustained challenges (records/challenges/*.yaml with outcome
'sustained'), and resolutions performed — not lines changed. AI-assisted commits are counted and shown, not
discounted.
"""
import subprocess, re, pathlib, datetime as dt, collections, sys
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
AREAS = {"design": "docs/master/", "schemas": "schemas/", "templates": "templates/", "tools": "tools/", "sim": "sim/", "records": "records/", "docs-derived": "docs/short/"}

def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True).stdout

def commits(since=None):
    fmt = "%H%x1f%an%x1f%ad%x1f%B%x1e"
    args = ["log", "--date=short", f"--format={fmt}", "--no-merges"]
    if since: args.append(f"--since={since}")
    out = git(*args)
    for chunk in out.split("\x1e"):
        if not chunk.strip(): continue
        h, author, date, body = chunk.strip("\n").split("\x1f", 3)
        files = git("show", "--name-only", "--format=", h).split()
        assisted = re.findall(r"^Assisted-by:\s*(.+)$", body, re.M)
        logs = re.findall(r"^Log:\s*(.+)$", body, re.M)
        yield {"hash": h[:10], "author": author, "date": date, "files": files, "assisted": assisted, "logs": logs,
               "subject": body.strip().split("\n")[0]}

def main():
    since = sys.argv[1] if len(sys.argv) > 1 else (dt.date.today() - dt.timedelta(days=92)).isoformat()
    per = collections.defaultdict(lambda: collections.Counter())
    assisted_by = collections.defaultdict(collections.Counter)
    for c in commits(since):
        areas = {a for a, pfx in AREAS.items() if any(f.startswith(pfx) for f in c["files"])}
        for a in areas: per[c["author"]][a] += 1
        per[c["author"]]["commits"] += 1
        for m in c["assisted"]: assisted_by[c["author"]][m] += 1
    sustained = collections.Counter(); performed = collections.Counter()
    for f in (ROOT / "records/challenges").glob("*.y*ml"):
        d = yaml.safe_load(f.read_text())
        if d.get("outcome") == "sustained": sustained[d.get("challenger", "?")] += 1
    for f in (ROOT / "records/resolutions").glob("*.y*ml"):
        d = yaml.safe_load(f.read_text()); performed[d.get("performer", "?")] += 1
    print(f"# Contribution record\n\n*Generated {dt.date.today().isoformat()} from git history since {since} and from `records/`.*\n")
    print("Credit follows merged change requests and sustained challenges, not lines changed. AI assistance is recorded, not discounted.\n")
    print("| contributor | commits | design | schemas | templates | tools | sim | records | AI-assisted commits (models) |")
    print("|---|---|---|---|---|---|---|---|---|")
    for a, cnt in sorted(per.items(), key=lambda kv: -kv[1]["commits"]):
        ai = ", ".join(f"{m} ×{n}" for m, n in assisted_by[a].items()) or "—"
        print(f"| {a} | {cnt['commits']} | {cnt['design']} | {cnt['schemas']} | {cnt['templates']} | {cnt['tools']} | {cnt['sim']} | {cnt['records']} | {ai} |")
    print("\n## Sustained challenges\n")
    for who, n in sustained.most_common(): print(f"- {who}: {n}")
    if not sustained: print("- none yet")
    print("\n## Resolutions performed\n")
    for who, n in performed.most_common(): print(f"- {who}: {n}")
    if not performed: print("- none yet")

if __name__ == "__main__":
    main()
