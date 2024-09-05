#  Write a python program to check weather the given value is present in the dictionary or not ?

d ={'name':"naveen",'id':10234,'salary':35000}
i= str(input("enter a value: "))
if i in d.values():
    print("value exist",i)
else:
    print("value not exists")
print("")