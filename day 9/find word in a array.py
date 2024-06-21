'''def string(m,s,i,j,k,t):
    if k==len(s):
        return 1
    if i<0 or j<0 or i>=n or j>=n or m[i][j]!=s[k]:
        return
    if m[i][j]==s[k]:
        m[i][j]=0
    t=string(m,s,i+1,j,k+1)
    t=string(m,s,i,j-1,k+1)
    t=string(m,s,i+1,j,k+1)
    t=string(m,s,i,j+1,k+1)
    return t
s=input()
n=int(input())
m=[]
for i in range(n):
    c=[]
    for j in range(n):
        x=input()
        c.append(x)
    m.append(c)
for i in range(n):
    for j in range(n):
        if m[i][j]==s[0]:
            co=string(m,s,i,j,1,0)
            if co==1:
                print("yes")
                break
if co==0:
    print("no")'''

            
