#Python program to check a String is palindrome or not.

x =(input("enter a word:"))
if x==x[::-1]:
    print("It is palindrome")
else:
    print('It is not palidrone')