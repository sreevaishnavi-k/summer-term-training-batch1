s="(([{}]))"
li=[]
for i in range(len(s)):
    if s[i] =='('or s[i]=='{'or s[i]=='[':
        li.append(s[i])
    elif len(li)!=0:
        if (s[i]==')'and li[-1]=='(')or (s[i]=='}'and li[-1]=='{')or (s[i]==']' and li[-1]=='['):
                li.pop()
        else:
            print(i)
            break
if len(li)==0:
    print(-1)
 
            