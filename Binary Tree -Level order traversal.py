#!/usr/bin/env python
# coding: utf-8

# In[21]:


class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
        self.hd=0
        self.level=0
def level_vertical_order(root,order):
    result_H={}
    result_V={}
    q=[(root,0,0)]
    while q:
        node,hd,lvl=q.pop(0)
        if lvl not in result_H:
            result_H[lvl]=[]
        if hd not in result_V:
            result_V[hd]=[]
        result_V[hd].append(node.data)
        result_H[lvl].append(node.data)
        if node.left:
            node.left.level=lvl+1
            node.left.hd=hd-1
            q.append((node.left,hd-1,lvl+1))
        if node.right:
            node.right.level=lvl+1
            node.right.hd=hd+1
            q.append((node.right,hd+1,lvl+1))
            
    if order=="H":
        for lvl in result_H.keys():
            print(result_H[lvl],end=",")
    if order=="V":
        for hd in result_V.keys():
            print(result_V[hd],end=",")
            
#DriverCode
root=Node(2)
root.left=Node(7)
root.right=Node(5)
root.left.left=Node(2)
root.left.right=Node(6)
root.left.right.left=Node(5)
root.left.right.right=Node(11)
root.right.right=Node(9)
root.right.right.left=Node(4)
print("--Level Order Traversal--")
print("Horizontal Traversal :")
level_vertical_order(root,"H")
print("\n Vertical Travesal :")
level_vertical_order(root,"V")

            


# In[30]:


class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
        self.hd=0
        self.level=0
def reverse_level_order(root,order):
    result_H={}
    result_V={}
    q=[(root,0,0)]
    while q:
        node,hd,lvl=q.pop(0)
        if lvl not in result_H:
            result_H[lvl]=[]
            
        result_H[lvl].append(node.data)
        if node.left:
            node.left.level=lvl+1
            node.left.hd=hd-1
            q.append((node.left,hd-1,lvl+1))
        if node.right:
            node.right.level=lvl+1
            node.right.hd=hd+1
            q.append((node.right,hd+1,lvl+1))
            
    for lvl in sorted(result_H.keys(),reverse=True):
        print(result_H[lvl],end=" ")
            
#DriverCode
root=Node(2)
root.left=Node(7)
root.right=Node(5)
root.left.left=Node(2)
root.left.right=Node(6)
root.left.right.left=Node(5)
root.left.right.right=Node(11)
root.right.right=Node(9)
root.right.right.left=Node(4)
print("--Level Order Traversal--")
print("Horizontal Traversal :")
level_vertical_order(root,"H")
print("\n Vertical Travesal :")
level_vertical_order(root,"V")


# In[36]:


class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
        
def printLeaves(root):
    if(root):
        printLeaves(root.left)
        if root.left is None and root.right is None:
            print(root.data,end=" ")
 
        printLeaves(root.right)
    
def printBoundaryLeft(root):
     
    if(root):
        if (root.left):
            print(root.data,end=" ")
            printBoundaryLeft(root.left)
         
        elif(root.right):
            print (root.data, end=" ")
            printBoundaryLeft(root.right)
def printBoundaryRight(root):
     
    if(root):
        if (root.right):
            printBoundaryRight(root.right)
            print(root.data,end=" ")
         
        elif(root.left):
            printBoundaryRight(root.left)
            print(root.data,end=" ")
def printBoundary(root):
    if (root):
        print(root.data,end=" ")
         
        printBoundaryLeft(root.left)
 
        printLeaves(root.left)
        printLeaves(root.right)
 
        printBoundaryRight(root.right)

    
root=Node(2)
root.left=Node(7)
root.right=Node(5)
root.left.left=Node(2)
root.left.right=Node(6)
root.left.right.left=Node(5)
root.left.right.right=Node(11)
root.right.right=Node(9)
root.right.right.left=Node(4)
print("Boundary traveresal :")
printBoundary(root)


# In[ ]:




