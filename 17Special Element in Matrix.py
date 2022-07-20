import sys
mat = []
m = int(input("Enter size of rows"))
n = int(input("Enter size of columns"))
for i in range(m):
    mat.append([int(i) for i in input().split()])

'''
for i in range(m):
    print(mat[i])
'''

l = []

for i in range(m):
    min = sys.maxsize
    max = 0
    for j in range(n):
        #
        print(i,j)
        if(min != -1):
            if(min == mat[i][j]):
                min = -1
            elif(mat[i][j] < min):
                min = mat[i][j]

        if(max != -1):
            if(max == mat[i][j]):
                max = -1
            elif(mat[i][j] > max):
                max = mat[i][j]
    if(min not in l):
        l.append(min)
    if(max not in l):
        l.append(max)

for i in range(n):
    min = sys.maxsize
    max = 0
    for j in range(m):
        #print(i,j)
        if(min != -1):
            if(min == mat[j][i]):
                min = -1
            elif(mat[j][i] < min):
                min = mat[j][i]

        if(max != -1):
            if(max == mat[j][i]):
                max = -1
            elif(mat[j][i] > max):
                max = mat[j][i]
    if(min not in l):
        l.append(min)
    if(max not in l):
        l.append(max)

print(l)
