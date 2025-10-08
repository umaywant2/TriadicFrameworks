```python
import unittest
import json
from loops_core import HarmonicLoops

class TestHarmonicLoops(unittest.TestCase):

    def setUp(self):
        self.hl = HarmonicLoops()

    def test_nest_structure(self):
        structure = self.hl.nest(2)
        self.assertIn("loop", structure)

    def test_feedback(self):
        fb = self.hl.feedback(3)
        self.assertEqual(len(fb), 3)
        self.assertIn("Resonance level 1", fb[0])

    def test_export(self):
        exported = self.hl.export(2)
        data = json.loads(exported)
        self.assertIn("loop", data)

if __name__ == "__main__":
    unittest.main()
