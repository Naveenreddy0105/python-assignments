# Python program to convert lowercase vowel to uppercase in string.

s= ("Python has a large standard library that provides a rich set of modules and functions")
vowels = "aeiou"
for char in s:
    if char in vowels:
        upper_char = char.upper()
        s = s.replace(char, upper_char)
print(s)

