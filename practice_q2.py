import re
st=input("Enter words deperated by comma: ").split(",")
res=[]

for s in st:
    if re.findall(r"o\Z", s):
        s=re.sub(r"o\Z","oes", s)
        
    elif re.findall(r"(a|e|i|o|u)y\Z", s):
        s=re.sub(r"y\Z","ys", s)
        
    elif re.findall(r"y\Z",s):
        s=re.sub(r"y\Z","ies", s)
    else:
        s= s +"s"
    res.append(s)

print(",".join(res))