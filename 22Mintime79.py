n = int(input())
m = int(input())
g = []
for i in range(n):
    g.append(int(input()))

a = {}
for i in range(n):
    t = int(input())
    k = g[i]
    if(g[i]):
        
        if(k not in a):
            
            a[k] = [t]
        else:
            (a[k]).append(t)

            
#print(sorted(a[i]))            
for i,j in a.items():
    (a[i]).sort()
'''        
for i,j in a.items():
    print(i,j)
'''
ac = 0
ad = 0
cnt = 0

if((3 in a)):
    while( len(a[3])>0 and (a[3][0]/2) <
          (a[1][0]+a[2][0])):
        
        ac += 1
        ad += 1
        cnt += a[3][0]
        l = a[3]
        del l[0]
        a[3] = l
       
        
if(1 in a):
    while(len(a[1]) > 0 and ac < m):
        
        ac += 1
        cnt += a[1][0]
        l = a[1]
        del l[0]
        a[1] = l
        

if(2 in a):
    while( len(a[2]) > 0 and ad < m):
        
        ad += 1
        cnt += a[2][0]
        l = a[2]
        del l[0]
        a[2] = l
        
if(ac < m or ad < m):
    print(-1)
else:
    print(cnt)
