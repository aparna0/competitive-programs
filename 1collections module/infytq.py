m = int(input())
p = int(input())

m1 = []
m2 = []
#m3 = []

for i in range(m):
    m1.append([int(i) for i in input().split()])

for i in range(p):
    m2.append([int(i) for i in input().split()])

n = len(m1[0])
q = len(m2[0])

om = []
print(m,n)
print(p,q)
        
'''
print(n,q)
for i in m1:
    print(i)
for i in m2:
    print(i)
for i in om:
    print(i)

for r in range(m):
    for c in range(n):
        print(r,c)
'''
for r in range(m):
    temp = []
    for c in range(n):
        
        #print(om[r][c],end=' ')
        print(r,c)
        if( (r==0 and c==0) or (r==(m-1) and c==(n-1)) ):
            if(r<=(p-1) and c<=(q-1)):
               temp.append(m1[r][c]*m2[r][c])
            else :
                temp.append(-1)
        else:
            product = []
            for i in range(p):
                for j in range(q):
                    product.append(m1[r][c]*m2[i][j])
            print(product)
    om.append(temp)
            
print('\n\n')
print(om)
'''
for r in range(m):
    for c in range(n):
        print(om[r][c],end= ' ')
    print()
'''
'''

            
            try:
                print(r,c)
                om[r][c] = m1[r][c]*m2[r][c]
            except:
                om[r][c] = -1
        else :
            om[r][c] = m1[r][c]
'''
