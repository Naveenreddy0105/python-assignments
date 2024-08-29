# Python program to calculate sum of integers in string.

s = input("enter a value:")
t = 0
for i in s:
    if i in "0123456789":
        t+=int(i)
print(t)
