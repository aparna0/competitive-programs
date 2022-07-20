def checkPrime(n):
    i = 2
    while((i*i)<n):
        if(n%i==0):
            return False
        i = i+1
    return True
no = int(input('enter no'))
if(checkPrime(no)):
    print('prime')
else :
    print('not prime')
