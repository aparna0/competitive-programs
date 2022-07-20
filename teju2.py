n = int(input())
a = [int(i) for i in input().split()]
d = {}
for i in a:
    d[i] = d.get(i,0) + 1
s = None
l = None
x = None
y = None
for (k,v) in d.items():
    if(s is None or s > v):
        s = v
        x = k
    if(l is None or l < v):
        l = v
        y = k
if(x < y):
    print(x)
else:
    print(y)
