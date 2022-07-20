from itertools import combinations as comb, combinations_with_replacement as cwr

com = comb([1,2,3,4,5],3)
for i in com :
    print(i)
'''
= RESTART: F:/python/python_programs/5competetive programming/2itertools modul/combinations demo.py
(1, 2, 3)
(1, 2, 4)
(1, 2, 5)
(1, 3, 4)
(1, 3, 5)
(1, 4, 5)
(2, 3, 4)
(2, 3, 5)
(2, 4, 5)
(3, 4, 5)
'''

com = comb([1,2,3,4,5],5)
for i in com :
    print(i)
'''
(1, 2, 3, 4, 5)
>>> 
'''

com = cwr([1,2,3,4,5],5)
for i in com :
    print('*',i)

    
com = comb(['a','b','c','d','e'],3)
for i in com :
    print(i)
'''
(1, 2, 3, 4, 5)
('a', 'b', 'c')
('a', 'b', 'd')
('a', 'b', 'e')
('a', 'c', 'd')
('a', 'c', 'e')
('a', 'd', 'e')
('b', 'c', 'd')
('b', 'c', 'e')
('b', 'd', 'e')
('c', 'd', 'e')
'''

com = comb('abcd',2)
for i in com :
    print(i)
'''
('a', 'b')
('a', 'c')
('a', 'd')
('b', 'c')
('b', 'd')
('c', 'd')
'''
