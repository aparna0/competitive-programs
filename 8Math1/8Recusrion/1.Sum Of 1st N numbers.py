# 3steps
'''
1) smallest possible input can be 1 and output for that is itself 1,
    so this can be a base condition
2) instead of calculating from 1 we can add simple n to the previous sum
3) mathematical function :
    Fn = 1            if n=1
    Fn = F(n-1)+n     if n>1
'''
def findSum(n):
    if n == 1: return 1
    else :     return (findSum(n-1)+n)

print(findSum(10))
