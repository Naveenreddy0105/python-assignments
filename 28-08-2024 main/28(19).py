#Python program to count alphabets, digits and special characters.

str= input("Please Enter your Own String : ")
alphabets = digits = special = 0

for i in range(len(str)):
    if(str[i].isalpha()):
        alphabets = alphabets + 1
    elif(str[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1
        
print("Total Number of Alphabets in this Str:  ",alphabets)
print("Total Number of Digits in this Str :  ",digits)
print("Total Number of Special Characters in this Str :  ",special)