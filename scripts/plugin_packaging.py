"""Deterministic packaging and structural validation for UI/UX Pro."""
from __future__ import annotations
import hashlib, json, os, re, shutil, stat, zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
METADATA = ROOT / 'config/ui-ux-pro.json'
SCHEMA = ROOT / 'schemas/agent-plugins/1.0.0/plugin.schema.json'
EXPECTED_SKILLS = {
    'accessibility-inclusive-design', 'color-systems', 'design-systems', 'ethical-persuasion',
    'forms-input', 'information-architecture', 'interaction-patterns', 'interface-layout',
    'journey-mapping', 'navigation-controls', 'persian-rtl-localization', 'responsive-design',
    'ui-ux-review', 'ux-discovery', 'visual-hierarchy',
}
SECRET_PATTERNS = [re.compile(p, re.I) for p in (
    r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,})\b',
    r'\bAKIA[0-9A-Z]{16}\b',
    r'\b(?:api[_-]?key|secret|token)\s*[:=]\s*["\']?[A-Za-z0-9_./+=-]{24,}',
)]


def load_metadata():
    return json.loads(METADATA.read_text(encoding='utf-8'))


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_files(source_root: Path | None = None) -> dict[str, bytes]:
    source_root = source_root or ROOT / '.agents/skills'
    result = {}
    if not source_root.is_dir():
        raise ValueError(f'missing canonical skills directory: {source_root}')
    for skill_dir in sorted(source_root.iterdir(), key=lambda p: p.name):
        if skill_dir.is_symlink():
            raise ValueError(f'symlink rejected: {skill_dir}')
        if not skill_dir.is_dir() or skill_dir.name.startswith('.'):
            continue
        for path in sorted(skill_dir.rglob('*')):
            rel = path.relative_to(source_root).as_posix()
            if path.is_symlink():
                raise ValueError(f'symlink rejected: {rel}')
            if path.is_dir():
                if path.name.startswith('.') or path.name in {'__pycache__', 'node_modules'}:
                    raise ValueError(f'hidden/cache directory rejected: {rel}')
                continue
            if not path.is_file():
                raise ValueError(f'unsupported filesystem entry: {rel}')
            if any(part.startswith('.') for part in PurePosixPath(rel).parts) or path.suffix.lower() in {'.pyc', '.pyo', '.env', '.key', '.pem', '.p12', '.pfx'}:
                raise ValueError(f'hidden/cache/private file rejected: {rel}')
            raw = path.read_bytes()
            try:
                content = raw.decode('utf-8')
            except UnicodeDecodeError as exc:
                raise ValueError(f'binary/non-UTF-8 file rejected: {rel}') from exc
            if any(pattern.search(content) for pattern in SECRET_PATTERNS):
                raise ValueError(f'credential-like content rejected: {rel}')
            result[rel] = raw
    skills = {PurePosixPath(p).parts[0] for p in result}
    if skills != EXPECTED_SKILLS:
        raise ValueError(f'expected exact 15 Skills; missing={sorted(EXPECTED_SKILLS-skills)}, unexpected={sorted(skills-EXPECTED_SKILLS)}')
    for skill in EXPECTED_SKILLS:
        if f'{skill}/SKILL.md' not in result:
            raise ValueError(f'{skill}: missing SKILL.md')
    return result


def manifest_bytes():
    m = load_metadata()
    manifest = {
        '$schema': 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json',
        'name': m['plugin_id'], 'version': m['version'], 'description': m['description'],
        'repository': m['repository'], 'license': m['license'],
        'keywords': ['ui', 'ux', 'design', 'accessibility', 'agent-skills'],
    }
    return (json.dumps(manifest, ensure_ascii=False, indent=2) + '\n').encode()


def package_files(source_root: Path | None = None) -> dict[str, bytes]:
    files = {'plugin.json': manifest_bytes(), 'LICENSE': (ROOT / 'LICENSE').read_bytes()}
    files.update({f'skills/{name}': content for name, content in source_files(source_root).items()})
    return files


def build_package(output: Path, source_root: Path | None = None, check: bool = False):
    expected = package_files(source_root)
    if check:
        actual = {}
        if output.exists():
            for p in output.rglob('*'):
                rel = p.relative_to(output).as_posix()
                if p.is_symlink():
                    raise ValueError(f'symlink rejected in package: {rel}')
                if p.is_file(): actual[rel] = p.read_bytes()
        if actual != expected:
            missing = sorted(set(expected)-set(actual)); extra = sorted(set(actual)-set(expected))
            changed = sorted(k for k in expected.keys() & actual.keys() if expected[k] != actual[k])
            raise ValueError(f'package drift: missing={missing}, extra={extra}, changed={changed}')
        return
    output = output.resolve()
    if output == ROOT or ROOT in output.parents:
        # Generated output may be the canonical plugins directory only.
        if output != ROOT / 'plugins/ui-ux-pro':
            raise ValueError('refusing to write package inside source tree outside plugins/ui-ux-pro')
    output.parent.mkdir(parents=True, exist_ok=True)
    stage = output.with_name(output.name + '.tmp-build')
    if stage.exists(): shutil.rmtree(stage)
    stage.mkdir()
    try:
        for rel, content in expected.items():
            target = stage / PurePosixPath(rel)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
        if output.exists(): shutil.rmtree(output)
        stage.replace(output)
    finally:
        if stage.exists(): shutil.rmtree(stage)


def _yaml_frontmatter(text: str, filename: str):
    import yaml
    if not text.startswith('---\n'):
        raise ValueError(f'{filename}: missing YAML frontmatter')
    closing = text.find('\n---\n', 4)
    if closing < 0:
        raise ValueError(f'{filename}: malformed YAML frontmatter delimiters')
    frontmatter = text[4:closing]
    try:
        data = yaml.safe_load(frontmatter)
    except yaml.YAMLError as exc:
        raise ValueError(f'{filename}: invalid YAML frontmatter: {exc}') from exc
    if not isinstance(data, dict) or any(not isinstance(k, str) for k in data):
        raise ValueError(f'{filename}: frontmatter must be a mapping of string keys')
    return data, text[closing + 5:]


def validate_package(package: Path, expected_source: Path | None = None):
    import jsonschema
    errors = []
    package = package.resolve()
    try:
        manifest_path = package / 'plugin.json'
        if manifest_path.is_symlink() or not manifest_path.is_file(): raise ValueError('missing or unsafe plugin.json')
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        schema = json.loads(SCHEMA.read_text(encoding='utf-8'))
        jsonschema.Draft202012Validator(schema).validate(manifest)
        if manifest.get('name') != 'ui-ux-pro': errors.append('manifest name must be ui-ux-pro')
        if manifest.get('extensions', {}).get('skills') is not None: errors.append('skills use the fixed root skills/ directory; extensions.skills is not supported')
        seen = set()
        skills_root = package / 'skills'
        for p in package.rglob('*'):
            rel = p.relative_to(package).as_posix()
            if p.is_symlink(): errors.append(f'symlink rejected: {rel}'); continue
            if p.is_file() and p.name != 'plugin.json':
                if any(part.startswith('.') for part in PurePosixPath(rel).parts) or p.suffix.lower() in {'.env','.pem','.key','.pyc','.pyo','.zip'}:
                    errors.append(f'hidden/private/cache file rejected: {rel}')
                try: content = p.read_text(encoding='utf-8')
                except UnicodeDecodeError: errors.append(f'binary file rejected: {rel}'); continue
                if any(pattern.search(content) for pattern in SECRET_PATTERNS): errors.append(f'credential-like content rejected: {rel}')
        if not skills_root.is_dir(): errors.append('missing skills directory')
        else:
            skill_dirs = sorted(p for p in skills_root.iterdir() if p.is_dir())
            names = [p.name for p in skill_dirs]
            if set(names) != EXPECTED_SKILLS: errors.append(f'exact 15 Skill IDs required; found={names}')
            if len(names) != len(set(names)): errors.append('duplicate Skill IDs')
            for directory in skill_dirs:
                skillfile = directory / 'SKILL.md'
                if not skillfile.is_file() or skillfile.is_symlink(): errors.append(f'{directory.name}: missing/unsafe SKILL.md'); continue
                try:
                    text = skillfile.read_text(encoding='utf-8')
                    front, body = _yaml_frontmatter(text, f'{directory.name}/SKILL.md')
                    name, desc = front.get('name'), front.get('description')
                    if not isinstance(name,str) or name != directory.name or not re.fullmatch(r'(?!-)(?!.*--)[a-z0-9-]{1,64}(?<!-)',name): errors.append(f'{directory.name}: invalid/mismatched Skill name')
                    if not isinstance(desc,str) or not (1 <= len(desc) <= 1024): errors.append(f'{directory.name}: description must contain 1..1024 chars')
                    documents = sorted(directory.rglob('*.md'))
                    for document in documents:
                        doc_text = document.read_text(encoding='utf-8')
                        refs = re.findall(r'\[[^]]+\]\(([^)]+)\)', doc_text)
                        refs += [ref for ref in re.findall(r'`([^`\n]+\.(?:md|py|json|csv|txt))`', doc_text) if '/' in ref or '\\' in ref]
                        for ref in refs:
                            if ref.startswith(('http://','https://','#','mailto:')): continue
                            pathpart = ref.split('#',1)[0].split('?',1)[0]
                            if not pathpart: continue
                            rel = PurePosixPath(pathpart)
                            if rel.is_absolute() or ':' in pathpart or pathpart.startswith(('~','/')) or '\\' in pathpart:
                                errors.append(f'{directory.name}: unsafe reference path in {document.relative_to(directory)}: {ref}'); continue
                            target = (document.parent / Path(*rel.parts)).resolve()
                            if directory.resolve() not in target.parents and target != directory.resolve(): errors.append(f'{directory.name}: reference escapes Skill root in {document.relative_to(directory)}: {ref}')
                            elif not target.exists(): errors.append(f'{directory.name}: broken local reference in {document.relative_to(directory)}: {ref}')
                except (OSError, UnicodeError, ValueError) as exc: errors.append(str(exc))
        if expected_source is not None:
            expected = package_files(expected_source)
            actual = {p.relative_to(package).as_posix(): p.read_bytes() for p in package.rglob('*') if p.is_file()}
            if actual != expected:
                errors.append('package bytes differ from canonical source/manifest (rebuild required)')
    except (OSError, json.JSONDecodeError, jsonschema.ValidationError, ValueError) as exc:
        errors.append(f'manifest/schema error: {exc}')
    return errors


def build_archive(package: Path, zip_path: Path, source_commit: str, version: str):
    if not re.fullmatch(r'[0-9a-f]{40}', source_commit): raise ValueError('source_commit must be a full 40-character lowercase Git SHA')
    package = package.resolve(); zip_path = zip_path.resolve(); zip_path.parent.mkdir(parents=True, exist_ok=True)
    files = {p.relative_to(package).as_posix(): p.read_bytes() for p in package.rglob('*') if p.is_file()}
    if not files or 'plugin.json' not in files: raise ValueError('package is missing plugin.json or files')
    with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in sorted(files):
            info = zipfile.ZipInfo(name, date_time=(2020,1,1,0,0,0))
            info.compress_type = zipfile.ZIP_DEFLATED; info.create_system = 3; info.external_attr = (stat.S_IFREG | 0o644) << 16
            archive.writestr(info, files[name], compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    inventory = [{'path': name, 'sha256': sha256(data), 'size_bytes': len(data)} for name,data in sorted(files.items())]
    sidecar = zip_path.with_suffix('.manifest.json')
    provenance = {'package':'ui-ux-pro','version':version,'source_commit':source_commit,'validation_status':'PASS','zip_sha256':sha256(zip_path.read_bytes()),'files':inventory}
    sidecar.write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return zip_path, sidecar
