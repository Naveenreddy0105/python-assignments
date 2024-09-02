# Write a python program to find most frequent element in tuple ?


from collections import Counter
my_tuple = (1,2,4,6,3,2,6,4,1,3,4,6,4,1,4,6,8,5,2,1)
counter = 0
counter = counter(my_tuple)
most_common_element,count = counter.most_common(1)[0]
print("Most frequent element:", most_common_element)
print("Frequency:", count)

