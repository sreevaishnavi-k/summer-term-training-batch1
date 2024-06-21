def rec(li,li1,li2,l,i,j):
    if i==l:
        return li
    if li[i]%2==0:
        if li[j]%2!=0:
            s=li[i]+li[j]
            li2.append(s)
        else:
            return rec(li,li1,li2,l,i,j)
    

li=[6,3,2,9,4,7]
li1=[8,7,5,3,6,9]
li2=[]
print(rec(li,li1,li2,len(li),0,0))
