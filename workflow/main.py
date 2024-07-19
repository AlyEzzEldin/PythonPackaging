import cv2
import numpy as np

# from addition_package import AddOperations,SubtractOperations
from multiplication_package import MulOperations, MulArrayOperations

def main():
    # add_operations = AddOperations()
    # print(add_operations.add_two_numbers(1, 2))
    # print(add_operations.increment_by_one(1))


    # mul_operations = MulOperations()
    # print(mul_operations.multiply_two_numbers(3, 2))
    # print(mul_operations.multiply_by_two(3))


    mul_array_operations = MulArrayOperations([1, 2, 3], [4, 5, 6])
    print(mul_array_operations.multiply())
    print(np.array([4, 10, 18]))
    print(mul_array_operations.multiply_by_scalar(2))

if __name__ == "__main__":
    main()

