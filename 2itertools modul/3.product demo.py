from itertools import product

#poduct(p, q) … by default [repeat=1]
#cartesian product, equivalent to a nested for-loop

p = product('abcd')
for i in p :
    print(i)
'''
= RESTART: F:\python\python_programs\5competetive programming\2itertools modul\5.product demo.py
('a',)
('b',)
('c',)
('d',)
>>>
because by default repeatation is 1
'''

p = product('abcd',repeat=2)
for i in p :
    print(i)
'''
('a', 'a')
('a', 'b')
('a', 'c')
('a', 'd')
('b', 'a')
('b', 'b')
('b', 'c')
('b', 'd')
('c', 'a')
('c', 'b')
('c', 'c')
('c', 'd')
('d', 'a')
('d', 'b')
('d', 'c')
('d', 'd')
'''
    
