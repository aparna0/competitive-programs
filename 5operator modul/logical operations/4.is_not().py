#operator.is_not(a, b)
#Return a is not b. Tests object identity.

import operator as op

print(op.is_not(1,1),op.is_not(1,2),op.is_not(1,1.0))                       #false true true
print(op.is_not(1,'1'),('a' is not 'a'))                                    #True false


class Demo:
    def __init__(self,no=None):
        self.no = no

d1 = Demo()
d2 = Demo(1)
d3 = d1

print(op.is_not(d1,d2),op.is_not(d1,d3))                                  #true false

