d={5:[7,3],7:[5,4],4:[7,6],8:[3,9,2],3:[5,8],2:[1,8],1:[2],6:[4],9:[8]}
q=[5]
v=[]
while (q):
    for i in d[q[0]]:
        if i not in q and i not in v:
            q.append(i)
    v.append(q.pop(0))
    print(v[-1],end=" ")
   