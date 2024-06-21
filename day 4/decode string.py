st=input()
n=int(input())
t=n%26
d=''
for i in st:
    if((ord(i)-t)>=97):
        d=d+chr(ord(i)-t)
    else:
        d=d+chr(ord(i)-t+26)
print(d)
            

    
   