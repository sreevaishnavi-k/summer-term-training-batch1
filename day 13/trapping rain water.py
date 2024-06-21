li=[2,5,2,3,6,7,1,0,5,7]
li1=[]
li2=[0]*len(li)
m=0
li1.append(li[0])
for i in range(len(li)-1):
    if li1[i]>li[i+1]:
        li1.append(max(li1))
    else:
        li1.append(li[i+1])
for i in range(len(li)-1,-1,-1):
    if li[i]>m:
        m=li[i]
    li2[i]=m
s=0
for i in range(len(li)):
    s=s+abs(min(li1[i],li2[i])-li[i])
print(s)    
    
    
    
        


        
    