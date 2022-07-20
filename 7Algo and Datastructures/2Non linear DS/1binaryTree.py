
#class to create tree node
class Node:
    def __init__(self,data):
        self.__left = None
        self.__data = data
        self.__right = None
        print('node created successfully...')
        
    def getData(self):
        return self.__data
    
    def setData(self,data):
        self.__data = data
        
    def getLeft(self):
        return self.__left
    
    def setLeft(self,left_node):
        self.__left = left_node

    def getRight(self):
        return self.__right
    
    def setRight(self,right_node):
        self.__right = right_node

class BSTTree:
    def __init__(self):
        self.__root = None

    def getRoot(self):
        return self.__root

    def setRoot(self,root):
        self.__root = root

    def insert(self,root,node):
        if self.__root == None:
            self.__root = node
        elif( node.getData()<root.getData() and root.getLeft()==None):
            print(node.getData(),'is inserted at left of ',root.getData())
            root.setLeft(node)
        elif( node.getData()>root.getData() and root.getRight()==None):
            print(node.getData(),'is inserted at right of ',root.getData())
            root.setRight(node)
        elif( node.getData()<root.getData() and root.getLeft()!=None):
            self.insert((root.getLeft()),node)
        elif( node.getData()>root.getData() and root.getRight()!=None):
            self.insert((root.getRight()),node)
        print('insertion done successfully...')

    
    def findSmallestNode(self,root):
        trav_node = root   #node to travel in left subtree to get smallest node
        while(trav_node.getLeft()):
            trav_node = trav_node.getLeft()
        return trav_node
            
    def delete(self,root,key):
        
        #s1st earch deleting node
        if(root==None):
            print('key not found')
            return root
        
        elif(key<root.getData()):   #if key is less than root value then search in left sub tree of root
            self.delete(root.getLeft(),key)
            
        elif(key>root.getData()):   #if key is greater than root value then search in right sub tree of root
            self.delete(root.getRight(),key)
        
        else :
            print('key found')      #if key is found at root

            #if deleting node does not have any childs then simply make node None, so considered as deleted
            if(root.getLeft()==None and root.getRight()==None):
                print('no child')
                root = None
                #root.setNode(None)
                
            #if left child of node is None then replace deleting node with right node, so deleting node get deleted
            elif(root.getLeft()==None):
                print('right child')
                root = root.getRight()

            #if right child of node is None then replace deleting node with left node, so deleting node get deleted
            elif(root.getRight()==None):
                print('left child')
                root = root.getLeft()

            #if deleting node have left and right child then replace node with smallest node in right subtree    
            else:
                #1st find smallest node in right subtree(Inorder successor)
                temp = self.findSmallestNode(root.getRight())
                #assign value of temp(smallest node) to root node and delete smallest node left right subtree
                #but temp can have childs, so again pass temp to delete() method as root to delete without loosing his childs
                root.right = self.delete(root.getRight(),temp.getData())
        return root
            

    def search(self,root,key):
        '''
        if(root.getData()==key):
            #print(root.getData())
            print('key is found')
        elif( key<root.getData() and root.getLeft()!=None):
            print('searching in left')
            self.search(root.getLeft(),key)
        elif( key>root.getData() and root.getRight()!=None):
            print('searching in right')
            self.search(root.getRight(),key)
        else :
            print('key not found')
        '''
        if(root == None):
            print('key is not found')
            return root
        elif( key<root.getData()):
            self.search(root.getLeft(),key)
        elif( key>root.getData()):
            #print('searching in right')
            self.search(root.getRight(),key)
        else :
            print('key found')
            
        
        

    def preOrder(self,root):
        if(root!=None):
            print(root.getData())
            self.preOrder(root.getLeft())
            self.preOrder(root.getRight())

    def inOrder(self,root):
        if(root!=None):
            self.inOrder(root.getLeft())
            print(root.getData())
            self.inOrder(root.getRight())

    def postOrder(self,root):
        if(root!=None):
            self.postOrder(root.getLeft())
            self.postOrder(root.getRight())
            print(root.getData())


tree = BSTTree()

while(True):
    print('\n1.Insert\n2.search\n3.travelsing\n4.delete \n5.quite')
    ch = int(input('Enter your choice'))

    if ch == 1:
        data = int(input('Enter data to insert'))
        node = Node(data)
        tree.insert(tree.getRoot(),node)
        
    elif ch == 2:
        if tree.getRoot()==None :
            print('Tree is empty!!!')
        else:
            key = int(input('Enter key to search'))
            tree.search(tree.getRoot(),key)
            '''
            if(tree.search(tree.getRoot(),key)):
                print('key is found')
            else :
                print('key not found')
            '''
            
        
    elif ch == 3:
        if tree.getRoot()==None :
            print('Tree is empty!!!')
        else :
            print('\n 1.In order\n 2.Pre order \n 3. Post order ')
            ch2 = int(input('Enter your choice'))
            if ch2 == 1:
                tree.inOrder(tree.getRoot())
            elif ch2 == 2:
                tree.preOrder(tree.getRoot())
            elif ch2 == 3:
                tree.postOrder(tree.getRoot())
            else :
                print('Enter correct choice!!!')

    elif ch == 4 :
        if tree.getRoot()==None :
            print('Tree is empty!!!')
        else :
            key = int(input('Enter key to delete that node '))
            tree.setRoot((tree.delete(tree.getRoot(),key)))

    elif ch == 5 :
        break

    else :
            print('Enter correct choice!!!')
        
        
        
        
