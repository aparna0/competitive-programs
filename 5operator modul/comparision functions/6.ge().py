
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

#1)operator.gt(a,b)/ >= / operator.__gt__(a,b)

print(op.ge(1,1),op.gt(2,1))                                        #true true

#print(op.lt(1,None))                                               #TypeError: '<' not supported between  'int' and 'NoneType'

print(op.ge(1.5,1),op.ge(1.5,1.5),op.ge(1.9,2.5))                   #true true false

print(op.ge('abc','d'),op.ge('abc','abc'))                          #false true

#print(op.ge(1,'a'))                                                #TypeError: '<' not supported between  'int' and 'str'

#print(op.ge(d1,d2),op.ge(d1,d3),op.ge(d1,d4))                  #TypeError: '<' not supported between instances of 'Demo' and 'Demo'
'''
lt() not able to perform on different datatypes but d1&d2 are of same type again it producing typeerror
solution , perform '>=' operator overloading
'''

class Demo():
    def __init__(self,no,msg):
        self.no = no
        self.msg = msg
    
    def display(self):
        print('no : ',self.no,'\t msg : ',self.msg)

    # >= overloaded method
    def __ge__(self,other):
        if(self.no >= other.no and self.msg >= other.msg):
            return True
        else:
            return False

    def __str__(self):
        return str(self.no)+self.msg
    
    
d1 = Demo(1,'efg')
d2 = Demo(2,'abc')
d3 = Demo(1,'axz')
d4 = Demo(0,'ebcd')
#after overloading eq() method in Demo class
print('ok',op.ge(d1,d2),op.ge(d1,d3),op.ge(d1,d4))               #false true true(as it calls ge() method of Demo class).
print(d1>=d2, d1>=d3, d1>=d4)                                    #false true true(as it calls ge() method of Demo class).


    


