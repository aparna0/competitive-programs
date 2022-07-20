
class Demo():
    def __init__(self,no,msg):
        self.no = no
        self.msg = msg
    
    def display(self):
        print('no : ',self.no,'\t msg : ',self.msg)

    def __str__(self):
        return str(self.no)+self.msg
    
    
d1 = Demo(1,'efg')
d2 = Demo(2,'abc')
d3 = Demo(1,'efg')
d4 = d1
print(d1)                                                           #1efg


#The object comparison functions are useful for all objects, and are named after the rich comparison operators they support:

import operator as op

#print(operator.eq(1,2))                        NameError: name 'operator' is not defined because we used alias for operator as op


#1)operator.eq(a,b)/ == / operator.__eq__(a,b)
print(op.eq(1,1),op.eq(1,2),op.eq(1,None))                          #true false false
print(op.eq(1.5,1),op.eq(1.5,1.5),op.eq(1.9,2.5))                   #false true false
print(op.eq(1,'a'),op.eq('abc','d'),op.eq('abc','abc'))             #false false true
print(op.eq(d1,d2),op.eq(d1,d3),op.eq(d1,d4))                       #false false true
'''
even d1 and d3 have same, it returning as false operator.eq() checks with reference therefore
for d1 and d4 it returned as a true because both references pointing to same refernce object(memory location)
problem , so how to compare objects with values that they hold
solution, operator overload, as methods defined in bove Demo class
'''

class Demo():
    def __init__(self,no,msg):
        self.no = no
        self.msg = msg
    
    def display(self):
        print('no : ',self.no,'\t msg : ',self.msg)

    # == overloaded method
    def __eq__(self,other):
        if(self.no == other.no and self.msg == other.msg):
            return True
        else:
            return False

    def __str__(self):
        return str(self.no)+self.msg
    
    
d1 = Demo(1,'efg')
d2 = Demo(2,'abc')
d3 = Demo(1,'efg')
d4 = d1
#after overloading eq() method in Demo class
print('ok',op.eq(d1,d2),op.eq(d1,d3),op.eq(d1,d4))                  #False True True (as it calls eq() method of Demo class).
print(d1==d2, d1==d3, d1==d4)                                       #fasle true true (as it calls eq() method of Demo class).


    


