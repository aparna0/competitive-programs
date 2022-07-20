from itertools import permutations 
import sys
n = input("enter number to find next graeter number from that digits itself")
n2 = [int(i) for i in n]
#print(n2)

large = 0
per = permutations(n2)
for p in per:
    s = ""
    for i in p:
        s += str(i)
    s = int(s)
    #print(s)
    
    if(s > large and s != int(n)):
        large = s
        break

m = sys.maxsize
print(large,m)
