```python
import unittest
import json
from tfe_core import TriadicFrameworks

class TestTFE(unittest.TestCase):

    def setUp(self):
        self.tfe = TriadicFrameworks()

    def test_define(self):
        defs = self.tfe.define()
        self.assertIn("TFE", defs)

    def test_apply_known_domain(self):
        physics = self.tfe.apply("physics")
        self.assertIsInstance(physics, list)

    def test_apply_unknown_domain(self):
        result = self.tfe.apply("unknown")
        self.assertIsInstance(result, str)

    def test_list_domains(self):
        domains = self.tfe.list_domains()
        self.assertIn("physics", domains)

    def test_export_known_domain(self):
        exported = self.tfe.export("computing")
        data = json.loads(exported)
        self.assertIn("computing", data)

    def test_export_unknown_domain(self):
        exported = self.tfe.export("unknown")
        data = json.loads(exported)
        self.assertIn("error", data)

if __name__ == "__main__":
    unittest.main()
