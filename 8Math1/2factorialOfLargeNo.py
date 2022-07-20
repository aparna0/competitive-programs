
def factorial(n):
    res = [1]
    
    for n in range(1,no+1):
        carry = 0
        for i in range(len(res)-1,-1,-1):
            x = n * res[i] + carry
            res[i] = x%10
            carry = x//10
        if (carry):
            res.insert(0,carry)

    return res
            
no = int(input('Enter number to find factorial of large number'))
r = factorial(no)
print(r)
for i in r:
    print(i,end='')


