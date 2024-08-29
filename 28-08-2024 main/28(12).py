# Python program to remove repeated character from string.

str = input("enter a value: ")
a =""
for char in str :
    if char not in a :
        a = a+char
print(a)