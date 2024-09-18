'''Write a Python program to find the minimum and maximum elements in a tuple of integers.
 python # Example Tuple: (10, 20, 5, 40, 25) # Expected Output: Min: 5, Max: 40'''

def find_min(numbers):
    return min(numbers)
def find_max(numbers):
    return max (numbers)
numbers = (10, 20, 5, 40, 25)
print("min:",find_min(numbers))
print("max:",find_max(numbers))