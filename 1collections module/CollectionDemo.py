'''
-------------class collections.Counter([iterable-or-mapping])--------------
-------------Counter_object.elements()--------------
-------------counter_object.values()----------------
-------------counter_object.most_common(int)--------

A Counter is a dict subclass for counting hashable objects.
It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
Counts are allowed to be any integer value including zero or negative counts.
The Counter class is similar to bags or multisets in other languages.
'''

from collections import Counter

l = [1,3,2,4,1,5,3,2,1,4,3,2,1,4,5]
cnt = Counter(l)
print(cnt)
print('occurance of 1 is ',cnt[1])
del cnt[1]
print('occurance of 1 after deletion is ',cnt[1])
'''
= RESTART: F:/python/python_programs/5competetive programming/collections module demo/CollectionDemo.py
Counter({1: 4, 3: 3, 2: 3, 4: 3, 5: 2})
occurance of 1 is  4
occurance of 1 after deletion is  0
'''

print('--------------------------------------------------------------------------------')

'''
elements()
Return an iterator over elements repeating each as many times as its count.
Elements are returned in the order first encountered.
If an element’s count is less than one, elements() will ignore it.
'''
iterator = cnt.elements()   # returns elements as a iterator
print(cnt.elements())
print('elements in counter are ',sorted(iterator))
for i in cnt.elements():
    print(i,end='   ')
print('\noccurance in counter are ',sorted(cnt.values()))
'''
--------------------------------------------------------------------------------
<itertools.chain object at 0x00000061C0C72F88>
elements in counter are  [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5]
3   3   3   2   2   2   4   4   4   5   5
occurance in counter are  [2, 3, 3, 3]
'''

print('--------------------------------------------------------------------------------')


'''
most_common([n])
Return a list of the n most common elements and their counts from the most common to the least.
If n is omitted or None, most_common() returns all elements in the counter.
Elements with equal counts are ordered in the order first encountered:
'''

print('print elements according to largest count\n ', cnt.most_common())
print('print elements according to largest count\n ', cnt.most_common(1))

print('top 3 elements having largest count', cnt.most_common(3))

'''
print elements according to largest count
  [(1, 4), (3, 3), (2, 3), (4, 3), (5, 2)]
top 3 elements having largest count [(1, 4), (3, 3), (2, 3)]
>>> 
'''

print('--------------------------------------------------------------------------------')

'''
subtract([iterable-or-mapping])
Elements are subtracted from an iterable or from another mapping (or counter).
Like dict.update() but subtracts counts instead of replacing them.
Both inputs and outputs may be zero or negative.
'''
l2 = [1,3,2,4,1,5]
cnt2 = Counter(l2)
cnt.subtract(cnt2)
print(cnt)
'''
--------------------------------------------------------------------------------
Counter({3: 2, 2: 2, 4: 2, 5: 1, 1: -2})
'''

print('--------------------------------------------------------------------------------')

print('sum of counts ',sum(cnt.values()))                 # total of all counts
list(cnt)                         # list unique elements
set(cnt)                          # convert to a set
dict(cnt)                         # convert to a regular dictionary
print(cnt.items())                       # convert to a list of (elem, cnt) pairs
#print(cnt.most_common()[:-n-1:-1])       # n least common elements
print(+cnt)                              # remove zero and negative counts
#print(Counter(dict(list_of_pairs)))    # convert from a list of (elem, cnt) pairs
cnt.clear()                       # reset all counts
'''
--------------------------------------------------------------------------------
sum of counts  5
dict_items([(3, 2), (2, 2), (4, 2), (5, 1), (1, -2)])
Counter({3: 2, 2: 2, 4: 2, 5: 1})
>>> 
'''

print('--------------------------------------------------------------------------------')


c = Counter(a=3, b=1)
d = Counter(a=1, b=2, c=3)
print(c + d)                       # add two counters together:  c[x] + d[x]

print(c - d)                      # subtract (keeping only positive counts)

print(c & d )                      # intersection:  min(c[x], d[x]) 

print(c | d )                      # union:  max(c[x], d[x])

c = Counter(a=2, b=-4)
print(+c)

print(-c)
'''
--------------------------------------------------------------------------------
Counter({'a': 4, 'b': 3, 'c': 3})
Counter({'a': 2})
Counter({'a': 1, 'b': 1})
Counter({'a': 3, 'c': 3, 'b': 2})
Counter({'a': 2})
Counter({'b': 4})
>>> 
'''



