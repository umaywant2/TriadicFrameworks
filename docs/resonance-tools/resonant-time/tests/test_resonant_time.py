```python
import unittest
from resonant_time import ResonantTime

class TestResonantTime(unittest.TestCase):

    def setUp(self):
        self.rt = ResonantTime()

    def test_define(self):
        defs = self.rt.define()
        self.assertIn("E", defs)
        self.assertIn("Resonant-Time", defs)

    def test_cycle_length(self):
        seq = self.rt.cycle(5)
        self.assertEqual(len(seq), 5)

    def test_cycle_ascii(self):
        ascii_seq = self.rt.cycle(4, ascii=True)
        self.assertIsInstance(ascii_seq, str)
        self.assertIn("→", ascii_seq)

    def test_compare(self):
        comp = self.rt.compare()
        self.assertIn("Relativity", comp)
        self.assertIn("Resonant-Time", comp)

if __name__ == "__main__":
    unittest.main()

