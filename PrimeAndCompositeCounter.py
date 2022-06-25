x = True
list1 =[]
composite = 0

while x:
    num = int(input("Enter your numbers:"))
    if num < 0:
        x = False
    else:
        list1.append(num)
print("List of numbers entered:",list1)

for x in list1:
    for i in range(2,x):
        if x % i == 0:
            composite+= 1
            break
print("Prime count from the given numbers= ", (len(list1)-composite))
print("Composite count from the given numbers = ",composite)        
