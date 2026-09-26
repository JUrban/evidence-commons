"""Validate YAML/JSON records against the schemas in schemas/."""
from __future__ import annotations
import json, pathlib, sys
import yaml
from jsonschema import Draft202012Validator, RefResolver

ROOT = pathlib.Path(__file__).resolve().parents[2]
SCHEMAS = ROOT / "schemas"

KIND_BY_DIR = {"claims": "claim", "challenges": "challenge", "resolutions": "resolution",
               "assessments": "assessment", "markets": "market", "logs": "workflow_log",
               "contributions": "contribution", "usage": "usage", "protocols": "protocol"}

def load_schema(kind: str):
    path = SCHEMAS / f"{kind}.schema.json"
    schema = json.loads(path.read_text())
    store = {}
    for p in SCHEMAS.glob("*.schema.json"):
        s = json.loads(p.read_text()); store[s["$id"]] = s; store[p.name] = s
    resolver = RefResolver(base_uri=schema["$id"], referrer=schema, store=store)
    return Draft202012Validator(schema, resolver=resolver)

def kind_for(path: pathlib.Path) -> str | None:
    for part in path.parts[::-1]:
        if part in KIND_BY_DIR: return KIND_BY_DIR[part]
    return None

def validate_file(path: pathlib.Path, kind: str | None = None) -> list[str]:
    kind = kind or kind_for(path)
    if kind is None: return [f"{path}: cannot infer record kind from directory"]
    data = yaml.safe_load(path.read_text())
    v = load_schema(kind)
    return [f"{path}: {e.json_path}: {e.message}" for e in sorted(v.iter_errors(data), key=lambda e: e.path)]

def validate_paths(paths: list[str]) -> tuple[int, list[str]]:
    errors = []; n = 0
    for p in paths:
        p = pathlib.Path(p)
        files = [p] if p.is_file() else [f for f in p.rglob("*") if f.suffix in (".yaml", ".yml", ".json")]
        for f in files:
            n += 1; errors += validate_file(f)
    return n, errors

def main(argv=None):
    argv = argv or sys.argv[1:]
    n, errors = validate_paths(argv or [str(ROOT / "records")])
    for e in errors: print(e)
    print(f"{n} record(s) checked, {len(errors)} error(s)")
    return 1 if errors else 0
