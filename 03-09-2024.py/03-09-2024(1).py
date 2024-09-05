'''1.Write a program which will find all such numbers which are divisible by 7 but are not a 
multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be 
printed in a comma-separated sequence on a single line'''

'''result =[]
#loooping the range of the elements.
for num in range(2000,3200):
#  divisible by 7 and not divisible by 5.
    if num %7 == 0 and num%5 != 0:
        result.append(str(num))
#print(result)'''


result = []
for num in range (2000,3200):
    if num %7 == 0 and num %5 != 0 :
        result.append (str(num))
print(result)