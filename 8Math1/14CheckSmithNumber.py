'''
number said to be smith number for given composite number
iff sum of digits of given number and sum of digit in all prime factors is eqaul

for example,

    no = 666
    sum of digits = (6+6+6) = 18
    prime factors = (2,3,3,37)
    sum of prime factors = (2+3+3+(3+7)) = 18
    sum of digits == sum of prime factors ,
        therefore given number is smith

steps ,
1)check given number is composite or not,
    if
        "No" then print("not smith no") and stop
    else
        proceed next step 
    
2)find sum of digits of given number
3)find prime factor
4)find sum of digits prime factors
5)compare both sum
    if equal
        print(smith no)

    else
       print("not smith no") 
'''

#function to check where passed number i smith or not
def isSmithNumber(no):

    #finding sum of digits of given number 
    noDash = no   
    sumOfNo = 0
    while(noDash > 0):
        sumOfNo += (noDash % 10)
        noDash //= 10
    #print(sumOfNo)     #this sum of digits of given number

    #finding prime factor
    i = 2
    out = '' 
    while(i <= no):
        if( no%i == 0):
            while( no%i == 0):
                no /= i
                print(i)
                out += str(i)
        
        i += 1
    #print([out])   this is string whose characters are prime factors
        
    #find sum of digits prime factors    
    sumOfPrimes = 0
    for i in out:
        sumOfPrimes += int(i)
        
    #compare both sums   
    if(sumOfPrimes == sumOfNo):
        return True
    return False


def isComposite(no):
    i = 2
    #print('ok')
    while((i*i)<=no):
        if(no%i == 0):
            return True
        i += 1
    return False


#drive code
no = int(input("Enter no to check where it smith or not"))


if(isComposite(no)):
    
    if(isSmithNumber(no)):
        print(no," is smith number")
        
    else :
        print(no," is not smith number")
    
else :                                       #if number is prime then it is not smith number
    print(no," is not smith number")
    

