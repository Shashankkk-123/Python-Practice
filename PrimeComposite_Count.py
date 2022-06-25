k = 0
i = 1
# counters for prime and composite numbers
prime = 0
composite = 0
while i != 0:
    k = 0
    x = int(input('Enter a number'))
    if x == -1:
        i = 0
        break

    # calculating number of factors
    for j in range(2, x):

        if x % j == 0:
            k = 1
            break

    if k == 0:

        prime += 1

    else:
        composite += 1

print("Prime numbers are ", prime)
print("Composite numbers are ", composite)
