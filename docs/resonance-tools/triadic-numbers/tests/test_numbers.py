```python
import unittest
import json
from numbers_core import TriadicNumbers

class TestTriadicNumbers(unittest.TestCase):

    def setUp(self):
        self.tn = TriadicNumbers()

    def test_genesis(self):
        g = self.tn.genesis(3)
        self.assertIn(1, g)
        self.assertEqual(len(g), 3)

    def test_map_sequence(self):
        seq = self.tn.map_sequence("E M OC")
        self.assertEqual(len(seq), 3)
        self.assertIn("1D", seq[0])

    def test_export(self):
        exported = self.tn.export(2)
        data = json.loads(exported)
        self.assertIn(1, data)
        self.assertIn(2, data)

if __name__ == "__main__":
    unittest.main()

