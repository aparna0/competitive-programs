'''
M x N matrix
0 -> empty grid
1 -> grid where person standing
2 -> grid with fire( if perticular grid have fire then its all adjecent grids catche fire)
promle statement -> find minimum number of safe moves to get person out of matrix.
                    if not possible then print -1.

---------------------------------------------Solution (using backtracking)---------------------------------------------------

 (input M*N matrix)     recursion function :-                                             (Recursion try)
     0 1 2 3                                                                              getMin(2,1,0) 
     _ _ _ _            if(person on edge grid) : return count                  {(2,0),(2,2),(1,1),(3,1)} <---possible moves       
  0 |0 0 0 0|           else if move is invalid : backtrack                                |     
  1 |2 0 0 0|           else : recursively check all 4 possibilities            getMin(2,2,1) <--valid move out of possibilities
  2 |2 1 0 0|                  from that grid and chooes minimum grid           {(2,1),(2,3),(1,2),(3,2)}
  3 |0 0 0 0|                  whoes moves is minimum among all                      /                \
                                                                                getMin(1,2,2)           getMin(2,3,2)  
                                                                        {(1,1),(1,3),(0,2),(2,2)}    {(2,2),(2,4),(1,3),(3,3)}
                                                                             /        \
                                                                    getMin(1,3,3)    getMin(0,2,3)
'''                                                                     
import sys
visited = []                            #to store index of visited grid to avoid duplication and infinite looping

def isValid(p1,p2,m):                   #to check grid index is valid and does not have fire
    #print(p1,p2)
    if( (p1>=0 and p1<len(m)) and (p2>=0 and p2 <len(m[0])) and m[p1][p2] != 2 ):
        return True
    
def isValidMove(p1, p2, m):             #check moving grid is safe or not by checking its adjecent grids
    if(m[p1][p2] == 1):
        return True
    
    if((p1,p2) not in visited and isValid(p1,p2,m) and isValid(p1,p2-1,m)
       and isValid(p1,p2+1,m)and isValid(p1-1,p2,m) and isValid(p1+1,p2,m)):
        return True

def getMinCount(p1, p2, m, cnt):
    #print(p1,p2)
    if( m[p1][p2] == 0 and (p1==0 or p1==len(m)-1 or p2==0 or p2==len(m[0])-1)):
        return cnt
    
    if( not isValidMove(p1,p2,m)):
        return sys.maxsize

    else:
        #print("branching")
        visited.append((p1,p2))
        return min(getMinCount(p1,p2-1,m,cnt+1),getMinCount(p1,p2+1,m,cnt+1),
                   getMinCount(p1-1,p2,m,cnt+1),getMinCount(p1+1,p2,m,cnt+1))
        
#m = [[0,2,0,0],[2,1,0,2],[2,0,0,0],[2,0,2,0]]
m = [[0,0,0,0],[2,0,0,0],[2,1,0,0],[2,2,0,0]]
res = getMinCount(2,1,m,0) 
if(res == sys.maxsize):
    print(-1)
else:
    print(res)

