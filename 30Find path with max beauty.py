from collections import Counter
n = int(input())
m = int(input())
a = input()
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
#print(x)
#print(y)
fcnt = 0
visited = []

d = {}
for i in range(m):
    if(x[i] not in d):
        d[x[i]] = [y[i]]
    else:
        d[x[i]].append(y[i])
#print(d)

def rec(cn, cs, cv):
    #print("cur node ",cn,"cnt ",cv)
    global fcnt
    if(fcnt == -1):
        return -1
    elif(cn in cv):
        #print(cv,"visited")
        fcnt = -1
        return -1
    else:
        cv.append(cn)
        v = cv
        if(cn in d):
            for j in d[cn]:
                cs += a[j-1]
                c = Counter(cs)
                x = c.most_common(1)
                #print(x,len(x))
                if(len(x)>0):
                    #print(x[0][1])
                    if(x[0][1] > fcnt):
                        fcnt = x[0][1]
                if(rec(j, cs, cv) == -1):
                    return -1
                #print(fcnt)
                if(len(cv) > 1):
                    cv.pop()
        
        
for i in x:
    s = a[i-1]
    cv = []
    rec(i, s, cv)
    #countRec(i,1)
 

print(fcnt)
