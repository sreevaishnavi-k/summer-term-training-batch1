l=list(map(int,input().split(" ")))
l1=list(map(int,input().split(" ")))
l2=[]
i=0
j=0
'''l2=l+l1
l2.sort()
print(l2)'''
while(i<len(l) and j<len(l1)):
    if l[i]<l1[j]:
        l2.append(l[i])
        i=i+1
    else:
        l2.append(l1[j])
        j=j+1
while(j<len(l1)):
    l2.append(l1[j])
    j=j+1
while(i<len(l)):
    l2.append(l[i])
    i=i+1    
print(l2)
