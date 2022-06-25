
x = input("Enter the string:")

dict1 = {}

for i in x:
 if i in dict1:
    dict1[i] += 1
 else:
           dict1[i] = 1

print("Count of all the Characters in the given string is :\n "+ str(dict1))
