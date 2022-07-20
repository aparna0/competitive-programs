# find prim factorization of given number

def primFactorization(no):
    i = 2
    while(i<=no):
        if(no%i==0):
            cnt = 0
            while(no%i==0):
                #print(no)
                cnt += 1
                no /= i
            print(i,' ',cnt)
        i += 1
            
primFactorization(100)

#best case time complexity is O(sqrt(n)) but worst case time is O(n)
'''
because consider given n is 210 factors are (2*5*3*7) whose exponentialis 1
then i runs from i to n
'''
#wrong logic
'''
#optimized code
#it proven that prime factors always lies below sqrt(n)
def primFactorization2(no):
    i = 2
    while((i*i) <= no):
        if(no%i == 0):
            cnt = 0
            while(no%i == 0):
                cnt += 1
                no /= i
            print(i,' ',cnt)
        i += 1
primFactorization2(10)
'''
    
