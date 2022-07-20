#problem statement
'''
you are given with set of elements and sum, subset of set whoes sum of elements in subset is equal to given sum
print True if there is subset is present or print false
'''

#1)Using backtracking(recursion)
'''
we start with empty subset and elements one by one
if element is less than sum and leads to sum then we include that element
otherwise exclude it and so on
'''

def checkSubsetOfSet(w,n,s):
    if(s == 0): return True
    if(n == 0): return False
    if(w[n-1] > s):
        return (checkSubsetOfSet(w,n-1,s))
    else:
        return (checkSubsetOfSet(w,n-1,s) or checkSubsetOfSet(w,n-1,s-w[n-1]))

    
waits = [int(i) for i in input('Enter set elements').split()]
givenSum = int(input('Enter sum to find subset'))
print(checkSubsetOfSet(waits,len(waits),givenSum))

'''
= RESTART: F:/python/python_programs/5competetive programming/15 sum of subset problems/1.find true or false.py
Enter set elements1 2 3
Enter sum to find subset5
True
>>> 
= RESTART: F:/python/python_programs/5competetive programming/15 sum of subset problems/1.find true or false.py
Enter set elements1 2 3
Enter sum to find subset7
False
>>> 
= RESTART: F:/python/python_programs/5competetive programming/15 sum of subset problems/1.find true or false.py
Enter set elements9 6 5 1
Enter sum to find subset11
True
>>> 
= RESTART: F:/python/python_programs/5competetive programming/15 sum of subset problems/1.find true or false.py
Enter set elements9 6 5 1
Enter sum to find subset7
True
>>> 
= RESTART: F:/python/python_programs/5competetive programming/15 sum of subset problems/1.find true or false.py
Enter set elements9 6 5 1
Enter sum to find subset8
False
>>> 
'''


#2)Using dynamic programming
def checkSubsetOfSet(w,n,s):
    #create table of 2D where rows are set elements and columns are sum from 0 to sum
    table = [[False for i in range(s+1)] for j in range(n+1)]

    #for sum 0 Subset is possible with empty set
    for i in range(n+1):
        table[i][0] = True
    '''
    for i in table:
        print(i)
    '''

    for i in range(1,n+1):
        for j in range(1,s+1):
            if(table[i-1][s] == True):  #for any element sum is True then no need to check further
                return True
            if(w[i-1]>j):
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = (table[i-1][j] or table[i-1][j-w[i-1]])

    return table[n][s]
    

waits = [int(i) for i in input('Enter set elements').split()]
givenSum = int(input('Enter sum to find subset'))
print(checkSubsetOfSet(waits,len(waits),givenSum))
'''
= RESTART: F:/python/python_programs/5competetive programming/15 sum of subset problems/1.find true or false.py
Enter set elements1 2 3
Enter sum to find subset3
True
>>> 
= RESTART: F:/python/python_programs/5competetive programming/15 sum of subset problems/1.find true or false.py
Enter set elements9 6 5 1
Enter sum to find subset8
False
>>> 
= RESTART: F:/python/python_programs/5competetive programming/15 sum of subset problems/1.find true or false.py
Enter set elements9 6 5 1 
Enter sum to find subset7
True
>>> 
'''
