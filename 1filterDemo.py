'''
The filter() function returns an iterator were the items are filtered
through a function to test if the item is accepted or not.

The syntax of filter() method is:
*filter(function, iterable)

filter() Parameters
filter() method takes two parameters:
function - function that tests if elements of an iterable return true or false
If None, the function defaults to Identity function - which returns false if any elements are false
iterable - iterable which is to be filtered, could be sets, lists, tuples, or containers of any iterators
'''
def test(l) :
    return 1 if l in b else 0
a = [5,5,6,7,7,7]
b = set(a)
for i in filter(test,a):
    print(i,end=' ')
    
print('\n')

for i in filter(test,[1,2]):
    print(i,end=' ')            #nothing will be printed
    

