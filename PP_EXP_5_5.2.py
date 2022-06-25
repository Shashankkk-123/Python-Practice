print("Enter the size of list:")
li = []
n = int(input())

print("Enter numbers:")
for i in range(n):
    li.append(int(input()))

odd = list(filter(lambda x: x%2 , li))

even = list(filter(lambda x: x%2==0 , li))

print(f"odd numbers are {odd},even numbers are {even}")
