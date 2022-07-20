'''
This module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.

Heaps are binary trees for which every parent node has a value less than or equal to any of its children.
This implementation uses arrays for which heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k, counting elements from zero.
For the sake of comparison, non-existing elements are considered to be infinite.
The interesting property of a heap is that its smallest element is always the root, heap[0].

The following functions are provided:

1)heapq.heappush(heap, item)
Push the value item onto the heap, maintaining the heap invariant.

2)heapq.heappop(heap)
Pop and return the smallest item from the heap, maintaining the heap invariant.
If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].

3)heapq.heappushpop(heap, item)
Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than
heappush()followed by a separate call to heappop().

4)heapq.heapify(x)
Transform list x into a heap, in-place, in linear time.

5)heapq.heapreplace(heap, item)
Pop and return the smallest item from the heap, and also push the new item. The heap size doesn’t change.
If the heap is empty, IndexError is raised.

6)heapq.nlargest(n, iterable, key=None)
Return a list with the n largest elements from the dataset defined by iterable.
key, if provided, specifies a function of one argument that is used to extract a comparison key from
each element in iterable(for example, key=str.lower).
Equivalent to: sorted(iterable, key=key, reverse=True)[:n].

7)heapq.nsmallest(n, iterable, key=None)
Return a list with the n smallest elements from the dataset defined by iterable.
key, if provided, specifies a function of one argument that is used to extract a comparison key from
each element in iterable (for example, key=str.lower). Equivalent to: sorted(iterable, key=key)[:n].
'''

import heapq

h = [2,1,3]

heapq.heappush(h,0)
print(h)                                                #[0, 2, 3, 1]

print(heapq.heappop(h))                                 #0
print(h)                                                #[1,2,3]

print(heapq.heappushpop(h,4))                           #1
print(h)                                                #[2,4,3]

heapq.heapify(h)                                            
print(h)                                                #[2,4,3]

print(heapq.heapreplace(h,7))                           #2                     
print(h)                                                #[3,4,7]

print(heapq.nsmallest(2,h))                             #[3,4]

print(heapq.nlargest(2,h))                              #[4,7]


#Problem statements
'''
The n-largest/n-smallest function of the heapq Package.
This function helps to return the top n smallest/largest elements in any lists and here again n is a number specified by the programmer.
'''

# Python code to find 3 largest and 4 smallest
# elements of a list.
import heapq
  
grades = [110, 25, 38, 49, 20, 95, 33, 87, 80, 90]
print(heapq.nlargest(3, grades))
print(heapq.nsmallest(4, grades))
'''
[110, 95, 90]
[20, 25, 33, 38]
>>> 
'''


# Sort elements is list

def heafSort(l):
    h = []
    for i in l :
        heapq.heappush(h,i)
    return [heapq.heappop(h) for i in range(len(h))]
print(heafSort([1,4,2,3,5]))                            #[1, 2, 3, 4, 5]
