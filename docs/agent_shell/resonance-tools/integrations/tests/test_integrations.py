```python
import unittest
from integrate_core import Integrations

class TestIntegrations(unittest.TestCase):

    def setUp(self):
        self.integ = Integrations()

    def test_define(self):
        defs = self.integ.define()
        self.assertIn("Integrations", defs)

    def test_demo_pipeline(self):
        demo = self.integ.demo_pipeline()
        self.assertIn("Resonant-Time", demo)
        self.assertIn("TFT (CPU)", demo)

    def test_dashboard(self):
        dash = self.integ.dashboard("cpu")
        self.assertIn("Domain", dash)
        self.assertIn("TFT", dash)
        self.assertIn("FFF", dash)

if __name__ == "__main__":
    unittest.main()

