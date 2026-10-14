import unittest
from scripts.run_codex_eval import build_parser, load_scenarios


class EvalRunnerTests(unittest.TestCase):
    def test_model_override_is_optional_so_the_host_can_choose(self):
        args = build_parser().parse_args(["activation", "--dry-run"])
        self.assertIsNone(args.model)

    def test_activation_runner_has_all_independent_prompt_ids(self):
        rows = load_scenarios("activation")
        self.assertEqual(len(rows), 30)
        self.assertEqual(len({row["id"] for row in rows}), 30)
        self.assertTrue(all(row.get("prompt") for row in rows))

    def test_quality_runner_has_all_scenario_prompts(self):
        rows = load_scenarios("quality")
        self.assertEqual(len(rows), 29)
        self.assertEqual(len({row["id"] for row in rows}), 29)
        self.assertTrue(all(row.get("prompt") for row in rows))


if __name__ == "__main__":
    unittest.main()
