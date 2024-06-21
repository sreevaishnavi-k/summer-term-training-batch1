def graph(d,li,a,c,t,mi,e):
    li.append(a)
    if a==e:
       if c<mi:
           mi=c
           t=li.copy()
       li.pop()
       return t,mi
    for i,j in d[a]:
        if i not in li:
            (t,mi)=graph(d,li,i,c+j,t,mi,e)
    li.pop()
    return (t,mi)
d={5:[(7,1),(3,1)],7:[(5,1),(4,2),(3,7)],4:[(7,2),(8,2),(2,3)],8:[(3,1),(4,2),(2,1)],3:[(5,1),(7,7),(8,1)],2:[(4,3),(8,1)]}
li=[]
t=[]
mi=100000 
print(graph(d,li,5,0,t,mi,2))