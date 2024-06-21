s=input("enter a password")
caps=[]
smalls=[]
nums=[]
special=[]
char=-1

for i in s:
    if i.isupper():
        caps.append(i)
    elif i.islower():
        smalls.append(i)
    elif i.isdigit():
        nums.append(i)
    else:
        special.append(i)

if len(s)>=8 and len(caps)!=0 and len(smalls)!=0 and len(nums)!=0 and len(special)!=0:
    print(char)
elif len(s)>8:
    char+=1
    if len(caps)==0:
        char+=1
    if len(smalls)==0:
        char+=1    
    if len(nums)==0:
        char+=1
    if len(special)==0:
        char+=1
    print(char) 
elif len(s)<8:
    char+=1
    if len(caps)==0:
        char+=1
    if len(smalls)==0:
        char+=1    
    if len(nums)==0:
        char+=1
    if len(special)==0:
        char+=1
    if char+len(s)<8:
        char=char+(8-len(s)-char)
    print(char)    
print(caps, smalls,nums,special)