s=input("enter string:")
counter=0

if(s.count("(")==s.count(")")):
    for x in s:
        if(x=="("):
            counter+=1
        elif(x==")"):
            counter-=1
        if counter<0:
            flag=0
            break
        else:
            flag=1

    if flag==0:
        print("False")
    elif flag==1:
        print("True")
else:
    print("False")