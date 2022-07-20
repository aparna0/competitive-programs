#recursion
def findExponential(x,y):
    if y == 0: return 1
    elif y == 1: return x
    else:
        res = findExponential(x,(y>>1))
        res = res * res
        if(y&1):
            res = res * x
        return res

n = findExponential(10,10)
print(n)



             
