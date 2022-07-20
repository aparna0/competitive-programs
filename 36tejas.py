from collections import Counter
n = int(input())
l = []
for i in range(n):
    x = input()
    l.append(x)
c = 0
for i in range(n):
    j=i+1;
    while(j < n):
        s = l[i]+l[j]
        d = Counter(s)
        if(len(d) == 10):
            c += 1
        j += 1
print(c)
