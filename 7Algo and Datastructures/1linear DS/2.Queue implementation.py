#1) using simple list

queue = list()
print('initial queue ',queue)
print('inserting 5 elements in queue')
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
print('after insertion queue front -> rear',queue)
print('delete element from queue')
queue.pop(0) # it will front most element
print('after deletion queue front -> rear',queue)
'''
initial queue  []
inserting 5 elements in queue
after insertion queue front -> rear [1, 2, 3, 4, 5]
delete element from queue
after deletion queue front -> rear [2, 3, 4, 5]
'''

print('------------------------------------------------------------------------')

max_size = int(input('enter size of stack '))
queue = [None] * max_size
front,rear = -1,-1
print('initial queue ',queue,'\nfront ',front,' rear ',rear)


def enqueue(ele):
    global front,rear, max_size, queue
    #1st check overflow
    if(rear == max_size-1):
        print('overflow...')
    else :
        if front == -1:
            front = 0
            rear = 0
        else:
            rear += 1
        queue[rear] = ele
        

def dequeue():
    global front,rear, max_size, queue
    #1st check underflow
    if(front == -1):
        print('underflow...')
    else :
        ele = queue[front]
        queue[front] = None
        if front == rear:
            front,rear=-1,-1
        else:
            front += 1
        
        return ele
         
def display():
    global front,rear, max_size, queue
    if(rear == -1):
        print('queue is empty')
    else :
        for i in range(front,rear+1):
            print(queue[i],end='\t')
        print('\n')

while(True):
    print(' 1.enqueue\n 2.dequeue\n 3.display\n 4.exit\nEnter your choice : ')
    ch = int(input())
    if ch == 1:
        print('enter element to insert : ')
        ele = int(input())
        enqueue(ele)
    elif ch == 2:
        print('deleted element : ',dequeue())
    elif ch == 3:
        display()
    elif ch == 4:
        break
    else :
        print('enter correct choice')
