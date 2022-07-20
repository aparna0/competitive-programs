from itertools import permutations
no = int(input())
per = permutations(range(1,no+1))
cnt = 0
for p in per:
    f = 1
    i = 0
   
    while(i < no):
        
        if(i == 0):
            if(p[i]%2 != p[i+1]%2):
                f = 0
                break
        elif(i == no-1):
            if(p[i]%2 != p[i-1]%2):
                f = 0
                break
        else:
            if( p[i]%2 != p[i-1]%2 and p[i]%2 != p[i+1]%2):
                f = 0
                break
            
        i += 1
    if(f):
        
        cnt += 1
    

print(cnt)
print(cnt%(10**9+7))
   
