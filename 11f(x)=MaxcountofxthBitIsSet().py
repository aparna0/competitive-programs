#prblem statement
'''
you are given with array A having N integers and a function f(x), where
f(x) = count of numbers in array for whichthe xth bit is set.
find out maximum value of f(x), where 0<=x<=31.

input format
    1st line contains integer denoting N
    2nd line consists of N space seperated integers denoting array A

output format
    print required otput

sample input                               output
    4                                        2
    1 2 3 4

explanation
f(0) = 2{1,3}
f(1) = 2{2,3}
f(2) = 2{4}
f(x) = 0:3<=x<=31
'''
import re
def findF(no):

    #conerting n to binary representation
    
    binary = {}         #to hold binary representation of each no

    #method1
    for n in no:
        rList = []
        d = n
        while(d > 1):
            r = d % 2
            d = d // 2
            rList.append(r)
        rList.append(1)
        binary[n] = rList
    print(binary)
    '''
    #method2 , using inbuild function
    for n in a:
        b = re.findall('\d',str(bin(n)))
        binary[n] = b
    '''   
    #finding f(x)
    fDict = {}
    for n in no:
        for i in range(len(binary[n])):
            if(binary[n][i]):
                fDict[i] = fDict.get(i,0) + 1
            
    return max(fDict.values())
            
N = int(input())
a = [int(i) for i in input().split()]
#print(N)
#print(a)
print(findF(a))
