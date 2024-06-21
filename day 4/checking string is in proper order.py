'''n=int(input())
l=[]
for i in range(n):
    cr=input()
    l.append(cr)
s=input()
le=len(s)
j=0
i=0
c=0
while i<n and j<len(s):
    if s[j] in l[i]:
        c=c+1
        j=j+1
        i=i+1
    else:
        print("false")
        break
    if i==n:
        i=0
if c==le:
    print("true")'''
n=int(input())
l=[]
for i in range(n):
    l.append(list(input()))
s=input()
f=0
for i in range(len(s)):
    if(s[i] not in m[i%n]):
        print("no")
        f=1
        break
    else:
        m[i].remove(s[i])
if(f==0):
    print("yes ")
f=0