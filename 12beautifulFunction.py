#problem statement
'''
let's define a beautiful function f(x) in suh a way, ass 1 to the vallue of x,
if result constains trailing zeros then remove them

for example :
    f(11) = 12
    f(19) = 2(20->2)
    f(99) = 1(100->10->1)

find total number of count that are reachable from given number N

for example,
    102 is reachable from 1099 as f(f(1099)) -> f(101) -> 102

sample input                          output
1                                    9 {1,2,3,4,5,6,7,8,9 are reachable from 1}

'''
#find the f(x) of given number recursively util you get number which is allready calculatd
#in our code use list F to store values of each f(x) to check where newly calulated values is allready
#present or not , if yes then stop calculating further f(x)
#because if resulting value is present then further sequence will be same which all these
#we all ready got3
#for example
#   N=2 -> 3,4,5,6,7,8,9,1,2 and stop here because after this we will get same sequence from 3(f(x)->3 and so on)
#   N=12 -> 13,14,15,16,17,18,19,2,3,4,5,6,7,8,9,1
#print count of list f

N = int(input())
F = []                              #to store values of f(x)
cnt = 0
Fx  = N + 1
while(Fx not in F):
    Fx = int( (str(Fx)).rstrip('0') )
    F.append(Fx)
    cnt += 1
    Fx = Fx + 1
print(F,cnt)
