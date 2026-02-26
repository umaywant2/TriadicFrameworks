# cli_test_suite.py — Validator-grade tests for lens overlays

import unittest
from lens_main import activate_lens

class TestLensOverlayCLI(unittest.TestCase):

    def test_cyclone_overlay(self):
        try:
            activate_lens("cyclone")
        except Exception as e:
            self.fail(f"Cyclone overlay failed: {e}")

    def test_lightning_overlay(self):
        try:
            activate_lens("lightning")
        except Exception as e:
            self.fail(f"Lightning overlay failed: {e}")

    def test_tornado_overlay(self):
        try:
            activate_lens("tornado")
        except Exception as e:
            self.fail(f"Tornado overlay failed: {e}")

    def test_fragments_overlay(self):
        try:
            activate_lens("fragments")
        except Exception as e:
            self.fail(f"Fragments overlay failed: {e}")

    def test_invalid_overlay(self):
        with self.assertRaises(ValueError):
            activate_lens("unknown")

if __name__ == "__main__":
    unittest.main()

