

def Remove_duplicate(x):
 list2 = []
 for n in x:
  if n not in list2:
    list2.append(n)
 return list2
 
x = input("Enter the list:").split()

print("The final list after removal of duplicates is:",Remove_duplicate(x))
