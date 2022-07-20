
s = []
for i in range(3):
    s.append(input())

small_s = None
for i in s:
    if(small_s == None):
        small_s = i
    else:
        if(len(i) < len(small_s)):
            small_s = i


cnt = 0
for i in range(3):
    if(s[i] != small_s):
        while(s[i] != small_s and len(s[i]) > len(small_s)):
            cs = s[i]
            s[i] = cs[1:]
            cnt += 1


if(s[0]==s[1] and s[0]==s[2] and s[1]==s[2]):
    print(cnt)
else:
    while(s[0]!=s[1] or s[0]!=s[2] or s[1]!=s[2]):
        s[0] = s[0][1:]
        s[1] = s[1][1:]
        s[2] = s[2][1:]
        cnt += 3
    print(cnt)
