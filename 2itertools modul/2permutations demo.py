from itertools import permutations as perm

per = perm([1,2,3],3)
for p in per:
    print(p)
'''
= RESTART: F:/python/python_programs/5competetive programming/2itertools modul/2permutations demo.py
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)
>>> 
'''

per = perm('abc',3)
for p in per:
    print(p)
'''
('a', 'b', 'c')
('a', 'c', 'b')
('b', 'a', 'c')
('b', 'c', 'a')
('c', 'a', 'b')
('c', 'b', 'a')
'''

per = perm([1,2,3,4,5],3)
for p in per:
    print(p)
'''
(1, 2, 3)
(1, 2, 4)
(1, 2, 5)
(1, 3, 2)
(1, 3, 4)
(1, 3, 5)
(1, 4, 2)
(1, 4, 3)
(1, 4, 5)
(1, 5, 2)
(1, 5, 3)
(1, 5, 4)
(2, 1, 3)
(2, 1, 4)
(2, 1, 5)
(2, 3, 1)
(2, 3, 4)
(2, 3, 5)
(2, 4, 1)
(2, 4, 3)
(2, 4, 5)
(2, 5, 1)
(2, 5, 3)
(2, 5, 4)
(3, 1, 2)
(3, 1, 4)
(3, 1, 5)
(3, 2, 1)
(3, 2, 4)
(3, 2, 5)
(3, 4, 1)
(3, 4, 2)
(3, 4, 5)
(3, 5, 1)
(3, 5, 2)
(3, 5, 4)
(4, 1, 2)
(4, 1, 3)
(4, 1, 5)
(4, 2, 1)
(4, 2, 3)
(4, 2, 5)
(4, 3, 1)
(4, 3, 2)
(4, 3, 5)
(4, 5, 1)
(4, 5, 2)
(4, 5, 3)
(5, 1, 2)
(5, 1, 3)
(5, 1, 4)
(5, 2, 1)
(5, 2, 3)
(5, 2, 4)
(5, 3, 1)
(5, 3, 2)
(5, 3, 4)
(5, 4, 1)
(5, 4, 2)
(5, 4, 3)
'''
