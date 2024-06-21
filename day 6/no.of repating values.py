li=list(map(int,input().split()))
l=len(li)
c=1
w=li[0]
for i in range(1,len(li)):
    if li[i]==w:
        c=c+1
    else:
        c=c-1
        if c==0:
            c=c+1
            w=li[i]
print(w)
    
        
        
        
    
        

