#1)list using Array

import sys
def getListDetails(l):
    #size = sys.getsizeof(l)
    #capacity = (size of list - size of empty list) // (size of one block)
    #size of empty list maens total number of bits for empty list
    capacity = (sys.getsizeof(l)-64)//8 
    left_size = ((sys.getsizeof(l)-64)-len(l)*8)//8
    #(size-36)//4 for 32bit system
    #(size-64)//8 for 64bit system
    print('size of list is ',sys.getsizeof(l))
    print('capacity is ',capacity)
    print('remaining capacity is ',left_size)
    
def insertAtBegin(l,ele):
    l.insert(0,ele)
def insertInBetween(l,index,ele):
    l.insert(index,ele)
def insertAtEnd(l,ele):
    l.append(ele)

def deleteAtBegin(l):
    l.pop(0)
def deleteAtBetween(l,index):
    l.pop(index)
def deleteAtEnd(l):
    l.pop(-1)

l = list()
getListDetails(l)

#inserting element at begin
insertAtBegin(l,1)

#inserting element in between
insertInBetween(l,1,2)

#inserting element at end
insertAtEnd(l,3)

#deleting at begin
deleteAtBegin(l)

print(l)
getListDetails(l)
'''
= RESTART: F:/python/python_programs/5competetive programming/7linear data structures/3.linklinst.py
size of list is  64
capacity is  0
remaining capacity is  0
[2, 3]
size of list is  96
capacity is  4
remaining capacity is  2
>>> 
'''

#but implementing link list using dynamic array i.e list have some disadvantages
'''
such that even it perform dynamic memory allocation still it having some issues like
1)involes shiftng of elements in insertion and deletion.
2)while insertion when list is full then it increases its capacity by double of its previous capacity,
    this may cause wastage of memory in the form reserved space

Exaple,
    consider list l of capacity 10,
        <insert element 1 to 10  #it will insert 1...10 elements in list
        <insert element 11  # here list is full , so it creates list of size 10*2=20(previous capacity * 2) and
                                shifts the elements this new list
                                and add new element 11 to increased caacity list.
        when is capacity get reache then it again increase the size by 20*2=40 and perform shifting of elements
        and insert new element and so on.
    therefore array list involves shifting of elements and memory wastage.
        
'''
print('------------------------------------------singly link list------------------------------------------')
#using classes and objects

#class to create node
class Node:
    def __init__(self,data):
        self.__data = data
        self.__next = None
        
    def getData(self):
        return self.__data
    
    def setData(self,data):
        self.__data = data
        
    def getNext(self):
        return self.__next
    
    def setNext(self,next_node):
        self.__next = next_node 

class LinkedList:
    def __init__(self):
        self.__head = None

    def getHead(self):
        return self.__head 
        
    def insertAtBegin(self,node):
        if self.__head == None :
            self.__head = node
        else :
            node.setNext(self.__head)
            self.__head = node
        print('insertion done successfully...')
        
    def insertInBetween(self,key,node):
        temp = self.__head
        while(temp.getNext()!=None and temp.getData()!=key):
            temp = temp.getNext()
        if(temp.getData()!=key):
            print('key not found\nInsertion faild!!!')
        else:
            node.setNext(temp.getNext())
            temp.setNext(node)
            print('insertion done successfully...')

    def insertAtEnd(self,node):
        if self.__head == None :
            self.__head = node
        else :
            temp = self.__head
            while(temp.getNext()!=None):
                temp = temp.getNext()
            temp.setNext(node)
        print('insertion done successfully...')
        

    def deleteAtBegin(self):
        self.__head  =  self.__head.getNext()
        print('deletion done successfully')
    
    def deleteInBetween(self,key):
        temp = self.__head
        while(temp.getNext()!=None and temp.getData()!=key):
            delete_node = temp
            temp = temp.getNext()
        if(temp.getData()!=key):
            print('key not found\nInsertion faild!!!')
        else:
            delete_node.setNext((delete_node.getNext()).getNext())
            print('deletion done successfully')

    def deleteAtEnd(self):
        temp = self.__head
        while(temp.getNext()!=None ):
            delete_node = temp
            temp = temp.getNext()
        delete_node.setNext(None)
        print('deletion done successfully')
        

    def travelsing(self):
        if self.__head == None :
            print('Empty List!!!')
        else:
            temp = self.__head
            #print(temp.getData())
            while(temp!=None):
                print(temp.getData())
                temp = temp.getNext()
            
        



link_list = LinkedList()            #it will create empty list

while(True):
    print('\n1.insertion\n2.deletion\n3.display\n4.quit\n Enter your choice')
    ch = int(input())
    if ch == 1:
        #create node
        data = int(input('Enter data '))
        node = Node(data)       

        #insertion of node in link list
        print('1.Insert At begining\n 2.Insert  In Between\n 3.Insert At End')
        ch2 = int(input('Enter your choice'))
        if ch2 == 1:
            link_list.insertAtBegin(node)
        elif ch2 == 2:
            key = int(input('Enter after which you want to insert node'))
            link_list.insertInBetween(key,node)
        elif ch2 == 3:
            link_list.insertAtEnd(node)
        else : print('Enter correct choice !!!')
        
    elif ch == 2:
        #ask for where to delete
        if link_list.getHead() == None:
            print('list is Empty!!!')
        else :
            print('1.Delete At begining\n 2.Delete  In Between\n 3.Delete At End')
            ch2 = int(input('Enter your choice'))
            if ch2 == 1:
                link_list.deleteAtBegin()
            elif ch2 == 2:
                key = int(input('Enter  which you want to delete node'))
                link_list.deleteInBetween(key)
            elif ch2 == 3:
                link_list.deleteAtEnd()
            else : print('Enter correct choice !!!')

    elif ch == 3:
        link_list.travelsing()
        
    elif ch == 4:
        break
    
    else : print('Enter correct choice !!!') 
        

print('------------------------------------------doubly link list------------------------------------------')

#class to create node
class Node:
    def __init__(self,data):
        self.__pre = None
        self.__data = data
        self.__next = None
        
    def getData(self):
        return self.__data
    
    def setData(self,data):
        self.__data = data
        
    def getNext(self):
        return self.__next
    
    def setNext(self,next_node):
        self.__next = next_node

    def getpre(self):
        return self.__pre
    
    def setNext(self,pre_node):
        self.__pre = pre_node
        
