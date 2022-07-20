'''
deque objects

class collections.deque([iterable[, maxlen]])
Returns a new deque object initialized left-to-right (using append()) with data from iterable.
If iterable is not specified, the new deque is empty.

Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”).
Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately
the same O(1) performance in either direction.

Though list objects support similar operations, they are optimized for fast fixed-length operations andincur O(n) memory movement
costs for pop(0) and insert(0, v) operations which change both the size and position of the underlying data representation.

If maxlen is not specified or is None, deques may grow to an arbitrary length.
Otherwise,the deque is bounded to thespecifiedmaximum length.
Once a bounded length deque is full, when new items are added, a corresponding number of items are discarded from the opposite end.
Bounded length deques provide functionality similar to the tail filter in Unix.
They are also useful for tracking transactions and other pools of data where only the most recent activity is of interest.

Deque objects support the following methods:

n1)append(x)
Add x to the right side of the deque.

2)appendleft(x)
Add x to the left side of the deque.

3)clear()
Remove all elements from the deque leaving it with length 0.

4)copy()
Create a shallow copy of the deque.

New in version 3.5.

5)count(x)
Count the number of deque elements equal to x.

New in version 3.2.

6)extend(iterable)
Extend the right side of the deque by appending elements from the iterable argument.

7)extendleft(iterable)
Extend the left side of the deque by appending elements from iterable. Note, the series of left appends results in reversing the order of elements in the iterable argument.

8)index(x[, start[, stop]])
Return the position of x in the deque (at or after index start and before index stop). Returns the first match or raises ValueError if not found.

New in version 3.5.

9)insert(i, x)
Insert x into the deque at position i.

If the insertion would cause a bounded deque to grow beyond maxlen, an IndexError is raised.

New in version 3.5.

10)pop()
Remove and return an element from the right side of the deque. If no elements are present, raises an IndexError.

11)popleft()
Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.

12)remove(value)
Remove the first occurrence of value. If not found, raises a ValueError.

13)reverse()
Reverse the elements of the deque in-place and then return None.

New in version 3.2.

14)rotate(n=1)
Rotate the deque n steps to the right. If n is negative, rotate to the left.

When the deque is not empty, rotating one step to the right is equivalent to d.appendleft(d.pop()),
and rotating one step to the left is equivalent to d.append(d.popleft()).

#Deque objects also provide one read-only attribute:

1)maxlen
Maximum size of a deque or None if unbounded.

New in version 3.1.

In addition to the above, deques support iteration, pickling, len(d), reversed(d), copy.copy(d), copy.deepcopy(d),
membership testing with the in operator, and subscript references such as d[0] to access the first element.
Indexed access is O(1) at both ends but slows to O(n) in the middle. For fast random access, use lists instead.

Starting in version 3.5, deques support __add__(), __mul__(), and __imul__().
'''

from collections import deque
d = deque('ghi')                 # make a new deque with three items
for elem in d:                   # iterate over the deque's elements
    print(elem.upper())
'''
G
H
I
'''
d.append('j')                    # add a new entry to the right side

d.appendleft('f')                # add a new entry to the left side

print(d)                         # show the representation of the deque
#deque(['f', 'g', 'h', 'i', 'j'])

print(d.pop())                          # return and remove the rightmost item
#'j'

print(d.popleft())                      # return and remove the leftmost item
#'f'

list(d)                          # list the contents of the deque
#['g', 'h', 'i']

d[0]                             # peek at leftmost item
#'g'

d[-1]                            # peek at rightmost item
#'i'

list(reversed(d))                # list the contents of a deque in reverse
#['i', 'h', 'g']

print('h' in d)                         # search the deque
#True

d.extend('jkl')                  # add multiple elements at once
print(d)
#deque(['g', 'h', 'i', 'j', 'k', 'l'])

d.rotate(1)                      # right rotation
print(d)
#deque(['l', 'g', 'h', 'i', 'j', 'k'])

d.rotate(-1)                     # left rotation
print(d)
#deque(['g', 'h', 'i', 'j', 'k', 'l'])

print(deque(reversed(d)))               # make a new deque in reverse order
#deque(['l', 'k', 'j', 'i', 'h', 'g'])

d.clear()                        # empty the deque
'''
d.pop()                          # cannot pop from an empty deque
Traceback (most recent call last):
    File "<pyshell#6>", line 1, in -toplevel-
        d.pop()
IndexError: pop from an empty deque
'''

d.extendleft('abc')              # extendleft() reverses the input order
print(d)
#deque(['c', 'b', 'a'])
