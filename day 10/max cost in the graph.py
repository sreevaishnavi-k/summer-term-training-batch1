def graph(d,li,a,c,t,ma):
    li.append(a)
    if a==2:
       if c>=ma:
           t=li[:]
           li.pop()
           return (t,c)
       li.pop()
       return (t,ma)
    for i,j in d[a]:
        if i not in li:
            (t,ma)=graph(d,li,i,c+j,t,ma)
    li.pop()
    return (t,ma)
d={5:[(7,1),(3,8)],7:[(5,1),(4,2),(3,7)],4:[(7,2),(8,6),(2,3)],8:[(3,5),(4,6),(2,4)],3:[(5,8),(7,7),(8,5)],2:[(4,3),(8,4)]}
li=[]
t=[]
ma=0
print(graph(d,li,5,0,t,ma))