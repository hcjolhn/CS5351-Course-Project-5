import unittest

from task.validate_api import validate_api


class ValidateApi(unittest.TestCase):
    def test_capture_network(self):
        network_traffic = validate_api.capture_network('http://localhost:8000/forms')
        self.assertTrue(network_traffic is not None)
