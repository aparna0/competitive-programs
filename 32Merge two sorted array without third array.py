a1 = [2,3,8,13]
a2 = [1,5,9,10,15,20]

p1 = 0
for p2 in range(len(a2)):
    while(p1 < len(a1)-1 and a1[p1]<a2[p2]):
        p1 += 1
    a1.insert(p1,a2[p2])
    #print(a1)
print(a1)
#print(a2)
