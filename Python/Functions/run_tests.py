import unittest
from unittest.mock import patch, Mock
from functions_challenges import get_float, miles_to_km, relay_distance

input_mock = Mock()
input_mock.side_effect = ["9", "9.0", "0.0"]


class TestCase(unittest.TestCase):
    @patch('builtins.input', input_mock)
    def test_get_float(self):
        
        inputs = {each_input: get_float("giff numba") for each_input in ["9", "9.0", "0.0"]}
        
        for key, val in inputs.items():
            self.assertEqual(type(val), float, msg=f"The input {key} resulted in returning a value of type {type(val)} instead of a float!")

    def test_miles_to_km(self):

        inputs = {x: 1.60934*x for x in [1, 5, 9000]}

        for key, val in inputs.items():
            self.assertEqual(miles_to_km(key), val, msg=f"The argument {key} resulted in returning a value of {miles_to_km(key)}! The correct answer was {val}!")

    def test_relay_distance(self):

        inputs = {2: (1, 2), 12: (3, 4), 0.25: (0.5, 0.5)}

        for key, val in inputs.items():
            self.assertEqual(key, relay_distance(*val), msg=f"The arguments {val} resulted in returning a value of {relay_distance(*val)}! The correct answer was {key}!")


runner = unittest.TextTestRunner(verbosity=2)

runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(TestCase))))
