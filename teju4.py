input1 = int(input())
input2 = [int(i) for i in input().split()]
input2.sort()
x = input2[-1]+1
i=0
while(i<input1):
    j=i+1
    while(j<input1 and input2[j]==input2[i]):
        input2[j] = x
        x += 1
        j = j+1
    i += 1
print(sum(input2))
