from itertools import combinations_with_replacement
n = int(input())
s = input()
l = ['a','b','c','d','e']
com = combinations_with_replacement(l,n)
cnt = 0
for c in com:
    x = ''
    for i in c:
        x += i
    if(x < s):
        cnt += 1
        print(x)

print(cnt)
    
