from addition_package.addition_module import AddOperations
import time

def RunAddition():
    add_operations = AddOperations()
    print(add_operations.add_two_numbers(1, 2))
    time.sleep(5)
    print(add_operations.increment_by_one(1))
