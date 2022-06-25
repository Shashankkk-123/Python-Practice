def checkAmstrong(n):
    s=0
    rem=0
    a=n
    while n>0:
        rem = n%10
        s += rem**3
        n = n//10
    if s == a:
        print("Given Number is Amstrong")
    else:
        print("Given Number is not an Amstrong")
x = int(input("Enter a Number:"))
if x <= 0:
    print("Please enter a positive integer greater than zero.")
else:
    checkAmstrong(x)
    
