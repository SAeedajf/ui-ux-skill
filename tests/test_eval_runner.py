import unittest
from scripts.run_codex_eval import load_scenarios


class EvalRunnerTests(unittest.TestCase):
    def test_activation_runner_has_all_independent_prompt_ids(self):
        rows = load_scenarios("activation")
        self.assertEqual(len(rows), 30)
        self.assertEqual(len({row["id"] for row in rows}), 30)
        self.assertTrue(all(row.get("prompt") for row in rows))

    def test_quality_runner_has_all_scenario_prompts(self):
        rows = load_scenarios("quality")
        self.assertEqual(len(rows), 19)
        self.assertEqual(len({row["id"] for row in rows}), 19)
        self.assertTrue(all(row.get("prompt") for row in rows))


if __name__ == "__main__":
    unittest.main()
