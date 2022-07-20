n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

finalr = 0
l = 1
outs = 0
while(l <= n):
    ins = 0
    i = 0
    while(i < n):
        m = max(a[i],a[l])
        print(m)
        ins += m
        i += l
    outs += ins * l
    l += 1
print(outs)
'''
for l in range(n):
   
    for r in range(l,n):
        #m = a[l]
        
        
        m = max(a[l:r+1])
        #print(m , (r - l + 1))
        res = m * (r - l + 1)
        finalr += res
        #finalr %= 1000000007 
        
       

#res %= 1000000007
#print(res)
print(finalr)
'''


'''
l = 1
ous = 0
while(k <= n):
    ins = 0
    i = 0

'''
'''
        j = l
        while(j <= r):
            if(m < a[j]):
                m = a[j]
            j += 1
'''
'''
    while(i < n):
        m = a[i]
        
        i += 
    l += 1
'''
