```python
import unittest
import json
from tft_core import TFT

class TestTFT(unittest.TestCase):

    def setUp(self):
        self.tft = TFT()

    def test_define(self):
        defs = self.tft.define()
        self.assertIn("TFT", defs)

    def test_apply_known_domain(self):
        cpu = self.tft.apply("cpu")
        self.assertIsInstance(cpu, list)

    def test_apply_unknown_domain(self):
        result = self.tft.apply("unknown")
        self.assertIsInstance(result, str)

    def test_compare(self):
        comp = self.tft.compare()
        self.assertIn("Triadic", comp)
        self.assertIn("Quadratic", comp)

    def test_export_known_domain(self):
        exported = self.tft.export("cpu")
        data = json.loads(exported)
        self.assertIn("cpu", data)

    def test_export_unknown_domain(self):
        exported = self.tft.export("unknown")
        data = json.loads(exported)
        self.assertIn("error", data)

if __name__ == "__main__":
    unittest.main()

