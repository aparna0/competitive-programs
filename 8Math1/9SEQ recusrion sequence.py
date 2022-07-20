t = int(input())
'''
def findSeq(k,b,c,n):
    if(n<k):return b[n-1]
    else:
        s = 0
        for i in range(0,k):
            s += c[i]*findSeq(k,b,c,n-i)
            print(s)
        return s
'''
def findSeq(k,b,c,no):
    
    for n in range(k,no):
        s = 0
        for i in range(k+1):
            s += c[i]*b[n-i]
        b.append(s)
    return b
    '''
    for n in range(1,no+1):
        for i in range(1,k+1):
           s += c[i]*b[n-i]
        b.append(s)
    return b[no]
    '''
        
    
        
while(t>0):
    k = int(input())
    b = [int(i) for i in input().split()]
    #b.insert(0,None) 
    c = [int(i) for i in input().split()]
    #c.insert(0,None)
    n = int(input())
    #print(k)
    #print(b)
    #print(c)
    print(findSeq(k-1,b,c,n))
    t = t - 1
