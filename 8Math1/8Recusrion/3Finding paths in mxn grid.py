def findPath(n,m):
    if(n==1 or m==1): return 1
    else : return (findPath(n,m-1)+findPath(n-1,m))


print(findPath(1,3))
print(findPath(2,2))
print(findPath(3,3))
    
