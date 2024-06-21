arr=[12,3,14,56,77,13]
#arr=[2,3,4,56,77,3]
num=13
diff=2
c=0
for i in range(len(arr)):
    if abs(arr[i]-num)<=diff:
        c=c+1
if c==0:
    print("-1")
else:
    print(c)
