# Write  a python program to sort dictionary by keys or values ?

# Initial dictionary
dict = {}
dict[5] = "16"
dict[4] = "24"
dict[3] = "40"
dict[2] = "70"
dict[1] = "56"

# Print original dictionary
print("Original dictionary:")
print(dict)

# Sorting dictionary by keys
sorted_by_keys = dict.copy()
sorted_by_keys = {k: sorted_by_keys[k] for k in sorted(sorted_by_keys.keys())}

# Sorting dictionary by values
sorted_by_values = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}

# Output the sorted dictionaries
print("\nDictionary sorted by keys:")
print(sorted_by_keys)

print("\nDictionary sorted by values:")
print(sorted_by_values)
