def binary_exponential1(x,y):
    res = 1
    while(y>0):
        if(y&1):#if odd
            res = res * x
        x = x * x
        y = y>>1
    return res

#using recursion
def binary_exponential2(x,y):
    if(y==0): return 1
    elif(y==1): return x
    else:
        res = binary_exponential2(x,(y>>1))
        res = res * res
        if(y&1):
            res = res * x
        return res
    
x,y = [int(i) for i in input('Enter x and y ').split()]
print(x,y)
print('x^y ',binary_exponential1(x,y))
print('x^y ',binary_exponential2(x,y))

