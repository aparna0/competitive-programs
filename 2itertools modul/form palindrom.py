from itertools import permutations as perm

def isPal(lst):
    i=0
    j=len(lst)-1
    while(i<=j):
        if(lst[i] != lst[j]) :
            return False
        i += 1
        j -= 1
    return True;
        
lst = [int(i) for i in input()]
per = perm(lst,len(lst))
f = 0
out = -1
ol = []
for p in per:
    if(isPal(p)):
        ol.append(''.join(str(e) for e in p))
if(len(ol)) : out = max(ol)
print(out)
