def even(a,i,s):
    if i==len(a):
        return s
    if a[i]%2==0:
        s=s+a[i]
    return even(a,i+1,s)
def odd(b,i,su):
    if i==len(b):
        return su
    if b[i]%2!=0:
        su=su+b[i]
    return odd(b,i+1,su)

a=[3,8,5,4,3]
b=[5,0,9,3,2]
print('(',even(a,0,0),',',odd(b,0,0),')')

