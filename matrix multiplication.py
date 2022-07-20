m = int(input())
m1 = []
for i in range(m):
    m1.append([int(j) for j in input().split(',')])
    
n = int(input())
m2 = []
for i in range(n):
    m2.append([int(j) for j in input().split(',')])

mul = [[sum(a*b for a,b in zip(m1_r, m2_c))
        for m2_c in zip(*m2)]
           for m1_r in m1]

out = []
r=0
c=0
f = 1
cnt = 0
while(r<len(mul) and c<len(mul[0])):
    cnt += 1
    out.append(mul[r][c])
    r += 1
    if(r==m and c<m):
        r = 0
        if(mul[r][c] in out):
            c += 1
            f = 0
    if(cnt == 2):
        cnt = 0
        if(f):
            c += 1

out2 = []
r=0
c=0
f = 1
cnt = 0
while(c<len(mul) and r<len(mul[0])):
    cnt += 1
    out2.append(mul[r][c])
    mul[r][c] = -1
    c += 1
    if(c==m and r<m):
        c = 0
        if(mul[r][c] == -1):
            r += 1
            f = 0
            out2.append("ok")
    if(cnt == 2):
        cnt = 0
        if(f):
            r += 1
res = ""
res += ','.join(str(e) for e in (out+out2))
print(res)

