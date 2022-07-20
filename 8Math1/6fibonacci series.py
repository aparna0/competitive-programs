#1) using simpe method
def simpleFibo(no):
    p = 0
    q = 1
    for i in range(2,no+1):
        n = p + q
        p = q
        q = n
    return n

print(simpleFibo(10))

#2) using recursion function
def recFibo(no):
    if no == 0: return 0
    elif no == 1: return 1
    else :
        return (recFibo(no-1) + recFibo(no-2))
print(recFibo(10))
'''
disadvanges :
    as it consumes lot of time because it makes redundant calls to function for same number for another number
    for example to calculate fibo of 5th call involve calls as below, f(1), f(0) are called many times like for f(3,4,5) and
    similary lower fibo get called for every time of function call of their higher number. 
                                                    f(5)
                                                    /   \
                                                f(3)     f(4)
                                                /   \    /    \
                                            f(1)   f(2)  f(2)   f(3)
                                                 /  \    / \     / \
                                             f(0)f(1)  f(0)f(1) f(1)f(2)
                                                                     /  \
                                                                  f(0)  f(1)

    # solution:
        solution to this problem is dynamic programming,
            that is instaed of calling recusively we can store fibonacci as they get computed and can be directly used for
            next number fibonacci                                                
'''

#3) using dynamic programming
def dynamicFibo(no):
    f=[0,1]
    for i in range(2,no+1):
        f.append(f[i-2] + f[i-1])
    return f[no]
print(dynamicFibo(10))


#4) Golden ratio:
'''
Golden ratio = (1 + sqrt {5})/2 =1.6180339887...
nth fibonacci number = round(n-1th Fibonacci number X golden ratio)
                  fn = round(fn-1 * Golden ratio)
'''

# Python3 code to find n-th Fibonacci number
 
# Approximate value of golden ratio
PHI = 1.6180339
 
# Fibonacci numbers upto n = 5
f = [ 0, 1, 1, 2, 3, 5 ]
 
# Function to find nth
# Fibonacci number
def fib ( n ):
 
    # Fibonacci numbers for n < 6
    if n < 6:
        return f[n]
 
    # Else start counting from
    # 5th term
    t = 5
    fn = 5
     
    while t < n:
        fn = round(fn * PHI)
        t+=1
     
    return fn
 
# driver code
n = 10
print(n, "th Fibonacci Number =", fib(n))
 
# This code is contributed by "Sharad_Bhardwaj".
