# shifting is equivalent to multipliacation and division :-
'''
1)Right shift :
    ( M >> n ) => M / (2^n)  where n>=1

2)Left shift :
    ( M << n ) => M * (2^n)  where n>=1
'''

def mulBy2(m):
    return(m<<1)

def divBy2(m):
    return(m>>1)

def mulBy4(m):
    return(m<<2)

def divBy4(m):
    return(m>>2)

def mulBy6(m):
    return(m<<3)

def divBy6(m):
    return(m>>3)

#and so on...

print('2*2 ',mulBy2(2))
print('6/2 ',divBy2(6))

print('10*4 ',mulBy4(10))
print('10/4 ',divBy4(10))


