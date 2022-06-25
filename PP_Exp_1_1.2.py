a="Python programming" #Assigning variable a the given string

print ("b)",a[15]) #getting the letter 'i' from the string through its index

print ("c)",len(a)) #Printing the string length

print ("d)",a[0:6]) #Printing just the string 'Python' from the given string

print ("e)",a[7:14]) #Printing just the string 'program' from the given string

print ("f)",a[2:4]+a[15:18]) #Printing just the string 'thing' from the given string


a=a.upper() #Changing the given string to all Uppercases
print ("g)",a)

b=" is interesting" #Joining two strings together
print("h)",a+b)

print("i)")

c=a.title() #Changing a string to Title font
print("using title()- ",c)

d=c.swapcase() #Swapping the uppercase and lowercase letters of a string
print ("using swapcase()- ",d)

e=c.startswith("Python") #Checking if a string starts with a particular string
print("using startswith()- ",e)

f=c.rindex("n") # Show the last occurrance of the character n in a string
print("using startswith()- ",f)




