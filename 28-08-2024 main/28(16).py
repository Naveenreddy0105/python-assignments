# Python program to count the Occurrence Of Vowels & Consonants in a String.

str = str(input("enter a value: "))
vowels = "aeiou"
vowels1=0
consonants_count=0
count = len(str)
for i in str:
    if i.isalpha():

      if i in vowels:
        vowels1 +=1
      else:
        consonants_count +=1
print(vowels1)
print(consonants_count)