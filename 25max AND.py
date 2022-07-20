from itertools import combinations
n = int(input())
k = int(input())
l = []
for i in range(n):
    l.append(int(input()))
#print(l)

if(k > n):
    print(0)
elif(k == n):
    x = 1
    for i in l:
        x = x & i
    print(x)
else:
    
