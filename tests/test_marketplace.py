import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.plugin_packaging import manifest_bytes

ROOT = Path(__file__).resolve().parents[1]


def catalog(source_path='./plugins/ui-ux-pro'):
    return {
        'name': 'ui-ux-pro-marketplace',
        'interface': {'displayName': 'UI/UX Pro Marketplace'},
        'plugins': [{
            'name': 'ui-ux-pro',
            'source': {'source': 'local', 'path': source_path},
            'policy': {'installation': 'AVAILABLE', 'authentication': 'ON_INSTALL'},
            'category': 'Creativity',
        }],
    }


class MarketplaceValidationTests(unittest.TestCase):
    def validate_fixture(self, data):
        from scripts.validate_marketplace import validate_marketplace
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            shutil.copytree(ROOT / 'plugins/ui-ux-pro', repo / 'plugins/ui-ux-pro')
            marketplace = repo / '.agents/plugins/marketplace.json'
            marketplace.parent.mkdir(parents=True)
            marketplace.write_text(json.dumps(data), encoding='utf-8')
            return validate_marketplace(marketplace, repo)

    def test_current_portable_manifest_uses_fixed_skills_directory_without_extension(self):
        manifest = json.loads(manifest_bytes())
        self.assertNotIn('extensions', manifest)
        self.assertEqual('ui-ux-pro', manifest['name'])

    def test_official_shape_local_path_and_all_fifteen_skills_validate(self):
        self.assertEqual([], self.validate_fixture(catalog()))

    def test_duplicate_plugin_identity_is_rejected(self):
        data = catalog()
        data['plugins'].append(dict(data['plugins'][0]))
        errors = self.validate_fixture(data)
        self.assertTrue(any('unique' in error.lower() for error in errors), errors)

    def test_traversal_home_and_absolute_sources_are_rejected(self):
        for path in ('../../outside', '~/private/plugin', '/tmp/plugin', './plugins/../../secret'):
            with self.subTest(path=path):
                errors = self.validate_fixture(catalog(path))
                self.assertTrue(errors, f'accepted unsafe path {path}')

    def test_missing_skill_and_bad_install_policy_are_rejected(self):
        data = catalog()
        data['plugins'][0]['policy']['installation'] = 'SILENTLY_INSTALL'
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            shutil.copytree(ROOT / 'plugins/ui-ux-pro', repo / 'plugins/ui-ux-pro')
            (repo / 'plugins/ui-ux-pro/skills/ux-discovery/SKILL.md').unlink()
            marketplace = repo / '.agents/plugins/marketplace.json'
            marketplace.parent.mkdir(parents=True)
            marketplace.write_text(json.dumps(data), encoding='utf-8')
            from scripts.validate_marketplace import validate_marketplace
            errors = validate_marketplace(marketplace, repo)
        self.assertTrue(any('installation' in error.lower() for error in errors), errors)
        self.assertTrue(any('skill' in error.lower() or 'manifest' in error.lower() for error in errors), errors)

    def test_nested_references_are_resolved_from_each_markdown_file(self):
        from scripts.plugin_packaging import validate_package
        with tempfile.TemporaryDirectory() as tmp:
            package = Path(tmp) / 'plugin'
            shutil.copytree(ROOT / 'plugins/ui-ux-pro', package)
            nested = package / 'skills/responsive-design/references/adapters/web.md'
            nested.write_text(nested.read_text() + '\n[good](../adaptation.md)\n')
            self.assertEqual([], validate_package(package))
            nested.write_text(nested.read_text() + '\n[bad](../../../outside.md)\n')
            errors = validate_package(package)
            self.assertTrue(any('escapes Skill root' in error or 'broken local reference' in error for error in errors), errors)

    def test_malformed_json_and_external_source_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            marketplace = repo / '.agents/plugins/marketplace.json'
            marketplace.parent.mkdir(parents=True)
            marketplace.write_text('{broken', encoding='utf-8')
            from scripts.validate_marketplace import validate_marketplace
            self.assertTrue(validate_marketplace(marketplace, repo))
        data = catalog()
        data['plugins'][0]['source'] = {'source': 'npm', 'package': 'ui-ux-pro'}
        self.assertTrue(self.validate_fixture(data))


if __name__ == '__main__':
    unittest.main()
