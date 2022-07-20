'''
operator.not_(obj)
operator.__not__(obj)
Return the outcome of not obj. (Note that there is no __not__() method for object instances;
only the interpreter core defines this operation.
The result is affected by the __nonzero__() and __len__() methods.)
'''

import operator as op

print(op.not_(1.5),op.not_(0),op.not_(0.5))             #false true false
print(op.not_('a'),op.not_(''),op.not_(' '))            #false true false
print(op.not_(None))                                    #true
print(op.__not__(1))                                    #false

class Demo:
    pass

d1 = Demo()
d1.no1 = 1
d2 = Demo()

print(op.not_(d1),op.__not__(d2))                       #false false
#print(!d1)                                             #invalid syntax

class Demo:
    def __init__(self,no=None):
        self.no = no
    def __not__(self):
        if self.no == None:
            return True
        else :
            return False

d1 = Demo()
d2 = Demo(1)

print(d1.not_())                                        #calls __not__(self) method

