# find maximum ways to give change for given amount from given set of coins

def getMaxWays(coins,m,n):
    #create array of 1D to store max ways for sum 0 to n
    ways = [0]*(n+1)

    #initially max ways for sum 0 is 1
    ways[0] = 1

    #for each coin 
    for i in range(m):#i will be current coins index
        
        #find ways from sum current coin to sum n
        for j in range(coins[i],n+1):

            ways[j] = ways[j] + ways[j-coins[i]]

    return ways[n]      
    

m = int(input('Enter number of coins'))
coins = [int(i) for i in input('enter set of coins').split()]
n = int(input('Enter amount to pay'))
print(getMaxWays(coins,m,n))
'''
= RESTART: C:/Users/DELL/AppData/Local/Programs/Python/Python37/1.find max ways.py
Enter number of coins3
enter set of coins1 2 5
Enter amount to pay12
13
>>> 
= RESTART: C:/Users/DELL/AppData/Local/Programs/Python/Python37/1.find max ways.py
Enter number of coins3
enter set of coins1 2 3
Enter amount to pay4
4
>>> 
'''
