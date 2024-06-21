def tree(n,m,r1,c1):
    if r1<0 or c1<0 or r1>=n or c1>=n or m[r1][c1]!=1:
        return 
    if m[r1][c1]==1:
        m[r1][c1]=2
        tree(n,m,r1-1,c1)
        tree(n,m,r1,c1-1)
        tree(n,m,r1+1,c1)
        tree(n,m,r1,c1+1)
n=int(input())
m=[]
for i in range(n):
    c=[]
    for j in range(n):
        s=int(input())
        c.append(s)
    m.append(c)
r1=int(input())
c1=int(input())
co=0
tree(n,m,r1,c1)
for i in range(n):
    for j in range(n):
        if m[i][j]==1:
            co=co+1
print(co)
                
                
        
            
            

        
        
        
        
        
        