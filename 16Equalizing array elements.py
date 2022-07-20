n = int(input("size of array"))
print("enter ",n," elements")

#a = [int(i) for i in input().split()]
a = []
a2 = []
for i in range(n):
    a.append(int(input()))
    a2.append(a[i])
    
r = int(input("Enter threshold value")) # no of elements should be same
d = int(input("enter divisor"))
#print(n)
#print(a2)
#print(r)
#print(d)

div = {}
f = 0

while(not f):
    for i in range(n):
        if(a2[i] not in div):
            #print(ok)
            l = [1,i]
            div[a2[i]] = l
        else:
            div[a2[i]][0] += 1
            (div[a2[i]]).append(i)
            
        if(div[a2[i]][0] == r):
            f = a2[i]
            break
    if(not f):
        for i in range(n):
            a2[i] = a2[i] // d

#print(div)
#print("f ",f)
cnt = 0
#print(len(div[f]))
for i in range(1,len(div[f])):
    #print(i)
    #print(div[f][i])
    while(a[div[f][i]]!= f):
        #print(a[div[f][i]])
        cnt += 1
        a[div[f][i]] = a[div[f][i]] // d
    

print("output ", cnt)
            


