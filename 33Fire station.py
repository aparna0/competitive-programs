'''
there are 'n' stations between two places A and B.
find numner of ways in which a train can be made to stop at 's' of intermediate stations
so that no two stopping stations are conseutive
'''

def fact(no):
    res = 1
    for i in range(2,no+1):
        res = res * i
    #print(res)
    return res

def nCf(n,r):
    return int(fact(n) / (fact(r) * fact(n-r)))

n = int(input())        #number of stations
s = int(input())        #number of stops

n = n-s+1               #because  no two stopping stations are conseutive

print(nCf(n,s))         # Using Combination formula(where we have to select s stations from n)
