n=12
k=2
i=n//2
c=1
if k==1:
    print(n)
else:
    while i>0:
        if n%i==0:
            c=c+1
            if c==k:
                print(i)
                break
        i=i-1