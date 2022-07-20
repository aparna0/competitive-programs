str1 = input()
str2 = input()
n = len(str1)
i = 0
j = n-1
while(str1[i] != str2[i]):
    i = i + 1
while(str1[j] != str2[j]):
    j = j - 1
print(str1[i:j])
