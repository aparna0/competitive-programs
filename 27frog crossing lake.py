n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

i = 0
jmp = 0
mjmp = a[0]
while(i < n):
    mjmp = a[i]
    jmp += 1 
    #f = 0
    j = i+1
    while(j <= a[i] and j < n):
        if(a[j] > mjmp):
            mjmp = a[j]
            f = 1
        j += 1
    i += mjmp
print(jmp)
'''
i = 1
j = 0
k = a[0]
while( i < n):
    j += 1
    k -= 1
    if(a[i] > k and k >= 0):
        i += a[i]
    else :
        i += 1
print(j)
'''

'''
i = 0
j = 0
while(i < n):
    j += 1
    i += a[i]

print(j)
'''

