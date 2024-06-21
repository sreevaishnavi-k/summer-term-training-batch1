n=int(input())
li=list(map(int,input().split()))
"""for i in range(n):
    if i not in li:
        print(i)"""
s=sum(li)
n=(n*(n+1))//2
print(n-s)
