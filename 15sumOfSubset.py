

def sumOfSubset(s,k,r,w,m):
    global x
    x[k] = 1
    if((s+w[k])==m):
        print(x)
        x = [0]*6   
        return 

    elif((s+w[k]+w[k+1]) <= m):
        
        sumOfSubset(s+w[k],k+1,r-w[k],w,m)
    if((s+r-w[k])>=m and (s+w[k+1])<=m):
        x[k] = 0
        sumOfSubset(s,k+1,r-w[k],w,m)

x = [0]*6      
sumOfSubset(0,0,73,[5,10,12,13,15,18],30)

