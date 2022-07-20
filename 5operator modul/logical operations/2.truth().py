'''
operator.truth(obj)
Return True if obj is true, and False otherwise. This is equivalent to using the bool constructor.
'''

import operator as op

print(op.truth(False))                      #false

print(op.truth(True))                       #True

print(op.truth(None))                       #false

print(op.truth('abc'))                      #true

print(op.truth(''))                         #FALSE

class Demo:
    def __init__(self,no=None):
        self.no = no

d1 = Demo()
d2 = Demo(1)

print(op.truth(d1))                         #true
print(op.truth(d2))                         #true


