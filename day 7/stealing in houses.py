def rec(li):
    if len(li)==0:
        return 0
    if len(li)==1:
        return li[0]
    if len(li)==2:
        return max(li)
    r1=li[0]+rec(li[2:])
    r2=li[1]+rec(li[3:])
    return max(r1,r2)
    
li=[13,9,4,10,5,7] 
print(rec(li))


    