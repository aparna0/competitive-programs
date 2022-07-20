#using recusrion
def catalanNumber(no):
    if no == 0:
        return 1
    s = 0
    for i in range(no):
        s = s + (catalanNumber(i)*catalanNumber(no-i-1))
    return s

for i in range(0,10):
    print(catalanNumber(i),end=' ')
    
#this recursion requires exponential time

#dynamic programming
def catalanNumber(no):
    c = [1]
    for n in range(1,no):
        s = 0
        for i in range(0,n):
            s = s + (c[i]*c[n-i-1])
        c.append(s)
    return c
print(catalanNumber(10))



#
# A dynamic programming based function to find nth
# Catalan number
 
 
def catalan(n):
    if (n == 0 or n == 1):
        return 1
 
    # Table to store results of subproblems
    catalan =[0]*(n+1)
 
    # Initialize first two values in table
    catalan[0] = 1
    catalan[1] = 1
 
    # Fill entries in catalan[]
    # using recursive formula
    for i in range(2, n + 1):
        for j in range(i):
            catalan[i] += catalan[j]* catalan[i-j-1]
     # Return last entry
     
    return catalan[n]
 
 
# Driver code
for i in range(10):
    print(catalan(i), end=" ")
# This code is contributed by Ediga_manisha






