def rev(n,re):
    if(n==0):
        return re
    s=n
    rem=n%10
    re=re*10+rem
    return rev(n//10,re)
n=int(input())
x=rev(n,0)
if(x==n):
    print("palindrome")
else:
    print("no")
    
