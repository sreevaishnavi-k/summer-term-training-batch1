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
    def rev_display(self):
        t=self.tail
        while(t!=None):
            print(t.data,end="<->")
            t=t.prev
        print()
    def search(self,x):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.nxt):
            if(t.data==x or t1.data==x):
                print("element found")
                break
            else:
                t=t.nxt
                t1=t1.prev
        if(t.data==x):
            print("element found")
        else:
            print("element not found")
    def evenodd(self):
        t=self.head
        t1=self.tail
        while(t!=t1 and t1!=t1.nxt):
            if t==t1.prev:
                print("even")
                break
            else:
                t=t.nxt
                t1=t1.prev
        else:
            print("odd")
    def palin(self):
        t=self.head
        t1=self.tail
        while(t!=t1 and t1!=t1.nxt):
            if(t.data==t1.data):
                t=t.nxt
                t1=t1.prev
            else:
                print("no")
                return
        print("yes")
    def div(self):
        t=self.head
        t1=self.tail
        s=self.tail
        while(t!=t1.prev):
            t=t.nxt
            t1=t1.prev
        t=self.head
        while(t1!=None):
            t.data,t1.data=t1.data,t.data
            t=t.nxt
            t1=t1.nxt
    def swapadj(self):
        t=self.head
        t1=t.nxt
        t2=None
        while(t!=None and t1.nxt!=None):
            if t==self.head:
                t.nxt=t1.nxt
                t1.nxt=t
                t1.prev=t2
                self.head=t1
                t,t1=t1,t
                t2=t1
            else:
                t.nxt=t1.nxt
                t1.nxt=t
                t1.prev=t2
                t2.nxt=t1
                t,t1=t1,t
                t2=t1
            t=t.nxt.nxt
            t1=t1.nxt.nxt
                
                
                
            
            
            
        
        
            
        
l=dll()
l.addbeg(8)
l.addbeg(7)
l.addbeg(5)
#l.display()
l.addback(2)
l.addback(1)
l.addback(4)
l.display()
'''l.rev_display()
l.search(4)
l.search(9)
l.evenodd()
l.palin()'''
'''l.div()
l.display()'''
l.swapadj()
l.display()




            
            
            
        
