'''
operator.mul(a, b)
operator.__mul__(a, b)
Return a * b, for a and b numbers.
'''

import operator as op

print(op.mul(10,20),op.__mul__(10,-20))                 #200 -200

#print(op.mul('abc','efg'))                             #TypeError: can't multiply sequence by non-int of type 'str'

class Demo:
    def __init__(self,no = 0):
        self.no = no
  
d1 = Demo(10)
d2 = Demo()

#print(op.mul(d1,d2))                                   #TypeError: unsupported operand type(s) for *: 'Demo' and 'Demo'

class Demo:
    def __init__(self,no = 1):
        self.no = no
    def __mul__(self,other):
        return (self.no * other.no)
  
d1 = Demo(10)
d2 = Demo()
d3 = Demo(50)

print(d1*d2)                                            #10
print(op.mul(d1,d3))                                    #500

