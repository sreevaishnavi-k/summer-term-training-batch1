class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Binary_tree:
    def create_node(self,data):
        return Node(data)
    def insert(self,node,data):
        if node is None:
            return self.create_node(data)
        if data<node.data:
            node.left=self.insert(node.left,data)
        else:
            node.right=self.insert(node.right,data)
        return node
    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
    def preorder(self,root):
        if root is not None:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)
    def addallnodes(self,root):
         if root==None:
             return 0
         return root.data+self.addallnodes(root.left)+self.addallnodes(root.right)
    def addevennodes(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return root.data+self.addevennodes(root.left)+self.addevennodes(root.right)
        else:
            return self.addevennodes(root.left)+self.addevennodes(root.right)
    def addoddnodes(self,root):
        if root==None:
            return 0
        if root.data%2!=0:
            return root.data+self.addoddnodes(root.left)+self.addoddnodes(root.right)
        else:
            return self.addoddnodes(root.left)+self.addoddnodes(root.right)
    def evenodd_diff(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return root.data+self.evenodd_diff(root.left)+self.evenodd_diff(root.right)
            
        return self.evenodd_diff(root.left)+self.evenodd_diff(root.right)-root.data
    def height(self,root):
        if root==None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1
    def balance(self,root):
        return abs(self.height(root.left)-self.height(root.right))<=1
    def leafnodes(self,root):
        if root==None:
            return 0
        if root.left == None and root.right == None:
           return 1
        return self.leafnodes(root.left)+self.leafnodes(root.right)
    def sumofLNData(self,root):
         if root==None:
             return 0
         if root.left == None and root.right == None:
            return root.data
         return self.sumofLNData(root.left)+self.sumofLNData(root.right)
    def depth(self,root,y,c):
        if root.data==y:
           return c
        elif y<root.data:
            return self.depth(root.left,y,c+1)
        elif y>root.data:
            return self.depth(root.right,y,c+1)
            
    def search(self,root,x):
        if root==None:
            return 0
        if root.data==x:
            return 1
            self.depth(root,x,0)
        elif x<root.data:
            return self.search(root.left,x)
        elif x>root.data:  
            return self.search(root.right,x)
    def leafnodes(self,root):
        if root!=None:
            if root.left==None and root.right==None:
                print(root.data)
            self.leafnodes(root.left)
            self.leafnodes(root.right)
    def leftview(self,root,c,l):
        if root==None:
            return
        if c not in l:
            print(root.data)
            l.append(c)
        self.leftview(root.left,c+1,l)
        self.leftview(root.right,c+1,l)
    def rightview(self,root,c,l):
        if root==None:
            return
        if c not in l:
            print(root.data)
            l.append(c)
        self.rightview(root.right,c+1,l)
        self.rightview(root.left,c+1,l)
    def topview(self,root):
        if root == None:
            return
        d={}
        q=[(root,0)]
        while(q):
            root=q[0][0]
            if root.left!=None:
                q.append((root.left,q[0][1]-1))
            if root.right!=None:
                q.append((root.right,q[0][1]+1))
            if q[0][1] not in d:
                d[q[0][1]]=root.data
            q.pop(0)
        for i in sorted(d):
            print(d[i],end=" ")
                
    def bottomview(self,root):
        if root == None:
            return
        d={}
        q=[(root,0)]
        while(q):
            root=q[0][0]
            if root.left!=None:
                q.append((root.left,q[0][1]-1))
            if root.right!=None:
                q.append((root.right,q[0][1]+1))
            d[q[0][1]]=root.data
            q.pop(0)
        for i in sorted(d):
            print(d[i],end=" ")   
        
            
tree=Binary_tree()
root=tree.create_node(10)
print("root node:",root.data)
tree.insert(root,5)
tree.insert(root,15)
tree.insert(root,2)
tree.insert(root,7)
tree.insert(root,11)
tree.insert(root,20)
tree.insert(root,4)
tree.insert(root,12)
tree.insert(root,3)
tree.insert(root,13)
tree.insert(root,14)
'''tree.inorder(root)
print()
tree.preorder(root)
print()
tree.postorder(root)'''
print(tree.addallnodes(root))
print(tree.addevennodes(root))
print(tree.addoddnodes(root))
print(tree.evenodd_diff(root))
print(tree.height(root))
if (tree.balance(root)):
    print("balanced")
else:
    print("not balanced")
print(tree.leafnodes(root))
print(tree.sumofLNData(root))
t=tree.search(root,2)
if(t==1):
    print("found")
else:
    print("not found")
print(tree.depth(root,2,0))
print("leafnodes:")
tree.leafnodes(root)
print("leftsideview:")
tree.leftview(root,0,[])
print("rightsideview:")
tree.rightview(root,0,[])s
print("topview:")
tree.topview(root)
print()
print("Bottomview:")
tree.bottomview(root)