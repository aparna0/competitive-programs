'''
operator.add(a, b)
operator.__add__(a, b)
Return a + b, for a and b numbers.
'''

import operator as op

print(op.add(10,20),op.__add__(10,-20))                 #30 -10

print(op.add('abc','efg'))                              #abcefg

#print(op.add('a',1))                                   #TypeError: can only concatenate str (not "int") to str

#print(op.add(1,None))                                  #TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'

class Demo:
    def __init__(self,no = 0):
        self.no = no
  
d1 = Demo(10)
d2 = Demo()

#print(op.add(d1,d2))                                   #TypeError: unsupported operand type(s) for +: 'Demo' and 'Demo'

class Demo:
    def __init__(self,no = 0):
        self.no = no
    def __add__(self,other):
        return (self.no + other.no)
  
d1 = Demo(10)
d2 = Demo()
d3 = Demo(50)

print(d1+d2)                                            #10
print(op.add(d1,d3))                                    #60

