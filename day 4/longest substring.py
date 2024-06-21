st=input()
i,m=0,0
c=1
for i in range(len(st)-1):
    if ord(st[i])==ord(st[i+1])-1:
        c=c+1
        i=i+1
    else:
        if(c>m):
            m=c
        c=1
if(c>m):
    m=c
print(m)
        
    
        
        
    
        
        


        
        
        
        
        
       
        
    