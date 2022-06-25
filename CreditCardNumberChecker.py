import re

num = input("enter your Credit Card Number:")

print(len(num))

if re.search(r'^[456]+', num)  and  re.search(r'[\d]', num)  and bool(re.search(r'\s', num))is False and bool (re.search(r'[a-z]', num)) is False and (bool(re.search(r'-', num)) is True and len(num) == 19):
    print("The entered Credit Card Number is valid")


else:
    print("The entered Credit Card Number is invalid")

