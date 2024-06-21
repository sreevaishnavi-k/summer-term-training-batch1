def graph(d,li,a,c):
    li.append(a)
    if a==2:
        print(li,c)
    for i,j in d[a]:
        if i not in li:
            graph(d,li,i,c+j)
    li.pop()
d={5:[(7,1),(3,1)],7:[(5,1),(4,2),(3,7)],4:[(7,2),(8,2),(2,3)],8:[(3,1),(4,2),(2,1)],3:[(5,1),(7,7),(8,1)],2:[(4,3),(8,1)]}
li=[]
print(graph(d,li,5,0))

