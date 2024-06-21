arr=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
mo=[5,6,5,9,11,2]
li=mo[:]
for i in range(1,len(arr)):
    for j in range(0,i):
        if arr[j][1]<=arr[i][0]:
            if li[j]+mo[i]>li[i]:
                li[i]=li[j]+mo[i]
print(max(li))
          
        