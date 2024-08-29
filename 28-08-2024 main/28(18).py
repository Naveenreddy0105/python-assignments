# Python program to Replace First Occurrence Of Vowel With ‘-‘ in String.

str = str(input("enter a value:"))
vowels = "aeiouAEIOU"
for ch in range(len(str)):
    if str [ch] in vowels :
        str=str[:ch]+'-' +str[ch+1:]
        break
print(str)