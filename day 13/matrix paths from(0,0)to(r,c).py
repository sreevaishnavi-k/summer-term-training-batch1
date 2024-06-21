def paths(m,r,c,path,c1):
    if r<0 or c<0 or r>=3 or c>=3:
        return c1
    if r==2 and c==2:
        c1=c1+1
        return c1
    path.append((r,c))
    
    if ((r+1,c)) not in path:
        c1=paths(m,r+1,c,path,c1)
    if ((r-1,c)) not in path:
        c1=paths(m,r-1,c,path,c1)
    if ((r,c+1)) not in path:
        c1=paths(m,r,c+1,path,c1)
    if ((r,c-1)) not in path:
        c1=paths(m,r,c-1,path,c1)
    path.pop()
        
    return c1
    
    


m=[['-','-','-'],['-','-','-'],['-','-','-']]
path=[]
print(paths(m,0,0,path,0))
for i in path:
    print(i)