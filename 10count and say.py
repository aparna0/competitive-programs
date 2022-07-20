#problem statement
'''
    count and say sequence of integers with firs five terms as following
    1. 1
    2. 11
    3. 21
    4. 1211
    5. 112121
    and so on

    1 is read as one1 or 11
    11 is read as two 1 or 21
    21 is read as one 2 one one 1 or 1211
    and so on

    for given N find the sequence

    sampleinput                                     output
        4                                            1211
'''

def countAndSay(no):
    res = '1'
    for n in range(2,no+1):
        i = 0
        temp = ''
        while(i < len(res)):
            cnt = 1
            j = i+1
            while(j < len(res) and res[j]==res[i]):
                cnt += 1
                j += 1
            temp += str(cnt)+ res[i]
            i = j
        #print(temp)
        res = temp
    return res

no = int(input())
print(countAndSay(no))
