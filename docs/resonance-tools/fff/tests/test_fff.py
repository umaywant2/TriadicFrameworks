```python
import unittest
import json
from fff_core import FFF

class TestFFF(unittest.TestCase):

    def setUp(self):
        self.fff = FFF()

    def test_define(self):
        defs = self.fff.define()
        self.assertIn("FFF", defs)

    def test_forces(self):
        forces = self.fff.simulate_forces(3)
        self.assertEqual(len(forces), 3)

    def test_fluids(self):
        fluids = self.fff.simulate_fluids(2)
        self.assertEqual(len(fluids), 2)

    def test_frequency(self):
        freq = self.fff.simulate_frequency(4)
        self.assertEqual(len(freq), 4)

    def test_export(self):
        self.fff.simulate_forces(1)
        exported = self.fff.export()
        data = json.loads(exported)
        self.assertIn("forces", data)

if __name__ == "__main__":
    unittest.main()

