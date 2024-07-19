from multiplication_package.multiplication_module import MulOperations, MulArrayOperations
import time

def RunMultiplication():
    mul_array_operations = MulArrayOperations([1, 2, 3], [4, 5, 6])
    print(mul_array_operations.multiply())
    time.sleep(5)
    print(mul_array_operations.multiply_by_scalar(2))
