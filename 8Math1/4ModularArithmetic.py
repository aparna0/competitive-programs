#problem statement (x^y)%m

#Modular proerties :-
'''
    1)(x+y)%m = [(x%m) + (y%m)] % m
    2)(x*y)%m = [(x%m) * (y%m)] % m
    3)(x-y)%m = [(x%m) - (y%m) + m] % m
    4)(x/y)%m = [(x%m) * ((y^-1)%m)] % m
'''
#here we can combine binary exponential and modular property of *
def exponentialAndModul(x,y,m):
    res = 1
    x = x%m
    
    if(x==0):
        return 0
    
    while(y>0):
        if(y&1):
            res = (res*x)%m
            
        x = (x * x)%m
        y = y>>1
        
    return res

print(exponentialAndModul(10,10,7))
print((10**10)%7)
