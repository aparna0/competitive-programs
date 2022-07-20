n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
A = int(input())
B = int(input())

a.sort()
print(a)

neg = 0
cnt = 0
while(neg < n):
    f = 1
   
    for i in range(0,n-1):
        if(a[i] < 0):
            neg += 1
        else:
            if(f and a[i] > A):
                a[i] -= A
                cnt += 1
                f = 0
                #print(i,cnt)
            else:
                a[i] -= B
        
    if(f):
        a[n-1] -= A
        f = 0
        cnt += 1
        #print(n-1,cnt)
    else:
        a[n-1] -= B
    if(a[n-1] < 0):
        neg += 1
    #print(a,neg)
print(cnt)   

    
        
#print(a)

    
