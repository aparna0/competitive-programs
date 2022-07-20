'''
#finding primes from 0 - n

def findPrimes1(n):
    p = [1] * (n+1)
    p[0]=p[1]=0
    i = 2
    while((i*i)<n):
        if(p[i]):
            k = 2
            j = i * k
            while(j<=n):
                p[j] = 0
                k = k + 1
                j = i * k
        i = i+1
    return p

def findPrimes2(n):
    p = [1] * (n+1)
    p[0]=p[1]=0
    i = 2
    while((i*i)<n):
        if(p[i]):
            j = i * i
            while(j<=n):
                p[j] = 0
                j = j + i
        i = i+1
    return [i for i in range(n+1) if(p[i])]
    
n = int(input('enter range'))
p = findPrimes1(n)
for i in range(n+1):
    if(p[i]):
        print(i)
p = findPrimes2(n)
print('\n',p)
'''

#find kth prime number in nth range
def find_Kth_Prime(n):  #this function will return prime nubers between 2 to n
    p = [1]*(n+1)
    p[0]=p[1]=0
    i = 2
    while(i*i < n):
        if(p[i]):
            j = i*i
            while(j<=n):
                p[j] = 0
                j = j+i
        i = i+1
    return [i for i in range(2,n+1) if(p[i])]

n,k =[int(i) for i in input('enter range and k ').split()]
print(n,k)
p = find_Kth_Prime(n)
print(p)
print('kth prime is ',p[k-1])

    

