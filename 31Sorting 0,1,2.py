#sort an array of 0's, 1's and 2's without any extra space(array except input array) or sorting algo
from collections import Counter
a = [1,2,0,0,1,0]
zero = ""
one  = ""
two = ""
for i in a:
    if(i == 0):
        zero += str(i) + " "
    elif(i == 1):
        one += str(i) + " "
    else:
        two += str(i) + " "
#print(zero+one+two)
a = [int(i) for i in (zero+one+two).split()]
print(a)

a = Counter(a)
print(a)
print(int("1 2"))

