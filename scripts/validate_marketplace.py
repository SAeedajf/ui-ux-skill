#!/usr/bin/env python3
"""Validate a repo-scoped OpenAI plugin marketplace and its local plugin sources."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path, PurePosixPath
try:
    from plugin_packaging import ROOT, EXPECTED_SKILLS, validate_package
except ModuleNotFoundError:
    from scripts.plugin_packaging import ROOT, EXPECTED_SKILLS, validate_package

CATEGORIES = {
    'Productivity', 'Creativity', 'Developer Tools', 'Business & Operations',
    'Data & Analytics', 'Communication', 'Education & Research', 'Security',
    'Finance', 'Healthcare', 'Travel', 'Entertainment', 'Other',
}
INSTALL_POLICIES = {'AVAILABLE', 'INSTALLED_BY_DEFAULT', 'NOT_AVAILABLE'}
AUTH_POLICIES = {'ON_INSTALL'}


def validate_marketplace(marketplace_path: Path, repo_root: Path | None = None) -> list[str]:
    errors: list[str] = []
    marketplace_path = marketplace_path.resolve()
    repo_root = (repo_root or marketplace_path.parents[2]).resolve()
    if repo_root.is_symlink(): return ['repository root must not be a symlink']
    try:
        data = json.loads(marketplace_path.read_text(encoding='utf-8'))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return [f'marketplace JSON cannot be read: {exc}']
    if not isinstance(data, dict): return ['marketplace root must be a JSON object']
    name = data.get('name')
    if not isinstance(name, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
        errors.append('marketplace name must be a stable kebab-case identifier')
    interface = data.get('interface')
    if not isinstance(interface, dict) or not isinstance(interface.get('displayName'), str) or not interface.get('displayName','').strip():
        errors.append('interface.displayName is required')
    plugins = data.get('plugins')
    if not isinstance(plugins, list) or not plugins:
        errors.append('plugins must be a non-empty array')
        return errors
    ids = []
    for index, entry in enumerate(plugins):
        label = f'plugins[{index}]'
        if not isinstance(entry, dict):
            errors.append(f'{label} must be an object'); continue
        plugin_id = entry.get('name')
        if not isinstance(plugin_id, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', plugin_id):
            errors.append(f'{label}.name must be a stable kebab-case plugin ID')
        else: ids.append(plugin_id)
        source = entry.get('source')
        if not isinstance(source, dict) or source.get('source') != 'local':
            errors.append(f'{label}.source must be a local source object'); continue
        rel = source.get('path')
        if not isinstance(rel, str) or not rel.startswith('./'):
            errors.append(f'{label}.source.path must be ./ relative to marketplace/repository root')
            continue
        path = PurePosixPath(rel[2:])
        if path.is_absolute() or not path.parts or '..' in path.parts or ':' in rel or '~' in rel or '\\' in rel:
            errors.append(f'{label}.source.path contains an unsafe or personal path'); continue
        plugin_root = (repo_root / Path(*path.parts)).resolve()
        if repo_root not in plugin_root.parents:
            errors.append(f'{label}.source.path resolves outside repository root'); continue
        policy = entry.get('policy')
        if not isinstance(policy, dict): errors.append(f'{label}.policy is required'); policy = {}
        if policy.get('installation') not in INSTALL_POLICIES:
            errors.append(f'{label}.policy.installation has an unsupported value')
        if policy.get('authentication') not in AUTH_POLICIES:
            errors.append(f'{label}.policy.authentication has an unsupported value')
        if entry.get('category') not in CATEGORIES:
            errors.append(f'{label}.category is not a supported plugin category')
        manifest_path = plugin_root / 'plugin.json'
        if plugin_root.is_symlink() or not manifest_path.is_file() or manifest_path.is_symlink():
            errors.append(f'{label}: plugin path or plugin.json is missing/unsafe'); continue
        try:
            manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            errors.append(f'{label}: invalid plugin.json: {exc}'); continue
        if manifest.get('name') != plugin_id:
            errors.append(f'{label}: marketplace ID does not match plugin manifest')
        if not isinstance(manifest.get('version'), str) or not re.fullmatch(r'\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?', manifest.get('version','')):
            errors.append(f'{label}: plugin manifest must contain a SemVer version')
        if plugin_id == 'ui-ux-pro':
            found = {p.name for p in (plugin_root / 'skills').iterdir() if p.is_dir()} if (plugin_root / 'skills').is_dir() else set()
            if found != EXPECTED_SKILLS:
                errors.append(f'{label}: expected all 15 Skills; missing={sorted(EXPECTED_SKILLS-found)}, unexpected={sorted(found-EXPECTED_SKILLS)}')
            errors.extend(f'{label}: {e}' for e in validate_package(plugin_root))
    if len(ids) != len(set(ids)): errors.append('plugin IDs must be unique')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('marketplace', nargs='?', type=Path, default=ROOT / '.agents/plugins/marketplace.json')
    parser.add_argument('--repo-root', type=Path, default=ROOT, help='repository root for ./ source paths')
    args = parser.parse_args()
    errors = validate_marketplace(args.marketplace, args.repo_root)
    if errors:
        for error in errors: print(f'FAIL: {error}')
        return 1
    print(f'PASS: {args.marketplace} has a valid marketplace and UI/UX Pro source')
    return 0

if __name__ == '__main__': raise SystemExit(main())
