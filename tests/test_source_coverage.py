import tempfile
import unittest
from pathlib import Path

from scripts.source_coverage import source_ids_in_files


class SourceCoverageTests(unittest.TestCase):
    def test_explicit_ids_and_source_ranges_are_detected(self):
        with tempfile.TemporaryDirectory() as directory:
            reference = Path(directory) / "reference.md"
            reference.write_text("Use **1, 3–4** and consult [S2] for context.", encoding="utf-8")
            self.assertEqual(source_ids_in_files([reference], set(range(1, 6))), {1, 2, 3, 4})

    def test_unlinked_registry_ids_remain_visible_to_the_caller(self):
        with tempfile.TemporaryDirectory() as directory:
            reference = Path(directory) / "reference.md"
            reference.write_text("Use [S2] for the method.", encoding="utf-8")
            registry_ids = set(range(1, 4))
            missing = registry_ids - source_ids_in_files([reference], registry_ids)
            self.assertEqual(missing, {1, 3})


if __name__ == "__main__":
    unittest.main()
