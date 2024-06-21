num=list(map(int,input().split(" ")))
target=int(input())
i=0
j=i+1
while i<j:
    if j<len(num):
        if num[i]+num[j]==target:
            print(i,j)
            break
        else:
            j=j+1
    else:
        i=i+1
        j=i+1
        
            
            
                
            
        
        
    