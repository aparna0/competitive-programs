#problem statement
'''
you are given with set of elements and sum,
find set of subsets sum of elements is equal to given sum
'''

'''
def findSubSet1(w,s,n):
    left = right = 0   #initialize both pointer to 0
    cs = 0      # assume current sum is 0 because no element is added
    
    while(True):
        if(cs == s):   # if current sum and sum is eaual then return subset from index left to right
            return w[left:right]
        
        elif(cs < s):  # if current sum is less then add element of right and increment right pointer
            cs += w[right]
            if(right == n-1):
                right = 0
            else :
                right += 1

        elif(cs > s):  # if current sum is greater then remove element from left and increment left pointer
            cs -= w[left]
            if(left == n-1):
                left = 0
            else :
                left += 1

w = [int(i) for i in input('enter set elements').split()]
s = int(input('enter sum'))
print(findSubSet1(w,s,len(w)))
'''

#but this approach is not applicable for,
'''
1)if subset is not possible then it will go in infinite loop beacuse base condion never execued

2)it only print 1 subset even there are more than 1 subset,
in below example subsets are 2 that are {2,3},{5} but only printed {2,3}
= RESTART: F:/python/python_programs/5competetive programming/15 sum of subset problems/3.find subsets for given sum.py
enter set elements1 2 3 4 5
enter sum5
[2, 3]

3)it is applicble only if subset elements are must come sequencly in main set
otherwise it will enter in infinite loop
'''

#Using backracking
def findSubSet2(s,k,r,w,m):
    global x
    x[k] = 1
    
    if((s+w[k]) == m):
        ret = [ w[i] for i in range(len(x)) if(x[i])]
        print(ret)
        for i in range(k,len(x)):
            x[i] = 0
        return
    
    elif((s+w[k]+w[k+1]) <= m):
        findSubSet2(s+w[k],k+1,r-w[k],w,m)

    if((s+r-w[k]) >= m and (s+w[k+1]) <= m):
        x[k] = 0
        findSubSet2(s,k+1,r-w[k],w,m)
    
    

w = [int(i) for i in input('enter set elements').split()]
m = int(input('enter sum'))
x = [0] * len(w)
findSubSet2(0,0,sum(w),w,m)
