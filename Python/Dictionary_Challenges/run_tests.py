import unittest, csv
from collections import Counter
from challenges import grocery_calculator, word_counter, create_colour_dict


class TestCase(unittest.TestCase):
    def test_grocery_calculator(self):
        test_cases = [
            {
                "Baby Spinach 100g bag": 2.78,
                "Hot Chocolate 300g": 3.70,
                "Crackers 250g packet": 2.10,
                "Coffee 500g": 9.00,
                "Carrots 1kg bag": 0.56,
                "Oranges 1kg bag": 3.08
            },
            {
                "Baby Spinach 100g bag": 2.78,
                "Hot Chocolate 300g": 3.70,
                "Crackers 250g packet": 2.10,
                "Coffee 500g": 9.00,
                "Carrots 1kg bag": 0.56
            },
            {
                "Baby Spinach 100g bag": 2.78,
                "Hot Chocolate 300g": 3.70,
                "Crackers 250g packet": 2.10,
                "Coffee 500g": 9.00
            },
            {
                "Baby Spinach 100g bag": 2.78,
                "Hot Chocolate 300g": 3.70,
                "Crackers 250g packet": 2.10
            },
            {
                "Baby Spinach 100g bag": 2.78,
                "Hot Chocolate 300g": 3.70
            },
            {}
        ]

        for case in test_cases:
            expected_result = sum(case.values())
            actual_result = grocery_calculator(case)

            if type(actual_result) != float and actual_result != 0:
                self.fail(msg=f"\nYour function was supposed to return a float, but instead it returned {type(actual_result)}!")

            self.assertEqual(
                expected_result,
                actual_result,
                msg=f"\nInput: {case}\nExpected result: {expected_result}\nActual result: {actual_result}"
            )

    def test_word_counter(self):
        test_cases = [
            ["apple", "banana", "apple", "cherry", "apple", "banana"],
            ["apple", "apple", "apple", "apple", "apple", "apple"],
            ["apple", "apple", "apple", "apple", "dragonfruit"],
            []
        ]

        for case in test_cases:
            expected_result = dict(Counter(case))
            actual_result = word_counter(case)

            if type(actual_result) != dict:
                self.fail(msg=f"\nYour function was supposed to return a dict, but instead it returned {type(actual_result)}!")

            self.assertEqual(
                expected_result,
                actual_result,
                msg=f"\nInput: {case}\nExpected result: {expected_result}\nActual result: {actual_result}"
            )

    def test_create_colour_dict(self):
        for case in [
            "./colours_3_very_simple.csv",
            "./colours_20_simple.csv",
            "./colours_865.csv"
        ]:
            actual_result = create_colour_dict(case)

            if type(actual_result) != dict:
                self.fail(msg=f"\nYour function was supposed to return a dict, but instead it returned {type(actual_result)}!")

            with open(case, "r") as file:
                reader = csv.DictReader(file)
                intended_result = {row["English"]: row["HEX"] for row in reader}

                self.assertDictEqual(
                    actual_result, 
                    intended_result,
                    msg=f"\nInput: {case}\nExpected result: {intended_result}\nActual result: {actual_result}"
                )

runner = unittest.TextTestRunner(verbosity=2)

runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(TestCase))))
