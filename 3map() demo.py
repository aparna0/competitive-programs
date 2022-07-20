'''
The Map function.

This function is a sneaky little shortcut that allows us to implement a simple function on a list of values in a very Unconventional Manner. The following example will give a simple application of this functionality.
The function takes as parameters the function name and the name of the list the function needs to be applied upon.
'''

#problem statement
'''
take list of elements from user and print list of quare of each element
'''
ip_list = list(map(int,input('enter numbers as many as you wants ').split()))
'''
1st split() function split the entered number by space and returns iterators as list of strings to map finction.
map function maps the each elements of iterator to int() function which is defined in Int class.
int() function convert passed element to int and finally map function returns map object, so we need to type cast it into list 
'''
print(ip_list)

def square(no):
    return no*no

op_list =list(map(square,ip_list))

print('output list ',op_list)
