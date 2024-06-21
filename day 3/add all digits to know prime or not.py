def sin(num):
    su,rem=0,0
    rem=num%10
    su=su+rem
    num=num//10
def prime(prime):
    for i in range(2,(su//2)+1):
        if(su%i==0):
            c=c+1
            return "notprime"
             
        if(c==0):
            return prime
       if(c>0):
        prime=prime+1
        num=prime
        sin(num)
num=int(input())
prime=num

        




    

