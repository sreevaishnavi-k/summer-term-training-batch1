class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def __init__(self):
        self.head=None

    def display(self):
       
        t=self.head
        while(t!=None):
            
            print(t.data,end="->")
            t=t.nxt
        
    def addback(self,x):
        t=self.head
        while(t.nxt!=None):
            t=t.nxt
        t.nxt=node(x)
    def addfront(self,x):
        t=node(x)
        t.nxt=self.head
        self.head=t
        
    def addeven(self):
        t=self.head
        s1=0
        while(t!=None):
            if(t.data%2==0):
                s1=s1+t.data
                t=t.nxt
            else:
                t=t.nxt
        print(s1)
    def search(self,x):
        t=self.head
        while(t.nxt!=None):
            if t.data==x:
                print("found")
                break
            else:
                t=t.nxt
        else:
            print("not found")
    def mid(self):
        f=self.head
        s=self.head
        while(f!=None and f.nxt!=None):
            s=s.nxt
            f=f.nxt.nxt
        return(s.data)
       
    def evenodd(self):
        #t=self.head
        #c=1
        #while(t!=None):
         #   c=c+1
          #  t=t.nxt
        #if c%2==0:
         #   print("even len")
        #else:
         #   print("odd len")
        f=self.head
        s=self.head
        while(f!=None and f.nxt!=None):
            s=s.nxt
            f=f.nxt.nxt
        if (f==None):
            print("odd")
        else:
            print("even")
    def longestSS(self):
        t=self.head
        c=1
        n=0
        m=0
        while(t.nxt!=None):
            if t.data+1==t.nxt.data:
                c=c+1
                t=t.nxt
                print(t.data)
            else:
                if c>m:
                    m=c
                t=t.nxt
                c=1
        if c>m:
            m=c
        print(m)
    def allpairs(self):
        t=self.head
        k=t.nxt
        while(t.nxt!=None):
            if k is not None:
                print(t.data,k.data)
                k=k.nxt
            else:
                t=t.nxt
                k=t.nxt
    def bubblesort(self):
        t1=self.head
        f=0
        p=None
        while(t1.nxt!=p):
            t2=self.head
            while(t2.nxt!=p):
                if t2.data>t2.nxt.data:
                    f=1
                    t2.data,t2.nxt.data=t2.nxt.data,t2.data
                t2=t2.nxt
            if f==0:
                break
            p=t2
            t1=t1.nxt
    def reverse()
l1=sll()
l2=sll()
l1.head=node(10)
l1.addback(20)
l1.addback(21)
l1.addback(22)
l1.addback(11)
l1.addback(12)
l2.head=node(100)
l2.addback(200)
l1.addfront(5)
l1.display()
print()
l2.display()
print()
l1.addeven()
l2.addeven()
l1.search(10)
print(l1.mid())
print(l2.mid())
l1.evenodd()
l2.evenodd()
l1.longestSS()
"l1.allpairs()"
l1.bubblesort()
l1.display()