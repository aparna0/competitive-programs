
#class to create tree node
class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
        print('node created successfully...')

def insert(root,data):
    if(root==None):
        return Node(data)
    elif(data<root.data):
        root.left = insert(root.left,data)
    elif(data>root.data):
        root.right = insert(root.right,data)
    return root

def search(root,data):
    if(root==None):
        print('key not found')
    elif(data<root.data):
        search(root.left,data)
    elif(data>root.data):
        search(root.right,data)
    else:   
        print('key found')
    

def preOrder(root):
    if(root!=None):
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)

def inOrder(root):
    if(root!=None):
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)

def postOrder(root):
    if(root!=None):
        postOrder(root.left)
        postOrder(root.right)
        print(root.data)

def findSmallestnode(root):
    trav_node = root   #node to travel in left subtree to get smallest node
    while(trav_node.left):
        trav_node = trav_node.left
    return trav_node

def delete(root,data):
    #s1st earch deleting node
    if(root==None):
        return root
    
    elif(data<root.data):   #if key is less than root value then search in left sub tree of root
        root.left = delete(root.left,data)
        #return root
        
    elif(data>root.data):   #if key is greater than root value then search in right sub tree of root
        root.right = delete(root.right,data)
        #return root
        
    else:
        print('key found')      #if key is found at this node
        #if deleting node does not have any childs then simply make node None, so considered as deleted
        if(root.left==None and root.right==None):
            return None

        #if left child of node is None then replace deleting node with right node, so deleting node get deleted
        elif(root.left==None):
            root = root.right

        #if right child of node is None then replace deleting node with left node, so deleting node get deleted
        elif(root.right==None):
            root = root.left
            
        #if deleting node have left and right child then replace node with smallest node in right subtree    
        else :
            #1st find smallest node in right subtree(Inorder successor)
            temp = findSmallestNode(root)
            #assign value of temp(smallest node) to root node and delete smallest node left right subtree
            #but temp can have childs, so again pass temp to delete() method as root to delete without loosing his childs
            root.data = temp.data
            root.right = delete(root.right,temp.data)
        
    return root
            
root = None

while(True):
    print('\n1.Insert\n2.search\n3.travelsing\n4.delete \n5.quite')
    ch = int(input('Enter your choice'))

    if ch == 1:
        data = int(input('Enter data to insert'))
        root = insert(root,data)
        print(root.data)
        
    elif ch == 2:
        if root==None :
            print('Tree is empty!!!')
        else:
            key = int(input('Enter key to search'))
            search(root,key)

    elif ch == 3:
        if root==None :
            print('Tree is empty!!!')
        else :
            print('\n 1.In order\n 2.Pre order \n 3. Post order ')
            ch2 = int(input('Enter your choice'))
            if ch2 == 1:
                inOrder(root)
            elif ch2 == 2:
                preOrder(root)
            elif ch2 == 3:
                postOrder(root)
            else :
                print('Enter correct choice!!!')

    elif ch == 4 :
        if root==None :
            print('Tree is empty!!!')
        else :
            key = int(input('Enter key to delete that node '))
            root = delete(root,key)

    elif ch == 5 :
        break

    else :
            print('Enter correct choice!!!')
        
