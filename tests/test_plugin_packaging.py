import json
import os
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / 'scripts' / 'build-plugin.py'
VALIDATE = ROOT / 'scripts' / 'validate-plugin.py'


def run(*args, cwd=ROOT):
    return subprocess.run([sys.executable, *map(str, args)], cwd=cwd, text=True, capture_output=True)


class PluginPackagingTests(unittest.TestCase):
    def test_build_is_repeatable_and_check_is_read_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / 'package'
            first = run(BUILD, '--output', output)
            self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
            snapshot = {p.relative_to(output).as_posix(): p.read_bytes() for p in output.rglob('*') if p.is_file()}
            second = run(BUILD, '--output', output)
            self.assertEqual(second.returncode, 0, second.stdout + second.stderr)
            self.assertEqual(snapshot, {p.relative_to(output).as_posix(): p.read_bytes() for p in output.rglob('*') if p.is_file()})
            check = run(BUILD, '--check', '--output', output)
            self.assertEqual(check.returncode, 0, check.stdout + check.stderr)
            self.assertEqual(snapshot, {p.relative_to(output).as_posix(): p.read_bytes() for p in output.rglob('*') if p.is_file()})

    def test_package_contains_exact_source_skill_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / 'package'
            result = run(BUILD, '--output', output)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            sources = ROOT / '.agents' / 'skills'
            for source in sources.rglob('*'):
                relative = source.relative_to(sources)
                if source.is_file() and not any(part.startswith('.') for part in relative.parts):
                    self.assertEqual(source.read_bytes(), (output / 'skills' / relative).read_bytes())
            self.assertEqual(15, len(list((output / 'skills').iterdir())))

    def test_invalid_manifest_and_source_drift_fail_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / 'package'
            build = run(BUILD, '--output', output)
            self.assertEqual(build.returncode, 0, build.stdout + build.stderr)
            manifest = output / 'plugin.json'
            data = json.loads(manifest.read_text())
            data['unsupported'] = True
            manifest.write_text(json.dumps(data))
            invalid = run(VALIDATE, '--package', output)
            self.assertNotEqual(invalid.returncode, 0)
            self.assertIn('FAIL', invalid.stdout + invalid.stderr)
            data.pop('unsupported')
            manifest.write_text(json.dumps(data))
            skill = next((output / 'skills').glob('*/SKILL.md'))
            skill.write_text(skill.read_text() + '\nDrift.\n')
            drift = run(VALIDATE, '--package', output)
            self.assertNotEqual(drift.returncode, 0)

    def test_broken_reference_and_unsafe_files_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / 'package'
            build = run(BUILD, '--output', output)
            self.assertEqual(build.returncode, 0, build.stdout + build.stderr)
            ref = next((output / 'skills').glob('*/SKILL.md'))
            ref.write_text(ref.read_text() + '\n[broken](references/missing.md)\n')
            result = run(VALIDATE, '--package', output)
            self.assertNotEqual(result.returncode, 0)
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / 'package'
            result = run(BUILD, '--output', output)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            (output / 'skills' / 'leak.env').write_text('TOKEN=not-a-real-secret')
            rejected = run(VALIDATE, '--package', output)
            self.assertNotEqual(rejected.returncode, 0)

    def test_archive_is_valid_reproducible_and_has_external_provenance(self):
        from scripts.plugin_packaging import build_archive
        with tempfile.TemporaryDirectory() as tmp:
            package = Path(tmp) / 'package'
            build = run(BUILD, '--output', package)
            self.assertEqual(build.returncode, 0, build.stdout + build.stderr)
            zip_one, sidecar_one = build_archive(package, Path(tmp) / 'one.zip', 'a' * 40, '0.1.0')
            zip_two, _ = build_archive(package, Path(tmp) / 'two.zip', 'a' * 40, '0.1.0')
            self.assertEqual(zip_one.read_bytes(), zip_two.read_bytes())
            with zipfile.ZipFile(zip_one) as archive:
                self.assertIsNone(archive.testzip())
                names = archive.namelist()
                self.assertIn('plugin.json', names)
                self.assertIn('LICENSE', names)
                self.assertFalse(any(n.startswith('/') or '..' in Path(n).parts for n in names))
            provenance = json.loads(sidecar_one.read_text())
            self.assertEqual('a' * 40, provenance['source_commit'])
            self.assertEqual('PASS', provenance['validation_status'])
            self.assertEqual(64, len(provenance['zip_sha256']))

    def test_offline_build_and_unsafe_reference_paths(self):
        from unittest.mock import patch
        from scripts.plugin_packaging import build_package
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / 'offline'
            with patch('urllib.request.urlopen', side_effect=AssertionError('network access attempted')):
                build_package(output)
            self.assertTrue((output / 'plugin.json').is_file())
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / 'package'
            result = run(BUILD, '--output', output)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            skill = next((output / 'skills').glob('*/SKILL.md'))
            skill.write_text(skill.read_text() + '\n[escape](../../outside.md)\n')
            rejected = run(VALIDATE, '--package', output, '--structure-only')
            self.assertNotEqual(rejected.returncode, 0)

    def test_malformed_yaml_and_bad_skill_name_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / 'package'
            result = run(BUILD, '--output', output)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            skill = next((output / 'skills').glob('*/SKILL.md'))
            skill.write_text('---\nname: [unterminated\ndescription: x\n---\nbody\n')
            rejected = run(VALIDATE, '--package', output, '--structure-only')
            self.assertNotEqual(rejected.returncode, 0)

    def test_symlink_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / 'package'
            result = run(BUILD, '--output', output)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            target = output / 'skills' / 'accessibility-inclusive-design' / 'unsafe-link'
            target.symlink_to(Path('/etc/passwd'))
            rejected = run(VALIDATE, '--package', output)
            self.assertNotEqual(rejected.returncode, 0)


if __name__ == '__main__':
    unittest.main()
