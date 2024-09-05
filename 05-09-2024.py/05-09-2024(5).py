# Write a python program to combine two dictionaries by adding values of common keys ?

dict1 ={'a':12,'b':23,'c':28}
dict2 ={'a':24,'b':56,'c':36}
for i in dict2:
    if i in dict1:
        dict2[i]=dict2[i]+dict1[i]

print(dict2)
