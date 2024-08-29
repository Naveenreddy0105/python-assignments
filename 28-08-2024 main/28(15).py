# Python program to delete vowels in a given string.


str =str(input("enter a value:"))
       
vowels = "aeiouAEIOU"
a = ""
for char in str:
    if char not in vowels:
        a += char
print(a)
