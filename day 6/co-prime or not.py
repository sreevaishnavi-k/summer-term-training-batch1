n=int(input())
m=int(input())
for i in range(2,(min(n,m)//2)+1):
    if(n%i==0) and (m%i==0):
        print("not co-prime")
        break
else:
    print("co-prime")
