li=[1,2,3,4,1,2,3,1,2]
li2=[]
i=0
c=0
while(c!=len(li)):
    li1=[]
    for i in range(len(li)):
        if(not li[i]=="@"):
            if li[i] not in li1:
                c=c+1
                li1.append(li[i])
                li[i]="@"
        
    
    li2.append(li1)
        
            
        
print(li2)           
            

            
        

            
            
       
            
        
        
    
    