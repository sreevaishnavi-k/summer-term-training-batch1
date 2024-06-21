n=int(input())
s=''
for i in range(n):
    ordr=input()
    wrd=input()

    for i in ordr:
        if i in wrd:
            s=s+(i*wrd.count(i))
    print(s)
    s=''
            
            



            
        