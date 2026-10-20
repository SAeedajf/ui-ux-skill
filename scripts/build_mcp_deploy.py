#!/usr/bin/env python3
"""Build a self-contained, private-root cPanel deployment archive."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "mcp-server"
SKILLS = ROOT / ".agents" / "skills"
OUT = ROOT / "dist"
ARCHIVE = OUT / "ui-ux-pro-mcp-0.1.0-cpanel.zip"
MANIFEST = OUT / "ui-ux-pro-mcp-0.1.0-cpanel.manifest.json"
PREFIX = "ui-ux-pro-mcp/"


def selected_files() -> list[tuple[Path, str]]:
    if not (APP / "vendor" / "autoload.php").is_file():
        raise SystemExit("Missing mcp-server/vendor. Run composer install --working-dir=mcp-server --no-dev first.")
    paths: list[tuple[Path, str]] = []
    for relative in ("composer.json", "composer.lock", "config.example.php", "cpanel-entrypoint.php"):
        path = APP / relative
        if path.is_file():
            paths.append((path, f"{PREFIX}{relative}"))
    for folder in ("src", "public", "vendor"):
        base = APP / folder
        for path in sorted(p for p in base.rglob("*") if p.is_file() and not p.is_symlink()):
            paths.append((path, f"{PREFIX}{folder}/{path.relative_to(base).as_posix()}"))
    for skill_dir in sorted(p for p in SKILLS.iterdir() if p.is_dir() and not p.is_symlink()):
        files = [skill_dir / "SKILL.md", *sorted((skill_dir / "references").rglob("*.md"))] if (skill_dir / "references").is_dir() else [skill_dir / "SKILL.md"]
        for path in files:
            if path.is_file() and not path.is_symlink():
                rel = path.relative_to(SKILLS).as_posix()
                paths.append((path, f"{PREFIX}content/skills/{rel}"))
    skills = {name.split("/")[3] for _, name in paths if "/content/skills/" in name and name.endswith("/SKILL.md")}
    if len(skills) != 15:
        raise SystemExit(f"Expected 15 canonical Skills in deployment bundle; found {len(skills)}.")
    return paths


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Validate current archive without rebuilding it")
    args = parser.parse_args()
    files = selected_files()
    records = []
    for path, archive_name in files:
        records.append({"path": archive_name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "size": path.stat().st_size})
    manifest = {"name": "ui-ux-pro-mcp", "version": "0.1.0", "transport": "streamable-http", "skills": 15, "files": records}
    OUT.mkdir(parents=True, exist_ok=True)
    expected_manifest = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode()
    if args.check:
        if not ARCHIVE.is_file() or not MANIFEST.is_file():
            raise SystemExit("Deployment archive/manifest is missing; run the build without --check.")
        if MANIFEST.read_bytes() != expected_manifest:
            raise SystemExit("Deployment manifest differs from current source files.")
        with zipfile.ZipFile(ARCHIVE) as archive:
            actual = {
                name: hashlib.sha256(archive.read(name)).hexdigest()
                for name in archive.namelist()
                if not name.endswith("/") and name != f"{PREFIX}DEPLOYMENT-MANIFEST.json"
            }
        expected = {record["path"]: record["sha256"] for record in records}
        if actual != expected:
            raise SystemExit("Deployment archive differs from current source files.")
        print(f"PASS: {len(records)} files; 15 Skills; deployment archive is current")
        return 0

    OUT.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path, archive_name in files:
            info = zipfile.ZipInfo(archive_name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100644 & 0xFFFF) << 16
            archive.writestr(info, path.read_bytes())
        info = zipfile.ZipInfo(f"{PREFIX}DEPLOYMENT-MANIFEST.json", date_time=(2026, 1, 1, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = (0o100644 & 0xFFFF) << 16
        archive.writestr(info, expected_manifest)
    MANIFEST.write_bytes(expected_manifest)
    print(f"Built: {ARCHIVE.relative_to(ROOT)} ({len(records)} files; 15 Skills)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
