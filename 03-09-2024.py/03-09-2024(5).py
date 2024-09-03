'''5.Write a program that accepts a sentence and calculate the number of letters and digits. 
Suppose the following input is supplied to the program: hello world! 123 Then, the output 
should be: LETTERS 10 DIGITS 3'''

input = ("hello world! 123")
alphabets = digits = 0

for i in range(len(input)):
    if(input[i].isalpha()):
        alphabets = alphabets + 1
    elif(input[i].isdigit()):
        digits = digits + 1
        
print("Total Number of Alphabets :  ",alphabets)
print("Total Number of Digits :  ",digits)
