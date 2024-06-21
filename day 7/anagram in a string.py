s='school'
inp=int(input())
li=[]
s2=''
for i in range(inp):
    n=input()
    li.append(n)
li1=[]
su=''
pre=''
j=0
li3=[]
for i in li:
    li1.append(int(i[-1]))
for i in li1:
    su=s[i:]
    pre=s[:i]
    for j in li:
        if j[0]=='l':
            li3.append(su+pre)
            break
        elif j[0]=='r':
            li3.append(pre+su)
            break
print(li3)
s1=''
for i in li3:
    s1=s1+i[0]
print(s1)
ss=[]
for i in range(len(s)-inp+1):
    ss.append(s[i:i+inp])
print(ss)
s2=""
s1=sorted(s1)
s2="".join(s1)
print(s2)    
for i in ss:
    if s2==i:
        print("True")
        break
else:
    print("False")
        

            
            
        
    
        
        
    

