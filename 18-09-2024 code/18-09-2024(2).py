'''Write a Python program to sort a tuple of tuples based on the second element of each tuple. 
python # Example Tuple: ((1, 2), (3, 1), (5, 0)) # Expected Output: ((5, 0), (3, 1), (1, 2))'''

t = eval(input("enter a value:"))
tuple1 =sorted(t,key=lambda x:x[1])
print(tuple(tuple1))    