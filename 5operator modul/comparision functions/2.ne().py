
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



import operator as op

#print(operator.eq(1,2))                        NameError: name 'operator' is not defined because we used alias for operator as op


#1)operator.eq(a,b)/ == / operator.__eq__(a,b)
print(op.ne(1,1),op.ne(1,2),op.ne(1,None))                          #false true true
print(op.ne(1.5,1),op.ne(1.5,1.5),op.ne(1.9,2.5))                   #true false true
print(op.ne(1,'a'),op.ne('abc','d'),op.ne('abc','abc'))             #true true false
print(op.ne(d1,d2),op.ne(d1,d3),op.ne(d1,d4))                       #true true flase
'''
even d1 and d3 have same, it returning as true operator.eq() checks with reference therefore
for d1 and d4 it returned as a false because both references pointing to same refernce object(memory location)
problem , so how to compare objects with values that they hold
solution, operator overload
'''

class Demo():
    def __init__(self,no,msg):
        self.no = no
        self.msg = msg
    
    def display(self):
        print('no : ',self.no,'\t msg : ',self.msg)

    # !=/ ne() overloaded method
    def __ne__(self,other):
        if(self.no != other.no and self.msg != other.msg):
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
print('ok',op.ne(d1,d2),op.ne(d1,d3),op.ne(d1,d4))                 #true false false (as it calls eq() method of Demo class).
print(d1!=d2, d1!=d3, d1!=d4)                                      #true false false (as it calls eq() method of Demo class).


    


