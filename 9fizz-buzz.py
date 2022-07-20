# problem statement :
'''
from 1 to 100
    no is divisible by 3 the print 'fizz'
    no is divisible by 5 the print 'buzz'
    else print no itself
'''
'''
#1)
for i in range(1,101):
    flag = True
    if(i%3 == 0) :
        print('fizz')
        flag = False
    if(i%5 == 0) :
        print('buzz')
        flag = False
    if(flag) : print(i)

#2)reducing print statements
for i in range(1,101):
    out = ''
    if(i%3 == 0):
        out += 'fizz '
    if(i%5 == 0):
        out += 'buzz'
    if(out == ''):
        print(i)
    else:
        print(out)
'''
#3) % is expensive operator ,so reduce complexity
cnt3 = 0
cnt5 = 0
for i in range(1,101):
    out = ''
    cnt3 += 1
    cnt5 += 1
    if(cnt3 == 3):
        out += 'fizz '
        cnt3 = 0
    if(cnt5 == 5):
        out += 'buzz'
        cnt5 = 0
    if(out == ''):
        print(i)
    else:
        print(out)

#4)
cnt3 = 0
cnt5 = 0
for i in range(1,101):
    cnt3 += 1
    cnt5 += 1
    if(cnt3 == 3):
        print('fizz')
        cnt3 = 0
    if(cnt5 == 5):
        print('buzz')
        cnt5 = 0
    if(cnt3 and cnt5 ):
        print(i)

        
    
