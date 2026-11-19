#!/usr/bin/env python3
"""Validate patterns/ against guidelines/decisions.yaml -> pattern_selection.
Usage: python3 scripts/check_patterns.py   (exit 1 on error)"""
import re, sys, pathlib
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
REQUIRED = ["Purpose", "Use when", "Do not use when", "Components", "Structure",
            "Interaction flow", "States", "Validation/errors", "Accessibility",
            "Responsive behavior", "Tokens", "Related components/patterns"]
# Specs written before the format was fixed: only warn about missing sections.
LEGACY = {"patterns/authentication/login-pattern-spec.md", "patterns/navigation/sidebar-pattern-spec.md",
          "patterns/filter-bar/filter-bar-pattern-spec.md", "patterns/skill/skill-pattern-spec.md"}

dec = yaml.safe_load((ROOT / "guidelines/decisions.yaml").read_text(encoding="utf-8"))
ps, cs = dec.get("pattern_selection", {}), dec.get("component_selection", {})
errors, warns = [], []

specs_in_entries = set()
for name, e in ps.items():
    for k in ("need", "intent", "components", "spec", "status", "not_for"):
        if k not in e:
            errors.append(f"{name}: missing field '{k}'")
    st = e.get("status")
    if st not in ("built", "spec", "candidate"):
        errors.append(f"{name}: invalid status {st!r}")
    sp = e.get("spec")
    if st == "candidate":
        if sp:
            errors.append(f"{name}: candidate must have spec: null")
        continue
    if not sp:
        errors.append(f"{name}: status {st} requires a spec path"); continue
    specs_in_entries.add(sp)
    f = ROOT / sp
    if not f.exists():
        errors.append(f"{name}: spec not found: {sp}"); continue
    text = f.read_text(encoding="utf-8")
    if sp not in LEGACY and sp not in ("patterns/navigation/sidebar-pattern-spec.md",):
        missing = [h for h in REQUIRED if not re.search(r"^## " + re.escape(h) + r"\s*$", text, re.M)]
        if missing:
            errors.append(f"{sp}: missing sections {missing}")
    elif sp in LEGACY:
        missing = [h for h in REQUIRED if not re.search(re.escape(h), text, re.I)]
        if missing:
            warns.append(f"{sp} (legacy): sections not found {missing}")

for f in sorted((ROOT / "patterns").glob("*/*-pattern-spec.md")):
    rel = f.relative_to(ROOT).as_posix()
    if rel not in specs_in_entries:
        errors.append(f"{rel}: no pattern_selection entry points to it")

for name, txt in cs.items():
    m = re.search(r"patterns/([a-z-]+)/", txt)
    if m and not (ROOT / "patterns" / m.group(1)).is_dir():
        errors.append(f"component_selection.{name}: references missing patterns/{m.group(1)}/")
    if "Brick of pattern" in txt and not m:
        errors.append(f"component_selection.{name}: brick without patterns/ path")

for w in warns: print("WARN ", w)
for e in errors: print("ERROR", e)
print(f"{len(ps)} patterns, {len(errors)} error(s), {len(warns)} warning(s)")
sys.exit(1 if errors else 0)
