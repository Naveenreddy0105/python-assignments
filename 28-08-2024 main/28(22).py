# Python program to print all non repeating character in string.

s = input("enter a value:")
for i in s:
    if s.count(i)<2:
        print(i)