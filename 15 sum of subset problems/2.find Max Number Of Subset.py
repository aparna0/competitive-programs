#problem subset
'''
you are given with set of elements and sum, subset of set whoes sum of elements in subset is equal to given sum
print maximum number of subset is present for given sum
'''
#Using dynamic programming
def findMaxCount(w,n,s):
    #initially max ways is 0 for all
    table = [[0 for i in range(s+1)] for i in range(n+1)]

    #for sum 1 max ways is 1 with empty set
    for i in range(n+1):
        table[i][0] = 1
    
    #print(table)
    
    for i in range(1,n+1):
        for j in range(1,s+1):
            if(w[i-1] > j):
                table[i][j] = table[i-1][j]
            else:
                 table[i][j] = ( (table[i-1][j]) + (table[i-1][j-w[i-1]]))
   
    return table[n][s]
    
    

waits = [int(i) for i in input('Enter set elements').split()]
givenSum = int(input('Enter sum to find subset'))
print(findMaxCount(waits,len(waits),givenSum))
    
