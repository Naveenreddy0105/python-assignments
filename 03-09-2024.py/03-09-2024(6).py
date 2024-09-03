'''Write a program that accepts a sentence and calculate the number of upper case letters 
and lower case letters. Suppose the following input is supplied to the program: Hello 
world! Then, the output should be: UPPER CASE 1 LOWER CASE 9'''

input =("Hello world!")
isupper= islower = 0

for i in range(len(input)):
    if(input[i].isupper()):
        isupper = isupper + 1
    elif(input[i].islower()):
        islower = islower + 1
        
print("Total Number of upper :  ",isupper)
print("Total Number of lower :  ",islower)
