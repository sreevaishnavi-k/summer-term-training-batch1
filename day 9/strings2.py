s="hello:5438,car:214,book:8799,apple:2187"
li=s.split(",")
s=""
for i in li:
    li1=i.split(":")
    l=len((li1[0]))
    if str(l) in li1[1]:
        s=s+li1[0][-1]
    else:
        for i in range(l-1,0,-1):
            if str(i) in li1[1]:
                s=s+li1[0][i-1]
                break
        else:
            s=s+"x"
print(s)
            
            
            
    
        
        
    
    