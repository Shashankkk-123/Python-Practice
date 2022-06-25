#Asking for inputs of dimensions and unit and storing them in variables
l=input("Enter the length: ")
b=input("Enter the width: ")
h=input("Enter the height: ")
unit=input("Enter the unit: ")


#Putting condition for checking if the input is a string
if (l.lstrip("-").isnumeric() and b.lstrip("-").isnumeric() and h.lstrip("-").isnumeric()) is False:
    print ("Try again using only Positive Nummeric Values instead of strings") #Asks user to input numbers instead
else: #If all inputs are numbers, program proceeds


#Conversion of input values to float
    l=float(l)
    b=float(b)
    h=float(h)


    if l<=0 or b<=0 or h<=0: #Putting condition for checking negative inputs and zero input
        print("Please Try again using all Positive values instead of negative ones")
    else: 
        v=l*b*h #Calculation of volume
        d=((l**2)+(b**2)+(h**2))**(0.5) #Calcullation of length of diagonal
        print("The volume is",v,"cubic",unit) #Printing volume
        print("Diagonal",d,unit) #Printing length of diagonal
