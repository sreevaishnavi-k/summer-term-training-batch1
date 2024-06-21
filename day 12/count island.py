def island(n,m,r1,c1,c2):
    if r1<0 or c1<0 or r1>=n or c1>=n or m[r1][c1]!=1:
        return c2 
    if m[r1][c1]==1:
        m[r1][c1]=2
        c2=c2+1
        c2=island(n,m,r1-1,c1,c2)
        c2=island(n,m,r1,c1-1,c2)
        c2=island(n,m,r1+1,c1,c2)
        c2=island(n,m,r1,c1+1,c2)
    return c2
n=int(input())
m=[]
for i in range(n):
    c=[]
    for j in range(n):
        s=int(input())
        c.append(s)
    m.append(c)
co=0
ma=0
for i in range(n):
    for j in range(n):
        if m[i][j]==1:
            k=island(n,m,i,j,0)
            co=co+1
            if ma<k:
                ma=k
print(co)
print(ma)
          