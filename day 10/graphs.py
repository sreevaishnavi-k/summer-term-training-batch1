def graph(d,li,a):
    li.append(a)
    if a==2:
        print(li)
    for i in d[a]:
        if i not in li:
            graph(d,li,i)
        li.pop()
    
    
    
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
li=[]
print(graph(d,li,5))
