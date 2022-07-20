from itertools import *

c = count(5)
#for i in c:
#    print(i)  it goes on infinite from 5 to n i.e 5,6,7,8,9,10,11,...
c = count(5,2)   # 2nd parameter specifies increament


c = cycle('abcd')
#for i in c:
    #print(i)   it goes on infinite a,b,c,d,a,b,c,d,a,b,c,d,...
   
r = repeat('abcd',5)
for i in r: 
    print(i)
'''
abcd
abcd
abcd
abcd
abcd
'''
