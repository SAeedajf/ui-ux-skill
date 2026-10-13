#!/usr/bin/env python3
"""Copy selected canonical Agent Skills into a host-specific discovery path."""
import argparse
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"
NAMES = sorted(p.name for p in SKILLS.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, help="Destination skill directory, e.g. .claude/skills")
    parser.add_argument("--skill", action="append", choices=NAMES, help="Skill to install; repeatable")
    parser.add_argument("--all", action="store_true", help="Install every Skill")
    parser.add_argument("--overwrite", action="store_true", help="Replace destination folders for selected Skills")
    parser.add_argument("--list", action="store_true", help="List available Skills")
    args = parser.parse_args()
    if args.list:
        print("\n".join(NAMES))
        return 0
    if not args.target:
        parser.error("--target is required unless --list is used")
    if bool(args.all) == bool(args.skill):
        parser.error("choose exactly one of --all or one or more --skill")
    selected = NAMES if args.all else list(dict.fromkeys(args.skill))
    target = args.target.expanduser().resolve()
    if target == ROOT or ROOT in target.parents:
        print("Refusing to install into the source repository.", file=sys.stderr)
        return 2
    target.mkdir(parents=True, exist_ok=True)
    conflicts = [name for name in selected if (target / name).exists()]
    if conflicts and not args.overwrite:
        print("Refusing to overwrite existing skill folders: " + ", ".join(conflicts), file=sys.stderr)
        return 2
    for name in selected:
        source = SKILLS / name
        destination = target / name
        with tempfile.TemporaryDirectory(prefix=".skill-install-", dir=target) as tmp:
            staged = Path(tmp) / name
            shutil.copytree(source, staged)
            if destination.exists():
                shutil.rmtree(destination)
            staged.rename(destination)
        print(f"installed {name} -> {destination}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
