#1) using simple list

stack = list()
print('initial stack ',stack)
print('inserting 5 elements in stack')
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
print('after insertion stack bottom -> top',stack)
print('delete element from stack')
stack.pop() # it will top most element
print('after deletion stack bottom -> top',stack)
'''
initial stack  []
inserting 5 elements in stack
after insertion stack bottom -> top [1, 2, 3, 4, 5]
delete element from stack
after deletion stack bottom -> top [1, 2, 3, 4]
'''

print('------------------------------------------------------------------------')

max_size = int(input('enter size of stack '))
stack = [None] * max_size
top = -1
print('initial stack ',stack,' and top ',top)

def insert(ele):
    global top, max_size, stack
    #1st check  stack overflow
    if(top == max_size-1):
        print('overflow...')
    else :
        top += 1
        stack[top] = ele

def delete():
    global top, max_size, stack
    #1st check  stack underflow
    if(top == -1):
        print('underflow...')
    else :
        ele = stack[top]
        top -= 1
        return ele
         
def display():
    if(top == -1):
        print('stack is empty')
    else :
        for i in range(0,top+1):
            print(stack[i])

while(True):
    print(' 1.insertion\n 2.deletion\n 3.display\n 4.exit\nEnter your choice : ')
    ch = int(input())
    if ch == 1:
        print('enter element to insert : ')
        ele = int(input())
        insert(ele)
    elif ch == 2:
        print('deleted element : ',delete())
    elif ch == 3:
        display()
    elif ch == 4:
        break
    else :
        print('enter correct choice')

print('------------------------------------------------------------------------')

class Stack:
    def __init__(self, size):
        self.__max_size = size
        self.__elements = [None] * size
        self.__top = -1
        
    def display(self):
        for i in range(0,self.__top+1):
            print(self.__elements[i])
        print('top : ',self.__top)
        #return (str() for i in range(0,top+1)+' and top : '+int(self.__top))

    def isFull(self):
        if self.__top == self.__max_size - 1:
            return True
        else :
            return False

    def isEmpty(self):
        if self.__top == -1:
            return True
        else :
            return False
        
    def insert(self,ele):
        if(self.isFull()):
            print('overflow...')
        else :
            self.__top += 1
            self.__elements[self.__top] = ele

    def delete(self):
        if(self.isEmpty()):
            print('underflow...')
        else :
            ele = self.__elements[self.__top]
            self.__elements[self.__top] = None
            self.__top -= 1
            return ele

s1 = Stack(3)

while(True):
    print(' 1.insertion\n 2.deletion\n 3.display\n 4.exit\nEnter your choice : ')
    ch = int(input())
    if ch == 1:
        print('enter element to insert : ')
        ele = int(input())
        s1.insert(ele)
    elif ch == 2:
        print('deleted element : ',s1.delete())
    elif ch == 3:
        s1.display()
    elif ch == 4:
        break
    else :
        print('enter correct choice')

            
    
        
    







