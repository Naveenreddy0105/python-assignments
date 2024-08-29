#1 .Python Program to count occurrence of a given characters in string.
str = ("Naveen Reddy Kosana")
a = input("enter the character to count:")
count = 0
for i in str:
    if i == a:
        count= count+1
print(count)