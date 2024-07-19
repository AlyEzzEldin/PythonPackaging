import unittest
import numpy as np
from multiplication_package import MulOperations, MulArrayOperations

class TestMultiplicationPackage(unittest.TestCase):
    def test_multiply_two_numbers(self):
        mul_operations = MulOperations()
        self.assertEqual(mul_operations.multiply_two_numbers(3, 2), 6)

    def test_multiply_by_two(self):
        mul_operations = MulOperations()
        self.assertEqual(mul_operations.multiply_by_two(3), 6)

    def test_multiply(self):
        mul_array_operations = MulArrayOperations([1, 2, 3], [4, 5, 6])
        self.assertEqual(mul_array_operations.multiply().tolist(), [4, 10, 18])

    def test_multiply_by_scalar(self):
        mul_array_operations = MulArrayOperations([1, 2, 3], [4, 5, 6])
        self.assertEqual(mul_array_operations.multiply_by_scalar(2).tolist(), [2, 4, 6])

if __name__ == "__main__":
    unittest.main()