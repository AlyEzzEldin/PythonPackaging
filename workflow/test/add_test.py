import unittest
from addition_package import AddOperations, SubtractOperations

class TestAdditionPackage(unittest.TestCase):
    def test_add_two_numbers(self):
        add_operations = AddOperations()
        self.assertEqual(add_operations.add_two_numbers(1, 2), 3)

    def test_increment_by_one(self):
        add_operations = AddOperations()
        self.assertEqual(add_operations.increment_by_one(1), 2)

    def test_subtract_two_numbers(self):
        subtract_operations = SubtractOperations()
        self.assertEqual(subtract_operations.subtract_two_numbers(2, 1), 1)
    def test_decrement_by_one(self):
        subtract_operations = SubtractOperations()
        self.assertEqual(subtract_operations.decrement_by_one(2), 1)

if __name__ == "__main__":
    unittest.main()
