words = [ i for i in input().split()]
d = dict()
for i in words :
    d[i] = d.get(i,0)+1

l = []
for (k,c) in d.items():
    if(c > 1):
        l.append(k)
    
l.sort()
for i in l:
    print(i, end = " ")
