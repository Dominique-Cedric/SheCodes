import unittest
from challenges import CodeWarrior


class TestCase(unittest.TestCase):
    def test_code_warrior(self):
        warrior_1 = CodeWarrior("Oliver")

        self.assertEqual(warrior_1.current_health, 100, msg=f"\nYour warrior was created with the wrong amount of health!\nExpected value: {100}\nActual value:{warrior_1.current_health}")
        self.assertEqual(warrior_1.character_name, "Oliver", msg=f"\nYour warrior was created with the wrong name!\nInput value: 'Oliver'\nself.character_name value:{warrior_1.character_name}")
        self.assertListEqual(list(), warrior_1.inventory_list, msg=f"\nYour warrior's starting inventory is incorrect!\nExpected value: {[]}\nAssigned value: {warrior_1.inventory_list}")

        warrior_1.update_health(10)
        self.assertEqual(warrior_1.current_health, 100, msg=f"\nIncreasing the warrior's health above 100 should have no effect, but adding ten health to your full-health warrior changed the value!")

        warrior_1.update_health(-10)
        self.assertEqual(warrior_1.current_health, 90, msg=f"\nDecreasing the warrior's health failed to occur correctly.")

        warrior_1.update_health(-100)
        self.assertEqual(warrior_1.current_health, 0, msg=f"\nYour warrior's health should not ever fall below 0, but subtracting 110 took your warrior to -10 health!")

        warrior_1.pick_up_item("apple")
        self.assertListEqual(["apple",], warrior_1.inventory_list, msg=f"\nPicking up an apple failed to add that apple to your warrior's inventory!")

        warrior_1.pick_up_item("apple")
        warrior_1.pick_up_item("apple")
        warrior_1.pick_up_item("apple")
        warrior_1.pick_up_item("apple")
        warrior_1.pick_up_item("apple")
        self.assertListEqual(["apple","apple","apple","apple","apple"], warrior_1.inventory_list, msg=f"\nYour warrior should not be able to fit more than five items in their inventory, but they were able to pick up six!")

runner = unittest.TextTestRunner(verbosity=2)

runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(TestCase))))
