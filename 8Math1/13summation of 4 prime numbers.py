'''
from itertools import combinations_with_replacement as cwr

#method1 using inbuild function
def findPrimes(n):
    p = [1] * (n+1)
    p[0] = 0
    p[1] = 0

    i = 2
    while( (i*i) < n ):
        if(p[i]):
            j = i * i
            while(j <= n):
                p[j] = 0
                j = j + i
        i += 1

    return [i for i in range(2,n+1) if p[i]]

def findSet(n):
    primes = findPrimes(n)
    #print(primes)
    com = cwr(primes, 4)
    for i in com:
        if(sum(i) == n):
            print(i)
            return 
    
    print(-1)

no = int(input())
findSet(no)
'''

'''
#method2 uing Goldbach's Conjecture
def isPrime(no):
    i = 2
    while((i*i)<=no):
        if(no%i == 0):
            return False
        i += 1
    return True

def findSet(x):
    for i in range(2,(x//2)+1):
        if(isPrime(i) and isPrime(x-i)):
            return [i,(x-i)]

def printSet(no):
    sum_set = []
    if(no <= 7):
        return -1
    
    else:
        if(no & 1):     #if no is odd
            sum_set.extend([2,3])
            sum_set.extend(findSet(no-5))

        else :          #if no is even
            sum_set.extend([2,2])
            sum_set.extend(findSet(no-4))

        return sum_set       
            
no = int(input())
print(printSet(no))
'''



