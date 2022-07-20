'''
operator.itemgetter(*items)
Return a callable object that fetches item from its operand using the operand’s __getitem__() method. If multiple items are specified, returns a tuple of lookup values. For example:

After f = itemgetter(2), the call f(r) returns r[2].

After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3]).
'''

import operator as op

print(op.itemgetter(1)('ancd'))                     #n

#print(op.itemgetter(1,3,5)(1,2,3,4,5,6))           #TypeError: itemgetter expected 1 arguments, got 6

print(op.itemgetter(1,3,5)([1,2,3,4,5,6]))          #(2,4,6)

s = 'aparna'

print(op.itemgetter(slice(1,-1))(s))                #parna
