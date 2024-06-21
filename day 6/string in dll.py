class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.tail.nxt=t
            t.prev=self.tail
            self.tail=t
    def addbeg(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            new=node(x)
            new.nxt=self.head
            self.head.prev=new
            new.prev=None
            self.head=new
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="<->")
            t=t.nxt
        print()
    def paran(self):
        t=self.head
        li=[]
        c=1
        while(t!=None):
            if t.data=='('or t.data=='{'or t.data=='[':
                li.append(t.data)
                c=c+1
            elif len(li)!=0:
                if (t.data==')'and li[-1]=='(')or (t.data=='}'and li[-1]=='{')or (t.data==']' and li[-1]=='['):
                        li.pop()
                        c=c+1
                else:
                    print(c)
                    break
            elif len(li)!=0:
                print(1)
            t=t.nxt
        if len(li)==0:
            print(-1)
    def evenodds_sum(self,t,x,y):
        if t==None:
            return abs(x-y)
        if t.data%2==0:
            x=x+t.data
        else:
            y=y+t.data
        return self.evenodds_sum(t.nxt,x,y)
    def checkprime(self,t,c):
        if t==None:
            return c
        def pn(s,n):
            if(s>(n//2)+1):
                return 1
            if n%s==0:
                return 0
            return pn(s+1,n)
        if(pn(2,t.data)):
            c=c+1
        return self.checkprime(t.nxt,c)
            
        
l=dll()
l.addback(1)
l.addback(2)
l.addback(3)
l.addback(4)
l.addback(5)
l.addback(6)
l.paran()
l.display()
print(l.evenodds_sum(l.head,0,0))
print(l.checkprime(l.head,0))
