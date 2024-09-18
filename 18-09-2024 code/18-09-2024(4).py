'''Given a tuple containing nested tuples, write a Python program to flatten it into a single tuple. 
python # Example Tuple: (1, (2, 3), (4, 5, 6)) # Expected Output: (1, 2, 3, 4, 5, 6)'''


def flatten_tuple(t):
    result =[]
    for item in t:
        if isinstance(item,tuple):
            result.extend(flatten_tuple(item))
        else:
            result.append(item)
    return (flatten_tuple)
print(flatten_tuple)
