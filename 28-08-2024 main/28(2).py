#2 .Python Program to check if two Strings are Anagram.

s1 = str(input("enter the s1 input:"))
s2 = str(input("enter the s2 input:"))
if (sorted(s1)==sorted(s2)):
    print("The two strings are anagrams")
else:
    print("The two strings are not anagrams")