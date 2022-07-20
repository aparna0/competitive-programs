#from given set of change coint{} of size m, find minimum coins required to pay amount n

import sys

def getMinCoins(coins,m,n):

    #create array of 1D to store minimum count of coins for sum 0 to n and initialize with max value
    table = [sys.maxsize] * (n+1)

    #for sum 0, 0 coins required therefore assign
    table[0] = 0

    #for each sum from1 to n
    for i in range(1,n+1):

        #for each coins -> it will be a index of current coin
        for j in range(m):

            #if amount is less than current coin create temperory i.e sub result
            if(coins[j] <= i):
                subRes = table[i - coins[j]]

                #if sub result is less that previous coint for that sum thn replace count of coins
                if( (subRes != sys.maxsize) and (subRes+1 < table[i]) ):
                    table[i] = subRes + 1
    
    if(table[n] == sys.maxsize) : return -1
    else: return table[n]


m = int(input('Enter number of coins'))
coins = [int(i) for i in input('enter set of coins').split()]
n = int(input('Enter amount to pay'))
print(getMinCoins(coins,m,n))
