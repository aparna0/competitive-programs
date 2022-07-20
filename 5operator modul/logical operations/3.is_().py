
#operator.is_(a, b)
#Return a is b. Tests object identity.


import operator as op

print(op.is_(1,1),op.is_(1,2),op.is_(1,1.0))                      #true false false
print(op.is_(1,'1'),('a' is 'a'))                                 #false true


class Demo:
    def __init__(self,no=None):
        self.no = no

d1 = Demo()
d2 = Demo(1)
d3 = d1

print(op.is_(d1,d2),op.is_(d1,d3))                                  #false true
