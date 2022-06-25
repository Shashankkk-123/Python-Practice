str1= input("Input a string:")
dig=let=0
for i in str1:
    if i.isdigit():
        dig=dig+1
    elif i.isalpha():
        let=let+1
    else:
        pass
print("Letters", let)
print("Digits", dig)