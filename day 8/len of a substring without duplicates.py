s=input()
m=0
st=''
d={}
c,i=0,0
while(i<len(s)):
    while(i<len(s)):
        if s[i] not in st:
            st=st+s[i]
            d[st[i]]=i
        else:
            if len(st)>m:
                m=len(st)
                st=''
                break
    i=d[s[i]]+1
print(m)

    
    