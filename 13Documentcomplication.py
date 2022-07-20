no = int(input())
a = [int(i) for i in input().split()]
cnt = 0
grp = []
i = 0
while(i < len(a)):
    if(a[i] in grp):
        cnt += 1
        grp.clear()
    else:
        grp.append(a[i])
    i += 1

print(cnt)
