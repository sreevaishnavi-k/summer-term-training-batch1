def combi(l,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
        return
    fun([],0)
li=[3,2,5,4,1,6,8]
k=3
combi(li,k)
'''i,c=0,0
j=i+1
k=j+1
for i in range(len(li)-2):
    for j in range(i+1,len(li)-1):
        for k in range(j+1,len(li)):
            if k<len(li):
                print(li[i],li[j],li[k])
                c=c+1
            elif k==len(li):
                j=j+1
                k=j+1
print(c)'''
            
