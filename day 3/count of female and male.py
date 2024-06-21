'''
st=input()
c,c2=0,0
for i in st:
    if i=='f':
        c=c+1
    if i=='m':
        c2=c2+1
if c==c2:
    print(0)
elif c>c2:
    print("f")
elif c2>c:
    print("m")'''
str="mmffmmfff"
c=0
le=len(str)
for i in str:
    if i=="m":
        c=c+1
    elif i=="f":
        c=c-1
if c==0:
    print(0)
elif c>0:
    print("m")
else:
    print("f")